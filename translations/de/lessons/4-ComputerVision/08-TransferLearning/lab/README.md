# Klassifikation von Oxford-Haustieren mit Transfer-Learning

Laboraufgabe aus dem [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Aufgabe

Stellen Sie sich vor, Sie müssen eine Anwendung für eine Tierpension entwickeln, um alle Haustiere zu katalogisieren. Eine großartige Funktion einer solchen Anwendung wäre die automatische Erkennung der Rasse anhand eines Fotos. In dieser Aufgabe werden wir Transfer-Learning verwenden, um echte Bilder von Haustieren aus dem [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) Haustier-Datensatz zu klassifizieren.

## Der Datensatz

Wir verwenden den originalen [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) Haustier-Datensatz, der 35 verschiedene Rassen von Hunden und Katzen enthält.

Um den Datensatz herunterzuladen, verwenden Sie diesen Code-Schnipsel:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Start des Notebooks

Beginnen Sie das Labor, indem Sie [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb) öffnen.

## Erkenntnis

Transfer-Learning und vortrainierte Netzwerke ermöglichen es uns, reale Bildklassifikationsprobleme relativ einfach zu lösen. Allerdings funktionieren vortrainierte Netzwerke gut bei Bildern ähnlicher Art, und wenn wir anfangen, sehr unterschiedliche Bilder zu klassifizieren (z. B. medizinische Bilder), werden die Ergebnisse wahrscheinlich deutlich schlechter ausfallen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.