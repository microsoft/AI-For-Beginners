<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "98c5222ff9556b55223fed2337145e18",
  "translation_date": "2025-08-26T07:38:21+00:00",
  "source_file": "lessons/2-Symbolic/README.md",
  "language_code": "tr"
}
-->
# Bilgi Temsili ve Uzman Sistemler

![Sembolik AI içeriğinin özeti](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.tr.png)

> Sketchnote: [Tomomi Imura](https://twitter.com/girlie_mac)

Yapay zeka arayışı, dünyayı insanların yaptığı gibi anlamlandırmak için bilgi arayışına dayanır. Peki, bunu nasıl gerçekleştirebilirsiniz?

## [Ders Öncesi Test](https://ff-quizzes.netlify.app/en/ai/quiz/3)

Yapay zekanın ilk zamanlarında, zeki sistemler oluşturmak için yukarıdan aşağıya yaklaşım (önceki derste tartışılmıştı) popülerdi. Fikir, insanlardan bilgiyi alıp makine tarafından okunabilir bir forma dönüştürmek ve ardından bu bilgiyi otomatik olarak problem çözmek için kullanmaktı. Bu yaklaşım iki büyük fikre dayanıyordu:

* Bilgi Temsili
* Akıl Yürütme

## Bilgi Temsili

Sembolik AI'deki önemli kavramlardan biri **bilgi**dir. Bilgiyi *bilgi* ya da *veri*den ayırmak önemlidir. Örneğin, kitapların bilgi içerdiğini söyleyebiliriz çünkü kitapları okuyarak uzmanlaşabiliriz. Ancak, kitapların içerdiği şey aslında *veri*dir ve kitapları okuyarak ve bu veriyi dünya modelimize entegre ederek bu veriyi bilgiye dönüştürürüz.

> ✅ **Bilgi**, kafamızda bulunan ve dünyayı anlama şeklimizi temsil eden bir şeydir. Bu, aldığımız bilgi parçalarını aktif dünya modelimize entegre eden aktif bir **öğrenme** süreciyle elde edilir.

Çoğu zaman bilgiyi kesin olarak tanımlamayız, ancak onu diğer ilgili kavramlarla [DIKW Piramidi](https://en.wikipedia.org/wiki/DIKW_pyramid) kullanarak hizalarız. Bu piramit şu kavramları içerir:

* **Veri**, yazılı metin veya konuşulan kelimeler gibi fiziksel bir ortamda temsil edilen bir şeydir. Veri, insanlardan bağımsız olarak var olur ve insanlar arasında aktarılabilir.
* **Bilgi**, veriyi kafamızda nasıl yorumladığımızdır. Örneğin, *bilgisayar* kelimesini duyduğumuzda, onun ne olduğunu anlarız.
* **Bilgi**, bilginin dünya modelimize entegre edilmesidir. Örneğin, bir bilgisayarın ne olduğunu öğrendiğimizde, onun nasıl çalıştığı, ne kadar maliyeti olduğu ve ne için kullanılabileceği hakkında bazı fikirler ediniriz. Bu birbiriyle ilişkili kavramlar ağı, bilgimizi oluşturur.
* **Bilgelik**, dünyayı anlama seviyemizin bir üst seviyesidir ve *meta-bilgi*yi temsil eder, örneğin bilginin nasıl ve ne zaman kullanılacağına dair bir kavrayış.

*Image [from Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), By Longlivetheux - Own work, CC BY-SA 4.0*

Dolayısıyla, **bilgi temsili** problemi, bilgiyi bilgisayar içinde veri biçiminde etkili bir şekilde temsil etmenin bir yolunu bulmaktır, böylece otomatik olarak kullanılabilir hale gelir. Bu, bir spektrum olarak görülebilir:

![Bilgi temsili spektrumu](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.tr.png)

> Görsel: [Dmitry Soshnikov](http://soshnikov.com)

* Solda, bilgisayarlar tarafından etkili bir şekilde kullanılabilecek çok basit bilgi temsilleri vardır. En basiti algoritmik olanıdır; bilgi bir bilgisayar programı ile temsil edilir. Ancak, bu bilgi temsili için en iyi yol değildir çünkü esnek değildir. Kafamızdaki bilgi genellikle algoritmik değildir.
* Sağda, doğal metin gibi temsiller vardır. Bu en güçlü olanıdır, ancak otomatik akıl yürütme için kullanılamaz.

> ✅ Bilgiyi kafanızda nasıl temsil ettiğinizi ve bunu notlara nasıl dönüştürdüğünüzü bir dakika düşünün. Bilgiyi daha iyi hatırlamanıza yardımcı olan belirli bir format var mı?

## Bilgisayar Bilgi Temsillerini Sınıflandırma

Bilgisayar bilgi temsili yöntemlerini şu kategorilerde sınıflandırabiliriz:

* **Ağ temsilleri**, kafamızda birbiriyle ilişkili kavramların bir ağı olduğu gerçeğine dayanır. Aynı ağları bir bilgisayar içinde bir grafik olarak yeniden oluşturabiliriz - bu, **anlamsal ağ** olarak adlandırılır.

1. **Nesne-Özellik-Değer üçlüleri** veya **özellik-değer çiftleri**. Bir grafik, bilgisayar içinde bir düğüm ve kenar listesi olarak temsil edilebildiğinden, bir anlamsal ağı nesneler, özellikler ve değerler içeren bir üçlü listesiyle temsil edebiliriz. Örneğin, programlama dilleri hakkında şu üçlüleri oluşturabiliriz:

Nesne | Özellik | Değer
-------|-----------|------
Python | is | Türsüz Dil
Python | invented-by | Guido van Rossum
Python | blok-syntax | girinti
Türsüz Dil | doesn't have | tür tanımları

> ✅ Üçlülerin diğer bilgi türlerini temsil etmek için nasıl kullanılabileceğini düşünün.

2. **Hiyerarşik temsiller**, kafamızda genellikle nesnelerin bir hiyerarşisini oluşturduğumuzu vurgular. Örneğin, kanaryanın bir kuş olduğunu ve tüm kuşların kanatları olduğunu biliriz. Ayrıca, kanaryanın genellikle ne renk olduğu ve uçuş hızları hakkında bir fikrimiz vardır.

   - **Çerçeve temsili**, her nesneyi veya nesne sınıfını **çerçeve** olarak temsil etmeye dayanır ve bu çerçeve **yuvalar** içerir. Yuvalar, olası varsayılan değerlere, değer kısıtlamalarına veya bir yuvanın değerini elde etmek için çağrılabilecek saklı prosedürlere sahip olabilir. Tüm çerçeveler, nesne yönelimli programlama dillerindeki nesne hiyerarşisine benzer bir hiyerarşi oluşturur.
   - **Senaryolar**, zaman içinde gelişebilecek karmaşık durumları temsil eden özel bir çerçeve türüdür.

**Python**

Yuva | Değer | Varsayılan Değer | Aralık |
-----|-------|------------------|--------|
Ad | Python | | |
Is-A | Türsüz Dil | | |
Değişken Durumu | | CamelCase | |
Program Uzunluğu | | | 5-5000 satır |
Blok Sözdizimi | Girinti | | |

3. **Prosedürel temsiller**, belirli bir koşul oluştuğunda yürütülebilecek bir dizi eylemle bilgiyi temsil etmeye dayanır.
   - Üretim kuralları, sonuç çıkarmamıza olanak tanıyan eğer-o zaman ifadeleridir. Örneğin, bir doktorun şu şekilde bir kuralı olabilir: **EĞER** bir hastada yüksek ateş **VEYA** kan testinde yüksek C-reaktif protein seviyesi varsa, **O ZAMAN** iltihaplanması vardır. Koşullardan birini karşılaştığımızda, iltihaplanma hakkında bir sonuca varabiliriz ve ardından bunu daha ileri akıl yürütmede kullanabiliriz.
   - Algoritmalar, prosedürel temsillerin başka bir biçimi olarak kabul edilebilir, ancak bilgi tabanlı sistemlerde neredeyse hiç doğrudan kullanılmazlar.

4. **Mantık**, evrensel insan bilgisini temsil etmenin bir yolu olarak Aristoteles tarafından önerilmiştir.
   - Önerme Mantığı, matematiksel bir teori olarak hesaplanabilir olmayacak kadar zengindir, bu nedenle genellikle Prolog'da kullanılan Horn cümleleri gibi bir alt kümesi kullanılır.
   - Tanımlayıcı Mantık, *anlamsal web* gibi dağıtılmış bilgi temsilleri ve nesne hiyerarşilerini temsil etmek ve bunlar üzerinde akıl yürütmek için kullanılan mantıksal sistemler ailesidir.

## Uzman Sistemler

Sembolik AI'nın erken başarılarından biri, belirli bir problem alanında uzman gibi davranmak üzere tasarlanmış **uzman sistemler**di. Bu sistemler, bir veya daha fazla insan uzmandan çıkarılan bir **bilgi tabanı**na dayanıyordu ve bunun üzerinde bazı akıl yürütmeler gerçekleştiren bir **çıkarım motoru** içeriyordu.

![İnsan Mimarisi](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.tr.png) | ![Bilgi Tabanlı Sistem](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.tr.png)
---------------------------------------------|------------------------------------------------
İnsan sinir sisteminin basitleştirilmiş yapısı | Bilgi tabanlı sistemin mimarisi

Uzman sistemler, insan akıl yürütme sistemine benzer şekilde inşa edilir; bu sistem **kısa süreli hafıza** ve **uzun süreli hafıza** içerir. Benzer şekilde, bilgi tabanlı sistemlerde şu bileşenleri ayırt ederiz:

* **Problem hafızası**: Şu anda çözülmekte olan problem hakkındaki bilgileri içerir, örneğin bir hastanın sıcaklığı veya kan basıncı, iltihaplanması olup olmadığı vb. Bu bilgiye **statik bilgi** de denir çünkü şu anda problem hakkında bildiklerimizin bir anlık görüntüsünü içerir - bu, *problem durumu* olarak adlandırılır.
* **Bilgi tabanı**: Bir problem alanı hakkındaki uzun süreli bilgiyi temsil eder. İnsan uzmanlardan manuel olarak çıkarılır ve danışmadan danışmaya değişmez. Çünkü bir problem durumundan diğerine geçiş yapmamıza olanak tanır, bu nedenle **dinamik bilgi** olarak da adlandırılır.
* **Çıkarım motoru**: Problem durumu alanında arama sürecini yönlendirir, gerektiğinde kullanıcıya sorular sorar. Ayrıca her duruma uygulanacak doğru kuralları bulmaktan da sorumludur.

Örneğin, fiziksel özelliklere dayalı bir hayvanı belirlemek için şu uzman sistemini ele alalım:

![AND-OR Ağacı](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.tr.png)

> Görsel: [Dmitry Soshnikov](http://soshnikov.com)

Bu diyagram bir **AND-OR ağacı** olarak adlandırılır ve bir dizi üretim kuralının grafiksel bir temsilidir. Bir uzmandan bilgi çıkarma sürecinin başında bir ağaç çizmek faydalıdır. Bilgiyi bilgisayar içinde temsil etmek için kuralları kullanmak daha uygundur:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Her kuralın sol tarafındaki koşul ve eylemin aslında nesne-özellik-değer (OÖD) üçlüleri olduğunu fark edebilirsiniz. **Çalışma hafızası**, şu anda çözülmekte olan problemle ilgili OÖD üçlülerini içerir. Bir **kural motoru**, bir koşulun sağlandığı kuralları arar ve bunları uygular, çalışma hafızasına başka bir üçlü ekler.

> ✅ Sevdiğiniz bir konu hakkında kendi AND-OR ağacınızı çizin!

### İleri ve Geri Çıkarım

Yukarıda açıklanan süreç **ileri çıkarım** olarak adlandırılır. Çalışma hafızasında problemle ilgili bazı başlangıç verileriyle başlar ve ardından şu akıl yürütme döngüsünü yürütür:

1. Hedef özellik çalışma hafızasında mevcutsa - dur ve sonucu ver
2. Koşulu şu anda sağlanan tüm kuralları ara - bir **çatışma kümesi** elde et.
3. **Çatışma çözümü** yap - bu adımda yürütülecek bir kural seç. Farklı çatışma çözüm stratejileri olabilir:
   - Bilgi tabanındaki ilk uygulanabilir kuralı seç
   - Rastgele bir kural seç
   - *Daha spesifik* bir kural seç, yani "sol taraf" (LHS) koşullarının çoğunu karşılayan bir kural
4. Seçilen kuralı uygula ve problem durumuna yeni bir bilgi parçası ekle
5. 1. adımdan tekrar et.

Ancak, bazı durumlarda problem hakkında hiçbir bilgiye sahip olmadan başlayabilir ve sonuca ulaşmamıza yardımcı olacak sorular sorabiliriz. Örneğin, tıbbi teşhis yaparken, hastayı teşhis etmeye başlamadan önce tüm tıbbi analizleri önceden yapmayız. Bunun yerine, bir karar verilmesi gerektiğinde analiz yapmak isteriz.

Bu süreç **geri çıkarım** kullanılarak modellenebilir. Bu, aradığımız **hedef** tarafından yönlendirilir - bulmaya çalıştığımız özellik değeri:

1. Bir hedefin değerini verebilecek tüm kuralları seç (örneğin, hedef sağ tarafta (RHS) olan kurallar) - bir çatışma kümesi
1. Bu özellik için hiçbir kural yoksa veya kullanıcıdan değeri sormamız gerektiğini söyleyen bir kural varsa - kullanıcıya sor, aksi takdirde:
1. Çatışma çözüm stratejisini kullanarak *hipotez* olarak kullanacağımız bir kural seç - bunu kanıtlamaya çalışacağız
1. Kuralların sol tarafındaki tüm özellikler için süreci yineleyerek bunları hedef olarak kanıtlamaya çalış
1. Süreç herhangi bir noktada başarısız olursa - 3. adımda başka bir kural kullan.

> ✅ Hangi durumlarda ileri çıkarım daha uygundur? Peki ya geri çıkarım?

### Uzman Sistemleri Uygulama

Uzman sistemleri farklı araçlar kullanılarak uygulanabilir:

* Doğrudan bir yüksek seviyeli programlama dilinde programlamak. Bu en iyi fikir değildir çünkü bilgi tabanlı bir sistemin ana avantajı, bilginin çıkarımdan ayrılmasıdır ve potansiyel olarak bir problem alanı uzmanı, çıkarım sürecinin ayrıntılarını anlamadan kurallar yazabilmelidir.
* **Uzman sistem kabuğu** kullanmak, yani bilgi temsili dili kullanılarak bilgiyle doldurulmak üzere özel olarak tasarlanmış bir sistem.

## ✍️ Egzersiz: Hayvan Çıkarımı

İleri ve geri çıkarım uzman sistemi uygulama örneği için [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) dosyasına bakın.
> **Not**: Bu örnek oldukça basittir ve yalnızca bir uzman sistemin nasıl göründüğüne dair bir fikir verir. Böyle bir sistem oluşturmaya başladığınızda, yalnızca belirli bir kural sayısına, yaklaşık 200+ kurala ulaştığınızda *zeki* bir davranış fark etmeye başlarsınız. Bir noktada, kurallar o kadar karmaşık hale gelir ki, hepsini akılda tutmak zorlaşır ve bu noktada sistemin neden belirli kararlar verdiğini merak etmeye başlayabilirsiniz. Ancak, bilgi tabanlı sistemlerin önemli özelliklerinden biri, alınan herhangi bir kararın tam olarak nasıl verildiğini her zaman *açıklayabilmenizdir*.
## Ontolojiler ve Anlamsal Web

20. yüzyılın sonunda, İnternet kaynaklarını bilgi temsili kullanarak açıklama girişimi ortaya çıktı. Bu sayede, çok spesifik sorgulara karşılık gelen kaynakları bulmak mümkün olacaktı. Bu girişim **Anlamsal Web** olarak adlandırıldı ve birkaç kavrama dayanıyordu:

- **[Tanım mantıkları](https://en.wikipedia.org/wiki/Description_logic)** (DL) temelli özel bir bilgi temsili. Çerçeve bilgi temsiline benzer, çünkü özelliklere sahip nesnelerin bir hiyerarşisini oluşturur, ancak formal mantıksal semantiğe ve çıkarıma sahiptir. Çıkarımın ifade gücü ve algoritmik karmaşıklığı arasında denge kuran bir DL ailesi vardır.
- Dağıtılmış bilgi temsili, tüm kavramların küresel bir URI tanımlayıcısı ile temsil edildiği, interneti kapsayan bilgi hiyerarşileri oluşturmayı mümkün kılan bir yapı.
- Bilgi açıklaması için XML tabanlı bir dil ailesi: RDF (Kaynak Tanım Çerçevesi), RDFS (RDF Şeması), OWL (Ontoloji Web Dili).

Anlamsal Web'in temel kavramı **Ontoloji** kavramıdır. Bu, bir problem alanının formal bir bilgi temsili kullanılarak açık bir şekilde tanımlanmasını ifade eder. En basit ontoloji, bir problem alanındaki nesnelerin bir hiyerarşisi olabilir, ancak daha karmaşık ontolojiler çıkarım için kullanılabilecek kuralları içerir.

Anlamsal webde, tüm temsiller üçlüler üzerine kuruludur. Her nesne ve her ilişki URI ile benzersiz bir şekilde tanımlanır. Örneğin, bu AI Müfredatının Dmitry Soshnikov tarafından 1 Ocak 2022'de geliştirildiği gerçeğini ifade etmek istersek, kullanabileceğimiz üçlüler şunlardır:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Burada `http://www.example.com/terms/creation-date` ve `http://purl.org/dc/elements/1.1/creator` *yaratıcı* ve *oluşturma tarihi* kavramlarını ifade etmek için kullanılan, iyi bilinen ve evrensel olarak kabul edilen URI'lardır.

Daha karmaşık bir durumda, bir yaratıcılar listesini tanımlamak istersek, RDF'de tanımlanan bazı veri yapılarını kullanabiliriz.

<img src="images/triplet-complex.png" width="40%"/>

> Yukarıdaki diyagramlar [Dmitry Soshnikov](http://soshnikov.com) tarafından hazırlanmıştır.

Anlamsal Web'in inşa edilmesindeki ilerleme, arama motorlarının ve metinden yapılandırılmış veri çıkarılmasını sağlayan doğal dil işleme tekniklerinin başarısı nedeniyle bir ölçüde yavaşladı. Ancak, bazı alanlarda ontolojileri ve bilgi tabanlarını sürdürmek için hala önemli çabalar gösterilmektedir. Dikkate değer birkaç proje:

* [WikiData](https://wikidata.org/) Wikipedia ile ilişkili makine tarafından okunabilir bilgi tabanlarının bir koleksiyonudur. Verilerin çoğu, Wikipedia sayfalarındaki yapılandırılmış içerik parçaları olan *InfoBox*lardan çıkarılır. WikiData'yı Anlamsal Web için özel bir sorgu dili olan SPARQL ile [sorgulayabilirsiniz](https://query.wikidata.org/). İşte insanların en popüler göz renklerini gösteren örnek bir sorgu:

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

> ✅ Kendi ontolojilerinizi oluşturmayı veya mevcut olanları açmayı denemek istiyorsanız, [Protégé](https://protege.stanford.edu/) adlı harika bir görsel ontoloji düzenleyici var. İndirin veya çevrimiçi kullanın.

<img src="images/protege.png" width="70%"/>

*Web Protégé düzenleyicisi Romanov Ailesi ontolojisi ile açık. Dmitry Soshnikov tarafından ekran görüntüsü.*

## ✍️ Alıştırma: Bir Aile Ontolojisi

Aile ilişkileri hakkında Anlamsal Web tekniklerini kullanmaya dair bir örnek için [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) dosyasına bakın. Yaygın GEDCOM formatında temsil edilen bir aile ağacını ve aile ilişkileri ontolojisini alacağız ve belirli bireyler için tüm aile ilişkilerinin bir grafiğini oluşturacağız.

## Microsoft Kavram Grafiği

Çoğu durumda, ontolojiler dikkatlice elle oluşturulur. Ancak, ontolojileri yapılandırılmamış verilerden, örneğin doğal dil metinlerinden **çıkarmak** da mümkündür.

Microsoft Research tarafından yapılan böyle bir girişim, [Microsoft Kavram Grafiği](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste) ile sonuçlandı.

Bu, `is-a` kalıtım ilişkisi kullanılarak gruplandırılmış büyük bir varlık koleksiyonudur. "Microsoft nedir?" gibi soruları yanıtlamayı sağlar - yanıt, "bir şirket (olasılık 0.87) ve bir marka (olasılık 0.75)" gibi bir şeydir.

Grafik, REST API olarak veya tüm varlık çiftlerini listeleyen büyük bir indirilebilir metin dosyası olarak kullanılabilir.

## ✍️ Alıştırma: Bir Kavram Grafiği

Microsoft Kavram Grafiği'ni kullanarak haber makalelerini birkaç kategoriye ayırmayı görmek için [MSConceptGraph.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb) defterini deneyin.

## Sonuç

Günümüzde, yapay zeka genellikle *Makine Öğrenimi* veya *Sinir Ağları* ile eş anlamlı olarak kabul edilir. Ancak, bir insan açık bir şekilde akıl yürütme sergiler, bu da şu anda sinir ağları tarafından ele alınmayan bir şeydir. Gerçek dünya projelerinde, açık akıl yürütme, açıklama gerektiren veya sistemin davranışını kontrollü bir şekilde değiştirme yeteneği gerektiren görevleri gerçekleştirmek için hala kullanılmaktadır.

## 🚀 Meydan Okuma

Bu derse bağlı Aile Ontolojisi defterinde, diğer aile ilişkileriyle deneme yapma fırsatı vardır. Aile ağacındaki insanlar arasında yeni bağlantılar keşfetmeyi deneyin.

## [Ders sonrası test](https://ff-quizzes.netlify.app/en/ai/quiz/4)

## İnceleme ve Kendi Kendine Çalışma

İnsanların bilgiyi nicelleştirmeye ve kodlamaya çalıştığı alanları keşfetmek için internette araştırma yapın. Bloom'un Taksonomisine göz atın ve insanların dünyalarını anlamlandırmaya çalıştığı tarihsel süreçlere geri dönün. Linnaeus'un organizmaların taksonomisini oluşturma çalışmalarını ve Dmitri Mendeleev'in kimyasal elementlerin tanımlanması ve gruplandırılması için bir yol yaratma çabalarını inceleyin. Başka hangi ilginç örnekler bulabilirsiniz?

**Ödev**: [Bir Ontoloji Oluşturun](assignment.md)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.