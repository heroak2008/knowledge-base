# local-rag 原型说明

## 目标
验证纯本地 RAG 问答链路：KB 的 Markdown 笔记 → bge-m3 向量 → Qdrant 检索 → qwen3:32b-q8_0 生成（附来源引用）。不依赖 AnythingLLM，全部命令行可复现。

## 架构
```
10-Papers/ 15-News/ 20-Vendors/ 30-Solutions/ 50-Docs/ 60-Projects/ 70-Knowledge/ + 根 README/HOME
        │ main.py ingest（分块 1200/重叠 250）
        ▼
  bge-m3 (ollama:11434) ──► Qdrant 集合 kb_docs (1024维, cosine)
                                    │ main.py ask --top 5
                                    ▼
                        qwen3:32b-q8_0 生成 + 来源列表
```

## 依赖
- 服务：ollama (127.0.0.1:11434)、qdrant (127.0.0.1:6333)，均已在 brew/LaunchAgent 常驻
- 模型：`bge-m3:latest`、`qwen3:32b-q8_0`
- Python 包（uv 管理）：`ollama`、`qdrant-client`、`fastapi`、`uvicorn`

## 运行
```bash
cd 40-Prototype/local-rag
uv run python main.py ingest          # 扫描KB入库/重建索引
uv run python main.py ask "这个知识库用什么embedding模型？"
uv run python main.py ask "问题" --top 5 --no-think
uv run python server.py               # 启动OpenAI兼容API (127.0.0.1:8000)，供Cherry Studio等客户端
```

## Cherry Studio 接入（GUI 聊 RAG）
1. 设置 → 模型服务 → 添加提供商（OpenAI 兼容）：API 地址 `http://127.0.0.1:8000/v1`，API Key 随便填
2. 手动添加模型，名称填 `kb-rag` 或 `kb-auto`
   - `kb-rag`：强制 RAG，总是检索并带来源回答
   - `kb-auto`：自动路由，检索分数 ≥0.50 走 RAG，低于阈值直接用 qwen3 自由回答（日常聊天选这个，不用手动切模型）
3. 聊天选模型即走"检索→生成"，RAG 模式回答开头自动带 📚 来源列表
4. 性能预期：模型驻留时首字 ~1s；空闲 30 分钟后下次提问要等 ~1 分钟（35GB 重新加载）；32B q8 生成约 5-6 token/s，长回答请耐心

注：服务已配置 LaunchAgent（~/Library/LaunchAgents/local.rag.server.plist）开机常驻，日志在 /tmp/kb-rag-server.log

## 如何验证
1. `curl -s localhost:6333/healthz` 返回 ok（qdrant 活着）
2. ingest 输出入库文件数与分块数
3. 问 README.md 里有明确答案的问题，如：
   `uv run python main.py ask "模型配置里 chunk 大小和 overlap 是多少？"`
   → 应回答 1200 / 250，且来源列表包含 `README.md`
