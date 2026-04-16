# Sinir Ağlarına Giriş. Çok Katmanlı Perceptron

Önceki bölümde, en basit sinir ağı modeli olan tek katmanlı perceptron, yani doğrusal iki sınıflı sınıflandırma modelini öğrendiniz.

Bu bölümde, bu modeli daha esnek bir çerçeveye genişleteceğiz. Bu sayede:

* İki sınıfın yanı sıra **çok sınıflı sınıflandırma** yapabiliriz  
* Sınıflandırmanın yanı sıra **regresyon problemlerini** çözebiliriz  
* Doğrusal olarak ayrılabilir olmayan sınıfları ayırabiliriz  

Ayrıca, farklı sinir ağı mimarileri oluşturabilmemizi sağlayacak kendi modüler Python çerçevemizi geliştireceğiz.

## [Ders Öncesi Testi](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Makine Öğreniminin Formalizasyonu

Makine Öğrenimi problemini formalize ederek başlayalım. Diyelim ki **X** adlı bir eğitim veri setimiz ve **Y** adlı etiketlerimiz var ve en doğru tahminleri yapacak bir model *f* inşa etmemiz gerekiyor. Tahminlerin kalitesi **Kayıp Fonksiyonu** &lagran; ile ölçülür. Aşağıdaki kayıp fonksiyonları sıkça kullanılır:

* Bir sayı tahmin etmemiz gereken regresyon problemlerinde, **mutlak hata** &sum;<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| veya **kare hata** &sum;<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup> kullanılabilir.  
* Sınıflandırma için, **0-1 kaybı** (temelde modelin **doğruluğu** ile aynıdır) veya **lojistik kayıp** kullanılır.

Tek katmanlı perceptron için, *f* fonksiyonu doğrusal bir fonksiyon olarak tanımlanır: *f(x)=wx+b* (burada *w* ağırlık matrisi, *x* giriş özelliklerinin vektörü ve *b* bias vektörüdür). Farklı sinir ağı mimarileri için bu fonksiyon daha karmaşık bir form alabilir.

> Sınıflandırma durumunda, ağ çıktısı olarak ilgili sınıfların olasılıklarını elde etmek genellikle istenir. Rastgele sayıları olasılıklara dönüştürmek (örneğin, çıktıyı normalize etmek) için genellikle **softmax** fonksiyonu &sigma; kullanılır ve *f* fonksiyonu *f(x)=&sigma;(wx+b)* haline gelir.

Yukarıdaki *f* tanımında, *w* ve *b* **parametreler** olarak adlandırılır: &theta;=⟨*w,b*⟩. Veri seti ⟨**X**,**Y**⟩ verildiğinde, tüm veri seti üzerindeki toplam hatayı parametrelerin bir fonksiyonu olarak hesaplayabiliriz.

> ✅ **Sinir ağı eğitiminin amacı, parametreleri &theta; değiştirerek hatayı minimize etmektir.**

## Gradyan İnişi Optimizasyonu

**Gradyan inişi** adı verilen iyi bilinen bir fonksiyon optimizasyon yöntemi vardır. Bu yöntemin temel fikri, kayıp fonksiyonunun parametrelere göre türevini (çok boyutlu durumda **gradyan** olarak adlandırılır) hesaplayarak, hatayı azaltacak şekilde parametreleri değiştirmektir. Bu şu şekilde formalize edilebilir:

* Parametreleri rastgele değerlerle başlat: w<sup>(0)</sup>, b<sup>(0)</sup>  
* Aşağıdaki adımı birçok kez tekrarla:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-&eta;&part;&lagran;/&part;w  
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-&eta;&part;&lagran;/&part;b  

Eğitim sırasında, optimizasyon adımları tüm veri seti dikkate alınarak hesaplanmalıdır (hatırlayın, kayıp tüm eğitim örnekleri üzerinden bir toplam olarak hesaplanır). Ancak, gerçek hayatta veri setinin küçük parçaları olan **minibatch'ler** alınır ve gradyanlar bir alt veri kümesine dayanarak hesaplanır. Alt küme her seferinde rastgele alındığı için bu yönteme **stokastik gradyan inişi** (SGD) denir.

## Çok Katmanlı Perceptronlar ve Geri Yayılım

Yukarıda gördüğümüz gibi, tek katmanlı bir ağ doğrusal olarak ayrılabilir sınıfları sınıflandırabilir. Daha zengin bir model oluşturmak için, ağın birkaç katmanını birleştirebiliriz. Matematiksel olarak bu, *f* fonksiyonunun daha karmaşık bir form alacağı ve birkaç adımda hesaplanacağı anlamına gelir:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>  
* z<sub>2</sub>=w<sub>2</sub>&alpha;(z<sub>1</sub>)+b<sub>2</sub>  
* f = &sigma;(z<sub>2</sub>)  

Burada, &alpha; bir **doğrusal olmayan aktivasyon fonksiyonu**, &sigma; bir softmax fonksiyonu ve parametreler &theta;=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>'dir.

Gradyan inişi algoritması aynı kalır, ancak gradyanları hesaplamak daha zor hale gelir. Zincir türev kuralı kullanılarak türevler şu şekilde hesaplanabilir:

* &part;&lagran;/&part;w<sub>2</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;w<sub>2</sub>)  
* &part;&lagran;/&part;w<sub>1</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;&alpha;)(&part;&alpha;/&part;z<sub>1</sub>)(&part;z<sub>1</sub>/&part;w<sub>1</sub>)  

> ✅ Zincir türev kuralı, kayıp fonksiyonunun parametrelere göre türevlerini hesaplamak için kullanılır.

Dikkat edin, bu ifadelerin en sol kısmı aynıdır ve bu nedenle türevleri etkili bir şekilde kayıp fonksiyonundan başlayarak "geri" doğru hesaplayabiliriz. Bu nedenle, çok katmanlı perceptron eğitme yöntemi **geri yayılım** veya 'backprop' olarak adlandırılır.

<img alt="hesaplama grafiği" src="../../../../../translated_images/tr/ComputeGraphGrad.4626252c0de03507.webp"/>

> TODO: görsel kaynağı

> ✅ Geri yayılımı, notebook örneğimizde çok daha ayrıntılı bir şekilde ele alacağız.

## Sonuç

Bu derste, kendi sinir ağı kütüphanemizi oluşturduk ve bunu basit bir iki boyutlu sınıflandırma görevi için kullandık.

## 🚀 Meydan Okuma

Eşlik eden notebook'ta, çok katmanlı perceptronlar oluşturmak ve eğitmek için kendi çerçevenizi uygulayacaksınız. Modern sinir ağlarının nasıl çalıştığını ayrıntılı bir şekilde görebileceksiniz.

[OwnFramework](OwnFramework.ipynb) notebook'una geçin ve üzerinde çalışın.

## [Ders Sonrası Testi](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Gözden Geçirme ve Kendi Kendine Çalışma

Geri yayılım, AI ve ML'de yaygın olarak kullanılan bir algoritmadır ve [daha ayrıntılı](https://wikipedia.org/wiki/Backpropagation) çalışmaya değerdir.

## [Ödev](lab/README.md)

Bu laboratuvarda, bu derste oluşturduğunuz çerçeveyi kullanarak MNIST el yazısı rakam sınıflandırmasını çözmeniz isteniyor.

* [Talimatlar](lab/README.md)  
* [Notebook](lab/MyFW_MNIST.ipynb)  

---

