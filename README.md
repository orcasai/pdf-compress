# Image Optimize - CV PDF Workflow

Ein Python-Tool zur automatischen Optimierung von CV-Bildern und deren Integration in PDF-Lebenslaufdokumente.

## 🔧 Funktionen

- **Automatische Bildverarbeitung**: Wandelt rechteckige Profilbilder in professionelle Kreisbilder um
- **Dual-Theme-Unterstützung**: Erstellt gleichzeitig Green und Orange CV-Varianten
- **Intelligente PDF-Integration**: Fügt Bilder präzise in vorhandene CV-Templates ein
- **Optimierte Komprimierung**: Reduziert PDF-Dateigröße bei hoher Qualität
- **Workflow-basiert**: Sequenzielle Verarbeitung mit nummerierten Ausgabedateien

## 🔧 Architektur

Das Tool folgt einer **3-Stufen-Pipeline**:

```
Input Bild → Kreis zuschneiden → In PDFs einfügen → Komprimieren → Finale CVs
```

### Pipeline-Stufen:

1. **Bildverarbeitung** (`src/crop_circle.py`)
   - Quadratisches Zuschneiden aus rechteckigen Bildern
   - Kreismaske mit Transparenz
   - Optimierte Gesichtspositionierung

2. **PDF-Integration** (`src/insert_image.py`)
   - Präzise Koordinatenplatzierung
   - Gleichzeitige Verarbeitung beider Themes
   - Professionelle Größenanpassung

3. **PDF-Komprimierung** (`src/compress_pdf.py`)
   - 7 verschiedene Komprimierungsstrategien
   - Ghostscript-Integration
   - Qualitäts-/Größenanalyse

## 📋 Schnellstart

### Voraussetzungen

- Python 3.10 oder höher
- [uv](https://github.com/astral-sh/uv) (empfohlen) oder pip
- Ghostscript für PDF-Komprimierung

#### Ghostscript Installation:
```bash
# macOS
brew install ghostscript

# Ubuntu/Debian
sudo apt-get install ghostscript

# Windows
# Download von https://www.ghostscript.com/download/gsdnld.html
```

### Installation

```bash
# Repository klonen
git clone <repository-url>
cd image-optimize

# Abhängigkeiten installieren
uv sync
# oder mit pip:
# pip install -r requirements.txt
```

### Eingabedateien vorbereiten

Legen Sie Ihre Dateien in die entsprechenden Verzeichnisse:

```
data/
 images/
    cv-image.jpg          # Ihr Profilbild
 pdfs/
     CV-PR-Green.pdf       # Green CV-Template
     CV-PR-Orange.pdf      # Orange CV-Template
```

## 📋 Verwendung

### Kompletter Workflow

```bash
# Vollständiger CV-Optimierungsworkflow
python main.py

# Mit uv
uv run python main.py
```

### Ausgabe-Struktur

Nach dem Ausführen erhalten Sie:

```
output/
 01-crop-circle-output.png           # Kreisförmiges Profilbild
 02-CV-PR-Green-with-image.pdf       # Green CV mit Bild
 02-CV-PR-Orange-with-image.pdf      # Orange CV mit Bild
 03-CV-PR-Green-final.pdf            # Komprimiertes Green CV
 03-CV-PR-Orange-final.pdf           # Komprimiertes Orange CV
```

### Einzelne Module testen

```bash
# Nur Bildverarbeitung
python src/crop_circle.py

# Nur PDF-Integration
python src/insert_image.py

# Nur Komprimierung
python src/compress_pdf.py

# Komprimierungsvergleich
python test_compression.py
```

## ⚙️ Konfiguration

### Optimierte Parameter

Das Tool verwendet vorkonfigurierte Parameter für professionelle CV-Qualität:

```python
# Bildverarbeitung
vertical_shift_pct=0.05      # Gesichtspositionierung
horizontal_shift_px=16       # Horizontale Ausrichtung
padding_pct=0.06            # Kreisgröße

# PDF-Integration
position=(35, 22)           # Präzise Koordinaten
size=(110, 110)            # Professionelle Bildgröße

# Komprimierung
quality="custom-balanced"   # Optimiert für CVs
```

### Komprimierungsqualität

- `screen`: Web-optimiert, kleinste Dateien
- `ebook`: Ausgewogen für digitales Lesen
- `printer`: Standard-Druckqualität
- `prepress`: Hochwertige Druckqualität
- `custom-balanced`: **Standard** - CV-optimierte Qualität/Größe
- `custom-high`: Maximale Qualitätserhaltung
- `custom-small`: Aggressive Komprimierung

## 🧪 Testing

### Vollständige Workflow-Tests

```bash
# Kompletter Test mit realen Dateien
python main.py

# Überprüfung der Ausgaben
ls -la output/
```

### Einzelmodule testen

```bash
# Bildverarbeitung testen
python src/crop_circle.py
# Erwartete Ausgabe: Kreisförmiges PNG mit Transparenz

# PDF-Integration testen
python src/insert_image.py
# Erwartete Ausgabe: PDF mit eingefügtem Bild

# Komprimierung testen
python src/compress_pdf.py
# Erwartete Ausgabe: Komprimiertes PDF

# Alle Komprimierungsoptionen vergleichen
python test_compression.py
# Erwartete Ausgabe: Größenvergleich aller Varianten
```

### Qualitätskontrolle

1. **Visuell**: öffnen Sie die generierten PDFs und prüfen Sie:
   - Bildqualität und Schärfe
   - Korrekte Positionierung
   - Transparenz-Handling

2. **Dateigröße**: überprüfen Sie die Komprimierungsraten:
   - Typisch: 30-60% Größenreduktion
   - Qualität sollte für Druck geeignet sein

3. **Kompatibilität**: Testen Sie die PDFs in verschiedenen Viewern

## 📋 Projektstruktur

```
image-optimize/
 src/                     # Haupt-Quellcode
    main_workflow.py     # Workflow-Orchestrierung
    crop_circle.py       # Bildverarbeitung
    insert_image.py      # PDF-Integration
    compress_pdf.py      # PDF-Komprimierung
 data/                    # Eingabedateien
    images/              # Profilbilder
    pdfs/                # CV-Templates
 output/                  # Ausgabedateien
 tests/                   # Test-Verzeichnis
 main.py                  # Haupteinstiegspunkt
 test_compression.py      # Komprimierungstest
 pyproject.toml          # Projektkonfiguration
 uv.lock                 # Abhängigkeitslock
 README.md               # Diese Datei
```

## 🛠️ Entwicklung

### Neue Features hinzufügen

1. **Bildverarbeitung**: Erweitern Sie `src/crop_circle.py`
2. **PDF-Integration**: Modifizieren Sie `src/insert_image.py`
3. **Komprimierung**: Fügen Sie Strategien in `src/compress_pdf.py` hinzu
4. **Workflow**: Aktualisieren Sie `src/main_workflow.py`

### Abhängigkeiten verwalten

```bash
# Neue Abhängigkeit hinzufügen
uv add package-name

# Abhängigkeit entfernen
uv remove package-name

# Abhängigkeiten aktualisieren
uv sync --upgrade
```

## ⚠️ Fehlerbehebung

### Häufige Probleme

**"Ghostscript nicht gefunden"**
```bash
# überprüfen Sie die Installation
gs --version

# Installieren Sie Ghostscript
brew install ghostscript  # macOS
```

**"Eingabedateien nicht gefunden"**
- Stellen Sie sicher, dass `data/images/cv-image.jpg` existiert
- überprüfen Sie, dass beide PDF-Templates vorhanden sind

**"Komprimierung fehlgeschlagen"**
- überprüfen Sie die Ghostscript-Installation
- Stellen Sie sicher, dass die PDF-Datei nicht beschädigt ist

### Debug-Modus

```bash
# Verbose-Ausgabe für Debugging
python main.py --verbose

# Einzelne Module für isolierte Tests
python src/crop_circle.py --debug
```

## 📋 Abhängigkeiten

### Python-Pakete

- `pillow>=11.3.0`: Bildverarbeitung und -manipulation
- `pymupdf>=1.26.3`: PDF-Lesen, -Bearbeitung und -Erstellung

### System-Abhängigkeiten

- **Ghostscript**: Erforderlich für PDF-Komprimierung
- **uv**: Moderner Python-Paketmanager (empfohlen)

## 📋 Wichtige Hinweise

### Qualitätsoptimierung

- Parameter sind für professionelle CV-Bildqualität voreingestellt
- Mehrere Komprimierungsstrategien gewährleisten optimale Dateigröße vs. Qualität
- Hauttöne werden im Bildverarbeitungsprozess bewahrt

### Dateiverwaltung

- Sequenzielles Nummerierungssystem (01-, 02-, 03-) für klare Workflow-Nachverfolgung
- Automatische Ausgabeverzeichnis-Erstellung
- Nicht-destruktive Verarbeitung (Originaldateien bleiben erhalten)

### Performance

- Einzelnes Kreisbild wird für beide PDF-Varianten wiederverwendet
- Effiziente Speichernutzung durch PIL-Optimierungen
- Ghostscript-Subprocess-Management für Komprimierung

## 🤖 KI-Unterstützte Entwicklung

Dieses Projekt demonstriert die effiziente Zusammenarbeit mit künstlicher Intelligenz zur schnellen Entwicklung professioneller Tools. Durch gezieltes Prompting und maximale Kontextübertragung können komplexe Aufgaben in kürzester Zeit umgesetzt werden.

### Dokumentierte Entwicklungshistorie

Das `context/` Verzeichnis enthält die vollständige Entwicklungshistorie und zeigt Best Practices für KI-gestützte Softwareentwicklung:

#### Prompting-Strategien (`context/prompting/`)
- **`chatgpt-avm-history.md`**: Dokumentation der ChatGPT-Interaktionen und Prompt-Optimierungen
- **`claude-desktop-history.md`**: Claude Desktop Workflow-Dokumentation und Kontextmanagement

#### Visuelle Entwicklungsbeispiele (`context/visual-examples/`)

**Workflow-Optimierungen** (`preferences/`):
- **`das-wichtigste-tool-von-allen.png`**: Demonstration der wichtigsten Entwicklungstools und deren Integration
- **`ein-kleiner-einblick-in-commit-workflow.png`**: Einblick in den effizienten Git-Commit-Workflow mit KI-Unterstützung
- **`kleiner-hinweis-wie-hier-informationen-hin-und-her-geschoben-werden.jpeg`**: Visualisierung der Informationsübertragung zwischen Entwickler und KI

**Problemlösungsansätze** (`issues/`):
- **`claude-code-in-die-knie-gezwungen-wegen-multi-edit-fehler.png`**: Dokumentation technischer Herausforderungen und deren Lösung

### Entwicklungseffizienz durch KI

Dieses Repository veranschaulicht, wie durch strukturierte KI-Zusammenarbeit:
- **Komplexe Bildverarbeitungslogik** in wenigen Iterationen entwickelt wird
- **Robuste PDF-Manipulation** ohne umfangreiche Dokumentationsstudien implementiert wird  
- **Professionelle Code-Qualität** durch iterative Verbesserung erreicht wird
- **Umfangreiche Dokumentation** parallel zur Entwicklung entsteht

Die visuellen Beispiele zeigen konkrete Arbeitsabläufe und demonstrieren, wie maximaler Kontext durch präzise Kommunikation übertragen wird, um optimale Ergebnisse zu erzielen.