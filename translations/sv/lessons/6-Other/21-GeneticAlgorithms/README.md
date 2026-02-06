# Genetiska Algoritmer

## [Quiz före föreläsningen](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetiska algoritmer** (GA) bygger på en **evolutionär metod** inom AI, där metoder för att utveckla en population används för att hitta en optimal lösning för ett givet problem. De föreslogs 1975 av [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetiska algoritmer baseras på följande idéer:

* Giltiga lösningar på problemet kan representeras som **gener**
* **Korsning** gör det möjligt att kombinera två lösningar för att få en ny giltig lösning
* **Urval** används för att välja mer optimala lösningar med hjälp av en **fitnessfunktion**
* **Mutationer** introduceras för att destabilisera optimeringen och ta oss ur lokala minima

Om du vill implementera en genetisk algoritm behöver du följande:

 * Hitta ett sätt att koda våra problemlösningar med hjälp av **gener** g&in;&Gamma;
 * På mängden gener &Gamma; behöver vi definiera en **fitnessfunktion** fit: &Gamma;&rightarrow;**R**. Mindre funktionsvärden motsvarar bättre lösningar.
 * Definiera en **korsningsmekanism** för att kombinera två gener och få en ny giltig lösning crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Definiera en **mutationsmekanism** mutate: &Gamma;&rightarrow;&Gamma;.

I många fall är korsning och mutation ganska enkla algoritmer för att manipulera gener som numeriska sekvenser eller bitvektorer.

Den specifika implementeringen av en genetisk algoritm kan variera från fall till fall, men den övergripande strukturen är följande:

1. Välj en initial population G&subset;&Gamma;
2. Välj slumpmässigt en av de operationer som ska utföras vid detta steg: korsning eller mutation
3. **Korsning**:
  * Välj slumpmässigt två gener g<sub>1</sub>, g<sub>2</sub> &in; G
  * Beräkna korsning g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Om fit(g)<fit(g<sub>1</sub>) eller fit(g)<fit(g<sub>2</sub>) - ersätt motsvarande gen i populationen med g.
4. **Mutation** - välj en slumpmässig gen g&in;G och ersätt den med mutate(g)
5. Upprepa från steg 2 tills vi får ett tillräckligt litet värde på fit, eller tills gränsen för antalet steg har nåtts.

## Typiska Uppgifter

Uppgifter som vanligtvis löses med genetiska algoritmer inkluderar:

1. Optimering av scheman
1. Optimal packning
1. Optimal skärning
1. Snabba upp uttömmande sökningar

## ✍️ Övningar: Genetiska Algoritmer

Fortsätt ditt lärande i följande anteckningsböcker:

Gå till [denna anteckningsbok](Genetic.ipynb) för att se två exempel på användning av genetiska algoritmer:

1. Rättvis fördelning av skatt
1. 8 drottningars problem

## Slutsats

Genetiska algoritmer används för att lösa många problem, inklusive logistik och sökproblem. Fältet är inspirerat av forskning som kombinerade ämnen inom psykologi och datavetenskap.

## 🚀 Utmaning

"Genetiska algoritmer är enkla att implementera, men deras beteende är svårt att förstå." [källa](https://wikipedia.org/wiki/Genetic_algorithm) Gör lite forskning för att hitta en implementering av en genetisk algoritm, som att lösa ett Sudoku-pussel, och förklara hur det fungerar som en skiss eller flödesschema.

## [Quiz efter föreläsningen](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Granskning & Självstudier

Titta på [denna fantastiska video](https://www.youtube.com/watch?v=qv6UVOQ0F44) som handlar om hur datorer kan lära sig spela Super Mario med hjälp av neurala nätverk tränade av genetiska algoritmer. Vi kommer att lära oss mer om hur datorer lär sig spela sådana spel [i nästa avsnitt](../22-DeepRL/README.md).

## [Uppgift: Diofantisk Ekvation](Diophantine.ipynb)

Ditt mål är att lösa den så kallade **Diofantiska ekvationen** - en ekvation med heltalsrötter. Till exempel, överväg ekvationen a+2b+3c+4d=30. Du behöver hitta heltalsrötterna som uppfyller denna ekvation.

*Denna uppgift är inspirerad av [detta inlägg](https://habr.com/post/128704/).*

Tips:

1. Du kan överväga rötterna att vara i intervallet [0;30]
1. Som en gen kan du använda listan över rotvärden

Använd [Diophantine.ipynb](Diophantine.ipynb) som startpunkt.

---

