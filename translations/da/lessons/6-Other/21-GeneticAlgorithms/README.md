# Genetiske Algoritmer

## [Quiz før forelæsning](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetiske Algoritmer** (GA) er baseret på en **evolutionær tilgang** til AI, hvor metoder fra evolutionen af en population bruges til at finde en optimal løsning på et givet problem. De blev foreslået i 1975 af [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetiske Algoritmer bygger på følgende ideer:

* Gyldige løsninger på problemet kan repræsenteres som **gener**
* **Krydsning** giver os mulighed for at kombinere to løsninger for at opnå en ny gyldig løsning
* **Udvælgelse** bruges til at vælge mere optimale løsninger ved hjælp af en **fitness-funktion**
* **Mutationer** introduceres for at destabilisere optimeringen og få os ud af lokale minima

Hvis du vil implementere en Genetisk Algoritme, skal du bruge følgende:

 * En metode til at kode vores problemløsninger ved hjælp af **gener** g&in;&Gamma;
 * På sættet af gener &Gamma; skal vi definere en **fitness-funktion** fit: &Gamma;&rightarrow;**R**. Mindre funktionsværdier svarer til bedre løsninger.
 * Definere en **krydsningsmekanisme** til at kombinere to gener for at få en ny gyldig løsning crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Definere en **mutationsmekanisme** mutate: &Gamma;&rightarrow;&Gamma;.

I mange tilfælde er krydsning og mutation ret simple algoritmer til at manipulere gener som numeriske sekvenser eller bitvektorer.

Den specifikke implementering af en genetisk algoritme kan variere fra tilfælde til tilfælde, men den overordnede struktur er som følger:

1. Vælg en startpopulation G&subset;&Gamma;
2. Vælg tilfældigt en af de operationer, der skal udføres i dette trin: krydsning eller mutation
3. **Krydsning**:
  * Vælg tilfældigt to gener g<sub>1</sub>, g<sub>2</sub> &in; G
  * Beregn krydsning g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Hvis fit(g)<fit(g<sub>1</sub>) eller fit(g)<fit(g<sub>2</sub>) - erstat det tilsvarende gen i populationen med g.
4. **Mutation** - vælg et tilfældigt gen g&in;G og erstat det med mutate(g)
5. Gentag fra trin 2, indtil vi opnår en tilstrækkelig lille værdi af fit, eller indtil grænsen for antallet af trin er nået.

## Typiske Opgaver

Opgaver, der typisk løses med Genetiske Algoritmer, inkluderer:

1. Optimering af tidsplaner
1. Optimal pakning
1. Optimal skæring
1. Acceleration af udtømmende søgning

## ✍️ Øvelser: Genetiske Algoritmer

Fortsæt din læring i følgende notebooks:

Gå til [denne notebook](Genetic.ipynb) for at se to eksempler på brug af Genetiske Algoritmer:

1. Retfærdig opdeling af skat
1. 8 Dronninge Problemet

## Konklusion

Genetiske Algoritmer bruges til at løse mange problemer, herunder logistik og søgeproblemer. Feltet er inspireret af forskning, der kombinerede emner inden for psykologi og datalogi.

## 🚀 Udfordring

"Genetiske algoritmer er nemme at implementere, men deres adfærd er svær at forstå." [kilde](https://wikipedia.org/wiki/Genetic_algorithm) Lav lidt research for at finde en implementering af en genetisk algoritme, såsom løsning af et Sudoku-puslespil, og forklar, hvordan det fungerer som en skitse eller et flowdiagram.

## [Quiz efter forelæsning](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Gennemgang & Selvstudie

Se [denne fantastiske video](https://www.youtube.com/watch?v=qv6UVOQ0F44), der taler om, hvordan en computer kan lære at spille Super Mario ved hjælp af neurale netværk trænet med genetiske algoritmer. Vi vil lære mere om, hvordan computere lærer at spille spil som dette [i næste sektion](../22-DeepRL/README.md).

## [Opgave: Diofantisk Ligning](Diophantine.ipynb)

Dit mål er at løse den såkaldte **Diofantiske ligning** - en ligning med heltalsrødder. For eksempel, betragt ligningen a+2b+3c+4d=30. Du skal finde de heltalsrødder, der opfylder denne ligning.

*Denne opgave er inspireret af [dette indlæg](https://habr.com/post/128704/).*

Tips:

1. Du kan overveje rødderne at være i intervallet [0;30]
1. Som et gen kan du overveje at bruge listen over rodværdier

Brug [Diophantine.ipynb](Diophantine.ipynb) som udgangspunkt.

---

