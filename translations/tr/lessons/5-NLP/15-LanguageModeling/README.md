# Dil Modelleme

Anlam gömme yöntemleri, Word2Vec ve GloVe gibi, aslında **dil modelleme** için bir ilk adımdır - dilin doğasını bir şekilde *anlayan* (veya *temsil eden*) modeller oluşturmak.

## [Ders öncesi quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

Dil modellemenin arkasındaki temel fikir, etiketlenmemiş veri setleri üzerinde denetimsiz bir şekilde eğitim yapmaktır. Bu önemlidir çünkü elimizde büyük miktarda etiketlenmemiş metin bulunmaktadır, oysa etiketlenmiş metin miktarı her zaman etiketleme için harcayabileceğimiz çaba ile sınırlı olacaktır. Genellikle, metindeki **eksik kelimeleri tahmin edebilen** dil modelleri oluşturabiliriz, çünkü metinde rastgele bir kelimeyi maskeleyip bunu bir eğitim örneği olarak kullanmak kolaydır.

## Gömme Eğitimleri

Önceki örneklerimizde, önceden eğitilmiş anlam gömmelerini kullandık, ancak bu gömmelerin nasıl eğitilebileceğini görmek ilginçtir. Kullanılabilecek birkaç olası fikir vardır:

* **N-Gram** dil modelleme, N önceki token'a bakarak bir token'ı tahmin ettiğimiz durumdur (N-gram)
* **Sürekli Kelime Torbası** (CBoW), bir token dizisi $W_{-N}$, ..., $W_N$ içindeki ortadaki token $W_0$'ı tahmin ettiğimiz durumdur.
* **Skip-gram**, ortadaki token $W_0$'dan komşu token'ların {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} bir kümesini tahmin ettiğimiz durumdur.

![kelimeleri vektörlere dönüştürme üzerine makaleden bir resim](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.tr.png)

> [bu makaleden](https://arxiv.org/pdf/1301.3781.pdf) alınmıştır.

## ✍️ Örnek Not Defterleri: CBoW modelini eğitme

Aşağıdaki not defterlerinde öğrenmeye devam edin:

* [TensorFlow ile CBoW Word2Vec Eğitimi](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [PyTorch ile CBoW Word2Vec Eğitimi](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Sonuç

Önceki derste, kelime gömmelerinin sihir gibi çalıştığını gördük! Artık kelime gömmelerini eğitmenin çok karmaşık bir görev olmadığını biliyoruz ve gerekirse alan spesifik metinler için kendi kelime gömmelerimizi eğitebilmeliyiz.

## [Ders sonrası quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Gözden Geçirme & Kendi Kendine Çalışma

* [Dil Modelleme üzerine resmi PyTorch eğitimi](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Word2Vec modelini eğitme üzerine resmi TensorFlow eğitimi](https://www.TensorFlow.org/tutorials/text/word2vec).
* En yaygın kullanılan gömmeleri birkaç satır kodla eğitmek için **gensim** çerçevesinin kullanımı [bu belgede](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html) açıklanmıştır.

## 🚀 [Görev: Skip-Gram Modelini Eğit](lab/README.md)

Laboratuvar çalışmasında, bu dersten aldığınız kodu CBoW yerine skip-gram modelini eğitmek için değiştirmenizi istiyoruz. [Detayları okuyun](lab/README.md)

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluğu sağlamak için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen dikkate alınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.