# Development Guidelines

## Dokumentationsstruktur

### Hierarchie
```
context/
├── prompting/           # KI-Interaktionshistorie
├── visual-examples/     # Screenshots und Workflow-Dokumentation
└── testing/            # Experimentelle Dokumentation
```

### Inhaltsrichtlinien
- Jede Markdown-Datei beginnt mit einem aussagekräftigen H1-Header
- Verwendung von klaren, strukturierten Überschriften
- Code-Beispiele in entsprechenden Fenced Code Blocks
- Konsistente Verwendung von Bullet Points und Nummerierungen

## Git-Workflow

### Commit-Nachrichten
- Verwende das Format: `type(scope): description`
- Beispiele: `docs(readme): add navigation links`, `feat(compress): implement pdf optimization`

### Branch-Naming
- Verwende kebab-case für Branch-Namen
- Beispiele: `feature/pdf-compression`, `fix/image-positioning`

## Code-Qualität

### Python-Spezifisch
- Verwende aussagekräftige Funktions- und Variablennamen
- Dokumentiere komplexe Algorithmen mit Inline-Kommentaren
- Halte Funktionen fokussiert und testbar

## KI-Zusammenarbeit

### Prompt-Engineering

**Dokumentation:**
- Alle KI-Interaktionen in `context/prompting/` dokumentieren
- Verwende kebab-case für Dateinamen
- Strukturiere Conversations chronologisch

**Best Practices:**
- Klare, spezifische Anfragen stellen
- Kontext und Ziele explizit kommunizieren
- Iterative Verbesserung dokumentieren

### Tool-Integration

**Claude Code:**
- Verwende CLAUDE.md für projektspezifische Anweisungen
- Dokumentiere wichtige Workflows und Kommandos
- Nutze strukturierte Prompt-Strategien

## Qualitätssicherung

### Review-Prozess

**Vor Commit:**
- Überprüfe Dateinamen-Konventionen
- Stelle sicher, dass Dokumentation aktuell ist
- Teste funktionale Änderungen

**Dokumentations-Reviews:**
- Prüfe auf Konsistenz mit etablierten Standards
- Validiere Links und Verweise
- Überprüfe Rechtschreibung und Grammatik

### Kontinuierliche Verbesserung

**Feedback-Integration:**
- Dokumentiere Learnings aus Problemen
- Aktualisiere Standards basierend auf Erfahrungen
- Teile bewährte Praktiken im Team

### Performance

**Optimierung:**
- Implementiere effiziente Algorithmen
- Dokumentiere Performance-kritische Bereiche
- Teste mit realistischen Datenmengen