<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d85c8b08f6d1b48fd7f35b99f93c1138",
  "translation_date": "2025-08-24T10:28:34+00:00",
  "source_file": "lessons/4-ComputerVision/11-ObjectDetection/README.md",
  "language_code": "pl"
}
-->
# Wykrywanie Obiektów

Modele klasyfikacji obrazów, które omawialiśmy do tej pory, przyjmowały obraz i zwracały wynik kategoryczny, na przykład klasę 'liczba' w problemie MNIST. Jednak w wielu przypadkach nie wystarczy wiedzieć, że na zdjęciu znajdują się obiekty – chcemy również określić ich dokładne położenie. Na tym właśnie polega **wykrywanie obiektów**.

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ai/quiz/21)

![Wykrywanie Obiektów](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/Screen_Shot_2016-11-17_at_11.14.54_AM.png)

> Obraz z [strony YOLO v2](https://pjreddie.com/darknet/yolov2/)

## Naiwne podejście do wykrywania obiektów

Załóżmy, że chcemy znaleźć kota na zdjęciu. Bardzo naiwne podejście do wykrywania obiektów mogłoby wyglądać następująco:

1. Podziel obraz na wiele kafelków.
2. Przeprowadź klasyfikację obrazu dla każdego kafelka.
3. Kafelki, które dają wystarczająco wysoką aktywację, można uznać za zawierające poszukiwany obiekt.

![Naiwne wykrywanie obiektów](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/naive-detection.png)

> *Obraz z [notatnika ćwiczeniowego](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection-TF.ipynb)*

Jednak takie podejście jest dalekie od ideału, ponieważ pozwala algorytmowi na bardzo niedokładne określenie granic obiektu. Aby uzyskać bardziej precyzyjne lokalizacje, musimy zastosować pewien rodzaj **regresji**, aby przewidzieć współrzędne granic obiektów – a do tego potrzebne są odpowiednie zestawy danych.

## Regresja w wykrywaniu obiektów

[Ten wpis na blogu](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491) oferuje świetne wprowadzenie do wykrywania kształtów.

## Zestawy danych do wykrywania obiektów

Możesz natknąć się na następujące zestawy danych do tego zadania:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) – 20 klas
* [COCO](http://cocodataset.org/#home) – Common Objects in Context. 80 klas, granice obiektów i maski segmentacyjne

![COCO](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/coco-examples.jpg)

## Metryki wykrywania obiektów

### Intersection over Union

Podczas gdy w klasyfikacji obrazów łatwo jest zmierzyć, jak dobrze działa algorytm, w wykrywaniu obiektów musimy ocenić zarówno poprawność klasy, jak i precyzję lokalizacji przewidzianych granic obiektów. Do tego ostatniego używamy metryki zwanej **Intersection over Union** (IoU), która mierzy, jak dobrze dwa obszary (lub dwie dowolne figury) się pokrywają.

![IoU](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/iou_equation.png)

> *Rysunek 2 z [tego świetnego wpisu na blogu o IoU](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

Idea jest prosta – dzielimy obszar przecięcia dwóch figur przez obszar ich unii. Dla dwóch identycznych obszarów IoU wynosi 1, a dla całkowicie rozłącznych obszarów wynosi 0. W innych przypadkach wartość IoU mieści się w przedziale od 0 do 1. Zazwyczaj bierzemy pod uwagę tylko te granice obiektów, dla których IoU przekracza określoną wartość.

### Średnia precyzja (Average Precision)

Załóżmy, że chcemy zmierzyć, jak dobrze rozpoznawana jest dana klasa obiektów $C$. Do tego celu używamy metryki **Average Precision**, która jest obliczana w następujący sposób:

1. Rozważ krzywą Precision-Recall, która pokazuje dokładność w zależności od wartości progu detekcji (od 0 do 1).
2. W zależności od progu, wykryjemy więcej lub mniej obiektów na obrazie, co da różne wartości precyzji i czułości.
3. Krzywa wygląda tak:

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *Obraz z [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

Średnia precyzja dla danej klasy $C$ to pole pod tą krzywą. Dokładniej, oś Recall jest zazwyczaj podzielona na 10 części, a precyzja jest uśredniana dla wszystkich tych punktów:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP i IoU

Rozważamy tylko te detekcje, dla których IoU przekracza określoną wartość. Na przykład w zestawie danych PASCAL VOC zazwyczaj $\mbox{IoU Threshold} = 0.5$, podczas gdy w COCO AP jest mierzony dla różnych wartości $\mbox{IoU Threshold}$.

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *Obraz z [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### Średnia średnia precyzja – mAP

Główna metryka dla wykrywania obiektów nazywa się **Mean Average Precision**, czyli **mAP**. Jest to wartość Average Precision, uśredniona dla wszystkich klas obiektów, a czasami także dla różnych wartości $\mbox{IoU Threshold}$. Szczegółowy opis procesu obliczania **mAP** znajdziesz
[w tym wpisie na blogu](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)), a także [tutaj z przykładami kodu](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734).

## Różne podejścia do wykrywania obiektów

Istnieją dwie główne klasy algorytmów wykrywania obiektów:

* **Sieci propozycji regionów** (R-CNN, Fast R-CNN, Faster R-CNN). Główna idea polega na generowaniu **Regionów Zainteresowania** (ROI) i uruchamianiu CNN na nich, szukając maksymalnej aktywacji. Jest to trochę podobne do naiwnego podejścia, z wyjątkiem tego, że ROI są generowane w bardziej inteligentny sposób. Jednym z głównych minusów takich metod jest ich wolne działanie, ponieważ wymagają wielu przejść klasyfikatora CNN przez obraz.
* Metody **jednoprzebiegowe** (YOLO, SSD, RetinaNet). W tych architekturach projektujemy sieć tak, aby przewidywała zarówno klasy, jak i ROI w jednym przebiegu.

### R-CNN: Region-Based CNN

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) używa [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) do generowania hierarchicznej struktury regionów ROI, które następnie są przepuszczane przez ekstraktory cech CNN i klasyfikatory SVM, aby określić klasę obiektu, oraz regresję liniową, aby określić współrzędne *granicy obiektu*. [Oficjalny artykuł](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/rcnn1.png)

> *Obraz z van de Sande et al. ICCV’11*

![RCNN-1](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/rcnn2.png)

> *Obrazy z [tego bloga](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - Fast R-CNN

To podejście jest podobne do R-CNN, ale regiony są definiowane po zastosowaniu warstw konwolucyjnych.

![FRCNN](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/f-rcnn.png)

> Obraz z [oficjalnego artykułu](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

Główna idea tego podejścia polega na użyciu sieci neuronowej do przewidywania ROI – tak zwanej *Region Proposal Network*. [Artykuł](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/faster-rcnn.png)

> Obraz z [oficjalnego artykułu](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: Region-Based Fully Convolutional Network

Ten algorytm jest jeszcze szybszy niż Faster R-CNN. Główna idea jest następująca:

1. Wyciągamy cechy za pomocą ResNet-101.
2. Cechy są przetwarzane przez **Position-Sensitive Score Map**. Każdy obiekt z $C$ klas jest podzielony na $k\times k$ regiony, a sieć uczy się przewidywać części obiektów.
3. Dla każdej części z $k\times k$ regionów wszystkie sieci głosują na klasy obiektów, a klasa obiektu z największą liczbą głosów jest wybierana.

![r-fcn image](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/r-fcn.png)

> Obraz z [oficjalnego artykułu](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO to algorytm jednoprzebiegowy w czasie rzeczywistym. Główna idea jest następująca:

 * Obraz jest podzielony na $S\times S$ regiony.
 * Dla każdego regionu **CNN** przewiduje $n$ możliwych obiektów, współrzędne *granicy obiektu* oraz *pewność*=*prawdopodobieństwo* * IoU.

 ![YOLO](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/yolo.png)

> Obraz z [oficjalnego artykułu](https://arxiv.org/abs/1506.02640)

### Inne algorytmy

* RetinaNet: [oficjalny artykuł](https://arxiv.org/abs/1708.02002)
   - [Implementacja w PyTorch w Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Implementacja w Keras](https://github.com/fizyr/keras-retinanet)
   - [Wykrywanie obiektów za pomocą RetinaNet](https://keras.io/examples/vision/retinanet/) w przykładach Keras
* SSD (Single Shot Detector): [oficjalny artykuł](https://arxiv.org/abs/1512.02325)

## ✍️ Ćwiczenia: Wykrywanie Obiektów

Kontynuuj naukę w następującym notatniku:

[ObjectDetection.ipynb](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)

## Podsumowanie

W tej lekcji odbyłeś szybki przegląd różnych sposobów, w jakie można realizować wykrywanie obiektów!

## 🚀 Wyzwanie

Przeczytaj te artykuły i notatniki o YOLO i spróbuj je samodzielnie:

* [Dobry wpis na blogu](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) opisujący YOLO
 * [Oficjalna strona](https://pjreddie.com/darknet/yolo/)
 * YOLO: [Implementacja w Keras](https://github.com/experiencor/keras-yolo2), [notatnik krok po kroku](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * YOLO v2: [Implementacja w Keras](https://github.com/experiencor/keras-yolo2), [notatnik krok po kroku](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ai/quiz/22)

## Przegląd i samodzielna nauka

* [Wykrywanie Obiektów](https://tjmachinelearning.com/lectures/1718/obj/) autorstwa Nikhila Sardany
* [Dobry przegląd algorytmów wykrywania obiektów](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Przegląd algorytmów głębokiego uczenia do wykrywania obiektów](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [Wprowadzenie krok po kroku do podstawowych algorytmów wykrywania obiektów](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implementacja Faster R-CNN w Pythonie do wykrywania obiektów](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Zadanie: Wykrywanie Obiektów](lab/README.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.