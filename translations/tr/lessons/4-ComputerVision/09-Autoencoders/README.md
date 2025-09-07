<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-26T07:25:14+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "tr"
}
-->
# Otomatik Kodlayıcılar (Autoencoders)

CNN'leri (Convolutional Neural Networks) eğitirken karşılaşılan sorunlardan biri, çok fazla etiketlenmiş veriye ihtiyaç duymamızdır. Görüntü sınıflandırma durumunda, görüntüleri farklı sınıflara ayırmamız gerekir ve bu manuel bir çabadır.

## [Ders Öncesi Testi](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/109)

Ancak, CNN özellik çıkarıcılarını eğitmek için ham (etiketlenmemiş) verileri kullanmak isteyebiliriz; bu, **kendinden denetimli öğrenme** (self-supervised learning) olarak adlandırılır. Etiketler yerine, eğitim görüntülerini hem ağ girişi hem de çıkışı olarak kullanacağız. **Otomatik kodlayıcı** (autoencoder) fikrinin temelinde, bir **kodlayıcı ağ** (encoder network) ile giriş görüntüsünü bir **gizli uzaya** (latent space) dönüştürmek (genellikle daha küçük boyutlu bir vektördür) ve ardından **kod çözücü ağ** (decoder network) ile orijinal görüntüyü yeniden oluşturmak yer alır.

> ✅ Bir [otomatik kodlayıcı](https://wikipedia.org/wiki/Autoencoder), "etiketlenmemiş verilerin verimli kodlamalarını öğrenmek için kullanılan bir yapay sinir ağı türüdür."

Otomatik kodlayıcıyı, orijinal görüntüden mümkün olduğunca fazla bilgi yakalamak ve doğru bir şekilde yeniden oluşturmak için eğittiğimizden, ağ, giriş görüntülerinin anlamını yakalamak için en iyi **gömülü temsili** (embedding) bulmaya çalışır.

![AutoEncoder Şeması](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.tr.jpg)

> Görsel: [Keras blog](https://blog.keras.io/building-autoencoders-in-keras.html)

## Otomatik Kodlayıcıların Kullanım Senaryoları

Orijinal görüntüleri yeniden oluşturmak kendi başına çok faydalı görünmese de, otomatik kodlayıcıların özellikle faydalı olduğu birkaç senaryo vardır:

* **Görüntülerin boyutunu düşürmek** veya **görüntü gömülü temsilleri eğitmek**. Otomatik kodlayıcılar genellikle PCA'dan daha iyi sonuçlar verir, çünkü görüntülerin mekansal doğasını ve hiyerarşik özelliklerini dikkate alır.
* **Gürültü giderme**, yani görüntüden gürültüyü kaldırma. Gürültü genellikle çok fazla gereksiz bilgi taşır, bu nedenle otomatik kodlayıcı, nispeten küçük bir gizli uzaya tüm bu bilgiyi sığdıramaz ve yalnızca görüntünün önemli kısmını yakalar. Gürültü gidericileri eğitirken, orijinal görüntülerle başlarız ve otomatik kodlayıcıya giriş olarak yapay olarak eklenmiş gürültü içeren görüntüleri kullanırız.
* **Süper çözünürlük**, görüntü çözünürlüğünü artırma. Yüksek çözünürlüklü görüntülerle başlarız ve otomatik kodlayıcıya giriş olarak daha düşük çözünürlüklü görüntüyü kullanırız.
* **Üretici modeller**. Otomatik kodlayıcıyı eğittikten sonra, kod çözücü kısmı rastgele gizli vektörlerden başlayarak yeni nesneler oluşturmak için kullanılabilir.

## Varyasyonel Otomatik Kodlayıcılar (VAE)

Geleneksel otomatik kodlayıcılar, giriş verilerinin boyutunu bir şekilde azaltır ve giriş görüntülerinin önemli özelliklerini belirler. Ancak, gizli vektörler genellikle çok anlamlı değildir. Örneğin, MNIST veri setini ele alırsak, farklı gizli vektörlerin hangi rakamlara karşılık geldiğini anlamak kolay değildir, çünkü yakın gizli vektörler mutlaka aynı rakamlara karşılık gelmez.

Öte yandan, *üretici* modelleri eğitmek için gizli uzayı anlamak daha iyidir. Bu fikir bizi **varyasyonel otomatik kodlayıcı**ya (VAE) götürür.

VAE, gizli parametrelerin *istatistiksel dağılımını* (latent distribution) tahmin etmeyi öğrenen bir otomatik kodlayıcıdır. Örneğin, gizli vektörlerin belirli bir ortalama z<sub>mean</sub> ve standart sapma z<sub>sigma</sub> (her ikisi de belirli bir boyut d'ye sahip vektörlerdir) ile normal olarak dağıtılmasını isteyebiliriz. VAE'deki kodlayıcı bu parametreleri tahmin etmeyi öğrenir ve ardından kod çözücü, bu dağılımdan rastgele bir vektör alarak nesneyi yeniden oluşturur.

Özetle:

* Giriş vektöründen, `z_mean` ve `z_log_sigma` tahmin edilir (standart sapmanın kendisini tahmin etmek yerine, logaritması tahmin edilir).
* `sample` adlı bir vektör, N(z<sub>mean</sub>,exp(z<sub>log_sigma</sub>)) dağılımından örneklenir.
* Kod çözücü, `sample` vektörünü giriş olarak kullanarak orijinal görüntüyü yeniden oluşturmaya çalışır.

<img src="images/vae.png" width="50%">

> Görsel: [Bu blog yazısı](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) - Isaak Dykeman

Varyasyonel otomatik kodlayıcılar, iki bölümden oluşan karmaşık bir kayıp fonksiyonu kullanır:

* **Yeniden yapılandırma kaybı** (Reconstruction loss), yeniden oluşturulan görüntünün hedefe ne kadar yakın olduğunu gösteren kayıp fonksiyonudur (örneğin, Ortalama Kare Hatası - MSE). Bu, normal otomatik kodlayıcılardaki kayıp fonksiyonuyla aynıdır.
* **KL kaybı**, gizli değişken dağılımlarının normal dağılıma yakın kalmasını sağlar. Bu, iki istatistiksel dağılımın ne kadar benzer olduğunu tahmin etmek için kullanılan [Kullback-Leibler sapması](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) kavramına dayanır.

VAEs'in önemli bir avantajı, yeni görüntüleri nispeten kolay bir şekilde oluşturabilmemize olanak tanımasıdır, çünkü hangi dağılımdan gizli vektörlerin örneklenmesi gerektiğini biliriz. Örneğin, MNIST üzerinde 2D gizli vektörle bir VAE eğitirsek, gizli vektörün bileşenlerini değiştirerek farklı rakamlar elde edebiliriz:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Görsel: [Dmitry Soshnikov](http://soshnikov.com)

Gizli parametre uzayının farklı bölümlerinden gizli vektörler almaya başladıkça, görüntülerin birbirine nasıl karıştığını gözlemleyin. Bu uzayı ayrıca 2D olarak görselleştirebiliriz:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Görsel: [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Egzersizler: Otomatik Kodlayıcılar

Otomatik kodlayıcılar hakkında daha fazla bilgi edinmek için şu not defterlerini inceleyin:

* [TensorFlow'da Otomatik Kodlayıcılar](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [PyTorch'ta Otomatik Kodlayıcılar](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Otomatik Kodlayıcıların Özellikleri

* **Veriye Özgü** - yalnızca eğitildikleri görüntü türleriyle iyi çalışırlar. Örneğin, bir süper çözünürlük ağı çiçekler üzerinde eğitilirse, portrelerde iyi çalışmaz. Bunun nedeni, ağın daha yüksek çözünürlüklü bir görüntü üretebilmek için eğitim veri setinden öğrendiği ince detayları kullanmasıdır.
* **Kayıplı** - yeniden oluşturulan görüntü, orijinal görüntüyle aynı değildir. Kayıp türü, eğitim sırasında kullanılan *kayıp fonksiyonu* ile tanımlanır.
* **Etiketlenmemiş veri** üzerinde çalışır.

## [Ders Sonrası Testi](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/209)

## Sonuç

Bu derste, bir AI bilim insanının kullanabileceği çeşitli otomatik kodlayıcı türlerini öğrendiniz. Bunları nasıl inşa edeceğinizi ve görüntüleri yeniden oluşturmak için nasıl kullanacağınızı öğrendiniz. Ayrıca VAE'yi ve yeni görüntüler oluşturmak için nasıl kullanılacağını öğrendiniz.

## 🚀 Meydan Okuma

Bu derste, görüntüler için otomatik kodlayıcıların kullanımını öğrendiniz. Ancak, bunlar müzik için de kullanılabilir! Magenta projesinin [MusicVAE](https://magenta.tensorflow.org/music-vae) projesine göz atın; bu proje, müziği yeniden oluşturmayı öğrenmek için otomatik kodlayıcıları kullanır. Bu kütüphane ile bazı [deneyler](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) yaparak neler yaratabileceğinizi görün.

## [Ders Sonrası Testi](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## İnceleme ve Kendi Kendine Çalışma

Referans için, otomatik kodlayıcılar hakkında daha fazla bilgi edinmek için şu kaynakları okuyun:

* [Keras'ta Otomatik Kodlayıcılar İnşa Etmek](https://blog.keras.io/building-autoencoders-in-keras.html)
* [NeuroHive'daki Blog Yazısı](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Varyasyonel Otomatik Kodlayıcılar Açıklaması](https://kvfrans.com/variational-autoencoders-explained/)
* [Koşullu Varyasyonel Otomatik Kodlayıcılar](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Ödev

[TensorFlow kullanarak bu not defterinin](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb) sonunda bir 'görev' bulacaksınız - bunu ödeviniz olarak kullanın.

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama durumunda sorumluluk kabul edilmez.