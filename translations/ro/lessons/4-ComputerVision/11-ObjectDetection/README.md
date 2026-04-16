# Detectarea Obiectelor

Modelele de clasificare a imaginilor pe care le-am abordat până acum au luat o imagine și au produs un rezultat categoric, cum ar fi clasa 'număr' într-o problemă MNIST. Totuși, în multe cazuri nu dorim doar să știm că o imagine conține obiecte - vrem să putem determina locația lor exactă. Acesta este scopul **detectării obiectelor**.

## [Chestionar înainte de lecție](https://ff-quizzes.netlify.app/en/ai/quiz/21)

![Detectarea Obiectelor](../../../../../translated_images/ro/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be.webp)

> Imagine de pe [site-ul YOLO v2](https://pjreddie.com/darknet/yolov2/)

## O Abordare Naivă pentru Detectarea Obiectelor

Presupunând că dorim să găsim o pisică într-o imagine, o abordare foarte naivă pentru detectarea obiectelor ar fi următoarea:

1. Împărțim imaginea în mai multe secțiuni.
2. Aplicăm clasificarea imaginilor pe fiecare secțiune.
3. Secțiunile care generează o activare suficient de mare pot fi considerate ca conținând obiectul în cauză.

![Detectare Naivă a Obiectelor](../../../../../translated_images/ro/naive-detection.e7f1ba220ccd08c6.webp)

> *Imagine din [Notebook-ul de exerciții](ObjectDetection-TF.ipynb)*

Totuși, această abordare este departe de a fi ideală, deoarece permite algoritmului să localizeze foarte imprecis caseta de delimitare a obiectului. Pentru o localizare mai precisă, trebuie să aplicăm un fel de **regresie** pentru a prezice coordonatele casetelor de delimitare - și pentru aceasta, avem nevoie de seturi de date specifice.

## Regresie pentru Detectarea Obiectelor

[Acest articol de blog](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491) oferă o introducere excelentă în detectarea formelor.

## Seturi de Date pentru Detectarea Obiectelor

Este posibil să întâlniți următoarele seturi de date pentru această sarcină:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 20 clase
* [COCO](http://cocodataset.org/#home) - Obiecte Comune în Context. 80 clase, casete de delimitare și măști de segmentare

![COCO](../../../../../translated_images/ro/coco-examples.71bc60380fa6cceb.webp)

## Metrice pentru Detectarea Obiectelor

### Intersecția peste Uniune

În timp ce pentru clasificarea imaginilor este ușor să măsurăm cât de bine performează algoritmul, pentru detectarea obiectelor trebuie să măsurăm atât corectitudinea clasei, cât și precizia locației casetei de delimitare inferate. Pentru aceasta din urmă, folosim așa-numita **Intersecția peste Uniune** (IoU), care măsoară cât de bine se suprapun două casete (sau două zone arbitrare).

![IoU](../../../../../translated_images/ro/iou_equation.9a4751d40fff4e11.webp)

> *Figura 2 din [acest articol excelent despre IoU](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

Ideea este simplă - împărțim aria de intersecție dintre două figuri la aria uniunii lor. Pentru două arii identice, IoU ar fi 1, în timp ce pentru arii complet separate va fi 0. În alte cazuri, va varia de la 0 la 1. De obicei, luăm în considerare doar acele casete de delimitare pentru care IoU depășește o anumită valoare.

### Precizia Medie

Să presupunem că dorim să măsurăm cât de bine este recunoscută o anumită clasă de obiecte $C$. Pentru a măsura acest lucru, folosim metrica **Precizia Medie**, care se calculează astfel:

1. Considerăm curba Precizie-Recall care arată acuratețea în funcție de o valoare de prag de detectare (de la 0 la 1).
2. În funcție de prag, vom detecta mai multe sau mai puține obiecte în imagine și vom obține valori diferite de precizie și recall.
3. Curba va arăta astfel:

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *Imagine din [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

Precizia Medie pentru o clasă dată $C$ este aria de sub această curbă. Mai precis, axa Recall este de obicei împărțită în 10 părți, iar Precizia este mediată pe toate aceste puncte:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP și IoU

Vom lua în considerare doar acele detectări pentru care IoU depășește o anumită valoare. De exemplu, în setul de date PASCAL VOC, de obicei $\mbox{IoU Threshold} = 0.5$ este presupus, în timp ce în COCO AP este măsurat pentru diferite valori ale $\mbox{IoU Threshold}$.

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *Imagine din [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### Precizia Medie Generală - mAP

Principala metrică pentru detectarea obiectelor se numește **Precizia Medie Generală**, sau **mAP**. Este valoarea Preciziei Medii, mediată pe toate clasele de obiecte și, uneori, și pe $\mbox{IoU Threshold}$. Procesul de calculare a **mAP** este descris în detaliu
[în acest articol de blog](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)), și de asemenea [aici cu exemple de cod](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734).

## Diferite Abordări pentru Detectarea Obiectelor

Există două clase largi de algoritmi de detectare a obiectelor:

* **Rețele de Propunere a Regiunilor** (R-CNN, Fast R-CNN, Faster R-CNN). Ideea principală este de a genera **Regiuni de Interes** (ROI) și de a aplica CNN pe acestea, căutând activarea maximă. Este oarecum similar cu abordarea naivă, cu excepția faptului că ROI-urile sunt generate într-un mod mai inteligent. Unul dintre principalele dezavantaje ale acestor metode este că sunt lente, deoarece necesită multe treceri ale clasificatorului CNN peste imagine.
* Metode **One-pass** (YOLO, SSD, RetinaNet). În aceste arhitecturi, proiectăm rețeaua pentru a prezice atât clasele, cât și ROI-urile într-o singură trecere.

### R-CNN: CNN Bazat pe Regiuni

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) folosește [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) pentru a genera o structură ierarhică de regiuni ROI, care sunt apoi trecute prin extractoare de caracteristici CNN și clasificatoare SVM pentru a determina clasa obiectului, și regresie liniară pentru a determina coordonatele *casetei de delimitare*. [Lucrare oficială](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/ro/rcnn1.cae407020dfb1d1f.webp)

> *Imagine de van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/ro/rcnn2.2d9530bb83516484.webp)

> *Imagini din [acest blog](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - Fast R-CNN

Această abordare este similară cu R-CNN, dar regiunile sunt definite după ce straturile de convoluție au fost aplicate.

![FRCNN](../../../../../translated_images/ro/f-rcnn.3cda6d9bb4188875.webp)

> Imagine din [Lucrarea Oficială](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

Ideea principală a acestei abordări este de a folosi o rețea neuronală pentru a prezice ROI-urile - așa-numita *Rețea de Propunere a Regiunilor*. [Lucrare](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../translated_images/ro/faster-rcnn.8d46c099b87ef30a.webp)

> Imagine din [lucrarea oficială](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: Rețea Complet Convoluțională Bazată pe Regiuni

Acest algoritm este chiar mai rapid decât Faster R-CNN. Ideea principală este următoarea:

1. Extragem caracteristici folosind ResNet-101.
2. Caracteristicile sunt procesate de **Position-Sensitive Score Map**. Fiecare obiect din $C$ clase este împărțit în regiuni $k\times k$, și antrenăm pentru a prezice părți ale obiectelor.
3. Pentru fiecare parte din regiunile $k\times k$, toate rețelele votează pentru clasele de obiecte, iar clasa de obiect cu votul maxim este selectată.

![r-fcn image](../../../../../translated_images/ro/r-fcn.13eb88158b99a3da.webp)

> Imagine din [lucrarea oficială](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO este un algoritm în timp real, cu o singură trecere. Ideea principală este următoarea:

 * Imaginea este împărțită în regiuni $S\times S$.
 * Pentru fiecare regiune, **CNN** prezice $n$ obiecte posibile, coordonatele *casetei de delimitare* și *încrederea*=*probabilitatea* * IoU.

 ![YOLO](../../../../../translated_images/ro/yolo.a2648ec82ee8bb4e.webp)

> Imagine din [lucrarea oficială](https://arxiv.org/abs/1506.02640)

### Alte Algoritmi

* RetinaNet: [lucrare oficială](https://arxiv.org/abs/1708.02002)
   - [Implementare PyTorch în Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Implementare Keras](https://github.com/fizyr/keras-retinanet)
   - [Detectarea Obiectelor cu RetinaNet](https://keras.io/examples/vision/retinanet/) în exemplele Keras
* SSD (Single Shot Detector): [lucrare oficială](https://arxiv.org/abs/1512.02325)

## ✍️ Exerciții: Detectarea Obiectelor

Continuă învățarea în următorul notebook:

[ObjectDetection.ipynb](ObjectDetection.ipynb)

## Concluzie

În această lecție ai explorat rapid toate modurile diferite prin care detectarea obiectelor poate fi realizată!

## 🚀 Provocare

Citește aceste articole și notebook-uri despre YOLO și încearcă-le singur:

* [Articol de blog bun](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) despre YOLO
 * [Site oficial](https://pjreddie.com/darknet/yolo/)
 * Yolo: [Implementare Keras](https://github.com/experiencor/keras-yolo2), [notebook pas cu pas](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [Implementare Keras](https://github.com/experiencor/keras-yolo2), [notebook pas cu pas](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Chestionar după lecție](https://ff-quizzes.netlify.app/en/ai/quiz/22)

## Recapitulare & Studiu Individual

* [Detectarea Obiectelor](https://tjmachinelearning.com/lectures/1718/obj/) de Nikhil Sardana
* [O comparație bună a algoritmilor de detectare a obiectelor](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Revizuirea algoritmilor de învățare profundă pentru detectarea obiectelor](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [Introducere pas cu pas în algoritmii de bază pentru detectarea obiectelor](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implementarea Faster R-CNN în Python pentru detectarea obiectelor](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Temă: Detectarea Obiectelor](lab/README.md)

---

