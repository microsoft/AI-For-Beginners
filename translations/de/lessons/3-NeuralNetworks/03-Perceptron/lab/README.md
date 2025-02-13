# Mehrklassenklassifikation mit Perzeptron

Laboraufgabe aus dem [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Aufgabe

Verwenden Sie den Code, den wir in dieser Lektion für die binäre Klassifikation von handgeschriebenen MNIST-Ziffern entwickelt haben, um einen Mehrklassenklassifikator zu erstellen, der in der Lage ist, jede Ziffer zu erkennen. Berechnen Sie die Klassifikationsgenauigkeit auf dem Trainings- und Testdatensatz und drucken Sie die Verwirrungsmatrix aus.

## Hinweise

1. Erstellen Sie für jede Ziffer einen Datensatz für den binären Klassifikator "diese Ziffer vs. alle anderen Ziffern"
1. Trainieren Sie 10 verschiedene Perzeptrons für die binäre Klassifikation (eines für jede Ziffer)
1. Definieren Sie eine Funktion, die eine Eingabenziffer klassifiziert

> **Hinweis**: Wenn wir die Gewichte aller 10 Perzeptrons in eine Matrix kombinieren, sollten wir in der Lage sein, alle 10 Perzeptrons auf die Eingabenziffern durch eine Matrixmultiplikation anzuwenden. Die wahrscheinlichste Ziffer kann dann einfach durch die Anwendung der `argmax`-Operation auf die Ausgabe gefunden werden.

## Notizbuch starten

Starten Sie das Labor, indem Sie [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb) öffnen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, bitten wir zu beachten, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache sollte als die maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung resultieren.