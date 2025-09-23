<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-26T07:34:19+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "tr"
}
-->
# Sinir Ağlarına Giriş. Çok Katmanlı Algılayıcı

Önceki bölümde, en basit sinir ağı modeli olan tek katmanlı algılayıcıyı, iki sınıflı doğrusal sınıflandırma modelini öğrendiniz.

Bu bölümde, bu modeli daha esnek bir çerçeveye genişleteceğiz ve böylece:

* **Çok sınıflı sınıflandırma** yapabilmenin yanı sıra iki sınıflı sınıflandırma yapabiliriz
* Sınıflandırmanın yanı sıra **regresyon problemlerini** çözebiliriz
* Doğrusal olarak ayrılabilir olmayan sınıfları ayırabiliriz

Ayrıca, farklı sinir ağı mimarileri oluşturabilmemizi sağlayacak kendi modüler Python çerçevemizi geliştireceğiz.

## [Ders Öncesi Testi](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Makine Öğreniminin Formalizasyonu

Makine Öğrenimi problemini formalize ederek başlayalım. Diyelim ki **X** eğitim veri setimiz ve **Y** etiketlerimiz var ve en doğru tahminleri yapacak bir model *f* oluşturmalıyız. Tahminlerin kalitesi **Kayıp Fonksiyonu** ℒ ile ölçülür. Sıkça kullanılan kayıp fonksiyonları şunlardır:

* Regresyon problemleri için, bir sayı tahmin etmemiz gerektiğinde, **mutlak hata** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| veya **kare hata** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup> kullanabiliriz.
* Sınıflandırma için, **0-1 kaybı** (temelde modelin **doğruluğu** ile aynıdır) veya **lojistik kayıp** kullanırız.

Tek katmanlı algılayıcı için, *f* fonksiyonu doğrusal bir fonksiyon olarak tanımlanmıştı: *f(x)=wx+b* (burada *w* ağırlık matrisi, *x* giriş özelliklerinin vektörü ve *b* önyargı vektörüdür). Farklı sinir ağı mimarileri için, bu fonksiyon daha karmaşık bir form alabilir.

> Sınıflandırma durumunda, ağ çıktısı olarak ilgili sınıfların olasılıklarını elde etmek genellikle arzu edilir. Rastgele sayıları olasılıklara dönüştürmek (örneğin çıktıyı normalleştirmek) için genellikle **softmax** fonksiyonu σ kullanılır ve *f* fonksiyonu *f(x)=σ(wx+b)* olur.

Yukarıdaki *f* tanımında, *w* ve *b* **parametreler** olarak adlandırılır: θ=⟨*w,b*⟩. Veri seti ⟨**X**,**Y**⟩ verildiğinde, tüm veri setindeki genel hatayı parametreler θ'nin bir fonksiyonu olarak hesaplayabiliriz.

> ✅ **Sinir ağı eğitiminin amacı, parametreler θ'yi değiştirerek hatayı minimize etmektir.**

## Gradyan İnişi Optimizasyonu

**Gradyan inişi** adı verilen iyi bilinen bir fonksiyon optimizasyon yöntemi vardır. Fikir, kayıp fonksiyonunun parametrelere göre türevini (çok boyutlu durumda **gradyan** olarak adlandırılır) hesaplayabileceğimiz ve parametreleri hatayı azaltacak şekilde değiştirebileceğimizdir. Bu şu şekilde formalize edilebilir:

* Parametreleri rastgele değerlerle başlatın: w<sup>(0)</sup>, b<sup>(0)</sup>
* Şu adımı birçok kez tekrarlayın:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Eğitim sırasında, optimizasyon adımları tüm veri seti dikkate alınarak hesaplanmalıdır (unutmayın ki kayıp, tüm eğitim örnekleri üzerinden bir toplam olarak hesaplanır). Ancak, gerçek hayatta veri setinin küçük bölümleri olan **minibatch'ler** alırız ve gradyanları bir alt veri kümesine dayanarak hesaplarız. Alt küme her seferinde rastgele alındığı için, bu yönteme **stokastik gradyan inişi** (SGD) denir.

## Çok Katmanlı Algılayıcılar ve Geri Yayılım

Tek katmanlı ağ, yukarıda gördüğümüz gibi, doğrusal olarak ayrılabilir sınıfları sınıflandırabilir. Daha zengin bir model oluşturmak için, ağın birkaç katmanını birleştirebiliriz. Matematiksel olarak bu, *f* fonksiyonunun daha karmaşık bir form alacağı ve birkaç adımda hesaplanacağı anlamına gelir:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Burada, α bir **doğrusal olmayan aktivasyon fonksiyonu**, σ bir softmax fonksiyonu ve parametreler θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>'dir.

Gradyan inişi algoritması aynı kalır, ancak gradyanları hesaplamak daha zor olur. Zincir türevleme kuralı sayesinde, türevleri şu şekilde hesaplayabiliriz:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Zincir türevleme kuralı, kayıp fonksiyonunun parametrelere göre türevlerini hesaplamak için kullanılır.

Bu ifadelerin en sol kısmı aynı olduğundan, türevleri kayıp fonksiyonundan başlayarak ve hesaplama grafiği boyunca "geri giderek" etkili bir şekilde hesaplayabiliriz. Bu nedenle, çok katmanlı bir algılayıcıyı eğitme yöntemi **geri yayılım** veya 'backprop' olarak adlandırılır.

<img alt="hesaplama grafiği" src="images/ComputeGraphGrad.png"/>

> TODO: görsel kaynağı

> ✅ Geri yayılımı, notebook örneğimizde çok daha ayrıntılı bir şekilde ele alacağız.  

## Sonuç

Bu derste, kendi sinir ağı kütüphanemizi oluşturduk ve bunu basit bir iki boyutlu sınıflandırma görevi için kullandık.

## 🚀 Meydan Okuma

Eşlik eden notebook'ta, çok katmanlı algılayıcılar oluşturmak ve eğitmek için kendi çerçevenizi uygulayacaksınız. Modern sinir ağlarının nasıl çalıştığını ayrıntılı bir şekilde görebileceksiniz.

[OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) notebook'una geçin ve üzerinde çalışın.

## [Ders Sonrası Testi](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## İnceleme ve Kendi Kendine Çalışma

Geri yayılım, AI ve ML'de yaygın olarak kullanılan bir algoritmadır ve [daha ayrıntılı](https://wikipedia.org/wiki/Backpropagation) çalışmaya değerdir.

## [Ödev](lab/README.md)

Bu laboratuvarda, bu derste oluşturduğunuz çerçeveyi kullanarak MNIST el yazısı rakam sınıflandırmasını çözmeniz isteniyor.

* [Talimatlar](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.