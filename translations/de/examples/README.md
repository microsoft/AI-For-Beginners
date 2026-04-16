# Anfängerfreundliche KI-Beispiele

Willkommen! Dieses Verzeichnis enthält einfache, eigenständige Beispiele, die Ihnen den Einstieg in KI und maschinelles Lernen erleichtern sollen. Jedes Beispiel ist anfängerfreundlich gestaltet und enthält ausführliche Kommentare sowie Schritt-für-Schritt-Erklärungen.

## 📚 Überblick über die Beispiele

| Beispiel | Beschreibung | Schwierigkeitsgrad | Voraussetzungen |
|----------|--------------|--------------------|-----------------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | Ihr erstes KI-Programm – einfache Mustererkennung | ⭐ Anfänger | Grundkenntnisse in Python |
| [Einfaches Neuronales Netzwerk](../../../examples/02-simple-neural-network.py) | Erstellen Sie ein neuronales Netzwerk von Grund auf | ⭐⭐ Anfänger+ | Python, grundlegende Mathematik |
| [Bildklassifikator](./03-image-classifier.ipynb) | Klassifizieren Sie Bilder mit einem vortrainierten Modell | ⭐⭐ Anfänger+ | Python, numpy |
| [Textstimmung](../../../examples/04-text-sentiment.py) | Analysieren Sie die Stimmung von Texten (positiv/negativ) | ⭐⭐ Anfänger+ | Python |

## 🚀 Erste Schritte

### Voraussetzungen

Stellen Sie sicher, dass Python installiert ist (empfohlen wird Version 3.8 oder höher). Installieren Sie die benötigten Pakete:

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

Oder verwenden Sie die Conda-Umgebung aus dem Hauptcurriculum:

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### Ausführen der Beispiele

**Für Python-Skripte (.py-Dateien):**
```bash
python 01-hello-ai-world.py
```

**Für Jupyter-Notebooks (.ipynb-Dateien):**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 Lernpfad

Wir empfehlen, die Beispiele in der folgenden Reihenfolge zu bearbeiten:

1. **Beginnen Sie mit "Hello AI World"** – Lernen Sie die Grundlagen der Mustererkennung
2. **Erstellen Sie ein einfaches neuronales Netzwerk** – Verstehen Sie, wie neuronale Netzwerke funktionieren
3. **Probieren Sie den Bildklassifikator aus** – Erleben Sie KI in Aktion mit echten Bildern
4. **Analysieren Sie die Textstimmung** – Erkunden Sie die Verarbeitung natürlicher Sprache

## 💡 Tipps für Anfänger

- **Lesen Sie die Kommentare im Code sorgfältig** – Sie erklären, was jede Zeile macht
- **Experimentieren Sie!** – Ändern Sie Werte und sehen Sie, was passiert
- **Machen Sie sich keine Sorgen, alles sofort zu verstehen** – Lernen braucht Zeit
- **Stellen Sie Fragen** – Nutzen Sie das [Diskussionsforum](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 Nächste Schritte

Nachdem Sie diese Beispiele abgeschlossen haben, erkunden Sie das vollständige Curriculum:
- [Einführung in KI](../lessons/1-Intro/README.md)
- [Neuronale Netzwerke](../lessons/3-NeuralNetworks/README.md)
- [Computer Vision](../lessons/4-ComputerVision/README.md)
- [Verarbeitung natürlicher Sprache](../lessons/5-NLP/README.md)

## 🤝 Mitwirken

Fanden Sie diese Beispiele hilfreich? Helfen Sie uns, sie zu verbessern:
- Melden Sie Probleme oder schlagen Sie Verbesserungen vor
- Fügen Sie weitere Beispiele für Anfänger hinzu
- Verbessern Sie die Dokumentation und Kommentare

---

*Denken Sie daran: Jeder Experte war einmal ein Anfänger. Viel Spaß beim Lernen! 🎓*

---

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.