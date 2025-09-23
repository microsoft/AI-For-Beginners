<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7d097f7fda9166ead615e4c34552381b",
  "translation_date": "2025-09-23T14:06:27+00:00",
  "source_file": "lessons/2-Symbolic/README.md",
  "language_code": "sk"
}
-->
# Reprezentácia znalostí a expertné systémy

![Zhrnutie obsahu Symbolickej AI](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.sk.png)

> Sketchnote od [Tomomi Imura](https://twitter.com/girlie_mac)

Hľadanie umelej inteligencie je založené na snahe o získanie znalostí, aby sme dokázali chápať svet podobne ako ľudia. Ale ako to dosiahnuť?

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/3)

V začiatkoch AI bol populárny prístup zhora nadol pri vytváraní inteligentných systémov (diskutovaný v predchádzajúcej lekcii). Myšlienka spočívala v extrakcii znalostí od ľudí do strojovo čitateľnej formy, ktorú by bolo možné automaticky použiť na riešenie problémov. Tento prístup bol založený na dvoch hlavných ideách:

* Reprezentácia znalostí
* Odvodzovanie

## Reprezentácia znalostí

Jedným z dôležitých konceptov v Symbolickej AI sú **znalosti**. Je dôležité rozlišovať znalosti od *informácií* alebo *údajov*. Napríklad, môžeme povedať, že knihy obsahujú znalosti, pretože ich štúdiom sa môžeme stať odborníkmi. Avšak to, čo knihy obsahujú, sa v skutočnosti nazýva *údaje*, a čítaním kníh a integráciou týchto údajov do nášho modelu sveta ich premieňame na znalosti.

> ✅ **Znalosti** sú niečo, čo máme v hlave a predstavujú naše chápanie sveta. Získavajú sa aktívnym procesom **učenia**, ktorý integruje kúsky informácií, ktoré dostávame, do nášho aktívneho modelu sveta.

Najčastejšie znalosti striktne nedefinujeme, ale zosúladíme ich s inými príbuznými konceptmi pomocou [DIKW pyramídy](https://en.wikipedia.org/wiki/DIKW_pyramid). Obsahuje nasledujúce koncepty:

* **Údaje** sú niečo, čo je reprezentované na fyzických médiách, ako je písaný text alebo hovorené slová. Údaje existujú nezávisle od ľudí a môžu sa medzi nimi prenášať.
* **Informácie** sú spôsob, akým interpretujeme údaje v našej hlave. Napríklad, keď počujeme slovo *počítač*, máme určitú predstavu o tom, čo to je.
* **Znalosti** sú informácie integrované do nášho modelu sveta. Napríklad, keď sa naučíme, čo je počítač, začneme mať predstavy o tom, ako funguje, koľko stojí a na čo sa dá použiť. Táto sieť vzájomne prepojených konceptov tvorí naše znalosti.
* **Múdrosť** je ešte jedna úroveň nášho chápania sveta a predstavuje *meta-znalosti*, napríklad predstavu o tom, ako a kedy by sa mali znalosti používať.

<img src="images/DIKW_Pyramid.png" width="30%"/>

*Obrázok [z Wikipédie](https://commons.wikimedia.org/w/index.php?curid=37705247), od Longlivetheux - Vlastná práca, CC BY-SA 4.0*

Problém **reprezentácie znalostí** teda spočíva v nájdení efektívneho spôsobu, ako reprezentovať znalosti v počítači vo forme údajov, aby boli automaticky použiteľné. To možno vnímať ako spektrum:

![Spektrum reprezentácie znalostí](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.sk.png)

> Obrázok od [Dmitry Soshnikov](http://soshnikov.com)

* Naľavo sú veľmi jednoduché typy reprezentácií znalostí, ktoré môžu byť efektívne použité počítačmi. Najjednoduchšou je algoritmická reprezentácia, keď sú znalosti reprezentované počítačovým programom. Toto však nie je najlepší spôsob reprezentácie znalostí, pretože nie je flexibilný. Znalosti v našej hlave sú často nealgoritmické.
* Napravo sú reprezentácie ako prirodzený text. Je to najvýkonnejšie, ale nemožno ho použiť na automatické odvodzovanie.

> ✅ Zamyslite sa na chvíľu nad tým, ako reprezentujete znalosti vo svojej hlave a premieňate ich na poznámky. Existuje konkrétny formát, ktorý vám pomáha pri zapamätaní?

## Klasifikácia počítačových reprezentácií znalostí

Rôzne metódy reprezentácie znalostí v počítači môžeme klasifikovať do nasledujúcich kategórií:

* **Sieťové reprezentácie** sú založené na tom, že v našej hlave máme sieť vzájomne prepojených konceptov. Môžeme sa pokúsiť reprodukovať rovnaké siete ako graf v počítači - tzv. **sémantická sieť**.

1. **Triplet objekt-atribút-hodnota** alebo **páry atribút-hodnota**. Keďže graf môže byť v počítači reprezentovaný ako zoznam uzlov a hrán, môžeme sémantickú sieť reprezentovať zoznamom tripletov obsahujúcich objekty, atribúty a hodnoty. Napríklad, vytvoríme nasledujúce triplety o programovacích jazykoch:

Objekt | Atribút | Hodnota
-------|---------|--------
Python | je | Nepísaný jazyk
Python | vynálezca | Guido van Rossum
Python | bloková syntax | odsadenie
Nepísaný jazyk | nemá | definície typov

> ✅ Zamyslite sa, ako by sa triplety mohli použiť na reprezentáciu iných typov znalostí.

2. **Hierarchické reprezentácie** zdôrazňujú fakt, že často vytvárame hierarchiu objektov vo svojej hlave. Napríklad vieme, že kanárik je vták a všetky vtáky majú krídla. Máme tiež predstavu o tom, akú farbu má kanárik zvyčajne a aká je jeho rýchlosť letu.

   - **Reprezentácia rámcov** je založená na reprezentácii každého objektu alebo triedy objektov ako **rámca**, ktorý obsahuje **sloty**. Sloty majú možné predvolené hodnoty, obmedzenia hodnôt alebo uložené procedúry, ktoré možno zavolať na získanie hodnoty slotu. Všetky rámce tvoria hierarchiu podobnú hierarchii objektov v objektovo orientovaných programovacích jazykoch.
   - **Scenáre** sú špeciálny druh rámcov, ktoré reprezentujú komplexné situácie, ktoré sa môžu rozvíjať v čase.

**Python**

Slot | Hodnota | Predvolená hodnota | Interval |
-----|---------|---------------------|----------|
Názov | Python | | |
Je-A | Nepísaný jazyk | | |
Premenná syntax | | CamelCase | |
Dĺžka programu | | | 5-5000 riadkov |
Bloková syntax | Odsadenie | | |

3. **Procedurálne reprezentácie** sú založené na reprezentácii znalostí zoznamom akcií, ktoré možno vykonať, keď nastane určitá podmienka.
   - Produkčné pravidlá sú if-then vyhlásenia, ktoré nám umožňujú robiť závery. Napríklad, lekár môže mať pravidlo hovoriace, že **AK** má pacient vysokú horúčku **ALEBO** vysokú hladinu C-reaktívneho proteínu v krvnom teste **POTOM** má zápal. Keď narazíme na jednu z podmienok, môžeme urobiť záver o zápale a potom ho použiť pri ďalšom odvodzovaní.
   - Algoritmy možno považovať za ďalšiu formu procedurálnej reprezentácie, hoci sa takmer nikdy nepoužívajú priamo v systémoch založených na znalostiach.

4. **Logika** bola pôvodne navrhnutá Aristotelom ako spôsob reprezentácie univerzálnych ľudských znalostí.
   - Predikátová logika ako matematická teória je príliš bohatá na to, aby bola výpočtovo realizovateľná, preto sa zvyčajne používa jej podmnožina, ako napríklad Hornove klauzuly používané v Prologu.
   - Deskriptívna logika je rodina logických systémov používaných na reprezentáciu a odvodzovanie hierarchií objektov distribuovaných reprezentácií znalostí, ako je *sémantický web*.

## Expertné systémy

Jedným z prvých úspechov symbolickej AI boli tzv. **expertné systémy** - počítačové systémy navrhnuté tak, aby fungovali ako odborník v obmedzenej oblasti problémov. Boli založené na **báze znalostí** extrahovanej od jedného alebo viacerých ľudských odborníkov a obsahovali **odvodzovací mechanizmus**, ktorý vykonával odvodzovanie na jej základe.

![Štruktúra človeka](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.sk.png) | ![Systém založený na znalostiach](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.sk.png)
---------------------------------------------|------------------------------------------------
Zjednodušená štruktúra ľudského nervového systému | Architektúra systému založeného na znalostiach

Expertné systémy sú postavené podobne ako systém ľudského odvodzovania, ktorý obsahuje **krátkodobú pamäť** a **dlhodobú pamäť**. Podobne v systémoch založených na znalostiach rozlišujeme nasledujúce komponenty:

* **Pamäť problému**: obsahuje znalosti o probléme, ktorý sa práve rieši, napr. teplotu alebo krvný tlak pacienta, či má zápal alebo nie, atď. Tieto znalosti sa tiež nazývajú **statické znalosti**, pretože obsahujú snímku toho, čo momentálne vieme o probléme - tzv. *stav problému*.
* **Báza znalostí**: reprezentuje dlhodobé znalosti o oblasti problémov. Je manuálne extrahovaná od ľudských odborníkov a nemení sa od konzultácie ku konzultácii. Pretože nám umožňuje navigovať z jedného stavu problému do druhého, nazýva sa tiež **dynamické znalosti**.
* **Odvodzovací mechanizmus**: orchestruje celý proces hľadania v priestore stavov problému, kladenie otázok používateľovi, keď je to potrebné. Je tiež zodpovedný za nájdenie správnych pravidiel, ktoré sa majú aplikovať na každý stav.

Ako príklad si vezmime nasledujúci expertný systém na určenie zvieraťa na základe jeho fyzických charakteristík:

![AND-OR strom](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.sk.png)

> Obrázok od [Dmitry Soshnikov](http://soshnikov.com)

Tento diagram sa nazýva **AND-OR strom** a je grafickou reprezentáciou množiny produkčných pravidiel. Nakreslenie stromu je užitočné na začiatku extrakcie znalostí od odborníka. Na reprezentáciu znalostí v počítači je však pohodlnejšie použiť pravidlá:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Môžete si všimnúť, že každá podmienka na ľavej strane pravidla a akcia sú v podstate tripletmi objekt-atribút-hodnota (OAV). **Pracovná pamäť** obsahuje množinu OAV tripletov, ktoré zodpovedajú problému, ktorý sa práve rieši. **Mechanizmus pravidiel** hľadá pravidlá, pre ktoré je podmienka splnená, a aplikuje ich, čím pridáva ďalší triplet do pracovnej pamäte.

> ✅ Nakreslite vlastný AND-OR strom na tému, ktorá vás zaujíma!

### Dopredné vs. spätné odvodzovanie

Proces opísaný vyššie sa nazýva **dopredné odvodzovanie**. Začína sa s určitými počiatočnými údajmi o probléme dostupnými v pracovnej pamäti a potom vykonáva nasledujúcu odvodzovaciu slučku:

1. Ak je cieľový atribút prítomný v pracovnej pamäti - zastavte a poskytnite výsledok
2. Vyhľadajte všetky pravidlá, ktorých podmienka je momentálne splnená - získajte **konfliktnú množinu** pravidiel.
3. Vykonajte **riešenie konfliktov** - vyberte jedno pravidlo, ktoré sa vykoná v tomto kroku. Môžu existovať rôzne stratégie riešenia konfliktov:
   - Vyberte prvé použiteľné pravidlo v báze znalostí
   - Vyberte náhodné pravidlo
   - Vyberte *špecifickejšie* pravidlo, t.j. to, ktoré spĺňa najviac podmienok na "ľavej strane" (LHS)
4. Aplikujte vybrané pravidlo a vložte nový kúsok znalostí do stavu problému
5. Opakujte od kroku 1.

Avšak v niektorých prípadoch môžeme chcieť začať s prázdnymi znalosťami o probléme a klásť otázky, ktoré nám pomôžu dospieť k záveru. Napríklad pri diagnostike pacienta zvyčajne nevykonávame všetky lekárske analýzy vopred pred začatím diagnostiky. Skôr chceme vykonať analýzy, keď je potrebné urobiť rozhodnutie.

Tento proces možno modelovať pomocou **spätného odvodzovania**. Je riadený **cieľom** - hodnotou atribútu, ktorú sa snažíme nájsť:

1. Vyberte všetky pravidlá, ktoré môžu poskytnúť hodnotu cieľa (t.j. s cieľom na RHS ("pravej strane")) - konfliktná množina
1. Ak neexistujú žiadne pravidlá pre tento atribút alebo existuje pravidlo hovoriace, že by sme mali hodnotu získať od používateľa - opýtajte sa na ňu, inak:
1. Použite stratégiu riešenia konfliktov na výber jedného pravidla, ktoré použijeme ako *hypotézu* - pokúsime sa ju dokázať
1. Rekurzívne opakujte proces pre všetky atribúty na LHS pravidla, pokúšajúc sa ich dokázať ako ciele
1. Ak proces kedykoľvek zlyhá - použite iné pravidlo v kroku 3.

> ✅ V ktorých situáciách je dopredné odvodzovanie vhodnejšie? A čo spätné odvodzovanie?

### Implementácia expertných systémov

Expertné systémy možno implementovať rôznymi nástrojmi:

* Priame programovanie v nejakom vysokoúrovňovom programovacom jazyku. Toto nie je najlepší nápad, pretože hlavnou výhodou systému založeného na znalostiach je, že znalosti sú oddelené od odvodzovania a potenciálne by odborník na danú oblasť mal byť schopný písať pravidlá bez pochopenia detailov procesu odvodzovania.
* Použitie **shellu expertných systémov**, t.j. systému špeciálne navrhnutého na naplnenie znalostí pomocou nejakého jazyka reprezentácie znalostí.

## ✍️ Cvičenie: Odvodzovanie zvierat

Pozrite si [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) pre príklad implementácie expertného systému s dopredným a spätným odvodzovaním.

> **Poznámka**: Tento príklad je pomerne jednoduchý a iba poskytuje predstavu o tom, ako expertný systém vyzerá. Keď začnete vytvárať takýto systém, všimnete si určitú *inteligentnú* správanie až po dosiahnutí určitého počtu pravidiel, približne 200+. V určitom bode sa pravidlá stanú príliš zložité na to, aby ste ich všetky udržali v hlave, a vtedy sa môžete začať pýtať, prečo systém robí určité rozhodnutia. Avšak dôležitou charakteristikou systémov založených na znalostiach je, že vždy môžete *vysvetliť*, ako bolo každé rozhodnutie urobené.

## Ontológie a sémantický web

Na konci 20. storočia existovala iniciatíva použiť reprezentáciu znalostí na anotáciu internetových zdrojov, aby bolo možné nájsť zdroje, ktoré zodpovedajú veľmi špecifickým dotazom. Tento pohyb sa nazýval **sémantický web** a opieral sa o niekoľko konceptov:

- Špeciálna reprezentácia znalostí založená na **[deskriptívnej logike](https://en.wikipedia.org/wiki/Description_logic)** (DL). Je podobná reprezentácii rámcov, pretože buduje hierarchiu objektov s vlastnosťami, ale
- Rodina jazykov založených na XML na popis znalostí: RDF (Resource Description Framework), RDFS (RDF Schema), OWL (Ontology Web Language).

Základným konceptom v Sémantickom webe je koncept **ontológie**. Ontológia označuje explicitnú špecifikáciu problémovej oblasti pomocou formálnej reprezentácie znalostí. Najjednoduchšia ontológia môže byť len hierarchia objektov v problémovej oblasti, ale zložitejšie ontológie zahŕňajú pravidlá, ktoré môžu byť použité na inferenciu.

V sémantickom webe sú všetky reprezentácie založené na trojiciach. Každý objekt a každá relácia sú jednoznačne identifikované URI. Napríklad, ak chceme uviesť fakt, že tento AI Curriculum bol vytvorený Dmitrym Soshnikovom 1. januára 2022, tu sú trojice, ktoré môžeme použiť:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Tu `http://www.example.com/terms/creation-date` a `http://purl.org/dc/elements/1.1/creator` sú niektoré známe a univerzálne akceptované URI na vyjadrenie konceptov *tvorca* a *dátum vytvorenia*.

V zložitejšom prípade, ak chceme definovať zoznam tvorcov, môžeme použiť niektoré dátové štruktúry definované v RDF.

<img src="images/triplet-complex.png" width="40%"/>

> Diagramy vyššie od [Dmitry Soshnikov](http://soshnikov.com)

Pokrok v budovaní Sémantického webu bol do istej miery spomalený úspechom vyhľadávačov a techník spracovania prirodzeného jazyka, ktoré umožňujú extrahovať štruktúrované dáta z textu. Avšak v niektorých oblastiach stále existujú významné snahy o udržiavanie ontológií a znalostných báz. Niekoľko projektov, ktoré stoja za zmienku:

* [WikiData](https://wikidata.org/) je kolekcia strojovo čitateľných znalostných báz spojených s Wikipédiou. Väčšina dát je získaná z *InfoBoxov* Wikipédie, čo sú štruktúrované časti obsahu na stránkach Wikipédie. Môžete [dotazovať](https://query.wikidata.org/) WikiData pomocou SPARQL, špeciálneho dotazovacieho jazyka pre Sémantický web. Tu je ukážkový dotaz, ktorý zobrazuje najpopulárnejšie farby očí medzi ľuďmi:

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

* [DBpedia](https://www.dbpedia.org/) je ďalší projekt podobný WikiData.

> ✅ Ak chcete experimentovať s budovaním vlastných ontológií alebo otváraním existujúcich, existuje skvelý vizuálny editor ontológií nazývaný [Protégé](https://protege.stanford.edu/). Stiahnite si ho alebo ho použite online.

<img src="images/protege.png" width="70%"/>

*Webový editor Protégé otvorený s ontológiou rodiny Romanovcov. Screenshot od Dmitry Soshnikov*

## ✍️ Cvičenie: Ontológia rodiny

Pozrite si [FamilyOntology.ipynb](https://github.com/Ezana135/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) pre príklad použitia techník Sémantického webu na odvodzovanie rodinných vzťahov. Vezmeme rodokmeň reprezentovaný v bežnom formáte GEDCOM a ontológiu rodinných vzťahov a vytvoríme graf všetkých rodinných vzťahov pre danú skupinu jednotlivcov.

## Microsoft Concept Graph

Vo väčšine prípadov sú ontológie starostlivo vytvárané ručne. Avšak je tiež možné **získať** ontológie z neštruktúrovaných dát, napríklad z textov prirodzeného jazyka.

Jedným z takýchto pokusov bol projekt Microsoft Research, ktorý viedol k [Microsoft Concept Graph](https://blogs.microsoft.com/ai/microsoft-researchers-release-graph-that-helps-machines-conceptualize/?WT.mc_id=academic-77998-cacaste).

Je to veľká kolekcia entít zoskupených pomocou dedičného vzťahu `is-a`. Umožňuje odpovedať na otázky ako "Čo je Microsoft?" - odpoveďou môže byť niečo ako "spoločnosť s pravdepodobnosťou 0,87 a značka s pravdepodobnosťou 0,75".

Graf je dostupný buď ako REST API, alebo ako veľký stiahnuteľný textový súbor, ktorý obsahuje všetky páry entít.

## ✍️ Cvičenie: Concept Graph

Vyskúšajte notebook [MSConceptGraph.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb), aby ste videli, ako môžeme použiť Microsoft Concept Graph na zoskupenie spravodajských článkov do niekoľkých kategórií.

## Záver

Dnes sa AI často považuje za synonymum pre *strojové učenie* alebo *neurónové siete*. Avšak človek tiež vykazuje explicitné uvažovanie, čo je niečo, čo aktuálne neurónové siete nezvládajú. V reálnych projektoch sa explicitné uvažovanie stále používa na vykonávanie úloh, ktoré vyžadujú vysvetlenia alebo schopnosť kontrolovane meniť správanie systému.

## 🚀 Výzva

V notebooku Ontológia rodiny, ktorý je spojený s touto lekciou, je príležitosť experimentovať s inými rodinnými vzťahmi. Pokúste sa objaviť nové spojenia medzi ľuďmi v rodokmeni.

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ai/quiz/4)

## Prehľad a samostatné štúdium

Preskúmajte na internete oblasti, kde sa ľudia pokúšali kvantifikovať a kodifikovať znalosti. Pozrite sa na Bloomovu taxonómiu a vráťte sa v histórii, aby ste sa dozvedeli, ako sa ľudia snažili pochopiť svoj svet. Preskúmajte prácu Linnaeusa na vytvorení taxonómie organizmov a pozorujte, ako Dmitrij Mendelejev vytvoril spôsob na popis a zoskupenie chemických prvkov. Aké ďalšie zaujímavé príklady môžete nájsť?

**Úloha**: [Vytvorte ontológiu](assignment.md)

---

