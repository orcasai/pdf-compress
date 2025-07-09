#!/usr/bin/env python3
"""
Test-Script für PDF-Komprimierung - testet alle Varianten
"""

from pathlib import Path
from src.compress_pdf import compress_pdf_variants

def main():
    BASE = Path(__file__).parent
    
    # Test-Datei
    input_pdf = BASE / "outputs" / "pdfs_with_images" / "CV-PR-Green-Final.pdf"
    
    if not input_pdf.exists():
        print(f"❌ Test-Datei nicht gefunden: {input_pdf}")
        print("Bitte erst den Hauptworkflow ausführen: uv run python main.py")
        return
    
    # Alle Varianten testen
    output_dir = BASE / "outputs" / "compression_tests"
    
    print("🧪 Starte Komprimierungs-Tests...")
    print("=" * 80)
    
    results = compress_pdf_variants(input_pdf, output_dir)
    
    print("\n🎯 Nächste Schritte:")
    print("1. Öffne die verschiedenen PDFs und prüfe die Qualität")
    print("2. Wähle die beste Kombination aus Größe und Qualität")
    print("3. Die Dateien sind hier zu finden:")
    print(f"   {output_dir}")
    
    # Alle erstellten Dateien auflisten
    print("\n📁 Erstellte Dateien:")
    for variant, data in results.items():
        if "error" not in data:
            print(f"   {data['path'].name}")

if __name__ == "__main__":
    main()