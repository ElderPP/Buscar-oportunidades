# Fontes

Ordem: **fonte oficial > portal do órgão > agregador**. Agregador descobre; o edital confirma prazo, valor e requisito.

## 1. Concursos

Oficiais:
- Diário Oficial da União — https://www.in.gov.br (editais federais saem aqui primeiro)
- Portal do MEC e páginas "Concursos" de cada IF e universidade federal — os editais docentes muitas vezes só saem lá
- Centro Paula Souza — https://www.cps.sp.gov.br (concursos ETEC/FATEC)
- Diários oficiais estaduais e municipais
- Bancas: Cebraspe, FGV, FCC, Vunesp, Cesgranrio, IBFC, IDECAN, Instituto AOCP

Agregadores (descoberta):
- PCI Concursos, Concursos no Brasil, Folha Dirigida

Para concurso docente, busque **o edital da edição anterior do mesmo órgão** para ver peso da prova de títulos e concorrência histórica. É onde o perfil dele decide.

Termos de busca úteis: "professor efetivo engenharia civil", "EBTT edificações", "magistério superior construção civil", "engenheiro civil analista", "perito engenharia tribunal".

## 2. Sistema S

Cada entidade publica em portal próprio, geralmente como "Comunicado" ou "Processo Seletivo Externo". Não saem no DOU. Verifique um por um:

- Sebrae-SP — https://sebrae.com.br/sp/sobre-nos/trabalhe-conosco/vagas-efetivas-2026
- Sebrae Nacional e demais estaduais — cada um tem seu "Trabalhe Conosco"
- Senai, Sesi e IEL — portais estaduais (FIESP/SP, FIEMG, FIRJAN etc.)
- Sesi/Senai-SP — todas as vagas (inclusive bancos de talentos de instrutor) em https://sesisenaisp.empregare.com/pt-br/vagas?pagina=1 (2, 3, 4…); o "Trabalhe conosco" de sp.senai.br redireciona para lá. Seleções maiores do Sesi-SP já saíram pelo Cebraspe
- Senac e Sesc — portais estaduais
- Sest/Senat, Sescoop
- Faculdade Sebrae (SP) — vagas de professor adjunto: comunicados do Sebrae-SP ("Trabalhe Conosco", PDFs numerados NNN_2026) e site da banca RBO Concursos, onde é feita a inscrição
- Credenciamento de instrutores e consultores do Sebrae (editais estaduais de credenciamento de pessoa jurídica para consultoria e instrutoria) — exige saída da ativa, marque como tal
- ALI — Agentes Locais de Inovação: portais estaduais do Sebrae e bancas do processo, para acompanhar o cronograma

Bancas que operam esses processos: RBO, IBFC, Instituto AOCP, FCC, Vunesp. Vale checar as páginas delas também.

Atenção: prazos de inscrição do Sistema S costumam ser curtíssimos, às vezes uma semana. Essa trilha justifica a varredura diária sozinha.

## 3. Contratação pública

- **PNCP** — https://pncp.gov.br/app/editais — portal oficial da Lei 14.133/2021. Filtre `status=recebendo_proposta`. Há API pública de consulta (Swagger em https://pncp.gov.br/api/consulta/swagger-ui/index.html); prefira a API à interface.
  - Limitação: nem todo município publica lá.
- Compras.gov.br — dispensa eletrônica e pregões federais
- Editais de credenciamento: buscar em portais de tribunais (TJSP, TRF3, TRTs), prefeituras da região e órgãos estaduais. Termos: "credenciamento perito", "credenciamento engenheiro", "chamamento público laudo"
- Cadastro de perito judicial: TJSP, TRF3, varas trabalhistas
- Plataformas de disputa: Licitações-e, BLL, Portal de Compras Públicas, BNC, BEC/SP

Antes de avaliar chance, consulte **atas e resultados de certames anteriores do mesmo órgão para o mesmo objeto** — é o melhor indicador de quantos concorrem.

## 4. Bolsas e fomento

- CAPES — gov.br/capes
- CNPq — gov.br/cnpq (chamadas públicas)
- FAPESP — fapesp.br (ele está em SP; concorrência menor que chamada nacional)
- Demais FAPs estaduais
- Pró-reitoria de pesquisa da UFSCar — editais internos, os menos disputados de todos
- FINEP, Sebrae (fomento a projeto e inovação)
- ANTAC, IBRACON — prêmios e chamadas da área
- Internacionais: DAAD, Chevening, Fulbright, Erasmus Mundus (checar exigência de TOEFL iBT/IELTS antes de reportar)

### Bolsista em convênios (toda execução)

- **Fundação PATRIA** (convênios com Marinha/CTMSP e Aeronáutica/DCTA) — rode `NODE_PATH=$(npm root -g) node patria.js`: lista bolsas e vagas abertas com data final. Edital em PDF: `https://sistemas.patria.org.br/repository//tmp/EDITAL<NN><PROJETO><ANO>ass.pdf` (ex.: EDITAL12FORNIT2026ass.pdf). Leia o local de atuação: a mesma bolsa costuma sair em editais separados por cidade.
- **FDTE** (Poli-USP; convênio 2130 com o CTMSP, bolsas P&D na área nuclear) — chamadas públicas numeradas em https://www.fdte.org.br/transparencia/portal-da-transparencia/procedimentos-licitatorios/ (a 20ª encerrou em 08/2026; P&D B = R$ 6.500, A = R$ 7.750) e vagas em https://www.fdte.org.br/vagas/. Use `curl`.
- **FAPESP Oportunidades** — https://fapesp.br/oportunidades/ (bolsas TT, PD, JP abertas em projetos; quase todas pedem dedicação exclusiva — sinalize). Filtre por engenharia, construção, materiais, incêndio, gestão, educação.
- **Bolsas EaD que aceitam quem tem outro vínculo (as mais compatíveis com a Marinha)** — remotas, carga parcial, bolsa CAPES/UAB ou do próprio programa:
  - UNIVESP — facilitador e editais da PRPG em https://univesp.br (ele já foi facilitador/tutor 2023-2025)
  - UAB/CAPES nas universidades: Unesp EaD (https://processoseletivo.ead.unesp.br), UFSCar SEaD, Unifesp, UFABC, IFSP; e fora de SP com atuação remota: UFMG DEDD (https://www.ufmg.br/dedd), UFMT SETEC (https://setec.ufmt.br), UFSC, UFF/CEDERJ. Cargos: professor formador, professor conteudista, tutor, coordenador de tutoria, designer instrucional. Busque "edital professor formador UAB engenharia 2026", "edital conteudista UAB 2026".
- **Fundações de apoio em SP** (projetos com bolsa; checar quando der, filtrar pela compatibilidade):
  - FUSP — https://www.fusp.org.br (USP); AUSPIN tem seleção de bolsista em fluxo contínuo
  - FIPT — https://www.fipt.org.br (IPT; construção civil, materiais, incêndio)
  - FAI-UFSCar — editais publicados em sistemas.fai.ufscar.br (programa PACTec com IFSP, inclusive campi da capital)
  - FapUnifesp, Fundunesp, FIPE, Fundação Vanzolini, Fundação Ezute (defesa; costuma ser CLT)
- Fora de SP, só se remota: FUNDEP (UFMG), FAPEU e FEESC (UFSC), FINATEC (UnB), FAURGS (UFRGS) — fazem muitos projetos com ministérios.

## 5. Emprego privado

- LinkedIn Jobs, Gupy, Vagas.com, InfoJobs, Catho
- Páginas de carreira de construtoras, incorporadoras, gerenciadoras e consultorias de contratações públicas
- Faculdades privadas com EaD: portais de "trabalhe conosco"

### Docência em universidades privadas de SP (toda execução)

1. **Rode `python3 gupy.py`** — lê as páginas Gupy de FMU, Cogna, Yduqs, Cruzeiro do Sul, Ânima, Unicid, PUC-SP, Ibmec, UniFECAF, Ceunsp, Facens e Senac e lista as vagas de docência em SP. Abra cada link novo (fora de `vistas.txt`) e confira requisitos. Se achar outra universidade no Gupy, acrescente o subdomínio em `PAGINAS`.
2. **Mackenzie** — não usa Gupy. Editais em https://www.mackenzie.br/processos-seletivos/docente (Processo Seletivo Docente Unificado, PSDU, um por semestre; o 2026.2 já foi concluído; o próximo deve sair perto do fim do ano). Inscrição por e-mail à unidade (Escola de Engenharia: engenharia@mackenzie.br). O WebFetch corta a página; use `curl` e procure links de PDF com "Edital".
3. **UNIP e Uninove** — não usam Gupy nem publicam edital de graduação de forma visível. Busque "UNIP professor engenharia vaga" / "Uninove professor engenharia vaga" no WebSearch e em LinkedIn/Indeed.
4. **LinkedIn** — bloqueia leitura automática. Use WebSearch com `site:linkedin.com/jobs professor engenharia civil São Paulo` só para descobrir; confirme no site da instituição ou no Gupy. O que não der para abrir vai para "não verificado".
5. FEI, Mauá, FIAP, Insper, Belas Artes, São Camilo: páginas "trabalhe conosco" próprias — checar quando houver tempo.

## 6. PJ / consultoria privada

Trilha sem portal centralizado — a maior parte não aparece sem rede de contatos. Ainda assim, dá pra varrer:

- LinkedIn: posts de escritórios de advocacia da construção e engenharia buscando assistente técnico, ou de construtoras/incorporadoras buscando laudo/avaliação avulsa (sujeito a bloqueio de acesso automatizado — ver nota técnica abaixo)
- Seguradoras e resseguradoras: páginas de "credenciamento de peritos/avaliadores" (ex.: engenharia de risco, vistoria predial)
- Escritórios de advocacia especializados em direito da construção e perícia técnica: páginas de "trabalhe conosco" ou parcerias
- Associações e conselho: SindusCon-SP, CREA-SP (comunicados, editais de credenciamento privado, bolsa de oportunidades se houver)
- Comunidades técnicas: ANTAC, IBRACON, ABECE — editais de consultoria e chamadas para pareceristas
- Termos de busca úteis: "assistente técnico perícia construção", "credenciamento perito seguradora", "laudo incêndio estrutura contratar", "consultoria orçamento obras PJ"

Limite honesto: é a trilha mais fraca em cobertura automatizada. Trate como complementar — sinalize no relatório quando a varredura ficou rasa por falta de fonte, em vez de forçar resultado.

## Notas técnicas

- LinkedIn, Lattes e vários portais bloqueiam acesso automatizado. Quando o WebFetch falhar, registre no rodapé como não verificado — nunca preencha de memória.
- Diários oficiais e PDFs de edital são as fontes mais confiáveis e menos bloqueadas. Prefira-os.
