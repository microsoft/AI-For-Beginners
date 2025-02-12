# Kunskapsrepresentation och Expert System

![Sammanfattning av Symbolisk AI-innehåll](../../../../translated_images/ai-symbolic.715a30cb610411a6964d2e2f23f24364cb338a07cb4844c1f97084d366e586c3.sw.png)

> Sketchnote av [Tomomi Imura](https://twitter.com/girlie_mac)

Jakten på artificiell intelligens baseras på en strävan efter kunskap, för att förstå världen på ett sätt som liknar hur människor gör. Men hur går man tillväga för att uppnå detta?

## [Förläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/102)

I AI:s tidiga dagar var den topp-ner-ansatsen för att skapa intelligenta system (diskuterad i den föregående lektionen) populär. Idén var att extrahera kunskap från människor till en maskinläsbar form och sedan använda den för att automatiskt lösa problem. Denna metod baserades på två stora idéer:

* Kunskapsrepresentation
* Resonemang

## Kunskapsrepresentation

Ett av de viktiga koncepten inom Symbolisk AI är **kunskap**. Det är viktigt att särskilja kunskap från *information* eller *data*. Till exempel kan man säga att böcker innehåller kunskap, eftersom man kan studera böcker och bli expert. Vad böcker innehåller kallas faktiskt *data*, och genom att läsa böcker och integrera dessa data i vår världsmodell omvandlar vi dessa data till kunskap.

> ✅ **Kunskap** är något som finns i vårt huvud och representerar vår förståelse av världen. Den erhålls genom en aktiv **inlärnings**process, som integrerar bitar av information som vi får in i vår aktiva modell av världen.

Ofta definierar vi inte strikt kunskap, utan vi kopplar den till andra relaterade koncept med hjälp av [DIKW-pyramiden](https://en.wikipedia.org/wiki/DIKW_pyramid). Den innehåller följande koncept:

* **Data** är något som representeras i fysiska medier, såsom skriven text eller talade ord. Data existerar oberoende av människor och kan överföras mellan personer.
* **Information** är hur vi tolkar data i vårt huvud. Till exempel, när vi hör ordet *dator*, har vi en viss förståelse av vad det är.
* **Kunskap** är information som integreras i vår världsmodell. Till exempel, när vi väl har lärt oss vad en dator är, börjar vi få idéer om hur den fungerar, hur mycket den kostar och vad den kan användas till. Detta nätverk av relaterade koncept formar vår kunskap.
* **Visdom** är ytterligare en nivå av vår förståelse av världen, och den representerar *meta-kunskap*, dvs. en viss uppfattning om hur och när kunskapen bör användas.

<img src="images/DIKW_Pyramid.png" width="30%"/>

*Bild [från Wikipedia](https://commons.wikimedia.org/w/index.php?curid=37705247), av Longlivetheux - Eget arbete, CC BY-SA 4.0*

Således är problemet med **kunskapsrepresentation** att hitta ett effektivt sätt att representera kunskap inuti en dator i form av data, för att göra den automatiskt användbar. Detta kan ses som ett spektrum:

![Kunskapsrepresentationsspektrum](../../../../translated_images/knowledge-spectrum.b60df631852c0217e941485b79c9eee40ebd574f15f18609cec5758fcb384bf3.sw.png)

> Bild av [Dmitry Soshnikov](http://soshnikov.com)

* Till vänster finns mycket enkla typer av kunskapsrepresentationer som kan användas effektivt av datorer. Den enklaste är algoritmisk, när kunskap representeras av ett datorprogram. Detta är dock inte det bästa sättet att representera kunskap, eftersom det inte är flexibelt. Kunskap i vårt huvud är ofta icke-algoritmisk.
* Till höger finns representationer såsom naturlig text. Det är den mest kraftfulla, men kan inte användas för automatisk resonemang.

> ✅ Tänk en minut på hur du representerar kunskap i ditt huvud och omvandlar den till anteckningar. Finns det ett särskilt format som fungerar bra för dig för att underlätta retention?

## Klassificering av datorers kunskapsrepresentationer

Vi kan klassificera olika metoder för kunskapsrepresentation i datorer i följande kategorier:

* **Nätverksrepresentationer** baseras på det faktum att vi har ett nätverk av relaterade koncept i vårt huvud. Vi kan försöka återskapa samma nätverk som en graf inuti en dator - ett så kallat **semantiskt nätverk**.

1. **Objekt-Attribut-Värde-trippel** eller **attribut-värde-par**. Eftersom en graf kan representeras inuti en dator som en lista av noder och kanter, kan vi representera ett semantiskt nätverk med en lista av trippel, som innehåller objekt, attribut och värden. Till exempel bygger vi följande trippel om programmeringsspråk:

Objekt | Attribut | Värde
-------|-----------|------
Python | är | Otypad-Språk
Python | uppfunnen-av | Guido van Rossum
Python | block-syntax | indentering
Otypad-Språk | har inte | typdefinitioner

> ✅ Tänk på hur trippel kan användas för att representera andra typer av kunskap.

2. **Hierarkiska representationer** betonar det faktum att vi ofta skapar en hierarki av objekt i vårt huvud. Till exempel vet vi att en kanariefågel är en fågel, och alla fåglar har vingar. Vi har också en viss uppfattning om vilken färg en kanariefågel vanligtvis har, och vad deras flyghastighet är.

   - **Ramrepresentation** baseras på att representera varje objekt eller klass av objekt som en **ram** som innehåller **platser**. Platser har möjliga standardvärden, värdebegränsningar eller lagrade procedurer som kan anropas för att få värdet av en plats. Alla ramar bildar en hierarki liknande en objektshierarki i objektorienterade programmeringsspråk.
   - **Scenarier** är en speciell typ av ramar som representerar komplexa situationer som kan utvecklas över tid.

**Python**

Plats | Värde | Standardvärde | Intervall |
-----|-------|---------------|----------|
Namn | Python | | |
Är-En | Otypad-Språk | | |
Variabelnamn | | CamelCase | |
Programlängd | | | 5-5000 rader |
Blocksyntax | Indent | | |

3. **Procedurala representationer** baseras på att representera kunskap genom en lista av åtgärder som kan utföras när ett visst villkor inträffar.
   - Produktionsregler är om-så uttalanden som tillåter oss att dra slutsatser. Till exempel kan en läkare ha en regel som säger att **OM** en patient har hög feber **ELLER** hög nivå av C-reaktivt protein i blodprovet **SÅ** har han en inflammation. När vi stöter på ett av villkoren kan vi dra en slutsats om inflammation, och sedan använda den i vidare resonemang.
   - Algoritmer kan betraktas som en annan form av procedural representation, även om de nästan aldrig används direkt i kunskapsbaserade system.

4. **Logik** föreslogs ursprungligen av Aristoteles som ett sätt att representera universell mänsklig kunskap.
   - Predikatlogik som en matematisk teori är för rik för att vara beräkningsbar, därför används normalt en delmängd av den, såsom Horn-klausuler som används i Prolog.
   - Beskrivande logik är en familj av logiska system som används för att representera och resonera om hierarkier av objekt i distribuerade kunskapsrepresentationer som *semantiskt web*.

## Expert System

En av de tidiga framgångarna för symbolisk AI var så kallade **expertsystem** - datorsystem som var designade för att agera som en expert inom ett begränsat problemområde. De baserades på en **kunskapsbas** som extraherades från en eller flera mänskliga experter, och de innehöll en **slutledningsmotor** som utförde resonemang ovanpå den.

![Mänsklig Arkitektur](../../../../translated_images/arch-human.5d4d35f1bba3ab1cdfda96af2f10b89574eb31e9796d0e3011cd9beda1c35112.sw.png) | ![Kunskapsbaserat System](../../../../translated_images/arch-kbs.3ec5c150b09fa8dadc2beb0931a4983c9e2b03913a89eebcc103b5bb841b0212.sw.png)
---------------------------------------------|------------------------------------------------
Förenklad struktur av ett mänskligt neuralt system | Arkitektur av ett kunskapsbaserat system

Expertsystem byggs som det mänskliga resonemangssystemet, som innehåller **korttidsminne** och **långtidsminne**. På liknande sätt särskiljer vi i kunskapsbaserade system följande komponenter:

* **Problemminne**: innehåller kunskap om det problem som för närvarande löses, dvs. temperaturen eller blodtrycket hos en patient, om han har inflammation eller inte, etc. Denna kunskap kallas också **statisk kunskap**, eftersom den innehåller en ögonblicksbild av vad vi för närvarande vet om problemet - det så kallade *problemstatus*.
* **Kunskapsbas**: representerar långsiktig kunskap om ett problemområde. Den extraheras manuellt från mänskliga experter och förändras inte från konsultation till konsultation. Eftersom den tillåter oss att navigera från ett problemstatus till ett annat, kallas den också **dynamisk kunskap**.
* **Slutledningsmotor**: orkestrerar hela processen av sökning i problemstatusens rum, ställer frågor till användaren när det är nödvändigt. Den är också ansvarig för att hitta rätt regler som ska tillämpas på varje status.

Som ett exempel, låt oss överväga följande expertsystem för att bestämma ett djur baserat på dess fysiska egenskaper:

![AND-OR Träd](../../../../translated_images/AND-OR-Tree.5592d2c70187f283703c8e9c0d69d6a786eb370f4ace67f9a7aae5ada3d260b0.sw.png)

> Bild av [Dmitry Soshnikov](http://soshnikov.com)

Detta diagram kallas ett **AND-OR-träd**, och det är en grafisk representation av en uppsättning produktionsregler. Att rita ett träd är användbart i början av kunskapsutvinning från experten. För att representera kunskapen inuti datorn är det mer bekvämt att använda regler:

```
IF the animal eats meat
OR (animal has sharp teeth
    AND animal has claws
    AND animal has forward-looking eyes
) 
THEN the animal is a carnivore
```

Du kan märka att varje villkor på vänster sida av regeln och åtgärden i grunden är objekt-attribut-värde (OAV) trippel. **Arbetsminnet** innehåller uppsättningen av OAV-trippel som motsvarar det problem som för närvarande löses. En **regelmotor** letar efter regler vars villkor är uppfyllda och tillämpar dem, vilket lägger till en annan trippel till arbetsminnet.

> ✅ Rita ditt eget AND-OR-träd om ett ämne du gillar!

### Framåt vs. Bakåt Slutledning

Processen som beskrivs ovan kallas **framåt slutledning**. Den börjar med viss initial data om problemet som finns i arbetsminnet, och utför sedan följande resonemangsslinga:

1. Om det målattributet finns i arbetsminnet - stoppa och ge resultatet
2. Leta efter alla regler vars villkor för närvarande är uppfyllda - erhåll **konfliktuppsättning** av regler.
3. Utför **konfliktlösning** - välj en regel som ska utföras i detta steg. Det kan finnas olika strategier för konfliktlösning:
   - Välj den första tillämpliga regeln i kunskapsbasen
   - Välj en slumpmässig regel
   - Välj en *mer specifik* regel, dvs. den som uppfyller flest villkor på "vänster sida" (LHS)
4. Tillämpa vald regel och sätt in en ny kunskapsbit i problemstatus
5. Upprepa från steg 1.

Men i vissa fall kanske vi vill börja med en tom kunskap om problemet och ställa frågor som hjälper oss att nå en slutsats. Till exempel, när vi gör medicinska diagnoser, utför vi vanligtvis inte alla medicinska analyser i förväg innan vi börjar diagnostisera patienten. Vi vill hellre utföra analyser när ett beslut behöver fattas.

Denna process kan modelleras med hjälp av **bakåt slutledning**. Den drivs av **målet** - det attributvärde som vi letar efter:

1. Välj alla regler som kan ge oss värdet av ett mål (dvs. med målet på RHS ("höger sida")) - en konfliktuppsättning
1. Om det inte finns några regler för detta attribut, eller det finns en regel som säger att vi ska fråga användaren om värdet - fråga efter det, annars:
1. Använd konfliktlösningsstrategin för att välja en regel som vi kommer att använda som *hypotes* - vi kommer att försöka bevisa den
1. Återkommande upprepa processen för alla attribut i LHS av regeln, och försöka bevisa dem som mål
1. Om processen misslyckas vid något tillfälle - använd en annan regel i steg 3.

> ✅ I vilka situationer är framåt slutledning mer lämplig? Hur är det med bakåt slutledning?

### Implementera Expertsystem

Expertsystem kan implementeras med hjälp av olika verktyg:

* Programmera dem direkt i något hög nivå programmeringsspråk. Detta är inte den bästa idén, eftersom den främsta fördelen med ett kunskapsbaserat system är att kunskapen är separerad från slutsatserna, och potentiellt bör en problemområdesexpert kunna skriva regler utan att förstå detaljerna i slutledningsprocessen.
* Använda **expertsystemskal**, dvs. ett system som är specifikt utformat för att fyllas med kunskap med hjälp av något kunskapsrepresentationsspråk.

## ✍️ Övning: Djur Slutledning

Se [Animals.ipynb](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) för ett exempel på att implementera framåt och bakåt slutledning i ett expertsystem.

> **Obs**: Detta exempel är ganska enkelt och ger bara en uppfattning om hur ett expertsystem ser ut. När du börjar skapa ett sådant system kommer du bara att märka något *intelligent* beteende från det när du når ett visst antal regler, omkring 200+. Vid en viss punkt blir reglerna för komplexa för att hålla dem alla i minnet, och vid denna punkt kan du börja undra varför ett system fattar vissa beslut. Men den viktiga egenskapen hos kunskapsbaserade system är att du alltid kan *förklara* exakt hur något av besluten fattades.

## Ontologier och det Semantiska Webben

I slutet av 1900-talet fanns det en initiativ för att använda kunskapsrepresentation för att annotera internetresurser, så att det skulle vara möjligt att hitta resurser som motsvarar mycket specifika frågor. Denna rörelse kallades **Semantiskt Web**, och den förlitade sig på flera koncept:

- En speciell kunskapsrepresentation baserad på **[beskrivningslogik](https://en.wikipedia.org/wiki/Description_logic)** (DL). Den liknar ramkunskapsrepresentation, eftersom den bygger en hierarki av objekt med egenskaper, men den har formell logisk semantik och slutsats. Det finns en hel familj av DL som balanserar mellan uttryckbarhet och algoritmisk komplexitet av slutsatser.
- Distribuerad kunskapsrepresentation, där alla koncept representeras av en global URI-identifierare, vilket gör det möjligt att skapa kunskapshierarkier som sträcker sig över internet.
- En familj av XML-baserade språk för kunskapsbeskrivning: RDF (Resource Description Framework), RDFS (RDF Schema), OWL (Ontology Web Language).

Ett kärnkoncept i det semantiska webben är konceptet **Ontologi**. Det hänvisar till en explicit specifikation av ett problemområde med hjälp av någon formell kunskapsrepresentation. Den enklaste ontologin kan vara enbart en hierarki av objekt i ett problemområde, men mer komplexa ontologier kommer att inkludera regler som kan användas för slutsats.

I det semantiska webben baseras alla representationer på trippel. Varje objekt och varje relation identifieras unikt av URI. Till exempel, om vi vill ange att denna AI-läroplan har utvecklats av Dmitry Soshnikov den 1 januari 2022 - här är trippeln vi kan använda:

<img src="images/triplet.png" width="30%"/>

```
http://github.com/microsoft/ai-for-beginners http://www.example.com/terms/creation-date “Jan 13, 2007”
http://github.com/microsoft/ai-for-beginners http://purl.org/dc/elements/1.1/creator http://soshnikov.com
```

> ✅ Här `http://www.example.com/terms/creation-date` and `http://purl.org/dc/elements/1.1/creator` är några välkända och allmänt accepterade URIs för att uttrycka koncepten *skapare* och *skapelsedatum*.

I ett mer komplext fall, om vi vill definiera en lista av skapare, kan vi använda några datakonstruktioner definierade i RDF.

<img src="images/triplet-complex.png" width="40%"/>

> Diagrammen ovan av [Dmitry Soshnikov](http://soshnikov.com)

Framstegen för att bygga det semantiska webben har på något sätt bromsats av framgången för sökmotorer och tekniker för naturlig språkbehandling, som gör det möjligt att extrahera strukturerad data från text. Men inom vissa områden finns det fortfarande betydande ansträngningar för att upprätthålla ontologier och kunskapsbaser. Några projekt värda att nämna:

* [WikiData](https://wikidata.org/) är en samling maskinläsbara kunskapsbaser kopplade till Wikipedia. Det mesta av datan utvinns från Wikipedia *InfoBoxes*, delar av strukturerat innehåll inom Wikipedia-sidor. Du kan [fråga](https://query.wikidata.org/) wikidata i SPARQL, ett specialiserat frågespråk för det semantiska webben. Här är ett exempel på en fråga som visar de mest populära ö

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår på grund av användningen av denna översättning.