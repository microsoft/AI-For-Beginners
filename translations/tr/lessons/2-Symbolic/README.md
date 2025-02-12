# Bilgi Temsili ve Uzman Sistemleri

![Sembolik AI içeriğinin özeti](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.tr.png)

> Sketchnote [Tomomi Imura](https://twitter.com/girlie_mac) tarafından

Yapay zeka arayışı, insanlara benzer şekilde dünyayı anlamak için bilgi arayışına dayanır. Peki, bunu nasıl yapabilirsiniz?

## [Ders öncesi quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/102)

Yapay zekanın ilk dönemlerinde, zeki sistemler oluşturmak için yukarıdan aşağıya yaklaşım (önceki derste tartışılan) popülerdi. Fikir, bilgiyi insanlardan makine tarafından okunabilir bir forma çıkarmak ve ardından bunu otomatik olarak sorunları çözmek için kullanmaktı. Bu yaklaşım iki büyük fikre dayanıyordu:

* Bilgi Temsili
* Akıl Yürütme

## Bilgi Temsili

Sembolik AI'deki önemli kavramlardan biri **bilgidir**. Bilgiyi *bilgi* veya *veri* ile ayırt etmek önemlidir. Örneğin, kitapların bilgi içerdiğini söyleyebiliriz, çünkü kitapları inceleyerek uzmanlaşabiliriz. Ancak, kitapların içeriği aslında *veri* olarak adlandırılır ve bu verileri okuyarak ve dünyamız modeline entegre ederek bu verileri bilgiye dönüştürürüz.

> ✅ **Bilgi**, kafamızda bulunan ve dünyayı anlama şeklimizi temsil eden bir şeydir. Aktif bir **öğrenme** süreci ile elde edilir; bu süreç, aldığımız bilgi parçalarını aktif dünya modelimize entegre eder.

Çoğu zaman bilgiyi katı bir şekilde tanımlamayız, ancak [DIKW Piramidi](https://en.wikipedia.org/wiki/DIKW_pyramid) gibi diğer ilgili kavramlarla ilişkilendiririz. Bu, aşağıdaki kavramları içerir:

* **Veri**, fiziksel medya üzerinde temsil edilen bir şeydir; yazılı metin veya sözel kelimeler gibi. Veri, insanlardan bağımsız olarak var olur ve insanlar arasında aktarılabilir.
* **Bilgi**, veriyi kafamızda nasıl yorumladığımızdır. Örneğin, "bilgisayar" kelimesini duyduğumuzda, bunun ne olduğu hakkında bir anlayışımız vardır.
* **Bilgi**, bilgilerin dünya modelimize entegre edilmesidir. Örneğin, bir bilgisayarın ne olduğunu öğrendiğimizde, bunun nasıl çalıştığı, ne kadar maliyeti olduğu ve ne amaçla kullanılabileceği hakkında bazı fikirler edinmeye başlarız. Bu birbiriyle ilişkili kavramlar ağı, bilgimizi oluşturur.
* **Bilgelik**, dünyayı anlama seviyemizin bir başka boyutudur ve *meta-bilgi* temsil eder; örneğin, bilginin nasıl ve ne zaman kullanılacağına dair bir kavram.

<img src="images/DIKW_Pyramid.png" width="30%"/>

*Görsel [Wikipedia'dan](https://commons.wikimedia.org/w/index.php?curid=37705247), Longlivetheux - Kendi çalışması, CC BY-SA 4.0*

Böylece, **bilgi temsili** sorunu, bilgiyi bir bilgisayar içinde veri biçiminde etkili bir şekilde temsil etmenin bir yolunu bulmaktır, böylece otomatik olarak kullanılabilir hale gelir. Bu, bir spektrum olarak görülebilir:

![Bilgi temsili spektrumu](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.tr.png)

> Görsel [Dmitry Soshnikov](http://soshnikov.com) tarafından

* Solda, bilgisayarlar tarafından etkili bir şekilde kullanılabilen çok basit bilgi temsilleri vardır. En basiti algoritmik olanıdır; burada bilgi, bir bilgisayar programı ile temsil edilir. Ancak, bu bilgi temsilinin en iyi yolu değildir, çünkü esnek değildir. Kafamızdaki bilgi genellikle algoritmik değildir.
* Sağda, doğal metin gibi temsiller vardır. En güçlü olanıdır, ancak otomatik akıl yürütme için kullanılamaz.

> ✅ Bilgiyi kafanızda nasıl temsil ettiğinizi ve notlara dönüştürdüğünüzü bir dakika düşünün. Hatırlamayı kolaylaştırmak için sizin için iyi çalışan belirli bir format var mı?

## Bilgisayar Bilgi Temsillerinin Sınıflandırılması

Farklı bilgisayar bilgi temsil yöntemlerini aşağıdaki kategorilere ayırabiliriz:

* **Ağ temsilleri**, kafamızda birbiriyle ilişkili kavramlar ağına sahip olduğumuz gerçeğine dayanır. Aynı ağları bir graf olarak bir bilgisayarda yeniden üretmeye çalışabiliriz - buna **anlamsal ağ** denir.

1. **Nesne-Aitlik-Değer üçlüleri** veya **aitlik-değer çiftleri**. Bir graf, bilgisayarda düğüm ve kenar listesini temsil edebileceği için, bir anlamsal ağı, nesneleri, özellikleri ve değerleri içeren üçlüler listesi ile temsil edebiliriz. Örneğin, programlama dilleri hakkında aşağıdaki üçlüleri oluştururuz:

Nesne | Aitlik | Değer
-------|-----------|------
Python | dir | Tipleme-İçermeyen-Dil
Python | icat-edildi | Guido van Rossum
Python | blok-sözdizimi | girinti
Tipleme-İçermeyen-Dil | yoktur | tür tanımlamaları

> ✅ Üçlülerin diğer bilgi türlerini temsil etmek için nasıl kullanılabileceğini düşünün.

2. **Hiyerarşik temsiller**, kafamızda sık sık nesnelerin bir hiyerarşisini oluşturduğumuzu vurgular. Örneğin, kanaryanın bir kuş olduğunu ve tüm kuşların kanatları olduğunu biliriz. Ayrıca, bir kanaryanın genellikle hangi renkte olduğunu ve uçuş hızının ne olduğunu da biliyoruz.

   - **Çerçeve temsili**, her nesneyi veya nesne sınıfını, **slotlar** içeren bir **çerçeve** olarak temsil etmeye dayanır. Slotların varsayılan değerleri, değer kısıtlamaları veya bir slotun değerini elde etmek için çağrılabilecek saklanan prosedürleri olabilir. Tüm çerçeveler, nesne yönelimli programlama dillerindeki nesne hiyerarşisine benzer bir hiyerarşi oluşturur.
   - **Senaryolar**, zaman içinde gelişebilecek karmaşık durumları temsil eden özel bir çerçeve türüdür.

**Python**

Slot | Değer | Varsayılan değer | Aralık |
-----|-------|---------------|----------|
İsim | Python | | |
Şu-Dir | Tipleme-İçermeyen-Dil | | |
Değişken Durumu | | CamelCase | |
Program Uzunluğu | | | 5-5000 satır |
Blok Sözdizimi | Girinti | | |

3. **Prosedürel temsiller**, bilgiyi belirli bir koşul gerçekleştiğinde yürütülebilecek eylemler listesi olarak temsil etmeye dayanır.
   - Üretim kuralları, sonuç çıkarmamıza izin veren eğer-o zaman ifadeleridir. Örneğin, bir doktorun "Eğer" bir hastada yüksek ateş "veya" kan testinde yüksek C-reaktif protein varsa "o zaman" bir iltihabı vardır şeklinde bir kuralı olabilir. Koşullardan birine ulaştığımızda, iltihap hakkında bir sonuç çıkarabiliriz ve bunu daha sonraki akıl yürütmede kullanabiliriz.
   - Algoritmalar, prosedürel temsilin başka bir biçimi olarak düşünülebilir, ancak neredeyse hiçbiri bilgi tabanlı sistemlerde doğrudan kullanılmaz.

4. **Mantık**, Aristoteles tarafından evrensel insan bilgisini temsil etmenin bir yolu olarak önerilmiştir.
   - Matematiksel bir teori olarak Predikat Mantığı, hesaplanabilirlik açısından çok zengin olduğu için genellikle bunun bir alt kümesi kullanılır; örneğin, Prolog'da kullanılan Horn cümleleri.
   - Tanımlayıcı Mantık, nesnelerin hiyerarşilerini temsil etmek ve akıl yürütmek için kullanılan mantıksal sistemler ailesidir; bu tür sistemler arasında *anlamsal web* yer alır.

## Uzman Sistemleri

Sembolik AI'nin erken başarılarından biri, belirli bir problem alanında uzman olarak hareket etmek üzere tasarlanmış bilgisayar sistemleri olan **uzman sistemleridir**. Bunlar, bir veya daha fazla insan uzmanından çıkarılan bir **bilgi tabanı** üzerine kurulmuştur ve üzerinde bazı akıl yürütmeler yapan bir **çıkarım motoru** içerir.

![İnsan Mimarisi](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.tr.png) | ![Bilgi Tabanlı Sistem](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.tr.png)
---------------------------------------------|------------------------------------------------
İnsan sinir sisteminin basitleştirilmiş yapısı | Bilgi tabanlı sistemin mimarisi

Uzman sistemleri, **kısa süreli bellek** ve **uzun süreli bellek** içeren insan akıl yürütme sistemi gibi inşa edilmiştir. Benzer şekilde, bilgi tabanlı sistemlerde aşağıdaki bileşenleri ayırt ederiz:

* **Problem belleği**: şu anda çözülen problem hakkında bilgiyi içerir; yani bir hastanın sıcaklığı veya kan basıncı, iltihap olup olmadığı vb. Bu bilgi, şu anda problem hakkında bildiklerimizin bir anlık görüntüsünü içerdiği için **statik bilgi** olarak da adlandırılır - bu, söz konusu *problem durumu*dur.
* **Bilgi tabanı**: bir problem alanı hakkında uzun süreli bilgiyi temsil eder. Bu, insan uzmanlarından manuel olarak çıkarılır ve danışmadan danışmaya değişmez. Bir problem durumundan diğerine geçiş yapmamıza olanak tanıdığı için, bu aynı zamanda **dinamik bilgi** olarak da adlandırılır.
* **Çıkarım motoru**: problem durumu alanında arama sürecini düzenler, gerektiğinde kullanıcıya sorular sorar. Ayrıca, her duruma uygulanacak doğru kuralları bulmaktan da sorumludur.

Örnek olarak, fiziksel özelliklerine dayanarak bir hayvanı belirleyen aşağıdaki uzman sistemini düşünelim:

![VE-VEYA Ağaç](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.tr.png)

> Görsel [Dmitry Soshnikov](http://soshnikov.com) tarafından

Bu diyagram bir **VE-VEYA ağacı** olarak adlandırılır ve bir dizi üretim kuralının grafiksel bir temsilidir. Bir ağacın çizilmesi, uzman bilgilerini çıkarmanın başlangıcında faydalıdır. Bilgisayar içinde bilgiyi temsil etmek için kuralları kullanmak daha uygundur:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Kuralların sol tarafındaki her koşul ve eylem esasen nesne-aitlik-değer (OAV) üçlüleridir. **Çalışma belleği**, şu anda çözülen probleme karşılık gelen OAV üçlüleri setini içerir. Bir **kural motoru**, bir koşulun karşılandığı kuralları arar ve uygular, çalışma belleğine başka bir üçlü ekler.

> ✅ Sevdiğiniz bir konuda kendi VE-VEYA ağacınızı çizin!

### İleri ve Geri Çıkarım

Yukarıda tanımlanan süreç **ileri çıkarım** olarak adlandırılır. Bu, çalışma belleğinde mevcut olan problemle ilgili bazı başlangıç verileri ile başlar ve ardından şu akıl yürütme döngüsünü yürütür:

1. Hedef özellik çalışma belleğinde mevcutsa - dur ve sonucu ver
2. Şu anda koşulu karşılanan tüm kuralları ara - **çelişki seti** elde et.
3. **Çelişki çözümü** gerçekleştir - bu adımda uygulanacak bir kural seç. Farklı çelişki çözümleme stratejileri olabilir:
   - Bilgi tabanındaki ilk uygulanabilir kuralı seç
   - Rastgele bir kural seç
   - En çok koşulu karşılayan *daha spesifik* bir kural seç, yani "sol taraf" (LHS) koşullarını en çok karşılayan kural
4. Seçilen kuralı uygula ve problem durumuna yeni bir bilgi ekle
5. 1. adıma geri dön.

Ancak, bazı durumlarda, problem hakkında boş bir bilgi ile başlamak isteyebiliriz ve sonuca ulaşmamıza yardımcı olacak sorular sorabiliriz. Örneğin, tıbbi teşhis yaparken, genellikle hastayı teşhis etmeye başlamadan önce tüm tıbbi analizleri yapmayız. Daha çok, bir karar vermemiz gerektiğinde analizler yapmak isteriz.

Bu süreç **geri çıkarım** kullanılarak modellenebilir. **Amaç** tarafından yönlendirilir - bulmaya çalıştığımız özellik değeri:

1. Amaç değerini verebilecek tüm kuralları seçin (yani, amaç sağ tarafta ("sağ taraf")) - bir çelişki seti
1. Bu özellik için kural yoksa ya da kullanıcıdan değer istememiz gerektiğini belirten bir kural varsa - bunu isteyin, aksi takdirde:
1. Bir hipotez olarak kullanacağımız bir kural seçmek için çelişki çözümleme stratejisini kullanın - bunu kanıtlamaya çalışacağız
1. Kuralın LHS'sindeki tüm özellikler için süreci tekrarlayın, bunları hedefler olarak kanıtlamaya çalışarak
1. Herhangi bir noktada süreç başarısız olursa - 3. adımda başka bir kural kullanın.

> ✅ Hangi durumlarda ileri çıkarım daha uygun? Geri çıkarım hakkında ne dersiniz?

### Uzman Sistemlerin Uygulanması

Uzman sistemler, farklı araçlar kullanılarak uygulanabilir:

* Bunları doğrudan bazı yüksek seviyeli programlama dillerinde programlamak. Bu en iyi fikir değildir, çünkü bilgi tabanlı bir sistemin ana avantajı bilginin çıkarımdan ayrılmasıdır ve potansiyel olarak bir problem alanı uzmanı, çıkarım sürecinin ayrıntılarını anlamadan kurallar yazabilmelidir.
* **Uzman sistemler kabuğu** kullanmak, yani bazı bilgi temsil dilleri kullanarak bilgi ile doldurulması için özel olarak tasarlanmış bir sistem.

## ✍️ Alıştırma: Hayvan Çıkarımı

İleri ve geri çıkarım uzman sisteminin uygulanmasına bir örnek için [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) dosyasına bakın.

> **Not**: Bu örnek oldukça basit olup, bir uzman sistemin nasıl göründüğüne dair sadece bir fikir vermektedir. Böyle bir sistem oluşturmaya başladığınızda, yaklaşık 200 kurala ulaştığınızda, sistemin belirli kararlar alma biçiminde bazı *zeka* davranışları fark edeceksiniz. Bir noktada, kurallar çok karmaşık hale gelir ve bunların hepsini akılda tutmak zorlaşır, bu noktada bir sistemin neden belirli kararlar verdiğini sorgulamaya başlayabilirsiniz. Ancak, bilgi tabanlı sistemlerin önemli bir özelliği, herhangi bir kararın nasıl alındığını her zaman *açıklayabilmenizdir*.

## Ontolojiler ve Anlamsal Web

20. yüzyılın sonunda, internet kaynaklarını işaretlemek için bilgi temsili kullanma girişimi vardı, böylece çok özel sorgulara karşılık gelen kaynakları bulmak mümkün olabilirdi. Bu hareket **Anlamsal Web** olarak adlandırıldı ve birkaç kavrama dayanıyordu:

- **[Tanım mantıkları](https://en.wikipedia.org/wiki/Description_logic)** (DL) üzerine kurulu özel bir bilgi temsili. Bu, özelliklerle nesnelerin bir hiyerarşisini oluşturduğu için çerçeve bilgi temsilinin benzeridir, ancak resmi mantıksal anlamı ve çıkarımı vardır. İfade gücü ve çıkarımın algoritmik karmaşıklığı arasında denge kuran bir dizi DL vardır.
- Tüm kavramların küresel bir URI tanımlayıcısı ile temsil edildiği dağıtık bilgi temsili, interneti kapsayan bilgi hiyerarşileri oluşturmayı mümkün kılar.
- Bilgi tanımlamak için XML tabanlı diller ailesi: RDF (Kaynak Tanım Çerçevesi), RDFS (RDF Şeması), OWL (Ontoloji Web Dili).

Anlamsal Web'deki temel kavram, **Ontoloji** kavramıdır. Bu, belirli bir problem alanının bazı resmi bilgi temsili kullanılarak açık bir şekilde tanımlanmasını ifade eder. En basit ontoloji, bir problem alanındaki nesnelerin hiyerarşisi olabilir, ancak daha karmaşık ontolojiler çıkarım için kullanılabilecek kuralları içerecektir.

Anlamsal webde, tüm temsiller üçlüler üzerine kuruludur. Her nesne ve her ilişki, URI ile benzersiz bir şekilde tanımlanır. Örneğin, bu AI Müfredatının 1 Ocak 2022'de Dmitry Soshnikov tarafından geliştirildiğini belirtmek istersek - kullanabileceğimiz üçlüler şunlardır:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Burada `http://www.example.com/terms/creation-date` and `http://purl.org/dc/elements/1.1/creator`, *yaratıcı* ve *oluşturma tarihi* kavramlarını ifade etmek için bazı iyi bilinen ve evrensel olarak kabul edilen URI'lardır.

Daha karmaşık bir durumda, bir yaratıcılar listesi tanımlamak istersek, RDF'de tanımlanan bazı veri yapıları kullanabiliriz.

<img src="images/triplet-complex.png" width="40%"/>

> Yukarıdaki diyagramlar [Dmitry Soshnikov](http://soshnikov.com) tarafından

Anlamsal Web'in inşası, arama motorlarının ve doğal dil işleme tekniklerinin başarısı nedeniyle bir nebze yavaşladı; bu teknikler metinden yapılandırılmış verileri çıkarmayı mümkün kılmaktadır. Ancak, bazı alanlarda hala ontolojileri ve bilgi tabanlarını sürdürmek için önemli çabalar gösterilmektedir. Dikkate değer birkaç

**Açıklama**:  
Bu belge, makine tabanlı AI çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluğa özen göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen dikkate alınız. Yerel dildeki orijinal belge, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilmektedir. Bu çevirinin kullanımından kaynaklanan herhangi bir yanlış anlama veya yanlış yorumlama için sorumluluk kabul etmiyoruz.