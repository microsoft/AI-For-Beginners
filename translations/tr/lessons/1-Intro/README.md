<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-26T07:24:04+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "tr"
}
-->
# Yapay Zekaya Giriş

![Yapay Zeka içeriğinin bir çizim özeti](../../../../translated_images/ai-intro.bf28d1ac4235881c096f0ffdb320ba4102940eafcca4e9d7a55a03914361f8f3.tr.png)

> Çizim notu: [Tomomi Imura](https://twitter.com/girlie_mac)

## [Ders Öncesi Test](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/101)

**Yapay Zeka**, bilgisayarların insanlara özgü yetenekleri sergilemesini, yani insanların iyi olduğu şeyleri yapmasını sağlayan heyecan verici bir bilim dalıdır.

Başlangıçta bilgisayarlar, [Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage) tarafından iyi tanımlanmış bir prosedürü - bir algoritmayı - takip ederek sayılar üzerinde işlem yapmak için icat edilmiştir. Modern bilgisayarlar, 19. yüzyılda önerilen orijinal modelden çok daha gelişmiş olsalar da, hala kontrollü hesaplama fikrini takip eder. Bu nedenle, bir hedefe ulaşmak için gereken adımların tam sırasını biliyorsak, bir bilgisayarı bir şey yapması için programlamak mümkündür.

![Bir kişinin fotoğrafı](../../../../translated_images/dsh_age.d212a30d4e54fb5f68b94a624aad64bc086124bcbbec9561ae5bd5da661e22d8.tr.png)

> Fotoğraf: [Vickie Soshnikova](http://twitter.com/vickievalerie)

> ✅ Bir kişinin fotoğrafından yaşını belirlemek, açıkça programlanamayan bir görevdir çünkü bunu yaparken kafamızda bir sayı nasıl oluştuğunu tam olarak bilmiyoruz.

---

Ancak, çözümünü açıkça bilmediğimiz bazı görevler vardır. Örneğin, bir kişinin fotoğrafından yaşını belirlemeyi düşünün. Bunu bir şekilde öğreniriz çünkü farklı yaşlardaki insanların birçok örneğini görmüşüzdür, ancak bunu nasıl yaptığımızı açıkça açıklayamayız veya bilgisayarı bunu yapacak şekilde programlayamayız. İşte tam da bu tür görevler **Yapay Zeka** (kısaca AI) için ilgi çekicidir.

✅ AI'dan faydalanabilecek bazı görevleri düşünün. Finans, tıp ve sanat gibi alanlarda bu alanlar bugün AI'dan nasıl faydalanıyor?

## Zayıf AI ve Güçlü AI

Zayıf AI | Güçlü AI
---------------------------------------|-------------------------------------
Zayıf AI, belirli bir görev veya dar bir görev seti için tasarlanmış ve eğitilmiş AI sistemlerini ifade eder. | Güçlü AI veya Genel Yapay Zeka (AGI), insan seviyesinde zeka ve anlayışa sahip AI sistemlerini ifade eder.
Bu AI sistemleri genel olarak zeki değildir; önceden tanımlanmış bir görevde mükemmel performans gösterirler ancak gerçek bir anlayış veya bilinçten yoksundurlar. | Bu AI sistemleri, bir insanın yapabileceği her türlü entelektüel görevi yerine getirebilir, farklı alanlara uyum sağlayabilir ve bir tür bilinç veya öz farkındalığa sahip olabilir.
Zayıf AI örnekleri arasında Siri veya Alexa gibi sanal asistanlar, akış hizmetleri tarafından kullanılan öneri algoritmaları ve belirli müşteri hizmeti görevleri için tasarlanmış sohbet robotları bulunur. | Güçlü AI'ya ulaşmak, AI araştırmalarının uzun vadeli bir hedefidir ve AI sistemlerinin geniş bir görev ve bağlam yelpazesinde akıl yürütebilmesi, öğrenebilmesi, anlayabilmesi ve uyum sağlayabilmesi için geliştirilmesini gerektirir.
Zayıf AI son derece özelleşmiştir ve dar alanının ötesinde insan benzeri bilişsel yeteneklere veya genel problem çözme yeteneklerine sahip değildir. | Güçlü AI şu anda teorik bir kavramdır ve hiçbir AI sistemi bu genel zeka seviyesine ulaşmamıştır.

Daha fazla bilgi için **[Artificial General Intelligence](https://en.wikipedia.org/wiki/Artificial_general_intelligence)** (AGI) bağlantısına bakabilirsiniz.

## Zeka Tanımı ve Turing Testi

**[Zeka](https://en.wikipedia.org/wiki/Intelligence)** terimiyle uğraşırken karşılaşılan sorunlardan biri, bu terimin net bir tanımının olmamasıdır. Zekanın **soyut düşünme** veya **öz farkındalık** ile bağlantılı olduğunu iddia edebilirsiniz, ancak bunu doğru bir şekilde tanımlayamayız.

![Bir kedinin fotoğrafı](../../../../translated_images/photo-cat.8c8e8fb760ffe45725c5b9f6b0d954e9bf114475c01c55adf0303982851b7eae.tr.jpg)

> [Fotoğraf](https://unsplash.com/photos/75715CVEJhI): [Amber Kipp](https://unsplash.com/@sadmax) tarafından Unsplash'tan alınmıştır.

*Zeka* teriminin belirsizliğini görmek için şu soruyu yanıtlamayı deneyin: "Bir kedi zeki midir?" Farklı insanlar bu soruya farklı yanıtlar verme eğilimindedir çünkü bu iddianın doğru olup olmadığını kanıtlayacak evrensel olarak kabul edilmiş bir test yoktur. Ve eğer olduğunu düşünüyorsanız - kedinizi bir IQ testine sokmayı deneyin...

✅ Zekayı nasıl tanımladığınızı bir dakika düşünün. Bir labirenti çözerek yiyeceğe ulaşabilen bir karga zeki midir? Bir çocuk zeki midir?

---

AGI'den bahsederken, gerçekten zeki bir sistem oluşturup oluşturmadığımızı anlamanın bir yoluna ihtiyacımız var. [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing), zekayı tanımlayan bir yöntem olan **[Turing Testi](https://en.wikipedia.org/wiki/Turing_test)**'ni önerdi. Bu test, verilen bir sistemi doğası gereği zeki bir şeyle - gerçek bir insanla - karşılaştırır ve herhangi bir otomatik karşılaştırma bir bilgisayar programı tarafından atlatılabileceği için, bir insan sorgulayıcı kullanırız. Yani, bir insan, metin tabanlı bir diyalogda gerçek bir kişi ile bir bilgisayar sistemi arasındaki farkı ayırt edemezse - sistem zeki kabul edilir.

> St. Petersburg'da geliştirilen [Eugene Goostman](https://en.wikipedia.org/wiki/Eugene_Goostman) adlı bir sohbet robotu, 2014 yılında Turing testini geçmeye yaklaşmıştır. Bunu, zekice bir kişilik hilesi kullanarak başarmıştır. Sohbet robotu, baştan 13 yaşında bir Ukraynalı çocuk olduğunu açıklamış, bu da bilgi eksikliğini ve metindeki bazı tutarsızlıkları açıklamıştır. Bot, 5 dakikalık bir diyalogdan sonra yargıçların %30'unu insan olduğuna ikna etmiştir. Ancak, bu durumun zeki bir sistem oluşturduğumuz anlamına gelmediğini veya bir bilgisayar sisteminin insan sorgulayıcıyı kandırdığını anlamak önemlidir - aslında sistemi değil, botun yaratıcıları insanları kandırmıştır!

✅ Hiç bir sohbet robotunun insan olduğuna inanarak kandırıldınız mı? Sizi nasıl ikna etti?

## Yapay Zekaya Farklı Yaklaşımlar

Bir bilgisayarın insan gibi davranmasını istiyorsak, bir şekilde bilgisayarın içinde düşünme biçimimizi modellememiz gerekir. Dolayısıyla, bir insanı zeki yapan şeyin ne olduğunu anlamaya çalışmamız gerekir.

> Bir makineye zeka programlayabilmek için, kendi karar verme süreçlerimizin nasıl çalıştığını anlamamız gerekir. Biraz kendinizi gözlemlerseniz, bazı süreçlerin bilinçaltında gerçekleştiğini fark edeceksiniz – örneğin, bir kediyi bir köpekten düşünmeden ayırt edebiliriz – oysa bazıları mantık yürütmeyi içerir.

Bu soruna iki olası yaklaşım vardır:

Üstten Aşağı Yaklaşım (Sembolik Akıl Yürütme) | Alttan Yukarı Yaklaşım (Sinir Ağları)
---------------------------------------|-------------------------------------
Üstten aşağı yaklaşım, bir kişinin bir sorunu çözmek için nasıl mantık yürüttüğünü modellemeye çalışır. Bu, bir insandan **bilgi** çıkarılmasını ve bunun bilgisayar tarafından okunabilir bir biçimde temsil edilmesini içerir. Ayrıca, bilgisayar içinde **akıl yürütmeyi** modellemenin bir yolunu geliştirmemiz gerekir. | Alttan yukarı yaklaşım, insan beyninin yapısını, **nöronlar** adı verilen çok sayıda basit birimden oluşan bir yapıyı modellemeye çalışır. Her nöron, girdilerinin ağırlıklı bir ortalaması gibi davranır ve nöronlardan oluşan bir ağı, **eğitim verileri** sağlayarak faydalı problemleri çözmek için eğitebiliriz.

Ayrıca zekaya yönelik bazı diğer olası yaklaşımlar da vardır:

* **Ortaya Çıkan**, **Sinergik** veya **çoklu ajan yaklaşımı**, karmaşık zeki davranışların çok sayıda basit ajanın etkileşimiyle elde edilebileceği gerçeğine dayanır. [Evrimsel sibernetik](https://en.wikipedia.org/wiki/Global_brain#Evolutionary_cybernetics)'e göre, zeka, *metasistem geçişi* sürecinde daha basit, tepkisel davranışlardan *ortaya çıkabilir*.

* **Evrimsel yaklaşım** veya **genetik algoritma**, evrim ilkelerine dayanan bir optimizasyon sürecidir.

Bu yaklaşımları kursun ilerleyen bölümlerinde ele alacağız, ancak şu anda iki ana yöne odaklanacağız: üstten aşağı ve alttan yukarı.

### Üstten Aşağı Yaklaşım

**Üstten aşağı yaklaşımda**, mantık yürütme sürecimizi modellemeye çalışırız. Mantık yürütürken düşüncelerimizi takip edebildiğimiz için, bu süreci resmileştirmeye ve bilgisayarın içine programlamaya çalışabiliriz. Buna **sembolik akıl yürütme** denir.

İnsanlar, karar verme süreçlerini yönlendiren bazı kurallara sahip olma eğilimindedir. Örneğin, bir doktor bir hastayı teşhis ederken, kişinin ateşi olduğunu fark edebilir ve bu nedenle vücutta bir iltihaplanma olabileceğini düşünebilir. Bir doktor, belirli bir soruna büyük bir kural seti uygulayarak nihai teşhise ulaşabilir.

Bu yaklaşım büyük ölçüde **bilgi temsili** ve **akıl yürütme**ye dayanır. Bir insan uzmandan bilgi çıkarmak en zor kısım olabilir çünkü bir doktor, çoğu durumda, belirli bir teşhise neden ulaştığını tam olarak bilmeyebilir. Bazen çözüm, açık bir düşünme olmadan kafasında belirir. Bir kişinin fotoğrafından yaşını belirlemek gibi bazı görevler, bilgi manipülasyonuna indirgenemez.

### Alttan Yukarı Yaklaşım

Alternatif olarak, beynimizdeki en basit unsurları – bir nöronu – modellemeye çalışabiliriz. Bilgisayarın içinde bir **yapay sinir ağı** oluşturabilir ve ardından ona örnekler vererek problemleri çözmeyi öğretmeye çalışabiliriz. Bu süreç, yeni doğmuş bir çocuğun çevresini gözlem yaparak öğrenmesine benzer.

✅ Bebeklerin nasıl öğrendiği hakkında biraz araştırma yapın. Bir bebeğin beyninin temel unsurları nelerdir?

> | Ya ML?         |      |
> |--------------|-----------|
> | Verilere dayalı olarak bir problemi çözmeyi öğrenen bilgisayarların oluşturduğu Yapay Zeka dalına **Makine Öğrenimi** denir. Bu kursta klasik makine öğrenimini ele almayacağız - sizi ayrı bir [Makine Öğrenimi için Başlangıç](http://aka.ms/ml-beginners) müfredatına yönlendiriyoruz. |   ![Başlangıç için ML](../../../../translated_images/ml-for-beginners.9e4fed176fd5817d7d1f7d358302515186579cbf09b2a6c5bd8092b345da7f22.tr.png)    |

## Yapay Zekanın Kısa Tarihi

Yapay Zeka, yirminci yüzyılın ortalarında bir alan olarak başladı. Başlangıçta, sembolik akıl yürütme yaygın bir yaklaşımdı ve uzman sistemler gibi bazı önemli başarılara yol açtı – sınırlı problem alanlarında uzman gibi davranabilen bilgisayar programları. Ancak, bu yaklaşımın iyi ölçeklenmediği kısa sürede anlaşıldı. Bir uzmandan bilgi çıkarmak, bunu bir bilgisayarda temsil etmek ve bu bilgi tabanını doğru tutmak çok karmaşık ve birçok durumda pratik olmayan bir görev olduğu ortaya çıktı. Bu durum, 1970'lerde [AI Kışı](https://en.wikipedia.org/wiki/AI_winter) olarak adlandırılan döneme yol açtı.

> Görsel Dmitry Soshnikov tarafından, [fotoğraf](https://unsplash.com/photos/r8LmVbUKgns) [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto) tarafından, Unsplash

## Son Dönem AI Araştırmaları

Sinir ağı araştırmalarındaki büyük büyüme, 2010 civarında, büyük halka açık veri setlerinin erişilebilir hale gelmesiyle başladı. Yaklaşık 14 milyon açıklamalı görüntü içeren [ImageNet](https://en.wikipedia.org/wiki/ImageNet) adlı büyük bir görüntü koleksiyonu, [ImageNet Büyük Ölçekli Görsel Tanıma Yarışması](https://image-net.org/challenges/LSVRC/) doğurdu.

![ILSVRC Doğruluk](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Görsel [Dmitry Soshnikov](http://soshnikov.com) tarafından

2012 yılında, [Convolutional Neural Networks](../4-ComputerVision/07-ConvNets/README.md) ilk kez görüntü sınıflandırmada kullanıldı ve sınıflandırma hatalarında önemli bir düşüşe yol açtı (neredeyse %30'dan %16.4'e). 2015 yılında, Microsoft Research'ten ResNet mimarisi [insan seviyesinde doğruluk](https://doi.org/10.1109/ICCV.2015.123) elde etti.

O zamandan beri, Sinir Ağları birçok görevde çok başarılı bir performans sergiledi:

---

Yıl | İnsan Seviyesinde Başarı
-----|--------
2015 | [Görüntü Sınıflandırma](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Konuşma Tanıma](https://arxiv.org/abs/1610.05256)
2018 | [Otomatik Makine Çevirisi](https://arxiv.org/abs/1803.05567) (Çince'den İngilizce'ye)
2020 | [Görüntü Açıklama](https://arxiv.org/abs/2009.13682)

Son birkaç yılda, BERT ve GPT-3 gibi büyük dil modelleriyle büyük başarılar gördük. Bu, büyük ölçüde genel metin verilerinin bol miktarda bulunması sayesinde gerçekleşti. Bu veriler, modellerin metinlerin yapısını ve anlamını yakalamasını, genel metin koleksiyonlarında önceden eğitilmesini ve ardından bu modellerin daha spesifik görevler için uzmanlaşmasını sağladı. Bu kursun ilerleyen bölümlerinde [Doğal Dil İşleme](../5-NLP/README.md) hakkında daha fazla bilgi edineceğiz.

## 🚀 Meydan Okuma

İnternette bir tur yaparak, AI'nin en etkili şekilde nerede kullanıldığını belirleyin. Bir haritalama uygulamasında mı, bir konuşmadan metne hizmette mi yoksa bir video oyununda mı? Sistemin nasıl inşa edildiğini araştırın.

## [Ders sonrası test](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Gözden Geçirme ve Kendi Kendine Çalışma

AI ve ML tarihini gözden geçirmek için [bu dersi](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML) okuyun. Bu dersin veya yukarıdaki dersin başındaki sketchnote'dan bir öğe seçin ve onun evrimini şekillendiren kültürel bağlamı daha iyi anlamak için daha derinlemesine araştırın.

**Ödev**: [Game Jam](assignment.md)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.