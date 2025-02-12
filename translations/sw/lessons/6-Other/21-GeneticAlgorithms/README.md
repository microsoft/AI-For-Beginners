# Genetiska Algoritmer

## [För-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Genetiska Algoritmer** (GA) bygger på en **evolutionär metod** för AI, där metoder för evolution av en population används för att uppnå en optimal lösning på ett givet problem. De föreslogs 1975 av [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetiska Algoritmer baseras på följande idéer:

* Giltiga lösningar på problemet kan representeras som **gener**
* **Crossover** gör att vi kan kombinera två lösningar för att få en ny giltig lösning
* **Urval** används för att välja mer optimala lösningar med hjälp av en viss **fitnessfunktion**
* **Mutationer** introduceras för att destabilisera optimeringen och få oss ur det lokala minimumet

Om du vill implementera en Genetisk Algoritm behöver du följande:

 * Att hitta en metod för att koda våra problemlösningar med hjälp av **gener** g∈Γ
 * På mängden av gener Γ behöver vi definiera en **fitnessfunktion** fit: Γ→**R**. Mindre funktionsvärden motsvarar bättre lösningar.
 * Att definiera en **crossover**-mekanism för att kombinera två gener för att få en ny giltig lösning crossover: Γ<sup>2</sub>→Γ.
 * Att definiera en **mutations**-mekanism mutate: Γ→Γ.

I många fall är crossover och mutation ganska enkla algoritmer för att manipulera gener som numeriska sekvenser eller bitvektorer.

Den specifika implementeringen av en genetisk algoritm kan variera från fall till fall, men den övergripande strukturen är följande:

1. Välj en initial population G⊂Γ
2. Slumptalsvälja en av de operationer som ska utföras i detta steg: crossover eller mutation
3. **Crossover**:
  * Slumptalsvälja två gener g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Beräkna crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Om fit(g)<fit(g<sub>1</sub>) eller fit(g)<fit(g<sub>2</sub>) - ersätt motsvarande gen i populationen med g.
4. **Mutation** - välj en slumpmässig gen g∈G och ersätt den med mutate(g)
5. Upprepa från steg 2, tills vi får ett tillräckligt litet värde av fit, eller tills gränsen för antalet steg nås.

## Typiska Uppgifter

Uppgifter som vanligtvis löses med Genetiska Algoritmer inkluderar:

1. Schemaläggningsoptimering
1. Optimal packning
1. Optimal skärning
1. Snabbare exhaustiv sökning

## ✍️ Övningar: Genetiska Algoritmer

Fortsätt ditt lärande i följande anteckningsböcker:

Gå till [denna anteckningsbok](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) för att se två exempel på användning av Genetiska Algoritmer:

1. Rättvis fördelning av skatt
1. 8 Drottningar Problemet

## Slutsats

Genetiska Algoritmer används för att lösa många problem, inklusive logistik och sökproblem. Fältet är inspirerat av forskning som sammanfogar ämnen inom psykologi och datavetenskap.

## 🚀 Utmaning

"Genetiska algoritmer är enkla att implementera, men deras beteende är svårt att förstå." [källa](https://wikipedia.org/wiki/Genetic_algorithm) Gör lite forskning för att hitta en implementation av en genetisk algoritm, såsom att lösa ett Sudoku-pussel, och förklara hur det fungerar som en skiss eller flödesdiagram.

## [Efter-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Granskning & Självstudie

Titta på [denna fantastiska video](https://www.youtube.com/watch?v=qv6UVOQ0F44) som handlar om hur datorer kan lära sig spela Super Mario med hjälp av neurala nätverk som tränats av genetiska algoritmer. Vi kommer att lära oss mer om datorer som lär sig spela sådana spel [i nästa avsnitt](../22-DeepRL/README.md).

## [Uppgift: Diophantine-ekvation](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Ditt mål är att lösa den så kallade **Diophantine-ekvationen** - en ekvation med heltalslösningar. Till exempel, betrakta ekvationen a+2b+3c+4d=30. Du behöver hitta de heltalslösningar som uppfyller denna ekvation.

*Denna uppgift är inspirerad av [detta inlägg](https://habr.com/post/128704/).*

Tips:

1. Du kan betrakta rötterna som liggande i intervallet [0;30]
1. Som en gen, överväg att använda listan av rotvärden

Använd [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) som en utgångspunkt.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår på grund av användningen av denna översättning.