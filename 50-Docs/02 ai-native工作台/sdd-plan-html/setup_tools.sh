#!/usr/bin/env bash
# 下载 PlantUML 与便携 JRE 到工具目录，供 build.py 使用。
# 用法：bash setup_tools.sh            → 默认目录 $SDD_PLANTUML_TOOLS 或 $TMPDIR/sdd-plan-tools
#      SDD_PLANTUML_TOOLS=./tools bash setup_tools.sh
# 依赖：curl、tar；支持 macOS（arm64/x86_64）与 Linux（aarch64/x64）
set -euo pipefail

TOOLS="${SDD_PLANTUML_TOOLS:-${TMPDIR:-/tmp}/sdd-plan-tools}"
PLANTUML_VERSION="1.2026.10"
mkdir -p "$TOOLS"

case "$(uname -m)" in
  arm64|aarch64) JARCH=aarch64 ;;
  x86_64|amd64) JARCH=x64 ;;
  *) echo "不支持的架构: $(uname -m)"; exit 1 ;;
esac
case "$(uname -s)" in
  Darwin) JOS=mac ;;
  Linux) JOS=linux ;;
  *) echo "不支持的系统: $(uname -s)"; exit 1 ;;
esac

if [ ! -f "$TOOLS/plantuml.jar" ]; then
  echo "下载 plantuml-$PLANTUML_VERSION.jar ..."
  curl -fL --retry 3 -o "$TOOLS/plantuml.jar" \
    "https://github.com/plantuml/plantuml/releases/download/v$PLANTUML_VERSION/plantuml-$PLANTUML_VERSION.jar"
fi

if ! ls "$TOOLS"/*/bin/java "$TOOLS"/*/Contents/Home/bin/java >/dev/null 2>&1; then
  echo "下载 Temurin JRE 21 ($JOS/$JARCH) ..."
  curl -fL --retry 3 -o "$TOOLS/jre.tar.gz" \
    "https://api.adoptium.net/v3/binary/latest/21/ga/$JOS/$JARCH/jre/hotspot/normal/eclipse?project=jdk"
  mkdir -p "$TOOLS/jdk-21"
  tar -xzf "$TOOLS/jre.tar.gz" -C "$TOOLS/jdk-21" --strip-components=1
  rm -f "$TOOLS/jre.tar.gz"
fi

echo "工具目录: $TOOLS"
ls -la "$TOOLS" | sed -n '1,12p'
echo "验证: python3 build.py"
