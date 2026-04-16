# Dil Modellemesi

Word2Vec ve GloVe gibi anlamsal gömmeler aslında **dil modellemesi**ne doğru atılmış ilk adımlardır - dilin doğasını bir şekilde *anlayan* (veya *temsil eden*) modeller oluşturmak.

## [Ders Öncesi Testi](https://ff-quizzes.netlify.app/en/ai/quiz/29)

Dil modellemesinin temel fikri, modelleri etiketlenmemiş veri kümeleri üzerinde gözetimsiz bir şekilde eğitmektir. Bu önemlidir çünkü elimizde çok büyük miktarda etiketlenmemiş metin bulunurken, etiketlenmiş metin miktarı her zaman etiketleme için harcayabileceğimiz çaba ile sınırlı olacaktır. Çoğu zaman, metindeki **eksik kelimeleri tahmin edebilen** dil modelleri oluşturabiliriz, çünkü metindeki rastgele bir kelimeyi gizlemek ve bunu bir eğitim örneği olarak kullanmak oldukça kolaydır.

## Gömmeleri Eğitmek

Önceki örneklerimizde önceden eğitilmiş anlamsal gömmeler kullandık, ancak bu gömmelerin nasıl eğitilebileceğini görmek ilginçtir. Kullanılabilecek birkaç fikir vardır:

* **N-Gram** dil modellemesi, burada bir tokeni önceki N tokena bakarak tahmin ederiz (N-gram).
* **Continuous Bag-of-Words** (CBoW), burada bir token dizisindeki $W_{-N}$, ..., $W_N$ arasında ortadaki token $W_0$'ı tahmin ederiz.
* **Skip-gram**, burada ortadaki token $W_0$'dan komşu tokenlerin bir setini {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} tahmin ederiz.

![Kelimeyi vektöre dönüştürme algoritmalarına dair makaleden görsel](../../../../../translated_images/tr/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> Görsel [bu makaleden](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Örnek Not Defterleri: CBoW Modeli Eğitimi

Aşağıdaki not defterlerinde öğreniminize devam edin:

* [TensorFlow ile CBoW Word2Vec Eğitimi](CBoW-TF.ipynb)
* [PyTorch ile CBoW Word2Vec Eğitimi](CBoW-PyTorch.ipynb)

## Sonuç

Önceki derste kelime gömmelerinin adeta sihir gibi çalıştığını gördük! Şimdi kelime gömmeleri eğitmenin çok karmaşık bir iş olmadığını biliyoruz ve gerekirse alan spesifik metinler için kendi kelime gömmelerimizi eğitebiliriz.

## [Ders Sonrası Testi](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Gözden Geçirme ve Kendi Kendine Çalışma

* [PyTorch'un Resmi Dil Modelleme Eğitimi](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [TensorFlow'un Resmi Word2Vec Modeli Eğitimi](https://www.TensorFlow.org/tutorials/text/word2vec).
* **gensim** çerçevesini kullanarak en yaygın kullanılan gömmeleri birkaç satır kodla eğitmek [bu belgede](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html) açıklanmıştır.

## 🚀 [Görev: Skip-Gram Modeli Eğitimi](lab/README.md)

Laboratuvarda, bu dersteki kodu değiştirerek CBoW yerine skip-gram modeli eğitmenizi istiyoruz. [Detayları okuyun](lab/README.md)

---

