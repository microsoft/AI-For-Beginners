# Çok Modlu Ağlar

Transformer modellerinin NLP görevlerini çözmedeki başarısının ardından, aynı veya benzer mimariler bilgisayarla görme görevlerine uygulanmıştır. Görsel ve doğal dil yeteneklerini *birleştiren* modeller oluşturma konusunda artan bir ilgi vardır. Bu tür girişimlerden biri OpenAI tarafından gerçekleştirilmiş olup, CLIP ve DALL.E olarak adlandırılmaktadır.

## Karşıt Görüntü Ön Eğitimi (CLIP)

CLIP'in ana fikri, metin istemlerini bir görüntü ile karşılaştırabilmek ve görüntünün istemle ne kadar iyi eşleştiğini belirlemektir.

![CLIP Mimarı](../../../../../translated_images/clip-arch.b3dbf20b4e8ed8be1c38e2bc6100fd3cc257c33cda4692b301be91f791b13ea7.tr.png)

> *Resim [bu blog yazısından](https://openai.com/blog/clip/) alınmıştır.*

Model, İnternetten elde edilen görüntüler ve bunların başlıkları üzerinde eğitilmektedir. Her bir grup için N (görüntü, metin) çiftini alır ve bunları bazı vektör temsillerine dönüştürür. Bu temsiller daha sonra bir araya getirilir. Kayıp fonksiyonu, bir çift (örneğin I ve T) ile ilgili vektörler arasındaki kosinüs benzerliğini maksimize edecek şekilde tanımlanmıştır ve diğer tüm çiftler arasındaki kosinüs benzerliğini minimize etmektedir. Bu nedenle bu yaklaşım **karşıt** olarak adlandırılmaktadır.

CLIP modeli/kütüphanesi [OpenAI GitHub](https://github.com/openai/CLIP) üzerinden mevcuttur. Yaklaşım [bu blog yazısında](https://openai.com/blog/clip/) ve daha ayrıntılı olarak [bu makalede](https://arxiv.org/pdf/2103.00020.pdf) açıklanmaktadır.

Bu model önceden eğitildiğinde, ona bir grup görüntü ve bir grup metin istemi verebiliriz ve o da bize olasılıklarla dolu bir tensör döndürecektir. CLIP, çeşitli görevler için kullanılabilir:

**Görüntü Sınıflandırması**

Diyelim ki, görüntüleri kediler, köpekler ve insanlar arasında sınıflandırmamız gerekiyor. Bu durumda, modele bir görüntü ve bir dizi metin istemi verebiliriz: "*bir kedinin resmi*", "*bir köpeğin resmi*", "*bir insanın resmi*". Sonuçta elde edilen 3 olasılık vektöründe, sadece en yüksek değere sahip olan indeksi seçmemiz yeterlidir.

![CLIP ile Görüntü Sınıflandırması](../../../../../translated_images/clip-class.3af42ef0b2b19369a633df5f20ddf4f5a01d6c8ffa181e9d3a0572c19f919f72.tr.png)

> *Resim [bu blog yazısından](https://openai.com/blog/clip/) alınmıştır.*

**Metin Tabanlı Görüntü Arama**

Aynı zamanda tersini de yapabiliriz. Eğer elimizde bir görüntü koleksiyonu varsa, bu koleksiyonu modele geçirebiliriz ve bir metin istemi - bu, verilen bir isteme en benzer görüntüyü bize verecektir.

## ✍️ Örnek: [CLIP ile Görüntü Sınıflandırma ve Görüntü Arama](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

CLIP'in uygulamasını görmek için [Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb) defterini açın.

## VQGAN+ CLIP ile Görüntü Üretimi

CLIP, bir metin isteminden **görüntü üretimi** için de kullanılabilir. Bunu yapmak için, bazı vektör girdilerine dayalı olarak görüntü üretebilen bir **üretici modeline** ihtiyacımız var. Bu tür modellerden biri [VQGAN](https://compvis.github.io/taming-transformers/) (Vektör-Kuantize GAN) olarak adlandırılmaktadır.

VQGAN'ı sıradan [GAN](../../4-ComputerVision/10-GANs/README.md)dan ayıran ana fikirler şunlardır:
* Görüntüyü oluşturan bağlam açısından zengin görsel parçaların bir dizisini üretmek için otoregresif transformer mimarisini kullanmak. Bu görsel parçalar, [CNN](../../4-ComputerVision/07-ConvNets/README.md) tarafından öğrenilmektedir.
* Görüntünün parçalarının "gerçek" mi yoksa "sahte" mi olduğunu tespit eden alt-görüntü ayrımcısı kullanmak (geleneksel GAN'daki "ya hepsi ya hiç" yaklaşımının aksine).

VQGAN hakkında daha fazla bilgi için [Taming Transformers](https://compvis.github.io/taming-transformers/) web sitesini ziyaret edin.

VQGAN ile geleneksel GAN arasındaki önemli farklardan biri, ikincisinin herhangi bir girdi vektöründen makul bir görüntü üretebilmesi iken, VQGAN'ın uyumlu bir görüntü üretme olasılığının daha düşük olmasıdır. Bu nedenle, görüntü oluşturma sürecini daha fazla yönlendirmemiz gerekmektedir ve bu, CLIP kullanılarak yapılabilir.

![VQGAN+CLIP Mimarı](../../../../../translated_images/vqgan.5027fe05051dfa3101950cfa930303f66e6478b9bd273e83766731796e462d9b.tr.png)

Bir metin istemine karşılık gelen bir görüntü üretmek için, VQGAN'dan bir görüntü üretmek üzere geçilen rastgele bir kodlama vektörü ile başlarız. Daha sonra CLIP, görüntünün metin istemine ne kadar iyi uyduğunu gösteren bir kayıp fonksiyonu üretmek için kullanılır. Amaç, bu kaybı minimize etmek ve girdi vektörü parametrelerini ayarlamak için geri yayılım kullanmaktır.

VQGAN+CLIP'i uygulayan harika bir kütüphane [Pixray](http://github.com/pixray/pixray)dir.

![Pixray tarafından üretilen bir resim](../../../../../translated_images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.2384968e9db8a0d09dc96de938b9f95bde8a7e1c721f48f286a7795bf16d56c7.tr.png) |  ![Pixray tarafından üretilen bir resim](../../../../../translated_images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.e0b6495f210a439077e1c32cc8afdf714e634fe24dc78dc5aa45fd2f560b0ed5.tr.png) | ![Pixray tarafından üretilen bir resim](../../../../../translated_images/a_closeup_oil_portrait_of_old_male_teacher_of_math.5362e67aa7fc2683b9d36a613b364deb7454760cd39205623fc1e3938fa133c0.tr.png)
----|----|----
*Bir kedinin resmi* isteminden üretilen resim | *Bir köpeğin resmi* isteminden üretilen resim | *Bir insanın resmi* isteminden üretilen resim

> Resimler **Yapay Öğretmenler** koleksiyonundan [Dmitry Soshnikov](http://soshnikov.com) tarafından alınmıştır.

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-E, istemlerden görüntü üretecek şekilde eğitilmiş bir GPT-3 versiyonudur. 12 milyar parametre ile eğitilmiştir.

CLIP'ten farklı olarak, DALL-E hem metin hem de görüntüyü her iki tür için tek bir token akışı olarak alır. Bu nedenle, birden fazla istemden, metne dayalı görüntüler üretebilirsiniz.

### [DALL-E 2](https://openai.com/dall-e-2)
DALL-E 1 ile 2 arasındaki ana fark, daha gerçekçi görüntüler ve sanat eserleri üretmesidir.

DALL-E ile görüntü üretim örnekleri:
![Pixray tarafından üretilen bir resim](../../../../../translated_images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.6c235e8271d9ed10ce985d86aeb241a58518958647973af136912116b9518fce.tr.png) |  ![Pixray tarafından üretilen bir resim](../../../../../translated_images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.f21dc4166340b6c8b4d1cb57efd1e22127407f9b28c9ac7afe11344065369e64.tr.png) | ![Pixray tarafından üretilen bir resim](../../../../../translated_images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.d331c2dfbdc3f7c46aa65c0809066f5e7ed4b49609cd259852e760df21051e4a.tr.png)
----|----|----
*Bir kedinin resmi* isteminden üretilen resim | *Bir köpeğin resmi* isteminden üretilen resim | *Bir insanın resmi* isteminden üretilen resim

## Kaynaklar

* VQGAN Makalesi: [Yüksek Çözünürlüklü Görüntü Sentezi için Transformer'ları Yola Çıkarma](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* CLIP Makalesi: [Doğal Dil Denetiminden Aktarılan Görsel Modellerin Öğrenilmesi](https://arxiv.org/pdf/2103.00020.pdf)

**Açıklama**:  
Bu belge, makine tabanlı AI çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlış anlamalar içerebileceğini lütfen dikkate alın. Orijinal belge, kendi dilinde otoriter kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul etmiyoruz.