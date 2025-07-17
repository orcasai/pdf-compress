(base) ~/Code/pdf-compress git:[main]
pandoc ./data/original/cv.docx -o ./data/original/cv.md
(base) ~/Code/pdf-compress git:[main]
uv run python main.py
🎯 Image Optimize - Optimierter CV PDF Workflow
==================================================
📋 Workflow-Schritte:
1. Profilbild EINMAL zu Kreis zuschneiden
2. Kreis in BEIDE PDF-Varianten (Green + Orange) einfügen
3. BEIDE PDFs komprimieren

🎯 Optimierter CV-PDF-Workflow
==================================================
📁 Input Bild: /Users/robin/Code/pdf-compress/data/images/cv-image.jpg
📁 Input PDFs: cv.pdf, cv (1).pdf
📁 Output: /Users/robin/Code/pdf-compress/output

📸 Schritt 1: Profilbild zu Kreis zuschneiden...
✅ Kreisbild erstellt: /Users/robin/Code/pdf-compress/output/01-crop-circle-output.png
✅ Kreis erstellt: 01-crop-circle-output.png

📄 Schritt 2: Kreis in beide PDFs einfügen...
✅ Bild in PDF eingefügt: /Users/robin/Code/pdf-compress/output/02-cv-with-image.pdf
✅ Green PDF erstellt: 02-cv-with-image.pdf
✅ Bild in PDF eingefügt: /Users/robin/Code/pdf-compress/output/02-cv (1)-with-image.pdf
✅ Orange PDF erstellt: 02-cv (1)-with-image.pdf

🗜️ Schritt 3: PDFs komprimieren...
✅ PDF komprimiert: /Users/robin/Code/pdf-compress/output/cv-robin-walter-scherler-gr.pdf
✅ Green: 23.96 MB → 1.92 MB (92.0% kleiner)
✅ PDF komprimiert: /Users/robin/Code/pdf-compress/output/cv-robin-walter-scherler-or.pdf
✅ Orange: 23.96 MB → 1.92 MB (92.0% kleiner)

🎉 Workflow erfolgreich abgeschlossen!
📁 Finale Dateien:
- cv-robin-walter-scherler-gr.pdf
- cv-robin-walter-scherler-or.pdf

🎉 Alle CV-Varianten erfolgreich erstellt!
%  