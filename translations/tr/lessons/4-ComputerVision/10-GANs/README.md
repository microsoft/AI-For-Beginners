<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-26T07:26:24+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "tr"
}
-->
# Üretici Çekişmeli Ağlar (Generative Adversarial Networks)

Önceki bölümde, **üretici modeller** hakkında bilgi edindik: eğitim veri kümesindeki görüntülere benzer yeni görüntüler üretebilen modeller. VAE, üretici bir modele iyi bir örnekti.

## [Ders Öncesi Test](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

Ancak, VAE ile makul bir çözünürlükte anlamlı bir şey, örneğin bir tablo, üretmeye çalışırsak, eğitimin iyi bir şekilde yakınsama sağlamadığını göreceğiz. Bu kullanım durumu için, özellikle üretici modellere yönelik başka bir mimariyi öğrenmeliyiz - **Üretici Çekişmeli Ağlar** veya GAN'ler.

GAN'in temel fikri, birbirine karşı eğitilecek iki sinir ağına sahip olmaktır:

<img src="images/gan_architecture.png" width="70%"/>

> Görsel: [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Küçük bir kelime bilgisi:
> * **Üretici (Generator)**, rastgele bir vektör alıp sonuç olarak bir görüntü üreten bir ağdır.
> * **Ayrımcı (Discriminator)**, bir görüntü alır ve bunun gerçek bir görüntü mü (eğitim veri kümesinden) yoksa bir üretici tarafından mı üretildiğini belirlemelidir. Esasen bir görüntü sınıflandırıcısıdır.

### Ayrımcı (Discriminator)

Ayrımcının mimarisi, sıradan bir görüntü sınıflandırma ağından farklı değildir. En basit durumda, tamamen bağlı bir sınıflandırıcı olabilir, ancak büyük olasılıkla bir [konvolüsyonel ağ](../07-ConvNets/README.md) olacaktır.

> ✅ Konvolüsyonel ağlara dayalı bir GAN, [DCGAN](https://arxiv.org/pdf/1511.06434.pdf) olarak adlandırılır.

Bir CNN ayrımcısı şu katmanlardan oluşur: birkaç konvolüsyon + havuzlama (azalan uzamsal boyutlarla) ve bir veya daha fazla tamamen bağlı katman, "özellik vektörü" elde etmek için, ardından ikili bir sınıflandırıcı.

> ✅ 'Havuzlama' (pooling) bu bağlamda, görüntünün boyutunu küçültme tekniğidir. "Havuzlama katmanları, bir katmandaki nöron kümelerinin çıktısını bir sonraki katmandaki tek bir nöronda birleştirerek verilerin boyutlarını azaltır." - [kaynak](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Üretici (Generator)

Üretici biraz daha karmaşıktır. Bunu tersine çevrilmiş bir ayrımcı olarak düşünebilirsiniz. Bir özellik vektörü yerine bir gizli vektörden başlayarak, gerekli boyut/şekle dönüştürmek için tamamen bağlı bir katmana sahiptir, ardından dekonvolüsyonlar + ölçek büyütme gelir. Bu, [otoenkoderin](../09-Autoencoders/README.md) *kod çözücü* kısmına benzer.

> ✅ Konvolüsyon katmanı, görüntü üzerinde bir doğrusal filtre olarak uygulandığından, dekonvolüsyon esasen konvolüsyona benzerdir ve aynı katman mantığı kullanılarak uygulanabilir.

<img src="images/gan_arch_detail.png" width="70%"/>

> Görsel: [Dmitry Soshnikov](http://soshnikov.com)

### GAN'in Eğitimi

GAN'ler **çekişmeli** olarak adlandırılır çünkü üretici ve ayrımcı arasında sürekli bir rekabet vardır. Bu rekabet sırasında hem üretici hem de ayrımcı gelişir, böylece ağ daha iyi ve daha iyi görüntüler üretmeyi öğrenir.

Eğitim iki aşamada gerçekleşir:

* **Ayrımcının eğitimi**. Bu görev oldukça basittir: üretici tarafından bir görüntü grubu oluştururuz, bunları sahte görüntü anlamına gelen 0 ile etiketleriz ve giriş veri kümesinden bir grup görüntü alırız (1 etiketiyle, gerçek görüntü). Bir *ayrımcı kaybı* elde ederiz ve geri yayılım yaparız.
* **Üreticinin eğitimi**. Bu biraz daha karmaşıktır çünkü üretici için beklenen çıktıyı doğrudan bilmiyoruz. Üretici ve ayrımcıdan oluşan tüm GAN ağına bazı rastgele vektörler besleriz ve sonucun 1 (gerçek görüntülere karşılık gelen) olmasını bekleriz. Ardından ayrımcının parametrelerini dondururuz (bu adımda eğitilmesini istemeyiz) ve geri yayılım yaparız.

Bu süreç sırasında, hem üretici hem de ayrımcı kayıpları önemli ölçüde azalmaz. İdeal durumda, her iki ağın performansını geliştirdiğini gösteren bir salınım yapmalıdırlar.

## ✍️ Alıştırmalar: GAN'ler

* [TensorFlow/Keras ile GAN Defteri](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [PyTorch ile GAN Defteri](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### GAN Eğitimiyle İlgili Sorunlar

GAN'lerin eğitimi özellikle zordur. İşte birkaç sorun:

* **Mod Çökmesi**. Bu terimle, üreticinin ayrımcıyı kandıran tek bir başarılı görüntü üretmeyi öğrenmesi ve farklı görüntüler üretmemesi kastedilir.
* **Hiperparametrelere duyarlılık**. Çoğu zaman, bir GAN'in hiç yakınsamadığını ve ardından öğrenme oranındaki ani bir düşüşle yakınsamaya başladığını görebilirsiniz.
* Üretici ve ayrımcı arasında bir **denge** sağlamak. Çoğu durumda, ayrımcı kaybı nispeten hızlı bir şekilde sıfıra düşebilir, bu da üreticinin daha fazla eğitim yapamamasına neden olur. Bunu aşmak için, üretici ve ayrımcı için farklı öğrenme oranları ayarlamayı deneyebilir veya kayıp zaten çok düşükse ayrımcı eğitimini atlayabiliriz.
* **Yüksek çözünürlük** için eğitim. Otoenkoderlerde olduğu gibi, bu sorun, çok fazla konvolüsyonel ağ katmanını yeniden yapılandırmanın artefaktlara yol açması nedeniyle ortaya çıkar. Bu sorun genellikle, önce birkaç katmanın düşük çözünürlüklü görüntüler üzerinde eğitildiği ve ardından katmanların "açıldığı" veya eklendiği **aşamalı büyüme** ile çözülür. Bir diğer çözüm, katmanlar arasında ek bağlantılar eklemek ve birden fazla çözünürlüğü aynı anda eğitmek olabilir - ayrıntılar için bu [Çok Ölçekli Gradient GAN'ler makalesine](https://arxiv.org/abs/1903.06048) bakabilirsiniz.

## Stil Transferi

GAN'ler sanatsal görüntüler üretmek için harika bir yöntemdir. Bir diğer ilginç teknik ise **stil transferi** olarak adlandırılır. Bu teknik, bir **içerik görüntüsü** alır ve onu farklı bir tarzda yeniden çizer, **stil görüntüsünden** filtreler uygular.

Bu yöntem şu şekilde çalışır:
* Rastgele bir gürültü görüntüsüyle başlarız (veya bir içerik görüntüsüyle, ancak anlamak için rastgele gürültüyle başlamak daha kolaydır)
* Amacımız, hem içerik görüntüsüne hem de stil görüntüsüne yakın olacak bir görüntü oluşturmaktır. Bu, iki kayıp fonksiyonu ile belirlenir:
   - **İçerik kaybı**, mevcut görüntü ve içerik görüntüsünden CNN tarafından bazı katmanlarda çıkarılan özelliklere dayanarak hesaplanır.
   - **Stil kaybı**, mevcut görüntü ve stil görüntüsü arasında, Gram matrisleri kullanılarak (daha fazla ayrıntı için [örnek deftere](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) bakabilirsiniz) hesaplanır.
* Görüntüyü daha pürüzsüz hale getirmek ve gürültüyü kaldırmak için, **Varyasyon kaybı** da ekleriz, bu kayıp komşu pikseller arasındaki ortalama mesafeyi hesaplar.
* Ana optimizasyon döngüsü, toplam kaybı (üç kaybın ağırlıklı toplamı) minimize etmek için mevcut görüntüyü gradyan inişi (veya başka bir optimizasyon algoritması) kullanarak ayarlar.

## ✍️ Örnek: [Stil Transferi](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Ders Sonrası Test](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## Sonuç

Bu derste, GAN'ler ve bunları nasıl eğiteceğinizi öğrendiniz. Ayrıca, bu tür Sinir Ağlarının karşılaşabileceği özel zorlukları ve bunların üstesinden nasıl gelinebileceğine dair bazı stratejileri öğrendiniz.

## 🚀 Meydan Okuma

[Stil Transferi defterini](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) kendi görüntülerinizle çalıştırın.

## İnceleme ve Kendi Kendine Çalışma

Referans için, GAN'ler hakkında daha fazla bilgi edinmek için şu kaynakları okuyun:

* Marco Pasini, [GAN'leri Bir Yıl Boyunca Eğitmekten Öğrendiğim 10 Ders](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), dikkate alınması gereken bir *de facto* GAN mimarisi
* [Azure ML'de GAN'ler Kullanarak Üretici Sanat Oluşturma](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Ödev

Bu derse ait iki defterden birini tekrar gözden geçirin ve GAN'i kendi görüntülerinizle yeniden eğitin. Neler oluşturabilirsiniz?

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.