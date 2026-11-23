#!/usr/bin/env python3
"""构建两个静态 HTML 方案页（方案 A：SDD 工具链系统化方案；方案 B：与 CoreALM-Next 结合方案）。

用法：
  python3 build.py                  # 渲染 puml/*.puml → build/svg/*.svg，再装配 src/*.html
  python3 build.py --skip-render    # 只装配（已有 SVG 时）
  python3 build.py --tools <dir>    # 指定 plantuml jar 与 JRE 所在目录（默认 $SDD_PLANTUML_TOOLS 或 $TMPDIR/sdd-plan-tools）

依赖：Java 17+ 与 plantuml.jar（运行 setup_tools.sh 可自动下载）。
验证：控制台打印每张图的尺寸与页面大小；退出码非 0 表示有图渲染失败或占位符未替换。
"""
from __future__ import annotations

import argparse
import base64
import html
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PUML_DIR = ROOT / "puml"
SVG_DIR = ROOT / "build" / "svg"
SRC_DIR = ROOT / "src"
CSS = ROOT / "assets" / "style.css"
OUT_DIR = ROOT.parent  # 50-Docs/02 ai-native工作台/

PAGES = {
    "A": "SDD工具链系统化方案.html",
    "B": "SDD工具链与CoreALM-Next结合方案.html",
}
# PlantUML 出错或告警时会把文字直接画进 SVG，这里列出需要拦截的关键词
ERROR_MARKERS = ("Syntax Error", "not recognized", "Diagram not supported", "Error line", "deprecated", "instead of")


def find_tools_dir(arg: str | None) -> Path | None:
    for cand in (arg, os_environ("SDD_PLANTUML_TOOLS"), str(Path(os_environ("TMPDIR", "/tmp")) / "sdd-plan-tools")):
        if cand and Path(cand).is_dir():
            return Path(cand)
    return None


def os_environ(name: str, default: str = "") -> str:
    import os

    return os.environ.get(name, default)


def find_java(tools: Path | None) -> str | None:
    candidates: list[str] = []
    if tools:
        candidates += [str(p) for p in sorted(tools.glob("*/Contents/Home/bin/java"))]
        candidates += [str(p) for p in sorted(tools.glob("*/bin/java"))]
    if shutil.which("java"):
        candidates.append(shutil.which("java"))  # type: ignore[arg-type]
    for java in candidates:
        try:
            r = subprocess.run([java, "-version"], capture_output=True, text=True, timeout=30)
            if r.returncode == 0 and ("version" in r.stderr or "version" in r.stdout):
                return java
        except (OSError, subprocess.TimeoutExpired):
            continue
    return None


def find_jar(tools: Path | None) -> Path | None:
    if not tools:
        return None
    exact = tools / "plantuml.jar"
    if exact.is_file():
        return exact
    jars = [p for p in sorted(tools.glob("plantuml-*.jar")) if "mit" not in p.name]
    return jars[0] if jars else None


def render(java: str, jar: Path) -> list[Path]:
    SVG_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(PUML_DIR.glob("*.puml"))
    # 注意：-o 的相对路径是相对源文件目录解析的，必须传绝对路径
    cmd = [java, "-Djava.awt.headless=true", "-jar", str(jar), "-charset", "UTF-8", "-tsvg", "-o", str(SVG_DIR), *[str(f) for f in files]]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 or "Error" in r.stderr:
        print(r.stdout[-2000:], r.stderr[-2000:], file=sys.stderr)
        raise SystemExit(f"PlantUML 渲染失败（退出码 {r.returncode}）")
    bad = []
    for f in files:
        svg = SVG_DIR / (f.stem + ".svg")
        if not svg.is_file():
            bad.append(f"{f.name}: 无输出")
            continue
        text = svg.read_text(encoding="utf-8")
        if any(m in text for m in ERROR_MARKERS):
            bad.append(f"{f.name}: SVG 内含错误标记")
    if bad:
        raise SystemExit("以下图渲染异常：\n  " + "\n  ".join(bad))
    return files


def svg_size(svg: Path) -> str:
    m = re.search(r'<svg[^>]*?\swidth="([\d.]+)px"[^>]*?\sheight="([\d.]+)px"', svg.read_text(encoding="utf-8"))
    return f"{int(float(m.group(1)))}×{int(float(m.group(2)))}" if m else "?"


def img_tag(name: str, alt: str) -> str:
    svg = SVG_DIR / f"{name}.svg"
    puml = PUML_DIR / f"{name}.puml"
    if not svg.is_file():
        raise SystemExit(f"缺少 {svg}，请先渲染")
    data = base64.b64encode(svg.read_bytes()).decode("ascii")
    src = html.escape(puml.read_text(encoding="utf-8").strip()) if puml.is_file() else "（无源码）"
    return (
        f'<img src="data:image/svg+xml;base64,{data}" alt="{html.escape(alt)}" loading="lazy">\n'
        f'<details class="src"><summary>PlantUML 源码 · {svg_size(svg)}</summary><pre>{src}</pre></details>'
    )


def assemble(letter: str) -> Path:
    src = SRC_DIR / f"{letter}.html"
    out = OUT_DIR / PAGES[letter]
    text = src.read_text(encoding="utf-8")
    text = text.replace("{{CSS}}", "<style>\n" + CSS.read_text(encoding="utf-8") + "\n</style>")
    names: list[str] = []

    def repl(m: re.Match[str]) -> str:
        names.append(m.group(1))
        return img_tag(m.group(1), m.group(2) or m.group(1))

    text = re.sub(r"\{\{IMG:([A-Za-z0-9_]+)(?:\|([^}]*))?\}\}", repl, text)
    if "{{" in text:
        raise SystemExit(f"{src.name} 仍有未替换占位符：{re.findall(r'{{[^}}]*}}', text)[:5]}")
    out.write_text(text, encoding="utf-8")
    size_kb = out.stat().st_size / 1024
    print(f"  {out.name}: {len(names)} 张图, {size_kb:.0f} KB")
    for n in names:
        print(f"    - {n} {svg_size(SVG_DIR / (n + '.svg'))}")
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--skip-render", action="store_true", help="跳过 PlantUML 渲染")
    ap.add_argument("--tools", help="plantuml jar 与 JRE 所在目录")
    args = ap.parse_args()
    tools = find_tools_dir(args.tools)
    if not args.skip_render:
        java = find_java(tools)
        jar = find_jar(tools)
        if not java or not jar:
            raise SystemExit("未找到 Java 或 plantuml jar：请运行 `bash setup_tools.sh` 后重试，或用 --tools 指定目录")
        files = render(java, jar)
        print(f"PlantUML 渲染完成：{len(files)} 张 → {SVG_DIR}")
    print("装配页面：")
    outs = [assemble(k) for k in sorted(PAGES)]
    print("验证：")
    for out in outs:
        t = out.read_text(encoding="utf-8")
        print(f"  {out.name}: img={t.count('<img ')} details={t.count('<details class=\"src\">')} 残留占位符={'{{' in t}")


if __name__ == "__main__":
    main()
