<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7d097f7fda9166ead615e4c34552381b",
  "translation_date": "2025-09-23T08:41:38+00:00",
  "source_file": "lessons/2-Symbolic/README.md",
  "language_code": "tr"
}
-->
# Bilgi Temsili ve Uzman Sistemler

![Sembolik AI içeriği özeti](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.tr.png)

> Sketchnote: [Tomomi Imura](https://twitter.com/girlie_mac)

Yapay zeka arayışı, dünyayı insanlara benzer şekilde anlamlandırmak için bilgi arayışına dayanır. Peki bunu nasıl gerçekleştirebilirsiniz?

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ai/quiz/3)

Yapay zekanın ilk günlerinde, zeki sistemler oluşturmak için yukarıdan aşağıya yaklaşım (önceki derste tartışıldı) popülerdi. Fikir, insanlardan bilgiyi makine tarafından okunabilir bir forma çıkarmak ve ardından bunu otomatik olarak problem çözmek için kullanmaktı. Bu yaklaşım iki büyük fikre dayanıyordu:

* Bilgi Temsili
* Akıl Yürütme

## Bilgi Temsili

Sembolik AI'deki önemli kavramlardan biri **bilgi**dir. Bilgiyi *bilgi* veya *veri*den ayırmak önemlidir. Örneğin, kitapların bilgi içerdiğini söyleyebiliriz, çünkü kitapları inceleyerek uzmanlaşabiliriz. Ancak, kitapların içerdiği şey aslında *veri* olarak adlandırılır ve kitapları okuyarak bu veriyi dünya modelimize entegre ettiğimizde bu veriyi bilgiye dönüştürürüz.

> ✅ **Bilgi**, kafamızda bulunan ve dünyayı anlama şeklimizi temsil eden bir şeydir. Aktif bir **öğrenme** süreciyle elde edilir ve aldığımız bilgileri aktif dünya modelimize entegre eder.

Çoğu zaman bilgiyi kesin olarak tanımlamayız, ancak onu diğer ilgili kavramlarla [DIKW Piramidi](https://en.wikipedia.org/wiki/DIKW_pyramid) kullanarak hizalarız. Bu piramit şu kavramları içerir:

* **Veri**, fiziksel medyada temsil edilen bir şeydir, örneğin yazılı metin veya konuşulan kelimeler. Veri, insanlardan bağımsız olarak var olur ve insanlar arasında aktarılabilir.
* **Bilgi**, veriyi kafamızda nasıl yorumladığımızdır. Örneğin, *bilgisayar* kelimesini duyduğumuzda, onun ne olduğunu anlamaya başlarız.
* **Bilgi**, bilginin dünya modelimize entegre edilmesidir. Örneğin, bir bilgisayarın ne olduğunu öğrendiğimizde, nasıl çalıştığı, maliyeti ve ne için kullanılabileceği hakkında fikirler ediniriz. Bu birbirine bağlı kavramlar ağı, bilgimizi oluşturur.
* **Bilgelik**, dünyayı anlamamızın bir başka seviyesidir ve *meta-bilgi*yi temsil eder, örneğin bilginin nasıl ve ne zaman kullanılacağına dair bir kavrayış.

<img src="images/DIKW_Pyramid.png" width="30%"/>

*Resim [Wikipedia'dan](https://commons.wikimedia.org/w/index.php?curid=37705247), By Longlivetheux - Own work, CC BY-SA 4.0*

Bu nedenle, **bilgi temsili** problemi, bilgiyi bir bilgisayar içinde veri şeklinde etkili bir şekilde temsil etmenin bir yolunu bulmaktır, böylece otomatik olarak kullanılabilir hale gelir. Bu bir spektrum olarak görülebilir:

![Bilgi temsili spektrumu](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.tr.png)

> Resim: [Dmitry Soshnikov](http://soshnikov.com)

* Sol tarafta, bilgisayarlar tarafından etkili bir şekilde kullanılabilecek çok basit bilgi temsilleri vardır. En basit olanı algoritmik temsildir, bilgi bir bilgisayar programı ile temsil edilir. Ancak bu, bilginin temsil edilmesi için en iyi yol değildir, çünkü esnek değildir. Kafamızdaki bilgi genellikle algoritmik değildir.
* Sağ tarafta, doğal metin gibi temsiller vardır. Bu en güçlü olanıdır, ancak otomatik akıl yürütme için kullanılamaz.

> ✅ Bilgiyi kafanızda nasıl temsil ettiğinizi ve bunu notlara nasıl dönüştürdüğünüzü bir dakika düşünün. Hatırlamayı kolaylaştıran belirli bir format var mı?

## Bilgisayar Bilgi Temsillerini Sınıflandırma

Bilgisayar bilgi temsili yöntemlerini şu kategorilerde sınıflandırabiliriz:

* **Ağ temsilleri**, kafamızda birbirine bağlı kavramlar ağı olduğu gerçeğine dayanır. Aynı ağları bir bilgisayar içinde bir grafik olarak yeniden oluşturabiliriz - **anlamsal ağ** olarak adlandırılır.

1. **Nesne-Özellik-Değer üçlüleri** veya **özellik-değer çiftleri**. Bir grafik, bir bilgisayar içinde düğüm ve kenarların bir listesi olarak temsil edilebildiğinden, bir anlamsal ağı nesneler, özellikler ve değerler içeren bir üçlü listesiyle temsil edebiliriz. Örneğin, programlama dilleri hakkında şu üçlüleri oluşturabiliriz:

Nesne | Özellik | Değer
-------|-----------|------
Python | is | Türsüz Dil
Python | invented-by | Guido van Rossum
Python | block-syntax | girinti
Türsüz Dil | doesn't have | tür tanımları

> ✅ Üçlülerin diğer bilgi türlerini temsil etmek için nasıl kullanılabileceğini düşünün.

2. **Hiyerarşik temsiller**, kafamızda genellikle nesnelerin bir hiyerarşisini oluşturduğumuz gerçeğini vurgular. Örneğin, kanaryanın bir kuş olduğunu ve tüm kuşların kanatları olduğunu biliriz. Ayrıca kanaryanın genellikle ne renk olduğu ve uçuş hızının ne olduğu hakkında bir fikrimiz vardır.

   - **Çerçeve temsili**, her nesneyi veya nesne sınıfını **çerçeve** olarak temsil etmeye dayanır ve bu çerçeve **yuvalar** içerir. Yuvalar, olası varsayılan değerler, değer kısıtlamaları veya bir yuvanın değerini elde etmek için çağrılabilecek saklı prosedürler içerebilir. Tüm çerçeveler, nesne yönelimli programlama dillerindeki nesne hiyerarşisine benzer bir hiyerarşi oluşturur.
   - **Senaryolar**, zaman içinde gelişebilecek karmaşık durumları temsil eden özel türde çerçevelerdir.

**Python**

Yuva | Değer | Varsayılan Değer | Aralık |
-----|-------|------------------|--------|
Ad | Python | | |
Is-A | Türsüz Dil | | |
Değişken Durumu | | CamelCase | |
Program Uzunluğu | | | 5-5000 satır |
Blok Sözdizimi | Girinti | | |

3. **Prosedürel temsiller**, belirli bir koşul meydana geldiğinde yürütülebilecek bir eylem listesiyle bilgiyi temsil etmeye dayanır.
   - Üretim kuralları, sonuç çıkarmamıza olanak tanıyan if-then ifadeleridir. Örneğin, bir doktorun **EĞER** bir hastanın yüksek ateşi **VEYA** kan testinde yüksek C-reaktif protein seviyesi varsa **O ZAMAN** iltihaplanması olduğu şeklinde bir kuralı olabilir. Koşullardan birini karşılaştığımızda, iltihaplanma hakkında bir sonuca varabiliriz ve ardından bunu daha ileri akıl yürütmede kullanabiliriz.
   - Algoritmalar, prosedürel temsillerin başka bir biçimi olarak kabul edilebilir, ancak bilgi tabanlı sistemlerde neredeyse hiç doğrudan kullanılmazlar.

4. **Mantık**, evrensel insan bilgisini temsil etmenin bir yolu olarak ilk kez Aristoteles tarafından önerilmiştir.
   - Mantıksal Mantık, matematiksel bir teori olarak çok zengin olduğu için hesaplanabilir değildir, bu nedenle genellikle Prolog'da kullanılan Horn cümleleri gibi bir alt kümesi kullanılır.
   - Tanımlayıcı Mantık, *anlamsal web* gibi nesne hiyerarşilerini ve dağıtılmış bilgi temsillerini temsil etmek ve akıl yürütmek için kullanılan mantıksal sistemler ailesidir.

## Uzman Sistemler

Sembolik AI'nın erken başarılarından biri, **uzman sistemler** olarak adlandırılan sistemlerdi - belirli bir problem alanında uzman gibi davranmak üzere tasarlanmış bilgisayar sistemleri. Bu sistemler, bir veya daha fazla insan uzmandan çıkarılan bir **bilgi tabanı**na dayanıyordu ve bunun üzerinde akıl yürütme yapan bir **çıkarım motoru** içeriyordu.

![İnsan Mimarisi](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.tr.png) | ![Bilgi Tabanlı Sistem](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.tr.png)
---------------------------------------------|------------------------------------------------
İnsan sinir sisteminin basitleştirilmiş yapısı | Bilgi tabanlı sistemin mimarisi

Uzman sistemler, insan akıl yürütme sistemine benzer şekilde inşa edilir, bu sistem **kısa süreli hafıza** ve **uzun süreli hafıza** içerir. Benzer şekilde, bilgi tabanlı sistemlerde şu bileşenleri ayırt ederiz:

* **Problem hafızası**: Şu anda çözülmekte olan problemle ilgili bilgileri içerir, örneğin bir hastanın sıcaklığı veya kan basıncı, iltihaplanma olup olmadığı vb. Bu bilgiye **statik bilgi** de denir, çünkü şu anda problem hakkında bildiklerimizin bir anlık görüntüsünü içerir - *problem durumu* olarak adlandırılır.
* **Bilgi tabanı**: Bir problem alanı hakkında uzun süreli bilgiyi temsil eder. İnsan uzmanlardan manuel olarak çıkarılır ve danışmadan danışmaya değişmez. Çünkü bir problem durumundan diğerine geçiş yapmamıza olanak tanır, aynı zamanda **dinamik bilgi** olarak da adlandırılır.
* **Çıkarım motoru**: Problem durumu alanında arama sürecini yönlendirir, gerektiğinde kullanıcıya sorular sorar. Ayrıca her duruma uygulanacak doğru kuralları bulmaktan sorumludur.

Örneğin, fiziksel özelliklere dayanarak bir hayvanı belirleyen bir uzman sistemini ele alalım:

![AND-OR Ağacı](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.tr.png)

> Resim: [Dmitry Soshnikov](http://soshnikov.com)

Bu diyagram **AND-OR ağacı** olarak adlandırılır ve üretim kurallarının grafiksel bir temsilidir. Uzmandan bilgi çıkarma sürecinin başında bir ağaç çizmek faydalıdır. Bilgiyi bilgisayar içinde temsil etmek için kuralları kullanmak daha uygundur:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Her kuralın sol tarafındaki koşul ve eylemin aslında nesne-özellik-değer (OÖD) üçlüleri olduğunu fark edebilirsiniz. **Çalışma hafızası**, şu anda çözülmekte olan problemle ilgili OÖD üçlülerini içerir. **Kural motoru**, bir koşulun karşılandığı kuralları arar ve bunları uygular, çalışma hafızasına başka bir üçlü ekler.

> ✅ Hoşunuza giden bir konuda kendi AND-OR ağacınızı çizin!

### İleri ve Geri Çıkarım

Yukarıda açıklanan süreç **ileri çıkarım** olarak adlandırılır. Çalışma hafızasında problemle ilgili bazı başlangıç verileriyle başlar ve ardından şu akıl yürütme döngüsünü uygular:

1. Hedef özellik çalışma hafızasında mevcutsa - dur ve sonucu ver
2. Şu anda koşulu karşılanan tüm kuralları ara - **çatışma kümesi** elde et.
3. **Çatışma çözümü** yap - bu adımda uygulanacak bir kural seç. Farklı çatışma çözüm stratejileri olabilir:
   - Bilgi tabanındaki ilk uygulanabilir kuralı seç
   - Rastgele bir kural seç
   - *Daha spesifik* bir kural seç, yani "sol taraf"ta (LHS) en çok koşulu karşılayan kuralı seç
4. Seçilen kuralı uygula ve problem durumuna yeni bir bilgi parçası ekle
5. 1. adımdan tekrar et.

Ancak, bazı durumlarda problem hakkında hiçbir bilgiye sahip olmadan başlayabilir ve bizi sonuca ulaştıracak sorular sorabiliriz. Örneğin, tıbbi teşhis yaparken, hastayı teşhis etmeye başlamadan önce tüm tıbbi analizleri önceden yapmayız. Bunun yerine, bir karar verilmesi gerektiğinde analiz yapmak isteriz.

Bu süreç **geri çıkarım** kullanılarak modellenebilir. **Hedef** tarafından yönlendirilir - aradığımız hedef değeri:

1. Hedefin değerini verebilecek tüm kuralları seç (yani hedef sağ tarafta (RHS) olan kurallar) - bir çatışma kümesi
1. Bu özellik için hiçbir kural yoksa veya kullanıcıdan değeri sormamız gerektiğini söyleyen bir kural varsa - kullanıcıya sor, aksi takdirde:
1. Çatışma çözüm stratejisini kullanarak *hipotez* olarak kullanacağımız bir kural seç - bunu kanıtlamaya çalışacağız
1. Süreci, kuralın sol tarafındaki (LHS) tüm özellikler için tekrarlayarak onları hedef olarak kanıtlamaya çalış
1. Süreç herhangi bir noktada başarısız olursa - 3. adımda başka bir kural kullan.

> ✅ İleri çıkarımın daha uygun olduğu durumlar nelerdir? Peki ya geri çıkarım?

### Uzman Sistemleri Uygulama

Uzman sistemler farklı araçlar kullanılarak uygulanabilir:

* Yüksek seviyeli bir programlama dilinde doğrudan programlama. Bu en iyi fikir değildir, çünkü bilgi tabanlı bir sistemin ana avantajı, bilginin çıkarımdan ayrılmasıdır ve potansiyel olarak bir problem alanı uzmanı, çıkarım sürecinin ayrıntılarını anlamadan kurallar yazabilmelidir.
* **Uzman sistem kabuğu** kullanmak, yani bilgi temsili dili kullanarak bilgiyle doldurulmak üzere özel olarak tasarlanmış bir sistem.

## ✍️ Egzersiz: Hayvan Çıkarımı

İleri ve geri çıkarım uzman sistemini uygulama örneği için [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) dosyasına bakın.

> **Not**: Bu örnek oldukça basittir ve bir uzman sisteminin nasıl göründüğüne dair bir fikir verir. Böyle bir sistem oluşturmaya başladığınızda, yalnızca belirli bir kural sayısına ulaştığınızda, yaklaşık 200+ kural, sistemin *zeki* davranışını fark etmeye başlarsınız. Bir noktada kurallar, hepsini akılda tutamayacak kadar karmaşık hale gelir ve bu noktada bir sistemin neden belirli kararlar verdiğini merak edebilirsiniz. Ancak, bilgi tabanlı sistemlerin önemli bir özelliği, alınan herhangi bir kararın tam olarak nasıl yapıldığını her zaman *açıklayabilmeniz*dir.

## Ontolojiler ve Anlamsal Web

20. yüzyılın sonunda, bilgi temsili kullanarak internet kaynaklarını açıklamak için bir girişim vardı, böylece çok spesifik sorgulara karşılık gelen kaynakları bulmak mümkün olabilirdi. Bu hareket **Anlamsal Web** olarak adlandırıldı ve birkaç kavrama dayanıyordu:

- **[Tanımlayıcı mantıklar](https://en.wikipedia.org/wiki/Description_logic)** (DL) üzerine kurulu özel bir bilgi temsili. Çerçeve bilgi temsiline benzer, çünkü nesnelerin özellikleriyle bir hiyerarşi oluşturur, ancak resmi mantıksal semantiği ve çıkarımı vardır. DL'lerin bir ailesi vardır ve ifade gücü ile çıkarımın algoritmik karmaşıklığı arasında denge kurar.
- Tüm kavramların küresel bir URI tanımlayıcı ile temsil edildiği, interneti kapsayan bilgi hiyerarşileri oluşturmayı mümkün kılan dağıtılmış bilgi temsili.
- Bilgi tanımlama için XML tabanlı bir dil ailesi: RDF (Kaynak Tanımlama Çerçevesi), RDFS (RDF Şeması), OWL (Ontoloji Web Dili).

Semantik Web'in temel kavramlarından biri **Ontoloji** kavramıdır. Bu, bir problem alanını açık bir şekilde tanımlamak için bazı resmi bilgi temsilleri kullanılarak yapılan bir spesifikasyona işaret eder. En basit ontoloji, bir problem alanındaki nesnelerin bir hiyerarşisi olabilir, ancak daha karmaşık ontolojiler çıkarım yapmak için kullanılabilecek kuralları içerir.

Semantik webde, tüm temsiller üçlüler üzerine kuruludur. Her nesne ve her ilişki URI ile benzersiz şekilde tanımlanır. Örneğin, bu AI Müfredatının Dmitry Soshnikov tarafından 1 Ocak 2022'de geliştirildiğini ifade etmek istersek, kullanabileceğimiz üçlüler şunlardır:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Burada `http://www.example.com/terms/creation-date` ve `http://purl.org/dc/elements/1.1/creator` *yaratıcı* ve *oluşturma tarihi* kavramlarını ifade etmek için kullanılan, iyi bilinen ve evrensel olarak kabul edilen URI'lardır.

Daha karmaşık bir durumda, bir yaratıcılar listesini tanımlamak istersek, RDF'de tanımlanan bazı veri yapılarını kullanabiliriz.

<img src="images/triplet-complex.png" width="40%"/>

> Yukarıdaki diyagramlar [Dmitry Soshnikov](http://soshnikov.com) tarafından hazırlanmıştır.

Semantik Web'in geliştirilmesi, arama motorlarının ve metinden yapılandırılmış veri çıkarılmasını sağlayan doğal dil işleme tekniklerinin başarısı nedeniyle bir ölçüde yavaşladı. Ancak, bazı alanlarda ontolojileri ve bilgi tabanlarını korumak için hala önemli çabalar gösterilmektedir. Dikkate değer birkaç proje:

* [WikiData](https://wikidata.org/) Wikipedia ile ilişkili makine tarafından okunabilir bilgi tabanlarının bir koleksiyonudur. Verilerin çoğu, Wikipedia sayfalarındaki yapılandırılmış içerik parçaları olan *InfoBox*lardan çıkarılır. WikiData'yı Semantik Web için özel bir sorgu dili olan SPARQL ile [sorgulayabilirsiniz](https://query.wikidata.org/). İşte insanların en popüler göz renklerini gösteren örnek bir sorgu:

```sparql
#defaultView:BubbleChart
SELECT ?eyeColorLabel (COUNT(?human) AS ?count)
WHERE
{
  ?human wdt:P31 wd:Q5.       # human instance-of homo sapiens
  ?human wdt:P1340 ?eyeColor. # human eye-color ?eyeColor
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?eyeColorLabel
```

* [DBpedia](https://www.dbpedia.org/) WikiData'ya benzer başka bir girişimdir.

> ✅ Kendi ontolojilerinizi oluşturmayı veya mevcut olanları açmayı denemek isterseniz, [Protégé](https://protege.stanford.edu/) adlı harika bir görsel ontoloji düzenleyici var. İndirin veya çevrimiçi kullanın.

<img src="images/protege.png" width="70%"/>

*Web Protégé düzenleyicisi Romanov Ailesi ontolojisi ile açık. Dmitry Soshnikov tarafından ekran görüntüsü.*

## ✍️ Alıştırma: Bir Aile Ontolojisi

Semantik Web tekniklerini kullanarak aile ilişkileri hakkında akıl yürütme örneği için [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) dosyasına bakın. Yaygın GEDCOM formatında temsil edilen bir aile ağacını ve aile ilişkileri ontolojisini alacağız ve belirli bir bireyler grubu için tüm aile ilişkilerinin bir grafiğini oluşturacağız.

## Microsoft Concept Graph

Çoğu durumda, ontolojiler dikkatlice elle oluşturulur. Ancak, ontolojileri yapılandırılmamış verilerden, örneğin doğal dil metinlerinden **çıkarmak** da mümkündür.

Microsoft Research tarafından yapılan böyle bir girişim, [Microsoft Concept Graph](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste) ile sonuçlandı.

Bu, `is-a` kalıtım ilişkisi kullanılarak bir araya getirilen büyük bir varlık koleksiyonudur. "Microsoft nedir?" gibi soruları yanıtlamayı sağlar - cevap, "bir şirket (olasılık 0.87) ve bir marka (olasılık 0.75)" gibi bir şey olabilir.

Grafik, REST API olarak veya tüm varlık çiftlerini listeleyen büyük bir indirilebilir metin dosyası olarak kullanılabilir.

## ✍️ Alıştırma: Bir Kavram Grafiği

Microsoft Concept Graph'ı kullanarak haber makalelerini birkaç kategoriye ayırmayı görmek için [MSConceptGraph.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb) defterini deneyin.

## Sonuç

Günümüzde, yapay zeka genellikle *Makine Öğrenimi* veya *Sinir Ağları* ile eş anlamlı olarak kabul edilir. Ancak, bir insan aynı zamanda açık bir şekilde akıl yürütme sergiler, bu da şu anda sinir ağları tarafından ele alınmayan bir şeydir. Gerçek dünya projelerinde, açık akıl yürütme, açıklama gerektiren veya sistemin davranışını kontrollü bir şekilde değiştirme yeteneği gerektiren görevleri gerçekleştirmek için hala kullanılmaktadır.

## 🚀 Meydan Okuma

Bu derse bağlı Aile Ontolojisi defterinde, diğer aile ilişkileriyle denemeler yapma fırsatı vardır. Aile ağacındaki insanlar arasında yeni bağlantılar keşfetmeyi deneyin.

## [Ders sonrası test](https://ff-quizzes.netlify.app/en/ai/quiz/4)

## Gözden Geçirme ve Kendi Kendine Çalışma

İnsanların bilgiyi nicelleştirmeye ve kodlamaya çalıştığı alanları keşfetmek için internette araştırma yapın. Bloom'un Taksonomisine göz atın ve insanların dünyalarını anlamlandırmaya çalıştığı tarihsel süreçlere geri dönün. Linnaeus'un organizmalar için bir taksonomi oluşturma çalışmalarını inceleyin ve Dmitri Mendeleev'in kimyasal elementlerin tanımlanması ve gruplandırılması için bir yol yaratma biçimini gözlemleyin. Başka hangi ilginç örnekler bulabilirsiniz?

**Ödev**: [Bir Ontoloji Oluşturun](assignment.md)

---

