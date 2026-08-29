#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Endfassungen landen hier; Zwischendateien entstehen und vergehen daneben.
OUT="out"
mkdir -p "$OUT"

[[ -d samples ]] || { echo "missing samples/ dir"; exit 1; }
shopt -s nullglob
# Build from a passed list of stems, or every samples/*.md by default.
# Usage: ./build.sh            → all samples
#        ./build.sh cv-de      → only samples/cv-de.md
if [[ $# -gt 0 ]]; then
  SAMPLES=(); for arg in "$@"; do SAMPLES+=("samples/${arg}.md"); done
else
  SAMPLES=(samples/*.md)
fi
[[ ${#SAMPLES[@]} -gt 0 ]] || { echo "no samples/*.md found"; exit 1; }

build_variant() {
  local BASE="$1"; local NAME="$2"; local CSS="$3"; local HTMLLANG="$4"
  local STEM="${OUT}/${BASE}-${NAME}"
  local HTML="${STEM}.html"
  local PDF_RAW="${STEM}-raw.pdf"
  local PDF_OUT="${STEM}.pdf"

  cat > "$HTML" <<HTMLEOF
<!doctype html>
<html lang="${HTMLLANG}">
<head>
<meta charset="utf-8">
<title>${TITLE}</title>
<style>
${CSS}
</style>
</head>
<body>
${BODY}
</body>
</html>
HTMLEOF

  "$CHROME" --headless --disable-gpu --no-pdf-header-footer \
    --print-to-pdf-no-header \
    --print-to-pdf="$(pwd)/$PDF_RAW" \
    "file://$(pwd)/$HTML" 2>/dev/null

  gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/printer \
     -dNOPAUSE -dQUIET -dBATCH \
     -dDownsampleColorImages=false -dDownsampleGrayImages=false \
     -sOutputFile="$PDF_OUT" "$PDF_RAW"

  rm -f "$PDF_RAW"
  echo "Built: $PDF_OUT ($(stat -f%z "$PDF_OUT") bytes)"
}

read -r -d '' CSS_COMPACT <<'CSSEOF' || true
@page { size: A4; margin: 0.45cm 0.9cm 0.45cm 0.9cm; }
html { font-family: -apple-system, "Helvetica Neue", Arial, sans-serif; font-size: 7.2pt; line-height: 1.16; color: #1a1a1a; }
body { margin: 0; }
.cv-photo-gutter { float: right; width: 3.0cm; height: 3.7cm; }
h1 { font-size: 10.2pt; margin: 0 0 0.08em 0; font-weight: 700; letter-spacing: -0.01em; }
h3 { font-size: 8.1pt; margin: 0.32em 0 0.12em 0; font-weight: 700; padding-top: 0.20em; border-top: 1px solid #e8e8e5; }
h3:first-of-type { border-top: none; padding-top: 0; }
p { margin: 0 0 0.22em 0; }
ul { margin: 0.06em 0 0.22em 0; padding-left: 0.85em; }
li { margin-bottom: 0.04em; }
blockquote { margin: 0.14em 0; padding: 0.18em 0.5em; border-left: 2px solid #888; background: #f6f6f4; font-size: 6.7pt; line-height: 1.18; border-radius: 1px; }
blockquote p { margin: 0 0 0.14em 0; }
blockquote p:last-child { margin-bottom: 0; }
hr { border: none; height: 1px; background: linear-gradient(to right, transparent, #b9b9b6 30%, #b9b9b6 70%, transparent); margin: 0.3em auto; width: 60%; }
table { border-collapse: collapse; width: 100%; margin: 0.10em 0 0.20em 0; font-size: 6.7pt; }
tr { break-inside: avoid; page-break-inside: avoid; }
th, td { border-bottom: 1px solid #d8d8d8; padding: 1.2pt 3.5pt; text-align: left; vertical-align: top; }
th { font-weight: 600; background: #f3f3f1; }
code { font-family: "SF Mono", Menlo, Monaco, "Courier New", monospace; font-size: 6.5pt; background: #f1f1ef; padding: 0.4pt 2pt; border-radius: 2px; }
em { color: #444; }
strong { color: #000; }
a { color: #1463b3; text-decoration: none; }

p:has(> strong:first-child) {
  margin-top: 0.55em;
  padding-top: 0.32em;
  border-top: 1px dashed #d8d8d4;
}
blockquote p:has(> strong:first-child),
li p:has(> strong:first-child) {
  margin-top: 0;
  padding-top: 0;
  border-top: none;
}
CSSEOF

read -r -d '' CSS_LOOSE <<'CSSEOF' || true
@page { size: A4; margin: 1.25cm 1.5cm 1.25cm 1.5cm; }
html { font-family: -apple-system, "Helvetica Neue", Arial, sans-serif; font-size: 9.15pt; line-height: 1.33; color: #1a1a1a; }
body { margin: 0; }
.cv-photo-gutter { float: right; width: 3.4cm; height: 4.3cm; }
h1 { font-size: 14.5pt; margin: 0 0 0.18em 0; font-weight: 700; letter-spacing: -0.01em; }
h3 { font-size: 10.8pt; margin: 0.55em 0 0.22em 0; font-weight: 700; padding-top: 0.35em; border-top: 1px solid #e8e8e5; }
h3:first-of-type { border-top: none; padding-top: 0; }
p { margin: 0 0 0.40em 0; }
ul { margin: 0.2em 0 0.45em 0; padding-left: 1.2em; }
li { margin-bottom: 0.15em; }
blockquote { margin: 0.4em 0 0.55em 0; padding: 0.45em 0.8em; border-left: 3px solid #999; background: #f6f6f4; font-size: 8.85pt; line-height: 1.36; border-radius: 1px; }
blockquote p { margin: 0 0 0.3em 0; }
blockquote p:last-child { margin-bottom: 0; }
hr { border: none; height: 1px; background: linear-gradient(to right, transparent, #b9b9b6 30%, #b9b9b6 70%, transparent); margin: 0.7em auto; width: 70%; }
table { border-collapse: collapse; width: 100%; margin: 0.25em 0 0.45em 0; font-size: 8.85pt; }
th, td { border-bottom: 1px solid #d8d8d8; padding: 2.5pt 6pt; text-align: left; vertical-align: top; }
th { font-weight: 600; background: #f3f3f1; }
code { font-family: "SF Mono", Menlo, Monaco, "Courier New", monospace; font-size: 8.5pt; background: #f1f1ef; padding: 0.8pt 3pt; border-radius: 2px; }
em { color: #444; }
strong { color: #000; }
a { color: #1463b3; text-decoration: none; }

p:has(> strong:first-child) {
  margin-top: 0.95em;
  padding-top: 0.55em;
  border-top: 1px dashed #d8d8d4;
}
blockquote p:has(> strong:first-child),
li p:has(> strong:first-child) {
  margin-top: 0;
  padding-top: 0;
  border-top: none;
}
p + p:not(:has(> strong:first-child)) {
  margin-top: 0.15em;
}
CSSEOF

read -r -d '' CSS_DARK <<'CSSEOF' || true
@page { size: A4; margin: 1.3cm 1.5cm 1.3cm 1.5cm; }
* { print-color-adjust: exact !important; -webkit-print-color-adjust: exact !important; }
html { font-family: -apple-system, "Helvetica Neue", Arial, sans-serif; font-size: 9.15pt; line-height: 1.46; color: #ececec; background: #0c0c0e; }
body { margin: 0; background: #0c0c0e; position: relative; }
.cv-photo-gutter { float: right; width: 3.4cm; height: 4.2cm; }
body::before { content: ""; position: fixed; top: -1.5cm; left: -2cm; right: -2cm; bottom: -1.5cm; background: #0c0c0e; z-index: -1; }
h1 { font-size: 14.5pt; margin: 0 0 0.22em 0; font-weight: 700; letter-spacing: -0.01em; color: #ffffff; }
h3 { font-size: 10.8pt; margin: 1.7em 0 0.45em 0; font-weight: 700; padding-top: 0.5em; border-top: 1px solid rgba(240,183,107,0.30); color: #f0b76b; break-after: avoid; page-break-after: avoid; }
h3:first-of-type { border-top: none; padding-top: 0; margin-top: 0.5em; }
p { margin: 0 0 0.45em 0; color: #ececec; }
ul { margin: 0.35em 0 0.7em 0; padding-left: 1.2em; }
li { margin-bottom: 0.3em; break-inside: avoid; }
blockquote { margin: 0.6em 0 0.8em 0; padding: 0.55em 0.9em; border-left: 3px solid #f0b76b; background: #16161a; font-size: 8.85pt; line-height: 1.45; border-radius: 1px; color: #d8d8d8; }
blockquote p { margin: 0 0 0.3em 0; color: #d8d8d8; }
blockquote p:last-child { margin-bottom: 0; }
hr { border: none; height: 1px; background: linear-gradient(to right, transparent, #f0b76b 30%, #f0b76b 70%, transparent); margin: 1.1em auto; width: 60%; opacity: 0.7; }
table { border-collapse: collapse; width: 100%; margin: 0.3em 0 0.55em 0; font-size: 8.85pt; background: #16161a; }
tr { break-inside: avoid; page-break-inside: avoid; }
th, td { border-bottom: 1px solid rgba(236,236,236,0.10); padding: 3pt 6pt; text-align: left; vertical-align: top; color: #ececec; }
th { font-weight: 600; background: #1f1f23; color: #f0b76b; }
code { font-family: "SF Mono", Menlo, Monaco, "Courier New", monospace; font-size: 8.5pt; background: #1f1f23; padding: 0.8pt 3pt; border-radius: 2px; color: #f0b76b; }
em { color: #b8b8b8; font-style: italic; }
strong { color: #ffffff; }
a { color: #f0b76b; text-decoration: none; }

/* Entry header (company / school / skill category): dashed rule + room above */
p:has(> strong:first-child) {
  margin-top: 1.3em;
  padding-top: 0.6em;
  border-top: 1px dashed rgba(240,183,107,0.30);
  break-after: avoid;
  page-break-after: avoid;
}
/* Masthead tagline and first entry after a section heading: suppress the double rule */
h1 + p:has(> strong:first-child),
h3 + p:has(> strong:first-child) {
  margin-top: 0.5em;
  padding-top: 0;
  border-top: none;
}
/* Italic sub-section label inside an entry: breathing room above its bullets */
p:has(> em:only-child) {
  margin-top: 0.75em;
  margin-bottom: 0.28em;
}
blockquote p:has(> strong:first-child),
li p:has(> strong:first-child) {
  margin-top: 0;
  padding-top: 0;
  border-top: none;
}
p + p:not(:has(> strong:first-child)) {
  margin-top: 0.18em;
}
CSSEOF

read -r -d '' CSS_EDITORIAL <<'CSSEOF' || true
@page { size: A4; margin: 1.2cm 1.45cm 1.2cm 1.45cm; }
html { font-family: "Charter", "Iowan Old Style", "Georgia", serif; font-size: 8.7pt; line-height: 1.48; color: #1a1a1a; }
body { margin: 0; }
.cv-photo-gutter { float: right; width: 3.4cm; height: 4.2cm; }
h1 { font-family: "Helvetica Neue", -apple-system, Arial, sans-serif; font-size: 17pt; margin: 0 0 0.35em 0; font-weight: 800; letter-spacing: -0.015em; text-transform: none; color: #111; padding-bottom: 0.32em; border-bottom: 3px solid #111; overflow: hidden; }
h3 { font-family: "Helvetica Neue", -apple-system, Arial, sans-serif; font-size: 11pt; margin: 2.1em 0 0.65em 0; font-weight: 700; padding-top: 0.65em; border-top: 2px solid #111; text-transform: uppercase; letter-spacing: 0.05em; color: #111; break-after: avoid; page-break-after: avoid; }
h3:first-of-type { border-top: none; padding-top: 0; margin-top: 0.65em; }
p { margin: 0 0 0.58em 0; text-align: justify; hyphens: auto; }
ul { margin: 0.5em 0 0.9em 0; padding-left: 1.35em; list-style: none; }
li { margin-bottom: 0.42em; position: relative; break-inside: avoid; }
li::before { content: "▍"; position: absolute; left: -1.1em; color: #111; font-size: 0.85em; top: 0.15em; }
blockquote { margin: 0.7em 0 0.85em 0; padding: 0.65em 0.95em 0.65em 1.1em; border-left: 4px solid #111; background: #f7f5f0; font-size: 9.4pt; line-height: 1.5; font-style: italic; }
blockquote p { margin: 0 0 0.35em 0; }
blockquote p:last-child { margin-bottom: 0; }
hr { border: none; height: 0; margin: 1.6em 0; text-align: center; }
hr::after { content: "❦"; font-family: "Charter", "Iowan Old Style", "Georgia", serif; font-size: 1.1em; color: #111; }
table { border-collapse: collapse; width: 100%; margin: 0.5em 0 0.7em 0; font-size: 9.2pt; border-top: 2px solid #111; border-bottom: 2px solid #111; }
th, td { padding: 3.5pt 7pt; text-align: left; vertical-align: top; }
th { font-weight: 700; border-bottom: 1px solid #111; background: #f0ece4; font-family: "Helvetica Neue", -apple-system, Arial, sans-serif; font-size: 8.6pt; text-transform: uppercase; letter-spacing: 0.04em; }
tr td { border-bottom: 1px dotted #b0a999; }
tr:last-child td { border-bottom: none; }
code { font-family: "SF Mono", Menlo, Monaco, "Courier New", monospace; font-size: 8.7pt; background: #f0ece4; padding: 1pt 4pt; border-radius: 0; color: #333; }
em { font-style: italic; color: #333; }
strong { color: #111; font-weight: 700; }
a { color: #1a1a1a; text-decoration: underline; text-decoration-thickness: 1px; text-underline-offset: 2px; }

/* Entry header (company / school / skill category): heavy rule + room above */
p:has(> strong:first-child) {
  margin-top: 1.6em;
  padding-top: 0.65em;
  border-top: 2px solid #111;
  break-after: avoid;
  page-break-after: avoid;
}
/* Masthead tagline and first entry after a section heading: suppress the double rule */
h1 + p:has(> strong:first-child),
h3 + p:has(> strong:first-child) {
  margin-top: 0.5em;
  padding-top: 0;
  border-top: none;
}
/* Italic sub-section label inside an entry: breathing room above its bullets */
p:has(> em:only-child) {
  margin-top: 0.95em;
  margin-bottom: 0.32em;
  color: #444;
}
blockquote p:has(> strong:first-child),
li p:has(> strong:first-child) {
  margin-top: 0;
  padding-top: 0;
  border-top: none;
}
CSSEOF

# Loop over every selected sample MD, build all 4 variants.
# Output PDFs are named "<stem>-<variant>.pdf" (stem = MD filename without .md).
for SAMPLE in "${SAMPLES[@]}"; do
  [[ -f "$SAMPLE" ]] || { echo "skip (missing): $SAMPLE"; continue; }
  BASE=$(basename "$SAMPLE" .md)
  # Derive html lang attr from a trailing 2-letter segment (…-de / …-en), else "de".
  TAIL="${BASE##*-}"
  if [[ "$TAIL" =~ ^[a-z]{2}$ ]]; then HTMLLANG="$TAIL"; else HTMLLANG="de"; fi
  # PDF <title> from the first H1 in the markdown, fallback to the stem.
  TITLE="$(grep -m1 '^# ' "$SAMPLE" | sed 's/^# //')"
  [[ -n "$TITLE" ]] || TITLE="$BASE"
  echo
  echo "=== $BASE ==="
  BODY="$(pandoc -f markdown -t html5 --no-highlight "$SAMPLE")"

  build_variant "$BASE" "compact"   "$CSS_COMPACT"   "$HTMLLANG"
  build_variant "$BASE" "loose"     "$CSS_LOOSE"     "$HTMLLANG"
  build_variant "$BASE" "dark"      "$CSS_DARK"      "$HTMLLANG"
  build_variant "$BASE" "editorial" "$CSS_EDITORIAL" "$HTMLLANG"

  # Dark needs full-page underlay; Chrome print-to-pdf leaves @page margins white.
  DARK_PDF="${OUT}/${BASE}-dark.pdf"
  DARK_TMP="${OUT}/${BASE}-dark-tmp.pdf"
  if [[ -f "$DARK_PDF" ]] && command -v uv >/dev/null 2>&1; then
    mv "$DARK_PDF" "$DARK_TMP"
    (cd .. && uv run python production-showcase/_underlay.py \
      "production-showcase/$DARK_TMP" "production-showcase/$DARK_PDF" "#0c0c0e") \
      && rm -f "$DARK_TMP" && echo "Dark ($BASE): full-page underlay applied"
  fi
done

echo
echo "Outputs:"
ls -la "$OUT"/*-compact.pdf "$OUT"/*-loose.pdf "$OUT"/*-dark.pdf "$OUT"/*-editorial.pdf 2>/dev/null

# Fertige PDFs nach iCloud spiegeln, damit sie auf dem iPhone verfügbar sind.
# iCloud folgt keinen Symlinks — deshalb kopieren statt verlinken.
ICLOUD="$HOME/Library/Mobile Documents/com~apple~CloudDocs/Bewerbung"
if [[ -d "$(dirname "$ICLOUD")" && -f icloud.txt ]]; then
  mkdir -p "$ICLOUD"
  # Nur was in icloud.txt steht — alles andere bleibt lokal in out/.
  grep -vE '^\s*(#|$)' icloud.txt \
    | rsync -a --files-from=- "$OUT"/ "$ICLOUD/" 2>/dev/null \
    && echo "iCloud: $(ls "$ICLOUD"/*.pdf 2>/dev/null | wc -l | tr -d ' ') Dateien → $ICLOUD"
fi
