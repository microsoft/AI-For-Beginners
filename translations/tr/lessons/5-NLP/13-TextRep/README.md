# Metinleri Tensörler Olarak Temsil Etme

## [Ders öncesi quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Metin Sınıflandırması

Bu bölümün ilk kısmında, **metin sınıflandırması** görevine odaklanacağız. [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset) veri setini kullanacağız; bu veri seti aşağıdaki gibi haber makalelerini içermektedir:

* Kategori: Bilim/Teknoloji
* Başlık: Ky. Şirketi Peptitleri İncelemek İçin Hibe Kazandı (AP)
* Metin: AP - Louisville Üniversitesi'nde bir kimya araştırmacısı tarafından kurulan bir şirket, geliştirmek için bir hibe kazandı...

Amacımız, haber maddesini metne dayalı olarak bir kategoriye sınıflandırmaktır.

## Metni Temsil Etme

Doğal Dil İşleme (NLP) görevlerini sinir ağları ile çözmek istiyorsak, metni tensörler olarak temsil etmenin bir yoluna ihtiyacımız var. Bilgisayarlar, metin karakterlerini, ekranınızdaki yazı tiplerine karşılık gelen sayılar olarak temsil eder; bu, ASCII veya UTF-8 gibi kodlamalar kullanılarak yapılır.

<img alt="Bir karakteri ASCII ve ikili temsile eşleyen diyagramı gösteren bir görüntü" src="images/ascii-character-map.png" width="50%"/>

> [Görüntü kaynağı](https://www.seobility.net/en/wiki/ASCII)

İnsanlar olarak, her harfin neyi **temsil ettiğini** anlarız ve tüm karakterlerin bir araya gelerek bir cümledeki kelimeleri nasıl oluşturduğunu biliriz. Ancak, bilgisayarlar kendi başlarına böyle bir anlayışa sahip değildir ve sinir ağı, eğitimi sırasında anlamı öğrenmek zorundadır.

Bu nedenle, metni temsil ederken farklı yaklaşımlar kullanabiliriz:

* **Karakter düzeyinde temsil**, metni her karakteri bir sayı olarak ele alarak temsil ettiğimiz durumdur. Metin koleksiyonumuzda *C* farklı karakter bulunduğunu varsayarsak, *Hello* kelimesi 5x*C* tensör ile temsil edilir. Her harf, bir sıcak kodlama (one-hot encoding) ile bir tensör sütununa karşılık gelir.
* **Kelime düzeyinde temsil**, metindeki tüm kelimelerin bir **kelime hazinesi** oluşturularak temsil edildiği durumdur; ardından kelimeleri sıcak kodlama ile temsil ederiz. Bu yaklaşım, her harfin kendisiyle çok fazla anlam ifade etmediği için daha iyidir ve bu nedenle daha yüksek düzeydeki anlamsal kavramları - kelimeleri - kullanarak sinir ağı için görevi basitleştiririz. Ancak, büyük sözlük boyutu nedeniyle yüksek boyutlu seyrek tensörlerle başa çıkmamız gerekir.

Temsilden bağımsız olarak, önce metni bir **token** dizisine dönüştürmemiz gerekir; bir token, ya bir karakter, bir kelime ya da bazen bir kelimenin bir parçası olabilir. Ardından, token'ı bir sayıya dönüştürürüz; genellikle **kelime hazinesi** kullanarak, bu sayı bir sinir ağına sıcak kodlama ile beslenebilir.

## N-Gramlar

Doğal dilde, kelimelerin kesin anlamı yalnızca bağlamda belirlenebilir. Örneğin, *sinir ağı* ve *balık avlama ağı* ifadelerinin anlamları tamamen farklıdır. Bu durumu dikkate almanın yollarından biri, modelimizi kelime çiftleri üzerinde inşa etmek ve kelime çiftlerini ayrı kelime hazinesi tokenleri olarak ele almaktır. Bu şekilde, *I like to go fishing* cümlesi aşağıdaki token dizisi ile temsil edilecektir: *I like*, *like to*, *to go*, *go fishing*. Bu yaklaşımın sorunu, sözlük boyutunun önemli ölçüde büyümesidir ve *go fishing* ve *go shopping* gibi kombinasyonlar, aynı fiil olmasına rağmen hiçbir anlamsal benzerlik paylaşmayan farklı tokenler tarafından temsil edilir.

Bazı durumlarda, üç kelimeden oluşan kombinasyonlar - tri-gramlar - kullanmayı da düşünebiliriz. Bu nedenle, bu yaklaşım genellikle **n-gramlar** olarak adlandırılır. Ayrıca, karakter düzeyinde temsil ile n-gramları kullanmak mantıklıdır; bu durumda n-gramlar kabaca farklı hecelere karşılık gelecektir.

## Kelime Torbası ve TF/IDF

Metin sınıflandırması gibi görevleri çözerken, metni tek bir sabit boyutlu vektörle temsil edebilmemiz gerekir; bu vektörü son yoğun sınıflandırıcıya girdi olarak kullanacağız. Bunu yapmanın en basit yollarından biri, tüm bireysel kelime temsillerini bir araya getirmektir; örneğin, bunları toplamak. Her kelimenin sıcak kodlamalarını toplarsak, metin içinde her kelimenin ne kadar sıklıkla geçtiğini gösteren bir frekans vektörü elde ederiz. Bu metin temsiline **kelime torbası** (BoW) denir.

<img src="images/bow.png" width="90%"/>

> Yazarın görüntüsü

BoW, metinde hangi kelimelerin ve hangi miktarlarda göründüğünü temsil eder; bu da metnin ne hakkında olduğu konusunda iyi bir gösterge olabilir. Örneğin, bir politikayla ilgili haber makalesi, muhtemelen *başkan* ve *ülke* gibi kelimeleri içerecektir; bilimsel bir yayında ise *çarpıştırıcı*, *bulundu* gibi kelimeler olacaktır. Bu nedenle, kelime sıklıkları birçok durumda metin içeriğinin iyi bir göstergesi olabilir.

BoW ile ilgili sorun, *ve*, *dir* gibi belirli yaygın kelimelerin çoğu metinde yer alması ve en yüksek sıklıklara sahip olmalarıdır; bu durum, gerçekten önemli olan kelimeleri gölgede bırakmaktadır. Bu kelimelerin önemini, kelimelerin tüm belge koleksiyonunda ne sıklıkla geçtiğini dikkate alarak azaltabiliriz. Bu, TF/IDF yaklaşımının temel fikridir ve bu konu, bu derse ekli not defterlerinde daha ayrıntılı olarak ele alınmaktadır.

Ancak, bu yaklaşımların hiçbiri metnin **anlamını** tam olarak dikkate alamaz. Bunu yapmak için daha güçlü sinir ağı modellerine ihtiyacımız var; bunu bu bölümün ilerleyen kısımlarında tartışacağız.

## ✍️ Alıştırmalar: Metin Temsili

Aşağıdaki not defterlerinde öğreniminize devam edin:

* [PyTorch ile Metin Temsili](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb)
* [TensorFlow ile Metin Temsili](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)

## Sonuç

Şu ana kadar, farklı kelimelere frekans ağırlığı ekleyebilen teknikleri inceledik. Ancak, bu teknikler anlamı veya sıralamayı temsil edemez. Ünlü dilbilimci J. R. Firth'ün 1935 yılında söylediği gibi, "Bir kelimenin tam anlamı her zaman bağlamsaldır ve bağlamdan ayrı bir anlam çalışması ciddiye alınamaz." Daha sonra kursta, metinden bağlamsal bilgileri nasıl yakalayacağımızı dil modelleme ile öğreneceğiz.

## 🚀 Zorluk

Kelime torbası ve farklı veri modelleri kullanarak bazı diğer alıştırmaları deneyin. Bu [Kaggle yarışmasından](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words) ilham alabilirsiniz.

## [Ders sonrası quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Gözden Geçirme & Kendi Kendine Çalışma

Metin gömme ve kelime torbası teknikleri ile becerilerinizi [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) üzerinde pratik yaparak geliştirin.

## [Ödev: Not Defterleri](assignment.md)

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlış anlamalar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak değerlendirilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.