# Çoklu-Ajan Sistemleri

Zeka elde etmenin olası yollarından biri, birçok nispeten basit ajanın birleşik davranışının, sistemin genelinde daha karmaşık (veya zeki) bir davranışa yol açabileceği gerçeğine dayanan **ortaya çıkan** (veya **sinergik**) yaklaşımdır. Teorik olarak, bu, daha düşük seviyedeki sistemlerden uygun bir şekilde bir araya getirildiğinde daha yüksek seviyedeki sistemlerin bir tür ek değer kazandığını belirten [Kollektif Zeka](https://en.wikipedia.org/wiki/Collective_intelligence), [Ortaya Çıkma](https://en.wikipedia.org/wiki/Global_brain) ve [Evrimsel Sibernetik](https://en.wikipedia.org/wiki/Global_brain) ilkelerine dayanmaktadır (buna *metasistem geçişi ilkesi* denir).

## [Ders Öncesi Quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/123)

**Çoklu-Ajan Sistemleri** yönelimi, 1990'larda internetin ve dağıtık sistemlerin büyümesine bir yanıt olarak AI'da ortaya çıkmıştır. Klasik AI ders kitaplarından biri olan [Yapay Zeka: Modern Bir Yaklaşım](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), Çoklu-Ajan Sistemleri açısından klasik AI'ya dair bir bakış açısına odaklanmaktadır.

Çoklu-ajan yaklaşımının merkezinde **Ajan** kavramı yer almaktadır - belirli bir **çevrede** yaşayan, bunu algılayabilen ve buna göre hareket edebilen bir varlık. Bu çok geniş bir tanım olup, ajanın birçok farklı türü ve sınıflandırması olabilir:

* Akıl yürütme yeteneklerine göre:
   - **Reaktif** ajanlar genellikle basit istek-cevap türünde bir davranış sergiler
   - **Deliberatif** ajanlar bir tür mantıksal akıl yürütme ve/veya planlama yetenekleri kullanır
* Ajanın kodunu çalıştırdığı yere göre:
   - **Statik** ajanlar, belirli bir ağ düğümünde çalışır
   - **Mobil** ajanlar, kodlarını ağ düğümleri arasında taşıyabilir
* Davranışlarına göre:
   - **Pasif ajanlar** belirli hedeflere sahip değildir. Bu tür ajanlar dışsal uyarıcılara yanıt verebilir, ancak kendileri herhangi bir eylem başlatmaz.
   - **Aktif ajanlar** belirli hedeflere sahiptir ve bunları takip eder
   - **Bilişsel ajanlar** karmaşık planlama ve akıl yürütme içerir

Günümüzde çoklu-ajan sistemleri birçok uygulamada kullanılmaktadır:

* Oyunlarda, birçok NPC (oyuncu olmayan karakter) bir tür AI kullanır ve zeki ajanlar olarak kabul edilebilir
* Video prodüksiyonunda, kalabalıkları içeren karmaşık 3D sahnelerin işlenmesi genellikle çoklu-ajan simülasyonu kullanılarak yapılır
* Sistem modellemesinde, karmaşık bir modelin davranışını simüle etmek için çoklu-ajan yaklaşımı kullanılmaktadır. Örneğin, çoklu-ajan yaklaşımı, COVID-19 hastalığının dünya çapında yayılmasını tahmin etmek için başarıyla kullanılmıştır. Benzer bir yaklaşım, şehirdeki trafiği modellemek ve trafik kurallarındaki değişikliklere nasıl tepki verdiğini görmek için kullanılabilir.
* Karmaşık otomasyon sistemlerinde, her cihaz bağımsız bir ajan olarak hareket edebilir, bu da tüm sistemi daha az monolitik ve daha dayanıklı hale getirir.

Çoklu-ajan sistemleri derinlemesine incelemek için fazla zaman harcamayacağız, ancak **Çoklu-Ajan Modelleme** örneğini ele alacağız.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) , [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) programlama dilinin değiştirilmiş bir versiyonuna dayanan çoklu-ajan modelleme ortamıdır. Bu dil, programlama kavramlarını çocuklara öğretmek için geliştirilmiştir ve hareket edebilen ve arkasında iz bırakan **kaplumbağa** adlı bir ajanın kontrolünü sağlar. Bu, karmaşık geometrik figürler oluşturmayı mümkün kılar, bu da bir ajanın davranışını anlamanın çok görsel bir yoludur.

NetLogo'da, `create-turtles` komutunu kullanarak birçok kaplumbağa oluşturabiliriz. Daha sonra tüm kaplumbağalara bazı eylemler gerçekleştirmelerini (aşağıdaki örnekte - 10 birim ileri) emredebiliriz:

```
create-turtles 10
ask turtles [
  forward 10
]
```

Elbette, tüm kaplumbağaların aynı şeyi yapması ilginç değildir, bu nedenle `ask` groups of turtles, eg. those who are in the vicinity of a certain point. We can also create turtles of different *breeds* using `breed [cats cat]` command. Here `cat` bir türün adıdır ve farklı komutların netlik açısından farklı biçimler kullandığı için hem tekil hem de çoğul kelimeyi belirtmemiz gerekir.

> ✅ NetLogo dilini öğrenmeye girmeyeceğiz - daha fazla bilgi edinmek isterseniz harika [Başlangıç Seviyesi Etkileşimli NetLogo Sözlüğü](https://ccl.northwestern.edu/netlogo/bind/) kaynağını ziyaret edebilirsiniz.

NetLogo'yu denemek için [indirin](https://ccl.northwestern.edu/netlogo/download.shtml) ve kurun.

### Modeller Kütüphanesi

NetLogo'nun harika bir yanı, deneyebileceğiniz çalışan modellerin bulunduğu bir kütüphane içermesidir. **Dosya → Modeller Kütüphanesi** menüsüne gidin ve birçok model kategorisinden birini seçin.

<img alt="NetLogo Modeller Kütüphanesi" src="images/NetLogo-ModelLib.png" width="60%"/>

> Dmitry Soshnikov tarafından modeller kütüphanesinin ekran görüntüsü

Bir model açabilirsiniz, örneğin **Biyoloji → Sürüler**.

### Ana İlkeler

Modeli açtıktan sonra, sizi ana NetLogo ekranına alır. İşte sınırlı kaynaklar (ot) göz önünde bulundurulduğunda kurtlar ve koyunların popülasyonunu tanımlayan bir örnek model.

![NetLogo Ana Ekranı](../../../../../translated_images/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.tr.png)

> Dmitry Soshnikov tarafından ekran görüntüsü

Bu ekranda şunları görebilirsiniz:

* **Arayüz** bölümü şunları içerir:
  - Tüm ajanların yaşadığı ana alan
  - Farklı kontroller: düğmeler, kaydırıcılar vb.
  - Simülasyonun parametrelerini görüntülemek için kullanabileceğiniz grafikler
* **Kod** sekmesi, NetLogo programını yazabileceğiniz editörü içerir

Çoğu durumda, arayüzde simülasyon durumunu başlatan bir **Kurulum** düğmesi ve yürütmeyi başlatan bir **Git** düğmesi bulunur. Bunlar, kodda şu şekilde görünen ilgili işleyiciler tarafından yönetilir:

```
to go [
...
]
```

NetLogo'nun dünyası aşağıdaki nesnelerden oluşur:

* Alan boyunca hareket edebilen ve bir şeyler yapabilen **Ajanlar** (kaplumbağalar). Ajanları, `ask turtles [...]` syntax, and the code in brackets is executed by all agents in *turtle mode*.
* **Patches** are square areas of the field, on which agents live. You can refer to all agents on the same patch, or you can change patch colors and some other properties. You can also `ask patches` kullanarak bir şeyler yapmaları için komut verirsiniz.
* **Gözlemci**, dünyayı kontrol eden benzersiz bir ajandır. Tüm düğme işleyicileri *gözlemci modu* içinde yürütülür.

> ✅ Çoklu-ajan ortamının güzelliği, kaplumbağa modunda veya yama modunda çalışan kodun, tüm ajanlar tarafından aynı anda paralel olarak yürütülmesidir. Böylece, biraz kod yazarak ve bireysel ajanın davranışını programlayarak, simülasyon sisteminin tamamının karmaşık davranışını oluşturabilirsiniz.

### Sürüleşme

Çoklu-ajan davranışına bir örnek olarak **[Sürüleşme](https://en.wikipedia.org/wiki/Flocking_(behavior))** konusunu ele alalım. Sürüleşme, kuş sürülerinin uçuşuna çok benzeyen karmaşık bir desen oluşturur. Onların uçuşunu izlerken, bir tür kolektif algoritmayı takip ettiklerini veya bir tür *kolektif zeka*ya sahip olduklarını düşünebilirsiniz. Ancak, bu karmaşık davranış, her bireysel ajanın (bu durumda bir *kuş*) sadece kısa bir mesafedeki diğer ajanları gözlemlemesi ve üç basit kurala uyması durumunda ortaya çıkar:

* **Hizalama** - komşu ajanların ortalama yönüne doğru yönelir
* **Birliktelik** - komşuların ortalama konumuna doğru yönelmeye çalışır (*uzun menzilli çekim*)
* **Ayrılma** - diğer kuşlara çok yaklaşınca uzaklaşmaya çalışır (*kısa menzilli itme*)

Sürüleşme örneğini çalıştırabilir ve davranışı gözlemleyebilirsiniz. Ayrıca, her kuşun görebildiği mesafeyi tanımlayan *ayrılma derecesi* veya *görüş açısı* gibi parametreleri ayarlayabilirsiniz. Görüş açısını 0'a düşürürseniz, tüm kuşlar kör olur ve sürüleşme durur. Ayrılmayı 0'a düşürürseniz, tüm kuşlar bir düz çizgi halinde toplanır.

> ✅ **Kod** sekmesine geçin ve sürüleşmenin üç kuralının (hizalama, birliktelik ve ayrılma) kodda nasıl uygulandığını görün. Sadece görüş alanında olan ajanslara nasıl atıfta bulunduğumuza dikkat edin.

### Görülecek Diğer Modeller

Deneyebileceğiniz birkaç ilginç model daha bulunmaktadır:

* **Sanat → Havai Fişekler**, bir havai fişeğin bireysel ateş akımlarının kolektif bir davranış olarak nasıl değerlendirilebileceğini gösterir
* **Sosyal Bilimler → Temel Trafik** ve **Sosyal Bilimler → Trafik Izgarası**, 1D ve 2D Izgara'da trafik modelini gösterir. Simülasyondaki her araç şu kurallara uyar:
   - Önündeki alan boşsa - hızlanır (belirli bir maksimum hıza kadar)
   - Önünde bir engel gördüğünde - frene basar (ve sürücünün ne kadar uzaktan görebileceğini ayarlayabilirsiniz)
* **Sosyal Bilimler → Parti**, insanların bir kokteyl partisinde nasıl gruplandığını gösterir. Hızlı bir şekilde grup mutluluğunu artıran parametre kombinasyonunu bulabilirsiniz.

Bu örneklerden de görebileceğiniz gibi, çoklu-ajan simülasyonları, aynı veya benzer mantığı takip eden bireylerden oluşan karmaşık bir sistemin davranışını anlamanın oldukça yararlı bir yolu olabilir. Ayrıca, [NPC'ler](https://en.wikipedia.org/wiki/NPC) gibi sanal ajanları veya 3D animasyonlu dünyalardaki ajanları kontrol etmek için de kullanılabilir.

## Deliberatif Ajanlar

Yukarıda tanımlanan ajanlar, çevredeki değişikliklere bir tür algoritma kullanarak yanıt veren çok basit ajandır. Bu nedenle, **reaktif ajanlar** olarak adlandırılırlar. Ancak, bazen ajanlar akıl yürütebilir ve eylemlerini planlayabilir, bu durumda **deliberatif** olarak adlandırılırlar.

Tipik bir örnek, bir insandan bir tatil turu rezervasyonu yapma talimatı alan kişisel bir ajandır. Varsayalım ki internette ona yardımcı olabilecek birçok ajan var. O zaman diğer ajanlarla iletişime geçmeli, hangi uçuşların mevcut olduğunu görmeli, farklı tarihler için otel fiyatlarını kontrol etmeli ve en iyi fiyatı pazarlık etmeye çalışmalıdır. Tatil planı tamamlandığında ve sahibi tarafından onaylandığında, rezervasyon yapmaya devam edebilir.

Bunu yapabilmek için, ajanların **iletişim kurması** gerekir. Başarılı iletişim için ihtiyaçları olanlar:

* Bilgi alışverişi için bazı **standart diller**, [Bilgi Değişim Formatı](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) ve [Bilgi Sorgulama ve Manipülasyon Dili](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML) gibi. Bu diller, [Konuşma Eylemi teorisi](https://en.wikipedia.org/wiki/Speech_act) temelinde tasarlanmıştır.
* Bu diller, farklı **ihale türlerine** dayalı bazı **pazarlık protokollerini** de içermelidir.
* Aynı kavramlara atıfta bulunabilmeleri için bir **ortak ontoloji** kullanılmalıdır.
* Farklı ajanların ne yapabileceğini **keşfetme** yolu, yine bir tür ontoloji temelinde olmalıdır.

Deliberatif ajanlar, çevredeki değişikliklere yalnızca tepki vermekle kalmadıkları için reaktif ajandan çok daha karmaşıktır; aynı zamanda eylemleri *başlatabilmelidirler*. Deliberatif ajanlar için önerilen mimarilerden biri, Belief-Desire-Intention (BDI) ajanı olarak adlandırılan yapıdır:

* **İnançlar**, bir ajanın çevresi hakkında bir bilgi seti oluşturur. Bu, bir bilgi tabanı veya ajanın çevredeki belirli bir duruma uygulayabileceği kurallar seti olarak yapılandırılabilir.
* **İstekler**, bir ajanın ne yapmak istediğini, yani hedeflerini tanımlar. Örneğin, yukarıdaki kişisel asistan ajanın hedefi bir tur rezervasyonu yapmaktır, otel ajanının hedefi ise karı maksimize etmektir.
* **Niyetler**, bir ajanın hedeflerine ulaşmak için planladığı belirli eylemlerdir. Eylemler tipik olarak çevreyi değiştirir ve diğer ajanlarla iletişim kurar.

Çoklu-ajan sistemleri inşa etmek için [JADE](https://jade.tilab.com/) gibi bazı platformlar mevcuttur. [Bu makale](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf), çoklu-ajan platformlarının bir incelemesini ve çoklu-ajan sistemlerinin kısa bir tarihini ve farklı kullanım senaryolarını içermektedir.

## Sonuç

Çoklu-Ajan sistemleri çok farklı biçimler alabilir ve birçok farklı uygulamada kullanılabilir. Hepsi, bireysel bir ajanın daha basit davranışına odaklanma eğilimindedir ve **sinergik etki** sayesinde genel sistemin daha karmaşık davranışını elde ederler.

## 🚀 Zorluk

Bu dersi gerçek dünyaya taşıyın ve bir problemi çözebilecek bir çoklu-ajan sistemi kavramsallaştırmaya çalışın. Örneğin, bir çoklu-ajan sisteminin bir okul otobüsü rotasını optimize etmek için ne yapması gerekir? Bir fırında nasıl çalışabilir?

## [Ders Sonrası Quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/223)

## Gözden Geçirme & Kendi Kendine Çalışma

Bu tür bir sistemin sanayideki kullanımını gözden geçirin. Üretim veya video oyunu endüstrisi gibi bir alan seçin ve çoklu-ajan sistemlerinin benzersiz sorunları çözmek için nasıl kullanılabileceğini keşfedin.

## [NetLogo Görevi](assignment.md)

**Açıklama**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde otorite kaynağı olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul etmiyoruz.