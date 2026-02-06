# Etikus és Felelős Mesterséges Intelligencia

Majdnem befejezted ezt a kurzust, és remélem, hogy mostanra világosan látod, hogy a mesterséges intelligencia számos formális matematikai módszeren alapul, amelyek lehetővé teszik számunkra, hogy kapcsolatokat találjunk az adatokban, és modelleket képezzünk ki az emberi viselkedés bizonyos aspektusainak utánzására. A történelem ezen pontján a mesterséges intelligenciát egy nagyon erőteljes eszköznek tekintjük, amely segít mintázatokat kinyerni az adatokból, és ezeket a mintázatokat új problémák megoldására alkalmazni.

## [Előadás előtti kvíz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

A tudományos fantasztikus irodalomban azonban gyakran találkozunk olyan történetekkel, ahol a mesterséges intelligencia veszélyt jelent az emberiségre. Ezek a történetek általában valamilyen mesterséges intelligencia-lázadás köré épülnek, amikor az MI úgy dönt, hogy szembeszáll az emberekkel. Ez azt sugallja, hogy az MI-nek valamilyen érzelmei vannak, vagy olyan döntéseket hozhat, amelyeket a fejlesztői nem láttak előre.

Az a mesterséges intelligencia, amelyről ebben a kurzusban tanultunk, nem más, mint nagy mátrixszámítás. Ez egy nagyon erőteljes eszköz, amely segít megoldani a problémáinkat, és mint minden más erőteljes eszköz - jó és rossz célokra egyaránt használható. Fontos megjegyezni, hogy *visszaélhetnek* vele.

## A Felelős Mesterséges Intelligencia Alapelvei

Annak érdekében, hogy elkerüljük az MI véletlen vagy szándékos visszaélését, a Microsoft meghatározta a fontos [Felelős Mesterséges Intelligencia Alapelveket](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Az alábbi fogalmak képezik ezen alapelvek alapját:

* **Méltányosság** a *modell torzítások* fontos problémájához kapcsolódik, amelyeket az okozhat, ha torzított adatokat használunk a tanításhoz. Például, ha megpróbáljuk megjósolni egy személy szoftverfejlesztői állásának valószínűségét, a modell valószínűleg nagyobb előnyben részesíti a férfiakat - egyszerűen azért, mert a tanító adathalmaz valószínűleg férfi közönségre volt torzítva. Gondosan egyensúlyba kell hoznunk a tanító adatokat, és meg kell vizsgálnunk a modellt, hogy elkerüljük a torzításokat, és biztosítsuk, hogy a modell relevánsabb jellemzőket vegyen figyelembe.
* **Megbízhatóság és biztonság**. Természetüknél fogva az MI modellek hibázhatnak. Egy neurális hálózat valószínűségeket ad vissza, és ezt figyelembe kell vennünk a döntéshozatal során. Minden modellnek van bizonyos pontossága és visszahívási aránya, és ezt meg kell értenünk, hogy megelőzzük a hibás tanácsok által okozott károkat.
* **Adatvédelem és biztonság** bizonyos MI-specifikus vonatkozásokkal bír. Például, amikor adatokat használunk egy modell tanításához, ezek az adatok valamilyen módon "beépülnek" a modellbe. Egyrészt ez növeli a biztonságot és az adatvédelmet, másrészt emlékeznünk kell arra, hogy milyen adatokkal tanítottuk a modellt.
* **Befogadás** azt jelenti, hogy nem azért építünk MI-t, hogy helyettesítsük az embereket, hanem hogy kiegészítsük őket, és kreatívabbá tegyük a munkánkat. Ez a méltányossághoz is kapcsolódik, mert amikor alulreprezentált közösségekkel foglalkozunk, a legtöbb általunk gyűjtött adathalmaz valószínűleg torzított, és biztosítanunk kell, hogy ezek a közösségek is be legyenek vonva, és helyesen kezelje őket az MI.
* **Átláthatóság**. Ez magában foglalja annak biztosítását, hogy mindig egyértelmű legyen, ha MI-t használunk. Továbbá, ahol csak lehetséges, olyan MI rendszereket szeretnénk használni, amelyek *értelmezhetők*.
* **Elszámoltathatóság**. Amikor az MI modellek bizonyos döntéseket hoznak, nem mindig világos, hogy ki a felelős ezekért a döntésekért. Biztosítanunk kell, hogy megértsük, hol rejlik az MI döntéseinek felelőssége. A legtöbb esetben azt szeretnénk, hogy emberek is részt vegyenek a fontos döntések meghozatalában, hogy ténylegesen emberek legyenek elszámoltathatók.

## Eszközök a Felelős Mesterséges Intelligenciához

A Microsoft kifejlesztette a [Felelős MI Eszköztárat](https://github.com/microsoft/responsible-ai-toolbox), amely egy sor eszközt tartalmaz:

* Értelmezhetőségi Irányítópult (InterpretML)
* Méltányossági Irányítópult (FairLearn)
* Hibaanalízis Irányítópult
* Felelős MI Irányítópult, amely tartalmazza:

   - EconML - eszköz az Ok-okozati Elemzéshez, amely a "mi lenne, ha" kérdésekre összpontosít
   - DiCE - eszköz az Ellentétes Elemzéshez, amely lehetővé teszi, hogy lássuk, mely jellemzőket kell megváltoztatni a modell döntésének befolyásolásához

További információért az MI etikáról, kérlek látogasd meg [ezt a leckét](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) a Gépi Tanulás Tantervben, amely feladatokat is tartalmaz.

## Áttekintés és Önálló Tanulás

Végezd el ezt a [Tanulási Útvonalat](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste), hogy többet megtudj a felelős MI-ről.

## [Előadás utáni kvíz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.