# Sinir Ağlarına Giriş. Çok Katmanlı Algılayıcı

Önceki bölümde, en basit sinir ağı modelini öğrendiniz - tek katmanlı algılayıcı, doğrusal iki sınıflı sınıflandırma modeli.

Bu bölümde, bu modeli daha esnek bir çerçeveye genişleterek şunları yapmayı sağlayacağız:

* İki sınıfa ek olarak **çok sınıflı sınıflandırma** gerçekleştirme
* Sınıflandırmaya ek olarak **regresyon (bağlanım) problemlerini** çözme
* Doğrusal olarak ayrılamayan sınıfları ayırma.

Python'da farklı sinir ağı mimarileri oluşturmamıza izin verecek kendi modüler çerçevemizi de geliştireceğiz.

## [Ders öncesi sınavı](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/104)

## Makine Öğrenmesinin Formülleştirilmesi

Makine Öğrenmesi problemini formülleştirerek başlayalım. **Y** etiketli bir **X** eğitim veri kümemiz olduğunu ve en doğru tahminleri yapacak bir *f* modeli oluşturmamız gerektiğini varsayalım. Tahminlerin kalitesi **kayıp işlevi** &lagran; ile ölçülür. Aşağıdaki kayıp fonksiyonları sıklıkla kullanılır:

* Bağlanım problemi için, bir sayıyı tahmin etmemiz gerektiğinde, **mutlak hata** &sum;<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| veya **kare hatası** &sum;<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i )</sup>)<sup>2</sup> kullanabiliriz.
* Sınıflandırma için **0-1 kaybı** (esas olarak modelin **doğruluğu** ile aynıdır) veya **lojistik kayıp** kullanırız.

Tek katmanlı algılayıcı için *f* işlevi, *f(x)=wx+b* doğrusal işlevi olarak tanımlanmıştır (burada *w* ağırlık matrisidir, *x* girdi özniteliklerinin vektörüdür ve *b* ek girdi vektörüdür). Farklı sinir ağı mimarileri için bu işlev daha karmaşık bir biçim alabilir.

> Sınıflandırma vakasında, genellikle ağ çıktısı olarak karşılık gelen sınıfların olasılıklarının alınması arzu edilir. Rastgele sayıları olasılıklara dönüştürmek için (örneğin çıktıyı normalleştirmek için), genellikle **softmaks** işlevi &sigma;'yı kullanırız ve *f* işlevi *f(x)=&sigma;(wx+b)* olur.

Yukarıdaki *f* tanımında *w* ve *b*, &theta;=⟨*w,b*⟩ **parametreler**i  olarak adlandırılır. Veri kümesi ⟨**X**,**Y**⟩ verildiğinde, &theta; parametrelerinin bir fonksiyonu olarak tüm veri kümesindeki genel bir hatayı hesaplayabiliriz.

> ✅ **Sinir ağı eğitiminin amacı, &theta; parametrelerini değiştirerek hatayı en aza indirmektir.**

## Gradyan İnişi Eniyilemesi

**Gradyan iniş**i adı verilen iyi bilinen bir işlev eniyileme yöntemi vardır. Buradaki fikir, parametrelere göre kayıp fonksiyonunun bir türevini (çok boyutlu durumda **gradyan** olarak adlandırılır) hesaplayabilmemiz ve parametreleri, hatanın azalacağı şekilde değiştirebilmemizdir. Bu, aşağıdaki gibi formüle dökülebilir:

* Parametreleri bazı rastgele değerlerle ilklet w<sup>(0)</sup>, b<sup>(0)</sup>
* Aşağıdaki adımı birçok kez tekrarlayın:
     - w<sup>(i+1)</sup> = w<sup>(i)</sup>-&eta;&part;&lagran;/&part;w
     - b<sup>(i+1)</sup> = b<sup>(i)</sup>-&eta;&part;&lagran;/&part;b

Eğitim esnasında, eniyileme adımlarının tüm veri kümesi dikkate alınarak hesaplanması gerekir (kaybın tüm eğitim örneklerinin toplamı olarak hesaplandığını unutmayın). Bununla birlikte, gerçek hayatta **minigruplar** olarak adlandırılan veri kümesinin küçük kısımlarını alır ve bir veri alt kümesine dayalı olarak gradyanları hesaplarız. Alt küme her seferinde rastgele alındığından, bu yönteme **rasgele gradyan inişi** (SGD - RGİ) denir.

## Çok Katmanlı Algılayıcılar ve Geri Yayma

Tek katmanlı ağ, yukarıda gördüğümüz gibi, doğrusal olarak ayrılabilir sınıfları sınıflandırma yeteneğine sahiptir. Daha zengin bir model oluşturmak için ağın birkaç katmanını birleştirebiliriz. Matematiksel olarak bu, *f* fonksiyonunun daha karmaşık bir forma sahip olacağı ve birkaç adımda hesaplanacağı anlamına gelir:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>&alpha;(z<sub>1</sub>)+b<sub>2</sub>
* f = &sigma;(z<sub>2</sub>)

Burada, &alpha; bir **doğrusal olmayan etkinleştirme işlevidir**, &sigma; bir softmaks işlevidir ve &theta;=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*> parametreleridir.

Gradyan inişi algoritması aynı kalacaktır, ancak gradyanları hesaplamak daha zor olacaktır. Zincir türev alma kuralı göz önüne alındığında, türevleri şu şekilde hesaplayabiliriz:

* &part;&lagran;/&part;w<sub>2</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;w<sub>2</sub>)
* &part;&lagran;/&part;w<sub>1</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;&alpha;)(&part;&alpha;/&part;z<sub>1</sub>)(&part;z<sub>1</sub>/&part;w<sub>1</sub>)

> ✅ Parametrelere göre kayıp fonksiyonunun türevlerini hesaplamak için zincir türev alma kuralı kullanılır.

Tüm bu ifadelerin en soldaki kısmının aynı olduğuna ve dolayısıyla kayıp fonksiyonundan başlayarak ve hesaplama çizgesi boyunca "geriye" doğru giden türevleri etkin bir şekilde hesaplayabileceğimize dikkat edin. Bu nedenle çok katmanlı bir algılayıcıyı eğitme yöntemine **geri yayma** veya 'geriyay' denir.

<img alt="compute graph" src="../images/ComputeGraphGrad.png"/>

> TODO: imge alıntısı

> ✅ Geriyay'ı not defteri örneğimizde çok daha ayrıntılı olarak ele alacağız.

## Vargılar

Bu dersimizde kendi sinir ağı kütüphanemizi oluşturduk ve onu basit bir iki boyutlu sınıflandırma görevi için kullandık.

## 🚀 Kendini Sınama

Ekteki not defterinde, çok katmanlı algılayıcıları oluşturmak ve eğitmek için kendi çerçevenizi uygulayacaksınız. Modern sinir ağlarının nasıl çalıştığını ayrıntılı olarak görebileceksiniz.

[OwnFramework (KendiCerveceniz)](OwnFramework.tr.ipynb) not defterine gidin ve üzerinde çalışın.

## [Ders sonrası sınavı](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/204)

## Gözden Geçirme ve Bireysel Çalışma

Geri yayma, YZ ve makine öğrenmesinde kullanılan yaygın bir algoritmadır ve [daha ayrıntılı olarak](https://wikipedia.org/wiki/Backpropagation) incelemeye değerdir.

## [Ödev](../lab/translations/README.tr.md)

Bu laboratuvarda, MNIST el yazısı rakam sınıflandırmasını çözmek için bu derste oluşturduğunuz çerçeveyi kullanmanız istenmektedir.

* [Talimatlar](../lab/translations/README.tr.md)
* [Not Defteri](../lab/translations/MyFW_MNIST.tr.ipynb)
