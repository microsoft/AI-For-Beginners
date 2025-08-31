<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "98c5222ff9556b55223fed2337145e18",
  "translation_date": "2025-08-31T17:45:07+00:00",
  "source_file": "lessons/2-Symbolic/README.md",
  "language_code": "lt"
}
-->
# Žinių Atvaizdavimas ir Ekspertinės Sistemos

![Santrauka apie simbolinį AI turinį](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.lt.png)

> Sketchnote sukūrė [Tomomi Imura](https://twitter.com/girlie_mac)

Dirbtinio intelekto siekis grindžiamas žinių paieška, siekiant suprasti pasaulį taip, kaip tai daro žmonės. Bet kaip tai galima pasiekti?

## [Prieš paskaitos testas](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/102)

Ankstyvosiomis AI dienomis populiarus buvo aukštyn-nusileidžiantis požiūris į intelektualių sistemų kūrimą (aptartas ankstesnėje pamokoje). Idėja buvo išgauti žinias iš žmonių į mašinai suprantamą formą ir tada jas naudoti problemoms automatiškai spręsti. Šis požiūris buvo pagrįstas dviem pagrindinėmis idėjomis:

* Žinių atvaizdavimas
* Samprotavimas

## Žinių Atvaizdavimas

Vienas svarbiausių simbolinio AI konceptų yra **žinios**. Svarbu atskirti žinias nuo *informacijos* ar *duomenų*. Pavyzdžiui, galima sakyti, kad knygos turi žinių, nes jas studijuodami galime tapti ekspertais. Tačiau tai, ką knygos iš tikrųjų turi, vadinama *duomenimis*, o skaitydami knygas ir integruodami šiuos duomenis į savo pasaulio modelį, mes paverčiame juos žiniomis.

> ✅ **Žinios** yra tai, kas yra mūsų galvoje ir atspindi mūsų pasaulio supratimą. Jos gaunamos aktyvaus **mokymosi** proceso metu, kuris integruoja gautą informaciją į mūsų aktyvų pasaulio modelį.

Dažniausiai mes griežtai neapibrėžiame žinių, bet jas siejame su kitais susijusiais konceptais naudodami [DIKW piramidę](https://en.wikipedia.org/wiki/DIKW_pyramid). Ji apima šiuos konceptus:

* **Duomenys** yra tai, kas pateikiama fizinėje laikmenoje, pavyzdžiui, rašytinis tekstas ar žodžiai. Duomenys egzistuoja nepriklausomai nuo žmonių ir gali būti perduodami tarp jų.
* **Informacija** yra tai, kaip mes interpretuojame duomenis savo galvoje. Pavyzdžiui, išgirdę žodį *kompiuteris*, mes turime tam tikrą supratimą, kas tai yra.
* **Žinios** yra informacija, integruota į mūsų pasaulio modelį. Pavyzdžiui, kai išmokstame, kas yra kompiuteris, mes pradedame turėti tam tikrų idėjų apie tai, kaip jis veikia, kiek jis kainuoja ir kam jis gali būti naudojamas. Šis tarpusavyje susijusių konceptų tinklas sudaro mūsų žinias.
* **Išmintis** yra dar vienas mūsų pasaulio supratimo lygis, kuris atspindi *metažinias*, pvz., supratimą, kaip ir kada žinios turėtų būti naudojamos.

*Image [iš Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), Autorius Longlivetheux - Nuosavas darbas, CC BY-SA 4.0*

Taigi, **žinių atvaizdavimo** problema yra rasti efektyvų būdą atvaizduoti žinias kompiuteryje duomenų forma, kad jos būtų automatiškai naudojamos. Tai galima įsivaizduoti kaip spektrą:

![Žinių atvaizdavimo spektras](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.lt.png)

> Vaizdas sukurtas [Dmitry Soshnikov](http://soshnikov.com)

* Kairėje yra labai paprasti žinių atvaizdavimo tipai, kuriuos kompiuteriai gali efektyviai naudoti. Paprasčiausias yra algoritminis, kai žinios atvaizduojamos kompiuterio programa. Tačiau tai nėra geriausias būdas atvaizduoti žinias, nes jis nėra lankstus. Žinios mūsų galvoje dažnai nėra algoritminės.
* Dešinėje yra tokie atvaizdavimai kaip natūralus tekstas. Tai yra galingiausias būdas, tačiau jis negali būti naudojamas automatiniam samprotavimui.

> ✅ Pagalvokite minutę, kaip jūs atvaizduojate žinias savo galvoje ir paverčiate jas užrašais. Ar yra tam tikras formatas, kuris jums padeda geriau įsiminti?

## Kompiuterinių Žinių Atvaizdavimo Klasifikavimas

Galime klasifikuoti skirtingus kompiuterinių žinių atvaizdavimo metodus į šias kategorijas:

* **Tinklo atvaizdavimai** yra pagrįsti tuo, kad mūsų galvoje yra tarpusavyje susijusių konceptų tinklas. Galime pabandyti atkurti tuos pačius tinklus kaip grafą kompiuteryje - vadinamąjį **semantinį tinklą**.

1. **Objekto-atributo-reikšmės trejetai** arba **atributo-reikšmės poros**. Kadangi grafas gali būti atvaizduotas kompiuteryje kaip mazgų ir briaunų sąrašas, semantinį tinklą galime atvaizduoti trejetų sąrašu, kuriame yra objektai, atributai ir reikšmės. Pavyzdžiui, galime sudaryti šiuos trejetus apie programavimo kalbas:

Objektas | Atributas | Reikšmė
---------|-----------|--------
Python | yra | Netipizuota kalba
Python | sukūrė | Guido van Rossum
Python | blokų sintaksė | įtrauka
Netipizuota kalba | neturi | tipų apibrėžimų

> ✅ Pagalvokite, kaip trejetai gali būti naudojami kitų tipų žinioms atvaizduoti.

2. **Hierarchiniai atvaizdavimai** pabrėžia faktą, kad mes dažnai kuriame objektų hierarchiją savo galvoje. Pavyzdžiui, mes žinome, kad kanarėlė yra paukštis, o visi paukščiai turi sparnus. Taip pat turime tam tikrą supratimą, kokios spalvos dažniausiai būna kanarėlės ir koks jų skrydžio greitis.

   - **Kadrų atvaizdavimas** yra pagrįstas kiekvieno objekto ar objektų klasės atvaizdavimu kaip **kadro**, kuris turi **lizdus**. Lizdai turi galimas numatytąsias reikšmes, reikšmių apribojimus arba saugomas procedūras, kurios gali būti iškviestos norint gauti lizdo reikšmę. Visi kadrai sudaro hierarchiją, panašią į objektų hierarchiją objektinio programavimo kalbose.
   - **Scenarijai** yra specialūs kadrai, kurie atvaizduoja sudėtingas situacijas, galinčias vystytis laikui bėgant.

**Python**

Lizdas | Reikšmė | Numatytoji reikšmė | Intervalas |
-------|---------|--------------------|------------|
Pavadinimas | Python | | |
Yra | Netipizuota kalba | | |
Kintamojo rašymas | | CamelCase | |
Programos ilgis | | | 5-5000 eilučių |
Blokų sintaksė | Įtrauka | | |

3. **Procedūriniai atvaizdavimai** yra pagrįsti žinių atvaizdavimu kaip veiksmų sąrašu, kuris gali būti vykdomas, kai įvyksta tam tikra sąlyga.
   - Produkcijos taisyklės yra jei-tada teiginiai, leidžiantys daryti išvadas. Pavyzdžiui, gydytojas gali turėti taisyklę, kuri sako, kad **JEI** pacientas turi aukštą temperatūrą **ARBA** aukštą C-reaktyvaus baltymo lygį kraujo tyrime, **TADA** jis turi uždegimą. Kai susiduriame su viena iš sąlygų, galime padaryti išvadą apie uždegimą ir tada naudoti ją tolesniam samprotavimui.
   - Algoritmai gali būti laikomi kita procedūrinio atvaizdavimo forma, nors jie beveik niekada nenaudojami tiesiogiai žiniomis pagrįstose sistemose.

4. **Logika** buvo iš pradžių pasiūlyta Aristotelio kaip būdas atvaizduoti universalias žmogaus žinias.
   - Predikatų logika kaip matematinė teorija yra per daug turtinga, kad būtų skaičiuojama, todėl paprastai naudojamas jos poskyris, pvz., Horn sąlygos, naudojamos Prolog'e.
   - Aprašomoji logika yra loginių sistemų šeima, naudojama atvaizduoti ir samprotauti apie objektų hierarchijas paskirstytose žinių atvaizdavimo sistemose, tokiose kaip *semantinis tinklas*.

## Ekspertinės Sistemos

Vienas iš ankstyvųjų simbolinio AI pasiekimų buvo vadinamosios **ekspertinės sistemos** - kompiuterinės sistemos, sukurtos veikti kaip ekspertas tam tikroje ribotoje problemų srityje. Jos buvo pagrįstos **žinių baze**, išgauta iš vieno ar daugiau žmonių ekspertų, ir turėjo **išvadų variklį**, kuris atliko tam tikrą samprotavimą.

![Žmogaus architektūra](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.lt.png) | ![Žiniomis pagrįstos sistemos architektūra](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.lt.png)
---------------------------------------------|------------------------------------------------
Supaprastinta žmogaus nervų sistemos struktūra | Žiniomis pagrįstos sistemos architektūra

Ekspertinės sistemos yra sukurtos panašiai kaip žmogaus samprotavimo sistema, kuri turi **trumpalaikę atmintį** ir **ilgalaikę atmintį**. Panašiai žiniomis pagrįstose sistemose išskiriame šiuos komponentus:

* **Problemos atmintis**: joje saugomos žinios apie šiuo metu sprendžiamą problemą, pvz., paciento temperatūra ar kraujospūdis, ar jis turi uždegimą ir pan. Šios žinios taip pat vadinamos **statinėmis žiniomis**, nes jos apima tai, ką šiuo metu žinome apie problemą - vadinamąją *problemos būseną*.
* **Žinių bazė**: atspindi ilgalaikes žinias apie problemos sritį. Ji rankiniu būdu išgaunama iš žmonių ekspertų ir nesikeičia nuo vienos konsultacijos iki kitos. Kadangi ji leidžia pereiti iš vienos problemos būsenos į kitą, ji taip pat vadinama **dinaminėmis žiniomis**.
* **Išvadų variklis**: koordinuoja visą procesą, ieškant problemos būsenos erdvėje, užduodant klausimus vartotojui, kai reikia. Jis taip pat atsakingas už tinkamų taisyklių taikymą kiekvienai būsenai.

Kaip pavyzdį, pažiūrėkime į šią ekspertinę sistemą, kuri nustato gyvūną pagal jo fizines savybes:

![AND-OR medis](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.lt.png)

> Vaizdas sukurtas [Dmitry Soshnikov](http://soshnikov.com)

Ši diagrama vadinama **AND-OR medžiu**, ir tai yra grafinis produkcijos taisyklių rinkinys. Medžio piešimas yra naudingas pradiniame žinių išgavimo iš eksperto etape. Norint atvaizduoti žinias kompiuteryje, patogiau naudoti taisykles:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Pastebėsite, kad kiekviena sąlyga kairėje taisyklės pusėje ir veiksmas iš esmės yra objekto-atributo-reikšmės (OAR) trejetai. **Darbinė atmintis** saugo OAR trejetų rinkinį, atitinkantį šiuo metu sprendžiamą problemą. **Taisyklių variklis** ieško taisyklių, kurių sąlyga yra patenkinta, ir jas taiko, pridėdamas dar vieną trejetą į darbinę atmintį.

> ✅ Sukurkite savo AND-OR medį jums patinkančia tema!

### Priekinė ir Atgalinė Išvada

Aukščiau aprašytas procesas vadinamas **priekine išvada**. Jis prasideda nuo tam tikrų pradinių duomenų apie problemą, esančių darbinėje atmintyje, ir tada vykdo šį samprotavimo ciklą:

1. Jei tikslinis atributas yra darbinėje atmintyje - sustokite ir pateikite rezultatą
2. Ieškokite visų taisyklių, kurių sąlyga šiuo metu yra patenkinta - gaukite **konflikto rinkinį**.
3. Atlikite **konflikto sprendimą** - pasirinkite vieną taisyklę, kuri bus vykdoma šiame žingsnyje. Gali būti naudojamos skirtingos konflikto sprendimo strategijos:
   - Pasirinkti pirmą taikomą taisyklę žinių bazėje
   - Pasirinkti atsitiktinę taisyklę
   - Pasirinkti *konkretesnę* taisyklę, t. y. tą, kuri atitinka daugiausiai sąlygų kairėje pusėje (LHS)
4. Taikyti pasirinktą taisyklę ir įterpti naują žinių dalį į problemos būseną
5. Kartoti nuo 1 žingsnio.

Tačiau kai kuriais atvejais galime norėti pradėti nuo tuščios žinių bazės apie problemą ir užduoti klausimus, kurie padės mums pasiekti išvadą. Pavyzdžiui, atliekant medicininę diagnozę, mes paprastai neatliekame visų medicininių tyrimų iš anksto prieš pradedant diagnozuoti pacientą. Vietoj to, mes norime atlikti tyrimus, kai reikia priimti sprendimą.

Šis procesas gali būti modeliuojamas naudojant **atgalinę išvadą**. Ji yra orientuota į **tikslą** - atributų reikšmę, kurią siekiame rasti:

1. Pasirinkite visas taisykles, kurios gali suteikti mums tikslinę reikšmę (t. y. su tikslu dešinėje pusėje (RHS)) - konfliktų rinkinys
1. Jei nėra taisyklių šiam atributui arba yra taisyklė, sakanti, kad reikšmę turėtume paklausti vartotojo - paklauskite jos, kitaip:
1. Naudokite konflikto sprendimo strategiją, kad pasirinktumėte vieną taisyklę, kurią naudosime kaip *hipotezę* - bandysime ją įrodyti
1. Rekursyviai kartokite procesą visiems atributams kairėje taisyklės pusėje, bandydami juos įrodyti kaip tikslus
1. Jei bet kuriuo metu procesas nepavyksta - naudokite kitą taisyklę 3 žingsnyje.

> ✅ Kokiose situacijose priekinei išvadai labiau tinka? O kaip dėl atgalinės išvados?

### Ekspertinių Sistemų Įgyvendinimas

Ekspertinės sistemos gali būti įgyvendinamos naudojant skirtingus įrankius:

* Jas programuojant tiesiogiai kokia nors aukšto lygio programavimo kalba. Tai nėra geriausia idėja, nes pagrindinis žiniomis pagrįstos sistemos privalumas yra tas, kad žinios yra atskirtos nuo išvadų, ir potencialiai problemos srities ekspertas turėtų galėti rašyti taisykles, nesuprasdamas išvadų proceso detalių.
* Naudojant **ekspertinių sistemų apvalkalą**, t. y. sistemą, specialiai sukurtą užpildyti žiniomis naudojant tam tikrą žinių atvaizdavimo kalbą.

## ✍️ Užduotis: Gyvūnų Išvada

Žr. [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) kaip pavyzdį, kaip įgyvendinti priekinių ir atgalinių išvadų ekspertinę sistemą.
> **Pastaba**: Šis pavyzdys yra gana paprastas ir tik suteikia idėją, kaip atrodo ekspertinė sistema. Kai pradėsite kurti tokią sistemą, pastebėsite tam tikrą *intelektualų* elgesį tik pasiekę tam tikrą taisyklių skaičių, maždaug 200+. Tam tikru momentu taisyklės tampa per sudėtingos, kad visas jas būtų galima išlaikyti galvoje, ir tada galite pradėti stebėtis, kodėl sistema priima tam tikrus sprendimus. Tačiau svarbi žinių pagrindu veikiančių sistemų savybė yra ta, kad visada galite *paaiškinti*, kaip buvo priimtas bet kuris sprendimas.
## Ontologijos ir Semantinis Tinklas

XX amžiaus pabaigoje atsirado iniciatyva naudoti žinių reprezentaciją interneto ištekliams žymėti, kad būtų galima rasti išteklius, atitinkančius labai specifinius užklausų kriterijus. Ši iniciatyva buvo pavadinta **Semantiniu Tinklu**, ir ji rėmėsi keliais pagrindiniais principais:

- Speciali žinių reprezentacija, pagrįsta **[aprašomosiomis logikomis](https://en.wikipedia.org/wiki/Description_logic)** (DL). Ji panaši į rėminę žinių reprezentaciją, nes kuria objektų hierarchiją su savybėmis, tačiau turi formalią loginę semantiką ir išvedimo galimybes. Yra visa DL šeima, kuri balansuoja tarp išraiškingumo ir algoritminio išvedimo sudėtingumo.
- Paskirstyta žinių reprezentacija, kur visi konceptai yra reprezentuojami globaliais URI identifikatoriais, leidžiančiais kurti žinių hierarchijas, apimančias visą internetą.
- XML pagrindu sukurtų kalbų šeima žinių aprašymui: RDF (Resursų Aprašymo Struktūra), RDFS (RDF Schema), OWL (Ontologijų Tinklo Kalba).

Pagrindinė Semantinio Tinklo sąvoka yra **Ontologija**. Ji reiškia aiškų problemos srities apibrėžimą naudojant formalią žinių reprezentaciją. Paprasčiausia ontologija gali būti tiesiog objektų hierarchija problemos srityje, tačiau sudėtingesnės ontologijos apima taisykles, kurios gali būti naudojamos išvedimui.

Semantiniame tinkle visos reprezentacijos yra pagrįstos tripletais. Kiekvienas objektas ir kiekvienas ryšys yra unikalus, identifikuojamas URI. Pavyzdžiui, jei norime nurodyti faktą, kad šis AI mokymo planas buvo sukurtas Dmitrijaus Soshnikovo 2022 m. sausio 1 d., štai tripletai, kuriuos galime naudoti:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Čia `http://www.example.com/terms/creation-date` ir `http://purl.org/dc/elements/1.1/creator` yra gerai žinomi ir visuotinai priimti URI, skirti išreikšti *kūrėjo* ir *sukūrimo datos* sąvokas.

Sudėtingesniu atveju, jei norime apibrėžti kūrėjų sąrašą, galime naudoti kai kurias RDF apibrėžtas duomenų struktūras.

<img src="images/triplet-complex.png" width="40%"/>

> Aukščiau pateikti diagramų pavyzdžiai – [Dmitrijaus Soshnikovo](http://soshnikov.com)

Semantinio Tinklo kūrimo pažangą šiek tiek sulėtino paieškos sistemų ir natūralios kalbos apdorojimo technikų sėkmė, kurios leidžia išgauti struktūrizuotus duomenis iš teksto. Tačiau kai kuriose srityse vis dar dedamos reikšmingos pastangos ontologijoms ir žinių bazėms palaikyti. Keletas projektų, kuriuos verta paminėti:

* [WikiData](https://wikidata.org/) – tai mašininio skaitymo žinių bazių kolekcija, susijusi su Wikipedia. Dauguma duomenų yra išgaunami iš Wikipedia *InfoBox* – struktūrizuoto turinio dalių Wikipedia puslapiuose. Galite [užklausti](https://query.wikidata.org/) WikiData naudodami SPARQL – specialią užklausų kalbą Semantiniam Tinklui. Štai pavyzdinė užklausa, rodanti populiariausias žmonių akių spalvas:

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

* [DBpedia](https://www.dbpedia.org/) – dar viena iniciatyva, panaši į WikiData.

> ✅ Jei norite eksperimentuoti kuriant savo ontologijas arba atidarant esamas, yra puikus vizualinis ontologijų redaktorius, vadinamas [Protégé](https://protege.stanford.edu/). Atsisiųskite jį arba naudokite internetu.

<img src="images/protege.png" width="70%"/>

*Web Protégé redaktorius atidarytas su Romanovų šeimos ontologija. Dmitrijaus Soshnikovo ekrano kopija*

## ✍️ Užduotis: Šeimos Ontologija

Žr. [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) pavyzdį, kaip naudoti Semantinio Tinklo technikas šeimos ryšiams analizuoti. Mes naudosime šeimos medį, pateiktą įprastu GEDCOM formatu, ir šeimos ryšių ontologiją, kad sukurtume visų šeimos ryšių grafą tam tikram asmenų rinkiniui.

## Microsoft Konceptų Grafas

Daugeliu atvejų ontologijos yra kruopščiai kuriamos rankiniu būdu. Tačiau taip pat galima **išgauti** ontologijas iš nestruktūrizuotų duomenų, pavyzdžiui, iš natūralios kalbos tekstų.

Vienas tokių bandymų buvo atliktas Microsoft Research ir rezultatas – [Microsoft Konceptų Grafas](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste).

Tai didelė subjektų kolekcija, sugrupuota naudojant `is-a` paveldėjimo ryšį. Ji leidžia atsakyti į klausimus, tokius kaip „Kas yra Microsoft?“ – atsakymas būtų kažkas panašaus į „kompanija su 0.87 tikimybe ir prekės ženklas su 0.75 tikimybe“.

Grafas yra prieinamas kaip REST API arba kaip didelis atsisiunčiamas tekstinis failas, kuriame išvardyti visi subjektų poros.

## ✍️ Užduotis: Konceptų Grafas

Išbandykite [MSConceptGraph.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb) užrašų knygelę, kad pamatytumėte, kaip galime naudoti Microsoft Konceptų Grafą naujienų straipsniams suskirstyti į kelias kategorijas.

## Išvada

Šiandien AI dažnai laikomas sinonimu *Mašininio Mokymosi* arba *Neuroninių Tinklų*. Tačiau žmogus taip pat demonstruoja aiškų samprotavimą, kuris šiuo metu nėra apdorojamas neuroninių tinklų. Realiuose projektuose aiškus samprotavimas vis dar naudojamas užduotims atlikti, kurioms reikia paaiškinimų arba galimybės kontroliuojamai keisti sistemos elgesį.

## 🚀 Iššūkis

Šeimos Ontologijos užrašų knygelėje, susijusioje su šia pamoka, yra galimybė eksperimentuoti su kitais šeimos ryšiais. Pabandykite atrasti naujus ryšius tarp žmonių šeimos medyje.

## [Po paskaitos testas](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/202)

## Apžvalga ir savarankiškas mokymasis

Atlikite tyrimus internete, kad sužinotumėte sritis, kuriose žmonės bandė kiekybiškai įvertinti ir kodifikuoti žinias. Pažvelkite į Bloom'o Taksonomiją ir grįžkite į istoriją, kad sužinotumėte, kaip žmonės bandė suprasti savo pasaulį. Išanalizuokite Linėjaus darbą, kuriant organizmų taksonomiją, ir stebėkite, kaip Dmitrijus Mendelejevas sukūrė būdą cheminiams elementams aprašyti ir grupuoti. Kokius kitus įdomius pavyzdžius galite rasti?

**Užduotis**: [Sukurkite Ontologiją](assignment.md)

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.