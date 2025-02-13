# Nesne Tespiti

Şimdiye kadar ele aldığımız görüntü sınıflandırma modelleri, bir görüntü alır ve MNIST probleminde 'sayı' sınıfı gibi kategorik bir sonuç üretir. Ancak birçok durumda, bir resmin nesneleri tasvir ettiğini bilmekle yetinmek istemiyoruz - bu nesnelerin kesin konumunu belirleyebilme yeteneğine sahip olmak istiyoruz. İşte bu, **nesne tespiti**nin tam anlamıdır.

## [Ön-derse Quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/111)

![Nesne Tespiti](../../../../../translated_images/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be1b905373ed9c858102c054b16e4595c76ec3f7bba0feb549.tr.png)

> [YOLO v2 web sitesi](https://pjreddie.com/darknet/yolov2/) kaynaklı görüntü

## Nesne Tespiti için Naif Bir Yaklaşım

Bir resimde bir kediyi bulmak istediğimizi varsayalım, nesne tespiti için çok naif bir yaklaşım aşağıdaki gibi olacaktır:

1. Resmi bir dizi kareye böl
2. Her bir kare üzerinde görüntü sınıflandırması yap.
3. Yeterince yüksek aktivasyon sonucu veren kareler, söz konusu nesneyi içeriyor olarak kabul edilebilir.

![Naif Nesne Tespiti](../../../../../translated_images/naive-detection.e7f1ba220ccd08c68a2ea8e06a7ed75c3fcc738c2372f9e00b7f4299a8659c01.tr.png)

> *[Alıştırma Defteri](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection-TF.ipynb)* kaynağından görüntü

Ancak bu yaklaşım, algoritmanın nesnenin sınırlayıcı kutusunu oldukça belirsiz bir şekilde yerleştirmesine olanak tanıdığı için ideal değildir. Daha kesin bir konum için, sınırlayıcı kutuların koordinatlarını tahmin etmek üzere bir tür **regresyon** uygulamamız gerekiyor - ve bunun için belirli veri setlerine ihtiyacımız var.

## Nesne Tespiti için Regresyon

[Bu blog yazısı](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491), şekil tespiti için harika bir giriş sunmaktadır.

## Nesne Tespiti için Veri Setleri

Bu görev için aşağıdaki veri setleriyle karşılaşabilirsiniz:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 20 sınıf
* [COCO](http://cocodataset.org/#home) - Bağlamda Ortak Nesneler. 80 sınıf, sınırlayıcı kutular ve segmentasyon maskeleri

![COCO](../../../../../translated_images/coco-examples.71bc60380fa6cceb7caad48bd09e35b6028caabd363aa04fee89c414e0870e86.tr.jpg)

## Nesne Tespiti Metrikleri

### Kesim Üzerine Birlik

Görüntü sınıflandırması için algoritmanın ne kadar iyi performans gösterdiğini ölçmek kolaydır, ancak nesne tespiti için hem sınıfın doğruluğunu hem de çıkarılan sınırlayıcı kutu konumunun doğruluğunu ölçmemiz gerekiyor. İkincisi için, iki kutunun (veya iki rastgele alanın) ne kadar örtüştüğünü ölçen **Kesim Üzerine Birlik** (IoU) adı verilen bir ölçüm kullanıyoruz.

![IoU](../../../../../translated_images/iou_equation.9a4751d40fff4e119ecd0a7bcca4e71ab1dc83e0d4f2a0d66ff0859736f593cf.tr.png)

> *[Bu mükemmel IoU blog yazısının](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/) 2. Şeması*

Fikir basit - iki şekil arasındaki kesişim alanını, bu şekillerin birleşim alanına bölüyoruz. İki özdeş alan için, IoU 1 olurken, tamamen ayrı alanlar için 0 olur. Aksi takdirde, 0 ile 1 arasında değişecektir. Genellikle, IoU'nun belirli bir değerin üzerinde olduğu sınırlayıcı kutuları dikkate alıyoruz.

### Ortalama Doğruluk

Verilen bir nesne sınıfı $C$'nin ne kadar iyi tanındığını ölçmek istiyoruz. Bunu ölçmek için, **Ortalama Doğruluk** metriklerini kullanıyoruz, bu da aşağıdaki gibi hesaplanır:

1. Doğruluk eşiğine (0 ile 1 arasında) bağlı olarak doğruluk değerlerini gösteren Doğruluk-Hatırlama eğrisini dikkate al.
2. Eşeğe bağlı olarak, görüntüde daha fazla veya daha az nesne tespit edeceğiz ve farklı doğruluk ve hatırlama değerleri elde edeceğiz.
3. Eğri şu şekilde görünecek:

> *[NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)* kaynağından görüntü

Verilen bir sınıf $C$ için ortalama Doğruluk, bu eğrinin altındaki alandır. Daha kesin olarak, Hatırlama ekseni genellikle 10 parçaya bölünür ve Doğruluk tüm bu noktalar üzerinde ortalanır:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Doğruluk}(\mbox{Hatırlama}={i\over10})
$$

### AP ve IoU

Sadece IoU'nun belirli bir değerin üzerinde olduğu tespitleri dikkate alacağız. Örneğin, PASCAL VOC veri setinde genellikle $\mbox{IoU Eşiği} = 0.5$ varsayılırken, COCO'da AP farklı $\mbox{IoU Eşiği}$ değerleri için ölçülmektedir. 

### Ortalama Ortalama Doğruluk - mAP

Nesne Tespiti için ana metrik **Ortalama Ortalama Doğruluk** veya **mAP** olarak adlandırılır. Bu, Tüm nesne sınıfları üzerinden ortalama alınmış Ortalama Doğruluk değeridir ve bazen de $\mbox{IoU Eşiği}$ üzerinden ortalama alınır. **mAP** hesaplama süreci daha ayrıntılı olarak [bu blog yazısında](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3) ve [burada kod örnekleri ile](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734) açıklanmaktadır.

## Farklı Nesne Tespiti Yaklaşımları

Nesne tespiti algoritmalarının iki geniş sınıfı vardır:

* **Bölge Teklif Ağları** (R-CNN, Fast R-CNN, Faster R-CNN). Ana fikir, **İlgi Alanları** (ROI) üretmek ve bunlar üzerinde maksimum aktivasyon aramak için CNN çalıştırmaktır. Bu, naif yaklaşıma biraz benziyor, tek fark, ROI'lerin daha akıllı bir şekilde üretilmesidir. Bu tür yöntemlerin en büyük dezavantajlarından biri, görüntü üzerinde CNN sınıflandırıcısının birçok geçişini gerektirdiği için yavaş olmalarıdır.
* **Tek geçiş** (YOLO, SSD, RetinaNet) yöntemleri. Bu mimarilerde, ağı hem sınıfları hem de ROI'leri tek bir geçişte tahmin edecek şekilde tasarlıyoruz.

### R-CNN: Bölge Tabanlı CNN

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf), ROI bölgelerinin hiyerarşik yapısını oluşturmak için [Seçici Arama](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) kullanır, bu bölgeler daha sonra CNN özellik çıkarıcıları ve SVM sınıflandırıcıları üzerinden geçirilerek nesne sınıfı belirlenir ve *sınırlayıcı kutu* koordinatlarını belirlemek için doğrusal regresyon uygulanır. [Resmi Makale](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/rcnn1.cae407020dfb1d1fb572656e44f75cd6c512cc220591c116c506652c10e47f26.tr.png)

> *van de Sande et al. ICCV’11 kaynağından görüntü*

![RCNN-1](../../../../../translated_images/rcnn2.2d9530bb83516484ec65b250c22dbf37d3d23244f32864ebcb91d98fe7c3112c.tr.png)

> *[Bu blog](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e) kaynağından görüntü*

### F-RCNN - Hızlı R-CNN

Bu yaklaşım R-CNN ile benzerdir, ancak bölgeler, konvolüsyon katmanları uygulandıktan sonra tanımlanır.

![FRCNN](../../../../../translated_images/f-rcnn.3cda6d9bb41888754037d2d9763e2298a96de5d9bc2a21db3147357aa5da9b1a.tr.png)

> Resim [Resmi Makale](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Daha Hızlı R-CNN

Bu yaklaşımın ana fikri, ROI'leri tahmin etmek için bir sinir ağı kullanmaktır - bu, *Bölge Teklif Ağı* olarak adlandırılır. [Makale](https://arxiv.org/pdf/1506.01497.pdf), 2016

![Daha HızlıRCNN](../../../../../translated_images/faster-rcnn.8d46c099b87ef30ab2ea26dbc4bdd85b974a57ba8eb526f65dc4cd0a4711de30.tr.png)

> Resim [resmi makaleden](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: Bölge Tabanlı Tam Konvolüsyonel Ağ

Bu algoritma, Daha Hızlı R-CNN'den bile daha hızlıdır. Ana fikir aşağıdaki gibidir:

1. Özellikler ResNet-101 kullanılarak çıkarılır.
2. Özellikler **Pozisyon-Duyarlı Skor Haritası** tarafından işlenir. $C$ sınıflarındaki her nesne $k\times k$ bölgeye ayrılır ve nesnelerin parçalarını tahmin etmek için eğitim yapılır.
3. $k\times k$ bölgelerden her bir parça için tüm ağlar nesne sınıfları için oy kullanır ve maksimum oy alan nesne sınıfı seçilir.

![r-fcn görüntüsü](../../../../../translated_images/r-fcn.13eb88158b99a3da50fa2787a6be5cb310d47f0e9655cc93a1090dc7aab338d1.tr.png)

> Resim [resmi makaleden](https://arxiv.org/abs/1605.06409)

### YOLO - Bir Kez Bakarsınız

YOLO, gerçek zamanlı bir tek geçiş algoritmasıdır. Ana fikir aşağıdaki gibidir:

 * Görüntü $S\times S$ bölgelere bölünür.
 * Her bölge için, **CNN** $n$ olası nesneyi, *sınırlayıcı kutu* koordinatlarını ve *güven* = *olasılık* * IoU'yu tahmin eder.

 ![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.tr.png)
> [Resmi makale](https://arxiv.org/abs/1506.02640) kaynağından görüntü

### Diğer Algoritmalar

* RetinaNet: [resmi makale](https://arxiv.org/abs/1708.02002)
   - [Torchvision'da PyTorch Uygulaması](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Keras Uygulaması](https://github.com/fizyr/keras-retinanet)
   - Keras Örneklerinde [RetinaNet ile Nesne Tespiti](https://keras.io/examples/vision/retinanet/)
* SSD (Tek Atış Dedektörü): [resmi makale](https://arxiv.org/abs/1512.02325)

## ✍️ Alıştırmalar: Nesne Tespiti

Aşağıdaki not defterinde öğreniminize devam edin:

[ObjectDetection.ipynb](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)

## Sonuç

Bu derste, nesne tespitinin gerçekleştirilebileceği çeşitli yolları hızlı bir şekilde keşfettiniz!

## 🚀 Zorluk

Bu makaleleri ve not defterlerini okuyun, YOLO hakkında bilgi edinin ve kendiniz deneyin.

* YOLO'yu tanımlayan [iyi bir blog yazısı](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/)
 * [Resmi site](https://pjreddie.com/darknet/yolo/)
 * Yolo: [Keras uygulaması](https://github.com/experiencor/keras-yolo2), [adım adım not defteri](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [Keras uygulaması](https://github.com/experiencor/keras-yolo2), [adım adım not defteri](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Ders sonrası sınav](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## Gözden Geçirme & Kendi Kendine Çalışma

* Nikhil Sardana tarafından [Nesne Tespiti](https://tjmachinelearning.com/lectures/1718/obj/)
* [Nesne tespit algoritmalarının iyi bir karşılaştırması](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Nesne Tespiti için Derin Öğrenme Algoritmalarının Gözden Geçirilmesi](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [Temel Nesne Tespit Algoritmalarına Adım Adım Giriş](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Nesne Tespiti için Python'da Daha Hızlı R-CNN Uygulaması](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Görev: Nesne Tespiti](lab/README.md)

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde otoriter kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanılması sonucunda ortaya çıkan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.