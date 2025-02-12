# Tekrarlayan Sinir Ağları

## [Ders öncesi quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/116)

Önceki bölümlerde, metnin zengin anlamsal temsillerini ve gömme katmanlarının üstünde basit bir doğrusal sınıflayıcı kullanıyorduk. Bu mimari, bir cümledeki kelimelerin toplam anlamını yakalamaya çalışır, ancak kelimelerin **sırasını** dikkate almaz; çünkü gömme katmanları üzerindeki toplama işlemi, bu bilgiyi orijinal metinden çıkarmıştır. Bu modeller kelime sıralamasını modelleyemediğinden, metin üretimi veya soru yanıtlama gibi daha karmaşık veya belirsiz görevleri yerine getiremezler.

Metin dizisinin anlamını yakalamak için, **tekrarlayan sinir ağı** (RNN) adı verilen başka bir sinir ağı mimarisi kullanmamız gerekiyor. RNN'de, cümlemizi bir sembolü bir seferde geçiriyoruz ve ağ, ardından bir **durum** üretiyor; bu durumu bir sonraki sembol ile birlikte tekrar ağa iletiyoruz.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.tr.png)

> Yazarın resmi

X<sub>0</sub>,...,X<sub>n</sub> token dizisi verildiğinde, RNN bir sinir ağı blokları dizisi oluşturur ve bu diziyi geri yayılım kullanarak uçtan uca eğitir. Her ağ bloğu, bir çift (X<sub>i</sub>,S<sub>i</sub>) alır ve S<sub>i+1</sub> olarak bir sonuç üretir. Son durum S<sub>n</sub> veya (çıkış Y<sub>n</sub>) bir doğrusal sınıflayıcıya gider ve sonucu üretir. Tüm ağ blokları aynı ağırlıkları paylaşır ve tek bir geri yayılım geçişi kullanılarak uçtan uca eğitilir.

Durum vektörleri S<sub>0</sub>,...,S<sub>n</sub> ağdan geçirilerek, kelimeler arasındaki sıralı bağımlılıkları öğrenebilir. Örneğin, dizide *not* kelimesi geçtiğinde, belirli öğeleri durum vektöründe olumsuzlamak için öğrenebiliriz, bu da olumsuzluk yaratır.

> ✅ Yukarıdaki resimdeki tüm RNN bloklarının ağırlıkları paylaşıldığından, aynı resim, ağın çıkış durumunu girdi olarak geri ileten bir tekrarlayan geri besleme döngüsü ile bir blok (sağda) olarak temsil edilebilir.

## RNN Hücresinin Anatomisi

Basit bir RNN hücresinin nasıl organize edildiğine bakalım. Önceki durum S<sub>i-1</sub> ve mevcut sembol X<sub>i</sub> olarak girdileri kabul eder ve çıkış durumu S<sub>i</sub> üretmelidir (ve bazen, üretken ağlarla olduğu gibi, başka bir çıkış Y<sub>i</sub> ile de ilgileniyoruz).

Basit bir RNN hücresinin içinde iki ağırlık matris vardır: biri bir giriş sembolünü dönüştürür (buna W diyelim), diğeri ise bir giriş durumunu dönüştürür (H). Bu durumda, ağın çıktısı σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b) olarak hesaplanır; burada σ aktivasyon fonksiyonu ve b ek bir önyargıdır.

<img alt="RNN Hücre Anatomisi" src="images/rnn-anatomy.png" width="50%"/>

> Yazarın resmi

Birçok durumda, giriş tokenları RNN'ye girmeden önce gömme katmanından geçirilir, bu da boyutu azaltır. Bu durumda, giriş vektörlerinin boyutu *emb_size* ve durum vektörü *hid_size* ise, W'nin boyutu *emb_size*×*hid_size* ve H'nin boyutu *hid_size*×*hid_size* olur.

## Uzun Kısa Süreli Bellek (LSTM)

Klasik RNN'lerin en büyük problemlerinden biri, sözde **kaybolan gradyanlar** problemidir. RNN'ler, tek bir geri yayılım geçişinde uçtan uca eğitildiğinden, hatayı ağın ilk katmanlarına iletmekte zorluk çeker ve dolayısıyla ağ, uzak tokenlar arasındaki ilişkileri öğrenemez. Bu problemi aşmanın yollarından biri, **açık durum yönetimi** sağlamak için sözde **kapılar** kullanmaktır. Bu türde iki iyi bilinen mimari vardır: **Uzun Kısa Süreli Bellek** (LSTM) ve **Kapalı Röle Birimi** (GRU).

![Uzun Kısa Süreli Bellek hücresini gösteren bir resim](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Resim kaynağı TBD

LSTM Ağı, RNN'e benzer bir şekilde organize edilmiştir, ancak katmanlar arasında geçirilen iki durum vardır: gerçek durum C ve gizli vektör H. Her birimde, gizli vektör H<sub>i</sub>, giriş X<sub>i</sub> ile birleştirilir ve durum C üzerindeki etkilerini **kapılar** aracılığıyla kontrol ederler. Her kapı, sigmoid aktivasyona sahip bir sinir ağıdır (çıkış [0,1] aralığında), bu da durum vektörü ile çarpıldığında bit düzeyinde bir maske olarak düşünülebilir. Yukarıdaki resimde soldan sağa doğru şu kapılar vardır:

* **Unutma kapısı**, bir gizli vektör alır ve vektör C'nin hangi bileşenlerini unutmamız gerektiğini ve hangilerini geçirmemiz gerektiğini belirler.
* **Giriş kapısı**, giriş ve gizli vektörlerden bazı bilgileri alır ve bunu duruma ekler.
* **Çıkış kapısı**, durumu *tanh* aktivasyonuna sahip bir doğrusal katman aracılığıyla dönüştürür, ardından yeni bir durum C<sub>i+1</sub> üretmek için gizli vektör H<sub>i</sub> kullanarak bazı bileşenlerini seçer.

Durum C'nin bileşenleri, açılıp kapanabilen bazı bayraklar olarak düşünülebilir. Örneğin, dizide *Alice* adını bulduğumuzda, bunun bir kadın karakteri ifade ettiğini varsayabiliriz ve cümlede bir kadın isim olduğu bayrağını açarız. Daha sonra *and Tom* ifadeleri ile karşılaştığımızda, çoğul bir isim olduğuna dair bayrağı açarız. Böylece durumu manipüle ederek cümle parçalarının dilbilgisel özelliklerini takip edebiliriz.

> ✅ LSTM'nin iç işleyişini anlamak için harika bir kaynak, Christopher Olah tarafından yazılmış [LSTM Ağlarını Anlamak](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) adlı makaledir.

## İki Yönlü ve Çok Katmanlı RNN'ler

Bir dizinin başlangıcından sonuna doğru tek yönde çalışan tekrarlayan ağları tartıştık. Bu doğal görünmektedir, çünkü okumaya ve konuşmayı dinlemeye benzer. Ancak, birçok pratik durumda girdi dizisine rastgele erişimimiz olduğundan, tekrarlayan hesaplamayı her iki yönde de çalıştırmak mantıklı olabilir. Bu tür ağlara **iki yönlü** RNN'ler denir. İki yönlü bir ağla çalışırken, her yön için iki gizli durum vektörüne ihtiyacımız olacaktır.

Bir Tekrarlayan ağ, ister tek yönlü ister iki yönlü olsun, bir dizideki belirli kalıpları yakalar ve bunları bir durum vektöründe depolayabilir veya çıkışa iletebilir. Konvolüsyonel ağlarla olduğu gibi, ilk katmanın çıkışından daha yüksek düzeyde kalıpları yakalamak ve ilk katmanın çıkardığı düşük düzey kalıplardan inşa etmek için üstte başka bir tekrarlayan katman oluşturabiliriz. Bu, **çok katmanlı RNN** kavramına götürür; bu, bir önceki katmanın çıktısının bir sonraki katmana girdi olarak iletildiği iki veya daha fazla tekrarlayan ağdan oluşur.

![Çok Katmanlı uzun-kısa süreli bellek RNN'yi gösteren bir resim](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.tr.jpg)

*Resim [bu harika yazıdan](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) Fernando López tarafından alınmıştır.*

## ✍️ Alıştırmalar: Gömme

Aşağıdaki defterlerde öğrenmeye devam edin:

* [PyTorch ile RNN'ler](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [TensorFlow ile RNN'ler](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## Sonuç

Bu birimde, RNN'lerin dizi sınıflandırması için kullanılabileceğini gördük, ancak aslında metin üretimi, makine çevirisi ve daha fazlası gibi birçok başka görevi de yerine getirebilirler. Bu görevleri bir sonraki birimde ele alacağız.

## 🚀 Zorluk

LSTM'ler hakkında bazı literatürleri okuyun ve uygulamalarını düşünün:

- [Grid Uzun Kısa Süreli Bellek](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Göster, Katıl ve Söyle: Görsel Dikkat ile Sinirsel Görüntü Başlığı Üretimi](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Ders sonrası quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/216)

## İnceleme & Kendi Kendine Çalışma

- [LSTM Ağlarını Anlamak](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) Christopher Olah tarafından.

## [Ödev: Defterler](assignment.md)

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanılması sonucu ortaya çıkan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul etmiyoruz.