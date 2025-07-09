from src.main_workflow import process_cv_workflow

def main():
    print("🎯 Image Optimize - Optimierter CV PDF Workflow")
    print("="*50)
    print("📋 Workflow-Schritte:")
    print("   1. Profilbild EINMAL zu Kreis zuschneiden")  
    print("   2. Kreis in BEIDE PDF-Varianten (Green + Orange) einfügen")
    print("   3. BEIDE PDFs komprimieren")
    print()
    
    success = process_cv_workflow()
    
    if success:
        print("\n🎉 Alle CV-Varianten erfolgreich erstellt!")
    else:
        print("\n❌ Workflow fehlgeschlagen!")
        exit(1)

if __name__ == "__main__":
    main()
