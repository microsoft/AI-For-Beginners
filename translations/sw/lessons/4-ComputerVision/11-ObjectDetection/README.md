<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d85c8b08f6d1b48fd7f35b99f93c1138",
  "translation_date": "2025-08-25T20:54:25+00:00",
  "source_file": "lessons/4-ComputerVision/11-ObjectDetection/README.md",
  "language_code": "sw"
}
-->
# Utambuzi wa Vitu

Mifano ya uainishaji wa picha tuliyoshughulikia hadi sasa ilichukua picha na kutoa matokeo ya kategoria, kama darasa 'nambari' katika tatizo la MNIST. Hata hivyo, katika hali nyingi hatutaki tu kujua kwamba picha inaonyesha vitu - tunataka kuweza kubaini eneo lao halisi. Hili ndilo hasa lengo la **utambuzi wa vitu**.

## [Maswali ya awali ya somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/111)

![Utambuzi wa Vitu](../../../../../translated_images/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be1b905373ed9c858102c054b16e4595c76ec3f7bba0feb549.sw.png)

> Picha kutoka [tovuti ya YOLO v2](https://pjreddie.com/darknet/yolov2/)

## Njia Rahisi ya Utambuzi wa Vitu

Tukichukulia tunataka kutafuta paka kwenye picha, njia rahisi ya utambuzi wa vitu inaweza kuwa kama ifuatavyo:

1. Gawanya picha katika vigae kadhaa.
2. Endesha uainishaji wa picha kwenye kila kigae.
3. Vigae vile vinavyotoa matokeo ya juu vya kutosha vinaweza kuchukuliwa kuwa na kitu kinachotafutwa.

![Utambuzi Rahisi wa Vitu](../../../../../translated_images/naive-detection.e7f1ba220ccd08c68a2ea8e06a7ed75c3fcc738c2372f9e00b7f4299a8659c01.sw.png)

> *Picha kutoka [Exercise Notebook](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection-TF.ipynb)*

Hata hivyo, njia hii si bora, kwa sababu inaruhusu tu algoriti kubaini kisanduku cha mipaka ya kitu kwa usahihi mdogo. Kwa usahihi zaidi wa eneo, tunahitaji kuendesha aina fulani ya **urekebishaji** ili kutabiri viwianishi vya visanduku vya mipaka - na kwa hilo, tunahitaji seti maalum za data.

## Urekebishaji kwa Utambuzi wa Vitu

[Chapisho hili la blogu](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491) lina utangulizi mzuri wa kutambua maumbo.

## Seti za Data kwa Utambuzi wa Vitu

Unaweza kukutana na seti zifuatazo za data kwa kazi hii:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - Darasa 20
* [COCO](http://cocodataset.org/#home) - Vitu vya Kawaida katika Muktadha. Darasa 80, visanduku vya mipaka na maski za kugawanya.

![COCO](../../../../../translated_images/coco-examples.71bc60380fa6cceb7caad48bd09e35b6028caabd363aa04fee89c414e0870e86.sw.jpg)

## Vipimo vya Utambuzi wa Vitu

### Muingiliano juu ya Muungano

Wakati wa uainishaji wa picha ni rahisi kupima jinsi algoriti inavyofanya kazi, kwa utambuzi wa vitu tunahitaji kupima usahihi wa darasa, pamoja na usahihi wa eneo la kisanduku cha mipaka kilichotabiriwa. Kwa hili la mwisho, tunatumia kipimo kinachoitwa **Muingiliano juu ya Muungano** (IoU), ambacho hupima jinsi visanduku viwili (au maeneo mawili ya kiholela) vinavyofanana.

![IoU](../../../../../translated_images/iou_equation.9a4751d40fff4e119ecd0a7bcca4e71ab1dc83e0d4f2a0d66ff0859736f593cf.sw.png)

> *Kielelezo cha 2 kutoka [blogu bora kuhusu IoU](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

Wazo ni rahisi - tunagawanya eneo la muingiliano kati ya maumbo mawili kwa eneo la muungano wao. Kwa maeneo mawili yanayofanana kabisa, IoU itakuwa 1, wakati kwa maeneo yasiyogusana kabisa itakuwa 0. Vinginevyo, itatofautiana kutoka 0 hadi 1. Kwa kawaida tunazingatia tu visanduku vya mipaka ambavyo IoU yake iko juu ya thamani fulani.

### Usahihi wa Wastani

Tukichukulia tunataka kupima jinsi darasa fulani la vitu $C$ linavyotambuliwa. Ili kupima hili, tunatumia kipimo cha **Usahihi wa Wastani**, ambacho huhesabiwa kama ifuatavyo:

1. Fikiria Mchoro wa Usahihi-Kumbukumbu unaonyesha usahihi kulingana na thamani ya kizingiti cha utambuzi (kutoka 0 hadi 1).
2. Kulingana na kizingiti, tutapata vitu vingi au vichache vilivyotambuliwa kwenye picha, na thamani tofauti za usahihi na kumbukumbu.
3. Mchoro utaonekana kama huu:

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *Picha kutoka [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

Usahihi wa Wastani kwa darasa fulani $C$ ni eneo chini ya mchoro huu. Kwa usahihi zaidi, mhimili wa Kumbukumbu kwa kawaida hugawanywa katika sehemu 10, na Usahihi huhesabiwa wastani kwa alama zote hizo:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP na IoU

Tutazingatia tu utambuzi ule, ambao IoU yake iko juu ya thamani fulani. Kwa mfano, katika seti ya data ya PASCAL VOC kwa kawaida $\mbox{IoU Threshold} = 0.5$ inachukuliwa, wakati katika COCO AP hupimwa kwa thamani tofauti za $\mbox{IoU Threshold}$.

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *Picha kutoka [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### Usahihi wa Wastani wa Kawaida - mAP

Kipimo kikuu cha Utambuzi wa Vitu kinaitwa **Usahihi wa Wastani wa Kawaida**, au **mAP**. Ni thamani ya Usahihi wa Wastani, wastani kwa darasa zote za vitu, na wakati mwingine pia kwa $\mbox{IoU Threshold}$. Kwa undani zaidi, mchakato wa kuhesabu **mAP** umeelezewa
[katika blogu hii](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)), na pia [hapa na sampuli za msimbo](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734).

## Njia Tofauti za Utambuzi wa Vitu

Kuna makundi mawili makuu ya algoriti za utambuzi wa vitu:

* **Mitandao ya Mapendekezo ya Eneo** (R-CNN, Fast R-CNN, Faster R-CNN). Wazo kuu ni kuunda **Maeneo ya Maslahi** (ROI) na kuendesha CNN juu yao, kutafuta uamsho wa juu zaidi. Ni kidogo kama njia rahisi, isipokuwa kwamba ROI zinatengenezwa kwa njia ya busara zaidi. Mojawapo ya mapungufu makubwa ya mbinu hizi ni kwamba ni polepole, kwa sababu tunahitaji kupitisha mara nyingi kipanga darasa cha CNN juu ya picha.
* **Njia ya kupita moja** (YOLO, SSD, RetinaNet). Katika usanifu huu tunabuni mtandao kutabiri darasa na ROI kwa kupita moja.

### R-CNN: CNN Inayotegemea Eneo

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) hutumia [Utafutaji wa Kuchagua](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) kuunda muundo wa kihierarkia wa maeneo ya ROI, ambayo kisha hupitishwa kupitia vipanga sifa vya CNN na vipanga darasa vya SVM ili kubaini darasa la kitu, na urekebishaji wa mstari ili kubaini viwianishi vya *kisanduku cha mipaka*. [Karatasi Rasmi](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/rcnn1.cae407020dfb1d1fb572656e44f75cd6c512cc220591c116c506652c10e47f26.sw.png)

> *Picha kutoka van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/rcnn2.2d9530bb83516484ec65b250c22dbf37d3d23244f32864ebcb91d98fe7c3112c.sw.png)

> *Picha kutoka [blogu hii](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)

### F-RCNN - R-CNN ya Haraka

Mbinu hii ni sawa na R-CNN, lakini maeneo yanabainishwa baada ya tabaka za convolution kutumika.

![FRCNN](../../../../../translated_images/f-rcnn.3cda6d9bb41888754037d2d9763e2298a96de5d9bc2a21db3147357aa5da9b1a.sw.png)

> Picha kutoka [Karatasi Rasmi](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

Wazo kuu la mbinu hii ni kutumia mtandao wa neva kutabiri ROI - kinachoitwa *Mtandao wa Mapendekezo ya Eneo*. [Karatasi](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../translated_images/faster-rcnn.8d46c099b87ef30ab2ea26dbc4bdd85b974a57ba8eb526f65dc4cd0a4711de30.sw.png)

> Picha kutoka [karatasi rasmi](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: Mtandao wa Kikamilifu wa Convolutional Inayotegemea Eneo

Algoriti hii ni ya haraka zaidi kuliko Faster R-CNN. Wazo kuu ni kama ifuatavyo:

1. Tunatoa sifa kwa kutumia ResNet-101.
2. Sifa zinachakatwa na **Ramani ya Alama ya Kifaa cha Nafasi**. Kila kitu kutoka darasa $C$ hugawanywa na $k\times k$ maeneo, na tunafundisha kutabiri sehemu za vitu.
3. Kwa kila sehemu kutoka $k\times k$ maeneo mitandao yote hupiga kura kwa darasa la vitu, na darasa la kitu lenye kura nyingi zaidi huchaguliwa.

![r-fcn image](../../../../../translated_images/r-fcn.13eb88158b99a3da50fa2787a6be5cb310d47f0e9655cc93a1090dc7aab338d1.sw.png)

> Picha kutoka [karatasi rasmi](https://arxiv.org/abs/1605.06409)

### YOLO - Unatazama Mara Moja Tu

YOLO ni algoriti ya wakati halisi ya kupita moja. Wazo kuu ni kama ifuatavyo:

 * Picha inagawanywa katika $S\times S$ maeneo.
 * Kwa kila eneo, **CNN** inatabiri $n$ vitu vinavyowezekana, viwianishi vya *kisanduku cha mipaka* na *uhakika*=*uwezekano* * IoU.

 ![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.sw.png)

> Picha kutoka [karatasi rasmi](https://arxiv.org/abs/1506.02640)

### Algoriti Nyingine

* RetinaNet: [karatasi rasmi](https://arxiv.org/abs/1708.02002)
   - [Utekelezaji wa PyTorch katika Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Utekelezaji wa Keras](https://github.com/fizyr/keras-retinanet)
   - [Utambuzi wa Vitu na RetinaNet](https://keras.io/examples/vision/retinanet/) katika Sampuli za Keras
* SSD (Single Shot Detector): [karatasi rasmi](https://arxiv.org/abs/1512.02325)

## ✍️ Mazoezi: Utambuzi wa Vitu

Endelea kujifunza katika daftari lifuatalo:

[ObjectDetection.ipynb](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)

## Hitimisho

Katika somo hili umechukua ziara ya haraka ya njia mbalimbali za kutekeleza utambuzi wa vitu!

## 🚀 Changamoto

Soma makala na daftari hizi kuhusu YOLO na ujaribu mwenyewe:

* [Blogu nzuri](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) inayofafanua YOLO.
 * [Tovuti rasmi](https://pjreddie.com/darknet/yolo/)
 * Yolo: [Utekelezaji wa Keras](https://github.com/experiencor/keras-yolo2), [daftari la hatua kwa hatua](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [Utekelezaji wa Keras](https://github.com/experiencor/keras-yolo2), [daftari la hatua kwa hatua](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Maswali ya baada ya somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## Mapitio na Kujisomea

* [Utambuzi wa Vitu](https://tjmachinelearning.com/lectures/1718/obj/) na Nikhil Sardana
* [Ulinganisho mzuri wa algoriti za utambuzi wa vitu](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Mapitio ya Algoriti za Kujifunza Kina kwa Utambuzi wa Vitu](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [Utangulizi wa Hatua kwa Hatua wa Algoriti za Msingi za Utambuzi wa Vitu](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Utekelezaji wa Faster R-CNN katika Python kwa Utambuzi wa Vitu](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Kazi: Utambuzi wa Vitu](lab/README.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.