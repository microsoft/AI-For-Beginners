<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "717775c4050ccbffbe0c961ad8bf7bf7",
  "translation_date": "2025-08-24T09:36:56+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/README.md",
  "language_code": "de"
}
-->
# Vorgefertigte Netzwerke und Transfer-Learning

Das Training von CNNs kann viel Zeit in Anspruch nehmen, und es wird eine große Menge an Daten dafür benötigt. Allerdings wird ein Großteil der Zeit darauf verwendet, die besten Low-Level-Filter zu lernen, die ein Netzwerk nutzen kann, um Muster aus Bildern zu extrahieren. Eine natürliche Frage stellt sich: Können wir ein neuronales Netzwerk, das auf einem Datensatz trainiert wurde, verwenden und anpassen, um andere Bilder zu klassifizieren, ohne den gesamten Trainingsprozess erneut durchlaufen zu müssen?

## [Quiz vor der Vorlesung](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/108)

Dieser Ansatz wird als **Transfer-Learning** bezeichnet, da wir Wissen von einem neuronalen Netzwerkmodell auf ein anderes übertragen. Beim Transfer-Learning beginnen wir typischerweise mit einem vortrainierten Modell, das auf einem großen Bilddatensatz wie **ImageNet** trainiert wurde. Diese Modelle können bereits verschiedene Merkmale aus generischen Bildern gut extrahieren, und in vielen Fällen reicht es aus, einen Klassifikator auf diesen extrahierten Merkmalen aufzubauen, um gute Ergebnisse zu erzielen.

> ✅ Transfer-Learning ist ein Begriff, den man auch in anderen akademischen Bereichen wie der Pädagogik findet. Er bezieht sich auf den Prozess, Wissen aus einem Bereich zu nehmen und in einem anderen anzuwenden.

## Vorgefertigte Modelle als Merkmalsextraktoren

Die in der vorherigen Sektion besprochenen Convolutional Networks enthalten eine Reihe von Schichten, die jeweils Merkmale aus dem Bild extrahieren sollen, beginnend mit Low-Level-Pixelkombinationen (wie horizontalen/vertikalen Linien oder Strichen) bis hin zu höherwertigen Kombinationen von Merkmalen, die beispielsweise einem Auge oder einer Flamme entsprechen. Wenn wir ein CNN auf einem ausreichend großen Datensatz mit generischen und vielfältigen Bildern trainieren, sollte das Netzwerk lernen, diese allgemeinen Merkmale zu extrahieren.

Sowohl Keras als auch PyTorch enthalten Funktionen, um vortrainierte neuronale Netzwerkgewichte für einige gängige Architekturen einfach zu laden, von denen die meisten auf ImageNet-Bildern trainiert wurden. Die am häufigsten verwendeten Modelle sind auf der Seite [CNN-Architekturen](../07-ConvNets/CNN_Architectures.md) aus der vorherigen Lektion beschrieben. Insbesondere könnten Sie eines der folgenden Modelle in Betracht ziehen:

* **VGG-16/VGG-19**, relativ einfache Modelle, die dennoch gute Genauigkeit liefern. Oft ist es eine gute Wahl, VGG als ersten Versuch zu verwenden, um zu sehen, wie Transfer-Learning funktioniert.
* **ResNet**, eine Modellfamilie, die 2015 von Microsoft Research vorgeschlagen wurde. Sie haben mehr Schichten und benötigen daher mehr Ressourcen.
* **MobileNet**, eine Modellfamilie mit reduzierter Größe, geeignet für mobile Geräte. Verwenden Sie sie, wenn Sie wenig Ressourcen haben und ein wenig Genauigkeit opfern können.

Hier sind Beispielmerkmale, die von einem Bild einer Katze durch das VGG-16-Netzwerk extrahiert wurden:

![Merkmale extrahiert durch VGG-16](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/features.png)

## Datensatz: Katzen vs. Hunde

In diesem Beispiel verwenden wir einen Datensatz von [Katzen und Hunden](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), der einem realen Szenario der Bildklassifikation sehr nahe kommt.

## ✍️ Übung: Transfer-Learning

Lassen Sie uns Transfer-Learning in Aktion in den entsprechenden Notebooks sehen:

* [Transfer-Learning - PyTorch](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb)
* [Transfer-Learning - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb)

## Visualisierung einer adversarialen Katze

Ein vortrainiertes neuronales Netzwerk enthält verschiedene Muster in seinem *Gehirn*, einschließlich Vorstellungen von einer **idealen Katze** (sowie einem idealen Hund, idealen Zebra usw.). Es wäre interessant, dieses Bild irgendwie **zu visualisieren**. Allerdings ist das nicht einfach, da die Muster über die Netzwerkgewichte verteilt und in einer hierarchischen Struktur organisiert sind.

Ein Ansatz, den wir verfolgen können, ist, mit einem zufälligen Bild zu beginnen und dann die Technik der **Gradientenabstiegsoptimierung** zu verwenden, um dieses Bild so anzupassen, dass das Netzwerk denkt, es sei eine Katze.

![Bildoptimierungsschleife](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/ideal-cat-loop.png)

Wenn wir dies jedoch tun, erhalten wir etwas, das einem zufälligen Rauschen sehr ähnlich ist. Dies liegt daran, dass *es viele Möglichkeiten gibt, das Netzwerk glauben zu lassen, dass das Eingabebild eine Katze ist*, einschließlich einiger, die visuell keinen Sinn ergeben. Während diese Bilder viele Muster enthalten, die typisch für eine Katze sind, gibt es nichts, das sie visuell unterscheidbar macht.

Um das Ergebnis zu verbessern, können wir einen weiteren Term in die Verlustfunktion hinzufügen, der als **Variationsverlust** bezeichnet wird. Dies ist eine Metrik, die zeigt, wie ähnlich benachbarte Pixel des Bildes sind. Die Minimierung des Variationsverlusts macht das Bild glatter und beseitigt Rauschen – wodurch visuell ansprechendere Muster sichtbar werden. Hier ist ein Beispiel für solche "idealen" Bilder, die mit hoher Wahrscheinlichkeit als Katze und Zebra klassifiziert werden:

![Ideale Katze](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/ideal-cat.png) | ![Ideales Zebra](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/ideal-zebra.png)
-----|-----
 *Ideale Katze* | *Ideales Zebra*

Ein ähnlicher Ansatz kann verwendet werden, um sogenannte **adversariale Angriffe** auf ein neuronales Netzwerk durchzuführen. Angenommen, wir möchten ein neuronales Netzwerk täuschen und einen Hund wie eine Katze aussehen lassen. Wenn wir das Bild eines Hundes nehmen, das vom Netzwerk als Hund erkannt wird, können wir es ein wenig anpassen, indem wir die Gradientenabstiegsoptimierung verwenden, bis das Netzwerk es als Katze klassifiziert:

![Bild eines Hundes](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/original-dog.png) | ![Bild eines Hundes, der als Katze klassifiziert wird](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/adversarial-dog.png)
-----|-----
*Originalbild eines Hundes* | *Bild eines Hundes, der als Katze klassifiziert wird*

Sehen Sie sich den Code an, um die oben genannten Ergebnisse in folgendem Notebook zu reproduzieren:

* [Ideale und adversariale Katze - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb)

## Fazit

Mit Transfer-Learning können Sie schnell einen Klassifikator für eine benutzerdefinierte Objektklassifikationsaufgabe zusammenstellen und eine hohe Genauigkeit erzielen. Sie sehen, dass komplexere Aufgaben, die wir jetzt lösen, eine höhere Rechenleistung erfordern und nicht einfach auf der CPU gelöst werden können. Im nächsten Abschnitt werden wir versuchen, eine leichtere Implementierung zu verwenden, um dasselbe Modell mit geringeren Rechenressourcen zu trainieren, was zu einer nur geringfügig niedrigeren Genauigkeit führt.

## 🚀 Herausforderung

In den begleitenden Notebooks gibt es am Ende Hinweise darauf, dass Transfer-Wissen am besten mit einigermaßen ähnlichen Trainingsdaten funktioniert (zum Beispiel eine neue Tierart). Experimentieren Sie mit völlig neuen Bildtypen, um zu sehen, wie gut oder schlecht Ihre Transfer-Wissen-Modelle abschneiden.

## [Quiz nach der Vorlesung](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Überprüfung & Selbststudium

Lesen Sie [TrainingTricks.md](TrainingTricks.md), um Ihr Wissen über andere Möglichkeiten zur Modellschulung zu vertiefen.

## [Aufgabe](lab/README.md)

In diesem Lab verwenden wir den realen [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) Haustierdatensatz mit 35 Katzen- und Hunderassen und erstellen einen Transfer-Learning-Klassifikator.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.