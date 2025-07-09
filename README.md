# Image Optimize - CV PDF Workflow

## 🎯 Portfolio-Projekt: KI-Unterstützte Problemlösung

Dieses Repository demonstriert die effiziente Zusammenarbeit mit künstlicher Intelligenz zur Lösung eines realen Problems aus der Praxis. Das Projekt zeigt, wie durch strukturierte KI-Kollaboration komplexe technische Herausforderungen schnell und professionell bewältigt werden können.

### Das Problem: KickResume PDF-Optimierung

**Ausgangssituation:**
- KickResume erstellt professionelle CVs, aber die PDF-Dateien sind **20+ MB groß**
- Herkömmliche Komprimierung (Ghostscript, etc.) führt zu **starker Bildqualitätsverlust**
- Die Webseite bietet nur die Option: entweder volles PDF mit Bild oder komprimiertes PDF ohne Bild

**Herausforderung:**
- Präzise Bildpositionierung in PDFs ohne Qualitätsverlust
- Komprimierung auf **~2MB** bei professioneller Bildqualität
- Automatisierte Verarbeitung für beide CV-Themes (Green/Orange)

### Die Lösung: KI-Gestützte Entwicklung

**Lösungsansatz entwickelt mit ChatGPT und Claude:**
1. **Problemanalyse**: PDF-Struktur analysiert, Bildpositionierung verstanden
2. **Iterative Entwicklung**: Python-Script für präzise Bildplatzierung
3. **Optimierung**: Exakte Koordinaten durch Test-Zyklen verfeinert
4. **Integration**: Vollständiger Workflow mit Pipeline-Verarbeitung

**Technische Lösung:**
- **Bildextraktion**: Kreisförmige Ausschnitte mit optimierter Gesichtspositionierung
- **PDF-Manipulation**: Präzise Koordinaten-basierte Bildplatzierung
- **Komprimierung**: Mehrstufige Optimierung ohne Qualitätsverlust

## 🤖 Dokumentierte KI-Zusammenarbeit

### Entwicklungshistorie ([`context/`](./context/))

#### Prompting-Strategien ([`context/prompting/`](./context/prompting/))

**ChatGPT-Entwicklungshistorie:**
- 📄 **[`chatgpt-avm-history.md`](./context/prompting/chatgpt-avm-history.md)**: Vollständige ChatGPT-Interaktionen zur Problemlösung
  - Initiale Problemanalyse der KickResume PDF-Struktur
  - Iterative Python-Script-Entwicklung für Bildpositionierung
  - Debugging-Strategien für präzise Koordinaten-Konfiguration
  - Prompt-Optimierungen für bessere Code-Qualität

**Claude Desktop-Entwicklungshistorie:**
- 📄 **[`claude-desktop-history.md`](./context/prompting/claude-desktop-history.md)**: Claude Desktop Workflow-Dokumentation
  - Strukturierte Codebase-Analyse und Architektur-Planung
  - Refactoring-Strategien für modulare Entwicklung
  - Dokumentations-Erstellung parallel zur Implementierung
  - Kontextmanagement für komplexe Entwicklungsaufgaben

#### Visuelle Entwicklungsbeispiele ([`context/visual-examples/`](./context/visual-examples/))

**Workflow-Optimierungen** ([`preferences/`](./context/visual-examples/preferences/)):

- 🖼️ **[`das-wichtigste-tool-von-allen.png`](./context/visual-examples/preferences/das-wichtigste-tool-von-allen.png)**: 
  - **Zweck**: Demonstration der wichtigsten Entwicklungstools und deren Integration
  - **Inhalt**: Screenshot der Tool-Konfiguration für optimale KI-Zusammenarbeit
  - **Relevanz**: Zeigt, wie durch richtige Tool-Auswahl die Entwicklungseffizienz maximiert wird

- 🖼️ **[`ein-kleiner-einblick-in-commit-workflow.png`](./context/visual-examples/preferences/ein-kleiner-einblick-in-commit-workflow.png)**: 
  - **Zweck**: Einblick in den effizienten Git-Commit-Workflow mit KI-Unterstützung
  - **Inhalt**: Visualisierung des strukturierten Commit-Prozesses
  - **Relevanz**: Demonstriert professionelle Versionskontrolle durch KI-assistierte Entwicklung

- 🖼️ **[`kleiner-hinweis-wie-hier-informationen-hin-und-her-geschoben-werden.jpeg`](./context/visual-examples/preferences/kleiner-hinweis-wie-hier-informationen-hin-und-her-geschoben-werden.jpeg)**: 
  - **Zweck**: Visualisierung der Informationsübertragung zwischen Entwickler und KI
  - **Inhalt**: Konkrete Beispiele für maximale Kontextübertragung
  - **Relevanz**: Zeigt Best Practices für effiziente KI-Kommunikation

**Problemlösungsansätze** ([`issues/`](./context/visual-examples/issues/)):

- 🖼️ **[`claude-code-in-die-knie-gezwungen-wegen-multi-edit-fehler.png`](./context/visual-examples/issues/claude-code-in-die-knie-gezwungen-wegen-multi-edit-fehler.png)**: 
  - **Zweck**: Dokumentation technischer Herausforderungen und deren Lösung
  - **Inhalt**: Konkreter Problemfall mit MultiEdit-Tool und Lösungsansatz
  - **Relevanz**: Zeigt Debugging-Methodik und iterative Problemlösung mit KI-Unterstützung

### Entwicklungseffizienz durch KI

**Erreichte Ergebnisse:**
- **Komplexe Bildverarbeitung** in wenigen Iterationen implementiert
- **Robuste PDF-Manipulation** ohne umfangreiche Dokumentationsstudien
- **Präzise Koordinaten-Konfiguration** durch iterative Verbesserung
- **Professionelle Code-Qualität** parallel zur Entwicklung

## 🔧 Technische Lösung

### 3-Stufen-Pipeline

```
Input Bild → Kreis zuschneiden → In PDFs einfügen → Komprimieren → Finale CVs
```

### Präzise Konfiguration

**Bildverarbeitung** (`src/crop_circle.py`):
```python
vertical_shift_pct=0.05      # Gesichtspositionierung optimiert
horizontal_shift_px=16       # Horizontale Feinjustierung
padding_pct=0.06            # Kreisgröße relativ zur Bildgröße
```

**PDF-Integration** (`src/insert_image.py`):
```python
position=(35, 22)           # Exakte Koordinaten für KickResume-Templates
size=(110, 110)            # Optimale Bildgröße für professionelle Darstellung
```

**Komprimierung** (`src/compress_pdf.py`):
```python
quality="custom-balanced"   # Speziell für CV-Qualität entwickelt
```

### Iterative Positionierung

**Testverfahren:**
1. PDF ohne Bild von KickResume exportieren (als Platzhalter)
2. Script ausführen und Bildposition visuell prüfen
3. Koordinaten anpassen und erneut testen
4. Finale Konfiguration für beide Themes (Green/Orange)

## 📋 Schnellstart

### Voraussetzungen

- Python 3.10 oder höher
- [uv](https://github.com/astral-sh/uv) (empfohlen) oder pip
- Ghostscript für PDF-Komprimierung

```bash
# macOS
brew install ghostscript

# Ubuntu/Debian
sudo apt-get install ghostscript
```

### Installation

```bash
git clone <repository-url>
cd image-optimize
uv sync
```

### Verwendung

```bash
# Vollständiger Workflow
python main.py

# Ergebnis: Komprimierte CVs (~2MB) mit optimaler Bildqualität
```

**Eingabe:**
```
data/
├── images/cv-image.jpg          # Ihr Profilbild
└── pdfs/
    ├── CV-PR-Green.pdf          # Green Theme (ohne Bild)
    └── CV-PR-Orange.pdf         # Orange Theme (ohne Bild)
```

**Ausgabe:**
```
output/
├── 01-crop-circle-output.png           # Kreisförmiges Profilbild
├── 02-CV-PR-Green-with-image.pdf       # Green CV mit Bild
├── 02-CV-PR-Orange-with-image.pdf      # Orange CV mit Bild
├── 03-CV-PR-Green-final.pdf            # Komprimiertes Green CV (~2MB)
└── 03-CV-PR-Orange-final.pdf           # Komprimiertes Orange CV (~2MB)
```

## 🎯 Problemlösung im Detail

### KickResume-Workflow

1. **PDF-Templates erstellen**: CVs auf KickResume ohne Profilbild exportieren
2. **Bildvorbereitung**: Profilbild als `cv-image.jpg` bereitstellen
3. **Automatisierte Verarbeitung**: Script führt komplette Pipeline aus
4. **Qualitätskontrolle**: Finale PDFs visuell prüfen

### Qualitätsverbesserung

**Vorher:** 20+ MB PDF von KickResume
**Nachher:** ~2MB PDF mit professioneller Bildqualität

**Technische Verbesserungen:**
- Präzise Bildpositionierung ohne manuelle Anpassung
- Optimierte Komprimierung ohne Qualitätsverlust
- Automatisierte Verarbeitung für beide Themes
- Reproduzierbare Ergebnisse durch konfigurierbare Parameter

## 🛠️ Projektstruktur

```
image-optimize/
├── src/                     # Haupt-Quellcode
│   ├── main_workflow.py     # Workflow-Orchestrierung
│   ├── crop_circle.py       # Kreisförmige Bildextraktion
│   ├── insert_image.py      # PDF-Bildintegration
│   └── compress_pdf.py      # Mehrstufige Komprimierung
├── context/                 # KI-Entwicklungshistorie
│   ├── prompting/           # Prompt-Strategien und Iterationen
│   └── visual-examples/     # Workflow-Screenshots und Problemlösungen
├── data/                    # Eingabedateien (Templates & Bilder)
├── output/                  # Optimierte CV-PDFs
└── main.py                  # Haupteinstiegspunkt
```

## 🧪 Testing & Qualitätskontrolle

### Iterative Verbesserung

```bash
# Einzelmodule testen
python src/crop_circle.py      # Bildverarbeitung
python src/insert_image.py     # PDF-Integration
python src/compress_pdf.py     # Komprimierung

# Komprimierungsvergleich
python test_compression.py     # Alle Qualitätsstufen testen
```

### Qualitätsprüfung

1. **Bildqualität**: Schärfe und Farbgenauigkeit in finalen PDFs
2. **Positionierung**: Exakte Platzierung ohne manuelle Nachbearbeitung
3. **Dateigröße**: Konsistente Komprimierung auf ~2MB
4. **Kompatibilität**: Funktioniert mit verschiedenen PDF-Viewern

## 📊 Abhängigkeiten

**Python-Pakete:**
- `pillow>=11.3.0`: Professionelle Bildverarbeitung
- `pymupdf>=1.26.3`: PDF-Manipulation und -Integration

**System-Abhängigkeiten:**
- **Ghostscript**: Hochwertige PDF-Komprimierung
- **uv**: Moderner Python-Paketmanager (empfohlen)

---

**Ergebnis:** Professionelle CV-Optimierung durch strukturierte KI-Zusammenarbeit - von der Problemanalyse bis zur produktionsreifen Lösung.