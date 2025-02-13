# Adlandırılmış Varlık Tanıma

Şimdiye kadar, çoğunlukla tek bir NLP görevine - sınıflandırmaya odaklandık. Ancak, sinir ağları ile gerçekleştirilebilecek başka NLP görevleri de vardır. Bu görevlerden biri **[Adlandırılmış Varlık Tanıma](https://wikipedia.org/wiki/Named-entity_recognition)** (NER) olup, metin içindeki belirli varlıkları tanımakla ilgilidir; bunlar yerler, kişi adları, tarih-saat aralıkları, kimyasal formüller ve benzeri olabilir.

## [Ders öncesi quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## NER Kullanım Örneği

Diyelim ki, Amazon Alexa veya Google Asistan'a benzer bir doğal dil sohbet botu geliştirmek istiyorsunuz. Akıllı sohbet botlarının çalışma şekli, kullanıcının ne istediğini *anlamak* için girdi cümlesi üzerinde metin sınıflandırması yapmaktır. Bu sınıflandırmanın sonucu, bir sohbet botunun ne yapması gerektiğini belirleyen **niyet** olarak adlandırılır.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Yazar tarafından sağlanan görsel

Ancak, bir kullanıcı ifadenin bir parçası olarak bazı parametreler verebilir. Örneğin, hava durumu sorduğunda, bir konum veya tarih belirtebilir. Bir bot, bu varlıkları anlamalı ve eylemi gerçekleştirmeden önce parametre alanlarını uygun şekilde doldurmalıdır. İşte NER tam burada devreye giriyor.

> ✅ Başka bir örnek, [bilimsel tıbbi makaleleri analiz etmek](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) olabilir. Dikkat etmemiz gereken ana şeylerden biri, hastalıklar ve tıbbi maddeler gibi belirli tıbbi terimlerdir. Küçük bir hastalık sayısı muhtemelen alt dize araması kullanılarak çıkarılabilirken, kimyasal bileşikler ve ilaç adları gibi daha karmaşık varlıklar, daha karmaşık bir yaklaşım gerektirir.

## NER'nin Token Sınıflandırması Olarak

NER modelleri esasen **token sınıflandırma modelleridir**, çünkü girdi tokenlerinden her biri için bunun bir varlığa ait olup olmadığını belirlememiz gerekiyor ve eğer aitse - hangi varlık sınıfına ait olduğunu.

Aşağıdaki makale başlığını düşünün:

**Triküspit kapak yetmezliği** ve **lityum karbonat** **zehirlenmesi** bir yeni doğan bebekte.

Buradaki varlıklar şunlardır:

* Triküspit kapak yetmezliği bir hastalıktır (`DIS`)
* Lityum karbonat bir kimyasal maddedir (`CHEM`)
* Zehirlenme de bir hastalıktır (`DIS`)

Bir varlığın birkaç tokenı kapsayabileceğini unutmayın. Ve, bu durumda olduğu gibi, iki ardışık varlık arasında ayrım yapmamız gerekiyor. Bu nedenle, her varlık için iki sınıf kullanmak yaygındır - birincisi varlığın ilk tokenını belirten (genellikle `B-` ön eki kullanılır, **b**aşlangıç için), diğeri ise bir varlığın devamı (`I-`, **i**ç token için). Ayrıca, tüm **d**iğer tokenları temsil etmek için `O` sınıfını da kullanırız. Bu tür token etiketleme, [BIO etiketleme](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (veya IOB) olarak adlandırılır. Etiketlendiğinde, başlığımız şu şekilde görünecektir:

Token | Etiket
------|-----
Triküspit | B-DIS
kapak | I-DIS
yetmezliği | I-DIS
ve | O
lityum | B-CHEM
karbonat | I-CHEM
zehirlenmesi | B-DIS
bir | O
yeni | O
doğan | O
bebek | O
. | O

Tokenlar ve sınıflar arasında bire bir karşılık kurmamız gerektiğinden, bu resimden sağdaki **çoktan-çoğa** sinir ağı modelini eğitebiliriz:

![Yaygın tekrar eden sinir ağı desenlerini gösteren bir görüntü.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.tr.jpg)

> *Görsel [bu blog yazısından](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) [Andrej Karpathy](http://karpathy.github.io/) tarafından alınmıştır. NER token sınıflandırma modelleri, bu resimdeki en sağdaki ağ mimarisine karşılık gelir.*

## NER Modellerinin Eğitimi

Bir NER modeli esasen bir token sınıflandırma modeli olduğundan, bu görev için zaten aşina olduğumuz RNN'leri kullanabiliriz. Bu durumda, her tekrarlayan ağ bloğu token kimliğini döndürecektir. Aşağıdaki örnek not defteri, token sınıflandırması için LSTM nasıl eğitileceğini göstermektedir.

## ✍️ Örnek Not Defterleri: NER

Aşağıdaki not defterinde öğreniminize devam edin:

* [TensorFlow ile NER](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Sonuç

Bir NER modeli, **token sınıflandırma modeli**dir, bu da token sınıflandırması yapmak için kullanılabileceği anlamına gelir. Bu, metin içindeki belirli varlıkları tanımaya yardımcı olan oldukça yaygın bir NLP görevidir; bunlar yerler, adlar, tarihler ve daha fazlasını içerir.

## 🚀 Zorluk

Aşağıda bağlantısı verilen ödevi tamamlayarak tıbbi terimler için bir adlandırılmış varlık tanıma modeli eğitin, ardından bunu farklı bir veri setinde deneyin.

## [Ders sonrası quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Gözden Geçirme & Kendi Kendine Çalışma

[Tekrarlayan Sinir Ağlarının Aşırı Etkili Olması](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) başlıklı blogu okuyun ve o makaledeki Daha Fazla Okuma bölümünü takip ederek bilginizi derinleştirin.

## [Ödev](lab/README.md)

Bu dersteki ödevde, bir tıbbi varlık tanıma modeli eğitmeniz gerekecek. Bu derste açıklanan LSTM modelini eğitmeye başlayabilir ve ardından BERT dönüştürücü modelini kullanmaya geçebilirsiniz. Tüm detayları öğrenmek için [talimatları](lab/README.md) okuyun.

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde otorite kaynağı olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanılması sonucunda ortaya çıkan yanlış anlamalar veya yanlış yorumlamalardan sorumlu değiliz.