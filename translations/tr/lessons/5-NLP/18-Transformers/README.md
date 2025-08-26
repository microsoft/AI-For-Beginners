<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7e617f0b8de85a43957a853aba09bfeb",
  "translation_date": "2025-08-26T08:39:56+00:00",
  "source_file": "lessons/5-NLP/18-Transformers/README.md",
  "language_code": "tr"
}
-->
# Dikkat Mekanizmaları ve Transformerlar

## [Ders Öncesi Testi](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/118)

NLP alanındaki en önemli problemlerden biri, Google Translate gibi araçların temelini oluşturan **makine çevirisi**dir. Bu bölümde, makine çevirisine ya da daha genel olarak herhangi bir *diziden-diziye* (sequence-to-sequence) göreve (bu aynı zamanda **cümle dönüşümü** olarak da adlandırılır) odaklanacağız.

RNN'lerle, diziden-diziye işlemi iki tekrarlayan ağ ile gerçekleştirilir. Bu ağlardan biri olan **encoder**, bir giriş dizisini gizli bir duruma sıkıştırırken, diğer ağ olan **decoder**, bu gizli durumu çevrilmiş bir sonuca açar. Ancak bu yaklaşımda birkaç sorun vardır:

* Encoder ağının son durumu, bir cümlenin başlangıcını hatırlamakta zorlanır, bu da uzun cümleler için modelin kalitesinin düşmesine neden olur.
* Bir dizideki tüm kelimeler sonuca aynı etkiyi yapar. Ancak gerçekte, giriş dizisindeki belirli kelimeler genellikle ardışık çıktılar üzerinde diğerlerinden daha fazla etkiye sahiptir.

**Dikkat Mekanizmaları**, her bir giriş vektörünün RNN'nin her bir çıktı tahmini üzerindeki bağlamsal etkisini ağırlıklandırmanın bir yolunu sağlar. Bu, giriş RNN'sinin ara durumları ile çıkış RNN'si arasında kısayollar oluşturarak uygulanır. Bu şekilde, çıktı sembolü y<sub>t</sub>'yi oluştururken, farklı ağırlık katsayıları α<sub>t,i</sub> ile tüm giriş gizli durumlarını h<sub>i</sub> dikkate alırız.

![Bir ekleyici dikkat katmanına sahip encoder/decoder modelini gösteren görsel](../../../../../translated_images/encoder-decoder-attention.7a726296894fb567aa2898c94b17b3289087f6705c11907df8301df9e5eeb3de.tr.png)

> [Bahdanau ve diğerleri, 2015](https://arxiv.org/pdf/1409.0473.pdf)'teki ekleyici dikkat mekanizmasına sahip encoder-decoder modeli, [bu blog yazısından](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html) alıntılanmıştır.

Dikkat matrisi {α<sub>i,j</sub>}, belirli giriş kelimelerinin çıktı dizisindeki bir kelimenin oluşturulmasında ne derece rol oynadığını temsil eder. Aşağıda böyle bir matrisin bir örneği verilmiştir:

![Bahdanau - arviz.org'dan alınan, RNNsearch-50 tarafından bulunan bir örnek hizalamayı gösteren görsel](../../../../../translated_images/bahdanau-fig3.09ba2d37f202a6af11de6c82d2d197830ba5f4528d9ea430eb65fd3a75065973.tr.png)

> Şekil [Bahdanau ve diğerleri, 2015](https://arxiv.org/pdf/1409.0473.pdf)'ten alınmıştır (Şekil 3)

Dikkat mekanizmaları, NLP'deki mevcut veya mevcut duruma yakın en iyi performansın büyük bir kısmından sorumludur. Ancak dikkat eklemek, model parametrelerinin sayısını büyük ölçüde artırır ve bu da RNN'lerle ölçekleme sorunlarına yol açar. RNN'lerin ölçeklenmesindeki temel kısıtlama, modellerin tekrarlayıcı doğasının, eğitimi toplu işleme ve paralelleştirme açısından zorlaştırmasıdır. Bir RNN'de bir dizinin her bir öğesi sıralı bir şekilde işlenmelidir, bu da kolayca paralelleştirilemeyeceği anlamına gelir.

![Dikkatli Encoder Decoder](../../../../../lessons/5-NLP/18-Transformers/images/EncDecAttention.gif)

> Şekil [Google'ın Blogu](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)'ndan alınmıştır.

Dikkat mekanizmalarının benimsenmesi ve bu kısıtlama, bugün bildiğimiz ve kullandığımız BERT ve Open-GPT3 gibi en iyi performans gösteren Transformer Modellerinin oluşturulmasına yol açmıştır.

## Transformer Modelleri

Transformerların arkasındaki temel fikirlerden biri, RNN'lerin sıralı doğasından kaçınmak ve eğitim sırasında paralelleştirilebilir bir model oluşturmaktır. Bu, iki fikirle gerçekleştirilir:

* pozisyonel kodlama
* RNN'ler (veya CNN'ler) yerine desenleri yakalamak için kendine dikkat mekanizmasının kullanılması (bu nedenle transformerları tanıtan makale *[Attention is all you need](https://arxiv.org/abs/1706.03762)* olarak adlandırılmıştır)

### Pozisyonel Kodlama/Gömme

Pozisyonel kodlama fikri şu şekildedir:
1. RNN'ler kullanıldığında, tokenların göreceli pozisyonu adım sayısıyla temsil edilir ve bu nedenle açıkça temsil edilmesine gerek yoktur.
2. Ancak, dikkate geçtiğimizde, bir dizideki tokenların göreceli pozisyonlarını bilmemiz gerekir.
3. Pozisyonel kodlama elde etmek için, token dizimizi dizideki token pozisyonlarının bir dizisiyle (örneğin, 0,1, ...) genişletiriz.
4. Daha sonra token pozisyonunu bir token gömme vektörüyle karıştırırız. Pozisyonu (tam sayı) bir vektöre dönüştürmek için farklı yaklaşımlar kullanabiliriz:

* Token gömmeye benzer şekilde eğitilebilir gömme. Burada bu yaklaşımı ele alıyoruz. Hem tokenlar hem de pozisyonları üzerinde gömme katmanları uygularız, aynı boyutlarda gömme vektörleri elde ederiz ve bunları toplarız.
* Orijinal makalede önerildiği gibi sabit pozisyon kodlama fonksiyonu.

<img src="images/pos-embedding.png" width="50%"/>

> Görsel yazar tarafından oluşturulmuştur.

Pozisyonel gömme ile elde ettiğimiz sonuç, hem orijinal tokenı hem de dizideki pozisyonunu gömmektir.

### Çoklu Başlı Kendine Dikkat

Sonraki adımda, dizimizdeki bazı desenleri yakalamamız gerekir. Bunu yapmak için transformerlar, giriş ve çıkış olarak aynı diziye uygulanan dikkat mekanizması olan **kendine dikkat** mekanizmasını kullanır. Kendine dikkat uygulamak, cümle içindeki **bağlamı** dikkate almamızı ve hangi kelimelerin birbiriyle ilişkili olduğunu görmemizi sağlar. Örneğin, *it* gibi zamirlerin hangi kelimelere atıfta bulunduğunu görmemizi ve bağlamı dikkate almamızı sağlar:

![](../../../../../translated_images/CoreferenceResolution.861924d6d384a7d68d8d0039d06a71a151f18a796b8b1330239d3590bd4947eb.tr.png)

> Görsel [Google Blogu](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)'ndan alınmıştır.

Transformerlarda, ağın uzun vadeli ve kısa vadeli kelime ilişkileri, eş referanslar gibi farklı bağımlılık türlerini yakalama gücünü artırmak için **Çoklu Başlı Dikkat** kullanılır.

[TensorFlow Notebook](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb), transformer katmanlarının uygulanması hakkında daha fazla ayrıntı içerir.

### Encoder-Decoder Dikkati

Transformerlarda dikkat iki yerde kullanılır:

* Giriş metni içindeki desenleri yakalamak için kendine dikkat
* Dizi çevirisi yapmak için - bu, encoder ve decoder arasındaki dikkat katmanıdır.

Encoder-decoder dikkati, bu bölümün başında RNN'lerde kullanılan dikkat mekanizmasına çok benzerdir. Bu animasyonlu diyagram, encoder-decoder dikkatinin rolünü açıklar.

![Transformer modellerinde değerlendirmelerin nasıl yapıldığını gösteren animasyonlu GIF.](../../../../../lessons/5-NLP/18-Transformers/images/transformer-animated-explanation.gif)

Her giriş pozisyonu bağımsız olarak her çıkış pozisyonuna eşlendiğinden, transformerlar RNN'lere göre daha iyi paralelleştirilebilir, bu da çok daha büyük ve daha ifade gücü yüksek dil modellerini mümkün kılar. Her dikkat başlığı, kelimeler arasındaki farklı ilişkileri öğrenmek için kullanılabilir ve bu da Doğal Dil İşleme görevlerini geliştirir.

## BERT

**BERT** (Bidirectional Encoder Representations from Transformers), *BERT-base* için 12 katmanlı ve *BERT-large* için 24 katmanlı çok büyük bir transformer ağıdır. Model, büyük bir metin veri kümesi (WikiPedia + kitaplar) üzerinde denetimsiz eğitim (bir cümledeki maskelenmiş kelimeleri tahmin etme) kullanılarak önceden eğitilir. Ön eğitim sırasında model, dil anlayışının önemli seviyelerini öğrenir ve bu, diğer veri kümeleriyle ince ayar yapılarak kullanılabilir. Bu işleme **transfer öğrenme** denir.

![http://jalammar.github.io/illustrated-bert/ adresinden alınan görsel](../../../../../translated_images/jalammarBERT-language-modeling-masked-lm.34f113ea5fec4362e39ee4381aab7cad06b5465a0b5f053a0f2aa05fbe14e746.tr.png)

> Görsel [kaynağı](http://jalammar.github.io/illustrated-bert/)

## ✍️ Alıştırmalar: Transformerlar

Aşağıdaki defterlerde öğrenmeye devam edin:

* [PyTorch ile Transformerlar](../../../../../lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb)
* [TensorFlow ile Transformerlar](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb)

## Sonuç

Bu derste Transformerlar ve Dikkat Mekanizmaları hakkında bilgi edindiniz; bunlar NLP araç kutusundaki temel araçlardır. BERT, DistilBERT, BigBird, OpenGPT3 ve daha fazlası gibi birçok Transformer mimarisi varyasyonu vardır ve bunlar ince ayar yapılabilir. [HuggingFace paketi](https://github.com/huggingface/), bu mimarilerin birçoğunu hem PyTorch hem de TensorFlow ile eğitmek için bir depo sağlar.

## 🚀 Meydan Okuma

## [Ders Sonrası Testi](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/218)

## İnceleme ve Kendi Kendine Çalışma

* Transformerları açıklayan klasik [Attention is all you need](https://arxiv.org/abs/1706.03762) makalesini açıklayan bir [blog yazısı](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/).
* Transformerları detaylı bir şekilde açıklayan [bir dizi blog yazısı](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452).

## [Ödev](assignment.md)

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı bir yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel bir insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmez.