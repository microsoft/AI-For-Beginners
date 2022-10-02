# Bilgi Temsili ve Uzman Sistemler

![Simgesel YZ içerik özeti](../../sketchnotes/ai-symbolic.png)

> Çizim sahibi [Tomomi Imura](https://twitter.com/girlie_mac)

Yapay zeka arayışı, insanların yaptığı gibi dünyayı anlamlandırmak için bilgi aramaya dayanır. Ama bunu yapmak için nasıl bir yol izleyebilirsin?

## [Ders öncesi sınavı](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/102)

YZ'nin ilk günlerinde, akıllı sistemler oluşturmaya yönelik yukarıdan aşağıya yaklaşım (önceki derste tartışılmıştı) popülerdi. Buradaki fikir, insanlardan bilgiyi makine tarafından okunabilen bir forma döndürmek ve sonra bunu problemleri otomatik olarak çözmek için kullanmaktı. Bu yaklaşım iki büyük fikre dayanıyordu:

* Bilgi Temsili
* Akıl Yürütme

## Bilgi Temsili

Simgesel YZ'deki önemli kavramlardan biri **bilgidir**. Bilgiyi *enformasyondan* veya *veriden* ayırt etmek önemlidir. Örneğin, kitapların bilgi içerdiği söylenebilir, çünkü kişi kitaplara çalışabilir ve uzman olabilir. Ancak kitapların içerdiği şeye aslında *veri* denir ve kitap okuyarak ve bu verileri dünya modelimizle bütünleştirerek bilgiye dönüştürürüz.

> ✅ **Bilgi** kafamızın içinde yer alan ve dünyaya ilişkin anlayışımızı temsil eden bir şeydir. Aldığımız enformasyon parçalarını aktif dünya modelimizle bütünleştiren aktif bir **öğrenme** süreci ile elde edilir.

Çoğu zaman bilgiyi kesin olarak tanımlamayız, ancak [DIKW Piramidi](https://en.wikipedia.org/wiki/DIKW_pyramid) kullanarak onu diğer ilgili kavramlarla hizalarız. Aşağıdaki kavramları içerir:

* **Veri**, yazılı metin veya sözlü kelimeler gibi fiziksel ortamda temsil edilen bir şeydir. Veriler insanlardan bağımsız olarak var olur ve insanlar arasında aktarılabilir.
* **Enformasyon** verileri kafamızda nasıl yorumladığımızdır. Örneğin, *bilgisayar* kelimesini duyduğumuzda, onun ne olduğunu biraz anlarız.
* **Bilgi**, dünya modelimizle bütünleşen bilgidir. Örneğin, bir bilgisayarın ne olduğunu öğrendiğimizde nasıl çalıştığı, ne kadara mal olduğu ve ne için kullanılabileceği hakkında bazı fikirler edinmeye başlarız. Bu birbiriyle ilişkili kavramlar ağı bilgimizi oluşturur.
* **Bilgelik** dünyayı anlamamızın bir başka seviyesidir ve *başkalaşım-bilgisini* temsil eder, ör. bilginin nasıl ve ne zaman kullanılması gerektiğine dair biraz kanı.

<img src="../images/DIKW_Pyramid.png" width="30%"/>

*İmge [Wikipedia'dan](https://commons.wikimedia.org/w/index.php?curid=37705247), By Longlivetheux - Own work, CC BY-SA 4.0*

Bu nedenle, **bilgi temsili** sorunu, bilgiyi bir bilgisayar içinde veri biçiminde temsil etmenin, otomatik olarak kullanılabilir hale getirmenin etkili bir yolunu bulmaktır. Bu bir spektrum olarak görülebilir:

![Bilgi temsili spektrumu](../images/knowledge-spectrum.png)

> İmge sahibi [Dmitry Soshnikov](http://soshnikov.com)

* Solda, bilgisayarlar tarafından etkin bir şekilde kullanılabilecek çok basit bilgi temsili türleri vardır. En basit olanı, bilgi bir bilgisayar programı tarafından temsil edildiğinde algoritmiktir. Ancak bu, bilgiyi temsil etmenin en iyi yolu değildir, çünkü esnek değildir. Kafamızın içindeki bilgi genellikle algoritmik değildir.
* Sağda doğal metin gibi temsiller vardır. En güçlüsüdür, ancak otomatik akıl yürütme için kullanılamaz.

> ✅ Bir an için bilgiyi kafanızda nasıl temsil ettiğinizi düşünün ve onu notlara dönüştürün. Akılda tutmaya yardımcı olmada iyi çalışan belirli bir format var mı?

## Bilgisayar Bilgi Temsillerini Sınıflandırma

Farklı bilgisayar bilgisi temsil yöntemlerini aşağıdaki kategorilerde sınıflandırabiliriz:

* **Ağ temsilleri** kafamızın içinde birbiriyle ilişkili kavramlardan oluşan bir ağımız olduğu gerçeğine dayanmaktadır. Aynı ağları bir bilgisayarın içindeki bir çizge olarak yeniden üretmeyi deneyebiliriz - sözde **anlamsal ağ**.

1. **Nesne-Nitelik-Değer üçlüleri** veya **nitelik-değer çiftleri**. Bir öizge bir bilgisayar içinde düğümler ve kenarların bir listesi olarak gösterilebildiğinden, anlamsal bir ağı nesneler, nitelikler ve değerler içeren bir üçlüler listesiyle temsil edebiliriz. Örneğin, programlama dilleriyle ilgili aşağıdaki üçlüleri oluşturuyoruz:

Nesne  | Nitelik   | Değer
-------|-----------|------
Python | olmak | türsüz dil
Python | icat edilmek | Guido van Rossum
Python | blok sözdizimi | girinti
Türsüz dil | sahip olmamak | tür tanımları

> ✅ Diğer bilgi türlerini temsil etmek için üçlülerin nasıl kullanılabileceğini düşünün.

2. **Hiyerarşik temsiller**, genellikle kafamızın içinde bir nesneler hiyerarşisi oluşturduğumuz gerçeğini vurgular. Örneğin, kanarya bir kuştur ve tüm kuşların kanatları vardır. Ayrıca genellikle kanarya renginin ne olduğu ve uçuş hızlarının ne olduğu hakkında da bir fikrimiz var.

   - **Çerçeve temsili**, her bir nesneyi veya nesne sınıfını **yuvalar** içeren bir **çerçeve** olarak temsil etmeye dayanır. Yuvaların, bir yuvanın değerini elde etmek için çağrılabilecek olası varsayılan değerleri, değer kısıtlamaları veya saklı yordamları vardır. Tüm çerçeveler, nesne yönelimli programlama dillerindeki nesne hiyerarşisine benzer bir hiyerarşi oluşturur.
   - **Senaryolar**, zaman içinde ortaya çıkabilecek karmaşık durumları temsil eden özel tür çerçevelerdir.

**Python**
Yuva | Değer | Varsayılan Değer | Aralık |
-----|-------|---------------|----------|
İsim | Python | | |
Örneği Olmak | Türsüz Dil | | |
Değişken Harf Boyutu | | Deve Harf Boyutu (CamelCase) | |
Program Uzunluğu | | | 5-5000 satır |
Blok Sözdizimi | Girinti | | |

3. **Yöntemsel temsiller**, belirli bir koşul oluştuğunda yürütülebilecek bir eylemler listesiyle bilgiyi temsil etmeye dayanır.
   - Üretme kuralları, sonuç çıkarmamıza izin veren eğer-öyleyse ifadelerdir. Örneğin, bir doktorun, kan testinde **EĞER** bir hastanın ateşi yüksek **VEYA** yüksek düzeyde C-reaktif proteini varsa **O ZAMAN** iltihabı olduğunu söyleyen bir kuralı olabilir. Koşullardan biriyle karşılaştığımızda, iltihaplanma hakkında bir sonuca varabilir ve daha sonra bunu daha fazla akıl yürütmede kullanabiliriz.
   - Algoritmalar, neredeyse hiçbir zaman doğrudan bilgi tabanlı sistemlerde kullanılmamalarına rağmen, yöntemsel temsilin başka bir biçimi olarak düşünülebilir.

4. **Mantık** ilk olarak Aristo tarafından evrensel insan bilgisini temsil etmenin bir yolu olarak önerildi.
   - Matematiksel bir teori olarak Yüklem Mantığı, hesaplanamayacak kadar zengindir, bu nedenle normal olarak Prolog'da kullanılan Horn cümlecikleri gibi bazı alt kümeleri kullanılır.
   - Tanımlayıcı Mantık, *anlamsal ağ* gibi dağıtılmış bilgi temsilleri olan nesnelerin hiyerarşilerini temsil etmek ve bunlar hakkında akıl yürütmek için kullanılan bir mantıksal sistemler ailesidir.

## Uzman Sistemler

Simgesel YZ'nin ilk başarılarından biri, **uzman sistemler** olarak adlandırıldı - bazı sınırlı problem alanlarında uzman olarak davranmak üzere tasarlanmış bilgisayar sistemleridir. Bir veya daha fazla insan uzmanından alınan bir **bilgi tabanına** dayanıyorlardı ve bunun üzerinden bazı akıl yürütmeler yapan bir **çıkarsama motoru** içeriyorlardı.

![İnsan Mimarisi](../images/arch-human.png) | ![Bilgi Tabanlı Sistem](../images/arch-kbs.png)
---------------------------------------------|------------------------------------------------
Bir insan sinir sisteminin basitleştirilmiş yapısı | Bilgi tabanlı bir sistemin mimarisi

Uzman sistemler, **kısa süreli bellek** ve **uzun süreli bellek** içeren insan akıl yürütme sistemi gibi oluşturulmuştur. Benzer şekilde, bilgi tabanlı sistemlerde aşağıdaki bileşenleri fark edebiliriz:

* **Problem belleği**: Şu anda çözülmekte olan problem hakkındaki bilgileri, yani bir hastanın ateşi veya tansiyonu, iltihabı olup olmadığı vb. bilgileri içerir. Bu bilgi aynı zamanda **statik bilgi** olarak da adlandırılır, çünkü sorun hakkında şu anda bildiklerimizin bir anlık görüntüsünü içerir - sözde *problem durumu*.
* **Bilgi tabanı**: Bir problem alanı hakkında uzun vadeli bilgiyi temsil eder. İnsan uzmanlardan manuel olarak elde edilir ve muayeneden muayeneye değişmez. Bir problem durumundan diğerine geçmemize izin verdiği için **dinamik bilgi** olarak da adlandırılır.
* **Çıkarsama motoru**: Gerektiğinde kullanıcıya sorular sorarak, problem durumu alanında tüm arama sürecini düzenler. Ayrıca her duruma uygulanacak doğru kuralları bulmaktan da sorumludur.

Örnek olarak, bir hayvanın fiziksel özelliklerine göre belirleyen aşağıdaki uzman sistemi ele alalım:

![VE-VEYA Ağacı](../images/AND-OR-Tree.png)

> İmge sahibi [Dmitry Soshnikov](http://soshnikov.com)

Bu diyagrama **VE-VEYA ağacı** denir ve bir dizi üretme kuralının çizgesel bir temsilidir. Bir ağaç çizmek, uzmandan bilgi elde etmenin başlangıcında faydalıdır. Bilgisayardaki bilgiyi temsil etmek için kuralları kullanmak daha uygundur:

```
EĞER hayvan et yerse
VEYA (hayvan keskin dişleri varsa
     VE hayvanın pençeleri varsa
     VE hayvanın ileriye bakan gözleri varsa
)
O ZAMAN hayvan bir etoburdur
```

Kuralın ve eylemin sol tarafındaki her koşulun esasen nesne-nitelik-değer (NND) üçlüleri olduğunu fark edebilirsiniz. **Çalışan bellek**, o anda çözülmekte olan probleme karşılık gelen NND üçlüler kümesini içerir. Bir **kural motoru**, bir koşulun sağlandığı kuralları arar ve bunları uygulayarak, çalışan belleğe başka bir üçlü ekler.

> ✅ Beğendiğiniz bir konu üzerine kendi VE-VEYA ağacınızı yazın!

### İleri ve Geri Çıkarsama

Yukarıda açıklanan sürece **ileri çıkarsama** denir. Çalışma belleğinde bulunan problemle ilgili bazı başlangıç verileriyle başlar ve ardından aşağıdaki akıl yürütme döngüsünü yürütür:

1. Çalışan bellekte hedef niteliği mevcutsa - durun ve sonucu döndürün.
2. Şu anda koşulu sağlanan tüm kuralları arayın - kuralların **çatışma kümesini**  edinin.
3. **Çatışma gidermeyi** gerçekleştirin - bu adımda yürütülecek bir kural seçin. Farklı çatışma giderme stratejileri olabilir:
   - Bilgi tabanındaki ilk geçerli kuralı seçin.
   - Rastgele bir kural seçin.
   - *Daha özgül* bir kural seçin, mesela "sol tarafta" en çok koşulu karşılayanı.
4. Seçili kuralı uygula ve problem durumuna yeni bilgi parçası ekle.
5. 1. adımdan itibaren tekrarlayın.

Ancak bazı durumlarda problem hakkında boş bir bilgiyle başlamak ve sonuca varmamıza yardımcı olacak sorular sormak isteyebiliriz. Örneğin tıbbi teşhis yaparken genellikle hastaya teşhis koymadan önce tüm tıbbi analizleri yapmıyoruz. Bir karar verilmesi gerektiğinde analizler yapmayı tercih ediyoruz.

Bu süreç **geriye çıkarsama** kullanılarak modellenebilir. Bulmak istediğimiz nitelik değeri olan **hedef** tarafından yönlendirilir:

1. Bize bir hedefin değerini verebilecek tüm kuralları seçin (yani, ST'deki hedef ("sağ taraf") ile) - bir çatışma kümesi
1. Bu nitelik için herhangi bir kural yoksa veya değeri kullanıcıdan istememiz gerektiğini söyleyen bir kural varsa - kullanıcıya sorun, aksi takdirde:
1. *Hipotez* olarak kullanacağımız bir kuralı seçmek için çatışma giderme stratejisini kullanın - bunu kanıtlamaya çalışacağız
1. Kuralın sol tarafındaki tüm nitelikler için süreci tekrarlayarak, bunları hedef olarak kanıtlamaya çalışın
1. Herhangi bir noktada süreç başarısız olursa - 3. adımda başka bir kural kullanın.

> ✅ Hangi durumlarda ileriye çıkarsama daha uygundur? Geriye çıkarsamaya ne demeli?

### Uzman Sistemlerin Uygulanması

Uzman sistemler farklı araçlar kullanılarak uygulanabilir:

* Bunları doğrudan bazı üst düzey programlama dillerinde programlamak. Bu en iyi fikir değildir, çünkü bilgiye dayalı bir sistemin ana avantajı, bilginin çıkarsamadan ayrılmasıdır ve potansiyel olarak bir problem alanı uzmanı, çıkarsama sürecinin ayrıntılarını anlamadan kurallar yazabilmelidir.
* **Uzman sistemler kabuğu**, yani bazı bilgi temsil dili kullanılarak bilgi tarafından doldurulmak üzere özel olarak tasarlanmış bir sistem kullanmak.

## ✍️ Alıştırma: Hayvan Çıkarsama

İleri ve geri çıkarsama uzman sistemi uygulama örneği için [Animals.tr.ipynb](Animals.tr.ipynb) bölümüne bakın.

> **Not**: Bu örnek oldukça basittir ve yalnızca bir uzman sistemin nasıl göründüğü hakkında fikir verir. Böyle bir sistem oluşturmaya başladığınızda, yalnızca belirli sayıda kurala ulaştığınızda, yaklaşık 200'den fazlaysa, *akıllı* davranış fark edeceksiniz. Bir noktada, kurallar hepsini akılda tutamayacak kadar karmaşık hale gelir ve bu noktada bir sistemin neden belirli kararlar aldığını merak etmeye başlayabilirsiniz. Bununla birlikte, bilgi tabanlı sistemlerin önemli özelliği, kararlardan herhangi birinin nasıl verildiğini her zaman tam olarak *açıklayabilmenizdir*.

## Ontolojiler ve Anlamsal Web

20. yüzyılın sonunda, çok özel sorgulara karşılık gelen kaynakları bulmak mümkün olacak şekilde, İnternet kaynaklarına açıklama eklemek için bilgi temsilini kullanma girişimi vardı. Bu harekete **Anlamsal Web** adı verildi ve birkaç kavrama dayanıyordu:

- **[Tanım mantığına](https://en.wikipedia.org/wiki/Description_logic)** (TM) dayalı özel bir bilgi temsili. Çerçeve bilgi temsiline benzerdir, çünkü özelliklere sahip bir nesneler hiyerarşisi oluşturur, ancak biçimsel mantıksal anlambilimi ve çıkarsama vardır. Anlamlılığın ve çıkarsamanın algoritmik karmaşıklığı arasında denge kuran bütün bir TM ailesi vardır.
- Tüm kavramların küresel bir URI tanımlayıcısı tarafından temsil edildiği, interneti kapsayan bilgi hiyerarşileri oluşturmayı mümkün kılan dağıtılmış bilgi temsili.
- Bilgi tanımı için bir XML tabanlı dil ailesi: RDF (Kaynak Tanım Çerçevesi - Resource Description Framework), RDFS (RDF Şeması), OWL (Ontoloji Web Dili).

Anlamsal Web'deki temel bir kavram, **Ontoloji** kavramıdır. Bazı resmi bilgi temsillerini kullanarak bir problem alanının açık bir isterini ifade eder. En basit ontoloji, bir problem alanındaki nesnelerin sade bir hiyerarşisi olabilir, ancak daha karmaşık ontolojiler, çıkarsama için kullanılabilecek kuralları içerecektir.

In the semantic web, all representations are based on triplets. Each object and each relation are uniquely identified by the URI. For example, if we want to state the fact that this AI Curriculum has been developed by Dmitry Soshnikov on Jan 1st, 2022 - here are the triplets we can use:

Anlamsal ağda, tüm temsiller üçlülere dayanmaktadır. Her nesne ve her ilişki, URI tarafından benzersiz bir şekilde tanımlanır. Örneğin, bu YZ Müfredatının 1 Ocak 2022'de Dmitry Soshnikov tarafından geliştirildiğini belirtmek istersek - kullanabileceğimiz üçlüler böyledir:

<img src="../images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Burada `http://www.example.com/terms/creation-date` ve `http://purl.org/dc/elements/1.1/creator` *yaratıcı* ve *oluşturma tarihi* kavramlarını ifade etmek için iyi bilinen ve evrensel olarak kabul edilen bazı URI'lerdir. 

Daha karmaşık bir durumda, bir yaratıcı listesi tanımlamak istersek, RDF'de tanımlanan bazı veri yapılarını kullanabiliriz.

<img src="../images/triplet-complex.png" width="40%"/>

> Diyagramların sahibi [Dmitry Soshnikov](http://soshnikov.com)

Anlamsal Web'i oluşturmanın ilerlemesi, arama motorlarının ve metinden yapılandırılmış verilerin çıkarılmasına izin veren doğal dil işleme tekniklerinin başarısıyla bir şekilde yavaşladı. Bununla birlikte, bazı alanlarda ontolojileri ve bilgi tabanlarını sürdürmek için hala önemli çabalar vardır. Kayda değer birkaç proje:

* [WikiData](https://wikidata.org/), Wikipedia ile ilişkili makine tarafından okunabilen bilgi tabanlarının bir koleksiyonudur. Verilerin çoğu, Wikipedia sayfalarındaki yapılandırılmış içerik parçaları olan Wikipedia *Bilgi Kutularından* çıkarılır. Anlamsal Web için özel bir sorgu dili olan SPARQL ile wikidatada [sorgu](https://query.wikidata.org/) yapabilirsiniz. İşte insanlar arasında en popüler göz renklerini gösteren örnek bir sorgu:

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

* [DBpedia](https://www.dbpedia.org/) WikiData'ya benzer başka bir çalışmadır.

> ✅ Kendi ontolojilerinizi oluşturmayı veya mevcut olanları açmayı denemek istiyorsanız, [Protégé](https://protege.stanford.edu/) adında harika bir görsel ontoloji düzenleyicisi var. İndirin veya çevrimiçi kullanın.

<img src="../images/protege.png" width="70%"/>

*Romanov Ailesi ontolojisi ile açık Web Protégé editörü. Dmitry Soshnikov'un ekran görüntüsü*

## ✍️ Alıştırma: Bir Aile Ontolojisi

Aile ilişkileri hakkında akıl yürütmede Anlamsal Web tekniklerini kullanma örneği için [FamilyOntology.tr.ipynb](FamilyOntology.tr.ipynb) bölümüne bakın. Ortak GEDCOM formatında temsil edilen bir aile ağacını ve aile ilişkilerinin ontolojisini alacağız ve belirli bir grup birey için tüm aile ilişkilerinin bir çizgesini oluşturacağız.

## Microsoft Kavram Çizgesi

Çoğu durumda, ontolojiler dikkatle elle oluşturulur. Bununla birlikte, örneğin doğal dil metinlerinden yapılandırılmamış verilerden ontolojiler **çıkarmak** da mümkündür.

Böyle bir girişim Microsoft Research tarafından yapıldı ve [Microsoft Kavram Çizgesi](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste) ile sonuçlandı.

`is-a` (bir örneği olma) kalıtım ilişkisi kullanılarak gruplandırılmış geniş bir varlıklar topluluğudur. "Microsoft Nedir?" gibi soruların yanıtlanmasına olanak tanır - cevap, "0.87 olasılıkla bir şirket ve 0.75 olasılıkla bir marka" gibi bir şeydir.

Çizge, ya REST API olarak ya da tüm varlık çiftlerini listeleyen büyük bir indirilebilir metin dosyası olarak mevcuttur.

## ✍️ Alıştırma: Bir Kavram Çizgesi

Haber makalelerini birkaç kategoride gruplandırmak için Microsoft Kavram Çizgesi'ni nasıl kullanabileceğimizi görmek için [MSConceptGraph.tr.ipynb](MSConceptGraph.tr.ipynb) not defterini deneyin.

## Vargılar

Günümüzde YZ, genellikle *Makine Öğrenmesi* veya *Sinir Ağları* ile eşanlamlı olarak kabul edilir. Bununla birlikte, bir insan aynı zamanda şu anda sinir ağları tarafından ele alınmayan açık bir akıl yürütme sergiler. Gerçek dünya projelerinde, açıklama gerektiren görevleri gerçekleştirmek veya sistemin davranışını kontrollü bir şekilde değiştirebilmek için açık akıl yürütme hala kullanılmaktadır.

## 🚀 Kendini Sınama

Bu dersle ilişkili Aile Ontolojisi defterinde, diğer aile ilişkilerini deneme fırsatı vardır. Soy ağacındaki insanlar arasında yeni bağlantılar keşfetmeye çalışın.

## [Ders sonrası sınavı](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/202)

## Gözden Geçirme ve Bireysel Çalışma

İnsanların bilgiyi ölçmeye ve kodlamaya çalıştığı alanları keşfetmek için internette biraz araştırma yapın. Bloom'un Taksonomisine bir göz atın ve insanların dünyalarını nasıl anlamlandırmaya çalıştıklarını öğrenmek için tarihe bakın. Linnaeus'un bir organizma sınıflandırması yaratma çalışmalarını keşfedin ve Dmitri Mendeleev'in kimyasal elementlerin tanımlanması ve gruplandırılması için yarattığını yolu gözlemleyin. Başka hangi ilginç örnekleri bulabilirsiniz?

**Ödev**: [Bir Ontoloji Oluşturun](assignment.tr.md)
