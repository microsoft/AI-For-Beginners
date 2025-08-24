<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7336583e4630220c835335da640016db",
  "translation_date": "2025-08-24T09:41:10+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/lab/README.md",
  "language_code": "de"
}
-->
# Mehrklassenklassifikation mit Perzeptron

Laboraufgabe aus dem [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Aufgabe

Verwenden Sie den Code, den wir in dieser Lektion für die binäre Klassifikation von MNIST-Handschriftziffern entwickelt haben, um einen Mehrklassenklassifikator zu erstellen, der jede Ziffer erkennen kann. Berechnen Sie die Klassifikationsgenauigkeit für das Trainings- und Testdatenset und geben Sie die Verwirrungsmatrix aus.

## Hinweise

1. Erstellen Sie für jede Ziffer ein Datenset für einen binären Klassifikator von „diese Ziffer vs. alle anderen Ziffern“.
1. Trainieren Sie 10 verschiedene Perzeptrons für die binäre Klassifikation (jeweils eines für jede Ziffer).
1. Definieren Sie eine Funktion, die eine Eingabeziffer klassifiziert.

> **Hinweis**: Wenn wir die Gewichte aller 10 Perzeptrons in einer Matrix kombinieren, sollten wir in der Lage sein, alle 10 Perzeptrons durch eine einzige Matrixmultiplikation auf die Eingabeziffern anzuwenden. Die wahrscheinlichste Ziffer kann dann einfach durch die Anwendung der `argmax`-Operation auf die Ausgabe gefunden werden.

## Start-Notebook

Beginnen Sie das Labor, indem Sie [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb) öffnen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.