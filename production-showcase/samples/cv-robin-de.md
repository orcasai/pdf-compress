<div class="cv-photo-gutter"></div>

# Robin Walter Scherler

**Agentic Engineer · AI Engineer · Software Engineer · macOS/iOS Engineer**

Neidenstein, Deutschland · scherler89@gmail.com · +49 1627308662 · Geb. 24.08.1989 · Nationalität Deutsch · Pkw-Klasse B · Sprachen: Deutsch, Englisch, Spanisch, Katalanisch

---

### Über Mich

> **Am 27. November 2025 habe ich meine erste Zeile Swift geschrieben. Neun Monate später stehen 158.000 Zeilen Swift 6 in drei eigenen Apple-Produkten** — 2.666 Commits, alleiniger Entwickler, jedes Feature mit Spezifikation und Laufzeit-Abnahme.

Davor zehn Jahre Web, im Kern PHP, Laravel und Magento 2. Der Sprung ging nicht über schnelleres Tippen, sondern über eine andere Arbeitsweise. Ich schreibe Spezifikationen, Schnittstellen-Verträge und Abnahmekriterien — die Implementierung entsteht agentisch dagegen. Die Vorrichtungen, die das verlässlich machen, habe ich selbst gebaut: Guards, die vor dem Werkzeugaufruf greifen, Abnahme in wegwerfbaren VMs, ein eigener MCP-Server als Schnittstelle meiner Agenten auf mein Produkt.

**Die Programmiersprache ist damit zweitrangig geworden — die Muster nicht.** Ob Laravel-Service, SwiftUI-View oder FastAPI-Route: Was trägt, sind saubere Schnittstellen, ein klares Zustandsmodell, die Trennung von Domäne und Oberfläche, Idempotenz und Tests als Vertrag. Genau diese Muster prüfe ich an jeder agentisch erzeugten Zeile — sie sind der Grund, warum Swift 6 nach neun Monaten kein fremdes Land mehr ist. **Fertig heißt bei mir im echten System bewiesen** — nicht Build grün, nicht Unit-Tests grün.

Die Arbeitsteilung dahinter ist keine Einbahnstraße: Ich setze Rahmen, Muster und Abnahmemaß, die Agenten tragen die Ausführung, und beides verbessert sich mit jeder Runde. **KI und ich sind ein eingespieltes Team** — das ist der Grund für jede Zahl in diesem Lebenslauf.

*3.937 eigene Commits in 18 Monaten, 1.737 davon in den letzten beiden — der Sprung fällt mit dem Moment zusammen, in dem mein Agent-Harness stand.*

---

### Wie Entwicklung sich gerade verschiebt

Die Werkzeuge sind schneller geworden, die Verfahren nicht. Vorab festgelegte Schnittstellen stammen aus einer Zeit, in der eine Iteration Wochen kostete — sie später zu ändern war teurer, als sie vorher richtig zu raten. Mit einem funktionierenden Agent-Harness kostet sie Stunden, und die Rechnung dreht sich um.

An die Stelle der Vorabfestlegung tritt keine Beliebigkeit, sondern ein kürzerer Vertrag: Spezifikation und Abnahmekriterium pro Inkrement statt fürs ganze Produkt. **Die Architektur folgt damit der Erkenntnis statt der Annahme** — sichtbar an 264 von 1.815 Commits, die reine Spezifikation und Abnahme sind und über drei Monate verteilt liegen statt in einer Entwurfsphase gebündelt.

Ich nenne es **Iteration-First**: weniger ein neues Muster als die Konsequenz daraus, dass Erkenntnis inzwischen billiger ist als Annahme.

---

### Parallel arbeiten — planen, laufen lassen, weiterbauen

Meine Arbeitsweise ist auf Parallelität ausgelegt: Spezifikation schreiben, einen Agenten daraufsetzen, währenddessen am nächsten Strang weiterbauen. Nachweisbar aus den Sitzungsdaten der letzten drei Monate:

- **167 Agenten-Sessions über 119 getrennte Terminal-Panes** — bis zu 17 an einem einzigen Arbeitstag, in der Spitze 26 gleichzeitig offene Sitzungen.
- **14 aktive Git-Worktrees, 40 Branches** nebeneinander: jeder Strang in eigenem Arbeitsverzeichnis, damit gleichzeitige Läufe sich nicht in die Quere kommen.
- **Guards machen unbeaufsichtigte Läufe erst möglich.** Ein Agent ohne Aufsicht braucht Vorrichtungen, die falsche Abzweigungen vor dem Werkzeugaufruf abfangen. Ohne sie skaliert Parallelität nicht — sie vervielfacht nur die Fehler.
- **Skalierung heißt Wiederverwendung.** Spezifikationen, Abnahmelisten, Hooks und Slash-Commands liegen projektübergreifend an einer Stelle und wirken in jedem Repository. Ein verbesserter Workflow greift sofort überall.

*Ein Tag, abgelesen am Commit-Log — der 28. August 2026:* 09:44 eine Messung, die einen Refactor bestätigte. 16:16 Build 1669 ausgeliefert. 17:04 bis 21:12 Spezifikation und Zehn-Schritte-Plan für den nächsten Umbau. Am Abend, parallel dazu, dieser Lebenslauf. Dreizehn Feature-Zweige standen daneben, ein weiteres Projekt lief an. **Der Lebenslauf war der kleinste Posten des Tages.**

**Geteilte Domänen statt einer Datenbank**

Dieselbe Idee trägt die Architektur meines aktuellen Produkts: Die Datenhaltung ist in getrennte **Domänen** zerlegt — eigenständige Datenwelten mit je eigener Datenbank, zwischen denen Einträge bewusst transferiert werden, statt zu verschmelzen. Eine eigene Koordinationsschicht mit Transfer-Journal und Austauschprotokoll hält sie konsistent. Querschnitts-**Entitäten** liegen quer dazu und greifen polymorph über alle Eintragstypen.

Das parallelisiert Wissensarbeit: mehrere Kontexte gleichzeitig offen, ohne dass eine Abfrage versehentlich über eine Grenze liest — Privacy-by-Architecture als Bauweise, nicht als Absichtserklärung.

---

### Eigene Produkte — Apple-Plattform

**Aktuelles macOS-Produkt — multimodale KI-Erfassung, vollständig auf dem Gerät · alleiniger Entwickler · seit 05/2026**

101.000 Zeilen Swift 6, 1.815 Commits, 267 Test-Dateien in drei Monaten — rund 1.000 Zeilen Produktivcode pro Tag, jeden Tag, inklusive Spezifikation und Abnahme. Mehrere Datenmodalitäten mit je eigenem Erfassungs-, Verarbeitungs- und Persistenzpfad — sämtlich auf dem Gerät, kein Fremdanbieter im Datenpfad.

- **Live-Betrieb als Dauertest — von einem einzigen Nutzer.** 16.785 erfasste Einträge an 89 aktiven Tagen, im Schnitt 189 pro Tag, Spitzentag 475. Keine Seed- oder Testdaten: Entwickler und einziger Anwender in einer Person, jeder Fehler trifft mich am selben Tag.
- **Spezifikation vor Code.** 264 der 1.815 Commits betreffen ausschließlich Spezifikation und Abnahme. Jedes Feature läuft Spec → Umsetzungsplan → Laufzeit-Abnahme.
- **Abnahme als Infrastruktur — vom Agenten selbst durchgeführt.** Laufzeit-Tests in wegwerfbaren Tart-VMs, die den Nullzustand beliebig oft herstellen: Erstinstallation, Gatekeeper, Berechtigungen reproduzierbar statt einmalig. Der Agent klont die VM, spielt den Ausgangsbestand ein, **bedient die Oberfläche per AppleScript und prüft das Ergebnis selbst** — jeder Arbeitsstrang mit eigener Testumgebung, mehrere parallel. Abnahmeplan von 5.300 Zeilen, plus getrennte Liste für alles, was erst Zeit beantworten kann.
- **Guards statt Nacharbeit.** Jeder Fehler, der einmal durchkam, wird zu einer Vorrichtung, die ihn ausschließt — PreToolUse-Hooks, die vor dem Werkzeugaufruf greifen statt nach dem Fehlschlag zu melden.
- **Auslieferungsreife als eigene Disziplin.** Developer-ID-Signatur, Notarisierung, Sparkle-Appcast mit EdDSA, Diagnose-Rückkanal und Absturzberichte aus installierten Ständen. Ein Befehl baut das Testerpaket — notarisiertes DMG, signierte CLI, MCP-Server, Agenten-Setup, README — in zwei Sorten: still für Kunden, mit Telemetrie und eigenem Update-Kanal fürs Team; drei Update-Kanäle nebeneinander, die Notarisierung erkennt Voll- und Lokalmodus selbst. Zwei-Rechner-Betrieb in der VM abgenommen (20/20). Zwei Auslieferungsziele aus einer Codebasis über eine Build-Konfigurationsachse: sandboxed App-Store-Variante, Developer-ID-Variante; App-Store-Einreichung vorbereitet. Mehrnutzerbetrieb über OAuth2 auf eigenem Host geplant, Auslöser ist der zweite externe Nutzer.
- **Eigener MCP-Server** (TypeScript) als Agenten-Schnittstelle auf das Produkt — meine Agenten arbeiten produktiv gegen meine eigene Anwendung.
- **Zweite Plattform in fünf Tagen.** Eigene iOS-App mit 8.800 Zeilen Swift 6 und 208 Commits, vom leeren Projekt bis zum Gerät. Sie hängt an derselben Schnittstelle wie MCP-Server und macOS-Oberfläche — ein Bestand, eine Schnittstelle, drei Konsumenten, eine Stelle für Fehler. Zwischen den Geräten läuft alles Ende-zu-Ende verschlüsselt über WireGuard im eigenen Tailnet; die Netzgrenze ist die Autorisierung, bewusst kein zweiter Token. Schreibzugriffe append-only, per Whitelist begrenzt und idempotent per ID: Ein doppelter Versand ändert nichts.
- **Observability von Anfang an:** OpenTelemetry/OTLP-Spans in Grafana Tempo, Unified Logging über OSLog.

*Wie sich daraus ein Produkt fügt, zeige ich bei beidseitigem Interesse gern live. Ein Beleg steht aber schon hier: Das System hält Kontext über die eigene Arbeit — Ideen, Erfahrungen, Denkwege — und genau daraus ist dieser Lebenslauf entstanden. Die Zahlen oben hat ein Agent über seinen MCP-Server ausgelesen.*

**Hermes-Companion — macOS-MenuBar-App mit iOS-Begleiter · alleiniger Entwickler · 11/2025 – 06/2026**

Sprachgesteuerte Begleit-App für eine quelloffene Agenten-Plattform: 48.000 Zeilen Swift, 643 Commits, ein geteiltes Modell hinter zwei Oberflächen (macOS-Target und eigenes iOS-Target im selben Projekt).

- **Transkription auf dem Gerät** — drei Engines produktiv gefahren und gemessen: Whisper, Parakeet V3 über FluidAudio, Apple Speech. Im Nachfolgeprodukt auf Apples SpeechAnalyzer konsolidiert, sobald die Systemlösung in Genauigkeit und Latenz vorne lag: kein ausgeliefertes Fremdmodell mehr, kein Download, kein Speicherbudget.
- **Agenten-System** mit eigenem Hotkey, Modell und System-Prompt je Agent; Antworten mehrerer Modelle direkt vergleichbar, Prompt zur Laufzeit editierbar.
- **OpenRouter-Kaskade** über 100+ Modelle mit Verfügbarkeitsprüfung und Failover.
- **Zwei Agenten-Backends evaluiert, eines behalten.** Anbindung an Hermes über dessen multimodale API und SSE-Event-Streams, parallel an OpenClaw — am Ende vollständig auf Hermes konsolidiert, weil es besser trug. Slack als zweiter Kanal, Container-Status im iOS-Begleiter.
- **The Composable Architecture (TCA)** als durchgehendes Zustandsmodell über beide Plattformen.
- **CI-Gate seit 02/2026:** GitHub Actions mit Branch-Protection, automatisches Changelog über alle Repos, Build-Status und PR-Anfragen in Slack.

---

### Live-System & Deploy-Pipeline auf eigener Infrastruktur

**[agentic-engineer.online](https://agentic-engineer.online) — öffentlich testbares Recruiting-Werkzeug · alleiniger Entwickler · Entwicklung 04 – 05/2026, seither im Betrieb**

Firmenname und Website hinein, strukturiertes Firmenprofil mit offenen Stellen heraus. Aus einer Bewerbungsaufgabe entstanden — seither als eigenes Produkt weiterbetrieben und öffentlich testbar.

- **Kaskade statt einem Modell.** Sechs Modelle in Reihe, Free-Tier zuerst, zwei bezahlte Auffangstufen greifen erst bei 429 — **im gemessenen Betrieb 100 % Antwortquote bei unter 1 Cent pro Lead.** Die Architektur kennt die Kosten vor der Anfrage, nicht danach.
- **Acht ATS-Adapter** (Personio, Recruitee, Greenhouse, Lever u. a.) ziehen Stellendaten direkt aus den Widget-APIs; die LLM-Extraktion gegen Pydantic-Schema ist der generische Auffang gegen Schema-Drift. Vier Adapter live gegen echte Firmen-URLs verifiziert.
- **Gemessen, nicht geschätzt:** 15–40 s Extraktions-Latenz, 72 Unit- und 4 E2E-Tests, rund 75 % Real-World-Coverage. Mobile-Navigation von 8,7 s auf 1,5 s (5,8×) nach Cloudflare-Edge-Tuning.
- Python 3.11 · FastAPI · httpx · BeautifulSoup4 · SQLite · Jinja2 · Resend — auf einem Hetzner-VPS hinter einem outbound-only Cloudflare-Tunnel.

**Deploy-Pipeline aus Bausteinen — von blankem Ubuntu bis Produktion**

Die Infrastruktur hinter meinen Systemen ist selbst ein Produkt: zwölf wiederverwendbare Bausteine (Basis, Tunnel, Tailscale, Observability, Relays, Backup), aus denen jede Serverinstanz als Phasenliste zusammengesetzt wird.

- **Drei Skriptfamilien je Phase:** vorwärts ausrollen, Rückfallpunkt setzen, auf eine Phase zurückfallen. Bricht ein Schritt, geht es auf den letzten sauberen Stand zurück, das Skript wird angepasst, der Lauf wiederholt — statt von Hand nachzubessern.
- **Entscheidungsbaum statt Bauchgefühl:** Skript geändert → kompletter Neuaufbau ab blankem Ubuntu. Nur der Serverzustand kaputt → Rückfall auf die betroffene Phase. Im Zweifel der teure Weg, weil er in rund drei Minuten durchläuft.
- **Zwei Server laufen parallel** ohne Abhängigkeit voneinander; beide Pipelines starten gleichzeitig.
- Software-Praxis im Deployment: idempotente Schritte, versionierte Bausteine, ein dokumentierter Grund je Entscheidung — dieselbe Disziplin wie im Anwendungscode.

[Session-Clip ansehen](https://agentic-engineer.online/library#clip-1) · [Voice Pitch — ich stelle mich per Sprache vor, meine App antwortet und ist mit meinem Slack-Channel verbunden](https://www.linkedin.com/posts/robin-s-223606136_hiermit-lade-ich-alle-ein-mit-mir-ins-gespr%C3%A4ch-activity-7434159927142801408-2yGt/)

---

### Portfolio

- [agentic-engineer.online](https://agentic-engineer.online) — Live-Demo auf eigener Infrastruktur, inkl. [Session-Clip](https://agentic-engineer.online/library#clip-1).
- [GitHub orcasai](https://github.com/orcasai) — eigene Projekte neben vielen Forks. Die Forks sind der frühe Teil des Weges: erst lesen und sammeln, was andere bauen, dann eigene Werkzeuge daraus ableiten, heute eigene Produkte planen, bauen und betreiben. Wer die Historie liest, sieht diesen Weg — und dass die Commits der letzten anderthalb Jahre in eigenen Repositories liegen.
- [Voice Pitch](https://www.linkedin.com/posts/robin-s-223606136_hiermit-lade-ich-alle-ein-mit-mir-ins-gespr%C3%A4ch-activity-7434159927142801408-2yGt/) — persönliche Vorstellung, live per Sprache in der von mir entwickelten App.

---

### Fähigkeiten

**Agentic & KI:** Claude Code (Hooks, Subagenten, Slash-Commands, Headless-Mode) · MCP — eigene Server bauen (TypeScript, FastMCP) und als Client konsumieren · Spec-Driven Development · Context Engineering · Prompt Engineering · Multi-Agent-Orchestrierung · parallele Agenten-Sessions (tmux, Git-Worktrees) · Evals & Laufzeit-Abnahme · RAG / LLM-Knowledge-Compiler · OpenRouter-Modell-Kaskaden & Failover · LLM-Ops / OpenAI-Wire-Protocol-Gateways · Agentic Loops (ReAct) · Hermes Agent (Nous Research) · OpenClaw / NemoClaw · Cursor · Codex

**macOS / iOS / Swift:** Swift 6 (Concurrency, Sendable, Synchronization) · SwiftUI · AppKit · The Composable Architecture (TCA) · Observation · GRDB (WAL, FTS5) · SpeechAnalyzer / SpeechTranscriber · AVFoundation / AVAudioEngine / CoreAudio · ScreenCaptureKit · Vision (OCR) · HealthKit · CoreMotion · CoreImage / CoreGraphics / ImageIO · CryptoKit · NaturalLanguage · PDFKit · Rive · Global Hotkeys & MenuBar-Apps (NSStatusItem) · CGEvent / ApplicationServices · Swift ArgumentParser (CLI) · SwiftPM & XcodeGen · App Group · TCC-Permissions & App-Sandbox · Developer ID, codesign & notarytool · Sparkle (Appcast, EdDSA) · LaunchAgents / launchd

**Architektur & Daten:** Domänen-getrennte Datenbanken mit Transfer-Journal · polymorphe Entitäten über Eintragstypen · SQLite (WAL, FTS5) · GRDB · PostgreSQL · MySQL / MariaDB · Redis · Elasticsearch · JSON / JSON-LD / Schema.org · XML · YAML · Markdown · CSV

**Testing, Auslieferung & Observability:** Swift Testing & XCTest · Unit- und Integrationstests · Laufzeit-Abnahme in Tart-VMs · Testplan- und Langzeittest-Praxis · PreToolUse-Guards für Agenten · GitHub Actions (CI-Gate, Branch-Protection, Changelog) · Bitbucket Pipelines · Conventional Commits · Git-Worktrees & stacked branches · OpenTelemetry / OTLP · Grafana / Tempo · OSLog / Unified Logging · Diagnose-Rückkanal & Absturzberichte

**Infrastruktur & DevOps:** Hetzner Cloud (VPS, API-Rebuilds, Snapshot-Pipelines) · Cloudflare (Tunnel, DNS / SPF / DKIM / DMARC, Edge-Cache) · Caddy · Docker / Docker Compose · Tailscale (SSH / ACL) · systemd · UFW · Linux (Debian / Ubuntu) · frpc · rsync · idempotente & self-healing Deploys · Snapshot-Rollback · uv · Resend

**Sprachen & Web-Stack:** Swift · Python · TypeScript / Node.js · JavaScript · PHP (5.6–8.3) · Bash / Shell · SQL · HTML / CSS · FastAPI / Starlette / uvicorn · Pydantic · Jinja2 · React · Vue.js · Laravel · Magento 2 · React Native · Three.js · Electron · Playwright · Chrome DevTools Protocol (CDP) · PyMuPDF · Pillow · Slack Bolt · ffmpeg · Bun · zod

**Methoden:** Iteration-First (Architektur folgt der Erkenntnis) · Spec-Driven Development · abnahmegetriebene Entwicklung · Parallelisierung über isolierte Arbeitsverzeichnisse · Context Engineering (Target-State) · idempotente Deploy-Pipelines & Snapshot-Rollback · PRD-First Feature Development · Privacy-by-Architecture / Data Sovereignty · CLI-over-MCP · Zusammenarbeit mit nicht-technischen Stakeholdern

**Domänen:** Multimodale KI auf dem Gerät · On-Device-Inferenz & Local-First-Architektur · agentische Entwicklungssysteme & LLM-Ops · macOS-/iOS-Produktentwicklung · Recruitment-Tech / ATS-Automatisierung (DACH)

---

### Berufserfahrung vor der KI-Zeit

**Acht Jahre Festanstellung — Full-Stack, E-Commerce, APIs · 09/2016 – 01/2025**

- **Change IT Solutions GmbH** · Software Engineer · 10/2024 – 01/2025 — Migration der Entwicklungsumgebung auf Docker Compose, automatisierte Datenbankbereitstellung, KI-Einsatzszenarien zur Prozessautomatisierung.
- **Rissc Solutions GmbH** · Software Engineer · 02/2018 – 07/2024 — Web2Print-Editor zur Produkt-Individualisierung in Laravel; Eigenverantwortung für mehrere Magento-2-Shops inkl. Customization-Plugin, Multi-Store und Payment-Gateways; RESTful APIs zwischen Editor, Druckinfrastruktur und Shops; **Docker-Entwicklungsumgebung von Laravel auf Magento 2 übertragen** — dort gab es sie vorher nicht; CI/CD, Monitoring und Backups der Produktionsumgebung.
- **Full-Stack Engineer** · Karlsruhe · 06/2017 – 12/2017 — Web-Lösungen für Großkunden der Telekommunikationsbranche; PHP/Zend, MySQL, jQuery/AJAX, MVC und Plugin-Systeme.
- **redhotmagma GmbH** · Full-Stack Engineer · 09/2016 – 03/2017 — Web-Anwendungen in agilen Teams; HTML5, CSS3, JavaScript, Three.js.

---

### Ausbildung

**Fachinformatiker für Anwendungsentwicklung** · Peter Kwasny GmbH, Gundelsheim · 2013 – 2016. Davor **Técnico en Sistemas Microinformáticos y Redes** (IES Marcos Zaragoza, Spanien, 2010 – 2013) und **Mittlere Reife** (IES Castelló d'Empúries, Spanien, 2003 – 2008) — dreisprachig aufgewachsen: Spanisch, Katalanisch, Englisch.


---

### Datenhoheit als Architektur — und was ich unter Production verstehe

**Multimodale KI auf dem eigenen Gerät · täglich im Einsatz**

Laufend anfallende Arbeitsdaten mit hohem Personenbezug sind das Sensibelste, was ein Arbeitsrechner überhaupt zu sehen bekommt. Die übliche Antwort darauf ist Verschlüsselung in der Cloud. Meine Antwort ist, dass die Daten meine eigenen Geräte gar nicht erst verlassen.

- **Alles auf dem Gerät.** Transkription über Apples SpeechAnalyzer lokal, Persistenz in SQLite mit Volltextindex, kein Backend im Datenpfad, kein Fremdanbieter, kein Modell-Download. Diese Entscheidung ist bewusst gefallen — nicht aus Mangel an Infrastruktur, sondern weil sie bei diesen Daten die richtige ist.
- **Domänen als Grenzen.** Getrennte Datenbanken statt einer mit Mandantenspalte: Eine Abfrage *kann* nicht über eine Grenze lesen. Datenschutz als Bauweise statt als Einstellung.
- **Was sich bewegt, bewegt sich verschlüsselt.** Gerät zu Gerät über WireGuard im eigenen Tailnet, kein fremder Server im Weg; Update-, Diagnose- und Telemetriekanal über TLS; Sicherungen als authentifiziert verschlüsselte Archive, Schlüssel im Schlüsselbund — im Notfall mit Bordmitteln des Systems lesbar, ohne das Produkt.
- **Und trotzdem für KI nutzbar.** Ein eigener MCP-Server öffnet den gesamten Bestand strukturiert für Agenten — lokal, ohne dass ein Byte das Gerät verlässt. Genau das Problem, das Unternehmen unter DSGVO und AI Act haben, in meiner eigenen Umgebung gelöst und im Alltag bewiesen.
- **Lokal heißt begrenzt — also gehört Retention zur Architektur.** Wer alles auf dem Gerät hält, hat keinen elastischen Speicher. Seit Tag eins läuft ein Aufräumdienst im Produkt; der rollierende Pruner arbeitet bewusst **ohne VACUUM**, weil das kurzzeitig doppelten Platz bräuchte. Cleanup läuft abseits des Hauptthreads, Build-Artefakte und Wegwerf-VMs haben definierte Lebenszyklen.
- **Die Plattform ist kein Kompromiss, sondern Voraussetzung.** Das Ganze läuft samt paralleler VM-Testumgebungen auf einem einzelnen Mac mini mit 256 GB. On-Device-Inferenz, Tart-VMs und Notarisierung gibt es nur hier — nicht die meisten Ressourcen, aber die richtige Umgebung, gezielt gewählt.
- **Production heißt nicht eine Million Kunden.** Es heißt: ein System, das jeden Tag echte Arbeit trägt und bei Ausfall echten Schaden anrichtet. Genau das ist meines seit dem ersten Tag — diese Erfahrung habe ich mir nicht angelesen.

---

### Was ich mitbringe — und wofür

Ich habe in einer Umgebung, die ich vollständig selbst verantworte, den kompletten Weg gemacht: Problem verstanden, System gebaut, in den Produktivbetrieb gebracht, betrieben, gemessen, nachgeschärft. Ohne Entwicklerteam, ohne Sicherheitsnetz, mit KI als Verstärker.

- **Ausliefern statt vorführen.** Signierte und notarisierte Verteilung, eigener Update-Kanal, Diagnose-Rückkanal aus installierten Ständen. Ein Prototyp, der nur in der Vorführung läuft, hätte mich am selben Tag getroffen — ich war Entwickler und Anwender in einer Person.
- **Bewerten statt hoffen.** Jedes Feature hat ein Abnahmekriterium, bevor es Code hat: 5.300 Zeilen Abnahmeplan, Laufzeit-Tests in wegwerfbaren VMs, eine getrennte Liste für alles, was erst Zeit beantworten kann.
- **In fremden Stacks schnell handlungsfähig.** Von null Swift auf 158.000 Zeilen in neun Monaten — samt Nebenläufigkeitsmodell, Datenschicht, Systemframeworks und kompletter Signatur- und Auslieferungskette. Die Sprache war dabei der kleinste Teil. Was ich noch nicht kenne, gehe ich denselben Weg: Muster zuerst, Vokabular danach.
- **Nicht-technische Menschen mitnehmen.** Mein Projektpartner ist kein Entwickler. Ideen, Einwände und Testeindrücke kommen in Alltagssprache an; zurück gehen Anleitungen in Muss und Kann, damit ein neuer Stand ohne Rückfrage installiert ist, und Abnahmepläne, die ohne Code lesbar sind. Acht Jahre Kundenprojekte davor haben dasselbe verlangt: technisch tief bauen, verständlich übersetzen — in beide Richtungen.
- **Datenhoheit, wo sie verlangt wird.** Vollständiger KI-Zugriff auf sensible Daten, ohne dass sie das Gerät verlassen. Genau die Bedingung, unter der viele Unternehmen unter DSGVO und AI Act überhaupt erst anfangen können.
- **Kontext als Kernkompetenz.** Ideen, Erfahrungen und Denkwege so verfügbar zu halten, dass KI daraus etwas bauen kann, das trägt — dafür habe ich mein System gebaut, und dieser Lebenslauf ist daraus entstanden. Die Zahlen darin hat ein Agent über meinen eigenen MCP-Server ausgelesen.

**Was ich suche:** eine Rolle, in der KI in Betrieb gehen soll statt vorgeführt zu werden — mit viel eigener Verantwortung, an einem tiefen statt breiten Problem, gern dort, wo Daten das Haus nicht verlassen dürfen. Was mir dafür noch fehlt, hole ich mir; die letzten anderthalb Jahre sind der Beleg dafür. **Dieselbe Disziplin, dieselbe Bauweise — angewendet auf das Problem eines Unternehmens.**
