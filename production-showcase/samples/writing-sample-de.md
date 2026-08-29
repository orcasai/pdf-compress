# Writing Sample — Robin Walter Scherler

**Robin Walter Scherler · 18. Mai 2026 · Live-Demo:** [agentic-engineer.online](https://agentic-engineer.online)

> **Einordnung:** Bislang betreibe ich Production-LLM-Systeme in eigenem Setup und als öffentlich testbare Demo — die Lieferung an Dritte ist der nächste Schritt. Dieses Beispiel ist eine Recruitment-Probearbeit, die ich seither als eigenes Demo- und Lernprojekt selbst betreibe. Es zeigt, *wie ich Entscheidungen treffe und Trade-offs verantworte*. Seit anderthalb Jahren wechsele ich bewusst aus dem reinen Entwickler-Modus in die Owner-Rolle für KI-Lösungen — weil verantwortungsvolle KI-Arbeit Gesamt-Verantwortung verlangt, vom Schema bis zum Hosting. Den Ansatz, der diese Arbeit zusammenhält, nenne ich **Empirical Context Reinforcement**: sessionübergreifendes, empirisch verstärktes Bauen mit dem Kontext, der Wert trägt. Jeden Trade-off auf dieser Seite vertrete ich zu 100 % selbst.

---

### 1. Was war das Problem?

Der Brief beschrieb eine Web-Scraping-Aufgabe. Das eigentliche Problem, wie ich es zugeschnitten habe: **LLM-Extraktion muss reproduzierbar, billig und immer verfügbar sein** — sonst baut man Demoware, die unter Last bricht. Drei Bruchpunkte, die ich vor dem ersten Commit identifiziert und als Risiken festgehalten habe:

- **Schema-Drift.** Ohne explizites Datenmodell hat jede LLM-Antwort eine andere Form. Downstream-Tools brechen, sobald ein Feld fehlt oder anders heißt.
- **Korrelierte Rate-Limits.** Kostenlose OpenRouter-Modelle teilen sich denselben Venice-Provider und 429en oft gleichzeitig — eine Single-Modell-Lösung antwortet dann gar nicht.
- **Kostendecke.** Ohne harten Cap pro Lead skaliert eine KI-Lösung im Sales-Enablement-Kontext nicht. Die Architektur muss die Kosten *vor* jeder Anfrage kennen, nicht im Nachhinein.

### 2. Was habe ich gemacht?

Eine FastAPI-App mit asynchroner Job-Pipeline, jede Komponente von mir allein entschieden, gebaut und betrieben: Scraper findet die Karriere-Seite über URL- und Anchor-Text-Scoring → eine Kette aus acht ATS-Adaptern (Personio, Recruitee, Greenhouse, Lever u.a.) extrahiert Job-Daten direkt aus den jeweiligen Widget-APIs, LLM-Extraktion gegen Pydantic-Schema dient als generischer Fallback → Persistenz in SQLite → Bestätigungsmail via Resend, mit HTML-Preview-Fallback auf Disk bei unverifizierter Domain. Die Pipeline meldet jeden Stop sichtbar im HTML-Audit-Trail.

**Stack:** Python 3.11 · FastAPI + Uvicorn · httpx + BeautifulSoup4 · OpenRouter (6er-Modell-Kaskade via OpenAI-SDK) · SQLite · Jinja2 · Resend.

Was diese Arbeit kennzeichnet: mit KI-Tools lernen, während ich sie verwende — Agentic Engineering im wörtlichen Sinn.

**Drei Trade-offs, die ich heute genauso wieder treffen würde:**

- **SQLite statt Postgres.** Single-Tenant-Scope braucht keinen DB-Server. Bewusste Schuld, deren Trigger ich kenne — Upgrade-Pfad steht in §4.
- **6er-Modell-Kaskade statt Single-LLM.** Free-Tier zuerst, zwei Paid-Safety-Nets greifen erst bei 429. Hält die Antwort-Garantie bei kontrollierten Kosten und bleibt stabil bei Provider-Wechseln.
- **Self-hosted Hetzner-VPS hinter Cloudflare-Tunnel statt Managed-Cloud.** Outbound-only Tunnel, volle Datenhoheit, freie Provider-Wahl. Bei einer KI-Lösung halte ich die Kontrolle bei mir.

### 3. Was war das messbare Ergebnis?

Alle Werte sind am laufenden System gemessen — jede davon ein gesetztes Akzeptanz-Kriterium, das ich mir vor dem ersten Commit definiert habe.

| Metrik | Wert |
| --- | --- |
| Extraktions-Latenz | 15–40 s pro Firma |
| Kosten pro Lead (Paid-Fallback-Stufe) | < 1 Cent |
| Mobile-5-Page-Nav (iOS Safari, Singapore-Edge) | 8,7 s → 1,5 s (5,8×) nach Cloudflare-Edge-Cache-Tuning |
| Antwort-Verfügbarkeit | 100 % — Kaskade liefert eine Antwort, Mailer-Fehler werden im HTML-Audit-Trail gefangen |
| Coverage | ~75 % Real-World — 4 von 8 ATS-Adaptern (Personio, Recruitee, Greenhouse, Lever) live gegen echte Firmen-URLs verifiziert; 72 Unit-Tests + 4 E2E-Live-Tests grün |

Coverage als hartes Akzeptanz-Kriterium ist meiner Erfahrung nach die einzige verlässliche Form messbarer Code-Qualität — und diese Disziplin überträgt sich 1:1 auf jedes Skalierungs-Problem in Production: der Tech-Stack folgt der Test-Szenario-Definition, in dieser Reihenfolge.

System läuft seit der Probearbeit unter eigener Infrastruktur weiter und ist öffentlich testbar.

### 4. Was würde ich heute anders machen?

**Auf Engineering-Ebene halten alle Entscheidungen.** Jede Schuld ist bewusst aufgenommen, mit bekanntem Upgrade-Pfad und definiertem Auslöser:

- **Postgres** statt SQLite — sobald Multi-Tenancy gebraucht wird.
- **Server-Sent-Events** statt 800-ms-Polling auf `/api/status/{id}` — sobald UX-Feinheit zählt.

**Auf Präsentations-Ebene würde ich konsolidieren.** Das Video, das ich für diese Bewerbung produziert habe, trägt noch stellenspezifische Bezüge. Künftig schneide ich es als eigenständiges Owner-Asset — eine sorgfältig vorbereitete Stunde, die meine Arbeitsweise unabhängig vom konkreten Anlass darstellt. So lässt sich dasselbe Material für Presse-Beiträge, Fachartikel oder die Firmen-Präsentation einsetzen, wenn ein Unternehmen mich als Mitarbeiter vorstellt. Selbe Owner-Logik wie beim Stack: einmal richtig bauen, dauerhaft einsetzen.

**Auf Owner-Ebene habe ich von Anfang an für Wiederverwendung gebaut**: Stack, Layout und Extraktions-Pipeline sind bewusst so gewählt, dass sie in meinen eigenen Projekten weiterleben — unabhängig vom Ausgang dieser Bewerbung. Aus diesem Prototyp ist ein Werkzeug geworden, das ich täglich nutze und gegen das ich eigene Produkte teste — Entwickler und strengster Kunde meiner KI-Arbeit in einer Person.

Dieselbe Owner-Logik trägt die Infrastruktur darunter. Die Site läuft als eine Station in meiner mehrstufigen Hetzner-Pipeline (Ubuntu-Rebuild → Stage-Snapshots → Multi-Site-Cloudflare-Tunnel) — eine Pipeline, die ich ursprünglich für eigene KI-Projekte schrittweise aufgebaut und für diese Site erweitert habe. Sie wird AI-orchestriert betrieben: bricht ein Deploy-Schritt, fällt das System auf den letzten sauberen Snapshot zurück, das Skript wird angepasst, der Test wiederholt — empirisch, test-getrieben, ohne Hand-Tuning. Das ist der Empirical-Context-Reinforcement-Loop, den ich projektübergreifend fahre. Für Scaling auf viele Kunden wäre die Basis-Wahl Kubernetes + Terraform auf Docker — gesetzt, sobald das tatsächlich gebraucht wird, und erst dann.

Diese Verantwortung habe ich auf eigenes Risiko übernommen — und würde sie für jedes Projekt in einem Unternehmen genauso tragen.

---

*Zwei Beobachtungen als Eckdaten zu meiner Position im Feld:*

*Lokal gehöre ich zu den wenigen, die zwei voll funktionsfähige Claude-Code-Sessions (eigene MCP-Server, eigene Slash-Command-Erweiterungen, jeweils mit Projekt- und Session-Kontext beladen) projektübergreifend so orchestrieren, dass sie aus ihren Kontexten heraus mit mir und miteinander präzise arbeiten — und ich beide Fenster gleichzeitig beobachten und korrigieren kann. Damit halte ich über zwei Sessions dieselbe Qualität, die ich in einer einzelnen Session erreiche. Während der Markt versucht, ganze Agenten-Teams effizient zu machen — und dabei oft schon im Duo scheitert — ist das für mich die belastbare Vorstufe: erst die Zwei-Fenster-Disziplin messbar machen, dann lässt sich Multi-Agent verlässlich darauf aufsetzen. Flankiert wird das durch ein eigenes Graphen-System, das ich in jedem Projekt einsetze: es lenkt die Wissens-Daten meiner Sessions in die gewünschte Richtung, hält sie verfügbar und macht zugleich jeden Session-Verlauf nachvollziehbar. Das Werkzeug ist heute Claude Code, morgen vielleicht Pi, Codex oder ein anderes — was bleibt, ist die empirische Arbeitsweise.*

*Vor einem Jahr habe ich einem der größten KI-Häuser geschrieben, dass strategisches Claude-Code-Verständnis zur Schlüsselkompetenz wird. Die Rückmeldung damals war sinngemäß, ich sei ein Tool-Jünger. Ein Jahr später sagt dasselbe Haus öffentlich sinngemäß: wer Claude Code versteht, kann bei uns arbeiten.*

*Mein Fazit aus diesem Datenpunkt: ich trage KI-Entwicklung mit Verantwortung — und Innovation mit Priorität. Aus Überzeugung, weil mich die empirische Arbeit mit KI tagtäglich inspiriert und ich mich genau dadurch weiterentwickle. Das ist meiner Meinung nach das Profil eines guten KI-Entwicklers — und der einzige Stack, auf dem wir als Entwickler dem Markt weiterhin die Geschwindigkeit vorgeben können.*
