# Índice de Skills e Agentes — Claude Code

Catálogo das skills e dos agentes disponíveis num setup real do Claude Code, com o que cada um faz e quando usar. Feito para alunos: serve para descobrir o que existe antes de sair pedindo.

**Página buscável:** https://skills.gustavopires.dev — com link direto para os agentes em https://skills.gustavopires.dev/#agentes. Também funciona offline: abra `docs/index.html` direto no navegador.

| | Total | O que tem |
| --- | --- | --- |
| [Skills](#skills) | 68 | 35 ativas (13 da conta, 21 nativas, 1 local) + 33 em plugins do marketplace — levantadas em 22/10/2026 |
| [Agentes](#agentes) | 55 | 5 nativos + 37 em plugins do marketplace + 13 de projetos reais, anonimizados — levantados em 11/11/2026 |

---

## Skill ou agente?

As duas coisas estendem o Claude, mas rodam em lugares diferentes.

| | Skill | Agente |
| --- | --- | --- |
| Onde roda | **Dentro** da sua conversa | **Fora** dela, num Claude separado |
| Contexto | Compartilha o seu | Começa limpo, só com o que você mandar |
| O que volta | O Claude passa a seguir as instruções | Só a conclusão — o trabalho intermediário fica lá |
| Ferramentas e modelo | Os da sessão | Os que o arquivo do agente declarar |
| Arquivo | `.claude/skills/<nome>/SKILL.md` | `.claude/agents/<nome>.md` |
| Use para | Ensinar um jeito de fazer: formato, checklist, convenção | Delegar uma tarefa: busca larga, revisão independente, trabalho em paralelo |

Regra prática: se você quer que o Claude **saiba** fazer algo, é skill. Se quer que **outro** Claude faça algo e te devolva o resultado, é agente.

---

<a id="skills"></a>

# Skills

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

## Skills do marketplace oficial — 33 em 19 plugins

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

<a id="agentes"></a>

# Agentes

## O que é um agente

Um arquivo Markdown em `.claude/agents/<nome>.md`. O frontmatter diz quando ele é chamado e com o quê ele trabalha; o corpo é o prompt de sistema:

```markdown
---
name: revisor-de-testes
description: Use depois de criar ou alterar testes. Verifica se cobrem os casos de borda e se não testam só o caminho feliz.
tools: Read, Grep, Glob
model: sonnet
---

Você é um revisor de testes. Leia os testes alterados e...
```

| Campo | Obrigatório | O que faz |
| --- | --- | --- |
| `name` | sim | Como o agente é chamado |
| `description` | sim | Quando usar — é o que o Claude lê para decidir delegar, igual à skill |
| `tools` | não | Lista fechada de ferramentas. Omitido, herda todas. Dar só `Read, Grep, Glob` torna o agente somente-leitura |
| `model` | não | `haiku`, `sonnet`, `opus` ou `inherit`. Permite pôr um modelo barato numa tarefa mecânica e um forte numa revisão |

## Como usar

1. **Automático** — o Claude lê as descrições e delega quando a tarefa casa. Descrições com "Use proativamente" ou "Use ANTES de..." disparam mais.
2. **Pedindo pelo nome** — "usa o `code-explorer` para entender como o login funciona".
3. **Como agente principal da sessão** — `claude --agent <nome>`: a sessão inteira roda com o prompt e as ferramentas daquele agente.

O comando `/agents` lista, cria e edita os agentes disponíveis.

## Onde cada agente mora

| Lugar | Caminho | Alcance |
| --- | --- | --- |
| Projeto | `<projeto>/.claude/agents/<nome>.md` | Só naquele repositório — vai no git |
| Usuário | `~/.claude/agents/<nome>.md` | Todas as sessões da sua máquina |
| Plugin | instalado de um marketplace | Todas as sessões, com prefixo `<plugin>:<agente>` |

## Agentes nativos do Claude Code (5)

| Agente | O que faz | Use quando |
| --- | --- | --- |
| `general-purpose` | Uso geral, com todas as ferramentas: pesquisa, busca de código, tarefa de vários passos | Busca em que você não tem certeza de acertar o arquivo nas primeiras tentativas |
| `Explore` | Busca somente-leitura em leque largo; lê trechos e devolve só a conclusão — localiza código, não audita | A resposta exige passar por muitos arquivos e você só precisa do resultado |
| `Plan` | Arquiteto somente-leitura: plano de implementação, arquivos críticos, alternativas | Antes de uma mudança grande |
| `claude-code-guide` | Responde sobre o Claude Code, o Agent SDK e a API consultando a documentação | "Como eu faço um hook?", "o Claude Code consegue X?" |
| `statusline-setup` | Configura a linha de status | Mostrar branch, modelo ou custo na barra do terminal |

## Agentes do marketplace oficial — 37 em 10 plugins

Disponíveis, não instalados. Alguns são para você chamar; outros são **peças internas** de um fluxo maior, disparados pelo próprio plugin — vale ler mesmo assim, porque mostram como dividir um trabalho grande entre agentes especializados.

| Plugin | Agentes | O que fazem |
| --- | --- | --- |
| `feature-dev` | `code-explorer`, `code-architect`, `code-reviewer` | O ciclo de uma feature: entender o código existente, desenhar a planta (arquivos, componentes, fluxo de dados) e revisar com filtro de confiança |
| `pr-review-toolkit` | `code-reviewer`, `silent-failure-hunter`, `pr-test-analyzer`, `type-design-analyzer`, `comment-analyzer`, `code-simplifier` | Revisão de PR dividida por lente: diretrizes do projeto, erro engolido, cobertura de teste, desenho de tipos, comentário que vai apodrecer, legibilidade |
| `code-simplifier` | `code-simplifier` | Só o simplificador, como plugin isolado (`opus`) |
| `code-modernization` | `legacy-analyst`, `business-rules-extractor`, `test-engineer`, `architecture-critic`, `scaffolder`, `version-delta-analyst`, `uplift-migrator`, `security-auditor` | Modernização de legado em etapas: entender, extrair regra de negócio em Dado/Quando/Então, fixar o comportamento com teste, criticar a arquitetura nova, montar serviço, migrar versão módulo a módulo |
| `claude-security` | `claude-security` (sessão) + 8 internos: `scan-inventory`, `scan-researcher`, `scan-verifier`, `scan-redactor`, `scan-loader`, `explore`, `patch-generator`, `patch-verifier` | Uma varredura de segurança como linha de montagem: mapear, pesquisar por componente, votar achado por achado, redigir segredos, gerar e verificar patch |
| `plugin-dev` | `agent-creator`, `plugin-validator`, `skill-reviewer` | Gerar agente a partir de descrição, validar a estrutura do plugin, revisar a descrição de uma skill |
| `agent-sdk-dev` | `agent-sdk-verifier-py`, `agent-sdk-verifier-ts` | Verificam se um app do Agent SDK (Python ou TypeScript) segue as boas práticas |
| `hookify` | `conversation-analyzer` | Lê transcripts procurando comportamento que valeria bloquear com hook |
| `champion-kit` | `repo-scout` (interno) | Coletor de evidência somente-leitura: CI, `CLAUDE.md`, skills e configurações de um repositório |
| `math-proof` | `math-proof-judge`, `math-proof-worker`, `math-proof-worker-deep` (internos) | Juiz e trabalhadores do `/math-proof:siege`: o juiz planeja e mantém o livro do que está provado; os trabalhadores respondem uma pergunta cada, sem memória |

Dois padrões para notar:

- **Verificação por votação** (`claude-security`): um agente acha, vários outros votam se o achado é real. É assim que se derruba falso positivo sem um humano no meio.
- **Escrita com cerca** (`scaffolder`, `uplift-migrator`): o agente só pode escrever dentro da própria pasta. Restringir onde um agente escreve vale tanto quanto restringir que ferramentas ele tem.

## Agentes de projeto — 13 exemplos reais, anonimizados

Escritos para dois projetos de verdade: um **SaaS web multi-tenant** e um **jogo**. Os nomes e as descrições foram reescritos para mostrar o padrão, sem os detalhes do produto.

O que eles têm em comum, e o que o template padrão não ensina: **cada um tem um gatilho concreto** ("ANTES de fechar mudança em regra", "tocou em endpoint") e **um dono claro** — o auditor de segurança, por exemplo, delega isolamento de tenant ao guarda especializado em vez de duplicar a checagem.

### SaaS web multi-tenant (6)

| Agente | O que faz | Use quando |
| --- | --- | --- |
| `arquiteto-revisor` | Traça os codepaths, mapeia fluxos e estados de erro, desenha em ASCII a cobertura de testes e entrega o plano de testes; cobre migração de dados | **Antes** de implementar feature ou refatoração em mais de um arquivo |
| `guardiao-da-regra-de-negocio` | Regra de negócio na camada de serviço, views magras, frontend sem lógica de domínio, custo de query sob controle (N+1, índice, paginação) | Criou ou alterou endpoint, cálculo, transição de estado ou query pesada |
| `guarda-de-isolamento-multi-tenant` | Todo acesso filtra pelo tenant antes de buscar; RLS, soft delete, permissões. Dono do OWASP A01 no repositório | Qualquer query, permissão, job ou comando que toque dado de cliente |
| `guarda-de-contrato-de-api` | Envelope de resposta padronizado, breaking change, deriva entre os tipos do frontend e o schema OpenAPI | Tocou em endpoint, serializer, DTO ou cliente HTTP |
| `auditor-de-seguranca` | AppSec e LGPD: segredo no histórico do git, supply chain, pipeline, imagem Docker, webhook, dado pessoal | Antes de release, ou ao mexer em integração externa |
| `matador-de-friccao-de-ux` | Checklist próprio de fricção, os cinco estados por tela (carregando, vazio, erro, parcial, ok), i18n sem texto fixo, permissão refletida na interface | Criou ou alterou lista, tabela, painel, filtro, formulário ou modal |

### Jogo (7)

| Agente | O que faz | Use quando |
| --- | --- | --- |
| `auditor-de-regras` | Confere se a regra no código bate com as fontes de verdade do design (documentos e planilhas) | **Antes** de fechar mudança em regra, combate ou dados |
| `playtest-headless` | Roda a simulação sem interface e lê o resultado como design — mudou a letalidade? a duração do combate? — não só verde/vermelho | Depois de mudar regra ou dado, antes de fechar um marco |
| `pipeline-de-dados` | Valida e roda a exportação das planilhas de design para os JSON do jogo, e a carga no motor | A fonte de dados mudou, ou deu erro de carga |
| `curador-de-assets` | Livro-registro de assets: licença, proveniência, placeholder, escala | Antes de qualquer asset de terceiros entrar no projeto |
| `revisor-de-forma` | Olha prints e vídeos de um modelo 3D e diz, imagem por imagem, o que está errado em relação à referência | **Antes** de declarar uma malha pronta — métrica automática não enxerga forma |
| `diretor-de-identidade-sonora` | Briefing de compositor, especificação de cues, curadoria CC0, revisão de mixagem. Não gera áudio — regra de zero conteúdo generativo | Qualquer trabalho de áudio |
| `escriba` | Devlog e ADR (registro de decisão de arquitetura) no formato do repositório | Fim de sessão, ou ao fechar uma decisão que precisa virar ADR |

---

## Estrutura deste repo

```
README.md          este índice
docs/
  index.html       página buscável, com abas Skills e Agentes
  skills.json      as skills — fonte única
  agentes.json     os agentes — fonte única
scripts/
  embed.py         injeta os dois JSON dentro de index.html
```

Os JSON são a fonte da verdade. A página não faz `fetch` deles — isso quebraria ao abrir o arquivo local, porque o navegador bloqueia requisição em `file://`. Em vez disso, os dados ficam embutidos no HTML entre dois marcadores, e o `scripts/embed.py` regenera esse trecho.

Ou seja: **editou um JSON? rode `python scripts/embed.py`** antes de commitar. O `python scripts/embed.py --check` valida os campos e avisa se o HTML saiu de sincronia.

| Comando | O que faz |
| --- | --- |
| `python scripts/embed.py --check` | valida os JSON e confere se o HTML está sincronizado |
| `python scripts/embed.py` | injeta `skills.json` e `agentes.json` em `docs/index.html` |
| `python -m http.server 8000 --directory docs` | serve a página em http://localhost:8000 |

Não há nada a instalar: só Python 3 com a biblioteca padrão. A publicação é via GitHub Pages (branch `main`, pasta `/docs`).

## Proveniência

As descrições foram escritas a partir dos campos `name` e `description` dos `SKILL.md` e dos arquivos de agente instalados nesta máquina, e do catálogo do marketplace oficial. Os agentes de projeto foram anonimizados. Nomes e comportamentos mudam entre versões do Claude Code — confira com `/plugin`, `/agents` e a lista da sua própria sessão antes de considerar este índice atual.
