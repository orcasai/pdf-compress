<div class="cv-photo-gutter"></div>

# Robin Walter Scherler

**Agentic Engineer · AI Engineer · macOS/iOS Engineer · Context Engineer**

Neidenstein, Germany · scherler89@gmail.com · +49 1627308662 · Born 24/08/1989 · German national · Driving licence B · Languages: German, English, Spanish, Catalan

---

### About Me

> Agentic engineer with owner responsibility for AI solutions — from the data model to signed delivery. Verifiable since March 2025: 3,937 commits of my own across 18 months, including roughly 145,000 lines of Swift 6 in my own macOS and iOS products since November 2025.

Ten years of software engineering, the last eighteen months fully agentic. Today I mostly write specifications, interface contracts and acceptance criteria; the implementation is produced agentically against them. **Done means proven in the real system** — not a green build, not green unit tests.

An example of how I work: I ran three transcription engines in production, measured them, and removed my own integration once the platform solution beat it. I hold decisions exactly as long as the measurement supports them.

*One number:* 3,937 commits of my own in 18 months, 1,737 of them in the last two — the jump coincides with the moment my agent harness was in place.

---

### Own Products — Apple Platform

**Current macOS product · sole developer · since 05/2026**

97,000 lines of Swift 6, 1,684 commits, 254 test files in three months. I say nothing about the content before we work together — the working method is the point.

- **Specification before code.** 240 of the 1,684 commits concern specification and acceptance only. Every feature runs spec → implementation plan → runtime acceptance.
- **Acceptance as infrastructure.** Runtime tests in disposable Tart VMs that recreate the zero state at will: first install, Gatekeeper and permissions reproducible rather than one-off. An acceptance plan of 4,800 lines, plus a separate list for everything only time can answer.
- **Guards instead of rework.** Every defect that got through once becomes a device that rules it out — PreToolUse hooks that intervene before the tool call rather than reporting after the failure. They are aimed at my agents, not at me.
- **Release readiness as its own discipline.** Developer ID signing, notarization, Sparkle appcast with EdDSA, diagnostics channel and crash reports from installed builds.
- **Own MCP server** (TypeScript) as the agent interface onto the product — my agents work productively against my own application.
- **Observability from day one:** OpenTelemetry/OTLP spans in Grafana Tempo, unified logging via OSLog.

*I am happy to demonstrate the system live in conversation.*

**OpenClaw companion — macOS menu-bar app with iOS counterpart · sole developer · 11/2025 – 06/2026**

Voice-driven companion app for an open-source agent platform: 48,000 lines of Swift, 643 commits, one shared model behind two interfaces (a macOS target and a dedicated iOS target in the same project).

- **On-device transcription** — three engines run in production and measured: Whisper, Parakeet V3 via FluidAudio, Apple Speech. Consolidated onto Apple's SpeechAnalyzer in the successor product as soon as the platform solution led on accuracy and latency: no shipped third-party model, no download, no memory budget.
- **Agent system** with its own hotkey, model and system prompt per agent; responses from several models directly comparable, prompt editable at runtime.
- **OpenRouter cascade** across 100+ models with availability checks and failover.
- **The Composable Architecture (TCA)** as the state model throughout; Slack integration and container status in the iOS counterpart.
- **CI gate since 02/2026:** GitHub Actions with branch protection, automatic changelog across all repositories, build status and PR requests in Slack.

---

### Live System on Own Infrastructure

**[agentic-engineer.online](https://agentic-engineer.online) — publicly testable demo**

Python and FastAPI, an OpenRouter model cascade, SQLite persistence, on a Hetzner VPS behind a Cloudflare Tunnel. Delivered through a multi-stage, agentically orchestrated deploy pipeline with snapshot rollback: if a step breaks, the system falls back to the last clean snapshot, the script is adjusted, the test repeated — no hand-tuning.

[View a session clip](https://agentic-engineer.online/library#clip-1) · [Voice pitch — I introduce myself by voice, my app answers and is connected to my Slack channel](https://www.linkedin.com/posts/robin-s-223606136_hiermit-lade-ich-alle-ein-mit-mir-ins-gespr%C3%A4ch-activity-7434159927142801408-2yGt/)

---

### Skills

**Agentic & AI:** Claude Code (hooks, subagents, slash commands, headless mode) · MCP — building own servers (TypeScript, FastMCP) and consuming as a client · Spec-Driven Development · Context Engineering · Prompt Engineering · Multi-Agent Orchestration · Evals & runtime acceptance · RAG / LLM Knowledge Compiler · OpenRouter model cascades & failover · LLM Ops / OpenAI Wire Protocol gateways · Agentic Loops (ReAct) · OpenClaw / NemoClaw · Cursor · Codex

**macOS / iOS / Swift:** Swift 6 (Concurrency, Sendable, Synchronization) · SwiftUI · AppKit · The Composable Architecture (TCA) · Observation · GRDB (WAL, FTS5) · SpeechAnalyzer / SpeechTranscriber · AVFoundation / AVAudioEngine / CoreAudio · ScreenCaptureKit · Vision (OCR) · CoreImage / CoreGraphics / ImageIO · CryptoKit · NaturalLanguage · PDFKit · Rive · Global hotkeys & menu-bar apps (NSStatusItem) · CGEvent / ApplicationServices · Swift ArgumentParser (CLI) · SwiftPM & XcodeGen · App Group · TCC permissions & App Sandbox · Developer ID, codesign & notarytool · Sparkle (appcast, EdDSA) · LaunchAgents / launchd

**Testing, Delivery & Observability:** Swift Testing & XCTest · unit and integration tests · runtime acceptance in Tart VMs · test-plan and long-term-test practice · PreToolUse guards for agents · GitHub Actions (CI gate, branch protection, changelog) · Bitbucket Pipelines · Conventional Commits · Git worktrees & stacked branches · OpenTelemetry / OTLP · Grafana / Tempo · OSLog / unified logging · diagnostics channel & crash reports

**Infrastructure & DevOps:** Hetzner Cloud (VPS, API rebuilds, snapshot pipelines) · Cloudflare (Tunnel, DNS / SPF / DKIM / DMARC, edge cache) · Caddy · Docker / Docker Compose · Tailscale (SSH / ACL) · systemd · UFW · Linux (Debian / Ubuntu) · frpc · rsync · idempotent & self-healing deploys · snapshot rollback · uv · Resend

**Languages & Web Stack:** Swift · Python · TypeScript / Node.js · JavaScript · PHP (5.6–8.3) · Bash / Shell · SQL · HTML / CSS · FastAPI / Starlette / uvicorn · Pydantic · Jinja2 · React · Vue.js · Laravel · Magento 2 · React Native · Three.js · Electron · Playwright · PyMuPDF · Pillow · Slack Bolt · Bun · zod

**Databases & Data:** SQLite (WAL, FTS5) · GRDB · PostgreSQL · MySQL / MariaDB · Redis · Elasticsearch · Chrome DevTools Protocol (CDP) · HTTP scraping · ffmpeg · JSON / JSON-LD / Schema.org · XML · YAML · Markdown · CSV

**Methods:** Spec-Driven Development · acceptance-driven engineering · Context Engineering (target state) · idempotent deploy pipelines & snapshot rollback · PRD-first feature development · Privacy by Architecture / data sovereignty · CLI-over-MCP

**Domains:** Agentic development systems & LLM Ops · macOS/iOS product engineering · voice & on-device transcription · recruitment tech / ATS automation (DACH)

---

### Professional Experience Before AI

**Ten years of full-stack — web, e-commerce, APIs · 2016 – 2025**

- **Change IT Solutions GmbH** · Software Engineer · 10/2024 – 01/2025 — migrated the development environment to Docker Compose, automated database provisioning, designed AI scenarios for process automation.
- **Rissc Solutions GmbH** · Software Engineer · 02/2018 – 07/2024 — built a web-to-print editor for product customization in Laravel; owned several Magento 2 stores including the customization plugin, multi-store and payment gateways; RESTful APIs between editor, print infrastructure and stores; CI/CD, monitoring and backups of the production environment.
- **Full-Stack Engineer** · Karlsruhe · 06/2017 – 12/2017 — web solutions for major telecommunications clients; PHP/Zend, MySQL, jQuery/AJAX, MVC and plugin systems.
- **redhotmagma GmbH** · Full-Stack Engineer · 09/2016 – 03/2017 — web applications in agile teams; React, Three.js, React Native.

---

### Education

**IT Specialist for Application Development (Fachinformatiker)** · Peter Kwasny GmbH, Gundelsheim · 2013 – 2016

**Técnico en Sistemas Microinformáticos y Redes** · IES Marcos Zaragoza, Villajoyosa (Spain) · 2010 – 2013 — networking, systems administration, OOP, relational databases.

**Secondary education (ESO)** · IES Castelló d'Empúries (Spain) · 2003 – 2008 — trilingual: Spanish, Catalan, English.

---

### Portfolio

- [agentic-engineer.online](https://agentic-engineer.online) — live demo on own infrastructure, including a [session clip](https://agentic-engineer.online/library#clip-1).
- [GitHub orcasai](https://github.com/orcasai) — public project examples and tech stacks.
- [Voice pitch](https://www.linkedin.com/posts/robin-s-223606136_hiermit-lade-ich-alle-ein-mit-mir-ins-gespr%C3%A4ch-activity-7434159927142801408-2yGt/) — personal introduction, live by voice in the app I built.
