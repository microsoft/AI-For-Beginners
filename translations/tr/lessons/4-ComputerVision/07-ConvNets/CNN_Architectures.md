<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f7b97b375358cb51a1e098df306bf73",
  "translation_date": "2025-08-26T07:28:38+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md",
  "language_code": "tr"
}
-->
# Bilinen CNN Mimarileri

### VGG-16

VGG-16, 2014 yılında ImageNet top-5 sınıflandırmasında %92.7 doğruluk oranına ulaşan bir ağdır. Aşağıdaki katman yapısına sahiptir:

![ImageNet Katmanları](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.tr.jpg)

Gördüğünüz gibi, VGG geleneksel bir piramit mimarisini takip eder; bu, bir dizi evrişim-havuzlama katmanıdır.

![ImageNet Piramidi](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.tr.jpg)

> Görsel [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493) kaynağından alınmıştır.

### ResNet

ResNet, 2015 yılında Microsoft Research tarafından önerilen bir model ailesidir. ResNet'in ana fikri, **artık blokları** kullanmaktır:

<img src="images/resnet-block.png" width="300"/>

> Görsel [bu makaleden](https://arxiv.org/pdf/1512.03385.pdf) alınmıştır.

Kimlik geçişini kullanmanın nedeni, katmanımızın bir önceki katmanın sonucu ile artık bloğun çıktısı arasındaki **farkı** tahmin etmesini sağlamaktır - bu nedenle adına *artık* denir. Bu bloklar eğitilmesi çok daha kolaydır ve bu bloklardan yüzlercesiyle ağlar oluşturulabilir (en yaygın varyantlar ResNet-52, ResNet-101 ve ResNet-152'dir).

Bu ağı, veri setine göre karmaşıklığını ayarlayabilen bir yapı olarak da düşünebilirsiniz. Başlangıçta, ağı eğitmeye başladığınızda, ağırlık değerleri küçüktür ve sinyalin çoğu kimlik geçiş katmanlarından geçer. Eğitim ilerledikçe ve ağırlıklar büyüdükçe, ağ parametrelerinin önemi artar ve ağ, eğitim görüntülerini doğru bir şekilde sınıflandırmak için gereken ifade gücünü karşılayacak şekilde kendini ayarlar.

### Google Inception

Google Inception mimarisi bu fikri bir adım öteye taşır ve her ağ katmanını birkaç farklı yolun bir kombinasyonu olarak inşa eder:

<img src="images/inception.png" width="400"/>

> Görsel [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454) kaynağından alınmıştır.

Burada, 1x1 evrişimlerin rolünü vurgulamak gerekir, çünkü ilk bakışta mantıklı görünmeyebilir. Görüntüyü neden 1x1 filtreyle taramamız gerekiyor? Ancak, evrişim filtrelerinin aynı zamanda birkaç derinlik kanalında (başlangıçta - RGB renkleri, sonraki katmanlarda - farklı filtreler için kanallar) çalıştığını unutmamalısınız ve 1x1 evrişim, bu giriş kanallarını farklı eğitilebilir ağırlıklarla birleştirmek için kullanılır. Ayrıca kanal boyutunda bir alt örnekleme (havuzlama) olarak da görülebilir.

Bu konuda [iyi bir blog yazısı](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) ve [orijinal makale](https://arxiv.org/pdf/1312.4400.pdf) bulunmaktadır.

### MobileNet

MobileNet, mobil cihazlar için uygun, boyutları küçültülmüş bir model ailesidir. Kaynaklarınız sınırlıysa ve biraz doğruluk kaybını göze alabiliyorsanız, bu modelleri kullanabilirsiniz. Bu modellerin arkasındaki ana fikir, **derinlik ayrılabilir evrişim** olarak adlandırılan bir tekniktir. Bu teknik, evrişim filtrelerini, uzaysal evrişimlerin ve derinlik kanalları üzerinde 1x1 evrişimlerin bir bileşimi olarak temsil etmeye olanak tanır. Bu, parametre sayısını önemli ölçüde azaltır, ağı daha küçük hale getirir ve daha az veriyle eğitilmesini kolaylaştırır.

İşte [MobileNet hakkında iyi bir blog yazısı](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Sonuç

Bu bölümde, bilgisayarla görme sinir ağlarının temel konseptini - evrişimli ağları öğrendiniz. Görüntü sınıflandırma, nesne algılama ve hatta görüntü oluşturma ağlarını destekleyen gerçek yaşam mimarilerinin hepsi CNN'lere dayanır, sadece daha fazla katman ve bazı ek eğitim hileleriyle.

## 🚀 Meydan Okuma

Eşlik eden defterlerde, daha yüksek doğruluk elde etmenin yolları hakkında notlar bulunmaktadır. Daha yüksek doğruluk elde edip edemeyeceğinizi görmek için bazı deneyler yapın.

## [Ders Sonrası Test](https://ff-quizzes.netlify.app/en/ai/quiz/14)

## Gözden Geçirme ve Kendi Kendine Çalışma

CNN'ler genellikle Bilgisayarla Görme görevlerinde kullanılsa da, sabit boyutlu desenleri çıkarmada genel olarak iyidirler. Örneğin, seslerle çalışıyorsak, ses sinyalinde bazı belirli desenleri aramak için de CNN'leri kullanmak isteyebiliriz - bu durumda filtreler 1 boyutlu olur (ve bu CNN'e 1D-CNN denir). Ayrıca, bazen çok boyutlu uzayda özellikleri çıkarmak için 3D-CNN kullanılır, örneğin videoda meydana gelen belirli olaylar - CNN, zaman içinde değişen belirli özellik desenlerini yakalayabilir. CNN'lerle yapılabilecek diğer görevler hakkında biraz araştırma ve kendi kendine çalışma yapın.

## [Görev](lab/README.md)

Bu laboratuvarda, farklı kedi ve köpek ırklarını sınıflandırma görevi verilmektedir. Bu görüntüler, MNIST veri setinden daha karmaşıktır, daha yüksek boyutlardadır ve 10'dan fazla sınıf bulunmaktadır.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.