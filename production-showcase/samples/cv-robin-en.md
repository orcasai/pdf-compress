<div class="cv-photo-gutter"></div>

# Robin Walter Scherler

**Agentic Engineer · AI Engineer · Software Engineer · macOS/iOS Engineer**

Neidenstein, Germany · scherler89@gmail.com · +49 1627308662 · Born 24/08/1989 · German national · Driving licence B · Languages: German, English, Spanish, Catalan

---

### About Me

> **On 27 November 2025 I wrote my first line of Swift. Nine months later there are 158,000 lines of Swift 6 in three products of my own** — 2,651 commits, sole developer, every feature with a specification and runtime acceptance.

Before that, ten years of web work, mainly PHP, Laravel and Magento 2. The jump did not come from typing faster but from a different way of working. I write specifications, interface contracts and acceptance criteria — the implementation is produced agentically against them. The devices that make this reliable I built myself: guards that intervene before the tool call, acceptance in disposable VMs, my own MCP server as the interface from my agents onto my product.

**The programming language has become secondary — the patterns have not.** Laravel service, SwiftUI view or FastAPI route: what carries is clean interfaces, a clear state model, separation of domain and surface, idempotency, and tests as a contract. These are the patterns I check on every agentically produced line — and the reason Swift 6 is no longer foreign territory after nine months. **Done means proven in the real system** — not a green build, not green unit tests.

The division of labour behind it runs both ways: I set the frame, the patterns and the acceptance bar, the agents carry the execution, and both improve with every round. **AI and I are a well-practised team** — that is the reason behind every number in this CV.

*3,937 commits of my own across 18 months, 1,737 of them in the last two — the jump coincides with the moment my agent harness was in place.*

---

### How Engineering Is Shifting Right Now

The tools have become faster, the methods have not. Interfaces fixed in advance come from a time when one iteration cost weeks — changing them later was more expensive than guessing them right up front. With a working agent harness it costs hours, and the arithmetic reverses.

What replaces up-front commitment is not arbitrariness but a shorter contract: specification and acceptance criterion per increment instead of for the whole product. **Architecture therefore follows insight rather than assumption** — visible in 264 of 1,815 commits that are pure specification and acceptance, spread across three months instead of bundled into a design phase.

I call it **Iteration-First**: less a new pattern than the consequence of insight now being cheaper than assumption.

---

### Working in Parallel — Plan, Let It Run, Keep Building

My way of working is built for parallelism: write a specification, put an agent on it, keep building the next strand meanwhile. Verifiable from the session data of the past three months:

- **167 agent sessions across 119 separate terminal panes** — up to 17 on a single working day, 26 concurrently open sessions at peak.
- **14 active Git worktrees, 40 branches** side by side: each strand in its own working directory, so concurrent runs cannot get in each other's way.
- **Guards are what make unsupervised runs possible.** An agent without supervision needs devices that catch wrong turns before the tool call. Without them parallelism does not scale — it merely multiplies the errors.
- **Scaling means reuse.** Specifications, acceptance lists, hooks and slash commands live in one place across projects and take effect in every repository. An improved workflow applies everywhere at once.

*One day, read off the commit log — 28 August 2026:* 09:44 a measurement confirming a refactor. 16:16 build 1669 shipped. 17:04 to 21:12 specification and a ten-step plan for the next rebuild. In the evening, in parallel, this CV. Thirteen feature branches stood alongside, another project was starting up. **The CV was the smallest item of the day.**

**Shared domains instead of one database**

The same idea carries the architecture of my current product: storage is split into separate **domains** — self-contained data worlds each with their own database, between which entries are deliberately transferred rather than merged. A dedicated coordination layer with a transfer journal and exchange protocol keeps them consistent. Cross-cutting **entities** sit across them and reach polymorphically over all entry types.

That parallelises knowledge work: several contexts open at once, without a query ever reading across a boundary by accident — privacy by architecture as a construction method, not as a statement of intent.

---

### Own Products — Apple Platform

**Current macOS product — multimodal AI capture, entirely on device · sole developer · since 05/2026**

101,000 lines of Swift 6, 1,815 commits, 267 test files in three months — roughly 1,000 lines of production code per day, every day, specification and acceptance included. Several data modalities, each with its own capture, processing and persistence path — all on device, no third party in the data path.

- **Live operation as a continuous test — from a single user.** 16,785 captured entries across 89 active days, 189 per day on average, 475 on the peak day. No seed or test data: developer and sole user in one person, every defect hits me the same day.
- **Specification before code.** 264 of the 1,815 commits concern specification and acceptance only. Every feature runs spec → implementation plan → runtime acceptance.
- **Acceptance as infrastructure — carried out by the agent itself.** Runtime tests in disposable Tart VMs that recreate the zero state at will: first install, Gatekeeper and permissions reproducible rather than one-off. The agent clones the VM, seeds the starting state, **operates the interface via AppleScript and checks the result itself** — every work strand with its own test environment, several in parallel. An acceptance plan of 5,300 lines, plus a separate list for everything only time can answer.
- **Guards instead of rework.** Every defect that got through once becomes a device that rules it out — PreToolUse hooks that intervene before the tool call rather than reporting after the failure.
- **Release readiness as its own discipline.** Developer ID signing, notarization, Sparkle appcast with EdDSA, diagnostics channel and crash reports from installed builds. One command builds the tester package — notarized DMG, signed CLI, MCP server, agent setup, README — in two flavours: silent for customers, with telemetry and its own update channel for the team; three update channels side by side, and notarization detects full and local mode itself. Two-machine operation accepted in the VM (20/20). Two delivery targets from one codebase via a build-configuration axis: a sandboxed App Store variant and a Developer ID variant; App Store submission prepared. Multi-user operation via OAuth2 on my own host is planned, triggered by the second external user.
- **My own MCP server** (TypeScript) as the agent interface onto the product — my agents work productively against my own application.
- **A second platform in five days.** My own iOS app with 9,100 lines of Swift 6 and 193 commits, from an empty project to the device. It hangs off the same interface as the MCP server and the macOS interface — one store, one interface, three consumers, one place for defects. Everything between the devices runs end-to-end encrypted over WireGuard in my own tailnet; the network boundary is the authorization, deliberately no second token. Write access is append-only, limited by a whitelist and idempotent by ID: a duplicate send changes nothing.
- **Observability from day one:** OpenTelemetry/OTLP spans in Grafana Tempo, unified logging via OSLog.

*How this comes together as a product I am happy to demonstrate live given mutual interest. One piece of evidence is already here, though: the system holds context over one's own work — ideas, experience, lines of thought — and this CV came out of exactly that. The figures above were read by an agent through its MCP server.*

**Hermes companion — macOS menu-bar app with iOS counterpart · sole developer · 11/2025 – 06/2026**

Voice-driven companion app for an open-source agent platform: 48,000 lines of Swift, 643 commits, one shared model behind two interfaces (a macOS target and a dedicated iOS target in the same project).

- **On-device transcription** — three engines run in production and measured: Whisper, Parakeet V3 via FluidAudio, Apple Speech. Consolidated onto Apple's SpeechAnalyzer in the successor product as soon as the platform solution led on accuracy and latency: no shipped third-party model, no download, no memory budget.
- **Agent system** with its own hotkey, model and system prompt per agent; responses from several models directly comparable, prompt editable at runtime.
- **OpenRouter cascade** across 100+ models with availability checks and failover.
- **Two agent backends evaluated, one kept.** Connected to Hermes through its multimodal API and SSE event streams, to OpenClaw in parallel — consolidated entirely onto Hermes in the end because it carried better. Slack as a second channel, container status in the iOS counterpart.
- **The Composable Architecture (TCA)** as the state model throughout, across both platforms.
- **CI gate since 02/2026:** GitHub Actions with branch protection, automatic changelog across all repositories, build status and PR requests in Slack.

---

### Live System & Deploy Pipeline on Own Infrastructure

**[agentic-engineer.online](https://agentic-engineer.online) — publicly testable recruiting tool · sole developer · built 04 – 05/2026, in operation since**

Company name and website in, a structured company profile with open positions out. Grown out of an application exercise — operated as my own product ever since, and publicly testable.

- **A cascade instead of one model.** Six models in series, free tier first, two paid fallback stages engaging only on 429 — **a 100 % response rate in measured operation at under 1 cent per lead.** The architecture knows the cost before the request, not after.
- **Eight ATS adapters** (Personio, Recruitee, Greenhouse, Lever and others) pull job data straight from the widget APIs; LLM extraction against a Pydantic schema is the generic fallback against schema drift. Four adapters verified live against real company URLs.
- **Measured, not estimated:** 15–40 s extraction latency, 72 unit and 4 E2E tests, roughly 75 % real-world coverage. Mobile navigation from 8.7 s to 1.5 s (5.8×) after Cloudflare edge tuning.
- Python 3.11 · FastAPI · httpx · BeautifulSoup4 · SQLite · Jinja2 · Resend — on a Hetzner VPS behind an outbound-only Cloudflare Tunnel.

**A deploy pipeline made of building blocks — from bare Ubuntu to production**

The infrastructure behind my systems is a product in itself: twelve reusable blocks (base, tunnel, Tailscale, observability, relays, backup), from which each server instance is composed as a list of stages.

- **Three script families per stage:** roll forward, set a fallback point, fall back to a stage. If a step breaks, the system returns to the last clean state, the script is adjusted, the run repeated — instead of patching by hand.
- **A decision tree instead of a gut feeling:** script changed → full rebuild from bare Ubuntu. Only the server state broken → fall back to the affected stage. When in doubt the expensive path, because it completes in about three minutes.
- **Two servers run in parallel** with no dependency on one another; both pipelines start at the same time.
- Software practice applied to deployment: idempotent steps, versioned blocks, a documented reason per decision — the same discipline as in application code.

[View a session clip](https://agentic-engineer.online/library#clip-1) · [Voice pitch — I introduce myself by voice, my app answers and is connected to my Slack channel](https://www.linkedin.com/posts/robin-s-223606136_hiermit-lade-ich-alle-ein-mit-mir-ins-gespr%C3%A4ch-activity-7434159927142801408-2yGt/)

---

### Portfolio

- [agentic-engineer.online](https://agentic-engineer.online) — live demo on own infrastructure, including a [session clip](https://agentic-engineer.online/library#clip-1).
- [GitHub orcasai](https://github.com/orcasai) — my own projects alongside many forks. The forks are the early part of the path: first read and collect what others build, then derive your own tools from it, today plan, build and operate your own products. Anyone reading the history sees that path — and that the commits of the last eighteen months sit in repositories of my own.
- [Voice pitch](https://www.linkedin.com/posts/robin-s-223606136_hiermit-lade-ich-alle-ein-mit-mir-ins-gespr%C3%A4ch-activity-7434159927142801408-2yGt/) — personal introduction, live by voice in the app I built.

---

### Skills

**Agentic & AI:** Claude Code (hooks, subagents, slash commands, headless mode) · MCP — building own servers (TypeScript, FastMCP) and consuming as a client · Spec-Driven Development · Context Engineering · Prompt Engineering · Multi-Agent Orchestration · parallel agent sessions (tmux, Git worktrees) · Evals & runtime acceptance · RAG / LLM Knowledge Compiler · OpenRouter model cascades & failover · LLM Ops / OpenAI Wire Protocol gateways · Agentic Loops (ReAct) · Hermes Agent (Nous Research) · OpenClaw / NemoClaw · Cursor · Codex

**macOS / iOS / Swift:** Swift 6 (Concurrency, Sendable, Synchronization) · SwiftUI · AppKit · The Composable Architecture (TCA) · Observation · GRDB (WAL, FTS5) · SpeechAnalyzer / SpeechTranscriber · AVFoundation / AVAudioEngine / CoreAudio · ScreenCaptureKit · Vision (OCR) · HealthKit · CoreMotion · CoreImage / CoreGraphics / ImageIO · CryptoKit · NaturalLanguage · PDFKit · Rive · global hotkeys & menu-bar apps (NSStatusItem) · CGEvent / ApplicationServices · Swift ArgumentParser (CLI) · SwiftPM & XcodeGen · App Group · TCC permissions & App Sandbox · Developer ID, codesign & notarytool · Sparkle (appcast, EdDSA) · LaunchAgents / launchd

**Architecture & Data:** domain-separated databases with a transfer journal · polymorphic entities across entry types · SQLite (WAL, FTS5) · GRDB · PostgreSQL · MySQL / MariaDB · Redis · Elasticsearch · JSON / JSON-LD / Schema.org · XML · YAML · Markdown · CSV

**Testing, Delivery & Observability:** Swift Testing & XCTest · unit and integration tests · runtime acceptance in Tart VMs · test-plan and long-term-test practice · PreToolUse guards for agents · GitHub Actions (CI gate, branch protection, changelog) · Bitbucket Pipelines · Conventional Commits · Git worktrees & stacked branches · OpenTelemetry / OTLP · Grafana / Tempo · OSLog / unified logging · diagnostics channel & crash reports

**Infrastructure & DevOps:** Hetzner Cloud (VPS, API rebuilds, snapshot pipelines) · Cloudflare (Tunnel, DNS / SPF / DKIM / DMARC, edge cache) · Caddy · Docker / Docker Compose · Tailscale (SSH / ACL) · systemd · UFW · Linux (Debian / Ubuntu) · frpc · rsync · idempotent & self-healing deploys · snapshot rollback · uv · Resend

**Languages & Web Stack:** Swift · Python · TypeScript / Node.js · JavaScript · PHP (5.6–8.3) · Bash / Shell · SQL · HTML / CSS · FastAPI / Starlette / uvicorn · Pydantic · Jinja2 · React · Vue.js · Laravel · Magento 2 · React Native · Three.js · Electron · Playwright · Chrome DevTools Protocol (CDP) · PyMuPDF · Pillow · Slack Bolt · ffmpeg · Bun · zod

**Methods:** Iteration-First (architecture follows insight) · Spec-Driven Development · acceptance-driven engineering · parallelism through isolated working directories · Context Engineering (target state) · idempotent deploy pipelines & snapshot rollback · PRD-first feature development · privacy by architecture / data sovereignty · CLI-over-MCP · working with non-technical stakeholders

**Domains:** multimodal AI on device · on-device inference & local-first architecture · agentic development systems & LLM Ops · macOS/iOS product engineering · recruitment tech / ATS automation (DACH)

---

### Professional Experience Before AI

**Eight years employed — full-stack, e-commerce, APIs · 09/2016 – 01/2025**

- **Change IT Solutions GmbH** · Software Engineer · 10/2024 – 01/2025 — migrated the development environment to Docker Compose, automated database provisioning, designed AI scenarios for process automation.
- **Rissc Solutions GmbH** · Software Engineer · 02/2018 – 07/2024 — web-to-print editor for product customization in Laravel; ownership of several Magento 2 stores including the customization plugin, multi-store and payment gateways; RESTful APIs between editor, print infrastructure and stores; **carried the Docker development environment over from Laravel to Magento 2** — where none existed before; CI/CD, monitoring and backups of the production environment.
- **Full-Stack Engineer** · Karlsruhe · 06/2017 – 12/2017 — web solutions for major telecommunications clients; PHP/Zend, MySQL, jQuery/AJAX, MVC and plugin systems.
- **redhotmagma GmbH** · Full-Stack Engineer · 09/2016 – 03/2017 — web applications in agile teams; HTML5, CSS3, JavaScript, Three.js.

---

### Education

**IT Specialist for Application Development (Fachinformatiker)** · Peter Kwasny GmbH, Gundelsheim · 2013 – 2016. Before that **Técnico en Sistemas Microinformáticos y Redes** (IES Marcos Zaragoza, Spain, 2010 – 2013) and **secondary education** (IES Castelló d'Empúries, Spain, 2003 – 2008) — raised trilingual: Spanish, Catalan, English.

---

### Data Sovereignty as Architecture — and What I Mean by Production

**Multimodal AI on the user's own device · in daily use**

Continuously accruing work data with a high personal-data content is the most sensitive material a work machine ever sees. The usual answer is encryption in the cloud. My answer is that the data never leaves my own devices in the first place.

- **Everything on device.** Transcription through Apple's SpeechAnalyzer locally, persistence in SQLite with a full-text index, no backend in the data path, no third party, no model download. This decision was deliberate — not for want of infrastructure, but because it is the right one for this data.
- **Domains as boundaries.** Separate databases instead of one with a tenant column: a query *cannot* read across a boundary. Data protection as a construction method rather than a setting.
- **What moves, moves encrypted.** Device to device over WireGuard in my own tailnet, no third-party server in between; update, diagnostics and telemetry channels over TLS; backups as authenticated encrypted archives, key in the keychain — readable with the system's own tools in an emergency, without the product.
- **And usable by AI regardless.** A dedicated MCP server opens the entire store to agents in structured form — locally, without a single byte leaving the device. Exactly the problem companies face under GDPR and the AI Act, solved in my own environment and proven in daily use.
- **Local means finite — so retention belongs in the architecture.** Keeping everything on the device leaves no elastic storage. A cleanup service has run in the product since day one; the rolling pruner deliberately works **without VACUUM**, because that would briefly need twice the space. Cleanup runs off the main thread, build artefacts and disposable VMs have defined lifecycles.
- **The platform is not a compromise but a prerequisite.** All of it runs, parallel VM test environments included, on a single Mac mini with 256 GB. On-device inference, Tart VMs and notarization exist only here — not the most resources, but the right environment, deliberately chosen.
- **Production does not mean a million customers.** It means a system that carries real work every day and does real damage when it fails. That is what mine has been since day one — this experience is not something I read up on.

---

### What I Bring — and Where It Fits

I have walked the entire path in an environment I am fully responsible for: understood the problem, built the system, put it into production, operated it, measured it, sharpened it. No development team, no safety net, with AI as the amplifier.

- **Shipping instead of demonstrating.** Signed and notarized distribution, my own update channel, a diagnostics channel from installed builds. A prototype that only runs in the demo would have hit me the same day — I was developer and user in one person.
- **Evaluating instead of hoping.** Every feature has an acceptance criterion before it has code: 5,300 lines of acceptance plan, runtime tests in disposable VMs, a separate list for everything only time can answer.
- **Quickly effective in unfamiliar stacks.** From zero Swift to 158,000 lines in nine months — including the concurrency model, the data layer, system frameworks and the full signing and delivery chain. The language was the smallest part of it. What I do not yet know I approach the same way: patterns first, vocabulary after.
- **Bringing non-technical people along.** My project partner is not a developer. Ideas, objections and test impressions arrive in everyday language; what goes back are guides split into must and optional, so a new build installs without a follow-up question, and acceptance plans readable without code. Eight years of client projects before that demanded the same: build deep technically, translate clearly — in both directions.
- **Data sovereignty where it is required.** Full AI access to sensitive data without that data leaving the device. Precisely the condition under which many companies under GDPR and the AI Act can even begin.
- **Context as a core competence.** Keeping ideas, experience and lines of thought available in a form AI can build something durable from — that is what I built my system for, and this CV came out of it. The figures in it were read by an agent through my own MCP server.

**What I am looking for:** a role where AI is meant to go into operation rather than be demonstrated — with a great deal of personal responsibility, on a deep rather than a broad problem, ideally where data is not allowed to leave the building. What I still lack for it I will acquire; the last eighteen months are the evidence. **The same discipline, the same construction method — applied to a company's problem.**
