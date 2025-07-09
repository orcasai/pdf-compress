from pathlib import Path
from PIL import Image, ImageDraw

def crop_to_circle(
    input_path,
    output_path,
    vertical_shift_pct=0.12,
    horizontal_shift_px=0,
    padding_pct=0.0
):
    """
    Schneidet ein Bild zu einem Kreis zu.
    
    Args:
        input_path: Pfad zum Input-Bild
        output_path: Pfad zum Output-Bild (PNG mit Transparenz)
        vertical_shift_pct: Vertikale Verschiebung als Prozent der Bildgröße
        horizontal_shift_px: Horizontale Verschiebung in Pixeln
        padding_pct: Innenabstand als Prozent (macht Kreis kleiner)
    """
    image = Image.open(input_path)

    # Kleinstes Quadrat bestimmen + verschieben
    min_dim = min(image.width, image.height)
    shift_y = int(min_dim * vertical_shift_pct)
    shift_x = horizontal_shift_px

    crop_left = (image.width - min_dim) // 2 + shift_x
    crop_top = (image.height - min_dim) // 2 - shift_y
    crop_box = (crop_left, crop_top, crop_left + min_dim, crop_top + min_dim)
    square = image.crop(crop_box)

    # Maske vorbereiten mit Innenabstand (Padding)
    padding = int(min_dim * padding_pct)
    mask = Image.new("L", (min_dim, min_dim), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((padding, padding, min_dim - padding, min_dim - padding), fill=255)

    # Bild mit Maske kombinieren
    result = Image.new("RGBA", (min_dim, min_dim))
    result.paste(square, (0, 0), mask=mask)

    result.save(output_path)
    print(f"✅ Kreisbild erstellt: {output_path}")

# 🔧 Standalone-Beispiel für neue Projektstruktur
if __name__ == "__main__":
    BASE = Path(__file__).parent
    
    # Input aus data/ Verzeichnis
    input_image = BASE.parent / "data" / "images" / "cv-image.jpg"
    
    # Output ins output/ Verzeichnis
    output_dir = BASE.parent / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    output_image = output_dir / "01-crop-circle-output.png"
    
    print(f"🔄 Erstelle Kreis-Bild: {input_image.name} → {output_image.name}")
    
    crop_to_circle(
        input_path=input_image,
        output_path=output_image,
        vertical_shift_pct=0.05,     # Optimierte Parameter
        horizontal_shift_px=16,      # Optimierte Parameter  
        padding_pct=0.06             # Optimierte Parameter
    )
    
    print(f"✅ Kreis-Bild erstellt: {output_image}")