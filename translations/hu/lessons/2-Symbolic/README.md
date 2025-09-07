<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "98c5222ff9556b55223fed2337145e18",
  "translation_date": "2025-08-26T00:19:34+00:00",
  "source_file": "lessons/2-Symbolic/README.md",
  "language_code": "hu"
}
-->
# Tudásreprezentáció és szakértői rendszerek

![A szimbolikus AI tartalmának összefoglalása](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.hu.png)

> Sketchnote készítette: [Tomomi Imura](https://twitter.com/girlie_mac)

Az emberi intelligencia mesterséges megvalósításának célja a világ megértése, hasonlóan ahhoz, ahogyan az emberek teszik. De hogyan lehet ezt elérni?

## [Előadás előtti kvíz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/102)

Az AI korai időszakában népszerű volt az intelligens rendszerek létrehozásának felülről lefelé irányuló megközelítése (az előző leckében tárgyaltak szerint). Az ötlet az volt, hogy az emberek tudását gép által olvasható formába kell átültetni, majd ezt automatikusan problémák megoldására használni. Ez a megközelítés két nagy elképzelésen alapult:

* Tudásreprezentáció
* Következtetés

## Tudásreprezentáció

A szimbolikus AI egyik fontos fogalma a **tudás**. Fontos megkülönböztetni a tudást az *információtól* vagy az *adattól*. Például mondhatjuk, hogy a könyvek tudást tartalmaznak, mert tanulmányozva őket szakértővé válhatunk. Azonban amit a könyvek tartalmaznak, valójában *adat*, és amikor elolvassuk őket, és integráljuk ezt az adatot a világmodellünkbe, akkor alakítjuk át tudássá.

> ✅ **Tudás** az, ami a fejünkben van, és a világ megértését képviseli. Aktív **tanulási** folyamat révén szerezzük meg, amely integrálja az általunk kapott információkat a világ aktív modelljébe.

Leggyakrabban nem határozzuk meg szigorúan a tudást, hanem más kapcsolódó fogalmakkal hozzuk összefüggésbe a [DIKW piramis](https://en.wikipedia.org/wiki/DIKW_pyramid) segítségével. Ez a következő fogalmakat tartalmazza:

* **Adat**: Fizikai médiában reprezentált valami, például írott szöveg vagy kimondott szavak. Az adat függetlenül létezik az emberektől, és átadható közöttük.
* **Információ**: Az, ahogyan az adatot értelmezzük a fejünkben. Például, amikor meghalljuk a *számítógép* szót, van valamilyen elképzelésünk arról, hogy mi az.
* **Tudás**: Az információ integrálása a világmodellünkbe. Például, ha megtanuljuk, mi az a számítógép, elkezdünk ötleteket alkotni arról, hogyan működik, mennyibe kerül, és mire használható. Ez az összefüggő fogalmak hálózata alkotja a tudásunkat.
* **Bölcsesség**: Még egy szinttel mélyebb megértése a világnak, amely a *meta-tudást* képviseli, például azt, hogy hogyan és mikor kell használni a tudást.

*Image [from Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), By Longlivetheux - Own work, CC BY-SA 4.0*

Így a **tudásreprezentáció** problémája az, hogy találjunk valamilyen hatékony módot a tudás számítógépen belüli adatként való reprezentálására, hogy automatikusan használható legyen. Ez egy spektrumként értelmezhető:

![Tudásreprezentáció spektruma](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.hu.png)

> Kép készítette: [Dmitry Soshnikov](http://soshnikov.com)

* A bal oldalon nagyon egyszerű tudásreprezentáció típusok találhatók, amelyeket a számítógépek hatékonyan tudnak használni. A legegyszerűbb az algoritmikus megközelítés, amikor a tudást egy számítógépes program képviseli. Ez azonban nem a legjobb módja a tudás reprezentálásának, mert nem rugalmas. A fejünkben lévő tudás gyakran nem algoritmikus.
* A jobb oldalon olyan reprezentációk találhatók, mint a természetes szöveg. Ez a legkifejezőbb, de nem használható automatikus következtetésre.

> ✅ Gondolkodj el egy percre, hogyan reprezentálod a tudást a fejedben, és hogyan alakítod át jegyzetekké. Van-e olyan formátum, amely különösen jól segíti a megértést?

## Számítógépes tudásreprezentációk osztályozása

A számítógépes tudásreprezentáció különböző módszereit a következő kategóriákba sorolhatjuk:

* **Hálózati reprezentációk** azon az elven alapulnak, hogy a fejünkben egy összefüggő fogalmak hálózata található. Megpróbálhatjuk ugyanazokat a hálózatokat egy gráfként reprodukálni a számítógépben - egy úgynevezett **szemantikus hálózatként**.

1. **Objektum-Attribútum-Érték hármasok** vagy **attribútum-érték párok**. Mivel egy gráf számítógépen belül csomópontok és élek listájaként reprezentálható, egy szemantikus hálózatot hármasok listájaként is ábrázolhatunk, amelyek objektumokat, attribútumokat és értékeket tartalmaznak. Például a programozási nyelvekről a következő hármasokat építhetjük:

Objektum | Attribútum | Érték
---------|-----------|------
Python   | is        | Untyped-Language
Python   | invented-by | Guido van Rossum
Python   | block-syntax | indentation
Untyped-Language | doesn't have | type definitions

> ✅ Gondold át, hogyan lehetne hármasokat használni más típusú tudás reprezentálására.

2. **Hierarchikus reprezentációk** hangsúlyozzák azt a tényt, hogy gyakran hierarchiát hozunk létre a fejünkben lévő objektumok között. Például tudjuk, hogy a kanári egy madár, és minden madárnak van szárnya. Van elképzelésünk arról is, hogy milyen színű egy kanári általában, és milyen a repülési sebessége.

   - **Keretrendszer reprezentáció** azon alapul, hogy minden objektumot vagy objektumok osztályát egy **keretként** ábrázoljuk, amely **helyeket** tartalmaz. A helyeknek lehetnek alapértelmezett értékei, értékmegkötései vagy tárolt eljárásai, amelyeket a hely értékének megszerzéséhez lehet hívni. Az összes keret hierarchiát alkot, hasonlóan az objektumorientált programozási nyelvek objektumhierarchiájához.
   - **Forgatókönyvek** speciális keretek, amelyek összetett helyzeteket ábrázolnak, amelyek időben kibontakozhatnak.

**Python**

Hely | Érték | Alapértelmezett érték | Intervallum |
-----|-------|-----------------------|-------------|
Név  | Python |                       |             |
Is-A | Untyped-Language |             |             |
Változó eset | | CamelCase |             |
Program hossza | | | 5-5000 sor |
Blokk szintaxis | Behúzás | |             |

3. **Procedurális reprezentációk** azon alapulnak, hogy a tudást egy lista cselekvésként ábrázolják, amelyeket bizonyos feltételek bekövetkezésekor végrehajthatunk.
   - Produkciós szabályok olyan ha-akkor állítások, amelyek lehetővé teszik következtetések levonását. Például egy orvosnak lehet egy szabálya, amely szerint **HA** a betegnek magas láza van **VAGY** magas C-reaktív fehérje szintje van a vérvizsgálatban, **AKKOR** gyulladása van. Ha találkozunk az egyik feltétellel, következtetést vonhatunk le a gyulladásról, majd ezt további következtetésekhez használhatjuk.
   - Algoritmusok egy másik formája lehetnek a procedurális reprezentációnak, bár szinte soha nem használják őket közvetlenül tudásalapú rendszerekben.

4. **Logika** eredetileg Arisztotelész által javasolt módszer az univerzális emberi tudás reprezentálására.
   - Predikátum logika mint matematikai elmélet túl gazdag ahhoz, hogy számítógépes legyen, ezért általában annak egy részhalmazát használják, például a Prologban használt Horn-klauzulákat.
   - Leíró logika logikai rendszerek családja, amelyeket objektumok hierarchiáinak és elosztott tudásreprezentációk, például *szemantikus web* ábrázolására és következtetésére használnak.

## Szakértői rendszerek

A szimbolikus AI korai sikerei közé tartoztak az úgynevezett **szakértői rendszerek** - számítógépes rendszerek, amelyeket arra terveztek, hogy egy korlátozott problématerületen szakértőként működjenek. Ezek egy **tudásbázison** alapultak, amelyet egy vagy több emberi szakértőtől nyertek ki, és tartalmaztak egy **következtető motort**, amely valamilyen következtetést végzett rajta.

![Emberi architektúra](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.hu.png) | ![Tudásalapú rendszer](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.hu.png)
---------------------------------------------|------------------------------------------------
Az emberi idegrendszer egyszerűsített szerkezete | Tudásalapú rendszer architektúrája

A szakértői rendszerek az emberi következtetési rendszerhez hasonlóan épülnek fel, amely tartalmaz **rövid távú memóriát** és **hosszú távú memóriát**. Hasonlóképpen, a tudásalapú rendszerekben a következő komponenseket különböztetjük meg:

* **Problémamemória**: tartalmazza az aktuálisan megoldott problémával kapcsolatos tudást, például a beteg hőmérsékletét vagy vérnyomását, hogy van-e gyulladása vagy sem, stb. Ezt a tudást **statikus tudásnak** is nevezik, mert pillanatképet tartalmaz arról, amit jelenleg tudunk a problémáról - az úgynevezett *problémaállapotot*.
* **Tudásbázis**: a problématerületről szóló hosszú távú tudást képviseli. Ezt manuálisan nyerik ki emberi szakértőktől, és nem változik konzultációról konzultációra. Mivel lehetővé teszi, hogy egyik problémaállapotból a másikba navigáljunk, **dinamikus tudásnak** is nevezik.
* **Következtető motor**: irányítja az egész folyamatot, amely a problémaállapot térben való keresését végzi, szükség esetén kérdéseket tesz fel a felhasználónak. Felelős továbbá a megfelelő szabályok megtalálásáért, amelyeket minden állapotban alkalmazni kell.

Példaként vegyük a következő szakértői rendszert, amely egy állatot határoz meg fizikai jellemzői alapján:

![AND-OR fa](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.hu.png)

> Kép készítette: [Dmitry Soshnikov](http://soshnikov.com)

Ez a diagram egy **AND-OR fa**, amely a produkciós szabályok grafikus ábrázolása. A fa rajzolása hasznos az elején, amikor a tudást kinyerjük a szakértőtől. A tudás számítógépen belüli reprezentálásához azonban kényelmesebb szabályokat használni:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Észreveheted, hogy minden feltétel a szabály bal oldalán és az akció lényegében objektum-attribútum-érték (OAV) hármas. **Munkamemória** tartalmazza az OAV hármasok halmazát, amelyek megfelelnek az aktuálisan megoldott problémának. Egy **szabálymotor** keres olyan szabályokat, amelyek feltételei teljesülnek, és alkalmazza őket, új hármasokat adva a munkamemóriához.

> ✅ Készítsd el saját AND-OR fádat egy általad kedvelt témában!

### Előre- és visszafelé következtetés

A fent leírt folyamatot **előre következtetésnek** nevezzük. Ez azzal kezdődik, hogy a munkamemóriában rendelkezésre áll némi kezdeti adat a problémáról, majd a következő következtetési ciklust hajtja végre:

1. Ha a célattribútum jelen van a munkamemóriában - állj meg, és add meg az eredményt
2. Keress minden szabályt, amelynek feltételei jelenleg teljesülnek - hozz létre egy **konfliktushalmazt** a szabályokból.
3. Végez **konfliktusfeloldást** - válassz ki egy szabályt, amelyet ezen a lépésen végrehajtasz. Különböző konfliktusfeloldási stratégiák lehetnek:
   - Válaszd ki az első alkalmazható szabályt a tudásbázisban
   - Válassz véletlenszerű szabályt
   - Válassz egy *specifikusabb* szabályt, azaz azt, amelyik a legtöbb feltételt teljesíti a "bal oldalon" (LHS)
4. Alkalmazd a kiválasztott szabályt, és adj hozzá új tudáselemet a problémaállapothoz
5. Ismételd meg az 1. lépéstől.

Azonban bizonyos esetekben előfordulhat, hogy üres tudással szeretnénk kezdeni a problémáról, és kérdéseket feltenni, amelyek segítenek eljutni a következtetéshez. Például orvosi diagnózis során általában nem végezzük el az összes orvosi elemzést előre, mielőtt elkezdenénk diagnosztizálni a beteget. Inkább akkor végezzük el az elemzéseket, amikor döntést kell hozni.

Ez a folyamat **visszafelé következtetéssel** modellezhető. Ez a **cél** által vezérelt - az attribútumérték, amelyet keresünk:

1. Válassz ki minden szabályt, amely megadhatja a cél értékét (azaz a cél a szabály jobb oldalán (RHS) van) - egy konfliktushalmaz
1. Ha nincs szabály erre az attribútumra, vagy van egy szabály, amely szerint az értéket a felhasználótól kell kérni - kérdezd meg, különben:
1. Használj konfliktusfeloldási stratégiát, hogy kiválassz egy szabályt, amelyet *hipotézisként* fogsz használni - megpróbáljuk bizonyítani
1. Ismételten ismételd meg a folyamatot a szabály bal oldalán (LHS) lévő összes attribútumra, megpróbálva bizonyítani őket célként
1. Ha bármelyik ponton a folyamat meghiúsul - használj másik szabályt a 3. lépésben.

> ✅ Milyen helyzetekben megfelelőbb az előre következtetés? És mi a helyzet a visszafelé következtetéssel?

### Szakértői rendszerek megvalósítása

A szakértői rendszerek különböző eszközökkel valósíthatók meg:

* Közvetlen programozás valamilyen magas szintű programozási nyelven. Ez nem a legjobb ötlet, mert a tudásalapú rendszer fő előnye, hogy a tudás elkülönül a következtetéstől, és potenciálisan a problématerület szakértője képesnek kell lennie szabályokat írni anélkül, hogy megértené a következtetési folyamat részleteit.
* **Szakértői rendszerek héjának** használata, azaz egy olyan rendszer, amelyet kifejezetten arra terveztek, hogy tudással töltsék fel valamilyen tudásreprezentációs nyelv segítségével.

## ✍️ Gyakorlat: Állati következtetés

Lásd [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) példát az előre és visszafelé következtetés szakért
> **Megjegyzés**: Ez a példa meglehetősen egyszerű, és csak azt az elképzelést adja, hogy hogyan néz ki egy szakértői rendszer. Amint elkezdesz egy ilyen rendszert létrehozni, csak akkor fogsz észrevenni némi *intelligens* viselkedést, amikor elérsz egy bizonyos számú szabályt, körülbelül 200+. Egy ponton a szabályok túl bonyolulttá válnak ahhoz, hogy mindet fejben tartsd, és ekkor kezdhetsz azon tűnődni, miért hoz a rendszer bizonyos döntéseket. Azonban a tudásalapú rendszerek fontos jellemzője, hogy mindig pontosan *meg tudod magyarázni*, hogyan születtek meg az egyes döntések.
## Ontológiák és a szemantikus web

A 20. század végén kezdeményezés indult azzal a céllal, hogy az internetes erőforrásokat tudásreprezentációval annotálják, így lehetővé váljon olyan erőforrások megtalálása, amelyek nagyon specifikus lekérdezéseknek felelnek meg. Ezt a kezdeményezést **szemantikus webnek** nevezték, és több alapelvre épült:

- Egy speciális tudásreprezentáció, amely **[leíró logikákon](https://en.wikipedia.org/wiki/Description_logic)** (DL) alapul. Ez hasonló a keret-alapú tudásreprezentációhoz, mivel objektumok hierarchiáját építi fel tulajdonságokkal, de formális logikai szemantikával és következtetéssel rendelkezik. A DL-ek egy egész családja létezik, amelyek az expresszivitás és a következtetés algoritmikus komplexitása között egyensúlyoznak.
- Elosztott tudásreprezentáció, ahol minden fogalmat egy globális URI azonosító képvisel, lehetővé téve olyan tudáshierarchiák létrehozását, amelyek átfogják az internetet.
- XML-alapú nyelvek családja a tudás leírására: RDF (Resource Description Framework), RDFS (RDF Schema), OWL (Ontology Web Language).

A szemantikus web központi fogalma az **ontológia**. Ez egy probléma domainjének explicit specifikációjára utal, valamilyen formális tudásreprezentáció segítségével. A legegyszerűbb ontológia lehet egy objektumok hierarchiája egy probléma domainben, de a bonyolultabb ontológiák szabályokat is tartalmaznak, amelyek következtetésre használhatók.

A szemantikus webben minden reprezentáció tripleteken alapul. Minden objektumot és minden kapcsolatot egyedi URI azonosít. Például, ha azt szeretnénk kijelenteni, hogy ezt az AI Curriculumot Dmitry Soshnikov fejlesztette ki 2022. január 1-jén, itt vannak a használható tripletek:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Itt a `http://www.example.com/terms/creation-date` és a `http://purl.org/dc/elements/1.1/creator` néhány jól ismert és univerzálisan elfogadott URI, amelyek a *készítő* és a *létrehozás dátuma* fogalmakat fejezik ki.

Egy bonyolultabb esetben, ha egy készítők listáját szeretnénk meghatározni, használhatunk néhány RDF-ben definiált adatstruktúrát.

<img src="images/triplet-complex.png" width="40%"/>

> A fenti diagramokat [Dmitry Soshnikov](http://soshnikov.com) készítette.

A szemantikus web építésének előrehaladását némileg lelassította a keresőmotorok és a természetes nyelvfeldolgozási technikák sikere, amelyek lehetővé teszik a strukturált adatok kinyerését szövegekből. Azonban bizonyos területeken még mindig jelentős erőfeszítések történnek ontológiák és tudásbázisok fenntartására. Néhány figyelemre méltó projekt:

* [WikiData](https://wikidata.org/) egy gép által olvasható tudásbázisok gyűjteménye, amely a Wikipédiához kapcsolódik. Az adatok nagy része a Wikipédia *InfoBoxokból* származik, amelyek strukturált tartalomdarabok a Wikipédia oldalain. A WikiData-t [SPARQL](https://query.wikidata.org/) segítségével lehet lekérdezni, amely egy speciális lekérdezési nyelv a szemantikus webhez. Íme egy példa lekérdezés, amely megjeleníti az emberek körében leggyakoribb szemszíneket:

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

* [DBpedia](https://www.dbpedia.org/) egy másik kezdeményezés, amely hasonló a WikiData-hoz.

> ✅ Ha szeretnél kísérletezni saját ontológiák építésével vagy meglévők megnyitásával, van egy remek vizuális ontológia szerkesztő, a [Protégé](https://protege.stanford.edu/). Töltsd le, vagy használd online.

<img src="images/protege.png" width="70%"/>

*Web Protégé szerkesztő megnyitva a Romanov család ontológiájával. Dmitry Soshnikov képernyőképe*

## ✍️ Gyakorlat: Egy családi ontológia

Nézd meg a [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) fájlt, amely példát mutat arra, hogyan használhatók a szemantikus web technikái családi kapcsolatok elemzésére. Egy általános GEDCOM formátumban ábrázolt családfát és egy családi kapcsolatok ontológiáját fogjuk használni, hogy gráfot építsünk az adott egyének közötti családi kapcsolatokból.

## Microsoft Concept Graph

A legtöbb esetben az ontológiákat gondosan kézzel készítik. Azonban lehetséges ontológiákat **kinyerni** strukturálatlan adatokból, például természetes nyelvű szövegekből.

Egy ilyen próbálkozást a Microsoft Research végezte, amelynek eredménye a [Microsoft Concept Graph](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste).

Ez egy nagy gyűjteménye az entitásoknak, amelyeket `is-a` öröklési kapcsolat alapján csoportosítottak. Lehetővé teszi olyan kérdések megválaszolását, mint például "Mi a Microsoft?" - a válasz valami olyasmi, mint "egy vállalat 0,87 valószínűséggel, és egy márka 0,75 valószínűséggel".

A grafikon elérhető REST API-n keresztül, vagy egy nagy letölthető szövegfájlként, amely az összes entitáspárt felsorolja.

## ✍️ Gyakorlat: Egy fogalomgrafikon

Próbáld ki az [MSConceptGraph.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb) notebookot, hogy megnézd, hogyan használhatjuk a Microsoft Concept Graph-ot hírcikkek több kategóriába történő csoportosítására.

## Következtetés

Manapság az AI-t gyakran a *gépi tanulás* vagy *neurális hálózatok* szinonimájaként emlegetik. Azonban az emberi lények explicit következtetést is végeznek, ami olyasmi, amit jelenleg a neurális hálózatok nem kezelnek. Valós projektekben az explicit következtetést továbbra is használják olyan feladatok elvégzésére, amelyek magyarázatokat igényelnek, vagy amelyeknél a rendszer viselkedését kontrollált módon kell módosítani.

## 🚀 Kihívás

A leckéhez kapcsolódó Family Ontology notebookban lehetőség van más családi kapcsolatokkal kísérletezni. Próbálj meg új kapcsolatokat felfedezni az emberek között a családfában.

## [Utólagos kvíz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/202)

## Áttekintés és önálló tanulás

Kutatásokat végezhetsz az interneten, hogy felfedezd azokat a területeket, ahol az emberek megpróbálták a tudást számszerűsíteni és kódolni. Nézd meg Bloom taxonómiáját, és menj vissza a történelemben, hogy megtudd, hogyan próbálták az emberek értelmezni a világukat. Fedezd fel Linnaeus munkáját, amelyben az organizmusok taxonómiáját hozta létre, és figyeld meg, hogyan alkotta meg Dmitrij Mengyelejev a kémiai elemek leírására és csoportosítására szolgáló rendszert. Milyen más érdekes példákat találsz?

**Feladat**: [Építs egy ontológiát](assignment.md)

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.