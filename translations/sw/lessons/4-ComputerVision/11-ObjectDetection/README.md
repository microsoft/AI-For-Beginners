### YOLO - Du Tittar Endast En Gång

YOLO är en realtids algoritm som körs i ett enda steg. Huvudidén är följande:

* Bilden delas upp i $S\times S$ regioner
* För varje region, **CNN** förutser $n$ möjliga objekt, *bounding box* koordinater och *confidence*=*sannolikhet* * IoU.

![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.sw.png)
> Bild från [officiellt papper](https://arxiv.org/abs/1506.02640)

### Andra Algoritmer

* RetinaNet: [officiellt papper](https://arxiv.org/abs/1708.02002)
   - [PyTorch-implementation i Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Keras-implementation](https://github.com/fizyr/keras-retinanet)
   - [Objektdetektering med RetinaNet](https://keras.io/examples/vision/retinanet/) i Keras-exempel
* SSD (Single Shot Detector): [officiellt papper](https://arxiv.org/abs/1512.02325)

## ✍️ Övningar: Objektdetektering

Fortsätt din inlärning i följande anteckningsbok:

[ObjectDetection.ipynb](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)

## Slutsats

I den här lektionen fick du en snabb genomgång av alla olika sätt som objektdetektering kan utföras på!

## 🚀 Utmaning

Läs igenom dessa artiklar och anteckningsböcker om YOLO och prova dem själv

* [Bra blogginlägg](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) som beskriver YOLO
 * [Officiell webbplats](https://pjreddie.com/darknet/yolo/)
 * Yolo: [Keras-implementation](https://github.com/experiencor/keras-yolo2), [steg-för-steg anteckningsbok](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [Keras-implementation](https://github.com/experiencor/keras-yolo2), [steg-för-steg anteckningsbok](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Efterföreläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## Granskning & Självstudier

* [Objektdetektering](https://tjmachinelearning.com/lectures/1718/obj/) av Nikhil Sardana
* [En bra jämförelse av algoritmer för objektdetektering](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Översyn av djupinlärningsalgoritmer för objektdetektering](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [En steg-för-steg introduktion till de grundläggande algoritmerna för objektdetektering](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implementering av Faster R-CNN i Python för objektdetektering](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Uppgift: Objektdetektering](lab/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.