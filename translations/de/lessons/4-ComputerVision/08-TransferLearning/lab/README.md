# Klassifizierung von Oxford-Haustieren mit Transferlernen

Laboraufgabe aus dem [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Aufgabe

Stellen Sie sich vor, Sie müssen eine Anwendung für eine Tieraufzucht entwickeln, um alle Haustiere zu katalogisieren. Eine der großartigen Funktionen einer solchen Anwendung wäre die automatische Erkennung der Rasse anhand eines Fotos. In dieser Aufgabe werden wir Transferlernen nutzen, um echte Haustierbilder aus dem [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) Haustier-Datensatz zu klassifizieren.

## Der Datensatz

Wir verwenden den originalen [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) Haustier-Datensatz, der 35 verschiedene Rassen von Hunden und Katzen enthält.

Um den Datensatz herunterzuladen, verwenden Sie diesen Code-Schnipsel:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Notebook starten

Beginnen Sie das Labor, indem Sie [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb) öffnen.

## Fazit

Transferlernen und vortrainierte Netzwerke ermöglichen es uns, reale Bildklassifizierungsprobleme relativ einfach zu lösen. Allerdings funktionieren vortrainierte Netzwerke gut bei Bildern ähnlicher Art, und wenn wir beginnen, sehr unterschiedliche Bilder (z. B. medizinische Bilder) zu klassifizieren, werden wir wahrscheinlich viel schlechtere Ergebnisse erzielen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Verantwortung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.