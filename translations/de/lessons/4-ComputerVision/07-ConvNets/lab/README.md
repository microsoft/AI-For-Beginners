<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-24T09:36:20+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "de"
}
-->
# Klassifikation von Haustiergesichtern

Laboraufgabe aus dem [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Aufgabe

Stellen Sie sich vor, Sie müssen eine Anwendung für eine Tierpension entwickeln, um alle Haustiere zu katalogisieren. Eine großartige Funktion einer solchen Anwendung wäre, die Rasse automatisch anhand eines Fotos zu erkennen. Dies kann erfolgreich mit neuronalen Netzwerken durchgeführt werden.

Sie müssen ein konvolutionales neuronales Netzwerk trainieren, um verschiedene Katzen- und Hunderassen mithilfe des **Pet Faces**-Datensatzes zu klassifizieren.

## Der Datensatz

Wir verwenden den **Pet Faces**-Datensatz, der aus dem [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) Haustierdatensatz abgeleitet wurde. Er enthält 35 verschiedene Rassen von Hunden und Katzen.

![Datensatz, mit dem wir arbeiten werden](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/images/data.png)

Um den Datensatz herunterzuladen, verwenden Sie diesen Code-Schnipsel:

```python
!wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Start-Notebook

Beginnen Sie das Labor, indem Sie [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb) öffnen.

## Fazit

Sie haben ein relativ komplexes Problem der Bildklassifikation von Grund auf gelöst! Es gab eine ganze Menge Klassen, und Sie konnten trotzdem eine vernünftige Genauigkeit erreichen! Es ist auch sinnvoll, die Top-k-Genauigkeit zu messen, da es leicht ist, einige Klassen zu verwechseln, die selbst für Menschen nicht eindeutig unterschiedlich sind.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.