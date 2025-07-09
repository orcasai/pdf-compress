#!/usr/bin/env python3
"""
Optimierter CV-Image-Workflow:
1. Profilbild EINMAL zu Kreis zuschneiden
2. Kreis in BEIDE PDF-Varianten einfügen  
3. BEIDE PDFs komprimieren
"""

from pathlib import Path
from .crop_circle import crop_to_circle
from .insert_image import insert_image_to_pdf
from .compress_pdf import compress_pdf, get_pdf_size

def process_cv_workflow():
    """
    Optimierter CV-PDF-Workflow für beide Farben (Green + Orange).
    
    Workflow-Schritte:
    1. Profilbild einmal zu Kreis zuschneiden → 01-crop-circle-output.png
    2. Kreis in beide PDFs einfügen:
       - Green → 02-CV-PR-Green-with-image.pdf  
       - Orange → 02-CV-PR-Orange-with-image.pdf
    3. Beide PDFs komprimieren:
       - Green → 03-CV-PR-Green-final.pdf
       - Orange → 03-CV-PR-Orange-final.pdf
    """
    BASE = Path(__file__).parent.parent
    
    # Input-Pfade (neue Struktur)
    input_image = BASE / "data" / "images" / "cv-image.jpg"
    green_pdf = BASE / "data" / "pdfs" / "CV-PR-Green.pdf"
    orange_pdf = BASE / "data" / "pdfs" / "CV-PR-Orange.pdf"
    
    # Output-Verzeichnis
    output_dir = BASE / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Output-Pfade (nummeriert nach Workflow-Schritten)
    circle_image = output_dir / "01-crop-circle-output.png"
    green_with_image = output_dir / "02-CV-PR-Green-with-image.pdf"
    orange_with_image = output_dir / "02-CV-PR-Orange-with-image.pdf"
    green_final = output_dir / "03-CV-PR-Green-final.pdf"
    orange_final = output_dir / "03-CV-PR-Orange-final.pdf"
    
    print("🎯 Optimierter CV-PDF-Workflow")
    print("="*50)
    print(f"📁 Input Bild: {input_image}")
    print(f"📁 Input PDFs: {green_pdf.name}, {orange_pdf.name}")
    print(f"📁 Output: {output_dir}")
    
    # Prüfe Input-Dateien
    missing_files = []
    if not input_image.exists():
        missing_files.append(str(input_image))
    if not green_pdf.exists():
        missing_files.append(str(green_pdf))
    if not orange_pdf.exists():
        missing_files.append(str(orange_pdf))
        
    if missing_files:
        print(f"❌ Fehlende Input-Dateien:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    
    try:
        # 📸 SCHRITT 1: Profilbild EINMAL zu Kreis zuschneiden
        print(f"\n📸 Schritt 1: Profilbild zu Kreis zuschneiden...")
        crop_to_circle(
            input_path=input_image,
            output_path=circle_image,
            vertical_shift_pct=0.05,     # Optimierte Parameter
            horizontal_shift_px=16,      # Optimierte Parameter  
            padding_pct=0.06             # Optimierte Parameter
        )
        print(f"✅ Kreis erstellt: {circle_image.name}")
        
        # 📄 SCHRITT 2: Kreis in BEIDE PDFs einfügen
        print(f"\n📄 Schritt 2: Kreis in beide PDFs einfügen...")
        
        # Green PDF
        insert_image_to_pdf(
            pdf_path=green_pdf,
            image_path=circle_image,
            output_path=green_with_image,
            position=(35, 22),
            size=(110, 110)
        )
        print(f"✅ Green PDF erstellt: {green_with_image.name}")
        
        # Orange PDF  
        insert_image_to_pdf(
            pdf_path=orange_pdf,
            image_path=circle_image,
            output_path=orange_with_image,
            position=(35, 22),
            size=(110, 110)
        )
        print(f"✅ Orange PDF erstellt: {orange_with_image.name}")
        
        # 🗜️ SCHRITT 3: BEIDE PDFs komprimieren
        print(f"\n🗜️ Schritt 3: PDFs komprimieren...")
        
        # Green PDF komprimieren
        green_original_size = get_pdf_size(green_with_image)
        compress_pdf(
            input_path=green_with_image,
            output_path=green_final,
            quality="custom-balanced"
        )
        green_compressed_size = get_pdf_size(green_final)
        green_ratio = (1 - green_compressed_size / green_original_size) * 100
        print(f"✅ Green: {green_original_size:.2f} MB → {green_compressed_size:.2f} MB ({green_ratio:.1f}% kleiner)")
        
        # Orange PDF komprimieren
        orange_original_size = get_pdf_size(orange_with_image)
        compress_pdf(
            input_path=orange_with_image,
            output_path=orange_final,
            quality="custom-balanced"
        )
        orange_compressed_size = get_pdf_size(orange_final)
        orange_ratio = (1 - orange_compressed_size / orange_original_size) * 100
        print(f"✅ Orange: {orange_original_size:.2f} MB → {orange_compressed_size:.2f} MB ({orange_ratio:.1f}% kleiner)")
        
        print(f"\n🎉 Workflow erfolgreich abgeschlossen!")
        print(f"📁 Finale Dateien:")
        print(f"   - {green_final.name}")
        print(f"   - {orange_final.name}")
        
        return True
        
    except Exception as e:
        print(f"❌ Fehler im Workflow: {e}")
        return False

def main():
    """Hauptfunktion."""
    BASE = Path(__file__).parent.parent
    
    # Verfügbare Dateien anzeigen
    print("📂 Verfügbare Input-Dateien:")
    images_dir = BASE / "data" / "images"
    pdfs_dir = BASE / "data" / "pdfs"
    
    if images_dir.exists():
        print("  Bilder:")
        for img in images_dir.glob("*"):
            if img.is_file():
                print(f"    - {img.name}")
    
    if pdfs_dir.exists():
        print("  PDFs:")
        for pdf in pdfs_dir.glob("*.pdf"):
            print(f"    - {pdf.name}")
    
    # Starte optimierten Workflow
    print(f"\n🚀 Starte optimierten CV-Workflow...")
    success = process_cv_workflow()
    
    if not success:
        print(f"❌ Workflow fehlgeschlagen!")
        return False
    
    return True

if __name__ == "__main__":
    main()