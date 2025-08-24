<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f7b97b375358cb51a1e098df306bf73",
  "translation_date": "2025-08-24T09:36:02+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md",
  "language_code": "de"
}
-->
# Bekannte CNN-Architekturen

### VGG-16

VGG-16 ist ein Netzwerk, das 2014 eine Genauigkeit von 92,7 % bei der ImageNet-Top-5-Klassifikation erreichte. Es hat die folgende Schichtstruktur:

![ImageNet Layers](../../../../../lessons/4-ComputerVision/07-ConvNets/images/vgg-16-arch1.jpg)

Wie man sehen kann, folgt VGG einer traditionellen Pyramidenarchitektur, die aus einer Abfolge von Convolution-Pooling-Schichten besteht.

![ImageNet Pyramid](../../../../../lessons/4-ComputerVision/07-ConvNets/images/vgg-16-arch.jpg)

> Bild von [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet ist eine Modellfamilie, die 2015 von Microsoft Research vorgeschlagen wurde. Die Hauptidee von ResNet ist die Verwendung von **Residual Blocks**:

<img src="images/resnet-block.png" width="300"/>

> Bild aus [diesem Paper](https://arxiv.org/pdf/1512.03385.pdf)

Der Grund für die Verwendung von Identitätsdurchläufen ist, dass die Schicht **die Differenz** zwischen dem Ergebnis einer vorherigen Schicht und der Ausgabe des Residual Blocks vorhersagen soll – daher der Name *residual*. Diese Blöcke sind viel einfacher zu trainieren, und man kann Netzwerke mit mehreren Hundert solcher Blöcke konstruieren (die gängigsten Varianten sind ResNet-52, ResNet-101 und ResNet-152).

Man kann sich dieses Netzwerk auch so vorstellen, dass es seine Komplexität an den Datensatz anpassen kann. Zu Beginn des Trainings, wenn die Gewichtswerte klein sind, wird das meiste Signal durch die Identitätsdurchläufe weitergeleitet. Mit fortschreitendem Training und zunehmenden Gewichtswerten wächst die Bedeutung der Netzwerkparameter, und das Netzwerk passt sich an, um die erforderliche Ausdruckskraft zu erreichen, um die Trainingsbilder korrekt zu klassifizieren.

### Google Inception

Die Google-Inception-Architektur geht einen Schritt weiter und baut jede Netzwerkschicht als Kombination aus mehreren verschiedenen Pfaden auf:

<img src="images/inception.png" width="400"/>

> Bild von [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Hier muss die Rolle der 1x1-Convolutions hervorgehoben werden, da sie auf den ersten Blick keinen Sinn ergeben. Warum sollte man das Bild mit einem 1x1-Filter durchlaufen? Man muss jedoch bedenken, dass Convolution-Filter auch mit mehreren Tiefenkanälen arbeiten (ursprünglich RGB-Farben, in späteren Schichten Kanäle für verschiedene Filter), und 1x1-Convolutions werden verwendet, um diese Eingabekanäle mit unterschiedlichen trainierbaren Gewichten zu mischen. Es kann auch als Downsampling (Pooling) über die Kanaldimension betrachtet werden.

Hier ist [ein guter Blogbeitrag](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) zu diesem Thema und [das Originalpaper](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

MobileNet ist eine Modellfamilie mit reduzierter Größe, die für mobile Geräte geeignet ist. Verwenden Sie sie, wenn Sie nur begrenzte Ressourcen haben und ein wenig Genauigkeit opfern können. Die Hauptidee dahinter ist die sogenannte **Depthwise Separable Convolution**, die es ermöglicht, Convolution-Filter durch eine Kombination aus räumlichen Convolutions und 1x1-Convolutions über Tiefenkanäle darzustellen. Dies reduziert die Anzahl der Parameter erheblich, wodurch das Netzwerk kleiner wird und auch mit weniger Daten leichter trainiert werden kann.

Hier ist [ein guter Blogbeitrag zu MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Fazit

In dieser Einheit haben Sie das Hauptkonzept hinter neuronalen Netzwerken für Computer Vision gelernt – Convolutional Networks. Reale Architekturen, die Bildklassifikation, Objekterkennung und sogar Bildgenerierung ermöglichen, basieren alle auf CNNs, nur mit mehr Schichten und einigen zusätzlichen Trainingstricks.

## 🚀 Herausforderung

In den begleitenden Notebooks gibt es am Ende Hinweise darauf, wie man eine höhere Genauigkeit erzielen kann. Führen Sie einige Experimente durch, um zu sehen, ob Sie eine höhere Genauigkeit erreichen können.

## [Quiz nach der Vorlesung](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/207)

## Überprüfung & Selbststudium

Obwohl CNNs am häufigsten für Aufgaben im Bereich Computer Vision verwendet werden, eignen sie sich im Allgemeinen gut für die Extraktion von Mustern fester Größe. Wenn wir beispielsweise mit Tönen arbeiten, könnten wir CNNs verwenden, um nach bestimmten Mustern im Audiosignal zu suchen – in diesem Fall wären die Filter eindimensional (und dieses CNN würde als 1D-CNN bezeichnet). Manchmal wird auch ein 3D-CNN verwendet, um Merkmale in einem mehrdimensionalen Raum zu extrahieren, wie z. B. bestimmte Ereignisse, die in einem Video auftreten – CNN kann bestimmte Muster von Merkmalsänderungen im Laufe der Zeit erfassen. Machen Sie eine Überprüfung und ein Selbststudium zu anderen Aufgaben, die mit CNNs durchgeführt werden können.

## [Aufgabe](lab/README.md)

In diesem Labor sollen Sie verschiedene Katzen- und Hunderassen klassifizieren. Diese Bilder sind komplexer als der MNIST-Datensatz, haben höhere Dimensionen und es gibt mehr als 10 Klassen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.