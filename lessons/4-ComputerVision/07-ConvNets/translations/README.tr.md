# Evrişimli Sinir Ağları

Sinir ağlarının imgelerle başa çıkmada oldukça iyi olduğunu ve tek katmanlı algılayıcının bile MNIST veri kümesinden el yazısı rakamları makul bir doğrulukla tanıyabildiğini daha önce gördük. Ancak, MNIST veri kümesi çok özeldir ve tüm rakamlar imgenin içinde ortalanır, bu da görevi kolaylaştırır.

## [Ders öncesi sınavı](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/107)

Gerçek hayatta, resimdeki nesneleri, imgedeki tam konumlarından bağımsız olarak tanıyabilmek istiyoruz. Bilgisayarla görme, genel sınıflandırmadan farklıdır, çünkü resimde belirli bir nesneyi bulmaya çalışırken, belirli **örüntüleri** ve bunların kombinasyonlarını arayarak imgeyi tarıyoruz. Örneğin, bir kedi ararken, önce bıyık oluşturabilen yatay çizgilere bakabiliriz ve ardından belirli bir bıyık kombinasyonu bize bunun aslında bir kedi resmi olduğunu söyleyebilir. İmge üzerindeki tam konumları değil, belirli örüntülerin göreli konumu ve varlığı önemlidir.

Örüntüleri çıkarmak için **evrişimli filtreler** kavramını kullanacağız. Bildiğiniz gibi, bir imge bir 2B matris veya renk derinliği olan bir 3B tensör ile temsil edilir. Filtre uygulamak, nispeten küçük **filtre çekirdeği** matrisi almamız ve orijinal imgedeki her piksel için komşu noktalarla ağırlıklı ortalamayı hesaplamamız anlamına gelir. Bunu, tüm imgenin üzerinde kayan ve filtre çekirdeği matrisindeki ağırlıklara göre tüm piksellerin ortalamasını alan küçük bir pencere gibi görebiliriz.

![Dikey Kenar Filtresi](../images/filter-vert.png) | ![Yatay Kenar Filtresi](../images/filter-horiz.png)
----|----

> Imge sahibi Dmitry Soshnikov

For example, if we apply 3x3 vertical edge and horizontal edge filters to the MNIST digits, we can get highlights (e.g. high values) where there are vertical and horizontal edges in our original image. Thus those two filters can be used to "look for" edges. Similarly, we can design different filters to look for other low-level patterns:

Örneğin, MNIST rakamlarına 3x3 dikey kenar ve yatay kenar filtreleri uygularsak, orijinal imgemizde dikey ve yatay kenarların olduğu yerlerde vurgular (mesela yüksek değerler) elde edebiliriz. Böylece bu iki filtre kenarları "aramak" için kullanılabilir. Benzer şekilde, diğer düşük seviye kalıpları aramak için farklı filtreler tasarlayabiliriz:

<img src="../images/lmfilters.jpg" width="500" align="center"/>


> [Leung-Malik Filtre Bankası](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

Ancak, bazı örüntüleri manuel olarak çıkaracak filtreleri tasarlayabildiğimiz gibi, ağı otomatik olarak örüntüleri öğrenecek şekilde de tasarlayabiliriz. CNN'in arkasındaki ana fikirlerden biridir.

## CNN'in Arkasındaki Ana Fikirler

CNN'lerin çalışma şekli aşağıdaki önemli fikirlere dayanmaktadır:

* Evrişimli filtreler örüntüleri çıkarabilir.
* Ağı, filtrelerin otomatik olarak eğitileceği şekilde tasarlayabiliriz.
* Sadece orijinal imgede değil, üst düzey özniteliklerde de örüntü bulmak için aynı yaklaşımı kullanabiliriz. Böylece, CNN öznitelik çıkarımı, düşük seviyeli piksel kombinasyonlarından başlayıp daha yüksek seviyeli resim parçaları kombinasyonuna kadar bir öznitelikler hiyerarşisi üzerinde çalışır.

![Hiyerarşik Öznitelik Çıkarma](../images/FeatureExtractionCNN.png)

> [Hislop-Lynch'in bir makalesinden](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d) imge, onların ilgili [araştırmalarına](https://dl.acm.org/doi/abs/10.1145/1553374.1553453) dayanan.

## ✍️ Alıştırmalar: Evrişimli Sinir Ağları

Evrişimli sinir ağlarının nasıl çalıştığını ve eğitilebilir filtreleri nasıl elde edebileceğimizi ilgili not defterleri üzerinde çalışarak keşfetmeye devam edelim:

* [Evrişimli Sinir Ağları - PyTorch](ConvNetsPyTorch.tr.ipynb)
* [Evrişimli Sinir Ağları - TensorFlow](ConvNetsTF.tr.ipynb)

## Piramit Mimarisi

İmge işleme için kullanılan CNN'lerin çoğu, sözde bir piramit mimarisini takip eder. Orijinal imgelere uygulanan birinci evrişimli katman, tipik olarak, yatay/dikey kontur çizgileri gibi farklı piksel kombinasyonlarına karşılık gelen nispeten düşük sayıda filtreye (8-16) sahiptir. Bir sonraki aşamada, ağın uzamsal boyutunu azaltıyoruz ve basit özniteliklerin daha olası kombinasyonlarına karşılık gelen filtre sayısını artırıyoruz. Her katmanda son sınıflandırıcıya doğru gidildikçe imgenin uzamsal boyutları küçülür ve filtre sayısı artar.

Örnek olarak, 2014 yılında ImageNet'in ilk 5 sıralamasında %92.7 doğruluk elde eden bir ağ olan VGG-16'nın mimarisine bakalım:

![ImageNet Katmanları](../images/vgg-16-arch1.jpg)

![ImageNet Piramidi](../images/vgg-16-arch.jpg)

> İmge [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)'den

## En İyi Bilinen CNN Mimarileri

[En iyi bilinen CNN mimarileri hakkında çalışmanıza devam edin](CNN_Architectures.tr.md)