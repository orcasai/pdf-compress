# Writing Sample — Robin Walter Scherler

**Robin Walter Scherler · 18 May 2026 · Live demo:** [agentic-engineer.online](https://agentic-engineer.online)

> **Context:** To date I run production LLM systems in my own setup as a publicly testable demo — delivering to third parties is the next step. This example is a recruitment trial project that I have since been running as my own demo and learning environment. It shows *how I make decisions and take responsibility for trade-offs*. For the past year and a half I have been deliberately moving from pure developer mode into the Owner role for AI solutions — because responsible AI work demands end-to-end accountability, from schema to hosting. The approach that holds this work together I call **Empirical Context Reinforcement**: cross-session, empirically reinforced building with the context that carries value. I stand behind every trade-off on this page, 100 %.

---

### 1. What was the problem?

The brief described a web scraping task. The actual problem, as I framed it: **LLM extraction must be reproducible, cheap, and always available** — otherwise you build demo-ware that breaks under load. Three failure points I identified and logged as risks before the first commit:

- **Schema drift.** With no explicit data model, every LLM response has a different shape. Downstream tools break the moment a field is missing or renamed.
- **Correlated rate limits.** Free-tier OpenRouter models share the same Venice provider and 429 together — a single-model solution then gives no answer at all.
- **Cost ceiling.** With no hard cap per lead, an AI solution in a sales-enablement context does not scale. The architecture must know costs *before* each request, not after.

### 2. What did I do?

A FastAPI app with an asynchronous job pipeline, every component decided, built, and operated by me alone: the scraper locates the careers page via URL and anchor-text scoring → a chain of eight ATS adapters (Personio, Recruitee, Greenhouse, Lever, and others) extracts job data directly from their respective widget APIs, LLM extraction against a Pydantic schema serves as the generic fallback → persistence in SQLite → confirmation email via Resend, with an HTML preview fallback to disk for unverified domains. The pipeline surfaces every stop visibly in the HTML audit trail.

**Stack:** Python 3.11 · FastAPI + Uvicorn · httpx + BeautifulSoup4 · OpenRouter (6-model cascade via OpenAI SDK) · SQLite · Jinja2 · Resend.

What characterises this work: learning with AI tools while using them — Agentic Engineering in the literal sense.

**Three trade-offs I would make exactly the same way today:**

- **SQLite instead of Postgres.** Single-tenant scope requires no DB server. Deliberate debt, with a known trigger — upgrade path is in §4.
- **6-model cascade instead of single LLM.** Free tier first, two paid safety nets engage only on 429. Keeps the response guarantee at controlled costs and stable across provider changes.
- **Self-hosted Hetzner VPS behind Cloudflare Tunnel instead of managed cloud.** Outbound-only tunnel, full data sovereignty, free choice of provider. With an AI solution, I keep control on my side.

### 3. What was the measurable outcome?

All values are measured on the live system — each one an acceptance criterion I defined for myself before the first commit.

| Metric | Value |
| --- | --- |
| Extraction latency | 15–40 s per company |
| Cost per lead (paid fallback tier) | < 1 cent |
| Mobile 5-page nav (iOS Safari, Singapore edge) | 8.7 s → 1.5 s (5.8×) after Cloudflare edge-cache tuning |
| Response availability | 100 % — cascade delivers an answer, mailer errors are caught in the HTML audit trail |
| Coverage | ~75 % real-world — 4 of 8 ATS adapters (Personio, Recruitee, Greenhouse, Lever) verified live against real company URLs; 72 unit tests + 4 E2E live tests green |

Coverage as a hard acceptance criterion is, in my experience, the only reliable form of measurable code quality — and that discipline transfers 1:1 to every scaling problem in production: the tech stack follows the test-scenario definition, in that order.

The system has been running under its own infrastructure since the trial project and is publicly testable.

### 4. What would I do differently today?

**At the engineering level, every decision holds.** Every debt was taken on deliberately, with a known upgrade path and a defined trigger:

- **Postgres** instead of SQLite — as soon as multi-tenancy is required.
- **Server-Sent Events** instead of 800 ms polling on `/api/status/{id}` — as soon as UX fidelity matters.

**At the presentation level, I would consolidate.** The video I produced for this application still carries role-specific references. Going forward I will cut it as a standalone Owner asset — one carefully prepared hour that represents my working method independent of any particular occasion. The same material then serves press features, trade articles, or a company introduction when an employer presents me to the team. Same Owner logic as the stack: build it right once, deploy it indefinitely.

**At the Owner level, I built for reuse from day one**: stack, layout, and extraction pipeline were deliberately chosen to live on in my own projects — regardless of the outcome of this application. From this prototype a tool has emerged that I use daily and test my own products against — developer and strictest customer of my AI work in one person.

The same Owner logic carries the infrastructure beneath it. The site runs as one station in my multi-stage Hetzner pipeline (Ubuntu rebuild → stage snapshots → multi-site Cloudflare Tunnel) — a pipeline I originally built step by step for my own AI projects and extended for this site. It is operated AI-orchestrated: if a deploy step breaks, the system falls back to the last clean snapshot, the script is adjusted, the test repeated — empirically, test-driven, with no hand-tuning. That is the Empirical Context Reinforcement loop I run across projects. For scaling to many customers, the base choice would be Kubernetes + Terraform on Docker — committed the moment it is actually needed, and only then.

I took on that responsibility at my own risk — and would carry it the same way for any project inside a company.

---

*Two cornerstone observations on where I stand in the field:*

*Locally I am among the few who orchestrate two fully functional Claude Code sessions (own MCP servers, own slash-command extensions, each loaded with project and session context) across projects in such a way that they work precisely from their contexts — with me and with each other — while I observe and correct both windows simultaneously. This lets me maintain across two sessions the same quality I achieve in a single session. While the market is trying to make entire agent teams efficient — and often falters in a duo — this is, for me, the proven prerequisite: make the two-window discipline measurable first, then multi-agent can be reliably built on top of it. This is flanked by a proprietary graph system I deploy in every project: it steers the knowledge data of my sessions in the desired direction, keeps it available, and makes every session history traceable. The tool today is Claude Code, tomorrow perhaps Pi, Codex, or another — what remains is the empirical working method.*

*A year ago I wrote to one of the largest AI houses that strategic Claude Code understanding would become a key competency. The response at the time, in so many words, was that I was a tool fanboy. A year later the same house publicly says, in so many words: those who understand Claude Code can work here.*

*My conclusion from that data point: I carry AI development with accountability — and innovation with priority. From conviction, because the empirical work with AI inspires me every day and is precisely how I keep growing. That, in my view, is the profile of a good AI engineer — and the only stack on which we developers can keep setting the pace for the market.*
