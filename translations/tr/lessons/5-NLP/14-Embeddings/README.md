<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e40b47ac3fd48f71304ede1474e66293",
  "translation_date": "2025-08-26T07:20:38+00:00",
  "source_file": "lessons/5-NLP/14-Embeddings/README.md",
  "language_code": "tr"
}
-->
# Gömülü Temsiller

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ai/quiz/27)

BoW veya TF/IDF tabanlı sınıflandırıcılar eğitirken, `vocab_size` uzunluğunda yüksek boyutlu kelime torbası vektörleri üzerinde çalışıyorduk ve düşük boyutlu konumsal temsil vektörlerini seyrek tekil temsil vektörlerine açıkça dönüştürüyorduk. Ancak, bu tekil temsil bellek açısından verimli değildir. Ayrıca, her kelime birbirinden bağımsız olarak ele alınır, yani tekil kodlanmış vektörler kelimeler arasındaki herhangi bir anlamsal benzerliği ifade etmez.

**Gömülü temsil** fikri, kelimeleri bir şekilde bir kelimenin anlamsal anlamını yansıtan daha düşük boyutlu yoğun vektörlerle temsil etmektir. Daha sonra anlamlı kelime gömülü temsillerinin nasıl oluşturulacağını tartışacağız, ancak şimdilik gömülü temsilleri bir kelime vektörünün boyutunu düşürmenin bir yolu olarak düşünebiliriz.

Bu nedenle, gömülü katman bir kelimeyi giriş olarak alır ve belirtilen `embedding_size` boyutunda bir çıktı vektörü üretir. Bir anlamda, bu bir `Linear` katmana çok benzer, ancak tekil kodlanmış bir vektör almak yerine, bir kelime numarasını giriş olarak alabilir, böylece büyük tekil kodlanmış vektörler oluşturmaktan kaçınmamızı sağlar.

Sınıflandırıcı ağımızda ilk katman olarak bir gömülü katman kullanarak, kelime torbasından **gömülü torba** modeline geçebiliriz. Bu modelde, önce metnimizdeki her kelimeyi ilgili gömülü temsile dönüştürürüz ve ardından bu gömülü temsillerin tümü üzerinde `sum`, `average` veya `max` gibi bir toplama fonksiyonu hesaplarız.  

![Beş kelimelik bir dizi için bir gömülü sınıflandırıcıyı gösteren görsel.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.tr.png)

> Görsel yazar tarafından oluşturulmuştur

## ✍️ Alıştırmalar: Gömülü Temsiller

Aşağıdaki defterlerde öğrenmeye devam edin:
* [PyTorch ile Gömülü Temsiller](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb)
* [TensorFlow ile Gömülü Temsiller](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)

## Anlamsal Gömülü Temsiller: Word2Vec

Gömülü katman kelimeleri vektör temsiline eşlemeyi öğrenirken, bu temsilin mutlaka çok fazla anlamsal anlamı olmayabilir. Benzer kelimelerin veya eşanlamlıların, bazı vektör mesafeleri (ör. Öklid mesafesi) açısından birbirine yakın olan vektörlere karşılık geldiği bir vektör temsili öğrenmek güzel olurdu.

Bunu yapmak için, gömülü modelimizi büyük bir metin koleksiyonu üzerinde belirli bir şekilde önceden eğitmemiz gerekir. Anlamsal gömülü temsilleri eğitmenin bir yolu [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) olarak adlandırılır. Bu yöntem, kelimelerin dağıtılmış bir temsilini üretmek için kullanılan iki ana mimariye dayanır:

 - **Sürekli kelime torbası** (CBoW) — Bu mimaride, model çevredeki bağlamdan bir kelime tahmin etmek için eğitilir. $$(W_{-2},W_{-1},W_0,W_1,W_2)$$ ngram'ı verildiğinde, modelin amacı $W_0$'ı $$(W_{-2},W_{-1},W_1,W_2)$$'den tahmin etmektir.
 - **Sürekli atlama-gram** CBoW'un tersidir. Model, bağlam kelimelerinin çevresindeki pencereyi kullanarak mevcut kelimeyi tahmin eder.

CBoW daha hızlıdır, ancak atlama-gram daha yavaştır ve nadir kelimeleri temsil etmede daha iyidir.

![Kelimeleri vektörlere dönüştürmek için hem CBoW hem de Skip-Gram algoritmalarını gösteren görsel.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.tr.png)

> Görsel [bu makaleden](https://arxiv.org/pdf/1301.3781.pdf) alınmıştır

Word2Vec önceden eğitilmiş gömülü temsilleri (GloVe gibi diğer benzer modellerle birlikte) sinir ağlarındaki gömülü katman yerine de kullanılabilir. Ancak, kelime dağarcıklarıyla başa çıkmamız gerekir, çünkü Word2Vec/GloVe'yi önceden eğitmek için kullanılan kelime dağarcığı, metin korpusumuzdaki kelime dağarcığından farklı olabilir. Bu sorunun nasıl çözülebileceğini görmek için yukarıdaki defterlere göz atın.

## Bağlama Dayalı Gömülü Temsiller

Word2Vec gibi geleneksel önceden eğitilmiş gömülü temsil yöntemlerinin temel sınırlamalarından biri, kelime anlamı ayrımı problemidir. Önceden eğitilmiş gömülü temsiller, kelimelerin bağlamdaki anlamlarının bir kısmını yakalayabilse de, bir kelimenin her olası anlamı aynı gömülü temsile kodlanır. Bu, 'play' gibi birçok kelimenin kullanıldıkları bağlama bağlı olarak farklı anlamlara sahip olması nedeniyle, aşağı akış modellerinde sorunlara neden olabilir.

Örneğin, 'play' kelimesi şu iki farklı cümlede oldukça farklı anlamlara sahiptir:

- Tiyatroda bir **oyun** izledim.
- John arkadaşlarıyla **oynamak** istiyor.

Yukarıdaki önceden eğitilmiş gömülü temsiller, 'play' kelimesinin her iki anlamını da aynı gömülü temsilde ifade eder. Bu sınırlamayı aşmak için, büyük bir metin korpusu üzerinde eğitilmiş ve kelimelerin farklı bağlamlarda nasıl bir araya getirilebileceğini *bilen* bir **dil modeli** temelinde gömülü temsiller oluşturmamız gerekir. Bağlama dayalı gömülü temsilleri tartışmak bu dersin kapsamı dışındadır, ancak kursun ilerleyen bölümlerinde dil modellerini ele alırken bu konuya geri döneceğiz.

## Sonuç

Bu derste, kelimelerin anlamsal anlamlarını daha iyi yansıtmak için TensorFlow ve PyTorch'ta gömülü katmanların nasıl oluşturulacağını ve kullanılacağını keşfettiniz.

## 🚀 Meydan Okuma

Word2Vec, şarkı sözleri ve şiir oluşturma gibi ilginç uygulamalar için kullanılmıştır. Yazarın Word2Vec'i kullanarak şiir oluşturma sürecini anlattığı [bu makaleye](https://www.politetype.com/blog/word2vec-color-poems) göz atın. Ayrıca, bu tekniğin farklı bir açıklamasını keşfetmek için Dan Shiffmann'ın [bu videosunu](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) izleyin. Ardından, bu teknikleri kendi metin korpusunuza uygulamayı deneyin, belki Kaggle'dan bir kaynak kullanabilirsiniz.

## [Ders Sonrası Test](https://ff-quizzes.netlify.app/en/ai/quiz/28)

## Gözden Geçirme ve Kendi Kendine Çalışma

Word2Vec ile ilgili bu makaleyi okuyun: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [Ödev: Defterler](assignment.md)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.