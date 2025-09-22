<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b544f20b796402507fb05a0df893323",
  "translation_date": "2025-08-26T07:34:59+00:00",
  "source_file": "lessons/3-NeuralNetworks/05-Frameworks/README.md",
  "language_code": "tr"
}
-->
# Sinir Ağı Çerçeveleri

Daha önce öğrendiğimiz gibi, sinir ağlarını verimli bir şekilde eğitebilmek için iki şeyi yapmamız gerekiyor:

* Tensörler üzerinde işlem yapmak, örneğin çarpma, toplama ve sigmoid veya softmax gibi bazı fonksiyonları hesaplamak
* Tüm ifadelerin gradyanlarını hesaplamak, böylece gradyan inişi optimizasyonunu gerçekleştirebilmek

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ai/quiz/9)

`numpy` kütüphanesi ilk kısmı yapabilse de, gradyanları hesaplayacak bir mekanizmaya ihtiyacımız var. Önceki bölümde geliştirdiğimiz [kendi çerçevemizde](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb), tüm türev fonksiyonlarını `backward` metodunun içine manuel olarak programlamamız gerekiyordu. Bu yöntem geri yayılımı gerçekleştirir. İdeal olarak, bir çerçeve bize tanımlayabileceğimiz *herhangi bir ifadenin* gradyanlarını hesaplama fırsatı sunmalıdır.

Bir diğer önemli şey, GPU veya [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit) gibi diğer özel işlem birimlerinde hesaplama yapabilmektir. Derin sinir ağı eğitimi *çok fazla* hesaplama gerektirir ve bu hesaplamaları GPU'lar üzerinde paralelleştirebilmek oldukça önemlidir.

> ✅ 'Paralelleştirme' terimi, hesaplamaların birden fazla cihaz arasında dağıtılması anlamına gelir.

Şu anda en popüler iki sinir ağı çerçevesi: [TensorFlow](http://TensorFlow.org) ve [PyTorch](https://pytorch.org/). Her ikisi de CPU ve GPU üzerinde tensörlerle çalışmak için düşük seviyeli bir API sağlar. Düşük seviyeli API'nin yanı sıra, sırasıyla [Keras](https://keras.io/) ve [PyTorch Lightning](https://pytorchlightning.ai/) adı verilen yüksek seviyeli bir API de mevcuttur.

Düşük Seviyeli API | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
--------------------|-------------------------------------|--------------------------------
Yüksek Seviyeli API | [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**Düşük seviyeli API'ler**, her iki çerçevede de **hesaplama grafikleri** oluşturmanıza olanak tanır. Bu grafik, verilen giriş parametreleriyle çıktının (genellikle kayıp fonksiyonu) nasıl hesaplanacağını tanımlar ve GPU'da hesaplama için gönderilebilir. Bu hesaplama grafiğini türetmek ve gradyanları hesaplamak için fonksiyonlar vardır; bu gradyanlar daha sonra model parametrelerini optimize etmek için kullanılabilir.

**Yüksek seviyeli API'ler**, sinir ağlarını genellikle bir **katmanlar dizisi** olarak ele alır ve çoğu sinir ağını oluşturmayı çok daha kolay hale getirir. Modeli eğitmek genellikle verileri hazırlamayı ve ardından işi yapmak için bir `fit` fonksiyonu çağırmayı gerektirir.

Yüksek seviyeli API, tipik sinir ağlarını çok hızlı bir şekilde oluşturmanıza olanak tanır ve birçok ayrıntıyla uğraşmanıza gerek kalmaz. Aynı zamanda, düşük seviyeli API, eğitim süreci üzerinde çok daha fazla kontrol sağlar ve bu nedenle yeni sinir ağı mimarileriyle çalışırken araştırmalarda sıkça kullanılır.

Ayrıca, her iki API'yi birlikte kullanabileceğinizi anlamak önemlidir. Örneğin, düşük seviyeli API kullanarak kendi ağ katmanı mimarinizi geliştirebilir ve ardından bunu yüksek seviyeli API ile oluşturulan ve eğitilen daha büyük bir ağın içinde kullanabilirsiniz. Ya da katmanlar dizisi olarak yüksek seviyeli API kullanarak bir ağ tanımlayabilir ve ardından kendi düşük seviyeli eğitim döngünüzü kullanarak optimizasyon yapabilirsiniz. Her iki API de aynı temel kavramları kullanır ve birlikte iyi çalışacak şekilde tasarlanmıştır.

## Öğrenme

Bu kursta, içeriğin çoğunu hem PyTorch hem de TensorFlow için sunuyoruz. Tercih ettiğiniz çerçeveyi seçebilir ve yalnızca ilgili not defterlerini inceleyebilirsiniz. Hangi çerçeveyi seçeceğinizden emin değilseniz, **PyTorch vs. TensorFlow** hakkında internetteki bazı tartışmaları okuyabilirsiniz. Ayrıca, her iki çerçeveye de göz atarak daha iyi bir anlayış kazanabilirsiniz.

Mümkün olduğunda, basitlik için Yüksek Seviyeli API'leri kullanacağız. Ancak, sinir ağlarının temelden nasıl çalıştığını anlamanın önemli olduğuna inanıyoruz, bu nedenle başlangıçta düşük seviyeli API ve tensörlerle çalışmaya başlıyoruz. Ancak, hızlı bir şekilde başlamak ve bu ayrıntıları öğrenmek için fazla zaman harcamak istemiyorsanız, bunları atlayabilir ve doğrudan yüksek seviyeli API not defterlerine geçebilirsiniz.

## ✍️ Alıştırmalar: Çerçeveler

Öğreniminize aşağıdaki not defterlerinde devam edin:

Düşük Seviyeli API | [TensorFlow+Keras Not Defteri](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [PyTorch](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)
--------------------|-------------------------------------|--------------------------------
Yüksek Seviyeli API | [Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) | *PyTorch Lightning*

Çerçeveleri öğrendikten sonra, aşırı öğrenme (overfitting) kavramını tekrar gözden geçirelim.

# Aşırı Öğrenme

Aşırı öğrenme, makine öğreniminde son derece önemli bir kavramdır ve doğru bir şekilde anlaşılması çok önemlidir!

Aşağıdaki 5 noktayı (grafiklerde `x` ile gösterilen) yaklaşık olarak tahmin etme problemini düşünün:

![linear](../../../../../translated_images/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.tr.jpg) | ![overfit](../../../../../translated_images/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.tr.jpg)
-------------------------|--------------------------
**Doğrusal model, 2 parametre** | **Doğrusal olmayan model, 7 parametre**
Eğitim hatası = 5.3 | Eğitim hatası = 0
Doğrulama hatası = 5.1 | Doğrulama hatası = 20

* Solda, iyi bir doğru çizgisi yaklaşımı görüyoruz. Parametre sayısı yeterli olduğu için model, nokta dağılımının arkasındaki fikri doğru bir şekilde kavrıyor.
* Sağda, model çok güçlü. Sadece 5 noktamız olduğu ve modelin 7 parametresi olduğu için, tüm noktalardan geçecek şekilde ayarlanabiliyor ve bu da eğitim hatasını 0 yapıyor. Ancak, bu durum modelin verilerin arkasındaki doğru deseni anlamasını engelliyor ve bu nedenle doğrulama hatası çok yüksek oluyor.

Modelin zenginliği (parametre sayısı) ile eğitim örneklerinin sayısı arasında doğru bir denge kurmak çok önemlidir.

## Aşırı Öğrenme Neden Oluşur?

  * Yeterli eğitim verisinin olmaması
  * Çok güçlü bir model
  * Giriş verilerinde çok fazla gürültü

## Aşırı Öğrenme Nasıl Tespit Edilir?

Yukarıdaki grafikten de görebileceğiniz gibi, aşırı öğrenme çok düşük bir eğitim hatası ve yüksek bir doğrulama hatası ile tespit edilebilir. Normalde eğitim sırasında hem eğitim hem de doğrulama hatalarının azalmaya başladığını görürüz ve ardından bir noktada doğrulama hatası azalmayı durdurup artmaya başlayabilir. Bu, aşırı öğrenmenin bir işareti olacak ve eğitimi muhtemelen bu noktada durdurmamız gerektiğini (veya en azından modelin bir anlık görüntüsünü almamız gerektiğini) gösterecektir.

![overfitting](../../../../../translated_images/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.tr.png)

## Aşırı Öğrenme Nasıl Önlenir?

Aşırı öğrenmenin meydana geldiğini görüyorsanız, aşağıdakilerden birini yapabilirsiniz:

 * Eğitim verilerinin miktarını artırın
 * Modelin karmaşıklığını azaltın
 * [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout) gibi bazı [düzenleme tekniklerini](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md) kullanın. Bunları daha sonra ele alacağız.

## Aşırı Öğrenme ve Yanlılık-Varyans Dengesi

Aşırı öğrenme, aslında istatistikte [Yanlılık-Varyans Dengesi](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff) adı verilen daha genel bir problemin bir örneğidir. Modelimizdeki hata kaynaklarını düşündüğümüzde, iki tür hata görebiliriz:

* **Yanlılık hataları**, algoritmamızın eğitim verileri arasındaki ilişkiyi doğru bir şekilde yakalayamamasından kaynaklanır. Bu, modelimizin yeterince güçlü olmamasından (**eksik öğrenme**) kaynaklanabilir.
* **Varyans hataları**, modelin giriş verilerindeki gürültüyü anlamlı bir ilişki yerine yaklaşık olarak tahmin etmesinden kaynaklanır (**aşırı öğrenme**).

Eğitim sırasında, yanlılık hatası azalır (modelimiz verileri yaklaşık olarak öğrenir) ve varyans hatası artar. Aşırı öğrenmeyi önlemek için eğitimi - ya manuel olarak (aşırı öğrenmeyi tespit ettiğimizde) ya da otomatik olarak (düzenleme teknikleri kullanarak) - durdurmak önemlidir.

## Sonuç

Bu derste, iki en popüler yapay zeka çerçevesi olan TensorFlow ve PyTorch'un çeşitli API'leri arasındaki farkları öğrendiniz. Ayrıca, çok önemli bir konu olan aşırı öğrenme hakkında bilgi edindiniz.

## 🚀 Zorluk

Eşlik eden not defterlerinde, 'görevler' bölümünü bulacaksınız; not defterlerini inceleyin ve görevleri tamamlayın.

## [Ders Sonrası Test](https://ff-quizzes.netlify.app/en/ai/quiz/10)

## Gözden Geçirme ve Kendi Kendine Çalışma

Aşağıdaki konular hakkında biraz araştırma yapın:

- TensorFlow
- PyTorch
- Aşırı öğrenme

Kendinize şu soruları sorun:

- TensorFlow ve PyTorch arasındaki fark nedir?
- Aşırı öğrenme ve eksik öğrenme arasındaki fark nedir?

## [Ödev](lab/README.md)

Bu laboratuvarda, PyTorch veya TensorFlow kullanarak tek katmanlı ve çok katmanlı tam bağlantılı ağlarla iki sınıflandırma problemini çözmeniz isteniyor.

* [Talimatlar](lab/README.md)
* [Not Defteri](../../../../../lessons/3-NeuralNetworks/05-Frameworks/lab/LabFrameworks.ipynb)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.