# Üretken ağlar

## [Ders öncesi quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/117)

Tekrarlayan Sinir Ağları (RNN'ler) ve Long Short Term Memory Cells (LSTM'ler) ile Gated Recurrent Units (GRU'lar) gibi kapalı hücre varyantları, dil modellemesi için bir mekanizma sağladı; çünkü kelime sıralamasını öğrenebilirler ve bir dizideki bir sonraki kelime için tahminlerde bulunabilirler. Bu, RNN'leri **üretken görevler** için kullanmamıza olanak tanır; örneğin sıradan metin oluşturma, makine çevirisi ve hatta görüntü başlığı oluşturma.

> ✅ Yazarken metin tamamlama gibi üretken görevlerden faydalandığınız tüm zamanları düşünün. Favori uygulamalarınızda RNN'lerin kullanılıp kullanılmadığını görmek için biraz araştırma yapın.

Önceki biriminde tartıştığımız RNN mimarisinde, her RNN birimi bir sonraki gizli durumu bir çıktı olarak üretmiştir. Ancak, her tekrarlayan birime bir başka çıktı ekleyebiliriz; bu da bize **dizi** (orijinal dizinin uzunluğuna eşit) çıktısı vermemizi sağlar. Ayrıca, her adımda bir giriş kabul etmeyen RNN birimleri kullanabiliriz; sadece bazı başlangıç durumu vektörlerini alır ve ardından bir çıktı dizisi üretebiliriz.

Bu, aşağıdaki resimde gösterilen farklı sinir mimarilerine olanak tanır:

![Yaygın tekrarlayan sinir ağı desenlerini gösteren bir resim.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.tr.jpg)

> Resim [Andrej Karpaty](http://karpathy.github.io/) tarafından [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) başlıklı blog yazısından alınmıştır.

* **Bir-bir** bir giriş ve bir çıkışı olan geleneksel bir sinir ağıdır.
* **Bir-çok** bir giriş değeri kabul eden ve bir çıktı değeri dizisi üreten üretken bir mimaridir. Örneğin, bir resmi metin olarak tanımlayan bir **görüntü başlığı oluşturma** ağı eğitmek istiyorsak, resmi giriş olarak alabiliriz, bir CNN'den geçirerek gizli durumunu elde edebiliriz ve ardından tekrarlayan bir zincir ile başlık kelimelerini kelime kelime üretebiliriz.
* **Çok-bir** önceki birimde tanımladığımız RNN mimarilerine karşılık gelir, örneğin metin sınıflandırma.
* **Çok-çok**, veya **diziye-dizi** ise **makine çevirisi** gibi görevlerle ilgilidir; burada ilk RNN, giriş dizisinden tüm bilgileri gizli duruma toplar ve başka bir RNN zinciri bu durumu çıktı dizisine açar.

Bu birimde, metin oluşturmaya yardımcı olan basit üretken modellere odaklanacağız. Kolaylık olması açısından, karakter düzeyinde tokenizasyon kullanacağız.

Bu RNN'yi adım adım metin üretmesi için eğiteceğiz. Her adımda, `nchars` uzunluğunda bir karakter dizisi alacağız ve ağa her giriş karakteri için bir sonraki çıktı karakterini üretmesini isteyeceğiz:

!['HELLO' kelimesinin RNN ile üretilmesini gösteren bir örnek resim.](../../../../../translated_images/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.tr.png)

Metin oluştururken (çıkarım sırasında), bazı **uyarıcılarla** başlarız; bu, RNN hücrelerinden geçirilerek ara durumunu üretir ve ardından bu durumdan üretim başlar. Bir seferde bir karakter üretiriz ve durumu ve üretilen karakteri bir sonraki RNN hücresine geçirerek bir sonraki karakteri üretiriz; yeterli karakter ürettiğimizdeye kadar devam ederiz.

<img src="images/rnn-generate-inf.png" width="60%"/>

> Resim yazar tarafından

## ✍️ Alıştırmalar: Üretken Ağlar

Aşağıdaki not defterlerinde öğrenmeye devam edin:

* [PyTorch ile Üretken Ağlar](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb)
* [TensorFlow ile Üretken Ağlar](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)

## Yumuşak metin oluşturma ve sıcaklık

Her RNN hücresinin çıktısı, karakterlerin bir olasılık dağılımıdır. Eğer her zaman en yüksek olasılığa sahip karakteri üretilen metindeki bir sonraki karakter olarak alırsak, metin genellikle aynı karakter dizileri arasında "dönmeye" başlayabilir; bu örnekte olduğu gibi:

```
today of the second the company and a second the company ...
```

Ancak, bir sonraki karakterin olasılık dağılımına baktığımızda, en yüksek birkaç olasılık arasındaki farkın çok büyük olmayabileceği durumlar vardır; örneğin, bir karakterin olasılığı 0.2, diğerinin 0.19 olabilir. Örneğin, '*play*' dizisinde bir sonraki karakter, ya boşluk ya da **e** (örneğin *player* kelimesinde olduğu gibi) olabilir.

Bu, daha yüksek olasılığa sahip karakteri seçmenin her zaman "adil" olmadığını sonucuna götürür; çünkü ikinci en yüksek olanı seçmek de anlamlı bir metne yol açabilir. **Olasılık dağılımından** karakterler **örneklemek** daha akıllıcadır. Ayrıca, daha fazla rastgelelik eklemek istiyorsak olasılık dağılımını düzleştirecek bir parametre, **sıcaklık** kullanabiliriz; ya da en yüksek olasılığa sahip karakterlere daha fazla bağlı kalmak istiyorsak daha dik bir hale getirebiliriz.

Bu yumuşak metin oluşturmanın yukarıda bağlantılı not defterlerinde nasıl uygulandığını keşfedin.

## Sonuç

Metin oluşturma kendi başına yararlı olsa da, asıl faydalar, RNN'ler kullanarak bazı başlangıç özellik vektörlerinden metin üretebilme yeteneğinden gelir. Örneğin, metin oluşturma, makine çevirisinin bir parçası olarak kullanılır (bu durumda *encoder*'dan gelen durum vektörü, çevrilen mesajı üretmek veya *decode* etmek için kullanılır) veya bir görüntünün metinsel tanımını oluşturma (bu durumda özellik vektörü CNN çıkarıcısından gelir).

## 🚀 Zorluk

Bu konuda Microsoft Learn'da bazı dersler alın

* Metin Oluşturma ile [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Ders sonrası quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/217)

## Gözden Geçirme & Kendi Kendine Çalışma

Bilgilerinizi genişletmek için bazı makaleler

* Markov Zinciri, LSTM ve GPT-2 ile metin oluşturmanın farklı yaklaşımları: [blog yazısı](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* [Keras belgelerinde](https://keras.io/examples/generative/lstm_character_level_text_generation/) metin oluşturma örneği

## [Görev](lab/README.md)

Karakter karakter metin oluşturmanın nasıl yapıldığını gördük. Laboratuvar ortamında, kelime düzeyinde metin oluşturmayı keşfedeceksiniz.

**Açıklama**:  
Bu belge, makine tabanlı AI çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk konusunda çaba göstersek de, otomatik çevirilerin hatalar veya yanlış anlamalar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımı sonucunda ortaya çıkan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.