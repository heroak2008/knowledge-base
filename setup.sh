#!/bin/bash
set -e
KB_DIR="$(cd "$(dirname "$0")" && pwd)"
echo "=== AI-KB setup (M5 Pro 64GB) ==="

# 1. 目录
mkdir -p "$KB_DIR"/{00-Inbox,10-Papers,15-News,20-Vendors,30-Solutions,40-Prototype,50-Docs,60-Projects,70-Knowledge,90-Archive-PDF,99-Assets}
echo "[1/4] 目录 OK"

# 2. brew
if ! command -v brew >/dev/null; then
  echo "请先装 Homebrew: https://brew.sh"
  exit 1
fi
brew bundle --file="$KB_DIR/Brewfile" || true
echo "[2/4] brew OK"

# 3. ollama 模型 (后台启动)
brew services start ollama || ollama serve >/dev/null 2>&1 &
sleep 2
ollama pull qwen3:32b-q8_0 || true
ollama pull deepseek-coder-v2:16b || true
ollama pull bge-m3 || true
ollama pull nomic-embed-text || true
echo "[3/4] ollama 模型 OK"

# 4. python 工具：mineru (uv 管理，系统pip不装)
command -v mineru >/dev/null || uv tool install --python /opt/homebrew/bin/python3.12 mineru
echo "[4/4] mineru OK"
echo ""
echo "完成！下一步："
echo "1. 打开 Obsidian，'打开文件夹作为仓库': $KB_DIR"
echo "2. RAG问答: cd 40-Prototype/local-rag && uv run python server.py，Cherry Studio 添加OpenAI兼容提供商 http://127.0.0.1:8000/v1 模型 kb-rag"
echo "3. ./ingest.sh ~/Downloads/xxx.pdf  入库第一篇论文"
