# Sinir Ağı Çerçeveleri

Zaten öğrendiğimiz gibi, sinir ağlarını verimli bir şekilde eğitebilmek için iki şey yapmamız gerekiyor:

* Tensörler üzerinde işlem yapmak, örneğin çarpma, toplama ve sigmoid veya softmax gibi bazı fonksiyonları hesaplama
* Tüm ifadelerin gradyanlarını hesaplamak, böylece gradyan inişi optimizasyonu gerçekleştirebilmek

## [Ön-ders sınavı](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/105)

`numpy` kütüphanesi ilk kısmı yapabilse de, gradyanları hesaplamak için bir mekanizmaya ihtiyacımız var. Önceki bölümde geliştirdiğimiz [çerçevemizde](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb), `backward` yönteminin içinde tüm türev fonksiyonlarını manuel olarak programlamak zorunda kaldık. İdeal olarak, bir çerçeve, tanımlayabileceğimiz *herhangi bir ifadenin* gradyanlarını hesaplama fırsatını bize vermelidir.

Başka önemli bir şey de GPU veya diğer özel hesaplama birimleri, örneğin [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit) üzerinde hesaplamalar yapabilmektir. Derin sinir ağı eğitimi *çok fazla* hesaplama gerektirir ve bu hesaplamaları GPU'larda paralelleştirebilmek çok önemlidir.

> ✅ 'Paralelleştirme' terimi, hesaplamaları birden fazla cihaz arasında dağıtmak anlamına gelir.

Şu anda, en popüler iki sinir ağı çerçevesi: [TensorFlow](http://TensorFlow.org) ve [PyTorch](https://pytorch.org/). Her ikisi de CPU ve GPU üzerinde tensörlerle çalışmak için düşük seviyeli bir API sağlar. Düşük seviyeli API'nin üstünde, sırasıyla [Keras](https://keras.io/) ve [PyTorch Lightning](https://pytorchlightning.ai/) adında daha yüksek seviyeli API'ler de bulunmaktadır.

Düşük Seviye API | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
-----------------|-------------------------------------|--------------------------------
Yüksek Seviye API | [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**Düşük seviye API'ler**, her iki çerçevede de **hesaplama grafikleri** adı verilen yapılar oluşturmanıza olanak tanır. Bu grafik, belirli giriş parametreleriyle çıktıyı (genellikle kayıp fonksiyonu) nasıl hesaplayacağınızı tanımlar ve mevcutsa GPU üzerinde hesaplama için itilebilir. Bu hesaplama grafiğini farklılaştırmak ve gradyanları hesaplamak için işlevler vardır; bu gradyanlar daha sonra model parametrelerini optimize etmek için kullanılabilir.

**Yüksek seviye API'ler**, sinir ağlarını **katmanlar dizisi** olarak düşünür ve çoğu sinir ağını inşa etmeyi çok daha kolay hale getirir. Modeli eğitmek genellikle verileri hazırlamayı ve ardından işi yapmak için `fit` fonksiyonunu çağırmayı gerektirir.

Yüksek seviye API, tipik sinir ağlarını çok hızlı bir şekilde inşa etmenize olanak tanır; birçok detay hakkında endişelenmenize gerek kalmaz. Aynı zamanda, düşük seviye API, eğitim süreci üzerinde çok daha fazla kontrol sağlar, bu nedenle yeni sinir ağı mimarileriyle çalışırken araştırmalarda sıklıkla kullanılır.

Her iki API'yi bir arada kullanabileceğinizi de anlamak önemlidir; örneğin, düşük seviye API kullanarak kendi ağ katmanı mimarinizi geliştirebilir ve ardından yüksek seviye API ile inşa edilen ve eğitilen daha büyük bir ağın içinde kullanabilirsiniz. Ya da yüksek seviye API'yi katmanlar dizisi olarak kullanarak bir ağ tanımlayabilir ve ardından optimizasyon yapmak için kendi düşük seviye eğitim döngünüzü kullanabilirsiniz. Her iki API de aynı temel kavramları kullanır ve birlikte iyi çalışacak şekilde tasarlanmıştır.

## Öğrenme

Bu kursta, içeriğin çoğunu hem PyTorch hem de TensorFlow için sunuyoruz. Tercih ettiğiniz çerçeveyi seçebilir ve yalnızca ilgili not defterlerini inceleyebilirsiniz. Hangi çerçeveyi seçeceğinizden emin değilseniz, **PyTorch ve TensorFlow** ile ilgili internette bazı tartışmaları okuyabilirsiniz. Daha iyi bir anlayış elde etmek için her iki çerçeveye de göz atabilirsiniz.

Mümkün olduğunda, basitlik için Yüksek Seviye API'leri kullanacağız. Ancak, sinir ağlarının nasıl çalıştığını en baştan anlamanın önemli olduğunu düşünüyoruz, bu nedenle başlangıçta düşük seviye API ve tensörlerle çalışmaya başlıyoruz. Ancak, hızlı bir şekilde ilerlemek istiyorsanız ve bu detayları öğrenmek için çok fazla zaman harcamak istemiyorsanız, bunları atlayabilir ve doğrudan yüksek seviye API not defterlerine geçebilirsiniz.

## ✍️ Alıştırmalar: Çerçeveler

Aşağıdaki not defterlerinde öğreniminize devam edin:

Düşük Seviye API | [TensorFlow+Keras Not Defteri](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [PyTorch](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)
-----------------|-------------------------------------|--------------------------------
Yüksek Seviye API | [Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) | *PyTorch Lightning*

Çerçeveleri öğrendikten sonra, aşırı uyum kavramını gözden geçirelim.

# Aşırı Uyum

Aşırı uyum, makine öğreniminde son derece önemli bir kavramdır ve doğru bir şekilde anlamak çok önemlidir!

Aşağıdaki 5 noktayı (aşağıdaki grafiklerde `x` ile temsil edilmiştir) yaklaşık olarak çözme sorununu düşünün:

![linear](../../../../../translated_images/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.tr.jpg) | ![overfit](../../../../../translated_images/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.tr.jpg)
-------------------------|--------------------------
**Doğrusal model, 2 parametre** | **Doğrusal olmayan model, 7 parametre**
Eğitim hatası = 5.3 | Eğitim hatası = 0
Doğrulama hatası = 5.1 | Doğrulama hatası = 20

* Solda, iyi bir doğru çizgi yaklaşık olarak görüyoruz. Parametre sayısı uygun olduğundan, model nokta dağılımının arkasındaki fikri doğru anlıyor.
* Sağda, model çok güçlü. Sadece 5 noktamız olduğu için ve modelin 7 parametresi olduğu için, tüm noktaların üzerinden geçecek şekilde ayarlanabilir, bu da eğitim hatasının 0 olmasına neden olur. Ancak, bu modelin verilerin arkasındaki doğru deseni anlamasını engeller, bu nedenle doğrulama hatası çok yüksektir.

Modelin zenginliği (parametre sayısı) ile eğitim örneklerinin sayısı arasında doğru bir denge kurmak çok önemlidir.

## Aşırı Uyumun Nedenleri

  * Yeterince eğitim verisi olmaması
  * Çok güçlü model
  * Giriş verilerinde fazla gürültü

## Aşırı Uyumun Tespit Edilmesi

Yukarıdaki grafikten görebileceğiniz gibi, aşırı uyum, çok düşük bir eğitim hatası ve yüksek bir doğrulama hatası ile tespit edilebilir. Genellikle eğitim sırasında hem eğitim hem de doğrulama hatalarının azalmaya başladığını görürüz, ve sonra bir noktada doğrulama hatası azalmayı durdurup artmaya başlayabilir. Bu, aşırı uyumun bir işareti olacak ve muhtemelen bu noktada eğitimi durdurmamız gerektiğini (veya en azından modelin bir anlık görüntüsünü almamız gerektiğini) gösterir.

![overfitting](../../../../../translated_images/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.tr.png)

## Aşırı Uyumun Önlenmesi

Aşırı uyumun meydana geldiğini görüyorsanız, aşağıdakilerden birini yapabilirsiniz:

 * Eğitim verisi miktarını artırın
 * Modelin karmaşıklığını azaltın
 * Daha sonra ele alacağımız [düzenleme tekniklerinden](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md) birini kullanın, örneğin [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout).

## Aşırı Uyum ve Bias-Variance Ticaret Dengesi

Aşırı uyum aslında istatistikte daha genel bir problem olan [Bias-Variance Tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff) durumudur. Modelimizdeki hata kaynaklarını dikkate aldığımızda, iki tür hata görebiliriz:

* **Bias hataları**, algoritmamızın eğitim verileri arasındaki ilişkiyi doğru bir şekilde yakalayamamasından kaynaklanır. Bu, modelimizin yeterince güçlü olmamasından kaynaklanabilir (**aşırı uyum**).
* **Variance hataları**, modelin gürültüyü verilerdeki anlamlı ilişki yerine yaklaşık olarak değerlendirmesinden kaynaklanır (**aşırı uyum**).

Eğitim sırasında, bias hatası azalır (modelimiz verileri yaklaşık olarak öğrenirken) ve variance hatası artar. Aşırı uyumu önlemek için eğitimi durdurmak önemlidir - ya manuel olarak (aşırı uyumu tespit ettiğimizde) ya da otomatik olarak (düzenleme yaparak).

## Sonuç

Bu derste, en popüler iki AI çerçevesi olan TensorFlow ve PyTorch için çeşitli API'ler arasındaki farkları öğrendiniz. Ayrıca, çok önemli bir konu olan aşırı uyumu da öğrendiniz.

## 🚀 Zorluk

Eşlik eden not defterlerinde, en altta 'görevler' bulacaksınız; not defterlerini inceleyin ve görevleri tamamlayın.

## [Ders sonrası sınav](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/205)

## Gözden Geçirme & Kendi Kendine Çalışma

Aşağıdaki konular hakkında biraz araştırma yapın:

- TensorFlow
- PyTorch
- Aşırı uyum

Kendinize şu soruları sorun:

- TensorFlow ve PyTorch arasındaki fark nedir?
- Aşırı uyum ve yetersiz uyum arasındaki fark nedir?

## [Ödev](lab/README.md)

Bu laboratuvar çalışmasında, PyTorch veya TensorFlow kullanarak tek ve çok katmanlı tam bağlı ağlar ile iki sınıflandırma problemini çözmeniz isteniyor.

* [Talimatlar](lab/README.md)
* [Not Defteri](../../../../../lessons/3-NeuralNetworks/05-Frameworks/lab/LabFrameworks.ipynb)

**Açıklama**:  
Bu belge, makine tabanlı AI çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluğa özen göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, ana dilinde, otoriter kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.