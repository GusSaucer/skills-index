# Índice de Skills — Claude Code

Catálogo das skills disponíveis num setup real do Claude Code, com o que cada uma faz e quando ela dispara. Feito para alunos: serve para descobrir o que existe antes de sair pedindo.

**Página buscável:** `docs/index.html` — abra o arquivo direto no navegador, ou publique em GitHub Pages (Settings → Pages → branch `main`, pasta `/docs`).

Levantado em 22/10/2026. São **35 skills ativas** — 13 da conta Anthropic, 21 nativas do Claude Code e 1 instalada na máquina — mais **33 skills em 19 plugins** do marketplace oficial, disponíveis para instalar.

---

## O que é uma skill

Uma pasta com um `SKILL.md` dentro. O frontmatter tem dois campos obrigatórios:

```markdown
---
name: minha-skill
description: O que faz e quando o Claude deve carregar. Este campo é o que decide o disparo — escreva os gatilhos.
---

# Minha skill

As instruções que o Claude vai seguir.
```

O Claude lê só o `name` e a `description` de cada skill no início da sessão. O corpo do `SKILL.md` entra na janela de contexto apenas quando a skill é carregada, e arquivos de apoio em `references/` só quando são realmente abertos. É assim que a `reverse-engineer-anything` consegue cobrir 170 ferramentas sem pesar.

Consequência prática: **a `description` é a parte mais importante da skill.** Se ela não nomear os gatilhos, a skill nunca dispara, não importa o quão bom seja o corpo.

## Como invocar

1. **Automático** — o Claude casa o pedido com a descrição. Na maioria dos casos é só pedir em português: "faz uma planilha com isso" dispara a `xlsx`.
2. **Por nome, com barra** — `/code-review`, `/simplify`, `/init`. Serve para forçar a skill quando o pedido não é óbvio.
3. **Com argumento** — `/code-review high`, `/loop 5m /code-review`. O que vem depois da barra é passado para a skill.

Skills de plugin levam o prefixo do plugin: `/math-proof:solo`, `/plugin-dev:skill-development`.

## Onde cada skill mora

| Lugar | Caminho | Alcance |
| --- | --- | --- |
| Projeto | `<projeto>/.claude/skills/<nome>/SKILL.md` | Só naquele repositório — vai no git, o time todo recebe |
| Usuário | `~/.claude/skills/<nome>/SKILL.md` | Todas as sessões da sua máquina |
| Plugin | instalado de um marketplace | Todas as sessões, com prefixo `<plugin>:<skill>` |

Comandos úteis: `/plugin` (gerenciar plugins), `/skill-creator` (criar a sua), `/skill-doctor` (diagnosticar skill que não dispara), `/mcp` (servidores MCP conectados).

---

## Skills da conta Anthropic (13 ativas)

Ligadas na conta, valem em qualquer sessão: app, web ou terminal.

| Skill | O que faz | Use quando |
| --- | --- | --- |
| `docs` | Cria e edita docs vivos, com comentário e exportação para Word, PDF ou Markdown | Qualquer documento para guardar, compartilhar ou assinar — relatório, proposta, contrato, currículo |
| `docx` | Lê, cria e edita arquivos Word, inclusive controle de alterações e templates `.dotx` | O formato `.docx` for exigido por nome |
| `xlsx` | Abre, corrige e gera planilhas `.xlsx`, `.csv`, `.tsv`, com fórmulas e gráficos | O entregável for uma planilha, ou houver dado tabular sujo para limpar |
| `pptx` | Lê e monta apresentações PowerPoint, com layouts, notas e comentários | Pedirem `.pptx` por nome |
| `pdf` | Extrai texto e tabelas, junta, divide, rotaciona, preenche formulário, faz OCR | Qualquer tarefa com PDF |
| `google-workspace` | Cria e altera Google Docs, Sheets, Slides e arquivos no Drive | O pedido citar Google, ou vier um link `docs.google.com` |
| `deep-research` | Coordena subagentes de pesquisa e entrega um relatório narrativo com fontes | Comparar opções, revisar literatura, entender um mercado |
| `built-in-browser` | Regras do navegador embutido no app — abas, login persistente, leitura de página como texto | Antes do primeiro passo no navegador do próprio Claude |
| `chrome-browser` | Regras da extensão Claude in Chrome, que age no Chrome real com seus logins | Antes do primeiro passo no seu Chrome |
| `computer-use` | Regras do controle de desktop — print de tela, clique, digitação em apps locais | Mexer em um app do computador ou olhar a tela |
| `morning` | Monta o briefing matinal como página HTML, ou agenda como tarefa recorrente | Pedir ou configurar o `/morning` |
| `import-memory` | Importa um export de memória de outro assistente para a memória do Claude | Migrar de outra ferramenta de IA |
| `skill-creator` | Cria, edita e mede skills, com testes de disparo e análise de variância | Escrever a sua própria skill |

## Skills nativas do Claude Code (21)

Já vêm com o app — não precisa instalar nada. As de código e automação são as mais úteis no dia a dia.

| Skill | O que faz | Use quando |
| --- | --- | --- |
| `/code-review` | Revisa o diff atual, um PR, branch ou caminho, procurando bugs de corretude. Níveis `low` a `max`; `ultra` roda revisão multiagente na nuvem | Antes de abrir ou de aprovar um PR |
| `/simplify` | Revisa o código alterado procurando reuso, simplificação e eficiência, e aplica as correções | Terminou de implementar e quer limpar |
| `/security-review` | Revisão de segurança das alterações pendentes na branch | Mexeu em autenticação, permissão ou entrada de usuário |
| `/init` | Gera um `CLAUDE.md` inicial documentando o repositório | Abrir um projeto no Claude Code pela primeira vez |
| `/run` | Sobe e opera o app do projeto para ver a mudança funcionando de verdade | Quer prova visual, não só teste passando |
| `dataviz` | Método de design para qualquer gráfico, painel ou KPI: paleta acessível, escolha de marca, regras de interação | Antes da primeira linha de código de gráfico, em qualquer biblioteca |
| `artifact-design` | Fundamentos de design de Artifacts: título, tema claro/escuro, layout, bibliotecas, limites | Antes de escrever qualquer página de Artifact |
| `artifact-diagramming` | Como desenhar um diagrama que mostra o mecanismo real, em SVG legível nos dois temas | A página precisa de um desenho que explique algo |
| `artifact-capabilities` | Capacidades de runtime de um Artifact publicado: ler dados ao vivo, guardar estado compartilhado, saber quem está vendo, arquivos, câmera | A página precisa lembrar o que as pessoas fizeram nela |
| `update-config` | Configura o `settings.json`: hooks, permissões, variáveis de ambiente | Quer automação do tipo "sempre que X, faça Y" |
| `keybindings-help` | Personaliza atalhos de teclado em `~/.claude/keybindings.json` | Remapear teclas ou criar atalho em acorde |
| `fewer-permission-prompts` | Varre seus transcripts e monta uma allowlist priorizada no `settings.json` do projeto | Está cansado de aprovar o mesmo comando |
| `plugin-authoring` | Cria, altera e depura um mod: painel lateral, status line, slash command, hook em chamada de ferramenta | Quer mudar a própria interface do Claude |
| `workflow-authoring` | Referência para escrever um script da ferramenta Workflow, com API, retomada e padrões de qualidade | Vai orquestrar vários subagentes de forma determinística |
| `/loop` | Roda um prompt ou slash command em intervalo recorrente, ou com ritmo decidido pelo modelo | "Checa o deploy a cada 5 minutos" |
| `/schedule` | Cria e gerencia agentes de nuvem que rodam em cron, ou uma execução única agendada | Quer uma rotina que roda sem você estar presente |
| `schedule` (app) | Cria ou atualiza tarefa agendada do próprio app | "Todo dia de manhã", "me lembra em uma hora" |
| `claude-api` | Referência da API da Anthropic: IDs de modelo, preços, streaming, tool use, MCP, cache, contagem de tokens | Qualquer pergunta sobre modelo, preço ou limite — nunca responder de memória |
| `consolidate-memory` | Passa pelos arquivos de memória: funde duplicatas, corrige fato velho, poda o índice | A memória cresceu e começou a conflitar |
| `explain-usage` | Explica para onde foram os tokens da sessão, com um gráfico simples | "Por que essa sessão custou tanto?" |
| `setup-claude` | Setup guiado: instala plugins conforme seu papel, conecta ferramentas, testa uma skill | Primeiro dia de alguém no Claude Code |

## Skill instalada localmente (1)

Fica em `~/.claude/skills/` e vale em todas as sessões da máquina.

| Skill | O que faz | Use quando |
| --- | --- | --- |
| `reverse-engineer-anything` | Engenharia reversa com o REA: binário nativo, código gerenciado, Electron/JavaScript, pacote, firmware e navegador. Descompila, compara versões, explica feature a partir de evidência do artefato distribuído | A afirmação depende de um binário distribuído, de descompilação ou de evidência de runtime — **não** para análise de repositório com código-fonte completo |

Traz seis arquivos de referência (aplicações Android, JavaScript, nativas, observação de runtime, fluxos de evidência, recuperação de conexão) e expõe cerca de 170 ferramentas via servidor MCP. Instalar a skill não registra o servidor — isso é um passo separado.

## Marketplace oficial — 33 skills em 19 plugins

O marketplace `anthropics/claude-plugins-official` está cadastrado na máquina, mas **nenhum plugin está instalado**. O catálogo abaixo é o que dá para ligar com `/plugin install <nome>`.

| Plugin | Skills que traz | O que faz |
| --- | --- | --- |
| `plugin-dev` | `plugin-structure`, `command-development`, `agent-development`, `skill-development`, `hook-development`, `mcp-integration`, `plugin-settings` | O kit completo para criar plugin de Claude Code: estrutura de pasta, manifesto, slash commands, subagentes, skills, hooks, integração MCP e configuração por projeto |
| `mcp-server-dev` | `build-mcp-server`, `build-mcp-app`, `build-mcpb` | Constrói servidor MCP de ponta a ponta: escolhe o modelo de deploy, adiciona widget de UI interativa e empacota como `.mcpb` instalável |
| `claude-security` | `claude-security` | Varre o repositório, o diff da branch ou um PR procurando falha de segurança, e gera patches verificados por um painel de agentes |
| `claude-code-setup` | `claude-automation-recommender` | Analisa o código e recomenda que hooks, subagentes, skills, plugins e MCPs valem a pena naquele projeto |
| `claude-md-management` | `claude-md-improver` | Audita todos os `CLAUDE.md` do repositório, pontua contra templates e aplica correções |
| `frontend-design` | `frontend-design` | Direção estética para UI nova: tipografia, hierarquia visual, escolhas que não parecem template |
| `playground` | `playground` | Gera playground HTML autocontido: controles visuais, preview ao vivo e um prompt para copiar |
| `project-artifact` | `project-artifact` | Publica página de status do projeto com abas (visão geral, workstreams, próximos passos, riscos, decisões), e atualiza a mesma URL reportando só o delta |
| `receipts` | `receipts` | Monta relatório de uso e impacto a partir dos transcripts locais, cruzando com o histórico do git — serve para justificar o gasto |
| `session-report` | `session-report` | Relatório HTML explorável do uso da sessão: tokens, cache, subagentes, skills, prompts caros |
| `hookify` | `writing-hookify-rules` | Sintaxe e padrões para escrever regra de hook |
| `skill-creator` | `skill-creator` | Mesma skill que já está ativa na conta — criar, editar e medir skills |
| `math-proof` | `solo`, `siege` | Ataca um problema de matemática difícil e entrega um `proof.md`: `solo` sozinho em estágios, `siege` em rodadas com juiz e trabalhadores independentes (leva horas) |
| `math-olympiad` | `math-olympiad` | Problemas de olimpíada de matemática |
| `cwc-makers` | `m5-onboard`, `cardputer-buddy` | Placa M5Stack/ESP32: detecta no USB, grava firmware UIFlow 2.0, instala o bundle MicroPython e depois itera app por app sem regravar |
| `telegram` | `configure`, `access` | Liga o Claude a um canal do Telegram: salva o token do bot e controla quem pode falar |
| `discord` | `configure`, `access` | O mesmo para Discord: token, allowlist, política de DM e grupo |
| `imessage` | `configure`, `access` | O mesmo para iMessage: status do canal e política de acesso |
| `example-plugin` | `example-skill`, `example-command` | Template de referência: mostra o layout `skills/<nome>/SKILL.md` e as opções de frontmatter |

---

## Estrutura deste repo

```
README.md          este índice
docs/
  index.html       página buscável (GitHub Pages serve daqui)
  skills.json      os dados, uma entrada por skill — fonte única
  og.png           imagem de prévia (LinkedIn, WhatsApp), gerada
  CNAME            domínio do GitHub Pages: skills.gustavopires.dev
scripts/
  embed.py         injeta skills.json dentro de index.html
  og.py            gera docs/og.png com as contagens do skills.json
```

`docs/skills.json` é a fonte da verdade. A página não faz `fetch` do JSON — isso quebraria ao abrir o arquivo local, porque o navegador bloqueia requisição em `file://`. Em vez disso, os dados ficam embutidos no HTML entre dois marcadores, e o `scripts/embed.py` regenera esse trecho.

Ou seja: **editou o `skills.json`? rode `python scripts/embed.py`** antes de commitar. O `python scripts/embed.py --check` avisa se os dois saíram de sincronia.

| Comando | O que faz |
| --- | --- |
| `python scripts/embed.py --check` | valida o JSON e confere se o HTML está sincronizado |
| `python scripts/embed.py` | injeta `skills.json` em `docs/index.html` |
| `python scripts/og.py` | regenera a imagem de prévia `docs/og.png` (precisa de Pillow) |
| `python -m http.server 8000 --directory docs` | serve a página em http://localhost:8000 |

Não há nada a instalar: só Python 3 com a biblioteca padrão. A publicação é via GitHub Pages (branch `main`, pasta `/docs`).

## Licença e proveniência

As descrições foram escritas a partir dos campos `name` e `description` dos `SKILL.md` instalados nesta máquina e do catálogo do marketplace oficial, em 22/10/2026. Nomes e comportamentos de skill mudam entre versões do Claude Code — confira com `/plugin` e com a lista de skills da sua própria sessão antes de considerar este índice atual.
