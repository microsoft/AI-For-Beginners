# Genetiske Algoritmer

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetiske algoritmer** (GA) er basert på en **evolusjonær tilnærming** til AI, der metoder for evolusjon av en populasjon brukes for å finne en optimal løsning for et gitt problem. De ble foreslått i 1975 av [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetiske algoritmer bygger på følgende ideer:

* Gyldige løsninger på problemet kan representeres som **gener**
* **Kryssing** lar oss kombinere to løsninger for å oppnå en ny gyldig løsning
* **Seleksjon** brukes til å velge mer optimale løsninger ved hjelp av en **fitness-funksjon**
* **Mutasjoner** introduseres for å destabilisere optimaliseringen og få oss ut av lokale minima

Hvis du vil implementere en genetisk algoritme, trenger du følgende:

 * En metode for å kode problemets løsninger ved hjelp av **gener** g&in;&Gamma;
 * På settet av gener &Gamma; må vi definere en **fitness-funksjon** fit: &Gamma;&rightarrow;**R**. Mindre verdier av funksjonen tilsvarer bedre løsninger.
 * Definere en **kryssingsmekanisme** for å kombinere to gener og få en ny gyldig løsning crossover: &Gamma;<sup>2</sub>&rightarrow;&Gamma;.
 * Definere en **mutasjonsmekanisme** mutate: &Gamma;&rightarrow;&Gamma;.

I mange tilfeller er kryssing og mutasjon ganske enkle algoritmer for å manipulere gener som numeriske sekvenser eller bitvektorer.

Den spesifikke implementeringen av en genetisk algoritme kan variere fra tilfelle til tilfelle, men den generelle strukturen er som følger:

1. Velg en startpopulasjon G&subset;&Gamma;
2. Velg tilfeldig en av operasjonene som skal utføres i dette steget: kryssing eller mutasjon
3. **Kryssing**:
  * Velg tilfeldig to gener g<sub>1</sub>, g<sub>2</sub> &in; G
  * Beregn kryssing g=crossover(g<sub>1</sub>,g<sub>2</sub>)
  * Hvis fit(g)<fit(g<sub>1</sub>) eller fit(g)<fit(g<sub>2</sub>) - erstatt det tilsvarende genet i populasjonen med g.
4. **Mutasjon** - velg et tilfeldig gen g&in;G og erstatt det med mutate(g)
5. Gjenta fra steg 2, til vi får en tilstrekkelig liten verdi av fit, eller til grensen for antall steg er nådd.

## Typiske Oppgaver

Oppgaver som typisk løses med genetiske algoritmer inkluderer:

1. Optimalisering av tidsplaner
1. Optimal pakking
1. Optimal kutting
1. Akselerering av uttømmende søk

## ✍️ Øvelser: Genetiske Algoritmer

Fortsett læringen i følgende notatbøker:

Gå til [denne notatboken](Genetic.ipynb) for å se to eksempler på bruk av genetiske algoritmer:

1. Rettferdig fordeling av skatter
1. 8-dronningers problemet

## Konklusjon

Genetiske algoritmer brukes til å løse mange problemer, inkludert logistikk og søkeproblemer. Feltet er inspirert av forskning som kombinerte temaer innen psykologi og informatikk.

## 🚀 Utfordring

"Genetiske algoritmer er enkle å implementere, men deres oppførsel er vanskelig å forstå." [kilde](https://wikipedia.org/wiki/Genetic_algorithm) Gjør litt research for å finne en implementering av en genetisk algoritme, for eksempel for å løse et Sudoku-puslespill, og forklar hvordan det fungerer som en skisse eller flytdiagram.

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Gjennomgang & Selvstudium

Se [denne flotte videoen](https://www.youtube.com/watch?v=qv6UVOQ0F44) som forklarer hvordan en datamaskin kan lære å spille Super Mario ved hjelp av nevrale nettverk trent med genetiske algoritmer. Vi skal lære mer om hvordan datamaskiner lærer å spille slike spill [i neste seksjon](../22-DeepRL/README.md).

## [Oppgave: Diofantisk Likning](Diophantine.ipynb)

Målet ditt er å løse den såkalte **Diofantiske likningen** - en likning med heltallsrøtter. For eksempel, vurder likningen a+2b+3c+4d=30. Du må finne heltallsrøttene som tilfredsstiller denne likningen.

*Denne oppgaven er inspirert av [denne artikkelen](https://habr.com/post/128704/).*

Tips:

1. Du kan vurdere røttene å være i intervallet [0;30]
1. Som et gen, vurder å bruke listen over rotverdier

Bruk [Diophantine.ipynb](Diophantine.ipynb) som utgangspunkt.

---

