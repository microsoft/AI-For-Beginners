<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58bf4adb210aab53e8f78c8082040e7c",
  "translation_date": "2025-08-26T07:19:48+00:00",
  "source_file": "lessons/5-NLP/16-RNN/README.md",
  "language_code": "tr"
}
-->
# Tekrarlayan Sinir Ağları

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ai/quiz/31)

Önceki bölümlerde, metinlerin zengin anlamsal temsillerini ve gömme katmanlarının üzerine basit bir doğrusal sınıflandırıcıyı kullandık. Bu mimarinin yaptığı şey, bir cümledeki kelimelerin toplu anlamını yakalamaktır, ancak kelimelerin **sırasını** dikkate almaz, çünkü gömme katmanlarının üzerindeki toplama işlemi bu bilgiyi orijinal metinden kaldırır. Bu modeller kelime sırasını modelleyemediği için, metin üretimi veya soru yanıtlama gibi daha karmaşık veya belirsiz görevleri çözemezler.

Metin dizisinin anlamını yakalamak için, **tekrarlayan sinir ağı** veya RNN adı verilen başka bir sinir ağı mimarisini kullanmamız gerekir. RNN'de, cümlemizi ağdan bir sembol bir sembol geçiririz ve ağ bir **durum** üretir, bu durumu bir sonraki sembolle birlikte tekrar ağa iletiriz.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.tr.png)

> Görsel: Yazar tarafından oluşturulmuştur

X<sub>0</sub>,...,X<sub>n</sub> giriş dizi sembolleri verildiğinde, RNN bir sinir ağı blokları dizisi oluşturur ve bu diziyi baştan sona geri yayılım kullanarak eğitir. Her ağ bloğu bir çift (X<sub>i</sub>,S<sub>i</sub>) giriş olarak alır ve sonuç olarak S<sub>i+1</sub> üretir. Son durum S<sub>n</sub> veya (çıktı Y<sub>n</sub>), sonucu üretmek için doğrusal bir sınıflandırıcıya gider. Tüm ağ blokları aynı ağırlıkları paylaşır ve tek bir geri yayılım geçişiyle baştan sona eğitilir.

Durum vektörleri S<sub>0</sub>,...,S<sub>n</sub> ağdan geçtiği için, kelimeler arasındaki sıralı bağımlılıkları öğrenebilir. Örneğin, dizide bir yerde *değil* kelimesi geçtiğinde, durum vektöründeki belirli öğeleri olumsuzlamak için öğrenebilir ve bu da olumsuzlama ile sonuçlanır.

> ✅ Yukarıdaki resimdeki tüm RNN bloklarının ağırlıkları paylaşıldığından, aynı resim bir geri besleme döngüsü olan tek bir blok (sağda) olarak temsil edilebilir ve ağın çıktı durumunu girişe geri iletir.

## Bir RNN Hücresinin Anatomisi

Basit bir RNN hücresinin nasıl organize edildiğini görelim. Önceki durum S<sub>i-1</sub> ve mevcut sembol X<sub>i</sub>'yi giriş olarak alır ve çıktı durumu S<sub>i</sub>'yi üretmek zorundadır (ve bazen, üretici ağlarda olduğu gibi, başka bir çıktı Y<sub>i</sub> ile de ilgileniriz).

Basit bir RNN hücresinin içinde iki ağırlık matrisi vardır: biri bir giriş sembolünü dönüştürür (W olarak adlandıralım) ve diğeri bir giriş durumunu dönüştürür (H). Bu durumda ağın çıktısı σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b) olarak hesaplanır, burada σ aktivasyon fonksiyonu ve b ek bir yanlılıktır.

<img alt="RNN Hücresi Anatomisi" src="images/rnn-anatomy.png" width="50%"/>

> Görsel: Yazar tarafından oluşturulmuştur

Çoğu durumda, giriş sembolleri RNN'ye girmeden önce boyutları düşürmek için gömme katmanından geçirilir. Bu durumda, eğer giriş vektörlerinin boyutu *emb_size* ve durum vektörünün boyutu *hid_size* ise - W'nin boyutu *emb_size*×*hid_size*, H'nin boyutu ise *hid_size*×*hid_size* olur.

## Uzun Kısa Süreli Bellek (LSTM)

Klasik RNN'lerin ana problemlerinden biri, **kaybolan gradyanlar** problemidir. RNN'ler tek bir geri yayılım geçişinde baştan sona eğitildiği için, hatayı ağın ilk katmanlarına iletmekte zorlanır ve bu nedenle ağ, uzak semboller arasındaki ilişkileri öğrenemez. Bu sorunu önlemenin bir yolu, **kapılar** kullanarak **açık durum yönetimi** tanıtmaktır. Bu tür iki iyi bilinen mimari vardır: **Uzun Kısa Süreli Bellek** (LSTM) ve **Kapılı Röle Birimi** (GRU).

![Bir uzun kısa süreli bellek hücresi örneğini gösteren görsel](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Görsel kaynağı belirlenecek

LSTM Ağı, RNN'ye benzer bir şekilde organize edilmiştir, ancak katmandan katmana geçen iki durum vardır: gerçek durum C ve gizli vektör H. Her birimde, gizli vektör H<sub>i</sub>, giriş X<sub>i</sub> ile birleştirilir ve bunlar **kapılar** aracılığıyla durum C'de ne olacağını kontrol eder. Her kapı, sigmoid aktivasyonlu (çıktı [0,1] aralığında) bir sinir ağıdır ve durum vektörü ile çarpıldığında bit düzeyinde bir maske olarak düşünülebilir. Aşağıdaki kapılar vardır (yukarıdaki resimde soldan sağa):

* **Unutma kapısı**, bir gizli vektör alır ve C vektörünün hangi bileşenlerini unutmamız gerektiğini ve hangilerini geçirmemiz gerektiğini belirler.
* **Giriş kapısı**, giriş ve gizli vektörlerden bazı bilgileri alır ve duruma ekler.
* **Çıkış kapısı**, durumu *tanh* aktivasyonlu bir doğrusal katman aracılığıyla dönüştürür, ardından yeni bir durum C<sub>i+1</sub> üretmek için gizli vektör H<sub>i</sub>'yi kullanarak bazı bileşenlerini seçer.

Durum C'nin bileşenleri, açılıp kapatılabilen bayraklar olarak düşünülebilir. Örneğin, dizide *Alice* adında bir isimle karşılaştığımızda, bunun bir kadın karaktere atıfta bulunduğunu varsaymak ve cümlede bir kadın isim olduğunu belirten bayrağı kaldırmak isteyebiliriz. Daha sonra *ve Tom* ifadeleriyle karşılaştığımızda, çoğul bir isim olduğunu belirten bayrağı kaldırabiliriz. Böylece, durumu manipüle ederek cümlenin gramer özelliklerini takip edebiliriz.

> ✅ LSTM'nin iç işleyişini anlamak için mükemmel bir kaynak, Christopher Olah'ın [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) adlı harika makalesidir.

## Çift Yönlü ve Çok Katmanlı RNN'ler

Bir dizinin başından sonuna doğru çalışan tekrarlayan ağları tartıştık. Bu doğal görünüyor, çünkü okuma ve konuşmayı dinleme şeklimize benziyor. Ancak, birçok pratik durumda giriş dizisine rastgele erişimimiz olduğu için, tekrarlayan hesaplamayı her iki yönde de çalıştırmak mantıklı olabilir. Bu tür ağlara **çift yönlü** RNN'ler denir. Çift yönlü bir ağla çalışırken, her yön için birer gizli durum vektörüne ihtiyacımız olacaktır.

Tek yönlü veya çift yönlü bir tekrarlayan ağ, bir dizideki belirli kalıpları yakalar ve bunları bir durum vektörüne depolayabilir veya çıktıya aktarabilir. Konvolüsyonel ağlarda olduğu gibi, ilk katman tarafından çıkarılan düşük seviyeli kalıplardan daha yüksek seviyeli kalıpları yakalamak ve inşa etmek için ilk katmanın üzerine başka bir tekrarlayan katman inşa edebiliriz. Bu bizi, önceki katmanın çıktısının bir sonraki katmana giriş olarak geçtiği iki veya daha fazla tekrarlayan ağdan oluşan bir **çok katmanlı RNN** kavramına götürür.

![Çok katmanlı uzun kısa süreli bellek RNN'yi gösteren görsel](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.tr.jpg)

*[Bu harika gönderiden](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) alınan resim, Fernando López tarafından yazılmıştır.*

## ✍️ Alıştırmalar: Gömme Katmanları

Aşağıdaki defterlerde öğrenmeye devam edin:

* [PyTorch ile RNN'ler](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [TensorFlow ile RNN'ler](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## Sonuç

Bu birimde, RNN'lerin dizi sınıflandırması için kullanılabileceğini gördük, ancak aslında metin üretimi, makine çevirisi ve daha fazlası gibi birçok görevi yerine getirebilirler. Bu görevleri bir sonraki birimde ele alacağız.

## 🚀 Zorluk

LSTM'ler hakkında bazı literatürleri okuyun ve uygulamalarını düşünün:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Ders Sonrası Test](https://ff-quizzes.netlify.app/en/ai/quiz/32)

## Gözden Geçirme ve Kendi Kendine Çalışma

- Christopher Olah'ın [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) adlı makalesi.

## [Ödev: Defterler](assignment.md)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.