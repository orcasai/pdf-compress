> Ich baue und betreibe eigenes agentic Tooling und KI-Produkte über viele Projekte hinweg — vom Claude-Code-"Betriebssystem", das ich täglich nutze, über Multi-Agent-Architekturen bis zu nativen KI-Apps — und teile dieses Wissen öffentlich. Darunter liegen 7+ Jahre Full-Stack-Engineering (Laravel, Magento, REST, CI/CD), die mir das Fundament geben, KI-Prototypen vom Schema bis zum Hosting in verantwortete Produktion zu überführen. Ich bin kein Web-Entwickler, der jetzt KI-Features einbaut, sondern jemand, der agentic Engineering als tägliche Arbeitsweise lebt und an Frontier-OSS aktiv mitarbeitet.

# Agentic Engineering & KI-Projekte

## Claude-Code-Betriebssystem — eigenes agentic Tooling, täglich betrieben

- Eigenes Claude-Code-"Betriebssystem" gebaut und täglich genutzt: ~32 Skills, 45+ Slash-Commands, 8+ research-synthetisierte Subagents, 9 Hooks, eigene MCP-Server (vault-mcp Knowledge-Compiler, context-search) — ~70 % Originalarbeit, 591 Commits in 6 Monaten.
- **agent-forge** gebaut — recherche-getriebener Subagent-Builder (parallele Research-Kanäle → Domänen-Wissen in System-Prompts, self-improving); **orchestrator** — Multi-Skill-Router mit Dependency-Graph; Session-Crash-Recovery-Hooks und Git-Worktree-/Symlink-Architektur über 20+ Repos.

## brandcite — Multi-Agent-Knowledge-Graph-Plattform (in Entwicklung)

- Multi-Agent-Plattform für Online-Sichtbarkeit gebaut (91 Commits): Claude-Squad-Orchestrierung über MCP, Crawl4AI-Web-Extraktion, Neo4j-Knowledge-Graph, deterministische Validierungsstufe gegen Halluzinationen.
- Docker-first (Next.js, FastAPI, Neo4j, Redis); aktiver Prototyp, von Architektur bis Test-Infrastruktur eigenverantwortet.

## jobs — macOS Voice-to-Text AI-Agent

- Native MenuBar-App gebaut (Swift, The Composable Architecture, 12 Feature-Reducer, 29 Dependency-Clients): Hotkey → Transkription → OpenRouter-Agent → Auto-Paste in die aktive App; Owner über 485+ Commits, ~92 % production-ready.
- Hybride Dual-Transkription: Apple Speech online + FluidAudio Parakeet V3 lokal, mit konfigurierbaren Agenten (Hotkeys, Modelle, System-Prompts) und LLM-Context-Review.

## iaar — Test-/Validierungs-Framework für agentic Systeme

- Async Python-Framework gebaut, das die Claude-Code-SDK gegen MCP-Server validiert (Session-Tests, parallele Tool-Validierung über mehrere MCP-Server, strukturiertes Logging) — systematische Qualitätssicherung für agentic Pipelines.

## Weitere Eigenprojekte (Auswahl)

- **cmux-tmux-workflow** (Pure Bash, 23 Commits) — Session-Orchestrator für parallele Agenten: Snapshot/Restore/Fork und benannte Multi-Agent-Workflows (CTFlow). **video-chat** (44 Commits) — progressive AI-Video-Streaming (Runway ML), "stream-as-you-generate". Dazu 20+ weitere Repos eigener Tools, Infrastruktur und Experimente — durchgängig git-belegte Eigenarbeit.

# Open-Source-Beiträge

- **Hermes Agent** (Nous Research) — zum Auth-Subsystem beigetragen (26 Commits): JWT-/Refresh-Logik, OAuth-Fallback, Token-Rotation, CI-Tests.
- **Anthropic Claude-Code-SDK (Python)** — Infrastruktur beigetragen (~39 Commits): Docker-Orchestrierung, CI/CD, Type-Checking-Pipeline, Pre-Commit-Hooks.
- **Pi** (Mario Zechner) — 2 gemergte Upstream-Bugfixes (bash-tool error handling mit Tests, #479). **claudecodeui** — Beiträge zur Claude-Code-Web-UI (27 Commits). **donna** — Distribution-/Release-Planung (78 Commits).

# Öffentliches Wissen

- Teile laufend Praxiswissen zu Agentic Engineering auf LinkedIn — 78 Beiträge (Juni 2025 – Juni 2026): Context Engineering, Claude-Code-Multi-Agent-Orchestrierung, Token- und Kosten-Strategie, AI-First-Produktdenken. (linkedin.com/in/robin-s-223606136)

# Berufserfahrung

> 7+ Jahre Full-Stack-Engineering bilden das Fundament, auf dem die agentic Arbeit aufsetzt — Schema-Design, REST-Integration, CI/CD und Produktionsbetrieb, die KI-Prototypen in verantwortete Produktion überführbar machen.

## Software Engineer — Change IT Solutions GmbH · Homeoffice · 10/2024 – 01/2025

- Entwicklungsumgebung von lokalem Apache/MySQL auf Docker Compose migriert — einheitliche Bedingungen fürs gesamte Team.
- Bestehende APIs auf Performance und Docker-Kompatibilität optimiert; Big-Data-Konzept und Evaluierung von KI-Einsatzszenarien zur Prozessautomatisierung erstellt.

## Software Engineer — Rissc Solutions GmbH · Homeoffice · 02/2018 – 07/2024

- Maßgeschneiderten Web2Print-Editor für individualisierbare Produkte konzipiert und kontinuierlich erweitert (Laravel + Magento); RESTful APIs zwischen Web-Editor, Druckinfrastruktur und Magento-Shops gebaut.
- Mehrere Magento-2-Shops eigenverantwortet: Customization-Tool als Plugin, dynamische Produktkonfigurationen, Multi-Store, Payment-Gateways, Sicherheitsupdates.
- CI/CD-Pipeline mit Git + Bitbucket betrieben (Feature-Branches, Hotfixes, Releases), Code-Reviews per Pull Request, Produktions-Monitoring und Backups verantwortet.

## Full-Stack Engineer · Karlsruhe · 06/2017 – 12/2017

- Maßgeschneiderte Web-Lösungen für Großkunden der Telekommunikationsbranche entwickelt: Deployment, Integration und Testing.
- Backend in PHP 5.6 mit Zend Framework und MySQL gebaut; Frontend mit JavaScript (jQuery/AJAX) und Zend/Smarty-Templating nach MVC-Architektur.

## Full-Stack Engineer — redhotmagma GmbH · Stuttgart · 09/2016 – 03/2017

- Moderne Web-Anwendungen in agilen Teams entwickelt (Jira, Bitbucket, Confluence; Git/SourceTree, Plugin-Entwicklung).
- Frontend mit HTML5, CSS3, JavaScript inkl. React und Three.js gebaut; mobile Apps mit React Native.

# Fähigkeiten

**Agentic & LLM:** Claude Code ■■■■■ · Multi-Agent-Orchestrierung ■■■■■ · Prompt- & Context-Engineering ■■■■■ · MCP-Server (eigene + Integration) ■■■■□ · LLM-Kosten-Kaskaden / Modellwahl ■■■■□ · OpenRouter / OpenAI-SDK ■■■■□ · RAG ■■■■□

**Programmiersprachen:** Python ■■■■□ · PHP (5.6–8.3) ■■■■■ · TypeScript ■■■■□ · JavaScript ■■■■□ · Swift ■■■□□ · Bash ■■■■□

**Backend & Infrastruktur:** FastAPI · Laravel ■■■■□ · RESTful APIs ■■■■■ · MySQL/SQL · PostgreSQL · Neo4j · SQLite · Redis · Docker / Docker Compose ■■■■■ · CI/CD (GitHub Actions, Bitbucket Pipelines) · self-hosted VPS / Cloudflare-Tunnel · Git ■■■■■

**Web:** Next.js · Vue.js · React · Magento 2 · HTML/CSS · Node.js

**Sprachen:** Deutsch · Englisch · Spanisch · Katalanisch

# Ausbildung

- **Fachinformatiker für Anwendungsentwicklung** — Peter Kwasny GmbH, Gundelsheim · 2013 – 2016
- **Técnico en Sistemas Microinformáticos y Redes** — IES Marcos Zaragoza, Villajoyosa (ES) · 2010 – 2013
- **Mittlere Reife (ESO)** — IES Castelló d'Empúries, Katalonien (ES) · 2003 – 2008
