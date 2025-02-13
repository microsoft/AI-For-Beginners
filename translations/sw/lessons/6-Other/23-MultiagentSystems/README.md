# Multi-Agent System

Ett av de möjliga sätten att uppnå intelligens är den så kallade **emergenta** (eller **synergetiska**) metoden, som bygger på det faktum att det kombinerade beteendet hos många relativt enkla agenter kan resultera i ett mer komplext (eller intelligent) beteende hos systemet som helhet. Teoretiskt sett baseras detta på principerna för [Kollektiv Intelligens](https://en.wikipedia.org/wiki/Collective_intelligence), [Emergentism](https://en.wikipedia.org/wiki/Global_brain) och [Evolutionär Cybernetik](https://en.wikipedia.org/wiki/Global_brain), som säger att högre nivåsystem får någon form av mervärde när de kombineras på rätt sätt från lägre nivåsystem (den så kallade *metasystemövergångsprincipen*).

## [För-föreläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/123)

Riktningen för **Multi-Agent System** har uppkommit inom AI på 1990-talet som ett svar på tillväxten av Internet och distribuerade system. En av de klassiska AI-läroböckerna, [Artificial Intelligence: A Modern Approach](https://en.wikipedia.org/wiki/Artificial_Intelligence:_A_Modern_Approach), fokuserar på synsättet av klassisk AI ur perspektivet av multi-agent system.

Centralt för multi-agent metoden är begreppet **Agent** - en enhet som lever i en viss **miljö**, som den kan uppfatta och agera på. Detta är en mycket bred definition, och det kan finnas många olika typer och klassificeringar av agenter:

* Efter deras förmåga att resonera:
   - **Reaktiva** agenter har vanligtvis ett enkelt begär-svar-beteende
   - **Deliberativa** agenter använder någon form av logiskt resonemang och/eller planeringsförmåga
* Efter platsen där agenten kör sin kod:
   - **Statisk** agenter arbetar på en dedikerad nätverksnod
   - **Mobila** agenter kan flytta sin kod mellan nätverksnoder
* Efter deras beteende:
   - **Passiva agenter** har inga specifika mål. Sådana agenter kan reagera på externa stimuli, men kommer inte att initiera några handlingar själva.
   - **Aktiva agenter** har vissa mål som de strävar efter
   - **Kognitiva agenter** involverar komplex planering och resonemang

Multi-agent system används idag i ett antal tillämpningar:

* Inom spel, många icke-spelarkaraktärer använder någon form av AI, och kan betraktas som intelligenta agenter
* Inom videoproduktion, rendering av komplexa 3D-scener som involverar folkmassor görs vanligtvis med hjälp av multi-agent simulering
* Inom systemmodellering används multi-agent metoden för att simulera beteendet hos en komplex modell. Till exempel har multi-agent metoden framgångsrikt använts för att förutsäga spridningen av COVID-19 sjukdomen världen över. En liknande metod kan användas för att modellera trafik i staden, och se hur den reagerar på förändringar i trafikregler.
* I komplexa automationssystem kan varje enhet agera som en oberoende agent, vilket gör hela systemet mindre monolitiskt och mer robust.

Vi kommer inte att spendera mycket tid på att gå djupt in i multi-agent system, men vi kommer att överväga ett exempel på **Multi-Agent Modellering**.

## NetLogo

[NetLogo](https://ccl.northwestern.edu/netlogo/) är en miljö för multi-agent modellering baserad på en modifierad version av [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) programmeringsspråket. Detta språk utvecklades för att lära ut programmeringskoncept till barn, och det låter dig styra en agent kallad **sköldpadda**, som kan röra sig och lämna ett spår bakom sig. Detta möjliggör skapandet av komplexa geometriska figurer, vilket är ett mycket visuellt sätt att förstå beteendet hos en agent.

I NetLogo kan vi skapa många sköldpaddor genom att använda kommandot `create-turtles`. Vi kan sedan befalla alla sköldpaddor att utföra vissa åtgärder (i exemplet nedan - mer 10 steg framåt):

```
create-turtles 10
ask turtles [
  forward 10
]
```

Självklart är det inte intressant när alla sköldpaddor gör samma sak, så vi kan `ask` groups of turtles, eg. those who are in the vicinity of a certain point. We can also create turtles of different *breeds* using `breed [cats cat]` command. Here `cat` är namnet på en ras, och vi behöver specificera både singular och plural ord, eftersom olika kommandon använder olika former för tydlighet.

> ✅ Vi kommer inte att gå in på att lära oss NetLogo-språket i sig - du kan besöka den briljanta [Beginner's Interactive NetLogo Dictionary](https://ccl.northwestern.edu/netlogo/bind/) resursen om du är intresserad av att lära dig mer.

Du kan [ladda ner](https://ccl.northwestern.edu/netlogo/download.shtml) och installera NetLogo för att prova det.

### Modeller Bibliotek

En fantastisk sak med NetLogo är att det innehåller ett bibliotek av fungerande modeller som du kan prova. Gå till **Fil → Modeller Bibliotek**, och du har många kategorier av modeller att välja mellan.

<img alt="NetLogo Modeller Bibliotek" src="images/NetLogo-ModelLib.png" width="60%"/>

> En skärmdump av modeller biblioteket av Dmitry Soshnikov

Du kan öppna en av modellerna, till exempel **Biologi → Flocking**.

### Huvudprinciper

Efter att ha öppnat modellen tas du till huvudskärmen för NetLogo. Här är en exempelmodell som beskriver populationen av vargar och får, givet ändliga resurser (gräs).

![NetLogo Huvudskärm](../../../../../translated_images/NetLogo-Main.32653711ec1a01b3cab22ec0b148e64193d0b979b055285bef329d5e3d6958c5.sw.png)

> Skärmdump av Dmitry Soshnikov

På den här skärmen kan du se:

* **Gränssnittet** som innehåller:
  - Huvudfältet, där alla agenter lever
  - Olika kontroller: knappar, reglage, etc.
  - Grafer som du kan använda för att visa parametrar för simuleringen
* **Kod** fliken som innehåller redigeraren, där du kan skriva NetLogo-program

I de flesta fall skulle gränssnittet ha en **Setup**-knapp, som initierar simuleringstillståndet, och en **Go**-knapp som startar körningen. Dessa hanteras av motsvarande hanterare i koden som ser ut så här:

```
to go [
...
]
```

NetLogos värld består av följande objekt:

* **Agenter** (sköldpaddor) som kan röra sig över fältet och göra något. Du kommanderar agenter genom att använda `ask turtles [...]` syntax, and the code in brackets is executed by all agents in *turtle mode*.
* **Patches** are square areas of the field, on which agents live. You can refer to all agents on the same patch, or you can change patch colors and some other properties. You can also `ask patches` för att göra något.
* **Observer** är en unik agent som kontrollerar världen. Alla knapphanterare utförs i *observatörsläge*.

> ✅ Skönheten med en multi-agent miljö är att koden som körs i sköldpaddsläge eller i patchläge utförs samtidigt av alla agenter parallellt. Således, genom att skriva lite kod och programmera beteendet hos enskilda agenter, kan du skapa ett komplext beteende för simuleringssystemet som helhet.

### Flocking

Som ett exempel på multi-agent beteende, låt oss överväga **[Flocking](https://en.wikipedia.org/wiki/Flocking_(behavior))**. Flocking är ett komplext mönster som är mycket likt hur fågelflockar flyger. När man ser dem flyga kan man tänka att de följer någon slags kollektiv algoritm, eller att de besitter någon form av *kollektiv intelligens*. Men detta komplexa beteende uppstår när varje individuell agent (i detta fall, en *fågel*) endast observerar några andra agenter på kort avstånd från sig, och följer tre enkla regler:

* **Justering** - den styr mot den genomsnittliga riktningen av grannagenter
* **Kohesion** - den försöker styra mot den genomsnittliga positionen av grannar (*långdistansattraktion*)
* **Separation** - när den kommer för nära andra fåglar, försöker den röra sig bort (*kortdistansrepulsion*)

Du kan köra flockningsexemplet och observera beteendet. Du kan också justera parametrar, såsom *grad av separation*, eller *synfältet*, som definierar hur långt varje fågel kan se. Observera att om du minskar synfältet till 0, blir alla fåglar blinda, och flockning stoppar. Om du minskar separationen till 0, samlas alla fåglar i en rak linje.

> ✅ Byt till **Kod** fliken och se var de tre reglerna för flockning (justering, kohesion och separation) implementeras i koden. Observera hur vi endast refererar till de agenter som är i sikte.

### Andra modeller att se

Det finns några fler intressanta modeller som du kan experimentera med:

* **Konst → Fyrverkerier** visar hur ett fyrverkeri kan betraktas som ett kollektivt beteende av individuella eldstrålar
* **Samhällsvetenskap → Trafik Grundläggande** och **Samhällsvetenskap → Trafik Rutnät** visar modellen för stads trafik i 1D och 2D-rutnät med eller utan trafikljus. Varje bil i simuleringen följer följande regler:
   - Om utrymmet framför den är tomt - accelerera (upp till en viss maxhastighet)
   - Om den ser ett hinder framför - bromsa (och du kan justera hur långt en förare kan se)
* **Samhällsvetenskap → Fest** visar hur människor grupperar sig under en cocktailfest. Du kan hitta kombinationen av parametrar som leder till den snabbaste ökningen av gruppens lycka.

Som du kan se från dessa exempel kan multi-agent simuleringar vara ett mycket användbart sätt att förstå beteendet hos ett komplext system bestående av individer som följer samma eller liknande logik. Det kan också användas för att styra virtuella agenter, såsom [NPCs](https://en.wikipedia.org/wiki/NPC) i datorspel, eller agenter i 3D-animerade världar.

## Deliberativa Agenter

Agenterna som beskrivs ovan är mycket enkla, reaktionära på förändringar i miljön med hjälp av någon slags algoritm. Som sådana är de **reaktiva agenter**. Men ibland kan agenter resonera och planera sina handlingar, i vilket fall de kallas **deliberativa**.

Ett typiskt exempel skulle vara en personlig agent som får en instruktion från en människa att boka en semesterresa. Anta att det finns många agenter som lever på internet, som kan hjälpa den. Den bör då kontakta andra agenter för att se vilka flyg som är tillgängliga, vad hotellpriserna är för olika datum, och försöka förhandla fram det bästa priset. När semesterplanen är klar och bekräftad av ägaren, kan den gå vidare med bokningen.

För att göra detta behöver agenterna **kommunicera**. För framgångsrik kommunikation behöver de:

* Några **standard språk för att utbyta kunskap**, såsom [Knowledge Interchange Format](https://en.wikipedia.org/wiki/Knowledge_Interchange_Format) (KIF) och [Knowledge Query and Manipulation Language](https://en.wikipedia.org/wiki/Knowledge_Query_and_Manipulation_Language) (KQML). Dessa språk är utformade baserat på [Speech Act theory](https://en.wikipedia.org/wiki/Speech_act).
* Dessa språk bör också inkludera några **protokoll för förhandlingar**, baserat på olika **auktionstyper**.
* En **gemensam ontologi** att använda, så att de hänvisar till samma begrepp och känner till deras semantik
* Ett sätt att **upptäcka** vad olika agenter kan göra, också baserat på någon form av ontologi

Deliberativa agenter är mycket mer komplexa än reaktiva, eftersom de inte bara reagerar på förändringar i miljön, utan också bör kunna *initiera* handlingar. En av de föreslagna arkitekturerna för deliberativa agenter är den så kallade Belief-Desire-Intention (BDI) agenten:

* **Tro** bildar en uppsättning kunskap om agentens miljö. Det kan struktureras som en kunskapsbas eller uppsättning regler som en agent kan tillämpa på en specifik situation i miljön.
* **Önskningar** definierar vad en agent vill göra, dvs. dess mål. Till exempel, målet för den personliga assistentagenten ovan är att boka en resa, och målet för en hotellagent är att maximera vinsten.
* **Avsikter** är specifika handlingar som en agent planerar att uppnå sina mål. Handlingar förändrar vanligtvis miljön och orsakar kommunikation med andra agenter.

Det finns några plattformar tillgängliga för att bygga multi-agent system, såsom [JADE](https://jade.tilab.com/). [Denna artikel](https://arxiv.org/ftp/arxiv/papers/2007/2007.08961.pdf) innehåller en översikt över multi-agent plattformar, tillsammans med en kort historia om multi-agent system och deras olika användningsscenarier.

## Slutsats

Multi-Agent system kan ta mycket olika former och användas i många olika tillämpningar. 
De tenderar alla att fokusera på det enklare beteendet hos en individuell agent och uppnå ett mer komplext beteende hos hela systemet på grund av **synergetisk effekt**.

## 🚀 Utmaning

Ta denna lektion till verkligheten och försök att konceptualisera ett multi-agent system som kan lösa ett problem. Vad skulle ett multi-agent system behöva göra för att optimera en skolbussrutt? Hur skulle det kunna fungera i ett bageri?

## [Efter-föreläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/223)

## Granskning & Självstudie

Granska användningen av denna typ av system inom industrin. Välj ett område som tillverkning eller videospelindustrin och upptäck hur multi-agent system kan användas för att lösa unika problem.

## [NetLogo Uppgift](assignment.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.