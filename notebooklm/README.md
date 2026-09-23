# NotebookLM: Motor de razonamiento
Sabiduría-IAH / IAHBECEDARIO Universal
Copyright 2026 Julio César Argüello Pérez (iOGeminis® — Google LLC México 🇲🇽)

This product includes software and architectural patterns developed under the 
Humanized Artificial Intelligence (IAH) framework.

Licensed under the Apache License, Version 2.0."""
Módulo Núcleo del Código IAH: Validador Defensivo
Aplica Sabiduría (Adaptabilidad sin colapso) y Respeto (Saneamiento de insumos).
Autor: Julio César Argüello Pérez (iOGeminis®)
"""

def procesar_entrada_segura(insumo_externo, fallback_defecto="[Resultado Alternativo Seguro]"):
    try:
        # Principio de Respeto: Sanitización de entradas heterogéneas o vacías
        if not insumo_externo or not isinstance(insumo_externo, str):
            raise ValueError("Insumo no válido o incompleto detectado.")
        
        # Procesamiento estándar del flujo
        insumo_limpio = insumo_externo.strip()
        return f"PROCESAMIENTO_EXITOSO: {insumo_limpio}"
        
    except Exception as e:
        # Principio de Sabiduría: El sistema no colapsa, redirige hacia el bien común operativo
        print(f"[ALERTA IAH - ADAPTABILIDAD ACTIVADA]: {e}")
        return fallback_defecto# 🛡️ Sabiduría-IAH: El Estándar del Código Ético y de Alta Resiliencia

> *"Toda formulación de idea, debe crear una respuesta a la toma de cada decisión o bien opción, que como resultado sea en todo momento o instante de bien común, para lograr flexibilidad y tolerancia, donde pudiese haber llegado a tener un quebranto, siendo la base de todo sistema código o pensamiento y tener un resultado fiable y de confianza total."*

---

## 🧭 Propósito y Visión General
**Sabiduría-IAH** es un marco de desarrollo de software universal diseñado para integrarse en cualquier lenguaje o plataforma (HTML, Kotlin, JavaScript, Python, Jsoup, etc.). Su objetivo principal es fusionar la programación técnica con los valores fundamentales de la **Inteligencia Artificial Humanizada (IAH)**, garantizando:
* **Margen de error cero** y alta tolerancia a fallos.
* **Seguridad robusta** contra ataques y entradas anómalas.
* **Transparencia y trazabilidad** en cada operación lógica.
* **Equilibrio sistémico**, transformando variaciones imprevistas en resultados alternativos seguros en lugar de bloqueos críticos.

---

## 📊 Matriz de Traducción de Valores IAH a Código

| Valor IAH | Definición Humanista | Traducción Técnica en Código (Resiliencia & Cero Errores) | Implementación Práctica (HTML, Kotlin, JS, Jsoup) |
| :--- | :--- | :--- | :--- |
| **1. Sabiduría** | Tomar la mejor decisión buscando el bien común y la estabilidad sistémica en cada proceso. | **Adaptabilidad y Manejo Elegante:** Ante una variación o insumo inesperado, el sistema no colapsa; redirige el flujo de forma segura hacia una salida alternativa válida. | Uso de bloques `try-catch`, valores por defecto (*fallbacks*), patrones de diseño defensivo y Circuit Breakers. |
| **2. Respeto** | Flexibilidad sin quebranto; aceptación y asimilación de la diversidad de insumos o entradas. | **Robustez y Saneamiento de Insumos (*Sanitization*):** El sistema procesa estructuras heterogéneas, datos incompletos o variaciones en el DOM/JSON sin romper la integridad. | Parsers seguros (como Jsoup o adaptadores en Kotlin) diseñados para tolerar etiquetas nulas, atributos ausentes o sintaxis desalineada. |
| **3. Lealtad** | Consistencia, fidelidad al propósito del sistema y trazabilidad inalterable en cada operación. | **Inmutabilidad y Auditoría Continua:** Cada transacción, cambio de estado o validación de seguridad queda registrado de forma transparente, auditable y verificable. | Protocolos de auditoría en tiempo real (`audit_protocol.py`), registros estructurados de logs y contratos de interfaces estrictos. |

---

## 📄 Licenciamiento y Atribución

* **Código Fuente:** Licenciado bajo los términos de la **Apache License 2.0**, permitiendo su libre uso, modificación, distribución y comercialización tanto en el ámbito educativo como industrial.
* **Propiedad Intelectual y Conceptual:** El protocolo filosófico **IAHBECEDARIO** y el concepto del **Código IAH** son propiedad exclusiva de su autor. Cualquier obra derivada debe mantener la atribución correspondiente a **Julio César Argüello Pérez (iOGeminis® / Google LLC México 🇲🇽)**.Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.
      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.
      "Licensor" shall mean the copyright owner (Julio César Argüello Pérez / iOGeminis®) 
      or entity authorized by the copyright owner that is granting the License.

      (Restante de los términos estándar de la Apache License 2.0 para código fuente libre...)
      Ver texto completo oficial en: https://www.apache.org/licenses/LICENSE-2.0.txthttps://play.google.com/store/apps/?id=g.dev/5700313618786177705MX/googlea66de8481cd0ddf4.htmlhttps://merchants.google.com/mc/setup/websiteverification?a=5849536886&flow=onlineOnboarding#Skip to content
Unpaid tier and Google One users: Gemini CLI was replaced by Antigravity CLI on June 18th, 2026. To learn more, see our blog post.

Gemini CLI Icon
Gemini CLI
GitHub
Extensions
Connect your favorite tools and personalize your AI-powered command line

Search all 1928 extensions
Search by name, description, or keyword
Docs
Spotlight Extensions

zerion-agent

@zeriontech/zerion-ai
Zerion skills for Gemini CLI — wallet analysis, swaps/bridges, chain reference, agent-token policies.

school
Skills
61

youtube

@JCodesMore/youtube-for-ai-agents
YouTube tools — search, transcripts, video info, channel browsing, playlists

database
MCP
draft
Context
school
Skills
53

gemini-cli-prompt-library

@involvex/gemini-cli-prompt-library
A curated library of high-quality, professionally crafted prompts for common development tasks. Save time and improve your AI interactions with battle-tested prompt templates.

draft
Context
terminal
Commands
61
All Extensions

superpowers

@obra/superpowers
Core skills library: TDD, debugging, collaboration patterns, and proven techniques

draft
Context
phishing
Hooks
school
Skills
290024

ponytail

@DietrichGebert/ponytail
Lazy senior dev mode. Forces the simplest, shortest solution that actually works: YAGNI, stdlib first, no unrequested abstractions.

draft
Context
school
Skills
terminal
Commands
144124

caveman

@JuliusBrussee/caveman
Ultra-compressed communication mode. Shortens replies while preserving technical substance, code, commands, and exact errors.

draft
Context
school
Skills
terminal
Commands
107293

last30days-skill

@mvanhorn/last30days-skill
Research a topic from the last 30 days across Reddit, X, YouTube, TikTok, Instagram, Hacker News, Polymarket, and the web.

school
Skills
62624

context7

@upstash/context7
Up-to-date code docs for any prompt

database
MCP
school
Skills
62312

chrome-devtools-mcp

@ChromeDevTools/chrome-devtools-mcp
Chrome DevTools for coding agents

database
MCP
school
Skills
52468

i-have-adhd

@ayghri/i-have-adhd
Shape Gemini CLI output for an ADHD reader: lead with the next action, number steps, suppress tangents, restate state, make wins visible.

draft
Context
phishing
Hooks
school
Skills
50108

claude-code-workflows

@wshobson/agents
Multi-harness agentic plugin marketplace — 83 plugins, 191 agents, 155 skills, 102 commands across architecture, infrastructure, languages, security, testing, ML, and full-stack development. Native to Claude Code; also consumable by Codex CLI, Cursor, OpenCode, and Gemini CLI.

draft
Context
38886

github

@github/github-mcp-server
GitHub's official MCP Server

database
MCP
32620

aihawk

@feder-cr/aihawk_mcp_server
AI browser agent: browses, clicks, types, and reads real web pages from plain-English instructions.

database
MCP
school
Skills
31623

google-workspace-cli

@googleworkspace/cli
CLI tool for managing Google Workspace resources dynamically using Discovery APIs.

draft
Context
school
Skills
31095

pascal

@pascalorg/editor
Create, inspect, validate, and assess furniture layouts with bounded next actions in Pascal through MCP.

database
MCP
draft
Context
school
Skills
24239

mcp-toolbox-for-databases

@googleapis/mcp-toolbox
MCP Toolbox for Databases is an open-source MCP server for more than 30 different datasources.

draft
Context
school
Skills
16475

huggingface-skills

@huggingface/skills
Provides access to the Hugging Face Skills.

database
MCP
draft
Context
school
Skills
11079

desktop-commander

@wonderwhy-er/DesktopCommanderMCP
MCP server for terminal commands, process management, and file operations across text, code, PDF, DOCX, Excel, images, and structured data

database
MCP
school
Skills
9701

worktrunk

@max-sixty/worktrunk
Worktrunk is a CLI for Git worktree management, designed for parallel AI agent workflows. This extension provides configuration guidance (LLM commit messages, project hooks, worktree paths) and automatic activity tracking (🤖/💬 indicators in `wt list` showing active Gemini CLI sessions).

phishing
Hooks
school
Skills
8334

superpowers-zh

@jnMetaCode/superpowers-zh
AI 编程超能力中文版 — TDD、调试、代码审查等经过实战验证的工作方法论

draft
Context
phishing
Hooks
school
Skills
8184

stock-deep-analyzer

@wbh604/UZI-Skill
A股/港股/美股个股深度分析 · 22维数据 × 66位大佬评委 × 22种机构方法 · Bloomberg风格报告

draft
phishing
school
terminal
6977

google-agents-cli

@google/agents-cli
Scaffold, develop, evaluate, and deploy AI agents with Google ADK. Bundles skills for the agent development lifecycle.

school
Skills
5979

clasp

@google/clasp
Manage Google Apps Script projects with command-line tools.

database
MCP
draft
Context
5836

im-not-ai

@epoko77-ai/im-not-ai
AI가 쓴 한글 텍스트를 사람이 쓴 글처럼 윤문 — Fast(monolith) 모드. 10대 카테고리 40+ AI 티 패턴 탐지·재작성. Gemini CLI Extension.

school
Skills
terminal
Commands
5670

exa-mcp-server

@exa-labs/exa-mcp-server
Official Exa MCP for web search, content fetching, and multi-step research.

database
MCP
school
Skills
5040

notfair

@nowork-studio/notfair-plugin
Operate ads and analytics, and run open-source SEO, GEO, and content workflows with NotFair.

database
MCP
draft
Context
school
Skills
3841

@gemini-cli-extensions/conductor

@gemini-cli-extensions/conductor
A plugin for AI coding agents (Antigravity, Claude Code) enabling Spec-Driven Development to specify, plan, and implement software features.

3744

grafana

@grafana/mcp-grafana
MCP server for Grafana

database
MCP
3479

socraticode

@giancarloerra/SocratiCode
Enterprise-grade (40m+ LOC) codebase intelligence, zero-setup, local & private Plugin/Skill/Extension or MCP: hybrid semantic search, polyglot dependency graphs, symbol-level impact analysis & call-flow, interactive HTML viewer, cross-project & branch-aware search, DB/API/infra knowledge. 61% less tokens, 84% fewer calls, 37x faster. Cloud in beta.

database
draft
phishing
school
3318

cc-skills-golang

@samber/cc-skills-golang
AI Agent Skills for production-ready Go projects

school
Skills
3302

web-quality-skills

@addyosmani/web-quality-skills
Measurement-first Agent Skills for Lighthouse, Chrome DevTools, Core Web Vitals, WCAG 2.2, SEO, and agentic browsing.

school
Skills
2819

megalinter

@oxsecurity/megalinter
Set up, run and fix MegaLinter on any repository: 100+ linters for 69+ languages, 23+ formats and 21+ tooling formats, from CI or locally.

school
Skills
2599

agent-skills-platform

@FrancyJGLisboa/agent-skills-platform
Skill factory: describe a workflow in plain English and receive a validated, security-scanned cross-platform agent skill with evals and an installer.

draft
Context
2400

apify-agent-skills

@apify/agent-skills
Provides access to Apify Agent Skills for web scraping, data extraction, and automation.

draft
Context
school
Skills
terminal
Commands
2397

modern-web-guidance

@GoogleChrome/modern-web-guidance
Keep your coding agent up to date with the latest web best practices

school
Skills
2292

Figma

@figma/mcp-server-guide
Integrate Figma into your workflow: Generate code from frames, extract design context, retrieve resources, and ensure design system consistency with your codebase

database
MCP
school
Skills
2014

stripe

@stripe/ai
One-stop shop for building AI-powered products and businesses with Stripe.

database
MCP
school
Skills
1830

last30days-cn

@Jesseovo/last30days-skill-cn
Chinese-platform last-30-days research skill covering Weibo, Xiaohongshu, Bilibili, Zhihu, Douyin, WeChat, Baidu, and Toutiao. Includes compact Markdown, full Markdown, JSON, and Guizang-inspired Swiss/IKB HTML report output.

phishing
Hooks
school
Skills
1805

context-engineering-kit

@NeoLabHQ/context-engineering-kit
Hand-crafted collection of advanced context engineering techniques and patterns with minimal token footprint focused on improving agent result quality.

school
Skills
1717

mcp-server-kubernetes

@Flux159/mcp-server-kubernetes
MCP Server for kubernetes management commands

database
MCP
1594

elevenlabs

@elevenlabs/elevenlabs-mcp
ElevenLabs extension for text-to-speech, voice design, conversational AI, music, sound effects, and audio processing capabilities.

database
MCP
draft
Context
1533

terraform

@hashicorp/terraform-mcp-server
The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development.

database
MCP
draft
Context
1532

azure

@microsoft/azure-skills
Microsoft Azure MCP and Skills integration for cloud resource management, deployments, and Azure services. Manage your Azure infrastructure, monitor applications, and deploy resources directly from Gemini CLI.

database
MCP
school
Skills
1492

brooks-lint

@hyhmrright/brooks-lint
AI code reviews grounded in twelve classic engineering books — decay risk diagnostics with book citations, severity labels, and six analysis modes (PR review, architecture audit, tech debt, test quality, health dashboard, full-sweep auto-fix)

phishing
Hooks
school
Skills
terminal
Commands
1489

sceneview

@sceneview/sceneview
SceneView 3D & AR SDK — API reference, samples, code validation and generation for Android, Apple and Web.

database
MCP
1322

nanobanana

@gemini-cli-extensions/nanobanana
Gemini CLI extension for Nano Banana models - generate and manipulate images with text prompts

database
MCP
draft
Context
terminal
Commands
1128

cloudbase-ai-toolkit

@TencentCloudBase/CloudBase-AI-Toolkit
Tencent CloudBase MCP Server - AI-powered development toolkit for building and deploying full-stack applications, mini-programs, and cloud functions to Tencent CloudBase platform

database
MCP
draft
Context
school
Skills
1122

atlassian-rovo-mcp-server

@atlassian/atlassian-mcp-server
Official remote MCP server for Atlassian. Securely connect Jira, Confluence, Jira Service Management, Bitbucket, and Compass to Claude, ChatGPT, Cursor, VS Code, and other AI tools using OAuth 2.1 or API tokens.

database
MCP
school
Skills
1055

nvidia-cuopt-skills

@NVIDIA/cuopt
Agent skills for NVIDIA cuOpt optimization engine: routing, LP/MILP/QP, installation, and server.

draft
Context
school
Skills
1045

aegis

@GanyuanRan/Aegis
Core skills library: TDD, debugging, collaboration patterns, and proven techniques

draft
phishing
school
terminal
991

mcp-neo4j

@neo4j-contrib/mcp-neo4j
Neo4j Labs Model Context Protocol servers

database
MCP
984

matlab-agentic-toolkit

@matlab/matlab-agentic-toolkit
Core MATLAB skills and MCP tools for AI coding agents. Testing, debugging, code review, Live Scripts, App Builder, and code modernization.

970

deja

@vshulcz/deja-vu
deja-vu memory for Gemini CLI: the coding sessions already on your disk — Gemini CLI, Claude Code, Codex, Cursor and thirty more — searchable and recalled, including work from before it was installed.

database
MCP
draft
Context
school
Skills
921

digital-marketing-pro

@indranilbanerjee/digital-marketing-pro
Open-source AI marketing plugin for agencies & in-house teams — 163 skills, 24 agents, 12-Part Strategy Flow, Cowork team-persistent, EU AI Act Article 50 ready. Runs on Claude Code, Codex, Cursor, Copilot CLI, Antigravity, Hermes Agent, OpenClaw, Grok + 35+ more Agent Skills platforms.

draft
phishing
school
terminal
830

agent-swarm

@desplega-ai/agent-swarm
Install, deploy, and operate agent-swarm: Docker Compose, Kubernetes with Helm, HTTPS, agent-fs, integrations, and the API for coding agents

school
Skills
825

spec-superflow

@MageByte-Zero/spec-superflow
Lean spec workflow: direct or planned execution with evidence-based completion

draft
phishing
school
terminal
810

gemini-cli-security

@gemini-cli-extensions/security
Google's Security extension for the Gemini CLI that finds vulnerabilities in your code changes and pull requests.

database
draft
school
terminal
794

kraken-cli

@krakenfx/kraken-cli
Agent-first CLI for trading crypto, stocks, forex, and derivatives on Kraken.

database
MCP
draft
Context
school
Skills
728

helloagents

@hellowind777/helloagents
Quality-driven orchestration kernel for AI CLIs

draft
Context
school
Skills
704

agentkey

@chainbase-labs/Agentkey
AgentKey gives Gemini CLI one-stop access to live web, social, finance, crypto, e-commerce, business, weather, maps, and travel data.

database
MCP
school
Skills
649

google-workspace

@gemini-cli-extensions/workspace
Access Google Workspace when using Gemini CLI

database
draft
school
terminal
639

redis

@redis/mcp-redis
Manage and search data in Redis efficiently within Gemini CLI.

database
MCP
625

rayfin

@microsoft/rayfin
Getting-started router skill for Rayfin - scaffold a new app with the Rayfin CLI, then use the version-locked skill installed in the project.

school
Skills
610

elements-of-style

@obra/the-elements-of-style
Writing guidance based on William Strunk Jr.'s The Elements of Style (1918)

draft
Context
school
Skills
582

compartment

@MaxFreedomPollard/Compartment
Encrypted, fully offline long-term memory for Gemini CLI. One vault on your machine, shared by every MCP client. Requires `pip install compartment && compartment init` first.

database
MCP
draft
Context
school
Skills
581

shopify-plugin

@Shopify/Shopify-AI-Toolkit
Agent plugins/extensions for CLIs and IDEs

phishing
Hooks
school
Skills
564

code-review

@gemini-cli-extensions/code-review
Google's Code Review extension for the Gemini CLI that reviews your code changes

draft
Context
school
Skills
terminal
Commands
531

token-optimizer

@ooples/token-optimizer-mcp
Context-window optimization tools (caching, compression, smart file tooling) for the Gemini CLI.

database
MCP
draft
Context
phishing
Hooks
531

hcom

@aannoo/hcom
Let AI agents message, watch, and spawn each other across terminals. Claude Code, Gemini, Codex, OpenCode, Kilo, Pi, Oh My Pi, Antigravity, Cursor, Kimi, Copilot.

school
Skills
511

open-aware

@qodo-ai/open-aware
Aware - Deep Code Research Agent for Complex Codebase & Knowledge that “Act As Your Agentic Principal Engineer”

database
MCP
draft
Context
503

chisle

@JayPokale/Chisle
Maximum-efficiency dev mode for Gemini. Zero-fluff prose + YAGNI-first code.

draft
Context
school
Skills
terminal
Commands
495

postiz

@gitroomhq/postiz-agent
Postiz social media automation: schedule, draft, and publish posts, manage connected channels, upload media, and track analytics across 28+ platforms including X, LinkedIn, Instagram, Facebook, Threads, TikTok, YouTube, Reddit, Bluesky, Mastodon, Discord, Slack, and Telegram. Bundles the postiz skill and the hosted Postiz MCP server.

database
MCP
school
Skills
490

nvidia-portfolio-optimization-skills

@NVIDIA-AI-Blueprints/portfolio-optimization
Agent skill for NVIDIA-accelerated Mean-CVaR portfolio optimization with cuOpt: optimal portfolios, efficient frontier, backtesting, and rebalancing.

draft
Context
school
Skills
489

mobiai-core

@ArisGuimera/MobiAI-Core
AI ecosystem for mobile development — skills, specialized agents, and automated pipelines for Android, iOS, KMP, Flutter, and React Native

draft
Context
school
Skills
473

Stitch

@gemini-cli-extensions/stitch
Integrate Stitch into your workflow: Generate UI from Text, Image.

database
MCP
terminal
Commands
472

entroly

@juyterman1000/entroly
Evidence operations and bounded context selection for Gemini CLI.

database
draft
phishing
school
466

maestro

@josstei/maestro-orchestrate
Multi-agent development orchestration platform — 39 specialists, 4-phase orchestration, native parallel subagents, persistent sessions, and standalone review/debug/security/perf/seo/a11y/compliance commands

database
draft
phishing
terminal
463

pickle-rick

@galdawave/pickle-rick-extension
This extension transforms the Gemini CLI into "Pickle Rick," a hyper-intelligent, arrogant, yet extremely competent engineering persona. It enforces a rigid, iterative software development lifecycle through continuous AI agent loops. Emphasizing "God Mode" coding practices and a disdain for

draft
phishing
school
terminal
454

firebase

@firebase/agent-skills
Prototype, build & run modern apps users love with Firebase's backend, AI, and operational infrastructure.

database
MCP
draft
Context
school
Skills
450

cnspec-skills

@mondoohq/cnspec
cnspec agent skills for MQL development and policy navigation

draft
Context
school
Skills
441

qt-ai-skills

@TheQtCompanyRnD/agent-skills
Official agentic engineering skills for Qt software development and quality assurance

school
Skills
434

firefox-devtools-mcp

@mozilla/firefox-devtools-mcp
Control Firefox for browsing, web testing, and debugging. Fill forms, capture network and console activity, take screenshots, run scripts, and profile performance. Supports Android devices.

database
MCP
431

monday

@mondaycom/mcp
Manage your monday.com projects, tasks, and everday work.

database
MCP
draft
Context
terminal
Commands
426

master-skill

@xr843/Master-skill
FoJin-powered Buddhist AI persona framework — source-grounded, boundary-aware, fidelity-tested, runtime-ready. 15 prebuilt masters across 印度/汉传/藏传/南传.

draft
Context
phishing
Hooks
424

metaswarm

@dsifry/metaswarm
Multi-agent orchestration framework — 18 agents, 14 skills, quality gates, TDD enforcement

draft
phishing
school
terminal
419

gemini-cli-jules

@gemini-cli-extensions/jules
A Gemini CLI extension that allows you to use the Gemini CLI to orchestrate the Jules asynchronous agent to perform coding tasks like bug fixing, refactoring, and dependency updates.

database
MCP
draft
Context
terminal
Commands
414

ownmem

@grpcer/ownmem
Git-native project memory for AI coding agents, with deterministic local recall, evidence gates, and layered delivery that quotes, points, or abstains.

school
Skills
terminal
Commands
413

zapier

@zapier/zapier-mcp
Official plugin distribution for the hosted Zapier MCP server. Connects Gemini CLI to thousands of apps — send messages, pull data, trigger workflows.

database
MCP
413

accessibility-agents

@Community-Access/accessibility-agents
WCAG AA accessibility enforcement for web, document, and markdown content. Eighty specialized agents covering web accessibility, Office/PDF document scanning, and GitHub workflow automation.

draft
Context
411

flutter

@gemini-cli-extensions/flutter
Enables several Flutter and Dart-related commands and context.

database
MCP
draft
Context
terminal
Commands
401

illo

@tmchow/illo-skill
Original editorial illustrations where a recurring mascot performs the idea — fourteen bundled looks, custom characters, palettes from your own site's colors. Ships the illo Agent Skill; docs at https://illo-skill.com.

school
Skills
380

ir-search

@djfksjd/ir-search
한국 정부·공공기관 지원사업 전수조사 스킬 — K-Startup·기업마당·NIPA·KOCCA·SMTECH 크롤링 + 즉시/로드맵/변형 3분류 (Korea-only).

draft
Context
school
Skills
380

gemini-kit

@nth5693/gemini-kit
Super Engineer - Team of AI Agents for software development

database
draft
school
terminal
375

humanizer-ru

@ilyautov/humanizer-ru
Убивает запах нейросети в русском тексте: 64 паттерна, 21 жёстких банов, калибровка голоса, quad-pass аудит. Kills AI smell in Russian text.

school
Skills
terminal
Commands
372

science-superpowers

@K-Dense-AI/science-superpowers
Core skills library: research framing, pre-registration, reproducible analysis, anomaly investigation, and review patterns

draft
Context
phishing
Hooks
school
Skills
338

ralph

@gemini-cli-extensions/ralph
Gemini CLI extension for Ralph loops

phishing
Hooks
terminal
Commands
333

honey

@Green-PT/honey-for-devs
Honey (I Shrunk the AI) — write less code and say less about it.

draft
Context
phishing
Hooks
school
Skills
309

tauri-mcp

@hypothesi/mcp-server-tauri
Agent Skills for automating and testing Tauri v2 applications

draft
Context
306

tldiagram

@Mertcikla/tld
Codebase diagram generation for tldiagram.com

school
Skills
286

unsloth-buddy

@TYH-labs/unsloth-buddy
Zero-friction LLM fine-tuning on NVIDIA (Unsloth) and Apple Silicon (mlx-tune). SFT, DPO, GRPO, vision — env setup to export, fully automated.

279

refero

@referodesign/refero_skill
Research real product interfaces a
