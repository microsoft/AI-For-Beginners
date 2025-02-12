# Gömme (Embeddings)

## [Ders öncesi quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/114)

BoW veya TF/IDF tabanlı sınıflandırıcıları eğitirken, uzunluğu `vocab_size` olan yüksek boyutlu kelime torbası (bag-of-words) vektörleri üzerinde çalıştık ve düşük boyutlu konumsal temsil vektörlerini seyrek bir one-hot temsiline açıkça dönüştürdük. Ancak bu one-hot temsili, bellek açısından verimli değildir. Ayrıca, her kelime birbirinden bağımsız olarak ele alınır; yani one-hot kodlanmış vektörler kelimeler arasında herhangi bir anlamsal benzerlik ifade etmez.

**Gömme** fikri, kelimeleri daha düşük boyutlu yoğun vektörler ile temsil etmektir ve bu vektörler bir kelimenin anlamsal anlamını bir şekilde yansıtır. Anlamlı kelime gömmeleri nasıl oluşturulacağını daha sonra tartışacağız, ancak şimdilik gömmeleri bir kelime vektörünün boyutunu düşürmenin bir yolu olarak düşünelim.

Bu nedenle, gömme katmanı bir kelimeyi girdi olarak alır ve belirli bir `embedding_size` uzunluğunda bir çıktı vektörü üretir. Bir anlamda, bu, `Linear` katmanına çok benzer, ancak bir one-hot kodlanmış vektör almak yerine, bir kelime numarasını girdi olarak alabilir, bu da büyük one-hot kodlanmış vektörler oluşturmaktan kaçınmamızı sağlar.

Sınıflandırıcı ağımızda gömme katmanını ilk katman olarak kullanarak, kelime torbasından **gömme torbası** modeline geçiş yapabiliriz; burada metnimizdeki her kelimeyi karşılık gelen gömme ile dönüştürüyor ve ardından `sum`, `average` veya `max` gibi tüm bu gömmeler üzerinde bazı toplama fonksiyonları hesaplıyoruz.

![Beş sıralı kelime için bir gömme sınıflandırıcısını gösteren bir resim.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.tr.png)

> Resim yazar tarafından hazırlanmıştır.

## ✍️ Alıştırmalar: Gömme

Aşağıdaki not defterlerinde öğrenmeye devam edin:
* [PyTorch ile Gömme](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb)
* [TensorFlow ile Gömme](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)

## Anlamsal Gömme: Word2Vec

Gömme katmanı kelimeleri vektör temsilcisine haritalamayı öğrenirken, bu temsilin mutlaka çok fazla anlamsal anlamı yoktu. Benzer kelimelerin veya eşanlamlıların, bazı vektör mesafesi (örneğin, Öklid mesafesi) açısından birbirine yakın vektörlere karşılık geldiği bir vektör temsilini öğrenmek güzel olurdu.

Bunu yapmak için, gömme modelimizi belirli bir şekilde büyük bir metin koleksiyonu üzerinde önceden eğitmemiz gerekiyor. Anlamsal gömmeleri eğitmenin bir yolu [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) olarak adlandırılır. Bu, kelimelerin dağıtılmış bir temsilini üretmek için kullanılan iki ana mimariye dayanır:

 - **Sürekli kelime torbası** (CBoW) — bu mimaride, modeli çevresindeki bağlamdan bir kelimeyi tahmin etmek için eğitiyoruz. ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$ verildiğinde, modelin amacı $(W_{-2},W_{-1},W_1,W_2)$'den $W_0$'ı tahmin etmektir.
 - **Sürekli skip-gram**, CBoW'nun tersidir. Model, mevcut kelimeyi tahmin etmek için çevresindeki bağlam kelimelerinin penceresini kullanır.

CBoW daha hızlıdır, oysa skip-gram daha yavaştır, ancak nadir kelimeleri temsil etme konusunda daha iyi bir iş çıkarır.

![Kelimeleri vektörlere dönüştürmek için hem CBoW hem de Skip-Gram algoritmalarını gösteren bir resim.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.tr.png)

> Resim [bu makaleden](https://arxiv.org/pdf/1301.3781.pdf) alınmıştır.

Word2Vec önceden eğitilmiş gömmeleri (ve GloVe gibi diğer benzer modeller) sinir ağlarındaki gömme katmanının yerinde de kullanılabilir. Ancak, kelime dağarcıkları ile ilgilenmemiz gerekiyor, çünkü Word2Vec/GloVe'yi önceden eğitmek için kullanılan kelime dağarcığı, metin koleksiyonumuzdaki kelime dağarcığından farklı olabilir. Bu sorunun nasıl çözülebileceğini görmek için yukarıdaki not defterlerine göz atın.

## Bağlamsal Gömme

Word2Vec gibi geleneksel önceden eğitilmiş gömme temsillerinin bir ana sınırlaması, kelime anlamı ayrımını yapma problemidir. Önceden eğitilmiş gömmeler, kelimelerin bağlam içindeki anlamlarının bir kısmını yakalayabilse de, bir kelimenin her olası anlamı aynı gömme içinde kodlanır. Bu, birçok kelimenin, örneğin 'play' kelimesinin, kullanıldığı bağlama bağlı olarak farklı anlamları olduğu için, aşağı akış modellerinde sorunlara neden olabilir.

Örneğin, 'play' kelimesi bu iki farklı cümlede oldukça farklı anlamlar taşır:

- Tiyatroda bir **oyun** izlemeye gittim.
- John arkadaşlarıyla **oynamak** istiyor.

Yukarıdaki önceden eğitilmiş gömmeler, 'play' kelimesinin bu iki anlamını da aynı gömme içinde temsil eder. Bu sınırlamanın üstesinden gelmek için, büyük bir metin koleksiyonu üzerinde eğitilen ve kelimelerin farklı bağlamlarda nasıl bir araya getirileceğini *bilen* **dil modeli** tabanlı gömmeler oluşturmamız gerekiyor. Bağlamsal gömmeleri tartışmak bu eğitimin kapsamı dışında, ancak daha sonra dil modellerinden bahsederken onlara geri döneceğiz.

## Sonuç

Bu derste, TensorFlow ve Pytorch'ta gömme katmanları oluşturmayı ve kullanmayı öğrendiniz; bu sayede kelimelerin anlamsal anlamlarını daha iyi yansıtabilirsiniz.

## 🚀 Zorluk

Word2Vec, şarkı sözleri ve şiir üretimi gibi bazı ilginç uygulamalar için kullanılmıştır. Yazarın Word2Vec kullanarak şiir nasıl ürettiğini anlatan [bu makaleye](https://www.politetype.com/blog/word2vec-color-poems) göz atın. Ayrıca, bu tekniğin farklı bir açıklamasını keşfetmek için [Dan Shiffmann'ın bu videosunu](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) izleyin. Ardından, bu teknikleri kendi metin koleksiyonunuza uygulamayı deneyin; belki Kaggle'dan elde ettiğiniz verilerle.

## [Ders sonrası quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/214)

## Gözden Geçirme & Kendi Kendine Çalışma

Word2Vec hakkında [Vektör Uzayında Kelime Temsillerinin Verimli Tahmini](https://arxiv.org/pdf/1301.3781.pdf) başlıklı bu makaleyi okuyun.

## [Ödev: Not Defterleri](assignment.md)

**Açıklama**:  
Bu belge, makine tabanlı AI çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluğa özen göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde otorite kaynağı olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul etmiyoruz.