## Objekt Erkennung

Die Bildklassifizierungsmodelle, mit denen wir bisher gearbeitet haben, nahmen ein Bild und lieferten ein kategoriales Ergebnis, wie die Klasse 'Zahl' in einem MNIST-Problem. In vielen Fällen wollen wir jedoch nicht nur wissen, dass ein Bild Objekte darstellt - wir wollen in der Lage sein, ihren genauen Standort zu bestimmen. Genau das ist der Punkt der **Objekt Erkennung**.

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/111)

![Objekt Erkennung](../../../../../translated_images/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be1b905373ed9c858102c054b16e4595c76ec3f7bba0feb549.de.png)

> Bild von [YOLO v2 Webseite](https://pjreddie.com/darknet/yolov2/)

## Ein Naiver Ansatz zur Objekt Erkennung

Angenommen, wir wollten eine Katze auf einem Bild finden, ein sehr naiver Ansatz zur Objekt Erkennung wäre folgender:

1. Zerlegen Sie das Bild in eine Anzahl von Kacheln.
2. Führen Sie die Bildklassifizierung auf jeder Kachel durch.
3. Die Kacheln, die eine ausreichend hohe Aktivierung ergeben, können als solche betrachtet werden, die das betreffende Objekt enthalten.

![Naive Objekt Erkennung](../../../../../translated_images/naive-detection.e7f1ba220ccd08c68a2ea8e06a7ed75c3fcc738c2372f9e00b7f4299a8659c01.de.png)

> *Bild aus [Übungsnotizbuch](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection-TF.ipynb)*

Dieser Ansatz ist jedoch alles andere als ideal, da er es dem Algorithmus nur ermöglicht, die Begrenzungsbox des Objekts sehr ungenau zu lokalisieren. Für eine genauere Lokalisierung müssen wir eine Art **Regression** durchführen, um die Koordinaten der Begrenzungsrahmen vorherzusagen - und dafür benötigen wir spezifische Datensätze.

## Regression zur Objekt Erkennung

[Dieser Blogbeitrag](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491) bietet eine großartige sanfte Einführung in die Erkennung von Formen.

## Datensätze zur Objekt Erkennung

Sie könnten auf die folgenden Datensätze für diese Aufgabe stoßen:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 20 Klassen
* [COCO](http://cocodataset.org/#home) - Gemeinsame Objekte im Kontext. 80 Klassen, Begrenzungsrahmen und Segmentierungs-Masken

![COCO](../../../../../translated_images/coco-examples.71bc60380fa6cceb7caad48bd09e35b6028caabd363aa04fee89c414e0870e86.de.jpg)

## Metriken zur Objekt Erkennung

### Schnittmenge über Vereinigung

Während es bei der Bildklassifizierung einfach ist, zu messen, wie gut der Algorithmus funktioniert, müssen wir bei der Objekt Erkennung sowohl die Richtigkeit der Klasse als auch die Präzision des abgeleiteten Begrenzungsrahmenstandorts messen. Für letzteres verwenden wir die sogenannte **Schnittmenge über Vereinigung** (IoU), die misst, wie gut zwei Boxen (oder zwei beliebige Bereiche) überlappen.

![IoU](../../../../../translated_images/iou_equation.9a4751d40fff4e119ecd0a7bcca4e71ab1dc83e0d4f2a0d66ff0859736f593cf.de.png)

> *Abbildung 2 aus [diesem ausgezeichneten Blogbeitrag über IoU](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

Die Idee ist einfach - wir teilen die Fläche der Schnittmenge zwischen zwei Figuren durch die Fläche ihrer Vereinigung. Für zwei identische Bereiche wäre IoU 1, während es für vollständig disjunkte Bereiche 0 sein würde. Ansonsten variiert es von 0 bis 1. Wir berücksichtigen typischerweise nur diejenigen Begrenzungsrahmen, für die IoU über einem bestimmten Wert liegt.

### Durchschnittliche Präzision

Angenommen, wir wollen messen, wie gut eine gegebene Klasse von Objekten $C$ erkannt wird. Um dies zu messen, verwenden wir **Durchschnittliche Präzisions**-Metriken, die wie folgt berechnet werden:

1. Betrachten Sie die Precision-Recall-Kurve, die die Genauigkeit in Abhängigkeit von einem Erkennungsschwellenwert (von 0 bis 1) zeigt.
2. Je nach Schwellenwert erhalten wir mehr oder weniger Objekte, die im Bild erkannt werden, und unterschiedliche Werte für Präzision und Rückruf.
3. Die Kurve sieht folgendermaßen aus:

> *Bild aus [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

Die durchschnittliche Präzision für eine gegebene Klasse $C$ ist die Fläche unter dieser Kurve. Genauer gesagt, wird die Recall-Achse typischerweise in 10 Teile unterteilt, und die Präzision wird über all diese Punkte gemittelt:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP und IoU

Wir werden nur diejenigen Erkennungen berücksichtigen, für die IoU über einem bestimmten Wert liegt. Zum Beispiel wird im PASCAL VOC-Datensatz typischerweise $\mbox{IoU-Schwellenwert} = 0.5$ angenommen, während im COCO AP für unterschiedliche Werte von $\mbox{IoU-Schwellenwert}$ gemessen wird.

### Durchschnittliche Durchschnittliche Präzision - mAP

Die Hauptmetrik für die Objekt Erkennung wird **Durchschnittliche Durchschnittliche Präzision** oder **mAP** genannt. Es ist der Wert der Durchschnittlichen Präzision, gemittelt über alle Objektklassen und manchmal auch über $\mbox{IoU-Schwellenwert}$. Im Detail wird der Prozess zur Berechnung von **mAP** in
[diesem Blogbeitrag](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3) beschrieben, und auch [hier mit Codebeispielen](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734).

## Verschiedene Ansätze zur Objekt Erkennung

Es gibt zwei breite Klassen von Algorithmen zur Objekt Erkennung:

* **Region Proposal Networks** (R-CNN, Fast R-CNN, Faster R-CNN). Die Hauptidee besteht darin, **Regionen von Interessen** (ROI) zu generieren und CNN darüber laufen zu lassen, um maximale Aktivierung zu suchen. Es ist ein wenig ähnlich wie der naive Ansatz, mit der Ausnahme, dass ROIs auf eine cleverere Weise generiert werden. Einer der größten Nachteile solcher Methoden ist, dass sie langsam sind, da wir viele Durchläufe des CNN-Klassifikators über das Bild benötigen.
* **Einmalige** (YOLO, SSD, RetinaNet) Methoden. In diesen Architekturen entwerfen wir das Netzwerk, um sowohl Klassen als auch ROIs in einem Durchgang vorherzusagen.

### R-CNN: Region-Based CNN

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) verwendet [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf), um eine hierarchische Struktur von ROI-Regionen zu generieren, die dann durch CNN-Feature-Extraktoren und SVM-Klassifizierer geleitet werden, um die Objektklasse zu bestimmen, und durch lineare Regression, um die *Begrenzungsrahmen*-Koordinaten zu bestimmen. [Offizielles Papier](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/rcnn1.cae407020dfb1d1fb572656e44f75cd6c512cc220591c116c506652c10e47f26.de.png)

> *Bild von van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/rcnn2.2d9530bb83516484ec65b250c22dbf37d3d23244f32864ebcb91d98fe7c3112c.de.png)

> *Bilder aus [diesem Blog](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - Fast R-CNN

Dieser Ansatz ähnelt R-CNN, aber die Regionen werden definiert, nachdem die Faltungsschichten angewendet wurden.

![FRCNN](../../../../../translated_images/f-rcnn.3cda6d9bb41888754037d2d9763e2298a96de5d9bc2a21db3147357aa5da9b1a.de.png)

> Bild aus [dem offiziellen Papier](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

Die Hauptidee dieses Ansatzes ist es, ein neuronales Netzwerk zu verwenden, um ROIs vorherzusagen - so genannte *Region Proposal Network*. [Papier](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../translated_images/faster-rcnn.8d46c099b87ef30ab2ea26dbc4bdd85b974a57ba8eb526f65dc4cd0a4711de30.de.png)

> Bild aus [dem offiziellen Papier](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: Region-Based Fully Convolutional Network

Dieser Algorithmus ist sogar schneller als Faster R-CNN. Die Hauptidee ist folgende:

1. Wir extrahieren Merkmale mit ResNet-101.
2. Merkmale werden durch **Positionssensitives Score Map** verarbeitet. Jedes Objekt aus $C$ Klassen wird in $k\times k$ Regionen unterteilt, und wir trainieren, um Teile von Objekten vorherzusagen.
3. Für jedes Teil aus $k\times k$ Regionen stimmen alle Netzwerke für Objektklassen ab, und die Objektklasse mit der maximalen Stimme wird ausgewählt.

![r-fcn image](../../../../../translated_images/r-fcn.13eb88158b99a3da50fa2787a6be5cb310d47f0e9655cc93a1090dc7aab338d1.de.png)

> Bild aus [offiziellen Papier](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO ist ein Echtzeit-Einmal-Algorithmus. Die Hauptidee ist folgende:

* Das Bild wird in $S\times S$ Regionen unterteilt.
* Für jede Region sagt **CNN** $n$ mögliche Objekte, *Begrenzungsrahmen*-Koordinaten und *Konfidenz*=*Wahrscheinlichkeit* * IoU voraus.

![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.de.png)
> Bild aus [offiziellen Papier](https://arxiv.org/abs/1506.02640)

### Andere Algorithmen

* RetinaNet: [offizielles Papier](https://arxiv.org/abs/1708.02002)
   - [PyTorch-Implementierung in Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Keras-Implementierung](https://github.com/fizyr/keras-retinanet)
   - [Objekterkennung mit RetinaNet](https://keras.io/examples/vision/retinanet/) in Keras-Beispielen
* SSD (Single Shot Detector): [offizielles Papier](https://arxiv.org/abs/1512.02325)

## ✍️ Übungen: Objekterkennung

Setze dein Lernen im folgenden Notizbuch fort:

[ObjectDetection.ipynb](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)

## Fazit

In dieser Lektion hast du eine rasante Tour durch die verschiedenen Möglichkeiten der Objekterkennung gemacht!

## 🚀 Herausforderung

Lies dir diese Artikel und Notizbücher über YOLO durch und probiere sie selbst aus.

* [Guter Blogbeitrag](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) der YOLO beschreibt
 * [Offizielle Seite](https://pjreddie.com/darknet/yolo/)
 * Yolo: [Keras-Implementierung](https://github.com/experiencor/keras-yolo2), [Schritt-für-Schritt-Notizbuch](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [Keras-Implementierung](https://github.com/experiencor/keras-yolo2), [Schritt-für-Schritt-Notizbuch](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Nach der Vorlesung Quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## Überprüfung & Selbststudium

* [Objekterkennung](https://tjmachinelearning.com/lectures/1718/obj/) von Nikhil Sardana
* [Ein guter Vergleich von Algorithmen zur Objekterkennung](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Überprüfung von Deep Learning-Algorithmen zur Objekterkennung](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [Eine Schritt-für-Schritt-Einführung in die grundlegenden Algorithmen zur Objekterkennung](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implementierung von Faster R-CNN in Python zur Objekterkennung](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Aufgabe: Objekterkennung](lab/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.