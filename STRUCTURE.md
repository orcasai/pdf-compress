# Project Structure & Conventions

## AI-First Naming Standards

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

### Dateinamen-Format

**Format:** kebab-case (nur Kleinbuchstaben, Bindestriche als Trennzeichen)
**Sprache:** Ausschließlich Englisch

**Beispiele:**
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

## Repository-Struktur

### Context Directory Organisation

```
context/
├── prompting/           # KI-Interaktionshistorie
│   ├── chatgpt-avm-history.md     # ChatGPT Entwicklungshistorie
│   └── claude-desktop-history.md  # Claude Desktop Workflows
├── visual-examples/     # Screenshots und Workflow-Dokumentation
│   ├── preferences/     # Tool-Konfigurationen und Workflows
│   └── issues/         # Problemlösungsansätze
└── testing/            # Experimentelle Dokumentation
    ├── image-compression-summary.md
    └── compression-commands-raw.txt
```

### Core Project Structure

```
pdf-compress/
├── src/                     # Haupt-Quellcode
│   ├── main_workflow.py     # Workflow-Orchestrierung
│   ├── crop_circle.py       # Kreisförmige Bildextraktion
│   ├── insert_image.py      # PDF-Bildintegration
│   └── compress_pdf.py      # Mehrstufige Komprimierung
├── context/                 # KI-Entwicklungshistorie
├── data/                    # Eingabedateien (Templates & Bilder)
├── output/                  # Optimierte CV-PDFs
├── tests/                   # Test-Dateien
└── main.py                  # Haupteinstiegspunkt
```

## Dokumentations-Hierarchie

### Inhaltsrichtlinien
- Jede Markdown-Datei beginnt mit einem aussagekräftigen H1-Header
- Verwendung von klaren, strukturierten Überschriften (H1-H6 Hierarchie)
- Code-Beispiele in entsprechenden Fenced Code Blocks
- Konsistente Verwendung von Bullet Points (`-`) und Nummerierungen
- Markdown-Links statt Rohtext-URLs für bessere Lesbarkeit
- Strukturierte Listen mit klarer Hierarchie und Einrückung

### LLM-Optimierte Struktur
- **LLMS.txt Standard:** Repository-Root mit strukturierter Übersicht
- **Semantische Organisation:** Logische Gruppierung verwandter Inhalte
- **Klare Verlinkung:** Direkte Links zu wichtigsten Dokumenten und Code-Modulen
- **Kontext-Bereitstellung:** Ausreichende Informationen für autonomes Verständnis