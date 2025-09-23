<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-28T15:03:15+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "no"
}
-->
# Genetiske Algoritmer

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetiske Algoritmer** (GA) er basert på en **evolusjonær tilnærming** til kunstig intelligens, der metoder for evolusjon av en populasjon brukes for å finne en optimal løsning på et gitt problem. De ble foreslått i 1975 av [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland).

Genetiske Algoritmer bygger på følgende ideer:

* Gyldige løsninger på problemet kan representeres som **gener**
* **Kryssing** lar oss kombinere to løsninger for å oppnå en ny gyldig løsning
* **Seleksjon** brukes til å velge mer optimale løsninger ved hjelp av en **fitness-funksjon**
* **Mutasjoner** introduseres for å destabilisere optimaliseringen og hjelpe oss ut av lokale minima

Hvis du vil implementere en Genetisk Algoritme, trenger du følgende:

* En metode for å kode problemets løsninger ved hjelp av **gener** g∈Γ
* På settet av gener Γ må vi definere en **fitness-funksjon** fit: Γ→**R**. Mindre funksjonsverdier tilsvarer bedre løsninger.
* En mekanisme for **kryssing** for å kombinere to gener og få en ny gyldig løsning crossover: Γ<sup>2</sub>→Γ.
* En mekanisme for **mutasjon** mutate: Γ→Γ.

I mange tilfeller er kryssing og mutasjon ganske enkle algoritmer som manipulerer gener som numeriske sekvenser eller bitvektorer.

Den spesifikke implementasjonen av en genetisk algoritme kan variere fra tilfelle til tilfelle, men den overordnede strukturen er som følger:

1. Velg en startpopulasjon G⊂Γ
2. Velg tilfeldig en av operasjonene som skal utføres i dette steget: kryssing eller mutasjon
3. **Kryssing**:
   * Velg tilfeldig to gener g<sub>1</sub>, g<sub>2</sub> ∈ G
   * Beregn kryssing g=crossover(g<sub>1</sub>,g<sub>2</sub>)
   * Hvis fit(g)<fit(g<sub>1</sub>) eller fit(g)<fit(g<sub>2</sub>) - erstatt det tilsvarende genet i populasjonen med g.
4. **Mutasjon** - velg et tilfeldig gen g∈G og erstatt det med mutate(g)
5. Gjenta fra steg 2, til vi oppnår en tilstrekkelig lav verdi av fit, eller til grensen for antall steg er nådd.

## Typiske Oppgaver

Oppgaver som typisk løses med Genetiske Algoritmer inkluderer:

1. Optimalisering av tidsplaner
1. Optimal pakking
1. Optimal skjæring
1. Akselerering av uttømmende søk

## ✍️ Øvelser: Genetiske Algoritmer

Fortsett læringen i følgende notatbøker:

Gå til [denne notatboken](Genetic.ipynb) for å se to eksempler på bruk av Genetiske Algoritmer:

1. Rettferdig fordeling av skatter
1. 8-dronningers problemet

## Konklusjon

Genetiske Algoritmer brukes til å løse mange problemer, inkludert logistikk- og søkeproblemer. Feltet er inspirert av forskning som kombinerte emner innen psykologi og informatikk.

## 🚀 Utfordring

"Genetiske algoritmer er enkle å implementere, men deres oppførsel er vanskelig å forstå." [kilde](https://wikipedia.org/wiki/Genetic_algorithm) Gjør litt research for å finne en implementasjon av en genetisk algoritme, som for eksempel å løse et Sudoku-puslespill, og forklar hvordan det fungerer som en skisse eller flytskjema.

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Gjennomgang og Selvstudium

Se [denne flotte videoen](https://www.youtube.com/watch?v=qv6UVOQ0F44) som forklarer hvordan en datamaskin kan lære å spille Super Mario ved hjelp av nevrale nettverk trent med genetiske algoritmer. Vi skal lære mer om hvordan datamaskiner lærer å spille slike spill [i neste seksjon](../22-DeepRL/README.md).

## [Oppgave: Diofantisk Likning](Diophantine.ipynb)

Målet ditt er å løse den såkalte **Diofantiske likningen** - en likning med heltallsrøtter. For eksempel, vurder likningen a+2b+3c+4d=30. Du må finne heltallsrøttene som tilfredsstiller denne likningen.

*Denne oppgaven er inspirert av [denne artikkelen](https://habr.com/post/128704/).*

Tips:

1. Du kan vurdere røtter i intervallet [0;30]
1. Som et gen, vurder å bruke listen over rotverdier

Bruk [Diophantine.ipynb](Diophantine.ipynb) som utgangspunkt.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.