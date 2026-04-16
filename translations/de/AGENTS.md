# AGENTS.md

## Projektübersicht

AI for Beginners ist ein umfassender 12-wöchiger Lehrplan mit 24 Lektionen, der die Grundlagen der Künstlichen Intelligenz abdeckt. Dieses Bildungs-Repository enthält praktische Lektionen mit Jupyter Notebooks, Quizfragen und interaktiven Übungen. Der Lehrplan umfasst:

- Symbolische KI mit Wissensrepräsentation und Expertensystemen
- Neuronale Netze und Deep Learning mit TensorFlow und PyTorch
- Techniken und Architekturen der Computer Vision
- Verarbeitung natürlicher Sprache (NLP), einschließlich Transformer und BERT
- Spezialisierte Themen: Genetische Algorithmen, Verstärkendes Lernen, Multi-Agenten-Systeme
- KI-Ethik und Prinzipien verantwortungsvoller KI

**Wichtige Technologien:** Python 3, Jupyter Notebooks, TensorFlow, PyTorch, Keras, OpenCV, Vue.js (für die Quiz-App)

**Architektur:** Bildungsinhalts-Repository mit Jupyter Notebooks, organisiert nach Themenbereichen, ergänzt durch eine Vue.js-basierte Quiz-Anwendung und umfangreiche mehrsprachige Unterstützung.

## Setup-Befehle

### Primäre Entwicklungsumgebung (Python/Jupyter)

Der Lehrplan ist für die Ausführung mit Python und Jupyter Notebooks konzipiert. Die empfohlene Methode ist die Verwendung von Miniconda:

```bash
# Clone the repository
git clone https://github.com/microsoft/ai-for-beginners
cd ai-for-beginners

# Create and activate conda environment
conda env create --name ai4beg --file environment.yml
conda activate ai4beg

# Start Jupyter Notebook
jupyter notebook
# OR
jupyter lab
```

### Alternative: Verwendung von devcontainer

```bash
# Open in VS Code and select "Reopen in Container" when prompted
# The devcontainer will automatically set up the environment
```

### Einrichtung der Quiz-Anwendung

Die Quiz-App ist eine separate Vue.js-Anwendung, die sich unter `etc/quiz-app/` befindet:

```bash
cd etc/quiz-app
npm install
npm run serve  # Development server
npm run build  # Production build
npm run lint   # Lint and fix files
```

## Entwicklungsworkflow

### Arbeiten mit Jupyter Notebooks

1. **Lokale Entwicklung:**
   - Conda-Umgebung aktivieren: `conda activate ai4beg`
   - Jupyter starten: `jupyter notebook` oder `jupyter lab`
   - Zu den Lektionen-Ordnern navigieren und `.ipynb`-Dateien öffnen
   - Zellen interaktiv ausführen, um den Lektionen zu folgen

2. **VS Code mit Python-Erweiterung:**
   - Repository in VS Code öffnen
   - Python-Erweiterung installieren
   - VS Code erkennt und verwendet automatisch die Conda-Umgebung
   - `.ipynb`-Dateien direkt in VS Code öffnen

3. **Cloud-Entwicklung:**
   - **GitHub Codespaces:** Klicken Sie auf "Code" → "Codespaces" → "Codespace auf main erstellen"
   - **Binder:** Verwenden Sie das Binder-Badge in der README, um im Browser zu starten
   - Hinweis: Binder hat begrenzte Ressourcen und einige Einschränkungen beim Webzugriff

### GPU-Unterstützung für fortgeschrittene Lektionen

Spätere Lektionen profitieren erheblich von GPU-Beschleunigung:

- **Azure Data Science VM:** Verwenden Sie NC-Serie VMs mit GPU-Unterstützung
- **Azure Machine Learning:** Nutzen Sie Notebook-Funktionen mit GPU-Computing
- **Google Colab:** Laden Sie Notebooks einzeln hoch (kostenlose GPU-Unterstützung verfügbar)

### Entwicklung der Quiz-App

```bash
cd etc/quiz-app
npm run serve  # Hot-reload development server at http://localhost:8080
```

## Testanweisungen

Dieses Repository ist auf Lerninhalte ausgerichtet und nicht auf Softwaretests. Es gibt keine traditionelle Test-Suite.

### Validierungsansätze:

1. **Jupyter Notebooks:** Zellen nacheinander ausführen, um sicherzustellen, dass die Codebeispiele funktionieren
2. **Quiz-App-Tests:** Manuelles Testen über den Entwicklungsserver
3. **Validierung der Übersetzungen:** Überprüfen Sie die übersetzten Inhalte im Ordner `translations/`
4. **Linting der Quiz-App:** `npm run lint` in `etc/quiz-app/` ausführen

### Ausführung von Codebeispielen:

```bash
# Activate environment first
conda activate ai4beg

# Run Python scripts directly
python lessons/4-ComputerVision/07-ConvNets/pytorchcv.py

# Or execute notebooks
jupyter notebook lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb
```

## Code-Stil

### Python-Code-Stil

- Standard-Python-Konventionen für Bildungs-Code
- Klarer, lesbarer Code, der Lernen über Optimierung priorisiert
- Kommentare, die wichtige Konzepte erklären
- Jupyter Notebook-freundlich: Zellen sollten möglichst eigenständig sein
- Keine strengen Linting-Anforderungen für Lehrinhalte

### JavaScript/Vue.js (Quiz-App)

- ESLint-Konfiguration in `etc/quiz-app/package.json`
- `npm run lint` ausführen, um Probleme zu überprüfen und automatisch zu beheben
- Vue 2.x-Konventionen
- Komponentenbasierte Architektur

### Dateiorganisation

```
lessons/
  ├── 0-course-setup/          # Setup instructions
  ├── 1-Intro/                 # Introduction to AI
  ├── 2-Symbolic/              # Symbolic AI
  ├── 3-NeuralNetworks/        # Neural Networks basics
  ├── 4-ComputerVision/        # Computer Vision
  ├── 5-NLP/                   # Natural Language Processing
  ├── 6-Other/                 # Other AI techniques
  ├── 7-Ethics/                # AI Ethics
  └── X-Extras/                # Additional content

etc/
  ├── quiz-app/                # Vue.js quiz application
  └── quiz-src/                # Quiz source files

translations/                  # Multi-language translations
```

## Build und Deployment

### Jupyter-Inhalte

Kein Build-Prozess erforderlich - Jupyter Notebooks werden direkt ausgeführt.

### Quiz-Anwendung

```bash
cd etc/quiz-app

# Development
npm run serve

# Production build
npm run build  # Outputs to etc/quiz-app/dist/

# Deploy to Azure Static Web Apps
# Azure automatically creates GitHub Actions workflow
# See etc/quiz-app/README.md for detailed deployment instructions
```

### Dokumentationsseite

Das Repository verwendet Docsify für die Dokumentation:
- `index.html` dient als Einstiegspunkt
- Kein Build erforderlich - direkt über GitHub Pages bereitgestellt
- Zugriff unter: https://microsoft.github.io/AI-For-Beginners/

## Richtlinien für Beiträge

### Pull-Request-Prozess

1. **Titel-Format:** Klare, beschreibende Titel, die die Änderung erklären
2. **CLA-Anforderung:** Microsoft CLA muss unterzeichnet sein (automatische Überprüfung)
3. **Inhaltsrichtlinien:**
   - Bildungsfokus und anfängerfreundlichen Ansatz beibehalten
   - Alle Codebeispiele in Notebooks testen
   - Sicherstellen, dass Notebooks durchgehend ausführbar sind
   - Übersetzungen aktualisieren, wenn englische Inhalte geändert werden
4. **Änderungen an der Quiz-App:** `npm run lint` vor dem Commit ausführen

### Übersetzungsbeiträge

- Übersetzungen werden automatisiert über GitHub Actions mit co-op-translator durchgeführt
- Manuelle Übersetzungen werden in `translations/<language-code>/` abgelegt
- Quiz-Übersetzungen in `etc/quiz-app/src/assets/translations/`
- Unterstützte Sprachen: Über 40 Sprachen (siehe README für vollständige Liste)

### Aktive Beitragsbereiche

Siehe `etc/CONTRIBUTING.md` für aktuelle Bedürfnisse:
- Abschnitte zu Deep Reinforcement Learning
- Verbesserungen bei der Objekterkennung
- Beispiele für Named Entity Recognition
- Trainingsbeispiele für benutzerdefinierte Einbettungen

## Umgebungskonfiguration

### Erforderliche Abhängigkeiten

```bash
# Core Python packages (from requirements.txt)
tensorflow==2.17.0
torch (via conda)
torchvision (via conda)
keras==3.5.0
opencv (via conda)
scikit-learn
numpy==1.26
pandas==2.2.2
matplotlib==3.9
jupyter
```

### Umgebungsvariablen

Keine speziellen Umgebungsvariablen für die grundlegende Nutzung erforderlich.

Für Azure-Bereitstellungen (Quiz-App):
- `AZURE_STATIC_WEB_APPS_API_TOKEN` (automatisch von Azure gesetzt)

## Debugging und Fehlerbehebung

### Häufige Probleme

**Problem:** Erstellung der Conda-Umgebung schlägt fehl
- **Lösung:** Conda zuerst aktualisieren: `conda update conda -y`
- Ausreichend Speicherplatz sicherstellen (50GB empfohlen)

**Problem:** Jupyter-Kernel nicht gefunden
- **Lösung:** 
  ```bash
  conda activate ai4beg
  python -m ipykernel install --user --name ai4beg
  ```

**Problem:** GPU wird in Notebooks nicht erkannt
- **Lösung:** 
  - CUDA-Installation überprüfen: `nvidia-smi`
  - PyTorch-GPU überprüfen: `python -c "import torch; print(torch.cuda.is_available())"`
  - TensorFlow-GPU überprüfen: `python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"`

**Problem:** Quiz-App startet nicht
- **Lösung:**
  ```bash
  cd etc/quiz-app
  rm -rf node_modules package-lock.json
  npm install
  npm run serve
  ```

**Problem:** Binder läuft ab oder blockiert Downloads
- **Lösung:** Verwenden Sie GitHub Codespaces oder lokale Einrichtung für besseren Ressourcen-Zugriff

### Speicherprobleme

Einige Lektionen erfordern erheblichen RAM (8GB+ empfohlen):
- Verwenden Sie Cloud-VMs für ressourcenintensive Lektionen
- Schließen Sie andere Anwendungen, wenn Modelle trainiert werden
- Reduzieren Sie die Batch-Größen in Notebooks, wenn der Speicher knapp wird

## Zusätzliche Hinweise

### Für Kursleiter

- Siehe `lessons/0-course-setup/for-teachers.md` für Lehranweisungen
- Lektionen sind eigenständig und können in Reihenfolge oder einzeln unterrichtet werden
- Geschätzte Dauer: 12 Wochen mit 2 Lektionen pro Woche

### Cloud-Ressourcen

- **Azure for Students:** Kostenlose Credits für Studierende verfügbar
- **Microsoft Learn:** Ergänzende Lernpfade, die im gesamten Lehrplan verlinkt sind
- **Binder:** Kostenlos, aber mit begrenzten Ressourcen und einigen Netzwerkeinschränkungen

### Optionen zur Codeausführung

1. **Lokal (empfohlen):** Volle Kontrolle, beste Leistung, GPU-Unterstützung
2. **GitHub Codespaces:** Cloud-basiertes VS Code, gut für schnellen Zugriff
3. **Binder:** Browserbasiertes Jupyter, kostenlos, aber begrenzt
4. **Azure ML Notebooks:** Unternehmensoption mit GPU-Unterstützung
5. **Google Colab:** Notebooks einzeln hochladen, kostenloser GPU-Tarif verfügbar

### Arbeiten mit Notebooks

- Notebooks sind so konzipiert, dass sie Zelle für Zelle ausgeführt werden können, um zu lernen
- Viele Notebooks laden Datensätze beim ersten Ausführen herunter (kann Zeit in Anspruch nehmen)
- Einige Modelle erfordern GPU für angemessene Trainingszeiten
- Vorgefertigte Modelle werden verwendet, wo möglich, um den Rechenaufwand zu reduzieren

### Leistungsüberlegungen

- Spätere Lektionen zur Computer Vision (CNNs, GANs) profitieren von GPU
- NLP-Transformer-Lektionen können erheblichen RAM erfordern
- Training von Grund auf ist lehrreich, aber zeitaufwendig
- Beispiele für Transfer-Learning minimieren die Trainingszeit

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.