#!/usr/bin/env python3
"""Docência privada em SP fora do Gupy: Mackenzie (PSDU) e LinkedIn (vagas de professor de engenharia).
Uso: python3 docencia_sp.py  ->  só o que ainda não está em vistas.txt.
Complementa o gupy.py. Rodar em toda execução; de novembro a fevereiro é a temporada das seleções 2027.1."""
import html
import pathlib
import re
import time
import urllib.parse
import urllib.request

BASE = pathlib.Path(__file__).parent
VISTAS = (BASE / "vistas.txt").read_text(encoding="utf-8")
UA = {"User-Agent": "Mozilla/5.0"}


def get(url):
    return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40).read().decode("utf-8", "replace")


# 1) Mackenzie: PDFs de edital docente na página de processos seletivos
try:
    t = get("https://www.mackenzie.br/processos-seletivos/docente")
    pdfs = sorted(set(re.findall(r'href="([^"]+\.pdf)"', t)))
    pdfs = [p if p.startswith("http") else "https://www.mackenzie.br" + p for p in pdfs]
    pdfs = [p for p in pdfs if re.search(r"PSDU|Docente|Edital", p, re.I)]
    novos = [p for p in pdfs if p not in VISTAS]
    print(f"## Mackenzie: {len(pdfs)} PDFs de processo docente na página, {len(novos)} novos")
    for p in novos:
        print("NOVO", p)
except Exception as e:
    print("!! Mackenzie: não consegui ler", e)

# 2) LinkedIn (API pública sem login): professor/docente de engenharia na Grande SP, última semana
TERMOS = ["professor engenharia civil", "docente engenharia", "professor construção civil",
          "professor gestão de projetos", "professor universitário engenharia"]
FORA = re.compile(r"medicina|enfermagem|odonto|fisioterap|direito|psicolog|nutri|educação física|"
                  r"veterin|ensino fundamental|ensino médio|EF1|EF2|infantil|idiomas|inglês|escola|col[ée]gio|"
                  r"Fundação Bradesco|ginecolog|contabilidade|ciberseguran|security|sistemas de informação|computação", re.I)
vistos = set()
print("## LinkedIn (docência, última semana)")
for termo in TERMOS:
    time.sleep(3)  # a API devolve 429 se apertar demais
    url = ("https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?"
           + urllib.parse.urlencode({"keywords": termo, "location": "São Paulo, Brasil", "f_TPR": "r604800"}))
    try:
        h = get(url)
    except Exception as e:
        print(f"!! LinkedIn '{termo}': {e}")
        continue
    for card in h.split("<li")[1:]:
        m = re.search(r'href="(https://[a-z]+\.linkedin\.com/jobs/view/[^"?]+)', card)
        jid = re.search(r"(\d{6,})", m.group(1)) if m else None
        if not jid or jid.group(1) in vistos or jid.group(1) in VISTAS:
            continue
        vistos.add(jid.group(1))

        def campo(c):
            r = re.search(r'class="' + c + r'[^"]*"[^>]*>(.*?)</', card, re.S)
            return " ".join(html.unescape(re.sub("<[^>]+>", "", r.group(1) if r else "")).split())

        titulo = campo("base-search-card__title")
        if not re.search(r"professor|docente|instrutor|tutor|coordenador de curso", titulo, re.I) or FORA.search(titulo + ' ' + campo('base-search-card__subtitle')):
            continue
        print(f"NOVO {titulo} | {campo('base-search-card__subtitle')} | {campo('job-search-card__location')} | "
              f"https://www.linkedin.com/jobs/view/{jid.group(1)}")
