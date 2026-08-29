# CV Translation — Robin Walter Scherler

**Source:** `cv.docx` (CV-Export-Tool export, 2026-05-18)
**Pipeline:** docx → pandoc → markdown → split by H1 → 6× parallel `german-translator` agents (DE→EN)

## Struktur

```
export/cv-translation/
├── INDEX.md                       # diese Datei
├── _source/
│   ├── cv-de-full.md              # pandoc Output, ungesplittet (Master DE)
│   ├── cv-en-full.md              # Concat aller EN-Sektionen (Master EN)
│   ├── cv-en-full.docx            # DOCX-Export inkl. Profilbild (Template = cv-template-clean.docx)
│   └── cv-en-full.pdf             # PDF-Export (Chrome-Headless aus pandoc-HTML), 11 Seiten
├── de/                            # Deutsche Sektion-Fragmente (Quelle für Übersetzung)
│   ├── 01-adresse.md
│   ├── 02-ueber-mich.md
│   ├── 03-berufserfahrungen.md
│   ├── 04-letzte-projekte-chronologisch.md
│   ├── 05-faehigkeiten.md
│   └── 06-ausbildung.md
└── en/                            # Englische Übersetzungen (paarweise zu de/)
    ├── 01-adresse.md              # Address
    ├── 02-ueber-mich.md           # About Me
    ├── 03-berufserfahrungen.md    # Professional Experience
    ├── 04-letzte-projekte-chronologisch.md  # Recent Projects (Chronological)
    ├── 05-faehigkeiten.md         # Skills
    └── 06-ausbildung.md           # Education
```

## Sektionen-Map

| # | DE-Datei | EN-Datei | DE-Zeilen | EN-Zeilen |
|---|----------|----------|----------:|----------:|
| 01 | `de/01-adresse.md` | `en/01-adresse.md` | 5 | 5 |
| 02 | `de/02-ueber-mich.md` | `en/02-ueber-mich.md` | 98 | 97 |
| 03 | `de/03-berufserfahrungen.md` | `en/03-berufserfahrungen.md` | 118 | 117 |
| 04 | `de/04-letzte-projekte-chronologisch.md` | `en/04-letzte-projekte-chronologisch.md` | 60 | 59 |
| 05 | `de/05-faehigkeiten.md` | `en/05-faehigkeiten.md` | 176 | 176 |
| 06 | `de/06-ausbildung.md` | `en/06-ausbildung.md` | 143 | 143 |
| **Σ** | | | **600** | **597** (Master nach Re-Concat: **603** inkl. 6 Blank-Separatoren) |

## Übersetzungsregeln (an Agenten gegeben)

- Markdown-Struktur 1:1 erhalten (Headings, Blank-Lines, Listen, Links)
- URLs unverändert
- Skill-Bars `■■■■□` zeichenweise erhalten (72× DE = 72× EN ✓)
- Datumsformat `MM/YYYY -- MM/YYYY` unverändert
- Eigennamen (Firmen, Produkte, Tech-Stack) verbatim
- Länder übersetzt: Deutschland→Germany, Spanien→Spain
- Bullet-Stil: deutsch-nominal → englisch verb-led, past-tense
- Bildungsabschlüsse: original + Erklärung in Klammern

## Workflow für Updates

1. CV-Export-Tool → neuer `cv.docx` Export → Projekt-Root
2. `pandoc cv.docx -t markdown -o export/cv-translation/_source/cv-de-full.md --wrap=none`
3. AWK-Split nach `^# ` neu ausführen (siehe Conversation History)
4. Für geänderte Sektionen: `german-translator` Agent für betroffene `de/NN-*.md` neu spawnen
5. Concat `cv-en-full.md` aus `en/*.md` neu erzeugen **mit Blank-Line-Separator** zwischen Sektionen (sonst werden Folge-H1s als Plain-Text geparst)
6. DOCX-Export neu generieren (siehe nächste Sektion)

## DOCX-Export

**Output:** `_source/cv-en-full.docx` (~215 KB inkl. eingebettetem Profilbild, Mai 2026)

### Bereinigtes Template

Der ursprüngliche `cv.docx`-Export enthielt im Header2 Werbung des CV-Export-Tools (Promo-Text + Logo-Banner-PNG). Statt direkt `cv.docx` als Reference-Doc zu nutzen, wird einmalig ein bereinigtes Template `cv-template-clean.docx` gebaut:

```bash
WORK=/tmp/cv-template-clean-build && rm -rf "$WORK" && mkdir -p "$WORK" && cd "$WORK"
unzip -q /Users/robin/Code/pdf-compress/cv.docx -d ./

# 1. Promo-Header2 durch leeres Scaffold ersetzen (clone von leerem header1)
cp word/header1.xml word/header2.xml

# 2. Werbe-Logo-PNG entfernen + Bindung lösen
rm -f word/media/image1.png && rmdir word/media 2>/dev/null
rm -f word/_rels/header2.xml.rels

# 3. Repack als clean template
zip -q -X /Users/robin/Code/pdf-compress/cv-template-clean.docx '[Content_Types].xml'
zip -q -rX /Users/robin/Code/pdf-compress/cv-template-clean.docx . -x '[Content_Types].xml'
```

Resultat: `cv-template-clean.docx` (~32 KB) im Projekt-Root — selbe Styles/Fonts/Themes wie Original, **ohne** Promo-Header und ohne Logo-Image.

### DOCX-Generierung

```bash
# Profilbild-Header für pandoc-Embed vorbereiten
PHOTO=/Users/robin/Code/pdf-compress/output/01-crop-circle-output.png
cat > /tmp/cv-photo-header.md <<EOF
![]($PHOTO){width=1.6in}

EOF
cat /tmp/cv-photo-header.md export/cv-translation/_source/cv-en-full.md > /tmp/cv-en-with-photo.md

# Pandoc-Run mit clean template + autolink-Extension
pandoc /tmp/cv-en-with-photo.md \
  --reference-doc=/Users/robin/Code/pdf-compress/cv-template-clean.docx \
  --from=markdown+autolink_bare_uris \
  --to=docx \
  --output=export/cv-translation/_source/cv-en-full.docx
```

**Was erhalten bleibt:**
- 6× `# Heading` → Word-Style "Heading 1" (Schriftgröße/Farbe aus Template)
- 22× `## Heading` → "Heading 2"
- 4× `### Heading` → "Heading 3"
- Skill-Bars `■■■■□` (273 Unicode-Glyphen, identisch zu Source)
- 10× bare URLs → klickbare Hyperlinks (`+autolink_bare_uris` Extension)
- Bullet-Listen mit numbering.xml aus Template
- Body-Font + Theme aus Template
- Profilbild `01-crop-circle-output.png` als embedded `<w:drawing>` am Dokumentanfang
- Page-Number-Footer (footer3 mit `PAGE`-Field bleibt erhalten)

**Was NICHT reproduziert wird (Trade-off):**
- Multi-Column-Layout (Sidebar/Hauptspalte) der Original-Vorlage

## PDF-Export

**Output:** `_source/cv-en-full.pdf` (~468 KB, 11 Seiten, Mai 2026)

Da keine lokale docx→pdf-Toolchain installiert ist (kein LibreOffice/wkhtmltopdf/LaTeX), Renderer-Pfad: **pandoc → standalone HTML mit eingebetteten Resources → Chrome-Headless `--print-to-pdf`**.

```bash
# 1. Photo-Header für pandoc-Embed
PHOTO=/Users/robin/Code/pdf-compress/output/01-crop-circle-output.png
cat > /tmp/cv-photo-header.md <<EOF
![]($PHOTO){width=160px}

EOF
cat /tmp/cv-photo-header.md export/cv-translation/_source/cv-en-full.md > /tmp/cv-en-with-photo.md

# 2. CV-CSS schreiben (Heading-Farben, Spacing, Page-Setup)
cat > /tmp/cv-css.css <<'CSS'
@page { size: A4; margin: 18mm 16mm; }
body { font-family: -apple-system, "Helvetica Neue", Arial, sans-serif; font-size: 10pt; line-height: 1.4; color: #222; max-width: 178mm; margin: 0 auto; }
h1 { font-size: 18pt; color: #1a5490; border-bottom: 2px solid #1a5490; padding-bottom: 4px; margin-top: 16pt; margin-bottom: 8pt; page-break-before: avoid; }
h1:first-of-type { margin-top: 0; }
h2 { font-size: 13pt; color: #2c6bb0; margin-top: 12pt; margin-bottom: 4pt; page-break-after: avoid; }
h3 { font-size: 11pt; color: #444; font-style: italic; margin-top: 6pt; margin-bottom: 2pt; }
p { margin: 4pt 0; }
ul { margin: 4pt 0; padding-left: 18pt; }
li { margin: 2pt 0; }
a { color: #1a5490; text-decoration: none; }
img { display: block; margin: 0 auto 10pt; }
CSS

# 3. Pandoc → standalone HTML mit Photo als data: URI eingebettet
pandoc /tmp/cv-en-with-photo.md \
  --from=markdown+autolink_bare_uris \
  --to=html5 \
  --standalone \
  --embed-resources \
  --css=/tmp/cv-css.css \
  --metadata title="Robin Walter Scherler — Curriculum Vitae" \
  --output=/tmp/cv-en-full.html

# 4. Chrome-Headless → PDF
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=export/cv-translation/_source/cv-en-full.pdf \
  "file:///tmp/cv-en-full.html"
```

**Was geliefert wird:**
- 11 Seiten A4 mit 18×16mm Margins
- Profilbild eingebettet auf Seite 1 (400×400 FlateDecode-PNG)
- Heading-Farben aus CSS (`#1a5490` H1 mit Border-Bottom, `#2c6bb0` H2)
- Klickbare Hyperlinks (CSS `text-decoration: none`, Farbe matched H1)
- Page-Break-Logik: H1+H2 mit `page-break-after: avoid` für saubere Section-Übergänge

**Fallback (falls Chrome nicht da):**
```bash
uv run python -c "
import fitz
doc = fitz.open('export/cv-translation/_source/cv-en-full.docx')
with open('export/cv-translation/_source/cv-en-full.pdf', 'wb') as f:
    f.write(doc.convert_to_pdf())
"
```
→ PyMuPDF-Renderer, 22 Seiten (single-column), **ohne** Profilbild (fitz-Limitation bei docx-Images).

**Verifikations-Kommandos (read-only):**
```bash
# Heading-Struktur prüfen
unzip -p _source/cv-en-full.docx word/document.xml | grep -oE 'w:val="Heading[0-9]"' | sort | uniq -c
# Hyperlink-Count
unzip -p _source/cv-en-full.docx word/document.xml | grep -oc "<w:hyperlink"
# Skill-Bar-Count
unzip -p _source/cv-en-full.docx word/document.xml | grep -oc "■"
```

**Erwartete Werte:** `Heading1=6  Heading2=22  Heading3=4 | Hyperlinks=10 | Skill-Bars=273`

## Fallstricke

**Concat-Bug (gefixt):** Pandoc-ATX-Headings (`# `) brauchen Blank-Line davor. `cat`-Concat ohne Separator → Folge-H1s werden als Text-Fortsetzung geparst. Build-Loop in INDEX.md Update-Workflow Step 5 fügt `echo ""` zwischen jeder Datei ein.

**Hyperlink-Default:** Pandoc `markdown` ohne Extension erkennt **keine** bare URLs als Links. `+autolink_bare_uris` ist Pflicht für klickbare Links im docx-Output.

## Diff zu Original `data/original/cv.md`

`data/original/cv.md` ist alter Snapshot (Jul 2025, 817 Zeilen Markdown — mit zusätzlichen Listen-Markern aus früherem Export). Neue Master-Quelle ist `_source/cv-de-full.md` (Mai 2026, 600 Zeilen, gleicher Inhalt aber schlanker formatiert).
