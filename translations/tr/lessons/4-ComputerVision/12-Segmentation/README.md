# Segmentasyon

Daha önce, nesne tespiti hakkında öğrendik; bu, görüntüdeki nesneleri *sınırlayıcı kutularını* tahmin ederek yerlerini belirlememizi sağlar. Ancak bazı görevler için yalnızca sınırlayıcı kutulara değil, aynı zamanda daha hassas nesne konumlandırmasına da ihtiyacımız var. Bu görev **segmentasyon** olarak adlandırılır.

## [Ders öncesi quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

Segmentasyon, **piksel sınıflandırması** olarak görülebilir; burada görüntünün **her** pikseli için sınıfını tahmin etmemiz gerekir (*arka plan* sınıflardan biridir). İki ana segmentasyon algoritması vardır:

* **Anlamsal segmentasyon**, yalnızca piksel sınıfını belirtir ve aynı sınıftaki farklı nesneler arasında ayrım yapmaz.
* **Örnek segmentasyonu**, sınıfları farklı örneklere böler.

Örnek segmentasyonunda, bu koyunlar farklı nesnelerken, anlamsal segmentasyonda tüm koyunlar tek bir sınıf olarak temsil edilir.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Resim [bu blog yazısından](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50) alınmıştır.

Segmentasyon için farklı sinir mimarileri bulunmaktadır, ancak hepsi aynı yapıya sahiptir. Bir bakıma, daha önce öğrendiğiniz otomatik kodlayıcıya benzer; ancak amacımız orijinal görüntüyü parçalamak yerine bir **maske** parçalamaktır. Bu nedenle, bir segmentasyon ağı aşağıdaki parçalara sahiptir:

* **Kodlayıcı**, giriş görüntüsünden özellikleri çıkarır.
* **Çözücü**, bu özellikleri **maske görüntüsüne** dönüştürür; bu maske, sınıf sayısına karşılık gelen aynı boyut ve kanal sayısına sahiptir.

<img src="images/segm.png" width="80%">

> Resim [bu yayından](https://arxiv.org/pdf/2001.05566.pdf) alınmıştır.

Segmentasyon için kullanılan kayıp fonksiyonunu özellikle belirtmeliyiz. Klasik otomatik kodlayıcılar kullanıldığında, iki görüntü arasındaki benzerliği ölçmemiz gerekir ve bunu yapmak için ortalama kare hatasını (MSE) kullanabiliriz. Segmentasyonda, hedef maske görüntüsündeki her piksel sınıf numarasını temsil eder (üçüncü boyutta one-hot kodlanmış), bu nedenle sınıflandırma için özel kayıp fonksiyonları kullanmalıyız - tüm pikseller üzerinde ortalaması alınan çapraz entropi kaybı. Maske ikili olduğunda - **ikili çapraz entropi kaybı** (BCE) kullanılır.

> ✅ One-hot kodlama, bir sınıf etiketini sınıf sayısına eşit uzunlukta bir vektöre kodlama yöntemidir. Bu teknik hakkında daha fazla bilgi için [bu makaleye](https://datagy.io/sklearn-one-hot-encode/) göz atın.

## Tıbbi Görüntüleme için Segmentasyon

Bu derste, ağı insan nevuslarını (benler olarak da bilinir) tıbbi görüntülerde tanımak için eğiterek segmentasyonun nasıl çalıştığını göreceğiz. Görüntü kaynağı olarak <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> Veritabanı</a> dermoskopi görüntülerini kullanacağız. Bu veri seti, tipik nevus, atipik nevus ve melanom olmak üzere üç sınıftan 200 görüntü içermektedir. Tüm görüntüler, nevusu belirten bir **maske** ile birlikte gelir.

> ✅ Bu teknik, bu tür tıbbi görüntüleme için özellikle uygundur, ancak başka hangi gerçek dünya uygulamalarını hayal edebilirsiniz?

<img alt="navi" src="images/navi.png"/>

> Resim PH<sup>2</sup> Veritabanından alınmıştır.

Herhangi bir nevusu arka plandan ayırmak için bir model eğiteceğiz.

## ✍️ Alıştırmalar: Anlamsal Segmentasyon

Aşağıdaki not defterlerini açarak farklı anlamsal segmentasyon mimarileri hakkında daha fazla bilgi edinin, onlarla çalışmayı pratik edin ve bunları eylemde görün.

* [Anlamsal Segmentasyon Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Anlamsal Segmentasyon TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Ders sonrası quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Sonuç

Segmentasyon, görüntü sınıflandırması için çok güçlü bir tekniktir; sınırlayıcı kutuların ötesine geçerek piksel düzeyinde sınıflandırma yapar. Bu teknik, tıbbi görüntüleme gibi çeşitli uygulamalarda kullanılmaktadır.

## 🚀 Zorluk

Vücut segmentasyonu, insan görüntüleriyle yapabileceğimiz yaygın görevlerden yalnızca biridir. Diğer önemli görevler arasında **iskelet tespiti** ve **poz tespiti** bulunmaktadır. Poz tespitinin nasıl kullanılabileceğini görmek için [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) kütüphanesini deneyin.

## Gözden Geçirme & Kendi Kendine Çalışma

Bu [wikipedia makalesi](https://wikipedia.org/wiki/Image_segmentation), bu tekniğin çeşitli uygulamaları hakkında iyi bir genel bakış sunmaktadır. Bu araştırma alanında Örnek segmentasyonu ve Panoptik segmentasyonun alt alanları hakkında kendi başınıza daha fazla bilgi edinin.

## [Görev](lab/README.md)

Bu laboratuvar çalışmasında, Kaggle'dan [Segmentasyon Tam Vücut MADS Veri Seti](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) kullanarak **insan vücudu segmentasyonu** yapmayı deneyin.

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluğa özen göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde otoriter kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanılması sonucu ortaya çıkan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.