# Segmentierung des menschlichen Körpers

Laboraufgabe aus dem [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Aufgabe

In der Videoproduktion, beispielsweise bei Wettervorhersagen, müssen wir oft ein menschliches Bild aus der Kamera ausschneiden und es über anderes Filmmaterial legen. Dies wird typischerweise mit **Chroma-Key**-Techniken durchgeführt, bei denen eine Person vor einem einfarbigen Hintergrund gefilmt wird, der anschließend entfernt wird. In diesem Labor werden wir ein neuronales Netzwerk trainieren, um die Silhouette eines Menschen auszuschneiden.

## Der Datensatz

Wir verwenden den [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) von Kaggle. Laden Sie den Datensatz manuell von Kaggle herunter.

## Start-Notebook

Beginnen Sie das Labor, indem Sie [BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb) öffnen.

## Erkenntnis

Die Segmentierung des Körpers ist nur eine der gängigen Aufgaben, die wir mit Bildern von Menschen durchführen können. Weitere wichtige Aufgaben umfassen **Skelett-Erkennung** und **Pose-Erkennung**. Schauen Sie sich die [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)-Bibliothek an, um zu sehen, wie diese Aufgaben umgesetzt werden können.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.