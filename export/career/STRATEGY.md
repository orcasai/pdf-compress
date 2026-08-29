# STRATEGY — Robin Walter Scherler · Positionierung "Agentic Engineer"

Stand: 2026-06-15. Stratege-Output (career-lead). Basis: EVIDENCE_DOSSIER.md (Tier-1/2/3 + Guardrails),
cv-de-editorial.html (kondensierte 2-Seiten-Basis), writing-sample-de-editorial.pdf (candidate-flow Case),
cv-de-full.md (alte Langversion = aktuelle Build-Quelle), build-cv.sh (Dark + Editorial Pipeline).

> Dies ist der Schlachtplan, nicht das fertige CV. Umsetzung: `cv-optimizer` (CV) + `linkedin-ghostwriter` (LinkedIn).
> Jede Aussage strikt an Dossier-Tiers gebunden. Niemals "gebaut" für Upstream-Projekte anderer.

---

## 1. POSITIONIERUNG

**Markenkern (eine Zeile):**
**Agentic Engineer — baut und betreibt eigene Production-LLM-Systeme, auf 7+ Jahren Full-Stack-Fundament.**

**Headline / Rollen-Titel (CV-Masthead + LinkedIn):**
`Agentic Engineer · Production-LLM-Systeme & Multi-Agent-Orchestrierung · 7+ Jahre Full-Stack`

(Ersetzt den alten Vier-Begriffe-Stapel "AI Engineer & Expert · Software Engineer · Context Engineer · Prompt Engineer".
Der alte Titel listet Disziplinen; der neue benennt eine Rolle mit Beweisbarkeit.)

**3-Satz-Narrativ:**
> Ich baue und betreibe eigene agentic Production-Systeme — von einer async LLM-Extraktions-Pipeline mit
> 6-Modell-Kosten-Kaskade (<1 Cent/Lead, 100 % Antwort-Garantie) bis zum self-hosted Deploy mit
> Snapshot-Rollback. Darunter liegen 7+ Jahre Full-Stack-Engineering (Laravel, Magento, REST, CI/CD), die
> mir das Fundament geben, KI-Prototypen in verantwortete, getestete Produktion zu überführen — vom Schema
> bis zum Hosting. Ich bin kein Web-Entwickler, der jetzt KI-Features einbaut, sondern jemand, der eigenes
> agentic Tooling als tägliche Arbeitsweise betreibt und an Frontier-OSS aktiv mitarbeitet.

**Die Verschiebung in einem Satz:** Vom *rückwärtsgewandten* "Software Engineer, der AI-Tools nutzt"
(alte Langversion) zum *vorwärtsgewandten* "Agentic Engineer mit Full-Stack-Fundament" — Full-Stack wird
vom Hauptgericht zur tragenden Beilage.

---

## 2. EVIDENZ → CLAIM-MAPPING

Spalte "Framing" markiert die erlaubte Verb-Klasse laut Dossier-Guardrails:
**[GEBAUT]** = Robins Originalarbeit · **[BEIGETRAGEN]** = echte OSS-Commits (N nennen) · **[NUTZT/STUDIERT]** = keine Autorschaft.

| # | CV-Aussage (Soll) | Evidenz (Tier) | Framing |
|---|---|---|---|
| 1 | "candidate-flow — live agentic Recruiter-Tool: async FastAPI-Pipeline, 6-Modell-Kosten-Kaskade, <1 Cent/Lead, 100 % Antwort-Garantie" | T1 · 102 Commits 100 % Robin, live agentic-engineer.online | **[GEBAUT]** |
| 2 | "8 ATS-Adapter (Personio, Recruitee, Greenhouse, Lever …), 4 live verifiziert; 72 Unit- + 4 E2E-Tests" | T1 · candidate-flow | **[GEBAUT]** |
| 3 | "Self-hosted Hetzner-VPS hinter Cloudflare-Tunnel, AI-orchestriertes Deploy mit Snapshot-Rollback" | T1 · candidate-flow Infra (Owner) | **[GEBAUT]** (Owner/Betrieb) |
| 4 | "jobs — macOS Voice-to-Text AI-Agent: Swift, TCA, 12 Feature-Reducer, hybrid Apple Speech + Parakeet V3" | T1 · 460 Commits Owner, ~92 % prod-ready | **[GEBAUT]** |
| 5 | "Claude-Code-Betriebssystem: ~32 Skills, 45+ Slash-Commands, 8+ Subagents, eigene MCP-Server (vault-mcp, context-search)" | T1 · agi/.claude, ~70 % Original, 591 Commits/6 Mo | **[GEBAUT]** |
| 6 | "agent-forge (recherche-getriebener Subagent-Builder), orchestrator (Multi-Skill-Router mit Dependency-Graph), Session-Crash-Recovery-Hooks" | T1 · agi/.claude Originalsysteme | **[GEBAUT]** |
| 7 | "cmux-tmux-workflow — Session-Orchestrator für parallele Agenten (CTFlow Multi-Agent-Workflows)" | T1 · 23 Commits 100 % Robin | **[GEBAUT]** |
| 8 | "Contributions zum Auth-Subsystem von Hermes Agent (Nous Research): JWT/Refresh, OAuth-Fallback, Token-Rotation — 20 Commits" | T2 · 20 Commits Mär–Mai 2026 | **[BEIGETRAGEN]** |
| 9 | "akzeptierte Upstream-Bugfixes in Pi (Mario Zechner): bash-tool error handling mit Tests — 2 gemergte PRs" | T2 · #479 + TUI-Fix | **[BEIGETRAGEN]** |
| 10 | "donna: Distribution-/App-Store-Planung & History-Fixes beigetragen — 78 Commits" | T2 · nicht Core-Engine | **[BEIGETRAGEN]** (Scope ehrlich abgrenzen) |
| 11 | "Orchestriert spezialisierte MCP-Server (LinkedIn, Memory-Compiler u.a.) und betreibt eigenes Claude-Code-Overlay auf openclaw" | T3 · 0 Code-Commits | **[NUTZT/STUDIERT]** — niemals "gebaut" |
| 12 | "Verfolgt Frontier-Research (Karpathy self-modifying agent loops), evaluiert browser-use Self-Healing-Harness" | T3 | **[NUTZT/STUDIERT]** |
| 13 | "7+ Jahre Full-Stack: Laravel/Magento Web2Print, REST-APIs, CI/CD, Produktions-Monitoring (Rissc 2018–2024 u.a.)" | alte CV-Historie | unverändert faktisch — als **Fundament**, nicht Hauptbild |

**Harte Verbote (aus Do-Not-Claim):** kein "gebaut/architektiert" für openclaw, browser-harness, autoresearch,
linkedin-mcp-server, claude-peers-mcp, iwdp-mcp, claude-memory-compiler, NemoClaw, agent-zero, Archon, cmux.
Keine Client-/Bewerbungs-PII aus `intelligence/bewerbung/`.

---

## 3. CV-RESTRUKTUR-PLAN (für `cv-optimizer`)

**Auftrag:** Editorial-CV (`cv-de-editorial.html`) als inhaltliche Basis nehmen, agentic-fokussiert
umschreiben, Ergebnis in die Build-Quelle schreiben, damit `build-cv.sh` Dark + Editorial baut.

### 3a. KRITISCHER PFAD-HINWEIS (zuerst klären)
`build-cv.sh` zieht NICHT aus `cv-de-editorial.html`, sondern aus
`export/cv-translation/_source/cv-de-full.md` — und diese Datei ist die **alte, web-dev-lastige Langversion
ohne die agentic Projekte**. Das kondensierte Editorial-HTML ist der bessere Inhalt, wird aber nicht gebaut.
→ Der neue, agentic-fokussierte CV-Text muss in `_source/cv-de-full.md` geschrieben werden (das wird die
neue Single Source of Truth). Markdown-Struktur muss zu den CSS-Selektoren in `build-cv.sh` passen
(`h1` = Sektion, `h2` = Rolle/Firma, `#adresse` wird ausgeblendet, Masthead kommt aus dem Script).
→ Masthead-Tagline in `build-cv.sh` (Zeile 11) auf die neue Headline aus §1 aktualisieren.

### 3b. Soll-Sektionsreihenfolge (Neuanordnung — das ist der eigentliche Hebel)

| # | Sektion | Status | Inhalt |
|---|---|---|---|
| 1 | **Masthead + Summary** | NEU schreiben | Headline aus §1 + 3-Satz-Narrativ. Kein Disziplinen-Stapel, kein "AI-First"-Manifest. |
| 2 | **Agentic Engineering & KI-Projekte** | **NEUE Leitsektion** | candidate-flow (Flaggschiff, mit Metriken) → jobs → Claude-Code-OS (agent-forge/orchestrator) → cmux-tmux. Je 2–3 Bullets, Verben aus §2-Mapping. |
| 3 | **Open-Source-Beiträge** | NEU (kompakt) | Hermes (20 Commits, Auth), Pi (2 PRs), donna (Distribution). Modest, mit Commit-Zahlen. Klar als "beigetragen". |
| 4 | **Berufserfahrung (Full-Stack-Fundament)** | KÜRZEN + behalten | Rissc/Change IT/Karlsruhe/redhotmagma — auf je 2–3 Bullets gestrafft. Rahmen-Satz: "Fundament, auf dem die agentic Arbeit aufsetzt." |
| 5 | **Fähigkeiten** | NEU ordnen | AI/Agentic FÜHREND. Reihenfolge: Agentic/LLM → Sprachen → Backend/Infra → Web (kompakt am Ende). |
| 6 | **Ausbildung** | STARK kürzen | 3 Zeilen statt 1 Seite. Kein Lernziel-Katalog. |

### 3c. Was rausfliegt / gekürzt wird
- **Komplettes "Über Mich"-Manifest** der alten Langversion (`cv-de-full.md` Z. 6–102): die GitHub-URL-Cluster,
  "Claude Desktop Conversation History"-Links, "Meine Vision: AI-First als Wettbewerbsvorteil", das 70/30-Prinzip.
  Das ist Marketing-Prosa mit URL-Clutter — raus. Ersetzt durch §1-Narrativ + Projekt-Evidenz.
- **Redundante Skill-Listen** mit ■■■■□-Balken über 9 Kategorien → auf 4–5 Gruppen verdichten, Balken nur
  dort wo sie differenzieren. PHP 5.6 muss nicht ■■■■■ führen.
- **Ausbildungs-Lernziel-Kataloge** (Z. 458–600): drei Zeilen reichen (Abschluss, Institution, Jahr).
- **"Letzte Projekte Chronologisch"** (alte Web2Print/Docker/API-Doku-Projekte): die schwächeren wandern raus,
  die Vapi-MCP-Erweiterung kann als kleiner KI-Brückenpunkt bleiben — aber die echten agentic Projekte (§2)
  ersetzen diese Sektion als Showcase.
- **PII-Check:** Telefonnummer + private Mail nur wenn Robin öffentlich will (siehe §6 offene Entscheidung).

### 3d. Ziel-Format
- **2 Seiten** bleiben das Ziel (das Editorial-CV erreicht das bereits). Neue Projekt-Sektion gewinnt Platz aus
  gekürzter Ausbildung + verdichteten Skills + entferntem Manifest — netto neutral bis enger.
- **Output:** beide Varianten via `build-cv.sh` → `cv-robin-walter-scherler-de-dark.pdf` (Robins Favorit,
  amber/schwarz) + `-editorial.pdf`. Dark ist die Bewerbungs-Hauptdatei, Editorial die print-seriöse Alternative.
- **Erfolgs-Check:** Erste Bildschirmseite muss candidate-flow + Agentic-Sektion zeigen, BEVOR Magento auftaucht.

---

## 4. LINKEDIN-BRIEF (für `linkedin-ghostwriter`)

**Konsistenz-Anker:** gleiche Headline-Rolle wie CV, gleiche Flaggschiff-Projekte, Voice aus Dossier
(imperative Direktheit, starke Satzanfänge, provokativ-selbstbewusst, selektive Emojis 🎯💪🤖, Haltung > Konsens).

**Neue Headline (Profil-Slogan):**
`Agentic Engineer · ich baue & betreibe Production-LLM-Systeme · Multi-Agent-Orchestrierung mit Claude Code`

**About-Richtung (Vorschlag, nicht ausformuliert):**
Aufhänger = der Owner-Shift aus dem Writing Sample ("vom Entwickler-Modus in die Owner-Rolle für KI-Lösungen —
vom Schema bis zum Hosting"). Dann candidate-flow als konkreter Beweis (Metriken nennen: <1 Cent/Lead,
100 % Antwort-Garantie). Schließen mit Haltung: "KI mit Verantwortung, Innovation mit Priorität." Full-Stack
nur als ein Satz Fundament. KEINE Upstream-Projekte als eigene ausgeben.

**Post-Idee 1 — candidate-flow Deep-Dive (Substanz-Beweis):**
These: "Eine LLM-Pipeline, die unter Last bricht, ist Demoware." Story der 3 Bruchpunkte aus dem Writing Sample
(Schema-Drift, Rate-Limits, Kostendecke) → die 6-Modell-Kaskade als Lösung → Metriken. Zeigt Engineering-Tiefe,
nicht Tool-Begeisterung. Ankert direkt am CV-Flaggschiff. Live-Link agentic-engineer.online.

**Post-Idee 2 — Multi-Agent-Orchestrierung (Differenzierung):**
These (aus Dossier-Proof-Point): "Bevor man Agenten-Teams baut, muss man zwei Sessions verlässlich
gleichzeitig fahren können." Robins gelebte Multi-Session-Disziplin als Vorstufe zu Multi-Agent, das
Claude-Code-OS (agent-forge/orchestrator) als Werkzeug. Haltungsstark, forschungstrend-getrieben (Karpathy).
Differenziert ihn vom "ich nutze ChatGPT"-Feld.

> Hinweis Reihenfolge: Posts erst NACH CV-Freeze ghostwriten, damit Headline/Projekt-Metriken 1:1 übereinstimmen.

---

## 5. KONSISTENZ-CHECK (CV ↔ Writing Sample ↔ LinkedIn)

Dieselbe Story über alle drei Flächen:
1. **Eine Rolle, ein Titel:** "Agentic Engineer" + Production-LLM/Multi-Agent — identisch in CV-Masthead,
   LinkedIn-Headline, Writing-Sample-Kopf. Nicht in einem "AI Engineer", im anderen "Agentic Engineer".
2. **Ein Flaggschiff:** candidate-flow ist überall der Hauptbeweis. Gleiche Metriken überall
   (<1 Cent/Lead, 100 % Antwort-Garantie, 8 ATS-Adapter/4 verifiziert, 72+4 Tests) — keine abweichenden Zahlen.
3. **Ein roter Faden:** der Owner-Shift ("vom Entwickler-Modus in die Owner-Rolle, vom Schema bis zum Hosting")
   ist das Narrativ des Writing Samples — CV-Summary und LinkedIn-About müssen denselben Bogen schlagen.
4. **Ein Ehrlichkeits-Standard:** Tier-Framing überall gleich — gebaut/beigetragen/nutzt sauber getrennt,
   identische Commit-Zahlen bei OSS. Was im CV "beigetragen" heißt, heißt auf LinkedIn nicht "gebaut".
5. **Eine Voice-Konsistenz:** Writing Sample und LinkedIn teilen Ton (direkt, pragmatisch, Haltung); CV bleibt
   nüchterner, aber dieselben Schlüsselbegriffe (Owner-Rolle, Kaskade, Empirical Context Reinforcement).

---

## 6. OFFENE ENTSCHEIDUNGEN FÜR ROBIN (max 5)

1. **Build-Quelle umstellen?** Der neue agentic-CV-Text geht in `export/cv-translation/_source/cv-de-full.md`
   (= aktuelle Build-Quelle), das schöne `cv-de-editorial.html` wird damit überschrieben/abgelöst. OK so, oder
   soll `build-cv.sh` stattdessen auf eine neue Quelldatei zeigen? (Empfehlung: bestehende Quelle ersetzen.)
2. **Zielmarkt DE oder DE+EN?** Es existiert `cv-en-full.md`. Soll der cv-optimizer nur DE liefern oder die
   EN-Version parallel mitziehen (doppelter Aufwand, aber konsistenter Auftritt für internationale Rollen)?
3. **Kontaktdaten öffentlich?** Private Mail + Telefon im CV-Masthead lassen oder durch ein Kontakt-Pseudonym /
   nur agentic-engineer.online ersetzen? (LinkedIn-DM als Default-Kanal?)
4. **OSS-Contribs wie offensiv?** Eigene Sektion (sichtbar, mit Commit-Zahlen) oder dezent als ein
   "Open-Source-Engagement"-Block? Hermes (Nous Research) ist ein starker Name — prominent oder modest?
5. **LinkedIn-Posts jetzt mitliefern?** Soll `linkedin-ghostwriter` direkt nach CV-Freeze die 2 Posts +
   Headline/About ausarbeiten, oder erst CV finalisieren und LinkedIn in einer zweiten Runde?

---

## DELEGATIONS-REIHENFOLGE (Quick-Reference)

1. **Robin entscheidet §6** (mind. Punkt 1–3 blocken den CV).
2. **`cv-optimizer`** → §3 umsetzen: `_source/cv-de-full.md` neu, Masthead-Tagline in `build-cv.sh`, Build Dark+Editorial. Abhängig von §6.1–6.3.
3. **`linkedin-ghostwriter`** → §4 umsetzen: Headline + About + 2 Posts. Abhängig von CV-Freeze (Metriken/Titel-Konsistenz) und §6.5.
4. **Konsistenz-Check §5** beim Zusammenführen.

**Nächster Schritt für Robin:** §6 beantworten (v.a. 1–3), dann `cv-optimizer` mit §3 starten.
