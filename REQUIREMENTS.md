# Requirements & Standards

## Übersicht

Dieses Dokument definiert die grundlegenden Anforderungen und Standards für die Entwicklung und Dokumentation in diesem Projekt. Diese Richtlinien sollen konsistente Arbeitsweisen und hohe Qualität sicherstellen.

## Dokumentations-Standards

### Sprach- und Naming-Konventionen

**AI-First Sprache-Standards:**
- **Dateinamen:** Ausschließlich Englisch (internationale Kompatibilität)
- **Dokumentationsinhalt:** Ausschließlich Deutsch (optimale KI-Kommunikation)
- **Code-Kommentare:** Englisch (Entwicklungsstandards)
- **Git-Commit-Messages:** Englisch (Conventional Commits Standard)

**AI-First Prinzip:**
Die bewusste Entscheidung für deutschen Dokumentationsinhalt folgt dem AI-First Ansatz:
- **Präzise Kommunikation:** Muttersprache ermöglicht exakte Vermittlung von Anforderungen
- **Iterative Prompt-Optimierung:** Klarer Ist-/Soll-Zustand für Prompt-Testing-Pipeline
- **Qualitätsfokus:** Bessere KI-Ergebnisse wichtiger als internationale Konventionen
- **Verständlichkeit:** Direkte Analyse von Prompt-Input und KI-Output ohne Übersetzungsschritt

**Dateinamen-Format:**
- **Format:** kebab-case (nur Kleinbuchstaben, Bindestriche als Trennzeichen)
- **Sprache:** Ausschließlich Englisch
- **Beispiele:**
  - ✅ `image-compression-summary.md`
  - ✅ `warp-ai-conversation-export.md`
  - ✅ `compression-commands-raw.txt`
  - ❌ `zusammenfassung-erkenntnisse.md`
  - ❌ `bildkomprimierung-commands-raw.txt`
  - ❌ `Image_Compression_Summary.md`

**Begründung:**
- **Internationale Kompatibilität:** Englische Dateinamen funktionieren in allen Systemen
- **Entwicklungsstandards:** Konsistenz mit internationalen Open-Source-Projekten
- **Automatisierung:** Einfachere Scripting-Integration ohne Umlaute
- **Team-Zusammenarbeit:** Universelle Verständlichkeit bei internationalen Teams
- **Klare Trennung:** Deutscher Inhalt für lokales Verständnis, englische Namen für technische Konsistenz

### Dokumentationsstruktur

**Hierarchie:**
```
context/
├── prompting/           # KI-Interaktionshistorie
├── visual-examples/     # Screenshots und Workflow-Dokumentation
└── testing/            # Experimentelle Dokumentation
```

**Inhaltsrichtlinien:**
- Jede Markdown-Datei beginnt mit einem aussagekräftigen H1-Header
- Verwendung von klaren, strukturierten Überschriften
- Code-Beispiele in entsprechenden Fenced Code Blocks
- Konsistente Verwendung von Bullet Points und Nummerierungen

## Entwicklungsstandards

### Git-Workflow

**Commit-Nachrichten:**
- Verwende das Format: `type(scope): description`
- Beispiele: `docs(readme): add navigation links`, `feat(compress): implement pdf optimization`

**Branch-Naming:**
- Verwende kebab-case für Branch-Namen
- Beispiele: `feature/pdf-compression`, `fix/image-positioning`

### Code-Qualität

**Python-Spezifisch:**
- Verwende aussagekräftige Funktions- und Variablennamen
- Dokumentiere komplexe Algorithmen mit Inline-Kommentaren
- Halte Funktionen fokussiert und testbar

## KI-Zusammenarbeit

### Prompt-Engineering

**Dokumentation:**
- Alle KI-Interaktionen in `context/prompting/` dokumentieren
- Verwende kebab-case für Dateinamen
- Strukturiere Conversations chronologisch

**Best Practices:**
- Klare, spezifische Anfragen stellen
- Kontext und Ziele explizit kommunizieren
- Iterative Verbesserung dokumentieren

### Tool-Integration

**Claude Code:**
- Verwende CLAUDE.md für projektspezifische Anweisungen
- Dokumentiere wichtige Workflows und Kommandos
- Nutze strukturierte Prompt-Strategien

## Qualitätssicherung

### Review-Prozess

**Vor Commit:**
- Überprüfe Dateinamen-Konventionen
- Stelle sicher, dass Dokumentation aktuell ist
- Teste funktionale Änderungen

**Dokumentations-Reviews:**
- Prüfe auf Konsistenz mit etablierten Standards
- Validiere Links und Verweise
- Überprüfe Rechtschreibung und Grammatik

### Kontinuierliche Verbesserung

**Feedback-Integration:**
- Dokumentiere Learnings aus Problemen
- Aktualisiere Standards basierend auf Erfahrungen
- Teile bewährte Praktiken im Team

## Technische Anforderungen

### Umgebung

**Python:**
- Version 3.10 oder höher
- Verwende uv für Dependency Management
- Halte requirements aktuell

**System-Dependencies:**
- Ghostscript für PDF-Verarbeitung
- Aktuelle Git-Version für Versionskontrolle

### Performance

**Optimierung:**
- Implementiere effiziente Algorithmen
- Dokumentiere Performance-kritische Bereiche
- Teste mit realistischen Datenmengen

---

**Hinweis:** Diese Standards sind lebende Dokumente und werden bei Bedarf aktualisiert. Alle Änderungen sollten im Team diskutiert und dokumentiert werden.