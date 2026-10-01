#!/usr/bin/env python3
"""Converte um relatório .md em PDF. Uso: python3 pdf.py relatorios/AAAA-MM-DD.md"""
import pathlib
import subprocess
import sys
import tempfile

import markdown

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

CSS = """
@page { size: A4; margin: 18mm 16mm; }
body { font-family: 'DejaVu Sans', Arial, sans-serif; font-size: 10.5pt; line-height: 1.45; color: #1a1a1a; }
h1 { font-size: 17pt; border-bottom: 2px solid #1a1a1a; padding-bottom: 4px; }
h2 { font-size: 13pt; margin-top: 18px; }
h3 { font-size: 11.5pt; margin-top: 16px; background: #f1f1f1; padding: 5px 8px; border-left: 4px solid #1a1a1a; }
ul { padding-left: 18px; }
li { margin: 3px 0; }
a { color: #0b57d0; word-break: break-all; }
code { font-size: 9.5pt; }
"""

origem = pathlib.Path(sys.argv[1])
destino = origem.with_suffix(".pdf")
corpo = markdown.markdown(origem.read_text(encoding="utf-8"), extensions=["extra", "sane_lists"])
html = f"<!doctype html><html lang='pt-BR'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{corpo}</body></html>"

with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
    f.write(html)

subprocess.run(
    [CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
     f"--print-to-pdf={destino.resolve()}", f"file://{f.name}"],
    check=True, capture_output=True,
)
print(destino)
