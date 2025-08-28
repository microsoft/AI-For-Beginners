<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d85c8b08f6d1b48fd7f35b99f93c1138",
  "translation_date": "2025-08-28T15:21:40+00:00",
  "source_file": "lessons/4-ComputerVision/11-ObjectDetection/README.md",
  "language_code": "da"
}
-->
# Objektgenkendelse

De billedklassifikationsmodeller, vi har arbejdet med indtil nu, tog et billede og producerede et kategorisk resultat, såsom klassen 'nummer' i et MNIST-problem. Men i mange tilfælde ønsker vi ikke blot at vide, at et billede viser objekter - vi vil også kunne bestemme deres præcise placering. Det er netop formålet med **objektgenkendelse**.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/111)

![Objektgenkendelse](../../../../../translated_images/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be1b905373ed9c858102c054b16e4595c76ec3f7bba0feb549.da.png)

> Billede fra [YOLO v2 websted](https://pjreddie.com/darknet/yolov2/)

## En naiv tilgang til objektgenkendelse

Antag, at vi ville finde en kat på et billede. En meget naiv tilgang til objektgenkendelse kunne være følgende:

1. Opdel billedet i en række fliser.
2. Kør billedklassifikation på hver flise.
3. De fliser, der resulterer i tilstrækkelig høj aktivering, kan betragtes som indeholdende det ønskede objekt.

![Naiv objektgenkendelse](../../../../../translated_images/naive-detection.e7f1ba220ccd08c68a2ea8e06a7ed75c3fcc738c2372f9e00b7f4299a8659c01.da.png)

> *Billede fra [Exercise Notebook](ObjectDetection-TF.ipynb)*

Denne tilgang er dog langt fra ideel, da den kun tillader algoritmen at lokalisere objektets afgrænsningsboks meget upræcist. For mere præcis lokalisering skal vi udføre en form for **regression** for at forudsige koordinaterne for afgrænsningsbokse - og til det har vi brug for specifikke datasæt.

## Regression til objektgenkendelse

[Dette blogindlæg](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491) giver en god introduktion til at genkende former.

## Datasæt til objektgenkendelse

Du kan støde på følgende datasæt til denne opgave:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 20 klasser
* [COCO](http://cocodataset.org/#home) - Common Objects in Context. 80 klasser, afgrænsningsbokse og segmenteringsmasker

![COCO](../../../../../translated_images/coco-examples.71bc60380fa6cceb7caad48bd09e35b6028caabd363aa04fee89c414e0870e86.da.jpg)

## Objektgenkendelsesmetrikker

### Intersection over Union

Mens det er nemt at måle, hvor godt algoritmen klarer sig ved billedklassifikation, skal vi ved objektgenkendelse måle både korrektheden af klassen og præcisionen af den udledte afgrænsningsboks placering. Til det sidste bruger vi den såkaldte **Intersection over Union** (IoU), som måler, hvor godt to bokse (eller to vilkårlige områder) overlapper.

![IoU](../../../../../translated_images/iou_equation.9a4751d40fff4e119ecd0a7bcca4e71ab1dc83e0d4f2a0d66ff0859736f593cf.da.png)

> *Figur 2 fra [dette fremragende blogindlæg om IoU](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

Ideen er enkel - vi dividerer arealet af overlapningen mellem to figurer med arealet af deres union. For to identiske områder vil IoU være 1, mens for helt adskilte områder vil det være 0. Ellers vil det variere fra 0 til 1. Vi overvejer typisk kun de afgrænsningsbokse, hvor IoU er over en vis værdi.

### Average Precision

Antag, at vi vil måle, hvor godt en given klasse af objekter $C$ genkendes. Til dette bruger vi **Average Precision**-metrikker, som beregnes således:

1. Betragt Precision-Recall-kurven, der viser nøjagtigheden afhængigt af en detektionstærskelværdi (fra 0 til 1).
2. Afhængigt af tærsklen vil vi få flere eller færre objekter detekteret på billedet og forskellige værdier for præcision og recall.
3. Kurven vil se sådan ud:

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *Billede fra [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

Den gennemsnitlige præcision for en given klasse $C$ er arealet under denne kurve. Mere præcist opdeles Recall-aksen typisk i 10 dele, og Precision gennemsnittes over alle disse punkter:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP og IoU

Vi overvejer kun de detektioner, hvor IoU er over en vis værdi. For eksempel antages $\mbox{IoU Threshold} = 0.5$ typisk i PASCAL VOC-datasættet, mens AP i COCO måles for forskellige værdier af $\mbox{IoU Threshold}$.

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *Billede fra [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### Mean Average Precision - mAP

Den vigtigste metrik for objektgenkendelse kaldes **Mean Average Precision**, eller **mAP**. Det er værdien af Average Precision, gennemsnitligt over alle objektklasser og nogle gange også over $\mbox{IoU Threshold}$. Processen med at beregne **mAP** er beskrevet mere detaljeret
[i dette blogindlæg](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)), og også [her med kodeeksempler](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734).

## Forskellige tilgange til objektgenkendelse

Der er to brede klasser af algoritmer til objektgenkendelse:

* **Region Proposal Networks** (R-CNN, Fast R-CNN, Faster R-CNN). Hovedideen er at generere **Regions of Interests** (ROI) og køre CNN over dem for at finde maksimal aktivering. Det minder lidt om den naive tilgang, med undtagelse af at ROIs genereres på en mere intelligent måde. En af de største ulemper ved sådanne metoder er, at de er langsomme, fordi vi har brug for mange passeringer af CNN-klassifikatoren over billedet.
* **One-pass** (YOLO, SSD, RetinaNet) metoder. I disse arkitekturer designer vi netværket til at forudsige både klasser og ROIs i én passering.

### R-CNN: Region-Based CNN

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) bruger [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) til at generere en hierarkisk struktur af ROI-regioner, som derefter sendes gennem CNN-featureekstraktorer og SVM-klassifikatorer for at bestemme objektklassen og lineær regression for at bestemme *afgrænsningsboksens* koordinater. [Officiel artikel](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/rcnn1.cae407020dfb1d1fb572656e44f75cd6c512cc220591c116c506652c10e47f26.da.png)

> *Billede fra van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/rcnn2.2d9530bb83516484ec65b250c22dbf37d3d23244f32864ebcb91d98fe7c3112c.da.png)

> *Billeder fra [denne blog](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)

### F-RCNN - Fast R-CNN

Denne tilgang ligner R-CNN, men regioner defineres efter, at konvolutionslagene er blevet anvendt.

![FRCNN](../../../../../translated_images/f-rcnn.3cda6d9bb41888754037d2d9763e2298a96de5d9bc2a21db3147357aa5da9b1a.da.png)

> Billede fra [den officielle artikel](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

Hovedideen med denne tilgang er at bruge et neuralt netværk til at forudsige ROIs - den såkaldte *Region Proposal Network*. [Artikel](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../translated_images/faster-rcnn.8d46c099b87ef30ab2ea26dbc4bdd85b974a57ba8eb526f65dc4cd0a4711de30.da.png)

> Billede fra [den officielle artikel](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: Region-Based Fully Convolutional Network

Denne algoritme er endnu hurtigere end Faster R-CNN. Hovedideen er følgende:

1. Vi udtrækker features ved hjælp af ResNet-101.
2. Features behandles af **Position-Sensitive Score Map**. Hvert objekt fra $C$ klasser opdeles i $k\times k$ regioner, og vi træner til at forudsige dele af objekter.
3. For hver del fra $k\times k$ regioner stemmer alle netværk for objektklasser, og den objektklasse med flest stemmer vælges.

![r-fcn billede](../../../../../translated_images/r-fcn.13eb88158b99a3da50fa2787a6be5cb310d47f0e9655cc93a1090dc7aab338d1.da.png)

> Billede fra [officiel artikel](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO er en realtids én-pass algoritme. Hovedideen er følgende:

 * Billedet opdeles i $S\times S$ regioner.
 * For hver region forudsiger **CNN** $n$ mulige objekter, *afgrænsningsboksens* koordinater og *confidence*=*sandsynlighed* * IoU.

 ![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.da.png)

> Billede fra [officiel artikel](https://arxiv.org/abs/1506.02640)

### Andre algoritmer

* RetinaNet: [officiel artikel](https://arxiv.org/abs/1708.02002)
   - [PyTorch-implementering i Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Keras-implementering](https://github.com/fizyr/keras-retinanet)
   - [Objektgenkendelse med RetinaNet](https://keras.io/examples/vision/retinanet/) i Keras Samples
* SSD (Single Shot Detector): [officiel artikel](https://arxiv.org/abs/1512.02325)

## ✍️ Øvelser: Objektgenkendelse

Fortsæt din læring i følgende notebook:

[ObjectDetection.ipynb](ObjectDetection.ipynb)

## Konklusion

I denne lektion tog du en hurtig rundtur i de forskellige måder, hvorpå objektgenkendelse kan udføres!

## 🚀 Udfordring

Læs disse artikler og notebooks om YOLO og prøv dem selv:

* [Godt blogindlæg](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) om YOLO
 * [Officielt websted](https://pjreddie.com/darknet/yolo/)
 * Yolo: [Keras-implementering](https://github.com/experiencor/keras-yolo2), [step-by-step notebook](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [Keras-implementering](https://github.com/experiencor/keras-yolo2), [step-by-step notebook](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## Gennemgang & Selvstudie

* [Objektgenkendelse](https://tjmachinelearning.com/lectures/1718/obj/) af Nikhil Sardana
* [En god sammenligning af objektgenkendelsesalgoritmer](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Gennemgang af dyb læringsalgoritmer til objektgenkendelse](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [En trin-for-trin introduktion til de grundlæggende objektgenkendelsesalgoritmer](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implementering af Faster R-CNN i Python til objektgenkendelse](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Assignment: Object Detection](lab/README.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.