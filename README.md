# Radar de oportunidades — Elder Pita

Monitora seis trilhas todo dia útil e entrega um relatório único, aberto pelos prazos que estão vencendo.

**Concursos · Sistema S · Contratação pública · Bolsas e fomento · Emprego privado · PJ/consultoria privada**

## Setup

```bash
chmod +x run.sh
./run.sh
```

O `perfil.md` já veio preenchido com seu currículo, Lattes e LinkedIn, incluindo os três campos que antes ficavam em aberto:

1. **Data de saída da ativa** — pode sair a qualquer momento, sem data fixa. As trilhas 3 e 5 tratam prazo como compatível por padrão.
2. **Salário mínimo** — sem piso para o que não exige saída da ativa (concursos, Sistema S, bolsas). Para o que exige saída (contratação pública, emprego privado), também sem piso definido — decisão caso a caso.
3. **Mobilidade geográfica** — qualquer estado, exceto emprego em empresa privada (trilha 5), que fica restrito a São Paulo.

## Calibrar antes de agendar

Rode uma trilha por vez nos primeiros dias:

```bash
./run.sh sistema_s
./run.sh concursos
./run.sh contratacao_publica
./run.sh bolsas
./run.sh emprego
./run.sh pj_privado
```

Se a nota vier inflada ou o recorte errado, ajuste o `perfil.md` — não o script.

## Agendar

```bash
crontab -e
```

```
0 5 * * 1-5 /caminho/absoluto/buscar-oportunidades/run.sh >> /caminho/absoluto/buscar-oportunidades/logs/cron.log 2>&1
```

Caminho absoluto sempre. Se der `claude: command not found`, rode `which claude` e use o caminho completo no `run.sh`. Autenticação: `claude setup-token` uma vez na máquina — sem isso o cron falha calado, e é para isso que serve o log.

## O funil

`oportunidades.csv` já vem com a vaga do Sebrae-SP registrada, prazo 17/08.

Status: `radar` → `inscrito` / `proposta_enviada` → `em_andamento` → `aprovado` / `reprovado` / `perdi_prazo`

```bash
claude "me inscrevi no Sebrae, muda o status e põe a prova de 25/08 como próximo passo"
claude "leia oportunidades.csv: o que vence este mês e eu ainda não comecei?"
```

## Regras embutidas no CLAUDE.md

- Nunca se inscreve, envia proposta ou preenche formulário por você
- Nunca reporta professor substituto ou temporário — só efetivo
- Toda oportunidade das trilhas 3, 5 e 6 vem marcada com o aviso de que exige saída da ativa
- Prazo sem confirmação no edital = a oportunidade não entra
- Nota mínima 3 para aparecer, e cada item declara o que pode te eliminar e qual documento você precisa providenciar

## Pendências suas, fora do radar

Coisas que aumentam sua nota em vários editais de uma vez:

1. **Registrar ART do que puder do trabalho na Marinha** — planilha orçamentária, ETP, especificação. Você tem cinco anos de produção provavelmente sem registro, e acervo construído dentro do serviço vale para o resto da carreira. Confirme com o CREA-SP o que é anotável na sua condição. Depois emita a CAT.
2. **Lançar Marinha e Estácio na "Atuação Profissional" do Lattes** e na experiência do LinkedIn. Hoje seu emprego atual está invisível nos dois.
3. **TOEFL iBT ou IELTS** — TOEIC e TOEFL ITP raramente são aceitos em bolsa internacional.
4. **Trocar as competências do LinkedIn** — hoje estão "Cooperation", "Dialogues", "Microsoft Outlook". Faltam Revit, AutoCAD, orçamento de obras, gestão de contratos, Lei 14.133.

## Limites honestos

- Cobertura do PNCP não é total; municípios menores publicam só em portal próprio.
- LinkedIn e Lattes bloqueiam acesso automatizado. O radar depende de diários oficiais e PDFs de edital, que funcionam bem.
- Sistema S não publica em lugar centralizado — o radar varre portal por portal, e prazos ali costumam ser de uma semana.
- PJ/consultoria privada não tem portal nenhum — é a trilha mais fraca em cobertura automatizada, depende de rede de contatos que o radar não alcança.
- Isto é triagem. Antes de se inscrever, leia o edital inteiro. Prazo e requisito eliminatório são responsabilidade sua.
