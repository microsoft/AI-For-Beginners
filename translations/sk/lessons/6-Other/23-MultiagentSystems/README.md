# Multi-agentné systémy

Jedným z možných spôsobov dosiahnutia inteligencie je tzv. **emergentný** (alebo **synergetický**) prístup, ktorý je založený na skutočnosti, že kombinované správanie mnohých relatívne jednoduchých agentov môže viesť k celkovo zložitejšiemu (alebo inteligentnejšiemu) správaniu systému ako celku. Teoreticky je to založené na princípoch [kolektívnej inteligencie](https://en.wikipedia.org/wiki/Collective_intelligence), [emergentizmu](https://en.wikipedia.org/wiki/Global_brain) a [evolučnej kybernetiky](https://en.wikipedia.org/wiki/Global_brain), ktoré tvrdia, že systémy na vyššej úrovni získavajú určitú pridanú hodnotu, keď sú správne kombinované zo systémov na nižšej úrovni (tzv. *princíp prechodu metasystému*).

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/45)

Smer **multi-agentných systémov** sa objavil v AI v 90. rokoch ako reakcia na rast internetu a distribuovaných systémov. Jedna z klasických učebníc AI, [Artificial Intelligence: A Modern Approach](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), sa zameriava na pohľad klasickej AI z perspektívy multi-agentných systémov.

Ústredným pojmom multi-agentného prístupu je **agent** – entita, ktorá žije v určitom **prostredí**, ktoré dokáže vnímať a ovplyvňovať. Toto je veľmi široká definícia a existuje mnoho rôznych typov a klasifikácií agentov:

* Podľa ich schopnosti uvažovať:
   - **Reaktívni** agenti majú zvyčajne jednoduché správanie typu požiadavka-odpoveď
   - **Deliberatívni** agenti využívajú určitý druh logického uvažovania a/alebo plánovacích schopností
* Podľa miesta, kde agent vykonáva svoj kód:
   - **Statickí** agenti pracujú na vyhradenom sieťovom uzle
   - **Mobilní** agenti môžu presúvať svoj kód medzi sieťovými uzlami
* Podľa ich správania:
   - **Pasívni agenti** nemajú konkrétne ciele. Takíto agenti môžu reagovať na vonkajšie podnety, ale sami nebudú iniciovať žiadne akcie.
   - **Aktívni agenti** majú určité ciele, ktoré sledujú
   - **Kognitívni agenti** zahŕňajú komplexné plánovanie a uvažovanie

Multi-agentné systémy sa dnes používajú v mnohých aplikáciách:

* V hrách mnoho postáv, ktoré nie sú hráčmi, využíva určitý druh AI a možno ich považovať za inteligentných agentov
* Pri produkcii videa sa renderovanie zložitých 3D scén, ktoré zahŕňajú davy, zvyčajne vykonáva pomocou simulácie multi-agentov
* Pri modelovaní systémov sa multi-agentný prístup používa na simuláciu správania zložitého modelu. Napríklad multi-agentný prístup bol úspešne použitý na predpovedanie šírenia ochorenia COVID-19 na celom svete. Podobný prístup možno použiť na modelovanie dopravy v meste a sledovanie reakcií na zmeny dopravných pravidiel.
* V komplexných automatizačných systémoch môže každé zariadenie fungovať ako nezávislý agent, čo robí celý systém menej monolitickým a robustnejším.

Nebudeme sa podrobne zaoberať multi-agentnými systémami, ale pozrieme sa na jeden príklad **modelovania multi-agentov**.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) je prostredie na modelovanie multi-agentov založené na upravenej verzii programovacieho jazyka [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)). Tento jazyk bol vyvinutý na výučbu programovacích konceptov pre deti a umožňuje ovládať agenta nazývaného **korytnačka**, ktorý sa môže pohybovať a zanechávať za sebou stopu. To umožňuje vytvárať zložité geometrické tvary, čo je veľmi vizuálny spôsob, ako pochopiť správanie agenta.

V NetLogo môžeme vytvoriť mnoho korytnačiek pomocou príkazu `create-turtles`. Potom môžeme všetkým korytnačkám prikázať vykonať nejaké akcie (v príklade nižšie - posunúť sa o 10 bodov dopredu):

```
create-turtles 10
ask turtles [
  forward 10
]
```

Samozrejme, nie je zaujímavé, keď všetky korytnačky robia to isté, takže môžeme `ask` skupiny korytnačiek, napr. tie, ktoré sú v blízkosti určitého bodu. Môžeme tiež vytvárať korytnačky rôznych *druhov* pomocou príkazu `breed [cats cat]`. Tu je `cat` názov druhu a musíme špecifikovať jednotné aj množné číslo, pretože rôzne príkazy používajú rôzne formy pre jasnosť.

> ✅ Nebudeme sa učiť jazyk NetLogo samotný - ak máte záujem dozvedieť sa viac, môžete navštíviť skvelý zdroj [Interaktívny slovník pre začiatočníkov NetLogo](https://ccl.northwestern.edu/netlogo/bind/).

Môžete si [stiahnuť](https://ccl.northwestern.edu/netlogo/download.shtml) a nainštalovať NetLogo, aby ste si ho vyskúšali.

### Knižnica modelov

Skvelou vecou na NetLogo je, že obsahuje knižnicu funkčných modelov, ktoré si môžete vyskúšať. Prejdite na **File &rightarrow; Models Library**, kde máte na výber mnoho kategórií modelov.

<img alt="NetLogo Models Library" src="../../../../../translated_images/sk/NetLogo-ModelLib.efe023afb4763c05.webp" width="60%"/>

> Snímka obrazovky knižnice modelov od Dmitry Soshnikov

Môžete otvoriť jeden z modelov, napríklad **Biology &rightarrow; Flocking**.

### Hlavné princípy

Po otvorení modelu sa dostanete na hlavnú obrazovku NetLogo. Tu je ukážkový model, ktorý popisuje populáciu vlkov a oviec, pričom zdroje (tráva) sú obmedzené.

![NetLogo Main Screen](../../../../../translated_images/sk/NetLogo-Main.32653711ec1a01b3.webp)

> Snímka obrazovky od Dmitry Soshnikov

Na tejto obrazovke môžete vidieť:

* Sekciu **Interface**, ktorá obsahuje:
  - Hlavné pole, kde žijú všetci agenti
  - Rôzne ovládacie prvky: tlačidlá, posuvníky atď.
  - Grafy, ktoré môžete použiť na zobrazenie parametrov simulácie
* Záložku **Code**, ktorá obsahuje editor, kde môžete písať program NetLogo

Vo väčšine prípadov bude rozhranie obsahovať tlačidlo **Setup**, ktoré inicializuje stav simulácie, a tlačidlo **Go**, ktoré spustí vykonávanie. Tieto sú spracované príslušnými obslužnými programami v kóde, ktoré vyzerajú takto:

```
to go [
...
]
```

Svet NetLogo pozostáva z nasledujúcich objektov:

* **Agenti** (korytnačky), ktorí sa môžu pohybovať po poli a niečo robiť. Agentom prikazujete pomocou syntaxe `ask turtles [...]`, pričom kód v zátvorkách vykonávajú všetci agenti v *režime korytnačky*.
* **Plochy** sú štvorcové oblasti poľa, na ktorých agenti žijú. Môžete sa odvolávať na všetkých agentov na rovnakej ploche alebo môžete meniť farby plôch a niektoré ďalšie vlastnosti. Môžete tiež `ask patches`, aby niečo vykonali.
* **Pozorovateľ** je jedinečný agent, ktorý ovláda svet. Všetky obslužné programy tlačidiel sa vykonávajú v *režime pozorovateľa*.

> ✅ Krása prostredia multi-agentov spočíva v tom, že kód, ktorý beží v režime korytnačky alebo v režime plochy, je vykonávaný všetkými agentmi súčasne paralelne. Tým, že napíšete trochu kódu a naprogramujete správanie jednotlivého agenta, môžete vytvoriť komplexné správanie simulačného systému ako celku.

### Flocking

Ako príklad správania multi-agentov si pozrime **[Flocking](https://en.wikipedia.org/wiki/Flocking_(behavior))**. Flocking je komplexný vzor, ktorý je veľmi podobný tomu, ako lietajú kŕdle vtákov. Pri ich pozorovaní môžete mať pocit, že nasledujú nejaký kolektívny algoritmus alebo že majú určitú formu *kolektívnej inteligencie*. Avšak toto komplexné správanie vzniká, keď každý jednotlivý agent (v tomto prípade *vták*) pozoruje iba niektorých agentov v krátkej vzdialenosti od seba a riadi sa tromi jednoduchými pravidlami:

* **Zarovnanie** - smeruje k priemernému smeru susedných agentov
* **Súdržnosť** - snaží sa smerovať k priemernej pozícii susedov (*dlhodobá príťažlivosť*)
* **Oddelenie** - keď sa dostane príliš blízko k iným vtákom, snaží sa vzdialiť (*krátkodobé odpudzovanie*)

Môžete spustiť príklad flockingu a pozorovať správanie. Môžete tiež upraviť parametre, ako napríklad *stupeň oddelenia* alebo *rozsah videnia*, ktorý definuje, ako ďaleko každý vták vidí. Všimnite si, že ak znížite rozsah videnia na 0, všetky vtáky sa stanú slepými a flocking sa zastaví. Ak znížite oddelenie na 0, všetky vtáky sa zhromaždia do jednej priamky.

> ✅ Prepnite na záložku **Code** a pozrite sa, kde sú tri pravidlá flockingu (zarovnanie, súdržnosť a oddelenie) implementované v kóde. Všimnite si, ako sa odvolávame iba na tých agentov, ktorí sú v dohľade.

### Ďalšie modely na preskúmanie

Existuje niekoľko ďalších zaujímavých modelov, ktoré môžete experimentovať:

* **Art &rightarrow; Fireworks** ukazuje, ako ohňostroj môže byť považovaný za kolektívne správanie jednotlivých prúdov ohňa
* **Social Science &rightarrow; Traffic Basic** a **Social Science &rightarrow; Traffic Grid** ukazujú model mestskej dopravy v 1D a 2D mriežke s alebo bez semaforov. Každé auto v simulácii nasleduje tieto pravidlá:
   - Ak je priestor pred ním prázdny - zrýchli (až do určitej maximálnej rýchlosti)
   - Ak vidí prekážku pred sebou - zabrzdí (a môžete upraviť, ako ďaleko vodič vidí)
* **Social Science &rightarrow; Party** ukazuje, ako sa ľudia zhromažďujú počas koktailovej párty. Môžete nájsť kombináciu parametrov, ktorá vedie k najrýchlejšiemu zvýšeniu šťastia skupiny.

Ako vidíte z týchto príkladov, simulácie multi-agentov môžu byť veľmi užitočným spôsobom na pochopenie správania zložitého systému pozostávajúceho z jednotlivcov, ktorí nasledujú rovnakú alebo podobnú logiku. Môže sa tiež použiť na ovládanie virtuálnych agentov, ako sú [NPC](https://en.wikipedia.org/wiki/NPC) v počítačových hrách alebo agenti v 3D animovaných svetoch.

## Deliberatívni agenti

Vyššie opísaní agenti sú veľmi jednoduchí, reagujú na zmeny v prostredí pomocou určitého algoritmu. Ako takí sú **reaktívni agenti**. Niekedy však agenti môžu uvažovať a plánovať svoje akcie, v takom prípade sa nazývajú **deliberatívni**.

Typickým príkladom by bol osobný agent, ktorý dostane pokyn od človeka rezervovať dovolenkový zájazd. Predpokladajme, že na internete žije mnoho agentov, ktorí mu môžu pomôcť. Mal by potom kontaktovať iných agentov, aby zistil, ktoré lety sú dostupné, aké sú ceny hotelov na rôzne dátumy, a pokúsiť sa vyjednať najlepšiu cenu. Keď je plán dovolenky dokončený a potvrdený majiteľom, môže pokračovať v rezervácii.

Na to, aby to dokázali, agenti potrebujú **komunikovať**. Pre úspešnú komunikáciu potrebujú:

* Niektoré **štandardné jazyky na výmenu znalostí**, ako [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) a [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Tieto jazyky sú navrhnuté na základe [teórie rečových aktov](https://en.wikipedia.org/wiki/Speech_act).
* Tieto jazyky by mali tiež obsahovať **protokoly na vyjednávanie**, založené na rôznych **typoch aukcií**.
* **Spoločnú ontológiu**, ktorú používajú, aby sa odvolávali na rovnaké koncepty s poznaním ich významu
* Spôsob, ako **objaviť**, čo rôzni agenti dokážu, tiež založený na určitom druhu ontológie

Deliberatívni agenti sú oveľa zložitejší ako reaktívni, pretože nereagujú len na zmeny v prostredí, ale mali by byť schopní aj *iniciovať* akcie. Jednou z navrhovaných architektúr pre deliberatívnych agentov je tzv. agent Belief-Desire-Intention (BDI):

* **Presvedčenia** tvoria súbor znalostí o prostredí agenta. Môže byť štruktúrovaný ako báza znalostí alebo súbor pravidiel, ktoré agent môže aplikovať na konkrétnu situáciu v prostredí.
* **Túžby** definujú, čo agent chce robiť, t. j. jeho ciele. Napríklad cieľom osobného asistenta vyššie je rezervovať zájazd a cieľom hotelového agenta je maximalizovať zisk.
* **Zámery** sú konkrétne akcie, ktoré agent plánuje na dosiahnutie svojich cieľov. Akcie zvyčajne menia prostredie a spôsobujú komunikáciu s inými agentmi.

Existujú niektoré platformy dostupné na budovanie multi-agentných systémov, ako napríklad [JADE](https://jade.tilab.com/). [Tento článok](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) obsahuje prehľad platforiem multi-agentov spolu s krátkou históriou multi-agentných systémov a ich rôznymi scenármi použitia.

## Záver

Multi-agentné systémy môžu mať veľmi rôzne formy a byť použité v mnohých rôznych aplikáciách. 
Všetky sa zameriavajú na jednoduchšie správanie jednotlivého agenta a dosahujú zložitejšie správanie celkového systému vďaka **synergetickému efektu**.

## 🚀 Výzva

Preneste túto lekciu do reálneho sveta a skúste konceptualizovať multi-agentný systém, ktorý dokáže vyriešiť problém. Čo by napríklad musel multi-agentný systém robiť, aby optimalizoval trasu školského autobusu? Ako by mohol fungovať v pekárni?

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ai/quiz/46)

## Prehľad a samostatné štúdium

Preskúmajte použitie tohto typu systému v priemysle. Vyberte si oblasť, ako je výroba alebo herný priemysel, a zistite, ako môžu multi-agentné systémy riešiť jedinečné problémy.

## [Úloha NetLogo](assignment.md)

---

