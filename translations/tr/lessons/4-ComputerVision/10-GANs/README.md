# Üretken Çatışmalı Ağlar

Önceki bölümde **üretken modeller** hakkında bilgi edindik: eğitim veri setindeki görüntülere benzer yeni görüntüler üretebilen modeller. VAE, bir üretken modelin iyi bir örneğiydi.

## [Ders öncesi quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

Ancak, VAE ile gerçekten anlamlı bir şey, örneğin makul bir çözünürlükte bir resim üretmeye çalıştığımızda, eğitimin iyi bir şekilde yakınsadığını göremeyiz. Bu kullanım durumu için, üretken modellere özel olarak hedeflenmiş başka bir mimari hakkında bilgi edinmemiz gerekir - **Üretken Çatışmalı Ağlar**, veya kısaca GAN'lar.

GAN'ın ana fikri, birbirine karşı eğitilecek iki sinir ağına sahip olmaktır:

<img src="images/gan_architecture.png" width="70%"/>

> Resim [Dmitry Soshnikov](http://soshnikov.com) tarafından

> ✅ Küçük bir kelime bilgisi:
> * **Üretici** (Generator), rastgele bir vektör alıp, sonuç olarak bir görüntü üreten bir ağdır.
> * **Ayrıştırıcı** (Discriminator), bir görüntü alır ve bunun gerçek bir görüntü olup olmadığını (eğitim veri setinden) ya da bir üretici tarafından üretilip üretilmediğini belirtmelidir. Temelde bir görüntü sınıflayıcısıdır.

### Ayrıştırıcı

Ayrıştırıcının mimarisi, sıradan bir görüntü sınıflama ağından farklı değildir. En basit durumda, tamamen bağlı bir sınıflayıcı olabilir, ancak büyük ihtimalle bir [konvolüsyonel ağ](../07-ConvNets/README.md) olacaktır.

> ✅ Konvolüsyonel ağlara dayanan bir GAN'a [DCGAN](https://arxiv.org/pdf/1511.06434.pdf) denir.

Bir CNN ayrıştırıcısı, aşağıdaki katmanlardan oluşur: birkaç konvolüsyon+havuzlama (azalan mekansal boyutlarla) ve "özellik vektörü" elde etmek için bir veya daha fazla tamamen bağlı katman, son ikili sınıflayıcı.

> ✅ Bu bağlamda 'havuzlama', görüntünün boyutunu azaltan bir tekniktir. "Havuzlama katmanları, bir katmandaki nöron kümelerinin çıktısını bir sonraki katmandaki tek bir nörona birleştirerek verinin boyutunu azaltır." - [kaynak](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Üretici

Üretici biraz daha karmaşıktır. Bunu tersine çevrilmiş bir ayrıştırıcı olarak düşünebilirsiniz. Gizli bir vektörden (özellik vektörünün yerinde) başlar, gerekli boyut/şekle dönüştürmek için bir tamamen bağlı katmana sahiptir ve ardından dekonvolüsyonlar+ölçekleme yapılır. Bu, [oto kodlayıcı](../09-Autoencoders/README.md) kısmının *çözücü* bölümüne benzerdir.

> ✅ Konvolüsyon katmanı görüntüyü tarayan bir lineer filtre olarak uygulandığı için, dekonvolüsyon temelde konvolüsyona benzer ve aynı katman mantığı kullanılarak uygulanabilir.

<img src="images/gan_arch_detail.png" width="70%"/>

> Resim [Dmitry Soshnikov](http://soshnikov.com) tarafından

### GAN'ı Eğitmek

GAN'lar **çatışmalı** olarak adlandırılır çünkü üretici ile ayrıştırıcı arasında sürekli bir rekabet vardır. Bu rekabet sırasında, hem üretici hem de ayrıştırıcı gelişir, böylece ağ daha iyi ve daha iyi resimler üretmeyi öğrenir.

Eğitim iki aşamada gerçekleşir:

* **Ayrıştırıcıyı Eğitmek**. Bu görev oldukça basittir: üretici tarafından bir görüntü partisi üretiyoruz, bunları sahte görüntü için 0 olarak etiketliyoruz ve giriş veri setinden (gerçek görüntü için etiket 1) bir görüntü partisi alıyoruz. Bazı *ayrıştırıcı kaybı* elde ediyoruz ve geri yayılım yapıyoruz.
* **Üreticiyi Eğitmek**. Bu biraz daha karmaşıktır, çünkü üretici için beklenen çıktıyı doğrudan bilmiyoruz. Bir üretici ve ardından ayrıştırıcıdan oluşan tüm GAN ağını alıyoruz, bazı rastgele vektörlerle besliyoruz ve sonucun 1 (gerçek görüntülere karşılık gelen) olmasını bekliyoruz. Ardından, ayrıştırıcının parametrelerini donduruyoruz (bu adımda eğitilmesini istemiyoruz) ve geri yayılım yapıyoruz.

Bu süreçte, hem üretici hem de ayrıştırıcı kayıpları önemli ölçüde düşmez. İdeal durumda, her iki ağın performanslarını geliştirmesine karşılık olarak osilasyon göstermelidirler.

## ✍️ Alıştırmalar: GAN'lar

* [TensorFlow/Keras'ta GAN Not Defteri](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [PyTorch'ta GAN Not Defteri](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### GAN eğitimindeki problemler

GAN'ların eğitiminin özellikle zor olduğu bilinmektedir. İşte birkaç problem:

* **Mod Çökmesi**. Bu terim, üreticinin bir başarılı görüntü üretmeyi öğrenmesi ve farklı görüntü çeşitliliği üretmemesi anlamına gelir.
* **Hiperparametrelere duyarlılık**. Genellikle bir GAN'ın hiç yakınsama göstermediğini görebilirsiniz ve ardından öğrenme oranında ani bir düşüş ile yakınsama sürecine girebilir.
* Üretici ve ayrıştırıcı arasında bir **denge** sağlamak. Birçok durumda ayrıştırıcı kaybı oldukça hızlı bir şekilde sıfıra düşebilir, bu da üreticinin daha fazla eğitim yapamamasına neden olur. Bunu aşmak için, üretici ve ayrıştırıcı için farklı öğrenme oranları belirlemeyi deneyebiliriz veya kayıp zaten çok düşükse ayrıştırıcı eğitimini atlayabiliriz.
* **Yüksek çözünürlük** için eğitim. Oto kodlayıcılarla benzer bir sorunu yansıtarak, çok sayıda konvolüsyonel ağ katmanını yeniden yapılandırmanın artefaktlara yol açması nedeniyle bu problem tetiklenir. Bu problem genellikle ilk olarak birkaç katmanın düşük çözünürlükteki görüntüler üzerinde eğitilmesi ve ardından katmanların "açılması" veya eklenmesiyle çözülen **ilerlemeli büyüme** ile çözülür. Diğer bir çözüm, katmanlar arasında ekstra bağlantılar eklemek ve birden fazla çözünürlükte eğitim yapmaktır - detaylar için bu [Çok Ölçekli Gradyan GAN'lar makalesine](https://arxiv.org/abs/1903.06048) bakın.

## Stil Aktarımı

GAN'lar sanatsal görüntüler oluşturmak için harika bir yoldur. Diğer ilginç bir teknik ise **stil aktarımı** olarak adlandırılır; bu teknik, bir **içerik görüntüsü** alır ve bunu farklı bir stil ile yeniden çizer, **stil görüntüsünden** filtreler uygulayarak.

Bu işlem şu şekilde çalışır:
* Rastgele bir gürültü görüntüsü ile başlarız (veya bir içerik görüntüsü ile, ancak anlamak açısından rastgele gürültü ile başlamak daha kolaydır).
* Amacımız, hem içerik görüntüsüne hem de stil görüntüsüne yakın bir görüntü oluşturmaktır. Bu, iki kayıp fonksiyonu ile belirlenir:
   - **İçerik kaybı**, mevcut görüntü ve içerik görüntüsünden çıkarılan özellikler kullanılarak hesaplanır.
   - **Stil kaybı**, mevcut görüntü ve stil görüntüsü arasındaki ilişkiyi akıllıca Gram matrisleri kullanarak hesaplar (daha fazla detay için [örnek not defterine](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) bakın).
* Görüntüyü daha pürüzsüz hale getirmek ve gürültüyü kaldırmak için, ayrıca komşu pikseller arasındaki ortalama mesafeyi hesaplayan **Varyasyon kaybı** da tanıtıyoruz.
* Ana optimizasyon döngüsü, toplam kaybı minimize etmek için mevcut görüntüyü gradyan inişi (veya başka bir optimizasyon algoritması) kullanarak ayarlamaktadır; bu, üç kaybın ağırlıklı toplamıdır.

## ✍️ Örnek: [Stil Aktarımı](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Ders sonrası quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## Sonuç

Bu derste, GAN'lar ve bunları nasıl eğiteceğiniz hakkında bilgi edindiniz. Ayrıca, bu tür bir Sinir Ağı'nın karşılaşabileceği özel zorluklar ve bunları aşmanın bazı stratejileri hakkında bilgi edindiniz.

## 🚀 Meydan Okuma

Kendi görüntülerinizi kullanarak [Stil Aktarımı not defterini](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) çalıştırın.

## İnceleme & Kendi Kendine Çalışma

Referans olarak, GAN'lar hakkında daha fazla bilgi edinmek için bu kaynakları okuyun:

* Marco Pasini, [Bir Yıl Boyunca GAN Eğitimiyle İlgili Öğrendiğim 10 Ders](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* Dikkate alınması gereken bir *de facto* GAN mimarisi olan [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN)
* [Azure ML'de GAN'lar kullanarak Üretken Sanat Oluşturma](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Görev

Bu derse bağlı iki not defterinden birini gözden geçirin ve GAN'ı kendi görüntüleriniz üzerinde yeniden eğitin. Ne yaratabilirsiniz?

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde otoriter bir kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanılması sonucunda ortaya çıkan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul etmiyoruz.