<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-28T15:02:28+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "sv"
}
-->
# Genetiska Algoritmer

## [Quiz före föreläsningen](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Genetiska Algoritmer** (GA) bygger på en **evolutionär metod** inom AI, där metoder för att utveckla en population används för att hitta en optimal lösning på ett givet problem. De föreslogs 1975 av [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetiska Algoritmer bygger på följande idéer:

* Giltiga lösningar på problemet kan representeras som **gener**
* **Korsning** gör det möjligt att kombinera två lösningar för att få en ny giltig lösning
* **Urval** används för att välja mer optimala lösningar med hjälp av en **fitnessfunktion**
* **Mutationer** introduceras för att destabilisera optimeringen och ta oss ur lokala minima

Om du vill implementera en Genetisk Algoritm behöver du följande:

 * En metod för att koda våra problemlösningar med hjälp av **gener** g∈Γ
 * På mängden gener Γ behöver vi definiera en **fitnessfunktion** fit: Γ→**R**. Lägre funktionsvärden motsvarar bättre lösningar.
 * Definiera en mekanism för **korsning** för att kombinera två gener och få en ny giltig lösning crossover: Γ<sup>2</sub>→Γ.
 * Definiera en mekanism för **mutation** mutate: Γ→Γ.

I många fall är korsning och mutation ganska enkla algoritmer för att manipulera gener som numeriska sekvenser eller bitvektorer.

Den specifika implementeringen av en genetisk algoritm kan variera från fall till fall, men den övergripande strukturen är följande:

1. Välj en initial population G⊂Γ
2. Välj slumpmässigt en av operationerna som ska utföras i detta steg: korsning eller mutation
3. **Korsning**:
  * Välj slumpmässigt två gener g<sub>1</sub>, g<sub>2</sub> ∈ G
  * Beräkna korsning g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Om fit(g)<fit(g<sub>1</sub>) eller fit(g)<fit(g<sub>2</sub>) - ersätt motsvarande gen i populationen med g.
4. **Mutation** - välj en slumpmässig gen g∈G och ersätt den med mutate(g)
5. Upprepa från steg 2 tills vi får ett tillräckligt lågt värde på fit, eller tills gränsen för antalet steg är nådd.

## Typiska Uppgifter

Uppgifter som vanligtvis löses med Genetiska Algoritmer inkluderar:

1. Optimering av scheman
1. Optimal packning
1. Optimal skärning
1. Snabbare uttömmande sökning

## ✍️ Övningar: Genetiska Algoritmer

Fortsätt ditt lärande i följande anteckningsböcker:

Gå till [denna anteckningsbok](Genetic.ipynb) för att se två exempel på användning av Genetiska Algoritmer:

1. Rättvis fördelning av skatt
1. 8 drottningars problem

## Slutsats

Genetiska Algoritmer används för att lösa många problem, inklusive logistik- och sökproblem. Fältet är inspirerat av forskning som förenade ämnen inom psykologi och datavetenskap.

## 🚀 Utmaning

"Genetiska algoritmer är enkla att implementera, men deras beteende är svårt att förstå." [källa](https://wikipedia.org/wiki/Genetic_algorithm) Gör lite forskning för att hitta en implementering av en genetisk algoritm, till exempel för att lösa ett Sudoku-pussel, och förklara hur den fungerar som en skiss eller flödesschema.

## [Quiz efter föreläsningen](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Granskning & Självstudier

Titta på [denna fantastiska video](https://www.youtube.com/watch?v=qv6UVOQ0F44) som pratar om hur datorer kan lära sig spela Super Mario med hjälp av neurala nätverk tränade av genetiska algoritmer. Vi kommer att lära oss mer om hur datorer lär sig spela spel som detta [i nästa avsnitt](../22-DeepRL/README.md).

## [Uppgift: Diofantisk Ekvation](Diophantine.ipynb)

Ditt mål är att lösa den så kallade **Diofantiska ekvationen** - en ekvation med heltalsrötter. Till exempel, överväg ekvationen a+2b+3c+4d=30. Du behöver hitta heltalsrötterna som uppfyller denna ekvation.

*Denna uppgift är inspirerad av [detta inlägg](https://habr.com/post/128704/).*

Tips:

1. Du kan överväga rötter i intervallet [0;30]
1. Som en gen kan du använda listan över rotvärden

Använd [Diophantine.ipynb](Diophantine.ipynb) som utgångspunkt.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller inexaktheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.