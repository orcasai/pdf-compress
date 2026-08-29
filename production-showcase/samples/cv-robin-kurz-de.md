<div class="cv-photo-gutter"></div>

# Robin Walter Scherler

**Agentic Engineer · AI Engineer · Software Engineer · macOS/iOS Engineer**

Neidenstein, Deutschland · scherler89@gmail.com · +49 1627308662 · Geb. 24.08.1989 · Nationalität Deutsch · Pkw-Klasse B · Sprachen: Deutsch, Englisch, Spanisch, Katalanisch

---

### Über Mich

> **Am 27. November 2025 habe ich meine erste Zeile Swift geschrieben. Neun Monate später stehen 145.000 Zeilen Swift 6 in zwei eigenen Apple-Produkten** — 2.327 Commits, alleiniger Entwickler, jedes Feature mit Spezifikation und Laufzeit-Abnahme.

Davor zehn Jahre Web, im Kern PHP, Laravel und Magento 2. Der Sprung ging nicht über schnelleres Tippen, sondern über eine andere Arbeitsweise: Ich schreibe Spezifikationen, Schnittstellen-Verträge und Abnahmekriterien — die Implementierung entsteht agentisch dagegen. **Die Programmiersprache ist damit zweitrangig geworden, die Muster nicht.** Ich setze Rahmen und Abnahmemaß, die Agenten tragen die Ausführung, und beides verbessert sich mit jeder Runde.

**Fertig heißt bei mir im echten System bewiesen** — nicht Build grün, nicht Unit-Tests grün.

*3.937 eigene Commits in 18 Monaten, 1.737 davon in den letzten beiden — der Sprung fällt mit dem Moment zusammen, in dem mein Agent-Harness stand.*

---

### Eigene Produkte & Systeme

**Aktuelles macOS-Produkt — multimodale KI-Erfassung, vollständig auf dem Gerät · alleiniger Entwickler · seit 05/2026**

97.000 Zeilen Swift 6, 1.684 Commits, 254 Test-Dateien in drei Monaten. Verarbeitet Sprache, Bildschirmvideo, Screenshots mit Texterkennung und Transkription — jede Modalität mit eigenem Pfad, keine davon in einer Cloud. **16.318 erfasste Einträge an 84 aktiven Tagen, ein einziger Nutzer: ich.** Keine Seed-Daten, echter Dauerbetrieb.

- **Datenhoheit als Bauweise.** Transkription lokal über Apples SpeechAnalyzer, Persistenz in SQLite mit Volltextindex, kein Backend im Datenpfad. Getrennte Datenbank-Domänen statt einer mit Mandantenspalte: Eine Abfrage *kann* nicht über eine Grenze lesen. **Trotzdem für KI nutzbar** — ein eigener MCP-Server öffnet den Bestand strukturiert für Agenten, ohne dass ein Byte das Gerät verlässt.
- **Auslieferungsreife als eigene Disziplin.** Developer-ID-Signatur, Notarisierung, Sparkle-Appcast mit EdDSA, Diagnose-Rückkanal aus installierten Ständen. Observability über OpenTelemetry/OTLP in Grafana Tempo.
- **Abnahme als Infrastruktur.** 4.800 Zeilen Abnahmeplan, Laufzeit-Tests in wegwerfbaren Tart-VMs: Der Agent klont die VM, bedient die Oberfläche per AppleScript und prüft selbst.

*Zum Produkt sage ich vor einer Zusammenarbeit nichts weiter — ich zeige es im Gespräch gern live.*

**Hermes-Companion — macOS-MenuBar-App mit iOS-Begleiter · alleiniger Entwickler · 11/2025 – 06/2026**

48.000 Zeilen Swift, 643 Commits, ein geteiltes Modell hinter zwei Oberflächen. Drei Transkriptions-Engines produktiv gefahren und gemessen (Whisper, Parakeet V3, Apple Speech), im Nachfolger auf SpeechAnalyzer konsolidiert. Zwei Agenten-Backends evaluiert, am Ende vollständig auf Hermes gesetzt. OpenRouter-Kaskade über 100+ Modelle, TCA als Zustandsmodell, CI-Gate mit Branch-Protection.

**[agentic-engineer.online](https://agentic-engineer.online) — öffentlich testbares Recruiting-Werkzeug · 04 – 05/2026, seither im Betrieb**

Firmenname hinein, strukturiertes Profil mit offenen Stellen heraus. Sechs-Modell-Kaskade mit **100 % Antwortgarantie bei unter 1 Cent pro Lead**; acht ATS-Adapter, vier live verifiziert; 72 Unit- und 4 E2E-Tests; Mobile-Navigation von 8,7 s auf 1,5 s nach Cloudflare-Edge-Tuning. Python, FastAPI, SQLite auf Hetzner-VPS hinter Cloudflare-Tunnel — ausgeliefert über eine Pipeline aus zwölf Bausteinen mit Snapshot-Rollback, die ab blankem Ubuntu in rund drei Minuten durchläuft.

---

### Arbeitsweise

- **Parallel bauen.** 167 Agenten-Sessions über 119 Terminal-Panes, bis zu 17 an einem Arbeitstag; 14 aktive Git-Worktrees nebeneinander, jeder Strang in eigenem Arbeitsverzeichnis.
- **Guards machen unbeaufsichtigte Läufe möglich.** Vorrichtungen, die falsche Abzweigungen vor dem Werkzeugaufruf abfangen. Ohne sie skaliert Parallelität nicht — sie vervielfacht nur die Fehler.
- **Spezifikation vor Code.** 240 von 1.684 Commits betreffen ausschließlich Spezifikation und Abnahme.
- **Wiederverwendung statt Wiederholung.** Spezifikationen, Abnahmelisten, Hooks und Slash-Commands liegen projektübergreifend an einer Stelle und wirken in jedem Repository.

---

### Fähigkeiten

**Agentic & KI:** Claude Code (Hooks, Subagenten, Slash-Commands, Headless) · MCP — eigene Server bauen (TypeScript, FastMCP) und als Client konsumieren · Spec-Driven Development · Context & Prompt Engineering · Multi-Agent-Orchestrierung · parallele Agenten-Sessions (tmux, Git-Worktrees) · Evals & Laufzeit-Abnahme · RAG · OpenRouter-Kaskaden & Failover · LLM-Ops · Hermes Agent · OpenClaw / NemoClaw · Cursor · Codex

**macOS / iOS / Swift:** Swift 6 (Concurrency, Sendable) · SwiftUI · AppKit · TCA · GRDB (WAL, FTS5) · SpeechAnalyzer · AVFoundation / CoreAudio · ScreenCaptureKit · Vision (OCR) · CryptoKit · Global Hotkeys & MenuBar-Apps · SwiftPM & XcodeGen · TCC & App-Sandbox · Developer ID, codesign & notarytool · Sparkle · launchd

**Sprachen, Web & Daten:** Python · TypeScript / Node.js · JavaScript · PHP (5.6–8.3) · Bash · SQL · FastAPI · Pydantic · React · Vue.js · Laravel · Magento 2 · SQLite (WAL, FTS5) · PostgreSQL · MySQL · Redis · Elasticsearch · Playwright · CDP

**Infrastruktur & Betrieb:** Hetzner Cloud · Cloudflare (Tunnel, DNS, Edge-Cache) · Caddy · Docker / Docker Compose · Tailscale · systemd · Linux · idempotente & self-healing Deploys · Snapshot-Rollback · GitHub Actions · OpenTelemetry / OTLP · Grafana / Tempo · Tart-VMs

**Domänen:** Multimodale KI auf dem Gerät · On-Device-Inferenz & Local-First-Architektur · agentische Entwicklungssysteme & LLM-Ops · macOS-/iOS-Produktentwicklung · Recruitment-Tech / ATS-Automatisierung (DACH)

---

### Berufserfahrung vor der KI-Zeit

**Acht Jahre Festanstellung — Full-Stack, E-Commerce, APIs · 09/2016 – 01/2025**

- **Change IT Solutions GmbH** · Software Engineer · 10/2024 – 01/2025 — Migration der Entwicklungsumgebung auf Docker Compose, automatisierte Datenbankbereitstellung, KI-Einsatzszenarien zur Prozessautomatisierung.
- **Rissc Solutions GmbH** · Software Engineer · 02/2018 – 07/2024 — Web2Print-Editor in Laravel; Eigenverantwortung für mehrere Magento-2-Kundenshops inkl. Customization-Plugin, Multi-Store und Payment-Gateways; RESTful APIs; Docker-Entwicklungsumgebung von Laravel auf Magento 2 übertragen; CI/CD, Monitoring, Backups.
- **Full-Stack Engineer** · Karlsruhe · 06/2017 – 12/2017 — Web-Lösungen für Großkunden der Telekommunikationsbranche; PHP/Zend, MySQL, jQuery.
- **redhotmagma GmbH** · Full-Stack Engineer · 09/2016 – 03/2017 — Web-Anwendungen in agilen Teams; HTML5, CSS3, JavaScript, Three.js.

**Ausbildung:** Fachinformatiker für Anwendungsentwicklung (Peter Kwasny GmbH, 2013 – 2016) · Técnico en Sistemas Microinformáticos y Redes (Spanien, 2010 – 2013) · Mittlere Reife (Spanien, 2003 – 2008), dreisprachig aufgewachsen.

---

### Was ich mitbringe — und wofür

- **Ausliefern statt vorführen.** Signierte, notarisierte Verteilung mit eigenem Update-Kanal und Diagnose-Rückkanal. Ein Prototyp, der nur in der Vorführung läuft, hätte mich am selben Tag getroffen — ich war Entwickler und Anwender in einer Person.
- **Bewerten statt hoffen.** Jedes Feature hat ein Abnahmekriterium, bevor es Code hat.
- **In fremden Stacks schnell handlungsfähig.** Von null Swift auf 145.000 Zeilen in neun Monaten — samt Nebenläufigkeit, Datenschicht, Systemframeworks und Auslieferungskette. Die Sprache war der kleinste Teil. Was ich noch nicht kenne, gehe ich denselben Weg: Muster zuerst, Vokabular danach.
- **Datenhoheit, wo sie verlangt wird.** Voller KI-Zugriff auf sensible Daten, ohne dass sie das Gerät verlassen.

**Was ich suche:** eine Rolle, in der KI in Betrieb gehen soll statt vorgeführt zu werden — mit viel eigener Verantwortung, an einem tiefen statt breiten Problem, gern dort, wo Daten das Haus nicht verlassen dürfen. Was mir dafür noch fehlt, hole ich mir; die letzten anderthalb Jahre sind der Beleg dafür.

[agentic-engineer.online](https://agentic-engineer.online) · [GitHub orcasai](https://github.com/orcasai) · [Voice Pitch auf LinkedIn](https://www.linkedin.com/posts/robin-s-223606136_hiermit-lade-ich-alle-ein-mit-mir-ins-gespr%C3%A4ch-activity-7434159927142801408-2yGt/)
