import subprocess
import shutil
from pathlib import Path

def compress_pdf_variants(input_path, output_dir):
    """
    Komprimiert eine PDF-Datei mit verschiedenen Ghostscript-Varianten zum Vergleich.
    
    Args:
        input_path: Pfad zur Input-PDF-Datei
        output_dir: Verzeichnis für alle Output-Varianten
    
    Returns:
        Dict mit Varianten-Namen und deren Pfaden/Größen
    """
    # Prüfe ob Ghostscript installiert ist
    if not shutil.which("gs"):
        raise FileNotFoundError(
            "Ghostscript ist nicht installiert. Installiere es mit: brew install ghostscript"
        )
    
    input_path = Path(input_path)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Absolute Spitzenqualität - Fokus auf perfekte Weißtöne und Bildoptimierung
    variants = {
        # Die beiden bewährten Champions
        "custom-balanced": [
            "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4", 
            "-dPDFSETTINGS=/printer", "-dNOPAUSE", "-dQUIET", "-dBATCH",
            "-dColorImageResolution=250", "-dGrayImageResolution=250",
            "-dDownsampleColorImages=false", "-dDownsampleGrayImages=false"
        ],
        "ultra-high-quality": [
            "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4", 
            "-dPDFSETTINGS=/prepress", "-dNOPAUSE", "-dQUIET", "-dBATCH",
            "-dColorImageResolution=600", "-dGrayImageResolution=600",
            "-dDownsampleColorImages=false", "-dDownsampleGrayImages=false",
            "-dUseFlateCompression=true"
        ],
        # ABSOLUTE PREMIUM QUALITÄT - Neue Champions
        "maximum-quality": [
            "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4", 
            "-dPDFSETTINGS=/prepress", "-dNOPAUSE", "-dQUIET", "-dBATCH",
            "-dColorImageResolution=1200", "-dGrayImageResolution=1200",
            "-dDownsampleColorImages=false", "-dDownsampleGrayImages=false",
            "-dUseFlateCompression=true", "-dCompressPages=false",
            "-dAutoFilterColorImages=false", "-dColorImageFilter=/FlateEncode"
        ],
        "perfect-whites": [
            "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4", 
            "-dPDFSETTINGS=/prepress", "-dNOPAUSE", "-dQUIET", "-dBATCH",
            "-dColorImageResolution=800", "-dGrayImageResolution=800",
            "-dDownsampleColorImages=false", "-dDownsampleGrayImages=false",
            "-dPreserveHalftoneInfo=true", "-dPreserveOPIComments=true",
            "-dUseFlateCompression=true", "-dColorConversionStrategy=/LeaveColorUnchanged"
        ],
        "skin-optimized": [
            "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4", 
            "-dPDFSETTINGS=/prepress", "-dNOPAUSE", "-dQUIET", "-dBATCH",
            "-dColorImageResolution=600", "-dGrayImageResolution=600",
            "-dDownsampleColorImages=false", "-dDownsampleGrayImages=false",
            "-dAutoFilterColorImages=false", "-dColorImageFilter=/FlateEncode",
            "-dAntiAliasColorImages=true", "-dAntiAliasGrayImages=true"
        ],
        "archive-quality": [
            "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4", 
            "-dPDFSETTINGS=/prepress", "-dNOPAUSE", "-dQUIET", "-dBATCH",
            "-dColorImageResolution=1200", "-dGrayImageResolution=1200",
            "-dDownsampleColorImages=false", "-dDownsampleGrayImages=false",
            "-dPreserveHalftoneInfo=true", "-dPreserveOPIComments=true",
            "-dPreserveOverprintSettings=true", "-dUseFlateCompression=true"
        ],
        "professional-print": [
            "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4", 
            "-dPDFSETTINGS=/prepress", "-dNOPAUSE", "-dQUIET", "-dBATCH",
            "-dColorImageResolution=1200", "-dGrayImageResolution=1200",
            "-dDownsampleColorImages=false", "-dDownsampleGrayImages=false",
            "-dColorConversionStrategy=/LeaveColorUnchanged",
            "-dPreserveOverprintSettings=true", "-dAutoRotatePages=/None"
        ]
    }
    
    results = {}
    base_name = input_path.stem
    
    print(f"📊 Teste {len(variants)} Komprimierungs-Varianten für: {input_path.name}")
    print(f"Original-Größe: {get_pdf_size(input_path):.2f} MB")
    print("-" * 80)
    
    for variant_name, cmd_base in variants.items():
        output_path = output_dir / f"{base_name}-{variant_name}.pdf"
        cmd = cmd_base + [f"-sOutputFile={output_path}", str(input_path)]
        
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            size_mb = get_pdf_size(output_path)
            original_size = get_pdf_size(input_path)
            compression_ratio = (1 - size_mb / original_size) * 100
            
            results[variant_name] = {
                "path": output_path,
                "size_mb": size_mb,
                "compression_ratio": compression_ratio
            }
            
            print(f"✅ {variant_name:15} → {size_mb:5.2f} MB ({compression_ratio:4.1f}% kleiner)")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ {variant_name:15} → FEHLER: {e}")
            results[variant_name] = {"error": str(e)}
    
    print("-" * 80)
    print("📈 Zusammenfassung (sortiert nach Komprimierung):")
    
    # Sortiere nach Komprimierungsrate
    successful = {k: v for k, v in results.items() if "error" not in v}
    sorted_results = sorted(successful.items(), key=lambda x: x[1]["compression_ratio"], reverse=True)
    
    for i, (variant, data) in enumerate(sorted_results, 1):
        print(f"{i}. {variant:15} → {data['size_mb']:5.2f} MB ({data['compression_ratio']:4.1f}% kleiner)")
    
    return results

def compress_pdf(input_path, output_path, quality="screen", dpi=150):
    """
    Komprimiert eine PDF-Datei mit der bewährten Ghostscript-Konfiguration.
    
    Args:
        input_path: Pfad zur Input-PDF-Datei
        output_path: Pfad zur Output-PDF-Datei
        quality: PDF-Qualitätsstufe ('screen', 'ebook', 'printer')
        dpi: DPI für Farbbilder
    """
    # Prüfe ob Ghostscript installiert ist
    if not shutil.which("gs"):
        raise FileNotFoundError(
            "Ghostscript ist nicht installiert. Installiere es mit: brew install ghostscript"
        )
    
    input_path = Path(input_path)
    output_path = Path(output_path)
    
    # Erstelle Output-Verzeichnis falls es nicht existiert
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Verwende die bewährte "custom-balanced" Konfiguration
    if quality == "custom-balanced":
        cmd = [
            "gs", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4", 
            "-dPDFSETTINGS=/printer", "-dNOPAUSE", "-dQUIET", "-dBATCH",
            "-dColorImageResolution=250", "-dGrayImageResolution=250",
            "-dDownsampleColorImages=false", "-dDownsampleGrayImages=false",
            f"-sOutputFile={output_path}",
            str(input_path)
        ]
    else:
        # Standard-Konfiguration
        cmd = [
            "gs",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            f"-dPDFSETTINGS=/{quality}",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            f"-dColorImageResolution={dpi}",
            f"-sOutputFile={output_path}",
            str(input_path)
        ]
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ PDF komprimiert: {output_path}")
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"❌ Fehler beim Komprimieren: {e}")
        print(f"Stderr: {e.stderr}")
        raise

def get_pdf_size(pdf_path):
    """Gibt die Dateigröße einer PDF in MB zurück."""
    return Path(pdf_path).stat().st_size / (1024 * 1024)

# Beispiel-Nutzung
if __name__ == "__main__":
    BASE = Path(__file__).parent.parent
    
    # Beispiel-Komprimierung für neue Projektstruktur
    input_pdf = BASE.parent / "output" / "02-cv-with-image.pdf"
    output_pdf = BASE.parent / "output" / "cv-robin-walter-scherler-gr.pdf"
    
    if input_pdf.exists():
        print(f"Original-Größe: {get_pdf_size(input_pdf):.2f} MB")
        compress_pdf(input_pdf, output_pdf)
        print(f"Komprimierte Größe: {get_pdf_size(output_pdf):.2f} MB")
    else:
        print(f"❌ Input-Datei nicht gefunden: {input_pdf}")