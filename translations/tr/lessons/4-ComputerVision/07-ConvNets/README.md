# Konvolüsyonel Sinir Ağları

Daha önce sinir ağlarının görüntülerle başa çıkmada oldukça iyi olduğunu ve hatta tek katmanlı algılayıcıların MNIST veri setinden el yazısı rakamlarını makul bir doğrulukla tanıyabildiğini gördük. Ancak, MNIST veri seti çok özel bir durumdur ve tüm rakamlar görüntünün içinde merkezlenmiştir, bu da görevi daha basit hale getirir.

## [Ön-dersten sınav](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/107)

Gerçek hayatta, bir resimde nesneleri tam konumlarına bakmaksızın tanıyabilmemiz gerekir. Bilgisayarla görme, genel sınıflandırmadan farklıdır, çünkü bir resimde belirli bir nesneyi bulmaya çalışırken, belirli **desenleri** ve bunların kombinasyonlarını aramak için görüntüyü tarıyoruz. Örneğin, bir kedi ararken önce, bıyıkları oluşturabilecek yatay çizgilere bakabiliriz ve ardından belirli bir bıyık kombinasyonu, bunun gerçekten bir kedi resmi olduğunu bize gösterebilir. Belirli desenlerin göreceli konumu ve varlığı önemlidir, görüntüdeki tam konumları değil.

Desenleri çıkarmak için **konvolüsyonel filtreler** kavramını kullanacağız. Bildiğiniz gibi, bir görüntü 2D-matris veya renk derinliği ile 3D-tensor ile temsil edilir. Bir filtre uygulamak, nispeten küçük bir **filtre çekirdek** matrisini alıp, orijinal görüntüdeki her piksel için komşu noktalarla ağırlıklı ortalama hesaplamak anlamına gelir. Bunu, görüntünün üzerinde kaydırılan küçük bir pencere gibi düşünebiliriz ve filtre çekirdek matrisindeki ağırlıklara göre tüm pikselleri ortalıyoruz.

![Dikey Kenar Filtre](../../../../../translated_images/filter-vert.b7148390ca0bc356ddc7e55555d2481819c1e86ddde9dce4db5e71a69d6f887f.tr.png) | ![Yatay Kenar Filtre](../../../../../translated_images/filter-horiz.59b80ed4feb946efbe201a7fe3ca95abb3364e266e6fd90820cb893b4d3a6dda.tr.png)
----|----

> Görüntü Dmitry Soshnikov'dan

Örneğin, MNIST rakamlarına 3x3 dikey kenar ve yatay kenar filtreleri uygularsak, orijinal görüntümüzdeki dikey ve yatay kenarların bulunduğu yerlerde vurgular (örneğin, yüksek değerler) alabiliriz. Böylece bu iki filtre, kenarları "arama" için kullanılabilir. Benzer şekilde, diğer düşük seviyeli desenleri aramak için farklı filtreler tasarlayabiliriz:
Veriler Ekim 2023'e kadar eğitim aldınız.

> [Leung-Malik Filtre Bankası](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html) görüntüsü

Ancak, bazı desenleri manuel olarak çıkarmak için filtreleri tasarlayabilsek de, ağı bu desenleri otomatik olarak öğrenmesi için tasarlayabiliriz. Bu, CNN'in arkasındaki ana fikirlerden biridir.

## CNN'in Ana Fikirleri

CNN'lerin çalışma şekli, aşağıdaki önemli fikirlere dayanır:

* Konvolüsyonel filtreler desenleri çıkarabilir
* Ağı, filtrelerin otomatik olarak eğitilmesini sağlayacak şekilde tasarlayabiliriz
* Aynı yaklaşımı, yalnızca orijinal görüntüde değil, yüksek seviyeli özelliklerde desenler bulmak için de kullanabiliriz. Böylece CNN özellik çıkarımı, düşük seviyeli piksel kombinasyonlarından başlayarak, resim parçalarının daha yüksek seviyeli kombinasyonlarına kadar bir özellik hiyerarşisi üzerinde çalışır.

![Hiyerarşik Özellik Çıkarma](../../../../../translated_images/FeatureExtractionCNN.d9b456cbdae7cb643fde3032b81b2940e3cf8be842e29afac3f482725ba7f95c.tr.png)

> [Hislop-Lynch'in bir makalesinden](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d) alınan görüntü, [araştırmalarına dayanmaktadır](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Alıştırmalar: Konvolüsyonel Sinir Ağları

Konvolüsyonel sinir ağlarının nasıl çalıştığını ve nasıl eğitilebilir filtreler elde edebileceğimizi keşfetmeye devam edelim, ilgili defterler üzerinden çalışarak:

* [Konvolüsyonel Sinir Ağları - PyTorch](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb)
* [Konvolüsyonel Sinir Ağları - TensorFlow](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)

## Piramit Mimarisi

Görüntü işleme için kullanılan çoğu CNN, sözde bir piramit mimarisini takip eder. Orijinal görüntülere uygulanan ilk konvolüsyonel katman genellikle nispeten düşük sayıda filtreye (8-16) sahiptir ve bu filtreler yatay/dikey çizgiler gibi farklı piksel kombinasyonlarına karşılık gelir. Bir sonraki seviyede, ağın mekansal boyutunu azaltır ve filtre sayısını artırırız, bu da daha fazla basit özellik kombinasyonuna karşılık gelir. Her katmanda, son sınıflandırıcıya doğru ilerledikçe, görüntünün mekansal boyutları azalır ve filtre sayısı artar.

Örneğin, 2014'te ImageNet'in en iyi-5 sınıflandırmasında %92.7 doğruluk elde eden VGG-16 ağının mimarisine bakalım:

![ImageNet Katmanları](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.tr.jpg)

![ImageNet Piramidi](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.tr.jpg)

> [Researchgate'den](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493) alınan görüntü

## En İyi Bilinen CNN Mimarileri

[En iyi bilinen CNN mimarileri hakkında çalışmaya devam edin](CNN_Architectures.md)

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk konusunda çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen dikkate alın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.