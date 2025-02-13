# Vorgefertigte Netzwerke und Transferlernen

Das Training von CNNs kann viel Zeit in Anspruch nehmen, und es wird eine große Menge an Daten benötigt. Ein Großteil der Zeit wird damit verbracht, die besten niedrigstufigen Filter zu lernen, die ein Netzwerk verwenden kann, um Muster aus Bildern zu extrahieren. Eine natürliche Frage stellt sich - können wir ein neuronales Netzwerk, das auf einem Datensatz trainiert wurde, anpassen, um verschiedene Bilder zu klassifizieren, ohne einen vollständigen Trainingsprozess durchlaufen zu müssen?

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/108)

Dieser Ansatz wird als **Transferlernen** bezeichnet, da wir Wissen von einem neuronalen Netzwerkmodell auf ein anderes übertragen. Beim Transferlernen beginnen wir typischerweise mit einem vortrainierten Modell, das auf einem großen Bilddatensatz wie **ImageNet** trainiert wurde. Diese Modelle können bereits gut darin sein, verschiedene Merkmale aus allgemeinen Bildern zu extrahieren, und in vielen Fällen kann der Aufbau eines Klassifikators auf Basis dieser extrahierten Merkmale zu guten Ergebnissen führen.

> ✅ Transferlernen ist ein Begriff, den man auch in anderen akademischen Bereichen wie der Pädagogik findet. Es bezieht sich auf den Prozess, Wissen aus einem Bereich zu nehmen und es auf einen anderen anzuwenden.

## Vorgefertigte Modelle als Merkmalsextraktoren

Die konvolutionalen Netzwerke, über die wir im vorherigen Abschnitt gesprochen haben, enthalten eine Reihe von Schichten, von denen jede einige Merkmale aus dem Bild extrahieren soll, beginnend mit niedrigstufigen Pixelkombinationen (wie horizontalen/vertikalen Linien oder Strichen) bis hin zu höherstufigen Kombinationen von Merkmalen, die Dingen wie einem Auge einer Flamme entsprechen. Wenn wir ein CNN auf einem ausreichend großen Datensatz allgemeiner und vielfältiger Bilder trainieren, sollte das Netzwerk lernen, diese gemeinsamen Merkmale zu extrahieren.

Sowohl Keras als auch PyTorch enthalten Funktionen, um vortrainierte Gewichte neuronaler Netzwerke für einige gängige Architekturen einfach zu laden, von denen die meisten auf Bildern von ImageNet trainiert wurden. Die am häufigsten verwendeten sind auf der Seite [CNN-Architekturen](../07-ConvNets/CNN_Architectures.md) aus der vorherigen Lektion beschrieben. Insbesondere möchten Sie möglicherweise eines der folgenden Modelle in Betracht ziehen:

* **VGG-16/VGG-19**, die relativ einfache Modelle sind, die dennoch eine gute Genauigkeit bieten. Oft ist die Verwendung von VGG als ersten Versuch eine gute Wahl, um zu sehen, wie das Transferlernen funktioniert.
* **ResNet** ist eine Familie von Modellen, die 2015 von Microsoft Research vorgeschlagen wurde. Sie haben mehr Schichten und benötigen daher mehr Ressourcen.
* **MobileNet** ist eine Familie von Modellen mit reduzierter Größe, die für mobile Geräte geeignet sind. Verwenden Sie sie, wenn Sie wenig Ressourcen haben und bereit sind, ein wenig Genauigkeit zu opfern.

Hier sind Beispiele für Merkmale, die von einem Bild einer Katze durch das VGG-16-Netzwerk extrahiert wurden:

![Merkmale, die von VGG-16 extrahiert wurden](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.de.png)

## Katzen- und Hundedatensatz

In diesem Beispiel verwenden wir einen Datensatz von [Katzen und Hunden](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), der sehr nah an einem realen Bildklassifizierungsszenario ist.

## ✍️ Übung: Transferlernen

Lassen Sie uns das Transferlernen in den entsprechenden Notebooks in Aktion sehen:

* [Transferlernen - PyTorch](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb)
* [Transferlernen - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb)

## Visualisierung des adversarialen Katers

Das vortrainierte neuronale Netzwerk enthält verschiedene Muster in seinem *Gehirn*, einschließlich Vorstellungen von **idealen Katzen** (sowie idealen Hunden, idealen Zebras usw.). Es wäre interessant, dieses Bild irgendwie **zu visualisieren**. Allerdings ist das nicht einfach, da die Muster über die Netzwerkgewichte verteilt und auch in einer hierarchischen Struktur organisiert sind.

Ein Ansatz, den wir verfolgen können, besteht darin, mit einem zufälligen Bild zu beginnen und dann die Technik der **Gradientenabstieg-Optimierung** zu verwenden, um dieses Bild so anzupassen, dass das Netzwerk anfängt zu denken, es sei eine Katze.

![Bildoptimierungsschleife](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.de.png)

Wenn wir dies jedoch tun, erhalten wir etwas, das sehr ähnlich wie Rauschen aussieht. Das liegt daran, dass *es viele Möglichkeiten gibt, das Netzwerk glauben zu lassen, dass das Eingabebild eine Katze ist*, einschließlich einiger, die visuell keinen Sinn ergeben. Während diese Bilder viele Muster enthalten, die typisch für eine Katze sind, gibt es nichts, was sie visuell unterscheidbar macht.

Um das Ergebnis zu verbessern, können wir einen weiteren Begriff in die Verlustfunktion einfügen, der als **Variationsverlust** bezeichnet wird. Es handelt sich um eine Metrik, die zeigt, wie ähnlich benachbarte Pixel des Bildes sind. Die Minimierung des Variationsverlusts macht das Bild glatter und beseitigt Rauschen – wodurch ansprechendere Muster sichtbar werden. Hier ist ein Beispiel für solche "idealen" Bilder, die mit hoher Wahrscheinlichkeit als Katze und als Zebra klassifiziert werden:

![Ideale Katze](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.de.png) | ![Ideales Zebra](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.de.png)
-----|-----
 *Ideale Katze* | *Ideales Zebra*

Ein ähnlicher Ansatz kann verwendet werden, um sogenannte **adversariale Angriffe** auf ein neuronales Netzwerk durchzuführen. Angenommen, wir möchten ein neuronales Netzwerk täuschen und einen Hund wie eine Katze aussehen lassen. Wenn wir ein Bild eines Hundes nehmen, das von einem Netzwerk als Hund erkannt wird, können wir es dann ein wenig anpassen, indem wir die Gradientenabstieg-Optimierung verwenden, bis das Netzwerk beginnt, es als Katze zu klassifizieren:

![Bild eines Hundes](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.de.png) | ![Bild eines Hundes, der als Katze klassifiziert wird](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.de.png)
-----|-----
*Ursprüngliches Bild eines Hundes* | *Bild eines Hundes, der als Katze klassifiziert wird*

Siehe den Code, um die oben genannten Ergebnisse im folgenden Notebook zu reproduzieren:

* [Ideale und adversariale Katze - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb)
## Fazit

Mit Transferlernen können Sie schnell einen Klassifikator für eine benutzerdefinierte Objektklassifizierungsaufgabe zusammenstellen und eine hohe Genauigkeit erreichen. Sie können sehen, dass komplexere Aufgaben, die wir jetzt lösen, mehr Rechenleistung erfordern und nicht einfach auf der CPU gelöst werden können. In der nächsten Einheit werden wir versuchen, eine leichtere Implementierung zu verwenden, um dasselbe Modell mit geringeren Rechenressourcen zu trainieren, was zu einer nur geringfügig niedrigeren Genauigkeit führt.

## 🚀 Herausforderung

In den begleitenden Notebooks gibt es Hinweise am Ende, wie der Wissenstransfer am besten mit einigermaßen ähnlichen Trainingsdaten funktioniert (vielleicht eine neue Tierart). Experimentieren Sie mit völlig neuen Bildtypen, um zu sehen, wie gut oder schlecht Ihre Modelle für den Wissenstransfer abschneiden.

## [Nachlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Überprüfung & Selbststudium

Lesen Sie [TrainingTricks.md](TrainingTricks.md) durch, um Ihr Wissen über einige andere Möglichkeiten zu vertiefen, wie Sie Ihre Modelle trainieren können.

## [Aufgabe](lab/README.md)

In diesem Labor werden wir den realen [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) Haustierdatensatz mit 35 Rassen von Katzen und Hunden verwenden und einen Klassifikator für das Transferlernen erstellen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, bitten wir zu beachten, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.