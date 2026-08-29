#!/usr/bin/env python3
"""Stempelt ein kreisförmiges Profilbild in die generierten CV-PDFs.

Mehrere Foto-Sets möglich (Original-Foto und KI-Bild mit AI-Generated-Badge).
Ein Lauf erzeugt jedes Set x jeden Stil -> viele Versionen zum Vergleichen.

Originalskripte (src/crop_circle.py, src/insert_image.py) bleiben unangetastet;
die Zusatzlogik (Disc-Hintergrund, Ring, Badge-Overlay, Klick-Link, Multi-Set)
lebt ausschliesslich hier.

Aufruf vom Repo-Root:
    uv run python production-showcase/add_photo.py                 # alle Sets x alle Stile
    uv run python production-showcase/add_photo.py --set ai        # nur KI-Set
    uv run python production-showcase/add_photo.py --only dark      # nur Dark-Stil

Ausgabe: <stem><suffix>.pdf neben dem jeweiligen Original (nicht-destruktiv).
  -photo     = Original-Lebenslaufbild
  -photo-ai  = KI-generiertes Bild + AI-Generated-Badge + Klick-Link auf GitHub
"""
from __future__ import annotations

import argparse
import sys
import tempfile
from pathlib import Path

import fitz
from PIL import Image, ImageDraw

BASE = Path(__file__).resolve().parent.parent  # Repo-Root
sys.path.insert(0, str(BASE))
from src.crop_circle import crop_to_circle        # unveraendert
from src.insert_image import insert_image_to_pdf  # unveraendert

SHOW = BASE / "production-showcase" / "out"  # Endfassungen; build.sh schreibt hierhin
IMG = BASE / "data" / "images"

# --- Stil-spezifisch: Position/Groesse/Disc-Hintergrund/Ring (fuer alle Sets) ---
# pos = (x, y) in Punkten von OBEN-LINKS, size = Durchmesser. Foto sitzt im
# .cv-photo-gutter (rechter Float in build.sh), darum keine Text-Ueberlappung.
STYLES = {
    # pos = flush oben-rechts an der Content-Box (Seite 595.3pt minus @page-Margin)
    "editorial": {"pos": (470, 34), "size": 84, "bg": "#ffffff", "ring": ("#d8d2c4", 3)},
    "loose":     {"pos": (469, 35), "size": 84, "bg": "#ffffff", "ring": ("#dcdcdc", 3)},
    "compact":   {"pos": (496, 13), "size": 74, "bg": "#ffffff", "ring": ("#dcdcdc", 2)},
    "dark":      {"pos": (469, 37), "size": 84, "bg": "#0c0c0e", "ring": ("#f0b76b", 3)},
}

# Sprachen: Ziel-PDFs heißen cv-robin-<lang>-<style>.pdf (build.sh-Konvention)
LANGS = ["de", "en", "kurz-de", "kurz-en"]

# --- Foto-Sets: Quellbild + Crop + optionales Badge + optionaler Klick-Link ---
# badge: kleines Banner unten in den Kreis (scale = Anteil Disc-Breite,
#        vpos_pct = vertikale Mitte als Anteil der Disc-Hoehe).
PHOTO_SETS = {
    "original": {
        "image": IMG / "cv-image.jpg",
        "crop": dict(vertical_shift_pct=0.05, horizontal_shift_px=16, padding_pct=0.06),
        "badge": None,
        "link": None,
        "suffix": "-photo",
    },
    "ai": {
        "image": IMG / "ai-generated.png",  # KI-generiertes Profilbild (winkend)
        "crop": dict(vertical_shift_pct=0.0, horizontal_shift_px=0, padding_pct=0.06),
        "badge": {"image": IMG / "ai-generated-github-marketing.jpeg",
                  "scale": 0.70, "gap": 0.06},  # ORCAS-AI-Banner UNTER den Kreis
        "link": "https://github.com/orcasai",         # Klick aufs Foto -> GitHub
        "suffix": "-photo-ai",
    },
}


def _disc_bbox(img: Image.Image) -> tuple[int, int, int, int]:
    """Kreis-Geometrie aus der Alpha-Bounding-Box (robust ggue. padding_pct)."""
    return img.split()[3].getbbox() or (0, 0, img.width, img.height)


def styled_circle(circle_png: Path, bg=None, ring=None) -> Image.Image:
    """Disc-Hintergrundfarbe + Rahmen-Ring auf das Kreis-PNG legen.
    Transparente Ecken bleiben transparent (PDF scheint durch)."""
    img = Image.open(circle_png).convert("RGBA")
    x0, y0, x1, y1 = _disc_bbox(img)
    if bg:
        base = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ImageDraw.Draw(base).ellipse((x0, y0, x1, y1), fill=bg)
        base.alpha_composite(img)
        img = base
    if ring:
        color, w = ring
        ins = w // 2
        ImageDraw.Draw(img).ellipse((x0 + ins, y0 + ins, x1 - ins, y1 - ins),
                                    outline=color, width=w)
    return img


def stack_badge(circle_img: Image.Image, badge_cfg: dict) -> tuple[Image.Image, float]:
    """Setzt das Badge-Banner mittig UNTER den Kreis (eigenes Bild, transparenter
    Spalt). Gibt (kombiniertes RGBA-Bild, Höhenfaktor) zurück; Faktor =
    Gesamthöhe / Kreis-Seitenlänge → für die Insert-Rect-Höhe."""
    cw = circle_img.width
    b = Image.open(badge_cfg["image"]).convert("RGBA")
    bw = int(cw * badge_cfg.get("scale", 0.92))
    bh = int(bw * b.height / b.width)
    b = b.resize((bw, bh), Image.Resampling.LANCZOS)
    gap = int(cw * badge_cfg.get("gap", 0.06))
    out = Image.new("RGBA", (cw, circle_img.height + gap + bh), (0, 0, 0, 0))
    out.alpha_composite(circle_img, (0, 0))
    out.alpha_composite(b, ((cw - bw) // 2, circle_img.height + gap))
    return out, out.height / circle_img.height


def add_link(pdf_path: Path, rect: tuple[float, float, float, float], uri: str) -> None:
    """Macht das Foto-Rect klickbar (URI-Link) — nach dem Bild-Insert."""
    doc = fitz.open(pdf_path)
    doc[0].insert_link({"kind": fitz.LINK_URI, "from": fitz.Rect(*rect), "uri": uri})
    doc.saveIncr()
    doc.close()


def mirror_to_icloud() -> None:
    """Fertige PDFs nach iCloud spiegeln — wie der Schlussschritt in build.sh.

    iCloud folgt keinen Symlinks, deshalb kopieren. Ohne iCloud passiert nichts.
    """
    import shutil
    import subprocess

    ziel = Path.home() / "Library/Mobile Documents/com~apple~CloudDocs/Bewerbung"
    manifest = SHOW.parent / "icloud.txt"
    if not ziel.parent.is_dir() or not manifest.exists():
        return
    namen = [z.strip() for z in manifest.read_text().splitlines()
             if z.strip() and not z.lstrip().startswith("#")]
    ziel.mkdir(parents=True, exist_ok=True)
    subprocess.run(["rsync", "-a", "--files-from=-", f"{SHOW}/", f"{ziel}/"],
                   input="\n".join(namen), text=True, check=True)
    print(f"iCloud: {len(list(ziel.glob('*.pdf')))} Dateien → {ziel}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--set", nargs="*", choices=list(PHOTO_SETS),
                    help="Foto-Sets (Default: alle)")
    ap.add_argument("--only", nargs="*", choices=list(STYLES),
                    help="Stile (Default: alle)")
    ap.add_argument("--lang", nargs="*", choices=LANGS,
                    help="Sprachen (Default: alle)")
    args = ap.parse_args()

    sets = args.set or list(PHOTO_SETS)
    styles = args.only or list(STYLES)
    langs = args.lang or LANGS

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for sk in sets:
            ps = PHOTO_SETS[sk]
            circle = tmp / f"circle-{sk}.png"
            crop_to_circle(ps["image"], circle, **ps["crop"])  # Originalskript
            for stk in styles:
                st = STYLES[stk]
                # gestyltes Foto-PNG einmal pro (Set, Stil) bauen, dann in alle Sprachen stempeln
                circ = styled_circle(circle, bg=st.get("bg"), ring=st.get("ring"))
                s = st["size"]
                x, y = st["pos"]
                png = tmp / f"{sk}-{stk}.png"
                if ps.get("badge"):
                    combined, hfac = stack_badge(circ, ps["badge"])
                    combined.save(png, "PNG", optimize=True)
                    h = s * hfac
                else:
                    circ.save(png, "PNG", optimize=True)
                    h = s
                for lang in langs:
                    pdf = SHOW / f"cv-robin-{lang}-{stk}.pdf"
                    if not pdf.exists():
                        print(f"⏭️  fehlt, uebersprungen: {pdf.name}")
                        continue
                    out = pdf.with_name(pdf.stem + ps["suffix"] + ".pdf")
                    insert_image_to_pdf(pdf, png, out, position=(x, y), size=(s, h))
                    if ps.get("link"):
                        add_link(out, (x, y, x + s, y + h), ps["link"])

    mirror_to_icloud()


if __name__ == "__main__":
    main()
