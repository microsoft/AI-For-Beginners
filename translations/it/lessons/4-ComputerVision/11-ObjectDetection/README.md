<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d85c8b08f6d1b48fd7f35b99f93c1138",
  "translation_date": "2025-08-26T07:01:38+00:00",
  "source_file": "lessons/4-ComputerVision/11-ObjectDetection/README.md",
  "language_code": "it"
}
-->
# Rilevamento degli Oggetti

I modelli di classificazione delle immagini che abbiamo trattato finora prendevano un'immagine e producevano un risultato categorico, come la classe 'numero' in un problema MNIST. Tuttavia, in molti casi non vogliamo solo sapere che un'immagine ritrae degli oggetti, ma desideriamo anche determinare la loro posizione precisa. Questo è esattamente l'obiettivo del **rilevamento degli oggetti**.

## [Quiz pre-lezione](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/111)

![Rilevamento degli Oggetti](../../../../../translated_images/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be1b905373ed9c858102c054b16e4595c76ec3f7bba0feb549.it.png)

> Immagine dal [sito web di YOLO v2](https://pjreddie.com/darknet/yolov2/)

## Un Approccio Naïve al Rilevamento degli Oggetti

Supponiamo di voler trovare un gatto in un'immagine. Un approccio molto semplice al rilevamento degli oggetti potrebbe essere il seguente:

1. Suddividere l'immagine in un certo numero di riquadri.
2. Eseguire la classificazione delle immagini su ciascun riquadro.
3. I riquadri che producono un'attivazione sufficientemente alta possono essere considerati contenenti l'oggetto in questione.

![Rilevamento Naïve](../../../../../translated_images/naive-detection.e7f1ba220ccd08c68a2ea8e06a7ed75c3fcc738c2372f9e00b7f4299a8659c01.it.png)

> *Immagine dal [Notebook di Esercizi](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection-TF.ipynb)*

Tuttavia, questo approccio è tutt'altro che ideale, poiché consente all'algoritmo di individuare il riquadro di delimitazione dell'oggetto in modo molto impreciso. Per una localizzazione più precisa, dobbiamo eseguire una sorta di **regressione** per prevedere le coordinate dei riquadri di delimitazione, e per farlo abbiamo bisogno di dataset specifici.

## Regressione per il Rilevamento degli Oggetti

[Questo articolo](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491) offre un'ottima introduzione al rilevamento delle forme.

## Dataset per il Rilevamento degli Oggetti

Potresti imbatterti nei seguenti dataset per questo compito:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 20 classi
* [COCO](http://cocodataset.org/#home) - Common Objects in Context. 80 classi, riquadri di delimitazione e maschere di segmentazione

![COCO](../../../../../translated_images/coco-examples.71bc60380fa6cceb7caad48bd09e35b6028caabd363aa04fee89c414e0870e86.it.jpg)

## Metriche per il Rilevamento degli Oggetti

### Intersezione su Unione

Mentre per la classificazione delle immagini è facile misurare quanto bene l'algoritmo si comporta, per il rilevamento degli oggetti dobbiamo misurare sia la correttezza della classe che la precisione della posizione del riquadro di delimitazione inferito. Per quest'ultimo, utilizziamo la cosiddetta **Intersezione su Unione** (IoU), che misura quanto bene due riquadri (o due aree arbitrarie) si sovrappongono.

![IoU](../../../../../translated_images/iou_equation.9a4751d40fff4e119ecd0a7bcca4e71ab1dc83e0d4f2a0d66ff0859736f593cf.it.png)

> *Figura 2 da [questo eccellente articolo su IoU](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

L'idea è semplice: dividiamo l'area di intersezione tra due figure per l'area della loro unione. Per due aree identiche, IoU sarà 1, mentre per aree completamente disgiunte sarà 0. Altrimenti varierà da 0 a 1. Consideriamo tipicamente solo quei riquadri di delimitazione per cui IoU supera un certo valore.

### Precisione Media

Supponiamo di voler misurare quanto bene una determinata classe di oggetti $C$ viene riconosciuta. Per misurarlo, utilizziamo la metrica della **Precisione Media** (AP), calcolata come segue:

1. Consideriamo la curva Precisione-Richiamo, che mostra l'accuratezza in base a un valore di soglia di rilevamento (da 0 a 1).
2. A seconda della soglia, rileveremo più o meno oggetti nell'immagine, con valori diversi di precisione e richiamo.
3. La curva avrà questo aspetto:

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *Immagine da [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

La Precisione Media per una data classe $C$ è l'area sotto questa curva. Più precisamente, l'asse del Richiamo è tipicamente diviso in 10 parti, e la Precisione è mediata su tutti questi punti:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP e IoU

Considereremo solo quei rilevamenti per cui IoU supera un certo valore. Ad esempio, nel dataset PASCAL VOC tipicamente $\mbox{IoU Threshold} = 0.5$, mentre in COCO AP viene misurato per diversi valori di $\mbox{IoU Threshold}$.

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *Immagine da [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### Precisione Media Media - mAP

La metrica principale per il Rilevamento degli Oggetti è chiamata **Precisione Media Media**, o **mAP**. È il valore della Precisione Media, mediato su tutte le classi di oggetti, e talvolta anche su $\mbox{IoU Threshold}$. Il processo di calcolo della **mAP** è descritto in dettaglio
[in questo articolo](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3), e anche [qui con esempi di codice](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734).

## Diversi Approcci al Rilevamento degli Oggetti

Esistono due grandi categorie di algoritmi di rilevamento degli oggetti:

* **Reti di Proposta di Regione** (R-CNN, Fast R-CNN, Faster R-CNN). L'idea principale è generare **Regioni di Interesse** (ROI) ed eseguire CNN su di esse, cercando l'attivazione massima. È un po' simile all'approccio naïve, con l'eccezione che le ROI vengono generate in modo più intelligente. Uno dei principali svantaggi di tali metodi è che sono lenti, poiché richiedono molti passaggi del classificatore CNN sull'immagine.
* Metodi **a passaggio unico** (YOLO, SSD, RetinaNet). In queste architetture, la rete è progettata per prevedere sia le classi che le ROI in un unico passaggio.

### R-CNN: CNN Basata su Regione

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) utilizza [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) per generare una struttura gerarchica di regioni ROI, che vengono poi passate attraverso estrattori di caratteristiche CNN e classificatori SVM per determinare la classe dell'oggetto, e una regressione lineare per determinare le coordinate del *riquadro di delimitazione*. [Articolo ufficiale](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/rcnn1.cae407020dfb1d1fb572656e44f75cd6c512cc220591c116c506652c10e47f26.it.png)

> *Immagine da van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/rcnn2.2d9530bb83516484ec65b250c22dbf37d3d23244f32864ebcb91d98fe7c3112c.it.png)

> *Immagini da [questo articolo](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - Fast R-CNN

Questo approccio è simile a R-CNN, ma le regioni vengono definite dopo che i livelli convoluzionali sono stati applicati.

![FRCNN](../../../../../translated_images/f-rcnn.3cda6d9bb41888754037d2d9763e2298a96de5d9bc2a21db3147357aa5da9b1a.it.png)

> Immagine dall'[articolo ufficiale](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

L'idea principale di questo approccio è utilizzare una rete neurale per prevedere le ROI - la cosiddetta *Rete di Proposta di Regione*. [Articolo](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../translated_images/faster-rcnn.8d46c099b87ef30ab2ea26dbc4bdd85b974a57ba8eb526f65dc4cd0a4711de30.it.png)

> Immagine dall'[articolo ufficiale](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: Rete Completamente Convoluzionale Basata su Regione

Questo algoritmo è ancora più veloce di Faster R-CNN. L'idea principale è la seguente:

1. Estraiamo caratteristiche utilizzando ResNet-101.
2. Le caratteristiche vengono elaborate da una **Mappa di Punteggio Sensibile alla Posizione**. Ogni oggetto delle classi $C$ viene suddiviso in regioni $k\times k$, e addestriamo la rete a prevedere parti degli oggetti.
3. Per ogni parte delle regioni $k\times k$, tutte le reti votano per le classi degli oggetti, e viene selezionata la classe con il massimo voto.

![r-fcn image](../../../../../translated_images/r-fcn.13eb88158b99a3da50fa2787a6be5cb310d47f0e9655cc93a1090dc7aab338d1.it.png)

> Immagine dall'[articolo ufficiale](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO è un algoritmo in tempo reale a passaggio unico. L'idea principale è la seguente:

 * L'immagine viene suddivisa in regioni $S\times S$.
 * Per ogni regione, **CNN** prevede $n$ oggetti possibili, le coordinate del *riquadro di delimitazione* e la *confidenza* = *probabilità* * IoU.

 ![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.it.png)

> Immagine dall'[articolo ufficiale](https://arxiv.org/abs/1506.02640)

### Altri Algoritmi

* RetinaNet: [articolo ufficiale](https://arxiv.org/abs/1708.02002)
   - [Implementazione PyTorch in Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Implementazione Keras](https://github.com/fizyr/keras-retinanet)
   - [Rilevamento degli Oggetti con RetinaNet](https://keras.io/examples/vision/retinanet/) nei campioni Keras
* SSD (Single Shot Detector): [articolo ufficiale](https://arxiv.org/abs/1512.02325)

## ✍️ Esercizi: Rilevamento degli Oggetti

Continua il tuo apprendimento nel seguente notebook:

[ObjectDetection.ipynb](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)

## Conclusione

In questa lezione hai fatto un rapido tour di tutti i vari modi in cui il rilevamento degli oggetti può essere realizzato!

## 🚀 Sfida

Leggi questi articoli e notebook su YOLO e prova a utilizzarli tu stesso:

* [Ottimo articolo](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) che descrive YOLO
 * [Sito ufficiale](https://pjreddie.com/darknet/yolo/)
 * YOLO: [Implementazione Keras](https://github.com/experiencor/keras-yolo2), [notebook passo-passo](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * YOLO v2: [Implementazione Keras](https://github.com/experiencor/keras-yolo2), [notebook passo-passo](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Quiz post-lezione](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## Revisione e Studio Autonomo

* [Rilevamento degli Oggetti](https://tjmachinelearning.com/lectures/1718/obj/) di Nikhil Sardana
* [Un buon confronto tra algoritmi di rilevamento degli oggetti](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Revisione degli Algoritmi di Deep Learning per il Rilevamento degli Oggetti](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [Introduzione passo-passo agli Algoritmi di Rilevamento degli Oggetti di Base](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implementazione di Faster R-CNN in Python per il Rilevamento degli Oggetti](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Compito: Rilevamento degli Oggetti](lab/README.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.