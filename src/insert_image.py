import fitz  # pip install pymupdf
from pathlib import Path

def insert_image_to_pdf(pdf_path, image_path, output_path, position, size):
    """
    Fügt ein Bild in eine PDF-Datei ein.
    
    Args:
        pdf_path: Pfad zur Input-PDF-Datei
        image_path: Pfad zum Bild, das eingefügt werden soll
        output_path: Pfad zur Output-PDF-Datei
        position: (x, y) Position in Punkten (von unten links)
        size: (width, height) Größe in Punkten
    """
    pdf_path = Path(pdf_path)
    image_path = Path(image_path)
    output_path = Path(output_path)
    
    # Erstelle Output-Verzeichnis falls es nicht existiert
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    doc = fitz.open(pdf_path)
    page = doc[0]  # erste Seite
    
    # Lade Bild
    img_rect = fitz.Rect(position[0], position[1],
                         position[0] + size[0], position[1] + size[1])
    page.insert_image(img_rect, filename=str(image_path), overlay=True)
    
    doc.save(output_path)
    doc.close()
    print(f"✅ Bild in PDF eingefügt: {output_path}")
    return output_path

# Beispiel-Nutzung
if __name__ == "__main__":
    BASE = Path(__file__).parent.parent
    
    # Beispiel für neue Projektstruktur
    input_pdf = BASE.parent / "data" / "pdfs" / "CV-PR-Green.pdf"
    input_image = BASE.parent / "output" / "01-crop-circle-output.png"
    output_pdf = BASE.parent / "output" / "02-CV-PR-Green-with-image.pdf"
    
    print(f"🔄 Füge {input_image.name} in {input_pdf.name} ein...")
    
    insert_image_to_pdf(
        pdf_path=input_pdf,
        image_path=input_image,
        output_path=output_pdf,
        position=(35, 22),           # X, Y in pt (von unten links)
        size=(110, 110)              # Breite, Höhe in pt
    )