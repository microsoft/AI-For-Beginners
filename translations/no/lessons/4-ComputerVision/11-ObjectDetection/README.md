# Objektgjenkjenning

Bildklassifiseringsmodellene vi har jobbet med så langt tar et bilde og gir et kategorisk resultat, som klassen 'nummer' i et MNIST-problem. Men i mange tilfeller ønsker vi ikke bare å vite at et bilde viser objekter – vi vil også kunne bestemme deres nøyaktige plassering. Dette er nettopp poenget med **objektgjenkjenning**.

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/21)

![Objektgjenkjenning](../../../../../translated_images/no/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be.webp)

> Bilde fra [YOLO v2 nettside](https://pjreddie.com/darknet/yolov2/)

## En naiv tilnærming til objektgjenkjenning

Anta at vi ønsket å finne en katt på et bilde. En veldig naiv tilnærming til objektgjenkjenning ville være følgende:

1. Del opp bildet i et antall fliser.
2. Kjør bildklassifisering på hver flis.
3. De flisene som gir tilstrekkelig høy aktivering kan anses å inneholde det aktuelle objektet.

![Naiv objektgjenkjenning](../../../../../translated_images/no/naive-detection.e7f1ba220ccd08c6.webp)

> *Bilde fra [Øvingsnotatbok](ObjectDetection-TF.ipynb)*

Denne tilnærmingen er imidlertid langt fra ideell, fordi den bare lar algoritmen lokalisere objektets avgrensningsboks veldig unøyaktig. For mer presis lokalisering må vi kjøre en form for **regresjon** for å forutsi koordinatene til avgrensningsboksene – og for det trenger vi spesifikke datasett.

## Regresjon for objektgjenkjenning

[Dette blogginnlegget](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491) gir en flott og enkel introduksjon til å oppdage former.

## Datasett for objektgjenkjenning

Du kan komme over følgende datasett for denne oppgaven:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) – 20 klasser
* [COCO](http://cocodataset.org/#home) – Common Objects in Context. 80 klasser, avgrensningsbokser og segmenteringsmasker

![COCO](../../../../../translated_images/no/coco-examples.71bc60380fa6cceb.webp)

## Objektgjenkjenningsmetrikker

### Intersection over Union

Mens det er enkelt å måle hvor godt algoritmen presterer for bildklassifisering, må vi for objektgjenkjenning måle både korrektheten av klassen og presisjonen til den utledede plasseringen av avgrensningsboksen. For sistnevnte bruker vi den såkalte **Intersection over Union** (IoU), som måler hvor godt to bokser (eller to vilkårlige områder) overlapper.

![IoU](../../../../../translated_images/no/iou_equation.9a4751d40fff4e11.webp)

> *Figur 2 fra [dette utmerkede blogginnlegget om IoU](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

Ideen er enkel – vi deler området for overlapp mellom to figurer med området for deres union. For to identiske områder vil IoU være 1, mens for helt adskilte områder vil det være 0. Ellers vil det variere fra 0 til 1. Vi vurderer vanligvis bare de avgrensningsboksene der IoU er over en viss verdi.

### Gjennomsnittlig presisjon

Anta at vi ønsker å måle hvor godt en gitt klasse av objekter $C$ blir gjenkjent. For å måle dette bruker vi **Gjennomsnittlig presisjon**-metrikker, som beregnes slik:

1. Vurder presisjon-recall-kurven som viser nøyaktigheten avhengig av en deteksjonsterskelverdi (fra 0 til 1).
2. Avhengig av terskelen vil vi få flere eller færre objekter oppdaget i bildet, og ulike verdier for presisjon og recall.
3. Kurven vil se slik ut:

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *Bilde fra [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

Gjennomsnittlig presisjon for en gitt klasse $C$ er området under denne kurven. Mer presist deles recall-aksen vanligvis inn i 10 deler, og presisjonen gjennomsnittliggjøres over alle disse punktene:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP og IoU

Vi vurderer kun de deteksjonene der IoU er over en viss verdi. For eksempel, i PASCAL VOC-datasettet antas vanligvis $\mbox{IoU Threshold} = 0.5$, mens i COCO måles AP for ulike verdier av $\mbox{IoU Threshold}$.

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *Bilde fra [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### Gjennomsnittlig presisjon – mAP

Hovedmetrikken for objektgjenkjenning kalles **Gjennomsnittlig presisjon**, eller **mAP**. Det er verdien av gjennomsnittlig presisjon, gjennomsnittlig over alle objektklasser, og noen ganger også over $\mbox{IoU Threshold}$. Prosessen for å beregne **mAP** er beskrevet i detalj
[i dette blogginnlegget](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)), og også [her med kodeeksempler](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734).

## Ulike tilnærminger til objektgjenkjenning

Det finnes to brede klasser av algoritmer for objektgjenkjenning:

* **Region Proposal Networks** (R-CNN, Fast R-CNN, Faster R-CNN). Hovedideen er å generere **Regions of Interests** (ROI) og kjøre CNN over dem, på jakt etter maksimal aktivering. Det ligner litt på den naive tilnærmingen, med unntak av at ROI-er genereres på en mer intelligent måte. En av de største ulempene med slike metoder er at de er trege, fordi vi trenger mange passeringer av CNN-klassifiseringen over bildet.
* **One-pass** (YOLO, SSD, RetinaNet)-metoder. I disse arkitekturene designer vi nettverket til å forutsi både klasser og ROI-er i én passering.

### R-CNN: Region-Based CNN

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) bruker [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) for å generere en hierarkisk struktur av ROI-regioner, som deretter sendes gjennom CNN-funksjonsekstraktorer og SVM-klassifisatorer for å bestemme objektklassen, og lineær regresjon for å bestemme *avgrensningsboks*-koordinater. [Offisiell artikkel](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/no/rcnn1.cae407020dfb1d1f.webp)

> *Bilde fra van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/no/rcnn2.2d9530bb83516484.webp)

> *Bilder fra [denne bloggen](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN – Fast R-CNN

Denne tilnærmingen ligner på R-CNN, men regioner defineres etter at konvolusjonslagene er blitt brukt.

![FRCNN](../../../../../translated_images/no/f-rcnn.3cda6d9bb4188875.webp)

> Bilde fra [den offisielle artikkelen](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

Hovedideen med denne tilnærmingen er å bruke et nevralt nettverk til å forutsi ROI-er – såkalte *Region Proposal Network*. [Artikkel](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../translated_images/no/faster-rcnn.8d46c099b87ef30a.webp)

> Bilde fra [den offisielle artikkelen](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: Region-Based Fully Convolutional Network

Denne algoritmen er enda raskere enn Faster R-CNN. Hovedideen er følgende:

1. Vi henter ut funksjoner ved hjelp av ResNet-101.
2. Funksjonene behandles av **Position-Sensitive Score Map**. Hvert objekt fra $C$ klasser deles inn i $k\times k$ regioner, og vi trener på å forutsi deler av objekter.
3. For hver del fra $k\times k$ regioner stemmer alle nettverkene på objektklasser, og objektklassen med flest stemmer blir valgt.

![r-fcn bilde](../../../../../translated_images/no/r-fcn.13eb88158b99a3da.webp)

> Bilde fra [offisiell artikkel](https://arxiv.org/abs/1605.06409)

### YOLO – You Only Look Once

YOLO er en sanntids én-pass-algoritme. Hovedideen er følgende:

 * Bildet deles inn i $S\times S$ regioner.
 * For hver region forutsier **CNN** $n$ mulige objekter, *avgrensningsboks*-koordinater og *confidence*=*sannsynlighet* * IoU.

 ![YOLO](../../../../../translated_images/no/yolo.a2648ec82ee8bb4e.webp)

> Bilde fra [offisiell artikkel](https://arxiv.org/abs/1506.02640)

### Andre algoritmer

* RetinaNet: [offisiell artikkel](https://arxiv.org/abs/1708.02002)
   - [PyTorch-implementasjon i Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Keras-implementasjon](https://github.com/fizyr/keras-retinanet)
   - [Objektgjenkjenning med RetinaNet](https://keras.io/examples/vision/retinanet/) i Keras-eksempler
* SSD (Single Shot Detector): [offisiell artikkel](https://arxiv.org/abs/1512.02325)

## ✍️ Øvelser: Objektgjenkjenning

Fortsett læringen i følgende notatbok:

[ObjectDetection.ipynb](ObjectDetection.ipynb)

## Konklusjon

I denne leksjonen tok du en rask gjennomgang av alle de ulike måtene objektgjenkjenning kan utføres på!

## 🚀 Utfordring

Les gjennom disse artiklene og notatbøkene om YOLO og prøv dem selv:

* [Godt blogginnlegg](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) som beskriver YOLO
 * [Offisiell nettside](https://pjreddie.com/darknet/yolo/)
 * Yolo: [Keras-implementasjon](https://github.com/experiencor/keras-yolo2), [steg-for-steg-notatbok](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [Keras-implementasjon](https://github.com/experiencor/keras-yolo2), [steg-for-steg-notatbok](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/22)

## Gjennomgang og selvstudium

* [Objektgjenkjenning](https://tjmachinelearning.com/lectures/1718/obj/) av Nikhil Sardana
* [En god sammenligning av algoritmer for objektgjenkjenning](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Gjennomgang av dyp læringsalgoritmer for objektgjenkjenning](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [En steg-for-steg introduksjon til grunnleggende algoritmer for objektgjenkjenning](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implementering av Faster R-CNN i Python for objektgjenkjenning](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Oppgave: Objektgjenkjenning](lab/README.md)

---

