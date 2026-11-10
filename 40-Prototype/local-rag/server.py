"""OpenAI 兼容 API 服务：把 Qdrant RAG 包成 /v1/chat/completions
Cherry Studio 等客户端添加自定义提供商指向 http://127.0.0.1:8000/v1 即可当 RAG 前端
启动: uv run python server.py
"""
import json
import time
import uuid

import ollama
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse, StreamingResponse
from pydantic import BaseModel

from main import CHAT_MODEL, COLLECTION, EMBED_MODEL, TOP_K_DEF, oc, qc

app = FastAPI(title="local-rag OpenAI API")
MODEL_NAME = "kb-rag"    # 强制RAG：总是检索+带来源回答
AUTO_MODEL = "kb-auto"   # 自动路由：检索分数达标走RAG，否则直接用qwen3自由回答
ROUTE_THRESH = 0.50      # 自动路由阈值：top1相似度低于此值视为"知识库答不了"，走直答
INSTR = (
    "你是本地知识库助手。仅根据资料回答问题，答案末尾列出用到的来源编号和文件名；"
    "资料不足以回答就直说。"
)
FREE_INSTR = "你是一名知识渊博的AI助手，用中文清晰简洁地回答。"


@app.exception_handler(Exception)
async def on_unexpected_error(request, exc):
    import traceback
    traceback.print_exc()  # 进 /tmp/kb-rag-server.log
    return JSONResponse({"error": {"message": f"server error: {exc}"}}, status_code=500)


class Msg(BaseModel):
    role: str
    content: object | None = None  # 兼容 null 和多模态数组 [{type:'text',text:...}]


class ChatReq(BaseModel):
    messages: list[Msg]
    model: str | None = None      # kb-rag=强制RAG, kb-auto=自动路由, 其余按kb-rag处理
    stream: bool | None = False  # 其余字段(temperature等)忽略，由服务端统一控制


def norm_content(c) -> str:
    """把各种形态的content归一化成纯文本"""
    if c is None:
        return ""
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return "".join(p.get("text", "") for p in c if isinstance(p, dict))
    return str(c)


def retrieve(question: str, top: int):
    """问题 -> bge-m3向量 -> Qdrant top-k"""
    qvec = oc.embed(model=EMBED_MODEL, input=[question])["embeddings"][0]
    return qc.query_points(COLLECTION, query=qvec, limit=top).points


def oai_chunk(cid: str, text: str | None = None, role: str | None = None, finish=None) -> str:
    delta: dict = {}
    if role:
        delta["role"] = role
    if text:
        delta["content"] = text
    return json.dumps(
        {"id": cid, "object": "chat.completion.chunk", "created": int(time.time()),
         "model": MODEL_NAME, "choices": [{"index": 0, "delta": delta, "finish_reason": finish}]},
        ensure_ascii=False,
    )


@app.get("/v1/models")
@app.get("/models")  # 兼容部分客户端把检查请求打到不带 /v1 的路径
def list_models():
    return {"object": "list", "data": [
        {"id": MODEL_NAME, "object": "model", "created": int(time.time()), "owned_by": "local"},
        {"id": AUTO_MODEL, "object": "model", "created": int(time.time()), "owned_by": "local"},
    ]}


@app.post("/v1/chat/completions")
def chat(req: ChatReq):
    if not qc.collection_exists(COLLECTION):
        return JSONResponse({"error": {"message": "索引不存在，先运行 uv run python main.py ingest"}},
                            status_code=500)
    # 只对最后一条 user 消息做检索，历史透传给生成模型
    history = [{"role": m.role, "content": norm_content(m.content)} for m in req.messages]
    last_q = next((m["content"] for m in reversed(history) if m["role"] == "user"), "")
    hits = retrieve(last_q, TOP_K_DEF)

    # ---- 自动路由：kb-auto 且 top1 分数低于阈值 → 无关知识库，直接自由回答 ----
    use_rag = True
    if req.model == AUTO_MODEL and (not hits or hits[0].score < ROUTE_THRESH):
        use_rag = False

    if use_rag:
        ctx = "\n\n".join(
            f"[{i+1}] 来源: {h.payload['file']}\n{h.payload['text']}" for i, h in enumerate(hits)
        )
        cite = "📚 检索来源:\n" + "\n".join(
            f"[{i+1}] {h.payload['file']} (score {h.score:.3f})" for i, h in enumerate(hits)
        ) + "\n\n"
        out_msgs = history[:-1] + [{"role": "user", "content": f"{INSTR}\n\n## 资料\n{ctx}\n\n## 问题\n{last_q}"}]
    else:
        # 直答模式：system换成自由助手提示，其余历史原样保留
        cite = ""
        out_msgs = [{"role": "system", "content": FREE_INSTR}] + \
            [m for m in history if m["role"] != "system"]

    cid = f"chatcmpl-{uuid.uuid4().hex[:12]}"
    gen = _gen_answer(out_msgs)  # 同步生成器: 产出回答文本片段

    if not req.stream:
        text = cite + "".join(gen)
        return {"id": cid, "object": "chat.completion", "created": int(time.time()),
                "model": MODEL_NAME,
                "choices": [{"index": 0, "message": {"role": "assistant", "content": text},
                             "finish_reason": "stop"}],
                "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}}

    def sse():
        yield f"data: {oai_chunk(cid, role='assistant')}\n\n"
        yield f"data: {oai_chunk(cid, text=cite)}\n\n"
        for t in gen:
            yield f"data: {oai_chunk(cid, text=t)}\n\n"
        yield f"data: {oai_chunk(cid, finish='stop')}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(sse(), media_type="text/event-stream")


def _gen_answer(messages: list[dict]):
    """qwen3 流式生成；默认关思考模式，旧版SDK无think参数则用 /no_think 指令"""
    try:
        stream = oc.chat(model=CHAT_MODEL, messages=messages, stream=True,
                         think=False, options={"temperature": 0.3}, keep_alive="30m")
        for part in stream:
            if (t := part["message"]["content"]):
                yield t
    except TypeError:
        messages[-1]["content"] += " /no_think"
        for part in oc.chat(model=CHAT_MODEL, messages=messages, stream=True,
                            options={"temperature": 0.3}, keep_alive="30m"):
            if (t := part["message"]["content"]):
                yield t


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="warning")
