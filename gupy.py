#!/usr/bin/env python3
"""Varre as páginas Gupy de universidades e lista vagas de docência no estado de SP (ou remotas).
Uso: python3 gupy.py  ->  uma linha por vaga: instituição | título | cidade | link
Só descobre: abra o link e confira requisitos antes de reportar."""
import json
import re
import urllib.request

# Páginas de carreira no Gupy (subdomínio). Mackenzie, UNIP e Uninove não usam Gupy: ver fontes.md.
PAGINAS = {
    "fmu": "FMU",
    "cogna": "Cogna (Anhanguera, Pitágoras, Unopar)",
    "yduqs": "Yduqs (Estácio, Ibmec, Wyden)",
    "cruzeirodosul": "Cruzeiro do Sul",
    "anima": "Ânima (São Judas, Anhembi Morumbi)",
    "unicid": "Unicid",
    "pucsp": "PUC-SP",
    "ibmec": "Ibmec",
    "unifecaf": "UniFECAF",
    "ceunsp": "Ceunsp",
    "facens": "Facens",
    "senac": "Senac",
}
DOCENCIA = re.compile(r"professor|docente|tutor|instrutor|coordenador(a)? de curso|coordena[çc][ãa]o de curso", re.I)
FORA_DO_PERFIL = re.compile(r"medicina|enfermagem|odonto|fisioterap|farm[áa]cia|nutri[çc]|psicolog|direito|"
                            r"veterin|biomedic|fonoaud|terapia ocupacional|educa[çc][ãa]o f[íi]sica|est[ée]tica|agronomia", re.I)


def vagas(slug):
    req = urllib.request.Request(f"https://{slug}.gupy.io/", headers={"User-Agent": "Mozilla/5.0"})
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "replace")
    m = re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        return

    def walk(o):
        if isinstance(o, dict):
            if "title" in o and "id" in o and ("workplace" in o or "type" in o):
                yield o
            for v in o.values():
                yield from walk(v)
        elif isinstance(o, list):
            for v in o:
                yield from walk(v)

    yield from walk(json.loads(m.group(1)))


for slug, nome in PAGINAS.items():
    try:
        lista = list(vagas(slug))
    except Exception as e:  # página fora do ar ou mudou de formato: avisa e segue
        print(f"!! {nome}: não consegui ler ({e})")
        continue
    for j in lista:
        titulo = " ".join(j.get("title", "").split())
        if not DOCENCIA.search(titulo) or FORA_DO_PERFIL.search(titulo):
            continue
        w = j.get("workplace") or {}
        end = w.get("address") or {} if isinstance(w, dict) else {}
        uf = end.get("stateShortName") or end.get("state") or ""
        remoto = "remote" in json.dumps(w).lower()
        if uf not in ("SP", "São Paulo") and not remoto and "SP" not in titulo.upper().split("/")[-1:]:
            continue
        print(f"{nome} | {titulo} | {end.get('city') or ('remoto' if remoto else '?')} | https://{slug}.gupy.io/jobs/{j['id']}")
