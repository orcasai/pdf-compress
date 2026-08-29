#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SOURCE="../export/cv-translation/_source/cv-de-agentic.md"
OUTDIR="cv"
LANG="de"
NAME="Robin Walter Scherler"
TAGLINE="Agentic Engineer · Production-LLM-Systeme &amp; Multi-Agent-Orchestrierung · 7+ Jahre Full-Stack"
LOCATION="Neidenstein · Deutschland · scherler89@gmail.com · agentic-engineer.online · linkedin.com/in/robin-s-223606136"

[[ -f "$SOURCE" ]] || { echo "missing source: $SOURCE"; exit 1; }
mkdir -p "$OUTDIR"

# Masthead injected before the pandoc body — the CV markdown has no name header.
MASTHEAD="<header class=\"masthead\"><div class=\"cvname\">${NAME}</div><div class=\"cvtag\">${TAGLINE}</div><div class=\"cvmeta\">${LOCATION}</div></header>"

build_variant() {
  local VARNAME="$1"; local CSS="$2"
  local STEM="${OUTDIR}/cv-robin-walter-scherler-${LANG}-${VARNAME}"
  local HTML="${STEM}.html"
  local PDF_RAW="${STEM}-raw.pdf"
  local PDF_OUT="${STEM}.pdf"

  cat > "$HTML" <<HTMLEOF
<!doctype html>
<html lang="${LANG}">
<head>
<meta charset="utf-8">
<title>${NAME} — Lebenslauf</title>
<style>
${CSS}
</style>
</head>
<body>
${MASTHEAD}
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

# ---------------------------------------------------------------------------
# DARK — black canvas, amber accent. Robin's favourite from the writing sample.
# ---------------------------------------------------------------------------
read -r -d '' CSS_DARK <<'CSSEOF' || true
@page { size: A4; margin: 1.2cm 1.4cm 1.2cm 1.4cm; }
* { print-color-adjust: exact !important; -webkit-print-color-adjust: exact !important; }
html { font-family: -apple-system, "Helvetica Neue", Arial, sans-serif; font-size: 9pt; line-height: 1.34; color: #ececec; background: #0c0c0e; }
body { margin: 0; background: #0c0c0e; position: relative; }
body::before { content: ""; position: fixed; top: -1.5cm; left: -2cm; right: -2cm; bottom: -1.5cm; background: #0c0c0e; z-index: -1; }

.masthead { margin: 0 0 0.5em 0; padding-bottom: 0.45em; border-bottom: 2px solid #f0b76b; }
.cvname { font-size: 22pt; font-weight: 800; letter-spacing: -0.02em; color: #ffffff; }
.cvtag { font-size: 9pt; color: #f0b76b; margin-top: 0.3em; letter-spacing: 0.01em; }
.cvmeta { font-size: 8.5pt; color: #9a9a9a; margin-top: 0.15em; }

/* Address section is redundant — location lives in the masthead. */
#adresse, #adresse + p { display: none; }

h1 { font-size: 12.5pt; font-weight: 700; color: #f0b76b; margin: 0.85em 0 0.3em 0; padding-top: 0.4em; border-top: 1px solid rgba(240,183,107,0.22); text-transform: uppercase; letter-spacing: 0.05em; break-after: avoid; page-break-after: avoid; }
h2 { font-size: 10.5pt; font-weight: 700; color: #ffffff; margin: 0.6em 0 0.1em 0; break-after: avoid; page-break-after: avoid; break-inside: avoid; }
h3 { font-size: 9.3pt; font-weight: 600; color: #f0b76b; margin: 0.15em 0 0.1em 0; break-after: avoid; page-break-after: avoid; }
p { margin: 0 0 0.3em 0; color: #ececec; }
ul { margin: 0.15em 0 0.4em 0; padding-left: 1.1em; }
li { margin-bottom: 0.12em; }
strong { color: #ffffff; }
em { color: #b8b8b8; font-style: italic; }
a { color: #f0b76b; text-decoration: none; word-break: break-all; }
blockquote { margin: 0.3em 0 0.65em 0; padding: 0.5em 0.85em; border-left: 3px solid #f0b76b; background: #16161a; color: #d8d8d8; font-size: 9pt; line-height: 1.4; }
blockquote p { margin: 0; color: #d8d8d8; }
hr { border: none; height: 1px; background: linear-gradient(to right, transparent, #f0b76b 30%, #f0b76b 70%, transparent); margin: 0.7em auto; width: 60%; opacity: 0.7; }
CSSEOF

# ---------------------------------------------------------------------------
# EDITORIAL — serif body, sans headings, heavy rules. Classic, print-serious.
# ---------------------------------------------------------------------------
read -r -d '' CSS_EDITORIAL <<'CSSEOF' || true
@page { size: A4; margin: 1.1cm 1.35cm 1.1cm 1.35cm; }
html { font-family: "Charter", "Iowan Old Style", "Georgia", serif; font-size: 8.8pt; line-height: 1.32; color: #1a1a1a; }
body { margin: 0; }

.masthead { border-bottom: 3px solid #111; margin-bottom: 0.55em; padding-bottom: 0.35em; }
.cvname { font-family: "Helvetica Neue", -apple-system, Arial, sans-serif; font-size: 23pt; font-weight: 800; letter-spacing: -0.015em; color: #111; }
.cvtag { font-family: "Helvetica Neue", -apple-system, Arial, sans-serif; font-size: 8.6pt; color: #444; margin-top: 0.35em; text-transform: uppercase; letter-spacing: 0.05em; }
.cvmeta { font-family: "Helvetica Neue", -apple-system, Arial, sans-serif; font-size: 8.4pt; color: #666; margin-top: 0.12em; }

#adresse, #adresse + p { display: none; }

h1 { font-family: "Helvetica Neue", -apple-system, Arial, sans-serif; font-size: 12pt; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #111; border-top: 2px solid #111; padding-top: 0.4em; margin: 0.85em 0 0.3em 0; break-after: avoid; page-break-after: avoid; }
h2 { font-family: "Helvetica Neue", -apple-system, Arial, sans-serif; font-size: 10pt; font-weight: 700; color: #111; margin: 0.55em 0 0.05em 0; break-after: avoid; page-break-after: avoid; break-inside: avoid; }
h3 { font-size: 9.3pt; font-weight: 700; font-style: italic; color: #333; margin: 0.1em 0 0.1em 0; break-after: avoid; page-break-after: avoid; }
p { margin: 0 0 0.32em 0; }
ul { margin: 0.2em 0 0.45em 0; padding-left: 1.2em; list-style: none; }
li { position: relative; margin-bottom: 0.14em; }
li::before { content: "▍"; position: absolute; left: -1em; color: #111; font-size: 0.8em; top: 0.15em; }
strong { color: #111; font-weight: 700; }
em { font-style: italic; color: #333; }
a { color: #1a1a1a; text-decoration: underline; text-underline-offset: 2px; word-break: break-all; }
blockquote { margin: 0.3em 0 0.65em 0; padding: 0.5em 0.9em 0.5em 1em; border-left: 4px solid #111; background: #f7f5f0; font-style: italic; font-size: 9pt; line-height: 1.4; }
blockquote p { margin: 0; }
hr { border: none; height: 0; margin: 0.85em 0; text-align: center; }
hr::after { content: "❦"; font-family: "Charter", "Iowan Old Style", "Georgia", serif; font-size: 1.1em; color: #111; }
CSSEOF

echo "=== Building CV ($LANG) ==="
BODY="$(pandoc -f markdown -t html5 --no-highlight "$SOURCE")"

build_variant "dark"      "$CSS_DARK"
build_variant "editorial" "$CSS_EDITORIAL"

# Dark needs a full-page underlay; Chrome leaves @page margins white.
DARK_PDF="${OUTDIR}/cv-robin-walter-scherler-${LANG}-dark.pdf"
DARK_TMP="${OUTDIR}/cv-robin-walter-scherler-${LANG}-dark-tmp.pdf"
if [[ -f "$DARK_PDF" ]] && command -v uv >/dev/null 2>&1; then
  mv "$DARK_PDF" "$DARK_TMP"
  (cd .. && uv run python production-showcase/_underlay.py \
    "production-showcase/$DARK_TMP" "production-showcase/$DARK_PDF" "#0c0c0e") \
    && rm -f "$DARK_TMP" && echo "Dark: full-page underlay applied"
fi

echo
echo "Outputs:"
ls -la "$OUTDIR"/*.pdf 2>/dev/null
