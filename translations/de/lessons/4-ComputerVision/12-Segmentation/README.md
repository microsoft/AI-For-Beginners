# Segmentierung

Wir haben zuvor über Objekterkennung gelernt, die es uns ermöglicht, Objekte im Bild zu lokalisieren, indem wir ihre *Umrandungsrahmen* vorhersagen. Für einige Aufgaben benötigen wir jedoch nicht nur Umrandungsrahmen, sondern auch eine genauere Lokalisierung der Objekte. Diese Aufgabe wird als **Segmentierung** bezeichnet.

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

Segmentierung kann als **Pixelklassifikation** betrachtet werden, wobei für **jedes** Pixel des Bildes seine Klasse vorhergesagt werden muss (hintergrund ist eine der Klassen). Es gibt zwei Hauptalgorithmen für die Segmentierung:

* **Semantische Segmentierung** gibt nur die Pixelklasse an und unterscheidet nicht zwischen verschiedenen Objekten derselben Klasse.
* **Instanzsegmentierung** unterteilt Klassen in verschiedene Instanzen.

Bei der Instanzsegmentierung sind diese Schafe unterschiedliche Objekte, während bei der semantischen Segmentierung alle Schafe durch eine Klasse repräsentiert werden.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Bild aus [diesem Blogbeitrag](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Es gibt verschiedene neuronale Architekturen für die Segmentierung, aber sie haben alle die gleiche Struktur. In gewisser Weise ähnelt es dem Autoencoder, den Sie zuvor gelernt haben, aber anstatt das ursprüngliche Bild zu dekonstruierten, besteht unser Ziel darin, eine **Maske** zu dekodieren. Daher hat ein Segmentierungsnetzwerk die folgenden Teile:

* **Encoder** extrahiert Merkmale aus dem Eingangsbild.
* **Decoder** transformiert diese Merkmale in das **Maskenbild**, mit der gleichen Größe und Anzahl von Kanälen, die der Anzahl der Klassen entsprechen.

<img src="images/segm.png" width="80%">

> Bild aus [dieser Veröffentlichung](https://arxiv.org/pdf/2001.05566.pdf)

Besonders erwähnenswert ist die Verlustfunktion, die für die Segmentierung verwendet wird. Bei klassischen Autoencodern müssen wir die Ähnlichkeit zwischen zwei Bildern messen, und wir können dazu den mittleren quadratischen Fehler (MSE) verwenden. In der Segmentierung repräsentiert jedes Pixel im Zielmaskenbild die Klassennummer (one-hot-encoded entlang der dritten Dimension), sodass wir Verlustfunktionen verwenden müssen, die spezifisch für die Klassifikation sind - Kreuzentropieverlust, gemittelt über alle Pixel. Wenn die Maske binär ist, wird **binärer Kreuzentropieverlust** (BCE) verwendet.

> ✅ One-Hot-Encoding ist eine Methode, um ein Klassenlabel in einen Vektor der Länge zu kodieren, die der Anzahl der Klassen entspricht. Schauen Sie sich [diesen Artikel](https://datagy.io/sklearn-one-hot-encode/) zu dieser Technik an.

## Segmentierung in der medizinischen Bildgebung

In dieser Lektion werden wir die Segmentierung in Aktion sehen, indem wir das Netzwerk trainieren, um menschliche Nävi (auch als Muttermale bekannt) auf medizinischen Bildern zu erkennen. Wir werden die <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> Datenbank</a> von Dermatoskopiebildern als Bildquelle verwenden. Dieses Dataset enthält 200 Bilder von drei Klassen: typischer Nevus, atypischer Nevus und Melanom. Alle Bilder enthalten auch eine entsprechende **Maske**, die den Nevus umreißt.

> ✅ Diese Technik ist besonders geeignet für diese Art der medizinischen Bildgebung, aber welche anderen realen Anwendungen könnten Sie sich vorstellen?

<img alt="navi" src="images/navi.png"/>

> Bild aus der PH<sup>2</sup> Datenbank

Wir werden ein Modell trainieren, um jeden Nevus von seinem Hintergrund zu segmentieren.

## ✍️ Übungen: Semantische Segmentierung

Öffnen Sie die folgenden Notebooks, um mehr über verschiedene Architekturen der semantischen Segmentierung zu erfahren, mit ihnen zu üben und sie in Aktion zu sehen.

* [Semantische Segmentierung Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Semantische Segmentierung TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Nachlesequiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Fazit

Segmentierung ist eine sehr leistungsfähige Technik für die Bildklassifikation, die über Umrandungsrahmen hinaus zur Klassifikation auf Pixel-Ebene übergeht. Sie ist eine Technik, die in der medizinischen Bildgebung und anderen Anwendungen verwendet wird.

## 🚀 Herausforderung

Die Körpersegmentierung ist nur eine der häufigen Aufgaben, die wir mit Bildern von Menschen durchführen können. Weitere wichtige Aufgaben sind **Skelettdetektion** und **Posenerkennung**. Probieren Sie die [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) Bibliothek aus, um zu sehen, wie die Posenerkennung verwendet werden kann.

## Überprüfung & Selbststudium

Dieser [Wikipedia-Artikel](https://wikipedia.org/wiki/Image_segmentation) bietet einen guten Überblick über die verschiedenen Anwendungen dieser Technik. Lernen Sie selbst mehr über die Teilbereiche der Instanzsegmentierung und der panoptischen Segmentierung in diesem Forschungsfeld.

## [Aufgabe](lab/README.md)

In diesem Labor versuchen Sie die **Segmentierung des menschlichen Körpers** mithilfe des [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) von Kaggle.

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Verantwortung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.