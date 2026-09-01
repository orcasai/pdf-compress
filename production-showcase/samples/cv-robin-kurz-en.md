<div class="cv-photo-gutter"></div>

# Robin Walter Scherler

**Agentic Engineer · AI Engineer · Software Engineer · macOS/iOS Engineer**

Neidenstein, Germany · scherler89@gmail.com · +49 1627308662 · Born 24/08/1989 · German national · Driving licence B · Languages: German, English, Spanish, Catalan

---

### About Me

> **On 27 November 2025 I wrote my first line of Swift. Nine months later there are 145,000 lines of Swift 6 in two products of my own** — 2,327 commits, sole developer, every feature with a specification and runtime acceptance.

Before that, ten years of web work, mainly PHP, Laravel and Magento 2. The jump did not come from typing faster but from a different way of working: I write specifications, interface contracts and acceptance criteria — the implementation is produced agentically against them. **The programming language has become secondary, the patterns have not.** I set the frame and the acceptance bar, the agents carry the execution, and both improve with every round.

**Done means proven in the real system** — not a green build, not green unit tests.

*3,937 commits of my own across 18 months, 1,737 of them in the last two — the jump coincides with the moment my agent harness was in place.*

---

### Own Products & Systems

**Current macOS product — multimodal AI capture, entirely on device · sole developer · since 05/2026**

97,000 lines of Swift 6, 1,684 commits, 254 test files in three months. Several data modalities, each with its own capture, processing and persistence path — all on device, no third party in the data path. **16,318 captured entries across 84 active days, a single user: me.** No seed data, genuine continuous operation.

- **Data sovereignty as a construction method.** Transcription locally through Apple's SpeechAnalyzer, persistence in SQLite with a full-text index, no backend in the data path. Separate database domains instead of one with a tenant column: a query *cannot* read across a boundary. **Usable by AI regardless** — a dedicated MCP server opens the store to agents in structured form, without a single byte leaving the device.
- **Release readiness as its own discipline.** Developer ID signing, notarization, Sparkle appcast with EdDSA, diagnostics channel from installed builds. Observability through OpenTelemetry/OTLP in Grafana Tempo.
- **Acceptance as infrastructure.** 4,800 lines of acceptance plan, runtime tests in disposable Tart VMs: the agent clones the VM, operates the interface via AppleScript and checks the result itself.

*I say nothing further about the product before we work together — given mutual interest I will demonstrate it live.*

**Hermes companion — macOS menu-bar app with iOS counterpart · sole developer · 11/2025 – 06/2026**

48,000 lines of Swift, 643 commits, one shared model behind two interfaces. Three transcription engines run in production and measured (Whisper, Parakeet V3, Apple Speech), consolidated onto SpeechAnalyzer in the successor. Two agent backends evaluated, settled entirely on Hermes in the end. OpenRouter cascade across 100+ models, TCA as the state model, CI gate with branch protection.

**[agentic-engineer.online](https://agentic-engineer.online) — publicly testable recruiting tool · built 04 – 05/2026, in operation since**

Company name in, a structured profile with open positions out. Six-model cascade with **a 100 % response rate in measured operation at under 1 cent per lead**; eight ATS adapters, four verified live; 72 unit and 4 E2E tests; mobile navigation from 8.7 s to 1.5 s after Cloudflare edge tuning. Python, FastAPI, SQLite on a Hetzner VPS behind a Cloudflare Tunnel — shipped through a pipeline of twelve building blocks with snapshot rollback that runs from bare Ubuntu in about three minutes.

---

### How I Work

- **Iteration-First.** Interfaces fixed in advance come from a time when one iteration cost weeks; with an agent harness it costs hours. Specification and acceptance criterion apply per increment rather than to the whole product — architecture follows insight rather than assumption. 240 of 1,684 commits are pure specification and acceptance.
- **Building in parallel.** 167 agent sessions across 119 terminal panes, up to 17 on one working day; 14 active Git worktrees side by side, each strand in its own working directory.
- **Guards are what make unsupervised runs possible.** Devices that catch wrong turns before the tool call. Without them parallelism does not scale — it merely multiplies the errors.
- **Reuse instead of repetition.** Specifications, acceptance lists, hooks and slash commands live in one place across projects and take effect in every repository.

---

### Skills

**Agentic & AI:** Claude Code (hooks, subagents, slash commands, headless) · MCP — building own servers (TypeScript, FastMCP) and consuming as a client · Iteration-First · Spec-Driven Development · Context & Prompt Engineering · Multi-Agent Orchestration · parallel agent sessions (tmux, Git worktrees) · Evals & runtime acceptance · RAG · OpenRouter cascades & failover · LLM Ops · Hermes Agent · OpenClaw / NemoClaw · Cursor · Codex

**macOS / iOS / Swift:** Swift 6 (Concurrency, Sendable) · SwiftUI · AppKit · TCA · GRDB (WAL, FTS5) · SpeechAnalyzer · AVFoundation / CoreAudio · ScreenCaptureKit · Vision (OCR) · CryptoKit · global hotkeys & menu-bar apps · SwiftPM & XcodeGen · TCC & App Sandbox · Developer ID, codesign & notarytool · Sparkle · launchd

**Languages, Web & Data:** Python · TypeScript / Node.js · JavaScript · PHP (5.6–8.3) · Bash · SQL · FastAPI · Pydantic · React · Vue.js · Laravel · Magento 2 · SQLite (WAL, FTS5) · PostgreSQL · MySQL · Redis · Elasticsearch · Playwright · CDP

**Infrastructure & Operations:** Hetzner Cloud · Cloudflare (Tunnel, DNS, edge cache) · Caddy · Docker / Docker Compose · Tailscale · systemd · Linux · idempotent & self-healing deploys · snapshot rollback · GitHub Actions · OpenTelemetry / OTLP · Grafana / Tempo · Tart VMs

**Domains:** multimodal AI on device · on-device inference & local-first architecture · agentic development systems & LLM Ops · macOS/iOS product engineering · recruitment tech / ATS automation (DACH)

---

### Professional Experience Before AI

**Eight years employed — full-stack, e-commerce, APIs · 09/2016 – 01/2025**

- **Change IT Solutions GmbH** · Software Engineer · 10/2024 – 01/2025 — migrated the development environment to Docker Compose, automated database provisioning, designed AI scenarios for process automation.
- **Rissc Solutions GmbH** · Software Engineer · 02/2018 – 07/2024 — web-to-print editor in Laravel; ownership of several Magento 2 client stores including the customization plugin, multi-store and payment gateways; RESTful APIs; carried the Docker development environment over from Laravel to Magento 2; CI/CD, monitoring, backups.
- **Full-Stack Engineer** · Karlsruhe · 06/2017 – 12/2017 — web solutions for major telecommunications clients; PHP/Zend, MySQL, jQuery.
- **redhotmagma GmbH** · Full-Stack Engineer · 09/2016 – 03/2017 — web applications in agile teams; HTML5, CSS3, JavaScript, Three.js.

**Education:** IT Specialist for Application Development (Peter Kwasny GmbH, 2013 – 2016) · Técnico en Sistemas Microinformáticos y Redes (Spain, 2010 – 2013) · secondary education (Spain, 2003 – 2008), raised trilingual.

---

### What I Bring — and Where It Fits

- **Shipping instead of demonstrating.** Signed, notarized distribution with my own update channel and a diagnostics channel. A prototype that only runs in the demo would have hit me the same day — I was developer and user in one person.
- **Evaluating instead of hoping.** Every feature has an acceptance criterion before it has code.
- **Quickly effective in unfamiliar stacks.** From zero Swift to 145,000 lines in nine months — including concurrency, the data layer, system frameworks and the delivery chain. The language was the smallest part. What I do not yet know I approach the same way: patterns first, vocabulary after.
- **Data sovereignty where it is required.** Full AI access to sensitive data without that data leaving the device.

**What I am looking for:** a role where AI is meant to go into operation rather than be demonstrated — with a great deal of personal responsibility, on a deep rather than a broad problem, ideally where data is not allowed to leave the building. What I still lack for it I will acquire; the last eighteen months are the evidence.

[agentic-engineer.online](https://agentic-engineer.online) · [GitHub orcasai](https://github.com/orcasai) · [Voice pitch on LinkedIn](https://www.linkedin.com/posts/robin-s-223606136_hiermit-lade-ich-alle-ein-mit-mir-ins-gespr%C3%A4ch-activity-7434159927142801408-2yGt/)
