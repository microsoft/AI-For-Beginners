# Klassifikation von Haustiergesichtern

Laboraufgabe aus dem [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Aufgabe

Stellen Sie sich vor, Sie müssen eine Anwendung für eine Tieraufzucht entwickeln, um alle Haustiere zu katalogisieren. Eine der großartigen Funktionen einer solchen Anwendung wäre die automatische Erkennung der Rasse anhand eines Fotos. Dies kann erfolgreich mit neuronalen Netzwerken durchgeführt werden.

Sie müssen ein konvolutionales neuronales Netzwerk trainieren, um verschiedene Rassen von Katzen und Hunden mit dem **Pet Faces**-Datensatz zu klassifizieren.

## Der Datensatz

Wir werden den **Pet Faces**-Datensatz verwenden, der aus dem [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) Haustierdatensatz stammt. Er enthält 35 verschiedene Rassen von Hunden und Katzen.

![Datensatz, mit dem wir arbeiten werden](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.de.png)

Um den Datensatz herunterzuladen, verwenden Sie diesen Code-Schnipsel:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## Notebook starten

Beginnen Sie das Labor, indem Sie [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb) öffnen.

## Fazit

Sie haben ein relativ komplexes Problem der Bildklassifikation von Grund auf gelöst! Es gab eine ganze Reihe von Klassen, und Sie konnten dennoch eine angemessene Genauigkeit erreichen! Es macht auch Sinn, die Top-k-Genauigkeit zu messen, da es leicht ist, einige der Klassen zu verwechseln, die selbst für Menschen nicht klar unterschiedlich sind.

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, sollten Sie sich bewusst sein, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.