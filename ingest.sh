#!/bin/bash
# ingest.sh - PDF/论文一键入库
# 用法: ./ingest.sh xxx.pdf [--keep-pdf]
set -e
KB_DIR="$(cd "$(dirname "$0")" && pwd)"
PDF="$1"
[ -z "$PDF" ] && echo "用法: ./ingest.sh xxx.pdf" && exit 1
[ ! -f "$PDF" ] && echo "找不到文件: $PDF" && exit 1

BASE=$(basename "$PDF" .pdf | tr ' ' '_')
DATE=$(date +%Y-%m-%d)
TMP_OUT="$KB_DIR/00-Inbox/${BASE}_${DATE}"

mkdir -p "$KB_DIR/00-Inbox" "$KB_DIR/10-Papers" "$KB_DIR/90-Archive-PDF"

echo ">> 解析: $PDF"
if command -v mineru >/dev/null; then
  mineru -p "$PDF" -o "$TMP_OUT" || echo "MinerU失败，改用pymupdf纯文本"
fi

# fallback: pymupdf 纯文本
MD_CANDIDATE=$(find "$TMP_OUT" -name "*.md" 2>/dev/null | head -1)
if [ -z "$MD_CANDIDATE" ]; then
  echo ">> MinerU无md输出，用pymupdf提取纯文本"
  MD_CANDIDATE="$TMP_OUT/fallback.md"
  mkdir -p "$TMP_OUT"
  uv run --with pymupdf python -c "
from pathlib import Path
import fitz
doc=fitz.open('$PDF')
text='\n\n'.join([p.get_text() for p in doc])
Path('$MD_CANDIDATE').write_text('# $BASE\n\n> 原文件：$PDF\n> 入库日期：$DATE\n\n'+text, encoding='utf-8')
print('pages:', len(doc))
"
fi

DEST="$KB_DIR/10-Papers/${DATE}-${BASE}.md"
# 加模板头
python3 -c "
from pathlib import Path
p=Path('$MD_CANDIDATE').read_text(encoding='utf-8', errors='ignore')
header='''---
type: paper
date: $DATE
source_pdf: $PDF
status: inbox
---

# $BASE

## 一句话总结（AI先填，人再改）
<!-- ollama run qwen3:32b "总结这篇论文3句话" -->

## 问题/方法/数据
-

## 局限
-

## 对我的启发（可复用到方案/原型）
-

## 原文摘录（自动解析内容在下面）
---
'''
Path('$DEST').write_text(header+p, encoding='utf-8')
print('wrote', '$DEST')
"

cp "$PDF" "$KB_DIR/90-Archive-PDF/" && echo ">> PDF原文已存档 90-Archive-PDF/"

echo ""
echo "完成: $DEST"
echo "下一步："
echo "1. Obsidian打开它，填上面的模板"
echo "2. Codex里问: codex \"总结 $DEST，输出对比表格\""
