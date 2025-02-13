# Bekannte CNN-Architekturen

### VGG-16

VGG-16 ist ein Netzwerk, das 2014 eine Genauigkeit von 92,7 % bei der Top-5-Klassifizierung von ImageNet erreicht hat. Es hat die folgende Schichtstruktur:

![ImageNet Layers](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.de.jpg)

Wie Sie sehen können, folgt VGG einer traditionellen Pyramidenarchitektur, die aus einer Sequenz von Faltungs-Pooling-Schichten besteht.

![ImageNet Pyramid](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.de.jpg)

> Bild von [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet ist eine Familie von Modellen, die 2015 von Microsoft Research vorgeschlagen wurde. Die Hauptidee von ResNet besteht darin, **Residualblöcke** zu verwenden:

<img src="images/resnet-block.png" width="300"/>

> Bild aus [diesem Papier](https://arxiv.org/pdf/1512.03385.pdf)

Der Grund für die Verwendung von Identitätsdurchgängen besteht darin, dass unsere Schicht **die Differenz** zwischen dem Ergebnis einer vorherigen Schicht und der Ausgabe des Residualblocks vorhersagen soll - daher der Name *residual*. Diese Blöcke sind viel einfacher zu trainieren, und man kann Netzwerke mit mehreren Hundert dieser Blöcke konstruieren (die gebräuchlichsten Varianten sind ResNet-52, ResNet-101 und ResNet-152).

Man kann sich dieses Netzwerk auch so vorstellen, dass es seine Komplexität an den Datensatz anpassen kann. Zu Beginn, wenn Sie das Netzwerk zu trainieren beginnen, sind die Gewichtswerte klein, und das meiste Signal geht durch die Identitätsschichten. Mit dem Fortschreiten des Trainings und zunehmenden Gewichtswerten wächst die Bedeutung der Netzwerkparameter, und das Netzwerk passt sich an, um die erforderliche Ausdruckskraft zu gewährleisten, um die Trainingsbilder korrekt zu klassifizieren.

### Google Inception

Die Google Inception-Architektur geht einen Schritt weiter und baut jede Netzwerkschicht als Kombination aus mehreren verschiedenen Pfaden auf:

<img src="images/inception.png" width="400"/>

> Bild von [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Hier müssen wir die Rolle von 1x1-Faltungen betonen, da sie zunächst keinen Sinn zu ergeben scheinen. Warum sollten wir mit einem 1x1-Filter über das Bild fahren? Sie müssen jedoch daran denken, dass Faltungfilter auch mit mehreren Tiefenkanälen arbeiten (ursprünglich - RGB-Farben, in nachfolgenden Schichten - Kanäle für verschiedene Filter), und die 1x1-Faltung wird verwendet, um diese Eingangskanäle mithilfe unterschiedlicher trainierbarer Gewichte zu mischen. Es kann auch als Herunterrechnen (Pooling) über die Kanaldimension betrachtet werden.

Hier ist [ein guter Blogbeitrag](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) zu diesem Thema sowie [das ursprüngliche Papier](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

MobileNet ist eine Familie von Modellen mit reduzierter Größe, die für mobile Geräte geeignet sind. Verwenden Sie sie, wenn Ihnen die Ressourcen ausgehen und Sie ein wenig Genauigkeit opfern können. Die Hauptidee dahinter ist die sogenannte **depthwise separable convolution**, die es ermöglicht, Faltungfilter als Kombination aus räumlichen Faltungen und 1x1-Faltungen über Tiefenkanäle darzustellen. Dies reduziert erheblich die Anzahl der Parameter, wodurch das Netzwerk kleiner wird und auch einfacher mit weniger Daten trainiert werden kann.

Hier ist [ein guter Blogbeitrag über MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Fazit

In dieser Einheit haben Sie das Hauptkonzept hinter neuronalen Netzwerken für Computer Vision - den Faltungsnetzwerken - kennengelernt. Echte Architekturen, die Bildklassifizierung, Objekterkennung und sogar Bildgenerierungsnetzwerke antreiben, basieren alle auf CNNs, nur mit mehr Schichten und einigen zusätzlichen Trainingstricks.

## 🚀 Herausforderung

In den begleitenden Notizbüchern finden Sie am Ende Hinweise, wie Sie eine höhere Genauigkeit erzielen können. Machen Sie einige Experimente, um zu sehen, ob Sie eine höhere Genauigkeit erreichen können.

## [Quiz nach der Vorlesung](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/207)

## Überprüfung & Selbststudium

Während CNNs am häufigsten für Aufgaben der Computer Vision verwendet werden, sind sie im Allgemeinen gut geeignet, um Muster fester Größe zu extrahieren. Wenn wir beispielsweise mit Klängen arbeiten, möchten wir möglicherweise auch CNNs verwenden, um nach bestimmten Mustern im Audiosignal zu suchen - in diesem Fall wären die Filter eindimensional (und dieses CNN würde als 1D-CNN bezeichnet). Manchmal wird auch ein 3D-CNN verwendet, um Merkmale im mehrdimensionalen Raum zu extrahieren, wie etwa bestimmte Ereignisse, die in einem Video auftreten - CNNs können bestimmte Muster der Merkmalsänderung über die Zeit erfassen. Machen Sie einige Überprüfungen und Selbststudien zu anderen Aufgaben, die mit CNNs durchgeführt werden können.

## [Aufgabe](lab/README.md)

In diesem Labor sind Sie damit beauftragt, verschiedene Katzen- und Hunderassen zu klassifizieren. Diese Bilder sind komplexer als der MNIST-Datensatz und haben höhere Dimensionen, und es gibt mehr als 10 Klassen.

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.