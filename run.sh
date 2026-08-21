#!/usr/bin/env bash
set -uo pipefail

# Radar diário de oportunidades via Claude Code headless.
# Uso: ./run.sh                 -> trilhas ativas conforme cadência do perfil.md
#      ./run.sh sistema_s       -> força uma trilha
#      trilhas: concursos | sistema_s | contratacao_publica | bolsas | emprego | pj_privado | todas

PROJETO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$PROJETO"

TRILHA="${1:-cadencia}"
HOJE=$(date +%F)
DIA_SEMANA=$(date +%A)
RELATORIO="relatorios/${HOJE}.md"
LOG="logs/${HOJE}.log"
mkdir -p relatorios logs

if [ -f "$RELATORIO" ] && [ "$TRILHA" = "cadencia" ]; then
  echo "Relatório de $HOJE já existe. Saindo."
  exit 0
fi

if [ "$TRILHA" = "cadencia" ]; then
  ESCOPO="Rode as trilhas ativas do perfil.md respeitando a cadência declarada lá. Hoje é ${DIA_SEMANA}."
else
  ESCOPO="Rode APENAS a trilha: ${TRILHA}. Ignore a cadência."
fi

PROMPT="Hoje é ${HOJE} (${DIA_SEMANA}).

${ESCOPO}

1. Leia perfil.md, fontes.md, vistas.txt e oportunidades.csv.
2. Monte a seção ⚠️ PRAZOS a partir do oportunidades.csv: o que vence em 7 dias.
3. Busque oportunidades novas nas fontes de cada trilha, priorizando fonte oficial.
   Abra cada candidata e confirme prazo, requisitos e valor no documento original.
4. Pontue de 0 a 5 pela rubrica do CLAUDE.md. Descarte nota <3.
5. Nas trilhas de contratação pública, emprego privado e PJ/consultoria privada, marque a exigência de saída da ativa.
6. Escreva o relatório em ${RELATORIO}, no formato do CLAUDE.md.
7. Acrescente URLs reportados a vistas.txt e as de nota 4-5 ao oportunidades.csv com status 'radar'.

Regras: não se inscreva, não envie proposta, não submeta nada, não preencha formulário.
Não invente oportunidade nem prazo. Não reporte professor substituto ou temporário.
O que não conseguir verificar vai no rodapé como não verificado."

timeout 45m claude -p "$PROMPT" \
  --allowedTools "Read,Write,Edit,Glob,Grep,WebSearch,WebFetch" \
  --permission-mode acceptEdits \
  --max-turns 150 \
  > "$LOG" 2>&1

STATUS=$?

if [ $STATUS -ne 0 ]; then
  echo "Falha na execução (código $STATUS). Veja $LOG"
  exit $STATUS
fi

if [ -f "$RELATORIO" ]; then
  echo "Pronto: $RELATORIO"
else
  echo "Rodou sem erro mas não gerou relatório. Veja $LOG"
fi
