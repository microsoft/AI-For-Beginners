# Sinir Ağlarına Giriş. Çok Katmanlı Algılayıcı

Önceki bölümde, en basit sinir ağı modelini - tek katmanlı algılayıcıyı, iki sınıflı lineer sınıflandırma modeli olarak öğrendiniz.

Bu bölümde, bu modeli daha esnek bir çerçeveye genişleteceğiz, böylece:

* iki sınıfın yanı sıra **çoklu sınıf sınıflandırması** gerçekleştirebileceğiz
* sınıflandırmanın yanı sıra **regresyon problemleri** çözebileceğiz
* lineer olarak ayrılamayan sınıfları ayırabileceğiz

Ayrıca, farklı sinir ağı mimarilerini oluşturmak için Python'da kendi modüler çerçevemizi geliştireceğiz.

## [Ders öncesi quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/104)

## Makine Öğreniminin Formülasyonu

Makine Öğrenimi problemini formüle etmeye başlayalım. Diyelim ki etiketleri **Y** olan bir eğitim veri setimiz **X** var ve en doğru tahminleri yapacak bir model *f* inşa etmemiz gerekiyor. Tahminlerin kalitesi **Kayıp fonksiyonu** ℒ ile ölçülür. Aşağıdaki kayıp fonksiyonları sıkça kullanılır:

* Regresyon problemi için, bir sayı tahmin etmemiz gerektiğinde, **mutlak hata** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| veya **kare hata** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup> kullanabiliriz.
* Sınıflandırma için, **0-1 kaybı** (bu, modelin **doğruluğu** ile özdeştir) veya **lojistik kayıp** kullanırız.

Tek katmanlı algılayıcı için, *f* fonksiyonu lineer bir fonksiyon olarak tanımlanmıştı *f(x)=wx+b* (burada *w* ağırlık matrisidir, *x* giriş özellikleri vektörüdür ve *b* önyargı vektörüdür). Farklı sinir ağı mimarileri için, bu fonksiyon daha karmaşık bir biçim alabilir.

> Sınıflandırma durumunda, genellikle ağ çıkışı olarak ilgili sınıfların olasılıklarını almak arzu edilir. Rastgele sayıları olasılıklara dönüştürmek için (örneğin, çıktıyı normalleştirmek amacıyla) genellikle **softmax** fonksiyonu σ kullanılır ve *f* fonksiyonu *f(x)=σ(wx+b)* haline gelir.

Yukarıdaki *f* tanımında, *w* ve *b* **parametreler** θ=⟨*w,b*⟩ olarak adlandırılır. Veri seti ⟨**X**,**Y**⟩ verildiğinde, tüm veri seti üzerinde genel bir hatayı parametreler θ'nın bir fonksiyonu olarak hesaplayabiliriz.

> ✅ **Sinir ağı eğitiminin amacı, parametre θ'yı değiştirerek hatayı minimize etmektir.**

## Gradyan İnişi Optimizasyonu

**Gradyan inişi** olarak bilinen bir fonksiyon optimizasyon yöntemi vardır. Fikir, kayıp fonksiyonunun parametreler ile olan türevini (çok boyutlu durumda **gradyan** olarak adlandırılır) hesaplayabilmemiz ve hatanın azalacak şekilde parametreleri değiştirebilmemizdir. Bu, aşağıdaki gibi formüle edilebilir:

* Parametreleri bazı rastgele değerlerle w<sup>(0)</sup>, b<sup>(0)</sup> ile başlatın.
* Aşağıdaki adımı birçok kez tekrarlayın:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Eğitim sırasında, optimizasyon adımlarının tüm veri setini dikkate alarak hesaplanması beklenir (kayıp, tüm eğitim örnekleri üzerinden bir toplam olarak hesaplandığını unutmayın). Ancak, gerçek hayatta **minibatch** olarak adlandırılan veri setinin küçük parçalarını alır ve gradyanları bir veri alt kümesine dayalı olarak hesaplarız. Her seferinde alt küme rastgele alındığı için, bu yöntem **stochastik gradyan inişi** (SGD) olarak adlandırılır.

## Çok Katmanlı Algılayıcılar ve Geri Yayılım

Yukarıda gördüğümüz tek katmanlı ağ, lineer olarak ayrılamayan sınıfları sınıflandırma yeteneğine sahiptir. Daha zengin bir model oluşturmak için, ağın birkaç katmanını birleştirebiliriz. Matematiksel olarak bu, *f* fonksiyonunun daha karmaşık bir biçim alacağı ve birkaç adımda hesaplanacağı anlamına gelir:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Burada, α **lineer olmayan aktivasyon fonksiyonu**dur, σ softmax fonksiyonudur ve parametreler θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>'dir.

Gradyan inişi algoritması aynı kalacak, ancak gradyanları hesaplamak daha zor olacaktır. Zincirleme türev kuralını göz önünde bulundurarak, türevleri şu şekilde hesaplayabiliriz:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Zincirleme türev kuralı, kayıp fonksiyonunun parametrelerle olan türevlerini hesaplamak için kullanılır.

Tüm bu ifadelerin en soldaki kısmının aynı olduğunu ve bu nedenle kayıp fonksiyonundan başlayarak "geriye" hesaplama grafiği üzerinden türevleri etkili bir şekilde hesaplayabileceğimizi unutmayın. Böylece çok katmanlı bir algılayıcının eğitilmesi yöntemi **geri yayılım** veya 'backprop' olarak adlandırılır.

<img alt="hesap grafiği" src="images/ComputeGraphGrad.png"/>

> TODO: resim alıntısı

> ✅ Geri yayılımı not defteri örneğimizde çok daha ayrıntılı bir şekilde ele alacağız.  

## Sonuç

Bu derste, kendi sinir ağı kütüphanemizi oluşturduk ve bunu basit bir iki boyutlu sınıflandırma görevinde kullandık.

## 🚀 Zorluk

Eşlik eden not defterinde, çok katmanlı algılayıcılar oluşturmak ve eğitmek için kendi çerçevenizi uygulayacaksınız. Modern sinir ağlarının nasıl çalıştığını ayrıntılı olarak görebileceksiniz.

[OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) not defterine geçin ve üzerinde çalışın.

## [Ders sonrası quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/204)

## Gözden Geçirme & Kendi Kendine Çalışma

Geri yayılım, AI ve ML'de yaygın olarak kullanılan bir algoritmadır, [daha ayrıntılı olarak](https://wikipedia.org/wiki/Backpropagation) incelenmeye değer.

## [Görev](lab/README.md)

Bu laboratuvar çalışmasında, bu derste inşa ettiğiniz çerçeveyi MNIST el yazısı rakam sınıflandırma sorununu çözmek için kullanmanız istenmektedir.

* [Talimatlar](lab/README.md)
* [Not Defteri](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanılması sonucu ortaya çıkan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul etmiyoruz.