# Sinir Ağları Çerçeveleri

Daha önce öğrendiğimiz gibi, sinir ağlarını verimli bir şekilde eğitebilmek için iki şey yapmamız gerekiyor:

* Tensörler üzerinde çalışmak için, örn. sigmoid veya softmaks gibi bazı işlevleri çarpmak, toplamak ve hesaplamak
* Gradyan inişi eniyileme gerçekleştirmek için tüm ifadelerin gradyanlarını hesaplamak

## [Ders öncesi sınavı](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/105)

`numpy` kitaplığı ilk kısmı yapabilirken, gradyanları hesaplamak için bazı mekanizmalara ihtiyacımız var. Önceki bölümde geliştirdiğimiz [çerçevemiz](../../04-OwnFramework/translations/OwnFramework.tr.ipynb)de tüm türev fonksiyonlarını geri yayan `backward` (geri) yöntemi içinde elle programlamamız gerekiyordu. İdeal olarak, bir çerçeve bize tanımlayabileceğimiz *herhangi bir ifadenin* gradyanlarını hesaplama fırsatı vermelidir.

Bir diğer önemli şey de hesaplamaları GPU'da veya [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit) gibi diğer özelleştirilmiş işlem birimlerinde gerçekleştirebilmektir. Derin sinir ağı eğitimi *çok* hesaplama gerektirir ve bu hesaplamaları GPU'larda paralel hale getirebilmek çok önemlidir.

> ✅ 'Paralelleştirme' terimi, hesaplamaları birden fazla cihaza dağıtmak anlamına gelir.

Şu anda en popüler iki sinirsel çerçeve şunlardır: [TensorFlow](http://TensorFlow.org) ve [PyTorch](https://pytorch.org/). Her ikisi de hem CPU hem de GPU üzerinde tensörlerle çalışmak için düşük düzey bir API sağlar. Düşük düzey API'nin yanı sıra, buna uygun olarak [Keras](https://keras.io/) ve [PyTorch Lightning](https://pytorchlightning.ai/) olarak adlandırılan daha üst düzey API de vardır.

Düşük düzey API | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
--------------|-------------------------------------|--------------------------------
Üst düzey API| [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**Düşük düzey API'ler** her iki çerçevede de **hesaplamalı çizgeler** oluşturmanıza olanak tanır. Bu çizge, verilen girdi parametreleriyle çıktının (genellikle kayıp işlevi) nasıl hesaplanacağını tanımlar ve varsa GPU'da hesaplama için gönderilebilir. Bu hesaplama çizgesinde türev almak ve daha sonra model parametrelerini optimize etmede kullanılabilecek gradyanları hesaplamak için işlevler vardır.

**Üst düzey API'ler** sinir ağlarını bir **katmanlar dizisi** olarak kabul eder ve sinir ağlarının çoğunu oluşturmayı çok daha kolay hale getirir. Modeli eğitmek genellikle verilerin hazırlanmasını ve ardından işi yapmak için bir `fit` (oturt) işlevinin çağrılmasını gerektirir.

Üst düzey API, çok fazla ayrıntı hakkında endişelenmeden tipik sinir ağlarını çok hızlı bir şekilde oluşturmanıza olanak tanır. Aynı zamanda, düşük seviyeli API, eğitim süreci üzerinde çok daha fazla kontrol sunar ve bu nedenle, yeni sinir ağı mimarileriyle uğraşırken araştırmalarda çok kullanılırlar.

Her iki API'yi birlikte kullanabileceğinizi anlamak da önemlidir, örn. düşük seviyeli API kullanarak kendi ağ katmanı mimarinizi geliştirebilir ve ardından bunu yüksek seviyeli API ile oluşturulmuş ve eğitilmiş daha büyük ağ içinde kullanabilirsiniz. Ayrıca bir dizi katman olarak üst düzey API'yi kullanarak bir ağ tanımlayabilir ve ardından eniyilemeyi gerçekleştirmek için kendi düşük düzeyli eğitim döngünüzü kullanabilirsiniz. Her iki API de aynı basit temel kavramları kullanır ve birlikte iyi çalışacak şekilde tasarlanmışlardır.

## Öğrenme

Bu kursta, içeriğin çoğunu hem PyTorch hem de TensorFlow için sunuyoruz. Tercih ettiğiniz çerçeveyi seçebilir ve yalnızca ilgili not defterlerini inceleyebilirsiniz. Hangi çerçeveyi seçeceğinizden emin değilseniz, internette **PyTorch ve TensorFlow** ile ilgili bazı tartışmaları okuyun. Daha iyi anlamak için her iki çerçeveye de bakabilirsiniz.

Mümkün olduğunda, basitlik için üst düzey API'leri kullanacağız. Ancak, sinir ağlarının sıfırdan nasıl çalıştığını anlamanın önemli olduğuna inanıyoruz, bu nedenle başlangıçta düşük seviye API ve tensörlerle çalışmaya başlıyoruz. Ancak, hızlı ilerlemek istiyorsanız ve bu ayrıntıları öğrenmek için çok fazla zaman harcamak istemiyorsanız, bunları atlayabilir ve doğrudan üst düzey API not defterlerine geçebilirsiniz.

## ✍️ Alıştırmalar: Çerçeveler

Öğrenmenize aşağıdaki not defterlerinde devam edin:

Düşük düzey API | [TensorFlow+Keras Not Defteri](IntroKerasTF.tr.ipynb) | [PyTorch](IntroPyTorch.tr.ipynb)
--------------|-------------------------------------|--------------------------------
Üst düzey API| [Keras](IntroKeras.tr.pynb) | *PyTorch Lightning*

Çerçevelere hakim olduktan sonra, [aşırı öğrenme](Overfitting.tr.md) kavramını tekrarlayalım.