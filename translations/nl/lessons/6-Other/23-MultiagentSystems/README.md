<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ddf651d7681b4449f9d09ea3b17911e",
  "translation_date": "2025-08-28T19:15:46+00:00",
  "source_file": "lessons/6-Other/23-MultiagentSystems/README.md",
  "language_code": "nl"
}
-->
# Multi-Agent Systemen

Een van de mogelijke manieren om intelligentie te bereiken is de zogenaamde **emergente** (of **synergetische**) benadering, die gebaseerd is op het feit dat het gecombineerde gedrag van veel relatief eenvoudige agenten kan resulteren in een algeheel complexer (of intelligenter) gedrag van het systeem als geheel. Theoretisch is dit gebaseerd op de principes van [Collectieve Intelligentie](https://en.wikipedia.org/wiki/Collective_intelligence), [Emergentisme](https://en.wikipedia.org/wiki/Global_brain) en [Evolutionaire Cybernetica](https://en.wikipedia.org/wiki/Global_brain), die stellen dat systemen op een hoger niveau een soort toegevoegde waarde verkrijgen wanneer ze op de juiste manier worden gecombineerd vanuit systemen op een lager niveau (het zogenaamde *principe van metasysteemtransitie*).

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/123)

De richting van **Multi-Agent Systemen** ontstond in AI in de jaren 1990 als reactie op de groei van het internet en gedistribueerde systemen. Een van de klassieke AI-handboeken, [Artificial Intelligence: A Modern Approach](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), richt zich op het perspectief van klassieke AI vanuit het oogpunt van multi-agent systemen.

Centraal in de multi-agent benadering staat het concept van een **Agent** - een entiteit die leeft in een bepaalde **omgeving**, die het kan waarnemen en waarop het kan handelen. Dit is een zeer brede definitie, en er kunnen veel verschillende soorten en classificaties van agenten zijn:

* Op basis van hun vermogen om te redeneren:
   - **Reactieve** agenten hebben meestal een eenvoudig verzoek-antwoord type gedrag
   - **Deliberatieve** agenten maken gebruik van een vorm van logisch redeneren en/of planningsmogelijkheden
* Op basis van de plaats waar de agent zijn code uitvoert:
   - **Statische** agenten werken op een toegewijde netwerknode
   - **Mobiele** agenten kunnen hun code verplaatsen tussen netwerknodes
* Op basis van hun gedrag:
   - **Passieve agenten** hebben geen specifieke doelen. Dergelijke agenten kunnen reageren op externe prikkels, maar zullen zelf geen acties initiëren.
   - **Actieve agenten** hebben bepaalde doelen die ze nastreven
   - **Cognitieve agenten** betrekken complexe planning en redenering

Multi-agent systemen worden tegenwoordig gebruikt in een aantal toepassingen:

* In games maken veel niet-speler personages gebruik van een vorm van AI en kunnen ze worden beschouwd als intelligente agenten
* In videoproductie wordt het renderen van complexe 3D-scènes met menigten meestal gedaan met behulp van multi-agent simulatie
* In systeemmodellering wordt de multi-agent benadering gebruikt om het gedrag van een complex model te simuleren. Bijvoorbeeld, de multi-agent benadering is succesvol gebruikt om de verspreiding van COVID-19 wereldwijd te voorspellen. Een soortgelijke benadering kan worden gebruikt om verkeer in een stad te modelleren en te zien hoe het reageert op veranderingen in verkeersregels.
* In complexe automatiseringssystemen kan elk apparaat functioneren als een onafhankelijke agent, wat het hele systeem minder monolithisch en robuuster maakt.

We zullen niet veel tijd besteden aan het diep ingaan op multi-agent systemen, maar we bekijken één voorbeeld van **Multi-Agent Modellering**.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) is een multi-agent modelleringsomgeving gebaseerd op een aangepaste versie van de [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) programmeertaal. Deze taal is ontwikkeld om programmeerconcepten aan kinderen te leren en stelt je in staat een agent genaamd **schildpad** te besturen, die kan bewegen en een spoor achterlaat. Dit maakt het mogelijk om complexe geometrische figuren te creëren, wat een zeer visuele manier is om het gedrag van een agent te begrijpen.

In NetLogo kunnen we veel schildpadden maken met het commando `create-turtles`. We kunnen vervolgens alle schildpadden opdrachten geven om acties uit te voeren (in het onderstaande voorbeeld - beweeg 10 punten vooruit):

```
create-turtles 10
ask turtles [
  forward 10
]
```

Natuurlijk is het niet interessant als alle schildpadden hetzelfde doen, dus we kunnen `ask` groepen schildpadden, bijvoorbeeld degenen die zich in de buurt van een bepaald punt bevinden. We kunnen ook schildpadden van verschillende *rassen* maken met het commando `breed [cats cat]`. Hier is `cat` de naam van een ras, en we moeten zowel het enkelvoud als het meervoud specificeren, omdat verschillende commando's verschillende vormen gebruiken voor duidelijkheid.

> ✅ We zullen niet ingaan op het leren van de NetLogo-taal zelf - je kunt de briljante [Beginner's Interactive NetLogo Dictionary](https://ccl.northwestern.edu/netlogo/bind/) raadplegen als je meer wilt leren.

Je kunt [NetLogo downloaden](https://ccl.northwestern.edu/netlogo/download.shtml) en installeren om het uit te proberen.

### Modellenbibliotheek

Een geweldig aspect van NetLogo is dat het een bibliotheek bevat met werkende modellen die je kunt proberen. Ga naar **File → Models Library**, en je hebt veel categorieën modellen om uit te kiezen.

<img alt="NetLogo Models Library" src="images/NetLogo-ModelLib.png" width="60%"/>

> Een screenshot van de modellenbibliotheek door Dmitry Soshnikov

Je kunt een van de modellen openen, bijvoorbeeld **Biology → Flocking**.

### Hoofdprincipes

Na het openen van het model kom je op het hoofdscherm van NetLogo. Hier is een voorbeeldmodel dat de populatie van wolven en schapen beschrijft, gegeven eindige middelen (gras).

![NetLogo Main Screen](../../../../../translated_images/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.nl.png)

> Screenshot door Dmitry Soshnikov

Op dit scherm kun je zien:

* Het **Interface**-gedeelte dat bevat:
  - Het hoofdveld, waar alle agenten leven
  - Verschillende bedieningsknoppen: knoppen, schuifregelaars, enz.
  - Grafieken die je kunt gebruiken om parameters van de simulatie weer te geven
* Het **Code**-tabblad dat de editor bevat, waar je NetLogo-programma's kunt typen

In de meeste gevallen bevat de interface een **Setup**-knop, die de simulatiestatus initialiseert, en een **Go**-knop die de uitvoering start. Deze worden afgehandeld door de bijbehorende handlers in de code die er als volgt uitzien:

```
to go [
...
]
```

De wereld van NetLogo bestaat uit de volgende objecten:

* **Agenten** (schildpadden) die over het veld kunnen bewegen en iets kunnen doen. Je geeft agenten opdrachten met behulp van de syntaxis `ask turtles [...]`, en de code tussen de haakjes wordt uitgevoerd door alle agenten in *schildpadmodus*.
* **Patches** zijn vierkante gebieden van het veld waarop agenten leven. Je kunt verwijzen naar alle agenten op dezelfde patch, of je kunt patchkleuren en enkele andere eigenschappen wijzigen. Je kunt ook `ask patches` om iets te doen.
* **Observer** is een unieke agent die de wereld bestuurt. Alle knophandlers worden uitgevoerd in *observatormodus*.

> ✅ Het mooie van een multi-agent omgeving is dat de code die wordt uitgevoerd in schildpadmodus of patchmodus tegelijkertijd wordt uitgevoerd door alle agenten parallel. Dus door een beetje code te schrijven en het gedrag van een individuele agent te programmeren, kun je complex gedrag van het simulatiesysteem als geheel creëren.

### Flocking

Als voorbeeld van multi-agent gedrag bekijken we **[Flocking](https://en.wikipedia.org/wiki/Flocking_(behavior))**. Flocking is een complex patroon dat erg lijkt op hoe vogelzwermen vliegen. Als je ze ziet vliegen, kun je denken dat ze een soort collectief algoritme volgen, of dat ze een vorm van *collectieve intelligentie* bezitten. Echter, dit complexe gedrag ontstaat wanneer elke individuele agent (in dit geval een *vogel*) alleen andere agenten observeert binnen een korte afstand en drie eenvoudige regels volgt:

* **Uitlijning** - het stuurt naar de gemiddelde richting van naburige agenten
* **Samenhang** - het probeert te sturen naar de gemiddelde positie van buren (*langeafstands aantrekkingskracht*)
* **Scheiding** - wanneer het te dicht bij andere vogels komt, probeert het weg te bewegen (*korteafstands afstoting*)

Je kunt het flocking-model uitvoeren en het gedrag observeren. Je kunt ook parameters aanpassen, zoals *mate van scheiding* of het *zichtbereik*, dat bepaalt hoe ver elke vogel kan zien. Merk op dat als je het zichtbereik verlaagt tot 0, alle vogels blind worden en het flocking stopt. Als je de scheiding verlaagt tot 0, verzamelen alle vogels zich in een rechte lijn.

> ✅ Schakel over naar het **Code**-tabblad en bekijk waar de drie regels van flocking (uitlijning, samenhang en scheiding) in de code zijn geïmplementeerd. Let op hoe we alleen verwijzen naar die agenten die in zicht zijn.

### Andere modellen om te bekijken

Er zijn nog een paar interessante modellen waarmee je kunt experimenteren:

* **Art → Fireworks** laat zien hoe een vuurwerk kan worden beschouwd als collectief gedrag van individuele vuurstromen
* **Social Science → Traffic Basic** en **Social Science → Traffic Grid** tonen het model van stadsverkeer in een 1D- en 2D-raster met of zonder verkeerslichten. Elke auto in de simulatie volgt de volgende regels:
   - Als de ruimte voor hem leeg is - versnellen (tot een bepaalde maximale snelheid)
   - Als het het obstakel voor zich ziet - remmen (en je kunt aanpassen hoe ver een bestuurder kan zien)
* **Social Science → Party** laat zien hoe mensen samenkomen tijdens een cocktailparty. Je kunt de combinatie van parameters vinden die leidt tot de snelste toename van de groepsgeluk.

Zoals je kunt zien uit deze voorbeelden, kunnen multi-agent simulaties een nuttige manier zijn om het gedrag van een complex systeem te begrijpen dat bestaat uit individuen die dezelfde of vergelijkbare logica volgen. Het kan ook worden gebruikt om virtuele agenten te besturen, zoals [NPC's](https://en.wikipedia.org/wiki/NPC) in computerspellen, of agenten in 3D-geanimeerde werelden.

## Deliberatieve Agenten

De hierboven beschreven agenten zijn heel eenvoudig en reageren op veranderingen in de omgeving met behulp van een soort algoritme. Als zodanig zijn ze **reactieve agenten**. Soms kunnen agenten echter redeneren en hun acties plannen, in welk geval ze **deliberatieve** agenten worden genoemd.

Een typisch voorbeeld zou een persoonlijke agent zijn die een instructie van een mens ontvangt om een vakantie te boeken. Stel dat er veel agenten op het internet leven die daarbij kunnen helpen. Het moet dan contact opnemen met andere agenten om te zien welke vluchten beschikbaar zijn, wat de hotelprijzen zijn voor verschillende datums, en proberen de beste prijs te onderhandelen. Wanneer het vakantieplan compleet is en bevestigd door de eigenaar, kan het doorgaan met boeken.

Om dit te doen, moeten agenten **communiceren**. Voor succesvolle communicatie hebben ze nodig:

* Sommige **standaardtalen om kennis uit te wisselen**, zoals [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) en [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Deze talen zijn ontworpen op basis van [Speech Act theory](https://en.wikipedia.org/wiki/Speech_act).
* Deze talen moeten ook enkele **protocollen voor onderhandelingen** bevatten, gebaseerd op verschillende **veilingtypes**.
* Een **gemeenschappelijke ontologie** om te gebruiken, zodat ze naar dezelfde concepten verwijzen en hun semantiek begrijpen
* Een manier om te **ontdekken** wat verschillende agenten kunnen doen, ook gebaseerd op een soort ontologie

Deliberatieve agenten zijn veel complexer dan reactieve, omdat ze niet alleen reageren op veranderingen in de omgeving, maar ook acties moeten kunnen *initiëren*. Een van de voorgestelde architecturen voor deliberatieve agenten is de zogenaamde Belief-Desire-Intention (BDI) agent:

* **Geloofsovertuigingen** vormen een set kennis over de omgeving van een agent. Het kan worden gestructureerd als een kennisbank of een set regels die een agent kan toepassen op een specifieke situatie in de omgeving.
* **Verlangens** definiëren wat een agent wil doen, d.w.z. zijn doelen. Bijvoorbeeld, het doel van de persoonlijke assistent-agent hierboven is om een reis te boeken, en het doel van een hotelagent is om winst te maximaliseren.
* **Intenties** zijn specifieke acties die een agent plant om zijn doelen te bereiken. Acties veranderen meestal de omgeving en veroorzaken communicatie met andere agenten.

Er zijn enkele platforms beschikbaar voor het bouwen van multi-agent systemen, zoals [JADE](https://jade.tilab.com/). [Dit artikel](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) bevat een overzicht van multi-agent platforms, samen met een korte geschiedenis van multi-agent systemen en hun verschillende gebruiksscenario's.

## Conclusie

Multi-agent systemen kunnen zeer verschillende vormen aannemen en worden gebruikt in veel verschillende toepassingen. 
Ze richten zich allemaal op het eenvoudigere gedrag van een individuele agent en bereiken complexer gedrag van het algehele systeem door **synergetisch effect**.

## 🚀 Uitdaging

Breng deze les naar de echte wereld en probeer een multi-agent systeem te conceptualiseren dat een probleem kan oplossen. Wat zou een multi-agent systeem bijvoorbeeld moeten doen om een schoolbusroute te optimaliseren? Hoe zou het kunnen werken in een bakkerij?

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/223)

## Review & Zelfstudie

Bekijk het gebruik van dit type systeem in de industrie. Kies een domein zoals productie of de videogame-industrie en ontdek hoe multi-agent systemen kunnen worden gebruikt om unieke problemen op te lossen.

## [NetLogo Opdracht](assignment.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.