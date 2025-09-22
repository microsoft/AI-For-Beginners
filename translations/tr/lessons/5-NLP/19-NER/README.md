<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd10f434e444bce61b7f97eeb1ff6a55",
  "translation_date": "2025-08-26T07:22:56+00:00",
  "source_file": "lessons/5-NLP/19-NER/README.md",
  "language_code": "tr"
}
-->
# Adlandırılmış Varlık Tanıma

Şimdiye kadar, çoğunlukla bir NLP görevi olan sınıflandırmaya odaklandık. Ancak, sinir ağlarıyla gerçekleştirilebilecek başka NLP görevleri de vardır. Bu görevlerden biri, metin içinde yer alan belirli varlıkları tanımayı amaçlayan **[Adlandırılmış Varlık Tanıma](https://wikipedia.org/wiki/Named-entity_recognition)** (NER) işlemidir. Bu varlıklar arasında yerler, kişi adları, tarih-zaman aralıkları, kimyasal formüller gibi unsurlar bulunabilir.

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ai/quiz/37)

## NER Kullanımına Bir Örnek

Diyelim ki Amazon Alexa veya Google Asistan gibi bir doğal dil sohbet botu geliştirmek istiyorsunuz. Akıllı sohbet botlarının çalışma şekli, kullanıcının ne istediğini anlamak için giriş cümlesi üzerinde metin sınıflandırması yapmaktır. Bu sınıflandırmanın sonucu, sohbet botunun ne yapması gerektiğini belirleyen **niyet** (intent) olarak adlandırılır.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Görsel: Yazar tarafından hazırlanmıştır

Ancak, bir kullanıcı cümle içinde bazı parametreler de verebilir. Örneğin, hava durumunu sorarken bir konum veya tarih belirtebilir. Bir bot, bu varlıkları anlayabilmeli ve eylemi gerçekleştirmeden önce parametre yuvalarını buna göre doldurabilmelidir. İşte tam da burada NER devreye girer.

> ✅ Bir başka örnek, [bilimsel tıbbi makalelerin analiz edilmesi](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) olabilir. Burada aramamız gereken temel unsurlardan biri, hastalıklar ve tıbbi maddeler gibi belirli tıbbi terimlerdir. Az sayıda hastalık, muhtemelen alt dize aramasıyla çıkarılabilirken, kimyasal bileşikler ve ilaç isimleri gibi daha karmaşık varlıklar için daha gelişmiş bir yaklaşım gereklidir.

## NER ve Token Sınıflandırması

NER modelleri aslında **token sınıflandırma modelleridir**, çünkü her bir giriş token'ı için bunun bir varlığa ait olup olmadığını ve eğer aitse hangi varlık sınıfına ait olduğunu belirlememiz gerekir.

Şu makale başlığını ele alalım:

**Tricuspid kapak yetmezliği** ve **lityum karbonat** **toksisitesi** bir yenidoğan bebekte.

Buradaki varlıklar şunlardır:

* Tricuspid kapak yetmezliği bir hastalıktır (`DIS`)
* Lityum karbonat bir kimyasal maddedir (`CHEM`)
* Toksisite de bir hastalıktır (`DIS`)

Dikkat edin, bir varlık birden fazla token içerebilir. Ve bu durumda olduğu gibi, ardışık iki varlığı ayırt etmemiz gerekebilir. Bu nedenle, her varlık için iki sınıf kullanmak yaygındır - biri varlığın ilk token'ını belirten (`B-` ön eki genellikle **başlangıç** için kullanılır) ve diğeri varlığın devamını belirten (`I-`, **iç token** için). Ayrıca, tüm **diğer** token'ları temsil etmek için `O` sınıfını kullanırız. Bu tür token etiketleme, [BIO etiketleme](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (veya IOB) olarak adlandırılır. Etiketlendiğinde, başlığımız şu şekilde görünecektir:

Token | Etiket
------|-----
Tricuspid | B-DIS
kapak | I-DIS
yetmezliği | I-DIS
ve | O
lityum | B-CHEM
karbonat | I-CHEM
toksisitesi | B-DIS
bir | O
yenidoğan | O
bebekte | O
. | O

Token'lar ve sınıflar arasında birebir bir ilişki kurmamız gerektiğinden, bu resimdeki gibi bir **çoktan-çoka** sinir ağı modeli eğitebiliriz:

![Yaygın tekrarlayan sinir ağı desenlerini gösteren bir görsel.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.tr.jpg)

> *Görsel, [Andrej Karpathy](http://karpathy.github.io/) tarafından yazılmış [bu blog yazısından](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) alınmıştır. NER token sınıflandırma modelleri, bu resimdeki en sağdaki ağ mimarisine karşılık gelir.*

## NER Modellerini Eğitmek

Bir NER modeli aslında bir token sınıflandırma modeli olduğundan, bu görev için zaten aşina olduğumuz RNN'leri kullanabiliriz. Bu durumda, tekrarlayan ağın her bir bloğu token kimliğini döndürecektir. Aşağıdaki örnek defter, token sınıflandırması için bir LSTM'nin nasıl eğitileceğini göstermektedir.

## ✍️ Örnek Defterler: NER

Aşağıdaki defterde öğrenmeye devam edin:

* [TensorFlow ile NER](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Sonuç

Bir NER modeli, bir **token sınıflandırma modeli** olup, token sınıflandırması gerçekleştirmek için kullanılabilir. Bu, metin içinde yerler, isimler, tarihler ve daha fazlasını tanımaya yardımcı olan çok yaygın bir NLP görevidir.

## 🚀 Zorluk

Aşağıda bağlantısı verilen ödevi tamamlayarak tıbbi terimler için bir adlandırılmış varlık tanıma modeli eğitin ve ardından bunu farklı bir veri kümesi üzerinde deneyin.

## [Ders Sonrası Test](https://ff-quizzes.netlify.app/en/ai/quiz/38)

## Gözden Geçirme ve Kendi Kendine Çalışma

[Recurrent Neural Networks'ün Akıl Almaz Etkililiği](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) başlıklı blog yazısını okuyun ve bu makaledeki Daha Fazla Okuma bölümünü takip ederek bilginizi derinleştirin.

## [Ödev](lab/README.md)

Bu dersin ödevinde, bir tıbbi varlık tanıma modeli eğitmeniz gerekecek. Bu derste açıklandığı gibi bir LSTM modeli eğiterek başlayabilir ve ardından BERT dönüştürücü modelini kullanmaya geçebilirsiniz. Tüm detayları öğrenmek için [talimatları okuyun](lab/README.md).

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.