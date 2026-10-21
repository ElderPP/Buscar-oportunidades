#!/usr/bin/env python3
"""Lista as vagas abertas da UNOPS (ONU) que são home-based ou no Brasil.
Uso: python3 unops.py  ->  título | local | nível | fim | link
Só descobre: abra cada link novo com WebFetch e confira requisitos, idioma e prazo (meia-noite de Copenhague)."""
import html
import re
import urllib.request

BASE = "https://careers.unops.org/careersmarketplace/SearchJobs/?jobRecordsPerPage=6&jobOffset={}"
LOCAL_OK = re.compile(r"home.?based|brazil|brasil|bras[ií]lia|s[ãa]o paulo|rio de janeiro|southern cone|cone sul", re.I)


def pagina(offset):
    req = urllib.request.Request(BASE.format(offset), headers={"User-Agent": "Mozilla/5.0"})
    return urllib.request.urlopen(req, timeout=40).read().decode("utf-8", "replace")


vistos, offset, total = {}, 0, None
CARD = re.compile(r'<h3[^>]*>\s*<a class="link" href="(https://careers\.unops\.org/careersmarketplace/JobDetail/[^"]+/\d+)"[^>]*>\s*(.*?)\s*</a>.*?'
                  r'list-item-Duty Station">(.*?)</span>.*?list-item-Seniority Level">(.*?)</span>.*?list-item-posted">(.*?)</span>', re.S)
while total is None or offset < total:
    h = pagina(offset)
    if total is None:
        m = re.search(r'aria-label="(\d+) results"', h)
        total = int(m.group(1)) if m else 0
    for link, titulo, local, nivel, fim in CARD.findall(h):
        vistos.setdefault(link, tuple(html.unescape(x.strip()) for x in (titulo, local, nivel, fim)))
    offset += 6

for link, (titulo, local, nivel, fim) in vistos.items():
    if LOCAL_OK.search(f"{titulo} {local}"):
        print(f"{titulo} | {local} | {nivel} | fim {fim} | {link}")
print(f"(lidas {len(vistos)} de {total})")
