<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ddf651d7681b4449f9d09ea3b17911e",
  "translation_date": "2025-08-25T23:20:56+00:00",
  "source_file": "lessons/6-Other/23-MultiagentSystems/README.md",
  "language_code": "hu"
}
-->
# Többügynökös rendszerek

Az intelligencia elérésének egyik lehetséges módja az úgynevezett **emergens** (vagy **szinergikus**) megközelítés, amely azon az elven alapul, hogy sok viszonylag egyszerű ügynök együttes viselkedése a rendszer egészének összetettebb (vagy intelligensebb) viselkedését eredményezheti. Elméletileg ez a [Kollektív intelligencia](https://en.wikipedia.org/wiki/Collective_intelligence), az [Emergentizmus](https://en.wikipedia.org/wiki/Global_brain) és az [Evolúciós kibernetika](https://en.wikipedia.org/wiki/Global_brain) elvein alapul, amelyek szerint a magasabb szintű rendszerek valamilyen hozzáadott értéket nyernek, ha megfelelően kombinálják őket alacsonyabb szintű rendszerekből (az úgynevezett *metarendszer-átmenet elve*).

## [Előadás előtti kvíz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/123)

A **többügynökös rendszerek** iránya az 1990-es években jelent meg a mesterséges intelligencia területén, válaszul az internet és az elosztott rendszerek növekedésére. Az egyik klasszikus mesterséges intelligencia tankönyv, az [Artificial Intelligence: A Modern Approach](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), a klasszikus mesterséges intelligencia szemléletét a többügynökös rendszerek nézőpontjából vizsgálja.

A többügynökös megközelítés központi eleme az **ügynök** fogalma – egy olyan entitás, amely egy bizonyos **környezetben** él, amelyet érzékelni tud, és amelyre hatással lehet. Ez egy nagyon tág definíció, és számos különböző típusú és osztályozású ügynök létezhet:

* Az érvelési képességük alapján:
   - **Reaktív** ügynökök általában egyszerű kérés-válasz típusú viselkedést mutatnak
   - **Deliberatív** ügynökök valamilyen logikai érvelési és/vagy tervezési képességet alkalmaznak
* Az alapján, hogy hol futtatják a kódjukat:
   - **Statikus** ügynökök egy dedikált hálózati csomóponton működnek
   - **Mobil** ügynökök képesek a kódjukat hálózati csomópontok között mozgatni
* A viselkedésük alapján:
   - **Passzív ügynökök** nem rendelkeznek konkrét célokkal. Ezek az ügynökök reagálhatnak külső ingerekre, de maguktól nem kezdeményeznek cselekvést.
   - **Aktív ügynökök** rendelkeznek bizonyos célokkal, amelyeket követnek
   - **Kognitív ügynökök** összetett tervezést és érvelést alkalmaznak

A többügynökös rendszereket manapság számos alkalmazásban használják:

* Játékokban sok nem játékos karakter (NPC) valamilyen mesterséges intelligenciát alkalmaz, és intelligens ügynöknek tekinthető
* Videógyártásban a komplex 3D jelenetek renderelése, amelyek tömegeket tartalmaznak, tipikusan többügynökös szimulációval történik
* Rendszermodellezésben a többügynökös megközelítést használják egy komplex modell viselkedésének szimulálására. Például a többügynökös megközelítést sikeresen alkalmazták a COVID-19 betegség globális terjedésének előrejelzésére. Hasonló megközelítés alkalmazható egy város forgalmának modellezésére, és annak vizsgálatára, hogyan reagál a forgalmi szabályok változásaira.
* Komplex automatizálási rendszerekben minden eszköz független ügynökként működhet, ami az egész rendszert kevésbé monolitikussá és robusztusabbá teszi.

Nem fogunk mélyen belemenni a többügynökös rendszerek részleteibe, de megvizsgálunk egy példát a **többügynökös modellezésre**.

## NetLogo

A [NetLogo](https://ccl.northwestern.edu/netlogo/) egy többügynökös modellezési környezet, amely a [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) programozási nyelv módosított változatán alapul. Ezt a nyelvet eredetileg a programozási koncepciók tanítására fejlesztették ki gyerekek számára, és lehetővé teszi egy **teknős** nevű ügynök irányítását, amely mozoghat, és nyomot hagyhat maga után. Ez lehetővé teszi komplex geometriai alakzatok létrehozását, ami vizuális módon segíti az ügynök viselkedésének megértését.

A NetLogo-ban sok teknőst hozhatunk létre a `create-turtles` parancs segítségével. Ezután utasíthatjuk az összes teknőst, hogy végezzen el bizonyos műveleteket (az alábbi példában - mozogjon előre 10 egységet):

```
create-turtles 10
ask turtles [
  forward 10
]
```

Természetesen nem túl érdekes, ha minden teknős ugyanazt csinálja, ezért a `ask` parancs segítségével csoportokat is utasíthatunk, például azokat, amelyek egy bizonyos pont közelében vannak. Különböző *fajtájú* teknősöket is létrehozhatunk a `breed [cats cat]` paranccsal. Itt a `cat` a fajta neve, és meg kell adnunk az egyes és többes számú alakot is, mert a különböző parancsok az érthetőség érdekében különböző formákat használnak.

> ✅ Nem fogunk belemenni a NetLogo nyelv tanulásába – ha érdekel, látogasd meg a kiváló [Beginner's Interactive NetLogo Dictionary](https://ccl.northwestern.edu/netlogo/bind/) oldalt.

A NetLogo-t [letöltheted](https://ccl.northwestern.edu/netlogo/download.shtml) és telepítheted, hogy kipróbáld.

### Modellek könyvtára

A NetLogo egyik nagyszerű tulajdonsága, hogy tartalmaz egy működő modellekből álló könyvtárat, amelyeket kipróbálhatsz. Lépj a **File → Models Library** menüpontra, és számos modellkategória közül választhatsz.

<img alt="NetLogo Models Library" src="images/NetLogo-ModelLib.png" width="60%"/>

> Dmitry Soshnikov által készített képernyőkép a modellek könyvtáráról

Megnyithatsz egy modellt, például **Biology → Flocking**.

### Főbb elvek

A modell megnyitása után a NetLogo fő képernyőjére kerülsz. Itt egy minta modell, amely a farkasok és juhok populációját írja le véges erőforrások (fű) mellett.

![NetLogo Main Screen](../../../../../translated_images/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.hu.png)

> Dmitry Soshnikov által készített képernyőkép

Ezen a képernyőn láthatod:

* Az **Interfész** szekciót, amely tartalmazza:
  - A fő mezőt, ahol az ügynökök élnek
  - Különböző vezérlőelemeket: gombokat, csúszkákat stb.
  - Grafikonokat, amelyeken a szimuláció paramétereit jelenítheted meg
* A **Kód** fület, amely tartalmazza a szerkesztőt, ahol a NetLogo programot írhatod

A legtöbb esetben az interfész tartalmaz egy **Setup** gombot, amely inicializálja a szimuláció állapotát, és egy **Go** gombot, amely elindítja a végrehajtást. Ezeket a megfelelő kezelők kezelik a kódban, amelyek így néznek ki:

```
to go [
...
]
```

A NetLogo világa a következő objektumokból áll:

* **Ügynökök** (teknősök), amelyek mozoghatnak a mezőn, és végezhetnek valamilyen tevékenységet. Az ügynököket a `ask turtles [...]` szintaxissal utasíthatod, és a zárójelek közötti kódot minden ügynök *teknős módban* hajtja végre.
* **Foltok** (patches), amelyek a mező négyzet alakú területei, ahol az ügynökök élnek. Hivatkozhatsz az ugyanazon a folton lévő összes ügynökre, vagy megváltoztathatod a foltok színét és egyéb tulajdonságait. A foltokat is utasíthatod a `ask patches` paranccsal.
* **Megfigyelő** (observer), amely egy egyedi ügynök, és a világot irányítja. Az összes gombkezelő *megfigyelő módban* fut.

> ✅ A többügynökös környezet szépsége abban rejlik, hogy a teknős módban vagy folt módban futó kódot az összes ügynök párhuzamosan hajtja végre. Így kevés kód megírásával és az egyes ügynökök viselkedésének programozásával komplex szimulációs rendszer viselkedését hozhatod létre.

### Flocking

A többügynökös viselkedés példájaként vizsgáljuk meg a **[Flocking](https://en.wikipedia.org/wiki/Flocking_(behavior))** jelenséget. A Flocking egy összetett minta, amely nagyon hasonlít arra, ahogyan a madárrajok repülnek. Ha figyeled őket, azt gondolhatod, hogy valamilyen kollektív algoritmust követnek, vagy hogy valamilyen *kollektív intelligenciával* rendelkeznek. Azonban ez az összetett viselkedés akkor jön létre, amikor minden egyes ügynök (ebben az esetben egy *madár*) csak a közvetlen közelében lévő ügynököket figyeli, és három egyszerű szabályt követ:

* **Igazodás** – az ügynök a szomszédos ügynökök átlagos irányába fordul
* **Kohézió** – az ügynök a szomszédok átlagos pozíciója felé próbál haladni (*hosszú távú vonzás*)
* **Elválás** – ha túl közel kerül más madarakhoz, távolodni próbál (*rövid távú taszítás*)

Futtathatod a flocking példát, és megfigyelheted a viselkedést. Állíthatod a paramétereket is, például az *elválás mértékét* vagy a *látótávolságot*, amely meghatározza, hogy egy madár milyen messzire lát. Figyeld meg, hogy ha a látótávolságot 0-ra csökkented, minden madár megvakul, és a flocking megszűnik. Ha az elválást 0-ra csökkented, minden madár egy egyenes vonalba gyűlik.

> ✅ Válts a **Kód** fülre, és nézd meg, hol vannak a flocking három szabálya (igazodás, kohézió és elválás) a kódban megvalósítva. Figyeld meg, hogy csak azokra az ügynökökre hivatkozunk, amelyek a látótávolságon belül vannak.

### Egyéb modellek, amelyeket érdemes megnézni

Van néhány további érdekes modell, amelyeket kipróbálhatsz:

* **Art → Fireworks** bemutatja, hogyan tekinthető egy tűzijáték az egyes tűzcsóvák kollektív viselkedésének
* **Social Science → Traffic Basic** és **Social Science → Traffic Grid** bemutatja a városi forgalom modelljét 1D-ben és 2D rácson, lámpákkal vagy anélkül. Minden autó a következő szabályokat követi:
   - Ha az előtte lévő hely üres – gyorsít (egy bizonyos maximális sebességig)
   - Ha akadályt lát maga előtt – fékez (és állíthatod, hogy milyen messzire lát a sofőr)
* **Social Science → Party** bemutatja, hogyan csoportosulnak az emberek egy koktélpartin. Megtalálhatod azokat a paraméterkombinációkat, amelyek a csoport boldogságának leggyorsabb növekedéséhez vezetnek.

Amint ezekből a példákból láthatod, a többügynökös szimulációk nagyon hasznosak lehetnek egy olyan komplex rendszer viselkedésének megértéséhez, amely egyénekből áll, akik ugyanazt vagy hasonló logikát követik. Használhatók virtuális ügynökök, például [NPC-k](https://en.wikipedia.org/wiki/NPC) irányítására számítógépes játékokban, vagy ügynökök irányítására 3D animált világokban.

## Deliberatív ügynökök

A fent leírt ügynökök nagyon egyszerűek, és valamilyen algoritmus segítségével reagálnak a környezet változásaira. Ezeket **reaktív ügynököknek** nevezzük. Azonban néha az ügynökök képesek érvelni és megtervezni a cselekvéseiket, ebben az esetben **deliberatív ügynököknek** nevezzük őket.

Egy tipikus példa lehet egy személyes ügynök, amely egy embertől kapott utasítást, hogy foglaljon le egy nyaralási utat. Tegyük fel, hogy az interneten sok ügynök él, akik segíthetnek neki. Az ügynöknek kapcsolatba kell lépnie más ügynökökkel, hogy megtudja, milyen járatok érhetők el, milyen árakon érhetők el a szállodák különböző időpontokban, és meg kell próbálnia a legjobb árat kialkudni. Amikor a nyaralási terv elkészül és a tulajdonos jóváhagyja, az ügynök folytathatja a foglalást.

Ehhez az ügynököknek **kommunikálniuk** kell. A sikeres kommunikációhoz szükségük van:

* Valamilyen **szabványos nyelvre a tudás cseréjéhez**, például [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) és [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Ezeket a nyelveket a [beszédaktus-elmélet](https://en.wikipedia.org/wiki/Speech_act) alapján tervezték.
* Ezeknek a nyelveknek tartalmazniuk kell valamilyen **tárgyalási protokollokat**, amelyek különböző **aukciótípusokon** alapulnak.
* Egy **közös ontológiára**, hogy ugyanazokra a fogalmakra hivatkozzanak, ismerve azok szemantikáját
* Egy módra, hogy **felfedezzék**, mit tudnak tenni a különböző ügynökök, szintén valamilyen ontológia alapján

A deliberatív ügynökök sokkal összetettebbek, mint a reaktívak, mert nemcsak a környezet változásaira reagálnak, hanem képesek *kezdeményezni* is cselekvéseket. Az egyik javasolt architektúra a deliberatív ügynökökhöz az úgynevezett Hiedelem-Vágy-Szándék (Belief-Desire-Intention, BDI) ügynök:

* **Hiedelmek** alkotják az ügynök környezetéről szóló tudásbázist. Ez lehet egy tudásbázis vagy szabályok halmaza, amelyeket az ügynök alkalmazhat egy adott helyzetre.
* **Vágyak** határozzák meg, hogy mit akar az ügynök elérni, azaz a céljait. Például a fent említett személyes asszisztens ügynök célja egy utazás lefoglalása, míg egy szállodai ügynök célja a profit maximalizálása.
* **Szándékok** azok a konkrét cselekvések, amelyeket az ügynök a céljai eléréséhez tervez. A cselekvések általában megváltoztatják a környezetet,

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.