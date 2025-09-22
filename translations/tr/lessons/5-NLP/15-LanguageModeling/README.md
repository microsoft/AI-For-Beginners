<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-26T07:22:25+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "tr"
}
-->
# Dil Modellemesi

Word2Vec ve GloVe gibi anlamsal gömme yöntemleri aslında **dil modellemesine** doğru atılmış ilk adımdır - dilin doğasını bir şekilde *anlayan* (veya *temsil eden*) modeller oluşturmak.

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ai/quiz/29)

Dil modellemesinin temel fikri, modelleri etiketlenmemiş veri kümeleri üzerinde gözetimsiz bir şekilde eğitmektir. Bu önemlidir çünkü elimizde büyük miktarda etiketlenmemiş metin bulunurken, etiketlenmiş metin miktarı her zaman etiketleme için harcayabileceğimiz çabayla sınırlı olacaktır. Çoğu zaman, metindeki **eksik kelimeleri tahmin edebilen** dil modelleri oluşturabiliriz, çünkü metindeki rastgele bir kelimeyi maskelemek ve bunu bir eğitim örneği olarak kullanmak oldukça kolaydır.

## Gömme Yöntemlerinin Eğitimi

Önceki örneklerimizde, önceden eğitilmiş anlamsal gömme yöntemlerini kullandık, ancak bu gömme yöntemlerinin nasıl eğitilebileceğini görmek ilginçtir. Kullanılabilecek birkaç farklı fikir vardır:

* **N-Gram** dil modellemesi: Bir belirteci, önceki N belirtece bakarak tahmin ettiğimiz yöntem (N-gram).
* **Sürekli Kelime Çantası** (CBoW): Bir belirteç dizisindeki $W_{-N}$, ..., $W_N$ belirteçleri arasında ortadaki belirteç $W_0$'ı tahmin ettiğimiz yöntem.
* **Skip-gram**: Ortadaki belirteç $W_0$'dan, komşu belirteçler kümesini {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} tahmin ettiğimiz yöntem.

![Kelimeleri vektörlere dönüştürme algoritmalarına dair bir makaleden görsel](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.tr.png)

> Görsel [bu makaleden](https://arxiv.org/pdf/1301.3781.pdf) alınmıştır.

## ✍️ Örnek Defterler: CBoW Modeli Eğitimi

Aşağıdaki defterlerde öğreniminize devam edebilirsiniz:

* [TensorFlow ile CBoW Word2Vec Eğitimi](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [PyTorch ile CBoW Word2Vec Eğitimi](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Sonuç

Önceki derste, kelime gömmelerinin adeta bir sihir gibi çalıştığını görmüştük! Şimdi ise kelime gömmelerini eğitmenin çok karmaşık bir iş olmadığını biliyoruz ve gerekirse alanına özgü metinler için kendi kelime gömmelerimizi eğitebileceğimizi öğrenmiş olduk.

## [Ders Sonrası Test](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Gözden Geçirme ve Kendi Kendine Çalışma

* [PyTorch'un Resmi Dil Modelleme Eğitimi](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [TensorFlow'un Word2Vec Modeli Eğitimi için Resmi Eğitimi](https://www.TensorFlow.org/tutorials/text/word2vec).
* **gensim** çerçevesini kullanarak en yaygın kullanılan gömme yöntemlerini birkaç satır kodla eğitme yöntemi [bu belgede](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html) açıklanmıştır.

## 🚀 [Görev: Skip-Gram Modeli Eğitin](lab/README.md)

Laboratuvarda, bu dersteki kodu değiştirerek CBoW yerine skip-gram modeli eğitmenizi istiyoruz. [Detayları okuyun](lab/README.md).

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.