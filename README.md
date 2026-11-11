# Índice de Skills — Claude Code

Catálogo das skills disponíveis num setup real do Claude Code, com o que cada uma faz e quando ela dispara. Feito para alunos: serve para descobrir o que existe antes de sair pedindo, e para escolher o que instalar a seguir.

**Página buscável:** `docs/index.html` — abra o arquivo direto no navegador, ou publique em GitHub Pages (Settings → Pages → branch `main`, pasta `/docs`).

Levantado em 22/10/2026 e ampliado em 11/11/2026 com uma **curadoria de 38 skills, plugins e agentes** em três trilhas (alunos, arquitetura e produto, presença digital). São **35 skills ativas** — 13 da conta Anthropic, 21 nativas do Claude Code e 1 instalada na máquina — mais **33 skills em 19 plugins** do marketplace oficial, disponíveis para instalar.

---

## Curadoria — três trilhas

Revisada em 11/11/2026, depois de uma varredura nos marketplaces oficiais (`anthropics/claude-plugins-official`, com 317 plugins nessa data, e `anthropics/skills`) e em coleções da comunidade. Na página, cada item tem o comando de instalar com botão de copiar, e cada trilha tem link próprio (`#alunos`, `#arquiteto`, `#presenca`) para mandar à turma.

Skill da comunidade pode rodar código na sua máquina: leia o `SKILL.md` e os scripts antes de instalar.

### Comece por aqui — para quem está no primeiro ou segundo projeto

Em ordem: primeiro o Claude explica, depois você constrói com método, e no fim mostra o trabalho com cara de produto.

| | Item | Nível | Por que | Instalar |
| --- | --- | --- | --- | --- |
| 1 | `/init` | iniciante | O Claude lê o seu projeto e escreve o manual dele. | `/init` |
| 2 | [`learning-output-style`](https://github.com/anthropics/claude-plugins-official) ★ | iniciante | O Claude para e pede para você escrever a parte que ensina. | `/plugin install learning-output-style@claude-plugins-official` |
| 3 | [`explanatory-output-style`](https://github.com/anthropics/claude-plugins-official) | iniciante | Cada decisão vem com o porquê. | `/plugin install explanatory-output-style@claude-plugins-official` |
| 4 | [`academy-guide`](https://github.com/anthropics/skills/tree/main/skills/academy-guide) | iniciante | Toda dúvida de 'como faço' vira um curso indicado. | `/plugin marketplace add anthropics/skills` ; `/plugin install academy-guide@anthropic-agent-skills` |
| 5 | [`discernment-nudge`](https://github.com/anthropics/skills/tree/main/skills/discernment-nudge) | iniciante | Perguntas para você checar antes de confiar na resposta. | `/plugin marketplace add anthropics/skills` ; `/plugin install discernment-nudge@anthropic-agent-skills` |
| 6 | [`andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) | iniciante | Quatro regras que impedem o Claude de complicar demais. | `/plugin marketplace add forrestchang/andrej-karpathy-skills` ; `/plugin install andrej-karpathy-skills@karpathy-skills` |
| 7 | [`context7`](https://github.com/upstash/context7) | iniciante | Documentação da versão certa, sem API inventada. | `/plugin install context7@claude-plugins-official` |
| 8 | [`frontend-design`](https://github.com/anthropics/skills/tree/main/skills/frontend-design) ★ | iniciante | Da tela genérica para uma interface com cara de produto. | `/plugin install frontend-design@claude-plugins-official` |
| 9 | [`algorithmic-art`](https://github.com/anthropics/skills/tree/main/skills/algorithmic-art) ★ | iniciante | Arte generativa em p5.js a partir de uma frase. | `/plugin marketplace add anthropics/skills` ; `/plugin install example-skills@anthropic-agent-skills` |
| 10 | [`canvas-design`](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | iniciante | Pôster com direção de arte, em PNG ou PDF. | `/plugin marketplace add anthropics/skills` ; `/plugin install example-skills@anthropic-agent-skills` |
| 11 | [`commit-commands`](https://github.com/anthropics/claude-plugins-official) | iniciante | /commit escreve a mensagem; /commit-push-pr abre o PR. | `/plugin install commit-commands@claude-plugins-official` |
| 12 | `/code-review` | intermediário | Um revisor que acha o bug antes do professor. | `/code-review` |
| 13 | [`playwright`](https://github.com/microsoft/playwright-mcp) ★ | intermediário | O Claude abre o navegador e testa o que acabou de fazer. | `/plugin install playwright@claude-plugins-official` |
| 14 | [`webapp-testing`](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) | intermediário | Teste de interface escrito e rodado pelo próprio Claude. | `/plugin marketplace add anthropics/skills` ; `/plugin install example-skills@anthropic-agent-skills` |
| 15 | [`superpowers`](https://github.com/obra/superpowers) ★ | intermediário | Brainstorm, plano, TDD e depuração com método de engenheiro sênior. | `/plugin install superpowers@claude-plugins-official` |
| 16 | `/skill-creator` | intermediário | Escreva a sua primeira skill e meça se ela dispara. | `/skill-creator` |
| 17 | [`voltagent-core-dev`](https://github.com/VoltAgent/awesome-claude-code-subagents) | intermediário | Um time de subagentes para delegar trabalho. | `/plugin marketplace add VoltAgent/awesome-claude-code-subagents` ; `/plugin install voltagent-core-dev@voltagent-subagents` |
| 18 | [`frontend-slides`](https://github.com/zarazhangrui/frontend-slides) | iniciante | Apresentação animada no navegador para a entrega do projeto. | `/plugin marketplace add zarazhangrui/frontend-slides` ; `/plugin install frontend-slides@frontend-slides` |
| 19 | [`remotion`](https://github.com/remotion-dev/skills) ★ | intermediário | Vídeo feito com código React, pronto para Reels. | `npx skills add remotion-dev/skills` |
| 20 | [`web-asset-generator`](https://github.com/alonw0/web-asset-generator) | iniciante | Favicon, ícone e prévia social de uma vez. | `/plugin marketplace add alonw0/web-asset-generator` ; `/plugin install web-asset-generator@web-asset-generator-marketplace` |

### Arquitetura e produto — para quem já entrega e quer escala

Método, revisão em camadas, segurança e integração. O que separa protótipo de sistema.

| | Item | Nível | Por que | Instalar |
| --- | --- | --- | --- | --- |
| 1 | [`context7`](https://github.com/upstash/context7) | iniciante | Documentação da versão certa, sem API inventada. | `/plugin install context7@claude-plugins-official` |
| 2 | [`andrej-karpathy-skills`](https://github.com/multica-ai/andrej-karpathy-skills) | iniciante | Quatro regras que impedem o Claude de complicar demais. | `/plugin marketplace add forrestchang/andrej-karpathy-skills` ; `/plugin install andrej-karpathy-skills@karpathy-skills` |
| 3 | [`playwright`](https://github.com/microsoft/playwright-mcp) ★ | intermediário | O Claude abre o navegador e testa o que acabou de fazer. | `/plugin install playwright@claude-plugins-official` |
| 4 | [`superpowers`](https://github.com/obra/superpowers) ★ | intermediário | Brainstorm, plano, TDD e depuração com método de engenheiro sênior. | `/plugin install superpowers@claude-plugins-official` |
| 5 | `deep-research` | intermediário | Uma pesquisa com subagentes que volta com relatório e fontes. | já vem ligada |
| 6 | `/code-review` | intermediário | Um revisor que acha o bug antes do professor. | `/code-review` |
| 7 | `claude-automation-recommender` | intermediário | Diz quais hooks, skills e MCPs valem a pena neste repositório. | `/plugin install claude-code-setup@claude-plugins-official` |
| 8 | [`feature-dev`](https://github.com/anthropics/claude-plugins-official) | intermediário | Explora, desenha a arquitetura e revisa antes de você aceitar. | `/plugin install feature-dev@claude-plugins-official` |
| 9 | [`security-guidance`](https://github.com/anthropics/claude-plugins-official) | intermediário | Avisa na hora em que o código inseguro é escrito, não depois. | `/plugin install security-guidance@claude-plugins-official` |
| 10 | [`doc-coauthoring`](https://github.com/anthropics/skills/tree/main/skills/doc-coauthoring) | intermediário | Specs, PRDs e RFCs escritos a quatro mãos. | `/plugin marketplace add anthropics/skills` ; `/plugin install example-skills@anthropic-agent-skills` |
| 11 | [`voltagent-core-dev`](https://github.com/VoltAgent/awesome-claude-code-subagents) | intermediário | Um time de subagentes para delegar trabalho. | `/plugin marketplace add VoltAgent/awesome-claude-code-subagents` ; `/plugin install voltagent-core-dev@voltagent-subagents` |
| 12 | [`react-best-practices`](https://github.com/vercel-labs/agent-skills) | intermediário | As regras de React e Next.js de quem faz o Next.js. | `npx skills add vercel-labs/agent-skills` |
| 13 | `claude-security` | avançado | Um painel de agentes caça a falha e já traz o patch verificado. | `/plugin install claude-security@claude-plugins-official` |
| 14 | [`pr-review-toolkit`](https://github.com/anthropics/claude-plugins-official) | avançado | Seis revisores especialistas olhando o mesmo PR. | `/plugin install pr-review-toolkit@claude-plugins-official` |
| 15 | [`chrome-devtools-mcp`](https://github.com/ChromeDevTools/chrome-devtools-mcp) | avançado | O DevTools do Chrome, operado pelo Claude. | `/plugin install chrome-devtools-mcp@claude-plugins-official` |
| 16 | [`mcp-builder`](https://github.com/anthropics/skills/tree/main/skills/mcp-builder) | avançado | Do serviço externo ao servidor MCP, com avaliação. | `/plugin marketplace add anthropics/skills` ; `/plugin install example-skills@anthropic-agent-skills` |
| 17 | [`wshobson/agents`](https://github.com/wshobson/agents) | avançado | 94 plugins especialistas; pegue só o do seu stack. | `/plugin marketplace add wshobson/agents` ; `/plugin install python-development@claude-code-workflows` |
| 18 | [`trailofbits`](https://github.com/trailofbits/skills) | avançado | Auditoria com CodeQL e Semgrep, do jeito de quem audita para valer. | `/plugin marketplace add trailofbits/skills` ; `/plugin install static-analysis@trailofbits` |

### Presença digital — Site, LinkedIn e Instagram no mesmo tom

SEO para o Google, GEO para as IAs, a sua voz nos posts e a arte no tamanho certo.

| | Item | Nível | Por que | Instalar |
| --- | --- | --- | --- | --- |
| 1 | [`frontend-design`](https://github.com/anthropics/skills/tree/main/skills/frontend-design) ★ | iniciante | Da tela genérica para uma interface com cara de produto. | `/plugin install frontend-design@claude-plugins-official` |
| 2 | [`social-media-skills`](https://github.com/charlie947/social-media-skills) ★ | iniciante | Aprende a sua voz e escreve LinkedIn, Reels e newsletter. | `/plugin marketplace add charlie947/social-media-skills` ; `/plugin install social-media-skills@social-media-skills` |
| 3 | [`canva`](https://github.com/anthropics/claude-plugins-official) | iniciante | Peça a arte em português e receba no Canva, já no tamanho. | `/plugin install canva@claude-plugins-official` |
| 4 | [`canvas-design`](https://github.com/anthropics/skills/tree/main/skills/canvas-design) | iniciante | Pôster com direção de arte, em PNG ou PDF. | `/plugin marketplace add anthropics/skills` ; `/plugin install example-skills@anthropic-agent-skills` |
| 5 | [`theme-factory`](https://github.com/anthropics/skills/tree/main/skills/theme-factory) | iniciante | Dez temas prontos para slide, doc e página. | `/plugin marketplace add anthropics/skills` ; `/plugin install example-skills@anthropic-agent-skills` |
| 6 | [`web-asset-generator`](https://github.com/alonw0/web-asset-generator) | iniciante | Favicon, ícone e prévia social de uma vez. | `/plugin marketplace add alonw0/web-asset-generator` ; `/plugin install web-asset-generator@web-asset-generator-marketplace` |
| 7 | [`remotion`](https://github.com/remotion-dev/skills) ★ | intermediário | Vídeo feito com código React, pronto para Reels. | `npx skills add remotion-dev/skills` |
| 8 | [`marketing-skills`](https://github.com/coreyhaines31/marketingskills) ★ | intermediário | Copy, SEO, GEO e lançamento: um time de marketing em forma de skill. | `/plugin marketplace add coreyhaines31/marketingskills` ; `/plugin install marketing-skills@marketingskills` |
| 9 | [`claude-seo`](https://github.com/AgriciDaniel/claude-seo) | intermediário | Auditoria de SEO em 15 minutos, com plano priorizado. | `/plugin marketplace add AgriciDaniel/claude-seo` ; `/plugin install claude-seo@agricidaniel-claude-seo` |
| 10 | [`geo-seo-claude`](https://github.com/zubair-trabzada/geo-seo-claude) | intermediário | Seu site citado pelas IAs, não só listado no Google. | `git clone https://github.com/zubair-trabzada/geo-seo-claude.git` |

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

## Marketplace oficial — seleção de 33 skills em 19 plugins

O marketplace `anthropics/claude-plugins-official` está cadastrado na máquina, mas **nenhum plugin está instalado**. A tabela abaixo é a seleção levantada em 22/10; em 11/11/2026 o marketplace já tinha 317 plugins, e os mais úteis entraram na curadoria acima. Tudo se liga com `/plugin install <nome>@claude-plugins-official`.

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
  skills.json      os dados, uma entrada por skill, mais as trilhas — fonte única
  og.png           imagem de prévia (LinkedIn, WhatsApp), gerada
  CNAME            domínio do GitHub Pages: skills.gustavopires.dev
scripts/
  embed.py         injeta skills.json dentro de index.html
  og.py            gera docs/og.png com as contagens do skills.json
```

`docs/skills.json` é a fonte da verdade. Os campos `nome`, `origem`, `plugin`, `comando`, `grupo`, `descricao` e `quando` são obrigatórios; a curadoria acrescenta `trilhas`, `nivel` (`iniciante`, `intermediario`, `avancado`), `brilho` (a frase de impacto do card), `instalar` (lista de comandos), `fonte` e `destaque`. A origem `comunidade` marca repositório de terceiros. A página não faz `fetch` do JSON — isso quebraria ao abrir o arquivo local, porque o navegador bloqueia requisição em `file://`. Em vez disso, os dados ficam embutidos no HTML entre dois marcadores, e o `scripts/embed.py` regenera esse trecho.

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
