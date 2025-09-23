<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a560d5b845962cf33dc102266e409568",
  "translation_date": "2025-09-23T08:38:27+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/README.md",
  "language_code": "tr"
}
-->
# Evrişimsel Sinir Ağları

Daha önce sinir ağlarının görüntülerle oldukça iyi başa çıktığını görmüştük; hatta tek katmanlı bir algılayıcı bile MNIST veri setindeki el yazısı rakamları makul bir doğrulukla tanıyabiliyor. Ancak, MNIST veri seti oldukça özeldir ve tüm rakamlar görüntünün ortasına hizalanmıştır, bu da görevi daha basit hale getirir.

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ai/quiz/13)

Gerçek hayatta, bir görüntüdeki nesneleri tam olarak nerede olduklarına bakmaksızın tanıyabilmek isteriz. Bilgisayarla görme, genel sınıflandırmadan farklıdır çünkü bir görüntüde belirli bir nesneyi bulmaya çalışırken, belirli **desenleri** ve bunların kombinasyonlarını arayarak görüntüyü tararız. Örneğin, bir kedi ararken önce yatay çizgiler arayabiliriz, bu çizgiler bıyıkları oluşturabilir ve ardından belirli bir bıyık kombinasyonu bize bunun bir kedi resmi olduğunu söyleyebilir. Belirli desenlerin göreceli konumu ve varlığı önemlidir, ancak görüntüdeki tam konumu önemli değildir.

Desenleri çıkarmak için **evrişimsel filtreler** kavramını kullanacağız. Bildiğiniz gibi, bir görüntü 2D bir matris veya renk derinliği olan bir 3D tensör olarak temsil edilir. Bir filtre uygulamak, nispeten küçük bir **filtre çekirdeği** matrisini alıp, orijinal görüntüdeki her bir piksel için komşu noktalarla ağırlıklı ortalamayı hesaplamak anlamına gelir. Bunu, filtre çekirdeği matrisindeki ağırlıklara göre tüm pikselleri ortalayan küçük bir pencerenin tüm görüntü üzerinde kayması gibi düşünebiliriz.

![Dikey Kenar Filtresi](../../../../../translated_images/filter-vert.b7148390ca0bc356ddc7e55555d2481819c1e86ddde9dce4db5e71a69d6f887f.tr.png) | ![Yatay Kenar Filtresi](../../../../../translated_images/filter-horiz.59b80ed4feb946efbe201a7fe3ca95abb3364e266e6fd90820cb893b4d3a6dda.tr.png)
----|----

> Görsel: Dmitry Soshnikov

Örneğin, MNIST rakamlarına 3x3 boyutunda dikey kenar ve yatay kenar filtreleri uygularsak, orijinal görüntümüzde dikey ve yatay kenarların olduğu yerlerde vurgular (örneğin, yüksek değerler) elde edebiliriz. Bu nedenle, bu iki filtre "kenarları aramak" için kullanılabilir. Benzer şekilde, diğer düşük seviyeli desenleri aramak için farklı filtreler tasarlayabiliriz:

<img src="images/lmfilters.jpg" width="500" align="center"/>

> Görsel: [Leung-Malik Filtre Bankası](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

Ancak, bazı desenleri çıkarmak için filtreleri manuel olarak tasarlayabileceğimiz gibi, ağı filtreleri otomatik olarak öğrenebilecek şekilde de tasarlayabiliriz. Bu, CNN'nin arkasındaki temel fikirlerden biridir.

## CNN'nin Temel Fikirleri

CNN'lerin çalışma şekli şu önemli fikirlere dayanır:

* Evrişimsel filtreler desenleri çıkarabilir.
* Ağı, filtrelerin otomatik olarak eğitileceği şekilde tasarlayabiliriz.
* Aynı yaklaşımı yalnızca orijinal görüntüde değil, yüksek seviyeli özelliklerdeki desenleri bulmak için de kullanabiliriz. Böylece, CNN özellik çıkarımı, düşük seviyeli piksel kombinasyonlarından başlayarak, görüntü parçalarının daha yüksek seviyeli kombinasyonlarına kadar bir özellik hiyerarşisi üzerinde çalışır.

![Hiyerarşik Özellik Çıkarımı](../../../../../translated_images/FeatureExtractionCNN.d9b456cbdae7cb643fde3032b81b2940e3cf8be842e29afac3f482725ba7f95c.tr.png)

> Görsel: [Hislop-Lynch'in bir makalesinden](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), [araştırmalarına dayanarak](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Alıştırmalar: Evrişimsel Sinir Ağları

Evrişimsel sinir ağlarının nasıl çalıştığını ve eğitilebilir filtrelere nasıl ulaşabileceğimizi keşfetmeye devam edelim. Bunun için ilgili defterler üzerinde çalışabilirsiniz:

* [Evrişimsel Sinir Ağları - PyTorch](ConvNetsPyTorch.ipynb)
* [Evrişimsel Sinir Ağları - TensorFlow](ConvNetsTF.ipynb)

## Piramit Mimarisi

Görüntü işleme için kullanılan çoğu CNN, sözde piramit mimarisini takip eder. Orijinal görüntülere uygulanan ilk evrişim katmanı genellikle nispeten az sayıda filtreye (8-16) sahiptir ve bu filtreler yatay/dikey çizgiler gibi farklı piksel kombinasyonlarına karşılık gelir. Bir sonraki seviyede, ağın uzamsal boyutunu azaltır ve basit özelliklerin daha fazla olası kombinasyonuna karşılık gelen filtre sayısını artırırız. Her katmanda, son sınıflandırıcıya doğru ilerledikçe, görüntünün uzamsal boyutları azalır ve filtre sayısı artar.

Örneğin, 2014 yılında ImageNet'in ilk 5 sınıflandırmasında %92.7 doğruluk elde eden VGG-16 ağının mimarisine bakalım:

![ImageNet Katmanları](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.tr.jpg)

![ImageNet Piramidi](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.tr.jpg)

> Görsel: [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## En İyi Bilinen CNN Mimarileri

[En iyi bilinen CNN mimarileri hakkında çalışmaya devam edin](CNN_Architectures.md)

---

