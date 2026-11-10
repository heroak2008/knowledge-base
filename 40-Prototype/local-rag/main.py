"""local-rag 入口：本地 RAG 问答原型
用法:
  uv run python main.py ingest                     # 扫描KB -> 分块 -> 向量化 -> 写入Qdrant
  uv run python main.py ask "问题" [--top 5] [--think]
"""
import argparse
import sys
from pathlib import Path

import ollama
from qdrant_client import QdrantClient, models

# ---- 配置（与根 README.md 模型配置一致）----
KB_ROOT = Path(__file__).resolve().parent.parent.parent  # AI-KB 根目录
SCAN_DIRS = [  # 入库范围：知识/产出目录 + 根README（不含 90-Archive-PDF、00-Inbox）
    KB_ROOT / "10-Papers",
    KB_ROOT / "15-News",
    KB_ROOT / "20-Vendors",
    KB_ROOT / "30-Solutions",
    KB_ROOT / "50-Docs",
    KB_ROOT / "60-Projects",
    KB_ROOT / "70-Knowledge",
    KB_ROOT / "README.md",
    KB_ROOT / "HOME.md",
]
COLLECTION = "kb_docs"
EMBED_MODEL = "bge-m3:latest"      # 1024 维
CHAT_MODEL = "qwen3:32b-q8_0"
CHUNK_SIZE = 1200                  # 根README约定：论文表格多，用大chunk
CHUNK_OVERLAP = 250
EMBED_DIM = 1024
TOP_K_DEF = 5                      # 默认召回块数

qc = QdrantClient(url="http://127.0.0.1:6333")
oc = ollama.Client(host="http://127.0.0.1:11434")


def chunk_text(text: str) -> list[str]:
    """按段落贪心合并到 CHUNK_SIZE，相邻块重叠 CHUNK_OVERLAP，尽量在换行处切"""
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks: list[str] = []
    cur = ""
    for p in paras:
        # 单段超长时硬切
        while len(p) > CHUNK_SIZE:
            if cur:
                chunks.append(cur)
                cur = cur[-CHUNK_OVERLAP:]
            cut = p.rfind("\n", 0, CHUNK_SIZE)
            cut = cut if cut > CHUNK_SIZE // 2 else CHUNK_SIZE
            chunks.append(p[:cut])
            p = p[max(cut - CHUNK_OVERLAP, 0):]
        if len(cur) + len(p) + 2 <= CHUNK_SIZE:
            cur = f"{cur}\n\n{p}" if cur else p
        else:
            chunks.append(cur)
            cur = cur[-CHUNK_OVERLAP:] + "\n\n" + p if CHUNK_OVERLAP else p
    if cur.strip():
        chunks.append(cur)
    return chunks


def collect_files() -> list[Path]:
    files = []
    for entry in SCAN_DIRS:
        if entry.is_file():
            files.append(entry)
        elif entry.is_dir():
            files.extend(sorted(entry.rglob("*.md")))
    return [f for f in files if f.name != "_template-*.md" or "*" in f.name]


def ingest() -> None:
    files = collect_files()
    if not files:
        print("没有找到任何 .md 文件，先往 10-Papers/ 等目录放笔记"); return

    # 重建集合（幂等：每次全量重建，KB规模小，够用）
    if qc.collection_exists(COLLECTION):
        qc.delete_collection(COLLECTION)
    qc.create_collection(
        collection_name=COLLECTION,
        vectors_config=models.VectorParams(size=EMBED_DIM, distance=models.Distance.COSINE),
    )

    total_chunks, batch, pid = 0, [], 0
    def flush():
        nonlocal total_chunks, batch, pid
        if not batch:
            return
        vecs = oc.embed(model=EMBED_MODEL, input=[b["text"] for b in batch])["embeddings"]
        qc.upsert(COLLECTION, points=[
            models.PointStruct(id=pid + i, vector=v, payload=b["payload"])
            for i, (b, v) in enumerate(zip(batch, vecs))
        ])
        pid += len(batch)
        total_chunks += len(batch)
        batch.clear()

    for f in files:
        rel = f.relative_to(KB_ROOT)
        text = f.read_text(encoding="utf-8", errors="ignore")
        for ci, chunk in enumerate(chunk_text(text)):
            batch.append({"payload": {
                "file": str(rel), "title": f.stem, "chunk": ci, "text": chunk,
            }, "text": chunk})
            if len(batch) >= 16:
                flush()
        print(f"  入库 {rel} ({len(chunk_text(text))} 块)")
    flush()
    print(f"\n✅ 完成：{len(files)} 个文件，{total_chunks} 个分块 -> Qdrant 集合 {COLLECTION}")


def ask(question: str, top: int, think: bool) -> None:
    if not qc.collection_exists(COLLECTION):
        print("索引不存在，先运行: uv run python main.py ingest"); return
    qvec = oc.embed(model=EMBED_MODEL, input=[question])["embeddings"][0]
    hits = qc.query_points(COLLECTION, query=qvec, limit=top).points
    if not hits:
        print("没有检索到任何内容"); return

    ctx = "\n\n".join(
        f"[{i+1}] 来源: {h.payload['file']}\n{h.payload['text']}" for i, h in enumerate(hits)
    )
    prompt = (
        "你是本地知识库助手。仅根据下面编号资料回答问题，"
        "答案末尾列出用到的来源编号和文件名；资料不足以回答就直说。\n\n"
        f"## 资料\n{ctx}\n\n## 问题\n{question}"
    )
    print(f"检索到 {len(hits)} 块（按相似度）:")
    for i, h in enumerate(hits):
        score = h.score
        print(f"  [{i+1}] {h.payload['file']} (chunk {h.payload['chunk']}, score {score:.3f})")
    print("\n---- 回答 ----")
    # qwen3 默认思考模式；默认关闭，--think 打开。keep_alive: 35GB大模型驻留30分钟，避免每次冷加载
    try:
        r = oc.chat(model=CHAT_MODEL, messages=[{"role": "user", "content": prompt}],
                    think=think, options={"temperature": 0.3}, keep_alive="30m")
        content = r.message.content
    except TypeError:  # 旧版SDK不支持think参数，用 /no_think 指令兜底
        r = oc.chat(model=CHAT_MODEL,
                    messages=[{"role": "user", "content": prompt + ("" if think else " /no_think")}],
                    options={"temperature": 0.3}, keep_alive="30m")
        content = r.message.content
    print(content)


def main() -> None:
    ap = argparse.ArgumentParser(description="本地RAG问答原型")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("ingest", help="扫描KB并重建向量索引")
    a = sub.add_parser("ask", help="提问")
    a.add_argument("question")
    a.add_argument("--top", type=int, default=TOP_K_DEF)
    a.add_argument("--think", action="store_true", help="开启qwen3思考模式")
    args = ap.parse_args()
    if args.cmd == "ingest":
        ingest()
    else:
        ask(args.question, args.top, args.think)


if __name__ == "__main__":
    sys.exit(main())
