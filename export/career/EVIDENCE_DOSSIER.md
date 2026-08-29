# Evidenz-Dossier — Robin Walter Scherler · Positionierung "Agentic Engineer"

Stand: 2026-08-28 (Tier-2-Korrektur, donna aktualisiert). Ursprung: 2026-06-15. Quelle: 6 Read-only-Scouts über ~/Code + LinkedIn-CSV (78 Posts, Juni 2025–Juni 2026).
Zweck: verteidigbare Faktenbasis für CV / Writing Sample / LinkedIn. Jede Aussage ist nach Autorschaft geprüft.

---

## LEITSATZ DER EHRLICHKEIT
Robin **baut eigene agentic Produkte & Tooling** UND **studiert/patcht Frontier-OSS-Frameworks**.
Beides ist stark — aber NICHT vermischen. Nie "built/architected" für Upstream-Projekte anderer.

---

## TIER 1 — Robins Originalarbeit (Headline-Evidenz, "gebaut/betrieben")

### candidate-flow — live agentic Web-Produkt  ★ Kern-Showcase
- **Autorschaft:** 102 Commits, 100% Robin (orcasai). Live unter agentic-engineer.online.
- **Was:** Recruiter-Tool. Firma+Website → Homepage/Karriereseite-Scraping → LLM-Struktur-Extraktion (Branche, Benefits, offene Stellen) → SQLite → Mail (Resend).
- **Engineering-Tiefe:** async FastAPI-Pipeline; **6-Modell-Kaskade** (Free-Tier zuerst, 2 Paid-Safety-Nets bei 429) → 100% Antwort-Garantie bei **<1 Cent/Lead**; Pydantic-Schema gegen Schema-Drift; 8 ATS-Adapter (Personio, Recruitee, Greenhouse, Lever …), 4 live verifiziert; 72 Unit- + 4 E2E-Tests.
- **Infra (Owner-Rolle):** self-hosted Hetzner-VPS hinter Cloudflare-Tunnel, AI-orchestriertes Deploy mit Snapshot-Rollback ("Empirical Context Reinforcement"-Loop).
- **= Das Projekt aus dem Writing Sample, produktiv weiterbetrieben.**

### jobs — macOS Voice-to-Text AI-Agent  ★
- **Autorschaft:** 460 Commits Robin (Owner) + 183 Co-Dev. ~92% production-ready.
- **Was:** MenuBar-App: Hotkey → Transkription → OpenRouter-Agent → Clipboard/Auto-Paste in aktive App.
- **Tiefe:** Swift 5.9+, **TCA (The Composable Architecture)**, 12 Feature-Reducer, 29 Dependency-Clients; Dual-Transkription Apple Speech + FluidAudio Parakeet V3 (hybrid online/lokal); konfigurierbare Agenten (Hotkeys, Modelle, System-Prompts), LLM-Context-Review.
- **Beleg für:** native Desktop-Engineering + agentic Patterns, nicht nur Web.

### agi / .claude — Robins Claude-Code-"Betriebssystem"  ★ tägliche Arbeit
- **Autorschaft:** ~70% Original (Rest Komposition/Best-Practice-Prompts, nichts geklont). Heute aktiv (591 Commits/6 Mo im Worktree).
- **Umfang (gezählt):** ~32 eigene Skills, 45+ Slash-Commands, 8+ research-synthetisierte Subagents, 9 Hooks, 6+ Output-Styles, eigene MCP-Server (u.a. **vault-mcp** Knowledge-Compiler, context-search).
- **Originelle Systeme:**
  - **agent-forge** — recherche-getriebener Subagent-Builder: parallele Research-Kanäle (Web, context7, vault) → synthetisiert Domänen-Wissen in System-Prompts, self-improving.
  - **orchestrator** — Multi-Skill-Router mit Dependency-Graph (Intent → Diagnose → Sequenz aus 9+ Skills).
  - **vault-Knowledge-System** — projektübergreifende Wissens-Compilation, Auto-Context-Detection über 20+ Repos.
  - **Session-Crash-Recovery-Hooks** — Zustandspersistenz über Claude-Code-Neustarts.
  - **Git-Worktree + Symlink-Architektur** — eine Quelle, automatische Versionierung über alle Projekte.
- **Beleg für:** Systems-Thinking, Multi-Agent-Orchestrierung, Context-Engineering als Disziplin.

### donna — eigenes macOS-Produkt  ★ Kern-Showcase (Stand 08/2026)
- **Autorschaft:** 1.684 Commits, **100 % Robin** (scherler89) — einzige Identität im Repo.
- **Umfang:** ~97.000 Zeilen Swift 6 in 331 Dateien, 254 Test-Dateien, 3 lokale Swift-Packages.
- **Tiefe:** multimodale Erfassung on-device; GRDB (WAL, FTS5); domänen-getrennte Datenbanken
  mit Transfer-Journal; eigener MCP-Server (TypeScript); Sparkle/Notarisierung;
  OTLP → Grafana Tempo; Laufzeit-Abnahme in Tart-VMs.
- **Nutzung:** 16.318 erfasste Einträge an 84 aktiven Tagen (ein Nutzer, täglicher Realbetrieb).

### cmux-tmux-workflow — Session-Orchestrator (Original-Tool)
- **Autorschaft:** 23 Commits, 100% Robin (orcasai). Pure Bash.
- **Was:** Persistenz-Layer für cmux-Terminals über tmux: Snapshot/Restore/Fork, **CTFlow** = benannte Multi-Agent-Workflows, Vault-Batch-Integration.
- **Beleg für:** praktisches Infra-Tooling für parallele Agenten-Szenarien.

---

## TIER 2 — Open-Source-Contributions

**Stand 2026-08-28: keine.** Robin hat in keinem Fremd-Repository eigene Commits.

Frühere Einträge zu **Hermes Agent** und **Pi** waren Fehlzuschreibungen: Die dort
gezählten Commits stammen von **Robin Fernandes** (`robin@soal.org`, Branches `rewbs/…`)
bzw. **Robin Wander** (`robinwander@…`) — zwei andere Personen mit demselben Vornamen.
Die Erhebung hatte nach Vornamen statt nach E-Mail/Handle gefiltert.

**Prüfregel für künftige Erhebungen:** Autorschaft ausschließlich über
`--author="scherler89\|netvista\|^Robin <>\|padawan89"` bestimmen. Ein Filter auf
"robin" trifft in großen OSS-Repos zuverlässig Namensvettern.

**Hermes Agent** gehört damit in Tier 3: genutzt, nicht beigetragen — als Agenten-Backend
im eigenen Companion (multimodale API, SSE-Event-Streams). **Pi** entfällt ganz.

---

## TIER 3 — Genutzt/studiert (Kontext & Frontier-Awareness, KEINE Autorschaft)
Verwendbar als "arbeitet täglich mit / evaluiert / studiert", NICHT als eigene Werke:
- **Hermes Agent** (Nous Research) — als Agenten-Backend im eigenen Companion angebunden (0 Code-Commits upstream).
- **openclaw** (P. Steinberger) — betreibt eigenes Claude-Code-Overlay/Deployment darauf (0 Code-Commits).
- **browser-harness** (browser-use) — nutzt CDP-Browser-Automation/Self-Healing-Harness.
- **autoresearch** (Karpathy) — studiert self-modifying ML-Agent-Loops (Frontier-Research-Tracking).
- **Third-Party-MCPs, die er produktiv nutzt:** linkedin-mcp-server (stickerdaniel), claude-peers-mcp (louislva), iwdp-mcp (nnemirovsky), claude-memory-compiler (coleam00). → "integriert/orchestriert spezialisierte MCP-Server", NICHT gebaut.
- Marginal/ignorieren: NemoClaw, agent-zero, Archon, cmux (0–1 Commits).

---

## LINKEDIN — Positionierung, Voice, Proof-Points (78 Posts)

**Positionierungs-Essenz:** Agentic Engineer, der KI nicht als Feature, sondern als strategische Entwicklungs- & Priorisierungs-Methode versteht. Production-LLM-Systeme, Token-Optimierung, Claude-Code-Multi-Agent-Orchestrierung. Radikal pragmatisch (Idee vor Tests, AI-First statt Dogmen), forschungstrend-getrieben (Karpathy).

**Voice (für konsistentes Ghostwriting):** imperative Direktheit, starke Satzanfänge; provokativ-selbstbewusst; technisch-pragmatische Metaphern (Sparringspartner, Harness, Token-Effizienz); selektive Emojis (🎯💪🤖); Haltung > Konsenssuche.

**Öffentlich gemachte Proof-Points (CV-tauglich, weil selbst kommuniziert):**
- betreibt Production-LLM-Systeme in eigenem Setup, orchestriert mehrere KI-Agenten parallel
- zwei voll funktionsfähige Claude-Code-Sessions projektübergreifend orchestriert (Multi-Session-Disziplin als Vorstufe zu Multi-Agent)
- Token-/Kontextfenster-Optimierung als messbarer Produktivitätshebel
- Modellwahl & Kosten-Kaskaden als strategische Entscheidung
- eigenes Graphen/Knowledge-System pro Projekt für nachvollziehbare Session-Historie

---

## ADDENDUM v2 (2026-06-15) — Richtungswechsel: Breite + öffentliches Wissen

**Entscheidung Robin:** candidate-flow KOMPLETT raus aus dem CV (Writing Sample wird ebenfalls weg vom Einzelbeispiel überarbeitet). Neuer Fokus: git-belegte **Breite** über viele ~/Code-Repos + öffentlich geteiltes **Wissen** (LinkedIn).

**Methodenhinweis:** Grober Author-Sweep (`--author=robin\|scherler\|…`) ÜBER-zählt (Substring-Matches wie "Canyon **Robins**", Merges). Immer mit fokussiertem Per-Repo-Check verifizieren.

**Neu bestätigte Eigenprojekte (showable, Robin Haupt-/Alleinautor):**
- **brandcite** (orcasai, 91 Commits) — Multi-Agent-Knowledge-Graph-Plattform: Claude-Squad über MCP, Crawl4AI, Neo4j, Docker-first (Next.js/FastAPI/Redis). **In Entwicklung** (Tasks 1–3/12), nicht deployed. "0 % Halluzination" ist Projektziel, nicht bewiesen → vorsichtig framen.
- **iaar** (Original, 100 % Robin) — async Test-/Validierungs-Framework für Claude-Code-SDK + MCP-Server. Agentic Infra.
- **video-chat** (orcasai, 44 Commits) — progressive AI-Video-Streaming (Runway ML, React/Node/Redis), stream-as-generate. Proof-of-Concept, nicht live.
- **claudecodeui** (27 Commits scherler89 ✓) — echter Beitrag zu Claude-Code-Web-UI (siteboon).
- + 20+ weitere eigene Repos (script-*-Familie/TaskMaster-Infra, code, paco, orca, brandcite-Backups, kleinere Tools/Experimente).

**Korrektur claude-code-sdk-python:** KEIN Fork in Robins Besitz — Anthropics offizielles SDK (Base: Lina Tawfik, Team). Robin ~39 Commits = **Infra/DevOps** (Docker, CI, Type-Checking, iaar-Integration). Framing: "Infrastruktur beigetragen", NIE "SDK gebaut".

**Thought Leadership (neu im CV):** LinkedIn 78 Beiträge (Juni 2025–Juni 2026) zu Agentic/Context Engineering, Claude-Code-Multi-Agent, Token-/Kosten-Strategie, AI-First. Profil: linkedin.com/in/robin-s-223606136.

**NEU auf Do-Not-Claim (v2):**
- ❌ roocode-steve / deve: Commits = **Canyon Robins** (canrobins13@gmail.com), NICHT Robin. Nie als Beitrag nennen.
- ❌ intelligence: Bot-Persona-Authorship (Nightcrawler/Jarvis@az-robin) + confidential `bewerbung/` → ganz aus dem CV.
- ❌ boeses-auto-include: nur Claude-Code-Config-Repo (orcasai/.claude), kein Produkt.
- candidate-flow: aus dem CV entfernt (nur noch ggf. Writing Sample).

---

## DO-NOT-CLAIM — harte Guardrails
- ❌ NICHT "gebaut/entwickelt/architektiert": linkedin-mcp-server, openclaw, iwdp-mcp, claude-peers-mcp, claude-memory-compiler, browser-harness, autoresearch, NemoClaw, agent-zero, Archon, cmux.
- ❌ Keine Client-/Bewerbungs-PII aus `intelligence/bewerbung/` oder confidential Templates.
- ✅ Erlaubt: "betreibt eigenes Overlay auf X", "nutzt/integriert/orchestriert X", "trägt zu X bei (N Commits)".
- Regel: Wenn Upstream-Autor ≠ Robin → max. "nutzt/studiert/patcht", nie "built".
