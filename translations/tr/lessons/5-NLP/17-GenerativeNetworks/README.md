<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9de7847385eeeda67cfdcce1640ab72",
  "translation_date": "2025-08-26T07:21:08+00:00",
  "source_file": "lessons/5-NLP/17-GenerativeNetworks/README.md",
  "language_code": "tr"
}
-->
# Üretken Ağlar

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ai/quiz/33)

Tekrarlayan Sinir Ağları (RNN'ler) ve Uzun Kısa Süreli Bellek Hücreleri (LSTM'ler) ile Gated Recurrent Units (GRU'ler) gibi kapılı hücre varyantları, dil modelleme için bir mekanizma sağlar. Bu mekanizma, kelime sıralamasını öğrenebilir ve bir dizideki bir sonraki kelime için tahminler sunabilir. Bu, RNN'lerin **üretken görevler** için kullanılmasını sağlar; örneğin, sıradan metin üretimi, makine çevirisi ve hatta görüntü açıklaması.

> ✅ Yazarken metin tamamlama gibi üretken görevlerden faydalandığınız tüm zamanları düşünün. Favori uygulamalarınızın RNN'leri kullanıp kullanmadığını görmek için biraz araştırma yapın.

Önceki birimde tartıştığımız RNN mimarisinde, her RNN birimi bir sonraki gizli durumu çıktı olarak üretir. Ancak, her tekrarlayan birime başka bir çıktı ekleyebiliriz, bu da bir **dizi** (orijinal dizinin uzunluğuna eşit) üretmemizi sağlar. Ayrıca, her adımda bir giriş kabul etmeyen ve sadece bir başlangıç durum vektörü alarak bir çıktı dizisi üreten RNN birimleri kullanabiliriz.

Bu, aşağıdaki resimde gösterilen farklı sinir mimarilerini mümkün kılar:

![Yaygın tekrarlayan sinir ağı desenlerini gösteren resim.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.tr.jpg)

> Resim, [Andrej Karpaty](http://karpathy.github.io/) tarafından yazılan [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) blog yazısından alınmıştır.

* **Bire bir**: Bir giriş ve bir çıkış ile geleneksel bir sinir ağıdır.
* **Bire çok**: Bir giriş değeri kabul eden ve bir çıktı değerleri dizisi üreten üretken bir mimaridir. Örneğin, bir **görüntü açıklama** ağı eğitmek istiyorsak, bir resmi giriş olarak alabilir, bir CNN'den geçirerek gizli durumunu elde edebilir ve ardından bir tekrarlayan zincir açıklamayı kelime kelime üretebiliriz.
* **Çoktan bire**: Önceki birimde tanımladığımız RNN mimarilerine karşılık gelir, örneğin metin sınıflandırma.
* **Çoktan çoğa** veya **diziden diziye**: **Makine çevirisi** gibi görevlere karşılık gelir. Burada, ilk RNN giriş dizisinden tüm bilgiyi gizli duruma toplar ve başka bir RNN zinciri bu durumu çıktı dizisine açar.

Bu birimde, metin üretmemize yardımcı olan basit üretken modeller üzerine odaklanacağız. Basitlik için karakter düzeyinde tokenizasyon kullanacağız.

Bu RNN'yi adım adım metin üretmek için eğiteceğiz. Her adımda, `nchars` uzunluğunda bir karakter dizisi alacağız ve ağdan her giriş karakteri için bir sonraki çıktı karakterini üretmesini isteyeceğiz:

![RNN'nin 'HELLO' kelimesini üretme örneğini gösteren resim.](../../../../../translated_images/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.tr.png)

Metin üretirken (çıkarsama sırasında), bazı **başlangıç noktası** ile başlarız. Bu başlangıç noktası RNN hücrelerinden geçirilerek ara durumu oluşturur ve ardından bu durumdan üretim başlar. Her seferinde bir karakter üretiriz ve durumu ve üretilen karakteri bir sonraki karakteri üretmek için başka bir RNN hücresine geçiririz. Bu işlem yeterli sayıda karakter üretilene kadar devam eder.

<img src="images/rnn-generate-inf.png" width="60%"/>

> Resim, yazar tarafından oluşturulmuştur.

## ✍️ Alıştırmalar: Üretken Ağlar

Aşağıdaki not defterlerinde öğrenmeye devam edin:

* [PyTorch ile Üretken Ağlar](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb)
* [TensorFlow ile Üretken Ağlar](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)

## Yumuşak Metin Üretimi ve Sıcaklık

Her RNN hücresinin çıktısı bir karakter olasılık dağılımıdır. Eğer üretilen metindeki bir sonraki karakter olarak her zaman en yüksek olasılığa sahip karakteri seçersek, metin genellikle aynı karakter dizileri arasında "dönmeye" başlayabilir, aşağıdaki örnekte olduğu gibi:

```
today of the second the company and a second the company ...
```

Ancak, bir sonraki karakter için olasılık dağılımına bakarsak, en yüksek olasılıklardan birkaçının arasındaki farkın büyük olmadığını görebiliriz. Örneğin, bir karakterin olasılığı 0.2, diğerinin ise 0.19 olabilir. Örneğin, '*play*' dizisindeki bir sonraki karakter, boşluk veya **e** (kelime *player*'daki gibi) olabilir.

Bu, her zaman en yüksek olasılığa sahip karakteri seçmenin "adil" olmadığını gösterir, çünkü ikinci en yüksek olasılığa sahip karakteri seçmek de anlamlı bir metin oluşturabilir. Daha akıllıca bir yaklaşım, ağ çıktısının verdiği olasılık dağılımından karakterleri **örneklemek** olacaktır. Ayrıca, olasılık dağılımını düzleştirmek veya daha dik hale getirmek için **sıcaklık** adlı bir parametre kullanabiliriz. Bu, daha fazla rastgelelik eklemek veya en yüksek olasılıklı karakterlere daha fazla bağlı kalmak istediğimizde işe yarar.

Bu yumuşak metin üretiminin yukarıdaki not defterlerinde nasıl uygulandığını keşfedin.

## Sonuç

Metin üretimi kendi başına faydalı olabilir, ancak asıl avantajlar, RNN'ler kullanılarak bir başlangıç özellik vektöründen metin üretme yeteneğinden gelir. Örneğin, metin üretimi makine çevirisinin bir parçası olarak kullanılır (diziden diziye, bu durumda *kodlayıcı*dan gelen durum vektörü çevrilen mesajı üretmek veya *çözmek* için kullanılır) veya bir görüntünün metinsel açıklamasını üretmek için kullanılır (bu durumda özellik vektörü CNN çıkarıcısından gelir).

## 🚀 Meydan Okuma

Bu konuyla ilgili Microsoft Learn'de bazı dersler alın:

* [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste) ile Metin Üretimi

## [Ders Sonrası Test](https://ff-quizzes.netlify.app/en/ai/quiz/34)

## İnceleme ve Kendi Kendine Çalışma

Bilginizi genişletmek için bazı makaleler:

* Markov Zinciri, LSTM ve GPT-2 ile metin üretimine farklı yaklaşımlar: [blog yazısı](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* [Keras dokümantasyonu](https://keras.io/examples/generative/lstm_character_level_text_generation/) içinde metin üretim örneği

## [Ödev](lab/README.md)

Metni karakter karakter nasıl üreteceğimizi gördük. Laboratuvarda, kelime düzeyinde metin üretimini keşfedeceksiniz.

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.