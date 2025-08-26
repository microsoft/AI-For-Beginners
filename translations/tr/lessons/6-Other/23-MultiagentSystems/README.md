<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ddf651d7681b4449f9d09ea3b17911e",
  "translation_date": "2025-08-26T07:31:55+00:00",
  "source_file": "lessons/6-Other/23-MultiagentSystems/README.md",
  "language_code": "tr"
}
-->
# Çoklu Ajan Sistemleri

Zekayı elde etmenin olası yollarından biri, **ortaya çıkan** (veya **sinergik**) yaklaşım olarak adlandırılan yöntemdir. Bu yaklaşım, birçok nispeten basit ajanın birleşik davranışının, sistemin bir bütün olarak daha karmaşık (veya zeki) bir davranış sergilemesine yol açabileceği gerçeğine dayanır. Teorik olarak, bu yaklaşım [Kolektif Zeka](https://en.wikipedia.org/wiki/Collective_intelligence), [Emergentizm](https://en.wikipedia.org/wiki/Global_brain) ve [Evrimsel Sibernetik](https://en.wikipedia.org/wiki/Global_brain) ilkelerine dayanır. Bu ilkeler, alt düzey sistemlerin uygun şekilde birleştirildiğinde üst düzey sistemlerin bir tür ek değer kazandığını ifade eder (*metasistem geçişi ilkesi* olarak adlandırılır).

## [Ders Öncesi Test](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/123)

**Çoklu Ajan Sistemleri** yönelimi, 1990'larda internetin ve dağıtık sistemlerin büyümesine yanıt olarak yapay zekâ alanında ortaya çıkmıştır. Klasik yapay zekâ ders kitaplarından biri olan [Artificial Intelligence: A Modern Approach](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), klasik yapay zekâya Çoklu Ajan Sistemleri perspektifinden bakar.

Çoklu ajan yaklaşımının merkezinde **Ajan** kavramı yer alır. Ajan, bir **çevrede** yaşayan, bu çevreyi algılayabilen ve üzerinde eylemde bulunabilen bir varlıktır. Bu oldukça geniş bir tanımdır ve birçok farklı türde ve sınıflandırmada ajan olabilir:

* Akıl yürütme yeteneklerine göre:
   - **Tepkisel** ajanlar genellikle basit istek-yanıt türü davranışlara sahiptir.
   - **Düşünsel** ajanlar bir tür mantıksal akıl yürütme ve/veya planlama yetenekleri kullanır.
* Kodlarını çalıştırdıkları yere göre:
   - **Statik** ajanlar belirli bir ağ düğümünde çalışır.
   - **Mobil** ajanlar kodlarını ağ düğümleri arasında taşıyabilir.
* Davranışlarına göre:
   - **Pasif ajanlar** belirli bir hedefe sahip değildir. Bu tür ajanlar dış uyaranlara tepki verebilir, ancak kendiliğinden bir eylem başlatmaz.
   - **Aktif ajanlar** belirli hedeflere sahiptir ve bu hedeflere ulaşmaya çalışır.
   - **Bilişsel ajanlar**, karmaşık planlama ve akıl yürütme içerir.

Günümüzde çoklu ajan sistemleri birçok uygulamada kullanılmaktadır:

* Oyunlarda, birçok oyuncu olmayan karakter bir tür yapay zekâ kullanır ve zeki ajanlar olarak kabul edilebilir.
* Video prodüksiyonunda, kalabalıkları içeren karmaşık 3D sahnelerin render edilmesi genellikle çoklu ajan simülasyonu kullanılarak yapılır.
* Sistem modellemede, çoklu ajan yaklaşımı karmaşık bir modelin davranışını simüle etmek için kullanılır. Örneğin, çoklu ajan yaklaşımı COVID-19 hastalığının dünya çapında yayılmasını tahmin etmek için başarıyla kullanılmıştır. Benzer bir yaklaşım, bir şehirdeki trafiği modellemek ve trafik kurallarındaki değişikliklere nasıl tepki verdiğini görmek için kullanılabilir.
* Karmaşık otomasyon sistemlerinde, her cihaz bağımsız bir ajan olarak hareket edebilir, bu da tüm sistemi daha az monolitik ve daha sağlam hale getirir.

Çoklu ajan sistemlerine derinlemesine dalmak için fazla zaman harcamayacağız, ancak **Çoklu Ajan Modelleme** örneğini ele alacağız.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/), [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) programlama dilinin değiştirilmiş bir versiyonuna dayanan bir çoklu ajan modelleme ortamıdır. Bu dil, çocuklara programlama kavramlarını öğretmek için geliştirilmiştir ve bir iz bırakarak hareket edebilen **kaplumbağa** adlı bir ajanı kontrol etmenizi sağlar. Bu, bir ajanın davranışını anlamanın oldukça görsel bir yolu olan karmaşık geometrik şekiller oluşturmayı mümkün kılar.

NetLogo'da, `create-turtles` komutunu kullanarak birçok kaplumbağa oluşturabiliriz. Daha sonra tüm kaplumbağalara bazı eylemler yapmalarını emredebiliriz (aşağıdaki örnekte - 10 birim ileri hareket):

```
create-turtles 10
ask turtles [
  forward 10
]
```

Tabii ki, tüm kaplumbağaların aynı şeyi yapması ilginç değildir, bu yüzden belirli bir noktanın yakınındaki kaplumbağalar gibi gruplara `ask` komutunu kullanarak emir verebiliriz. Ayrıca, `breed [cats cat]` komutunu kullanarak farklı *türlerde* kaplumbağalar oluşturabiliriz. Burada `cat`, bir türün adıdır ve hem tekil hem de çoğul kelimeyi belirtmemiz gerekir, çünkü farklı komutlar netlik için farklı formlar kullanır.

> ✅ NetLogo dilini öğrenmeye girmeyeceğiz - daha fazla bilgi edinmek isterseniz, harika [Başlangıç Seviyesi Etkileşimli NetLogo Sözlüğü](https://ccl.northwestern.edu/netlogo/bind/) kaynağını ziyaret edebilirsiniz.

NetLogo'yu [indirebilir](https://ccl.northwestern.edu/netlogo/download.shtml) ve kurarak deneyebilirsiniz.

### Modeller Kütüphanesi

NetLogo'nun harika bir özelliği, deneyebileceğiniz çalışan modellerin bulunduğu bir kütüphaneye sahip olmasıdır. **File → Models Library** seçeneğine gidin ve seçebileceğiniz birçok model kategorisi bulacaksınız.

<img alt="NetLogo Modeller Kütüphanesi" src="images/NetLogo-ModelLib.png" width="60%"/>

> Dmitry Soshnikov tarafından Modeller Kütüphanesi ekran görüntüsü

Bir modeli açabilirsiniz, örneğin **Biology → Flocking**.

### Ana İlkeler

Modeli açtıktan sonra, ana NetLogo ekranına yönlendirilirsiniz. İşte sınırlı kaynaklar (çimen) göz önüne alındığında kurtlar ve koyunların popülasyonunu tanımlayan bir örnek model:

![NetLogo Ana Ekran](../../../../../translated_images/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.tr.png)

> Dmitry Soshnikov tarafından ekran görüntüsü

Bu ekranda şunları görebilirsiniz:

* **Arayüz** bölümü, şunları içerir:
  - Tüm ajanların yaşadığı ana alan
  - Farklı kontroller: düğmeler, kaydırıcılar vb.
  - Simülasyon parametrelerini göstermek için kullanabileceğiniz grafikler
* **Kod** sekmesi, NetLogo programını yazabileceğiniz düzenleyiciyi içerir.

Çoğu durumda, arayüzde simülasyon durumunu başlatan bir **Setup** düğmesi ve yürütmeyi başlatan bir **Go** düğmesi bulunur. Bunlar, kodda şu şekilde görünen ilgili işleyiciler tarafından ele alınır:

```
to go [
...
]
```

NetLogo'nun dünyası şu nesnelerden oluşur:

* **Ajanlar** (kaplumbağalar), alan boyunca hareket edebilir ve bir şeyler yapabilir. Ajanlara `ask turtles [...]` sözdizimini kullanarak komut verirsiniz ve köşeli parantez içindeki kod, tüm ajanlar tarafından *kaplumbağa modunda* aynı anda yürütülür.
* **Yamalar**, ajanların yaşadığı alanın kare bölgeleridir. Aynı yamadaki tüm ajanlara başvurabilir veya yama renklerini ve diğer bazı özellikleri değiştirebilirsiniz. Ayrıca `ask patches` komutunu kullanarak yamalara bir şeyler yaptırabilirsiniz.
* **Gözlemci**, dünyayı kontrol eden benzersiz bir ajandır. Tüm düğme işleyicileri *gözlemci modunda* yürütülür.

> ✅ Çoklu ajan ortamının güzelliği, kaplumbağa modunda veya yama modunda çalışan kodun, tüm ajanlar tarafından aynı anda paralel olarak yürütülmesidir. Böylece, az miktarda kod yazarak ve bireysel bir ajanın davranışını programlayarak, tüm simülasyon sisteminin karmaşık davranışını oluşturabilirsiniz.

### Sürü Davranışı

Çoklu ajan davranışına bir örnek olarak, **[Sürü Davranışı](https://en.wikipedia.org/wiki/Flocking_(behavior))** ele alalım. Sürü davranışı, kuş sürülerinin uçuşuna çok benzeyen karmaşık bir desendir. Onları uçarken izlediğinizde, bir tür kolektif algoritmayı takip ettiklerini veya bir çeşit *kolektif zekâya* sahip olduklarını düşünebilirsiniz. Ancak, bu karmaşık davranış, her bir bireysel ajanın (bu durumda bir *kuş*) yalnızca kısa mesafedeki diğer ajanları gözlemlemesi ve üç basit kuralı takip etmesiyle ortaya çıkar:

* **Hizalanma** - komşu ajanların ortalama yönüne doğru yönelir.
* **Uyum** - komşuların ortalama konumuna doğru yönelmeye çalışır (*uzun menzilli çekim*).
* **Ayrılma** - diğer kuşlara çok yaklaştığında, uzaklaşmaya çalışır (*kısa menzilli itme*).

Sürü davranışı örneğini çalıştırabilir ve davranışı gözlemleyebilirsiniz. Ayrıca, *ayrılma derecesi* veya her kuşun ne kadar uzağı görebileceğini tanımlayan *görüş mesafesi* gibi parametreleri ayarlayabilirsiniz. Görüş mesafesini 0'a düşürdüğünüzde, tüm kuşlar kör olur ve sürü davranışı durur. Ayrılmayı 0'a düşürdüğünüzde, tüm kuşlar düz bir çizgide toplanır.

> ✅ **Kod** sekmesine geçin ve sürü davranışının üç kuralının (hizalanma, uyum ve ayrılma) kodda nerede uygulandığını görün. Sadece görüş alanındaki ajanlara başvurduğumuza dikkat edin.

### Görülecek Diğer Modeller

Deneyebileceğiniz birkaç ilginç model daha vardır:

* **Art → Fireworks**, bir havai fişeğin bireysel ateş akışlarının kolektif davranışı olarak nasıl düşünülebileceğini gösterir.
* **Social Science → Traffic Basic** ve **Social Science → Traffic Grid**, şehir trafiğinin 1D ve 2D Grid modellerini trafik ışıklarıyla veya ışıklar olmadan gösterir. Simülasyondaki her araba şu kuralları takip eder:
   - Önündeki alan boşsa - hızlanır (belirli bir maksimum hıza kadar).
   - Önündeki engeli görürse - fren yapar (ve bir sürücünün ne kadar uzağı görebileceğini ayarlayabilirsiniz).
* **Social Science → Party**, bir kokteyl partisinde insanların nasıl gruplandığını gösterir. Grubun mutluluğunun en hızlı artışına yol açan parametre kombinasyonunu bulabilirsiniz.

Bu örneklerden de görebileceğiniz gibi, çoklu ajan simülasyonları, aynı veya benzer mantığı izleyen bireylerden oluşan karmaşık bir sistemin davranışını anlamanın oldukça yararlı bir yolu olabilir. Ayrıca, bilgisayar oyunlarındaki [NPC'ler](https://en.wikipedia.org/wiki/NPC) gibi sanal ajanları veya 3D animasyonlu dünyalardaki ajanları kontrol etmek için de kullanılabilir.

## Düşünsel Ajanlar

Yukarıda açıklanan ajanlar oldukça basittir ve çevredeki değişikliklere bir tür algoritma kullanarak tepki verir. Bu tür ajanlar **tepkisel ajanlar** olarak adlandırılır. Ancak, bazen ajanlar akıl yürütebilir ve eylemlerini planlayabilir, bu durumda **düşünsel** olarak adlandırılırlar.

Tipik bir örnek, bir insandan tatil turu rezervasyonu yapma talimatı alan bir kişisel ajan olabilir. İnternette yaşayan birçok ajan olduğunu varsayalım, bu ajanlar ona yardımcı olabilir. Bu durumda, diğer ajanlarla iletişim kurarak hangi uçuşların mevcut olduğunu, farklı tarihler için otel fiyatlarını öğrenmeli ve en iyi fiyatı müzakere etmeye çalışmalıdır. Tatil planı tamamlandığında ve sahibi tarafından onaylandığında, rezervasyonu gerçekleştirebilir.

Bunu yapabilmek için ajanların **iletişim kurması** gerekir. Başarılı iletişim için şunlara ihtiyaç duyarlar:

* [Bilgi Değişim Formatı](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) ve [Bilgi Sorgulama ve Manipülasyon Dili](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML) gibi **bilgi alışverişi için standart dillere**. Bu diller, [Konuşma Eylemi Teorisi](https://en.wikipedia.org/wiki/Speech_act) temel alınarak tasarlanmıştır.
* Bu diller ayrıca farklı **müzakere protokollerini**, çeşitli **açık artırma türlerine** dayalı olarak içermelidir.
* Kullanılacak **ortak bir ontoloji**, böylece aynı kavramlara atıfta bulunabilir ve anlamlarını bilirler.
* Farklı ajanların ne yapabileceğini **keşfetme** yöntemi, yine bir tür ontolojiye dayalı olmalıdır.

Düşünsel ajanlar, tepkisel ajanlardan çok daha karmaşıktır, çünkü sadece çevredeki değişikliklere tepki vermekle kalmaz, aynı zamanda *eylemleri başlatabilmelidir*. Düşünsel ajanlar için önerilen mimarilerden biri, inanç-arzu-niyet (Belief-Desire-Intention, BDI) ajanıdır:

* **İnançlar**, bir ajanın çevresi hakkındaki bilgi kümesini oluşturur. Bu, bir bilgi tabanı veya bir ajanın çevredeki belirli bir duruma uygulayabileceği kurallar kümesi olarak yapılandırılabilir.
* **Arzular**, bir ajanın yapmak istediği şeyleri, yani hedeflerini tanımlar. Örneğin, yukarıdaki kişisel asistan ajanın hedefi bir tur rezervasyonu yapmakken, bir otel ajanın hedefi kârı maksimize etmektir.
* **Niyetler**, bir ajanın hedeflerine ulaşmak için planladığı belirli eylemlerdir. Eylemler genellikle çevreyi değiştirir ve diğer ajanlarla iletişim kurmayı gerektirir.

Çoklu ajan sistemleri oluşturmak için kullanılabilecek bazı platformlar mevcuttur, örneğin [JADE](https://jade.tilab.com/). [Bu makale](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf), çoklu ajan platformlarının bir incelemesini, çoklu ajan sistemlerinin kısa bir tarihçesi ve farklı kullanım senaryolarıyla birlikte sunmaktadır.

## Sonuç

Çoklu Ajan sistemleri çok farklı biçimler alabilir ve birçok farklı uygulamada kullanılabilir. 
Hepsi, bireysel bir ajanın daha basit davranışına odaklanma eğilimindedir ve **sinergik etki** sayesinde genel sistemin daha karmaşık bir davranış sergilemesini sağlar.

## 🚀 Meydan Okuma

Bu dersi gerçek dünyaya taşıyın ve bir sorunu çözebilecek bir çoklu ajan sistemi kavramsallaştırmaya çalışın. Örneğin, bir okul servisi rotasını optimize etmek için bir çoklu ajan sistemi ne yapmalıdır? Bir fırında nasıl çalışabilir?

## [Ders Sonrası Test](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/223)

## Gözden Geçirme ve Kendi Kendine Çalışma

Bu tür bir sistemin endüstride kullanımını gözden geçirin. Üretim veya video oyun endüstrisi gibi bir alan seçin ve çoklu ajan sistemlerinin benzersiz sorunları çözmek için nasıl kullanılabileceğini keşfedin.

## [NetLogo Ödevi](assignment.md)

**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belgenin kendi dilindeki hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.