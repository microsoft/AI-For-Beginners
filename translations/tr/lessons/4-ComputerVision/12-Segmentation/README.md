<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-26T07:25:49+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "tr"
}
-->
# Segmentasyon

Daha önce, nesneleri *bounding box* tahminiyle görüntüde bulmamızı sağlayan Nesne Tespiti hakkında bilgi edinmiştik. Ancak, bazı görevlerde yalnızca bounding box'lara değil, daha hassas nesne konumlandırmasına da ihtiyaç duyarız. Bu göreve **segmentasyon** denir.

## [Ders Öncesi Test](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

Segmentasyon, **piksel sınıflandırması** olarak görülebilir; burada görüntünün **her bir** pikseli için sınıfını tahmin etmemiz gerekir (*arka plan* da sınıflardan biri olarak kabul edilir). İki ana segmentasyon algoritması vardır:

* **Semantik segmentasyon**, yalnızca piksel sınıfını belirtir ve aynı sınıfa ait farklı nesneler arasında ayrım yapmaz.
* **Örnek segmentasyonu**, sınıfları farklı örneklere ayırır.

Örneğin, örnek segmentasyon için bu koyunlar farklı nesneler olarak kabul edilir, ancak semantik segmentasyon için tüm koyunlar tek bir sınıf olarak temsil edilir.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Görsel [bu blog yazısından](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50) alınmıştır.

Segmentasyon için farklı sinir ağı mimarileri vardır, ancak hepsi aynı yapıya sahiptir. Bir bakıma, daha önce öğrendiğiniz otomatik kodlayıcıya (autoencoder) benzer, ancak burada amacımız orijinal görüntüyü yeniden oluşturmak yerine bir **maske**yi yeniden oluşturmaktır. Bu nedenle, bir segmentasyon ağı şu parçalardan oluşur:

* **Kodlayıcı (Encoder)** giriş görüntüsünden özellikler çıkarır.
* **Kod Çözücü (Decoder)** bu özellikleri, sınıf sayısına karşılık gelen kanal sayısı ve aynı boyutta bir **maske görüntüsüne** dönüştürür.

<img src="images/segm.png" width="80%">

> Görsel [bu yayından](https://arxiv.org/pdf/2001.05566.pdf) alınmıştır.

Segmentasyon için kullanılan kayıp fonksiyonundan özellikle bahsetmeliyiz. Klasik otomatik kodlayıcılar kullanıldığında, iki görüntü arasındaki benzerliği ölçmemiz gerekir ve bunu yapmak için ortalama kare hatası (MSE) kullanılabilir. Segmentasyonda, hedef maske görüntüsündeki her piksel sınıf numarasını (üçüncü boyut boyunca tekil kodlama ile) temsil eder, bu nedenle sınıflandırma için özel kayıp fonksiyonları kullanmamız gerekir - tüm pikseller üzerinde ortalaması alınan çapraz entropi kaybı. Eğer maske ikili ise - **ikili çapraz entropi kaybı** (BCE) kullanılır.

> ✅ Tekil kodlama, bir sınıf etiketini, sınıf sayısına eşit uzunlukta bir vektöre kodlamanın bir yoludur. Bu teknik hakkında daha fazla bilgi için [bu makaleye](https://datagy.io/sklearn-one-hot-encode/) göz atın.

## Tıbbi Görüntüleme için Segmentasyon

Bu derste, tıbbi görüntülerde insan nevüslerini (benler olarak da bilinir) tanımak için ağı eğiterek segmentasyonu uygulamada göreceğiz. Görüntü kaynağı olarak <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> Veritabanı</a>'nı kullanacağız. Bu veri seti, üç sınıfa ait 200 görüntü içerir: tipik nevüs, atipik nevüs ve melanom. Tüm görüntüler ayrıca nevüsü çevreleyen bir **maske** içerir.

> ✅ Bu teknik özellikle bu tür tıbbi görüntüleme için uygundur, ancak başka hangi gerçek dünya uygulamalarını hayal edebilirsiniz?

<img alt="navi" src="images/navi.png"/>

> Görsel PH<sup>2</sup> Veritabanından alınmıştır.

Modelimizi, herhangi bir nevüsü arka plandan ayırmak için eğiteceğiz.

## ✍️ Alıştırmalar: Semantik Segmentasyon

Aşağıdaki defterleri açarak farklı semantik segmentasyon mimarileri hakkında daha fazla bilgi edinin, bunlarla çalışmayı pratik yapın ve bunları uygulamada görün.

* [Semantik Segmentasyon Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Semantik Segmentasyon TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Ders Sonrası Test](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Sonuç

Segmentasyon, görüntü sınıflandırması için çok güçlü bir tekniktir ve bounding box'lardan piksel düzeyinde sınıflandırmaya geçiş yapar. Bu teknik, tıbbi görüntüleme gibi birçok uygulamada kullanılır.

## 🚀 Zorluk

Vücut segmentasyonu, insan görüntüleriyle yapabileceğimiz yaygın görevlerden sadece biridir. Diğer önemli görevler arasında **iskelet tespiti** ve **poz tespiti** bulunur. [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) kütüphanesini deneyerek poz tespitinin nasıl kullanılabileceğini görün.

## İnceleme ve Kendi Kendine Çalışma

Bu [Vikipedi makalesi](https://wikipedia.org/wiki/Image_segmentation), bu tekniğin çeşitli uygulamaları hakkında iyi bir genel bakış sunar. Bu alandaki Örnek segmentasyonu ve Panoptik segmentasyon alt alanları hakkında kendi başınıza daha fazla bilgi edinin.

## [Ödev](lab/README.md)

Bu laboratuvarda, Kaggle'dan [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) kullanarak **insan vücudu segmentasyonu** yapmayı deneyin.

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.