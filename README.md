# AI-KB - 本地知识库 + Codex 原型工作流 (M5 Pro 64GB优化版)

> 给 AI 工具专家：技术笔记 + PDF/论文洞察 + 方案 + 原型，四合一。
> 全本地文件，Obsidian存，AnythingLLM问，Codex写原型。

## 目录结构
```
AI-KB/
  AGENTS.md              # Codex 入口，同时被子目录继承
  CLAUDE.md              # 备用，和AGENTS.md同内容
  Brewfile               # brew bundle 一键装机
  setup.sh               # 初始化：建目录+拉模型+起Qdrant
  ingest.sh              # PDF/论文一键入库：MinerU -> md -> 10-Papers
  HOME.md                # Obsidian 导航首页
  00-Inbox/              # 收集箱：待处理 PDF/剪藏/闪念，定期清空归档
  10-Papers/             # 论文洞察笔记（含_template-paper.md模板）
  15-News/              # 每日AI资讯日报（YYYY-MM-DD-AI资讯日报.md，参与RAG检索）
  20-Vendors/            # 厂商/工具测评（含模板）
  30-Solutions/          # 脱敏方案（唯一可喂给Codex云端的）
  40-Prototype/          # 原型，每个demo独立目录+自己的AGENTS.md
  50-Docs/               # 文档开发：可交付文档/报告/博客草稿（含模板）
  60-Projects/           # 咨询项目台账：每项目一个MOC索引页（含模板）
  70-Knowledge/          # 概念卡/永久笔记：原子知识+双链，问答语料核心（含模板）
  90-Archive-PDF/        # PDF原文存档，不进Codex上下文
  99-Assets/             # 附件（建议设为 Obsidian 附件默认目录）
```

## 快速开始（M5 Pro上执行）

```bash
# 1. 解压后进入
cd AI-KB
chmod +x setup.sh ingest.sh

# 2. 一键装机（Obsidian/Cherry/AnythingLLM/Ollama/Qdrant/uv）
./setup.sh

# 3. 入库第一篇论文
./ingest.sh ~/Downloads/some-paper.pdf
# 自动：MinerU解析 -> 00-Inbox转md -> 提示你填模板 -> 移入10-Papers

# 4. 问答（两种二选一）
# 纯聊天：打开 Cherry Studio，连本地 Ollama qwen3:32b-q8_0
# RAG带知识库：cd 40-Prototype/local-rag && uv run python server.py
#   Cherry Studio 添加 OpenAI 兼容提供商 http://127.0.0.1:8000/v1，模型名 kb-rag
#   或命令行: uv run python main.py ask "问题"

# 5. 做原型（核心）
cd 40-Prototype/demo-x
codex "根据 ../../30-Solutions/xxx方案.md 生成原型，参考 ../../20-Vendors/对比.md"
```

## Codex使用规范（防context爆炸）

1. 永远 `cd` 到 `40-Prototype/某个demo` 再调 `codex`，不要在根目录调。
2. 敏感PDF只放 `90-Archive-PDF/`，Codex默认不读。只有脱敏后的 `30-Solutions/*.md` 才喂给云端。
3. 本地敏感总结用：`ollama run qwen3:32b`，断网可跑。
4. 原型用 `uv` 管理，不污染系统Python。

## 模型配置（针对64GB统一内存）

- 主力洞察/方案：`qwen3:32b-q8_0` (~35GB) 中文最好
- 代码生成辅助：`deepseek-coder-v2:16b`
- Embedding：`bge-m3` (中英+代码召回最高)
- Rerank：暂未接入（ollama 对 rerank 模型支持弱，后续可在 local-rag 里加）
- Chunk：1200 / Overlap 250，论文表格多必须大chunk
