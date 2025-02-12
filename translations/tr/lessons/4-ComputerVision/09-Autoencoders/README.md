# Otomatik Kodlayıcılar

CNN'leri eğitirken, karşılaştığımız sorunlardan biri çok fazla etiketli veriye ihtiyaç duymamızdır. Görüntü sınıflandırması durumunda, görüntüleri farklı sınıflara ayırmamız gerekir ki bu da manuel bir çabadır.

## [Ön ders sınavı](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/109)

Ancak, CNN özellik çıkarıcılarını eğitmek için ham (etiketsiz) verileri kullanmak isteyebiliriz ki buna **kendinden denetimli öğrenme** denir. Etiketler yerine, eğitim görüntülerini hem ağ girişi hem de çıkışı olarak kullanacağız. **Otomatik kodlayıcı**nın ana fikri, girdi görüntüsünü bazı **gizli alanlara** (genellikle daha küçük boyutlu bir vektör) dönüştüren bir **kodlayıcı ağı**na sahip olmamızdır; ardından orijinal görüntüyü yeniden oluşturmayı amaçlayan **çözücü ağı** gelir.

> ✅ Bir [otomatik kodlayıcı](https://wikipedia.org/wiki/Autoencoder), "etiketsiz verilerin verimli kodlamalarını öğrenmek için kullanılan bir tür yapay sinir ağıdır."

Otomatik kodlayıcıyı, orijinal görüntüden mümkün olduğunca fazla bilgiyi yakalamak için eğittiğimiz için, ağ girdi görüntülerinin anlamını yakalamak için en iyi **gömülü alanı** bulmaya çalışır.

![Otomatik Kodlayıcı Diyagramı](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.tr.jpg)

> Görsel [Keras blogu](https://blog.keras.io/building-autoencoders-in-keras.html) kaynağındandır.

## Otomatik Kodlayıcıların Kullanım Senaryoları

Orijinal görüntüleri yeniden oluşturmanın kendi başına faydalı görünmemesi bir yana, otomatik kodlayıcıların özellikle yararlı olduğu birkaç senaryo vardır:

* **Görüntülerin boyutunu düşürmek için görselleştirme** veya **görüntü gömülü alanları eğitimi**. Genellikle otomatik kodlayıcılar, PCA'dan daha iyi sonuçlar verir çünkü görüntülerin mekansal doğasını ve hiyerarşik özelliklerini dikkate alır.
* **Gürültü azaltma**, yani görüntüden gürültüyü kaldırma. Çünkü gürültü birçok gereksiz bilgi taşır, otomatik kodlayıcı bunu nispeten küçük gizli alana sığdıramaz ve dolayısıyla yalnızca görüntünün önemli kısmını yakalar. Gürültü gidericileri eğitirken, orijinal görüntülerle başlarız ve otomatik kodlayıcı için girdi olarak yapay olarak eklenmiş gürültü içeren görüntüleri kullanırız.
* **Süper çözünürlük**, görüntü çözünürlüğünü artırma. Yüksek çözünürlüklü görüntülerle başlarız ve daha düşük çözünürlüklü görüntüyü otomatik kodlayıcı girişi olarak kullanırız.
* **Üretken modeller**. Otomatik kodlayıcıyı eğittikten sonra, çözücü kısmı rastgele gizli vektörlerden yeni nesneler oluşturmak için kullanılabilir.

## Varyasyonel Otomatik Kodlayıcılar (VAE)

Geleneksel otomatik kodlayıcılar, girdi verilerinin boyutunu bir şekilde azaltarak, girdi görüntülerinin önemli özelliklerini belirler. Ancak, gizli vektörler genellikle pek anlam ifade etmez. Başka bir deyişle, MNIST veri setini örnek alırsak, farklı gizli vektörlerin hangi rakamlara karşılık geldiğini bulmak kolay bir iş değildir, çünkü yakın gizli vektörler aynı rakamlara karşılık gelmeyebilir.

Diğer yandan, *üretken* modelleri eğitmek için gizli alanı anlamak daha iyidir. Bu fikir bizi **varyasyonel otomatik kodlayıcı** (VAE) kavramına götürür.

VAE, gizli parametrelerin *istatistiksel dağılımını* tahmin etmeyi öğrenen bir otomatik kodlayıcıdır, buna **gizli dağılım** denir. Örneğin, gizli vektörlerin belirli bir ortalama z<sub>mean</sub> ve standart sapma z<sub>sigma</sub> ile normal dağılıma sahip olmasını isteyebiliriz (hem ortalama hem de standart sapma belirli bir boyut d'ye sahip vektörlerdir). VAE'deki kodlayıcı bu parametreleri tahmin etmeyi öğrenir ve ardından çözücü, nesneyi yeniden oluşturmak için bu dağılımdan rastgele bir vektör alır.

Özetlemek gerekirse:

* Girdi vektöründen `z_mean` ve `z_log_sigma` tahmin ediyoruz (standart sapmayı tahmin etmek yerine, onun logaritmasını tahmin ediyoruz)
* Dağılımdan N(z<sub>mean</sub>,exp(z<sub>log_sigma</sub>)) dağılımından bir vektör `sample` örnekliyoruz
* Çözücü, `sample`'yi girdi vektörü olarak kullanarak orijinal görüntüyü çözmeye çalışır

 <img src="images/vae.png" width="50%">

> Görsel [bu blog yazısından](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) Isaak Dykeman'a aittir.

Varyasyonel otomatik kodlayıcılar, iki bölümden oluşan karmaşık bir kayıp fonksiyonu kullanır:

* **Yeniden yapılandırma kaybı**, yeniden oluşturulan bir görüntünün hedefe ne kadar yakın olduğunu gösteren kayıp fonksiyonudur (Bu, Ortalama Kare Hatası veya MSE olabilir). Bu, normal otomatik kodlayıcılardaki kayıp fonksiyonu ile aynıdır.
* **KL kaybı**, gizli değişken dağılımlarının normal dağılıma yakın kalmasını sağlar. Bu, iki istatistiksel dağılımın ne kadar benzer olduğunu tahmin etmek için kullanılan [Kullback-Leibler sapması](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) kavramına dayanır.

VAE'lerin önemli bir avantajı, yeni görüntüler oluşturmayı nispeten kolaylaştırmalarıdır çünkü gizli vektörleri örneklemek için hangi dağılımdan yararlanacağımızı biliyoruz. Örneğin, MNIST üzerinde 2D gizli vektörle VAE eğitimi yaptığımızda, farklı rakamlar elde etmek için gizli vektörün bileşenlerini değiştirebiliriz:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Görsel [Dmitry Soshnikov](http://soshnikov.com) tarafından sağlanmıştır.

Gizli parametre alanının farklı kısımlarından gizli vektörler almaya başladığımızda, görüntülerin birbirine nasıl karıştığını gözlemleyin. Bu alanı 2D olarak da görselleştirebiliriz:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Görsel [Dmitry Soshnikov](http://soshnikov.com) tarafından sağlanmıştır.

## ✍️ Alıştırmalar: Otomatik Kodlayıcılar

Otomatik kodlayıcılar hakkında daha fazla bilgi edinmek için ilgili not defterlerini inceleyin:

* [TensorFlow'da Otomatik Kodlayıcılar](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [PyTorch'ta Otomatik Kodlayıcılar](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Otomatik Kodlayıcıların Özellikleri

* **Veri Spesifik** - yalnızca eğitildikleri görüntü türleriyle iyi çalışırlar. Örneğin, çiçekler üzerinde süper çözünürlük ağı eğitirsek, portreler üzerinde iyi çalışmaz. Bunun nedeni, ağın eğitim veri setinden öğrenilen özelliklerden ince detaylar alarak daha yüksek çözünürlüklü görüntü üretebilmesidir.
* **Kaybı** - yeniden oluşturulan görüntü, orijinal görüntüyle aynı değildir. Kayıp doğası, eğitim sırasında kullanılan *kayıp fonksiyonu* tarafından tanımlanır.
* **Etiketsiz veriler** üzerinde çalışır.

## [Ders sonrası sınav](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/209)

## Sonuç

Bu derste, AI bilimcisine sunulan çeşitli otomatik kodlayıcı türlerini öğrendiniz. Onları nasıl inşa edeceğinizi ve görüntüleri nasıl yeniden oluşturmak için kullanacağınızı öğrendiniz. Ayrıca VAE'yi ve yeni görüntüler oluşturmak için nasıl kullanacağınızı öğrendiniz.

## 🚀 Meydan Okuma

Bu derste, otomatik kodlayıcıların görüntüler için nasıl kullanıldığını öğrendiniz. Ancak müzik için de kullanılabilirler! Otomatik kodlayıcıları müziği yeniden yapılandırmayı öğrenmek için kullanan Magenta projesinin [MusicVAE](https://magenta.tensorflow.org/music-vae) projesine göz atın. Ne yaratabileceğinizi görmek için bu kütüphane ile bazı [deneyler](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) yapın.

## [Ders sonrası sınav](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Gözden Geçirme & Kendi Kendine Çalışma

Otomatik kodlayıcılar hakkında daha fazla bilgi için bu kaynakları okuyun:

* [Keras'da Otomatik Kodlayıcılar İnşası](https://blog.keras.io/building-autoencoders-in-keras.html)
* [NeuroHive'daki Blog Yazısı](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Varyasyonel Otomatik Kodlayıcılar Açıklaması](https://kvfrans.com/variational-autoencoders-explained/)
* [Koşullu Varyasyonel Otomatik Kodlayıcılar](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Görev

[TensorFlow kullanan bu not defterinin](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersTF.ipynb) sonunda bir 'görev' bulacaksınız - bunu ödev olarak kullanın.

**Açıklama**:  
Bu belge, makine tabanlı AI çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlış anlamalar içerebileceğini lütfen dikkate alın. Orijinal belge, kendi dilinde otorite kaynağı olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımı sonucu ortaya çıkan yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.