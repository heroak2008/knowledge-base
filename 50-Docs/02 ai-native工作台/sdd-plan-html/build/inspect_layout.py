#!/usr/bin/env python3
"""打印 SVG 内文本坐标，用于在没有图像输入时检查布局（层是否对齐、是否错位）。用法: python3 inspect_layout.py a.svg [b.svg ...]"""
import re, sys, html
for p in sys.argv[1:]:
    s = open(p, encoding='utf-8').read()
    w = re.search(r'width:(\d+)px;height:(\d+)px', s)
    print(f'== {p} {w.group(1) if w else "?"}x{w.group(2) if w else "?"}')
    rows = []
    for m in re.finditer(r'<text([^>]*)>(.*?)</text>', s, flags=re.S):
        a = m.group(1); t = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
        x = re.search(r'\bx="([\d.]+)"', a); y = re.search(r'\by="([\d.]+)"', a); tl = re.search(r'textLength="([\d.]+)"', a)
        if x and y:
            rows.append((round(float(y.group(1))), round(float(x.group(1))), float(tl.group(1)) if tl else 0, t))
    for y, x, tl, t in sorted(rows):
        print(f'  y={y:5d} x={x:5d} w={tl:5.0f}  {t[:46]}')
