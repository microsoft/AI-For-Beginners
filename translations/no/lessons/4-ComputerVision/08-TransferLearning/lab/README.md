# Klassifisering av Oxford Pets ved bruk av Transfer Learning

Laboppgave fra [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Oppgave

Tenk deg at du skal utvikle en applikasjon for et dyrebarnehage for å katalogisere alle kjæledyr. En flott funksjon i en slik applikasjon ville være å automatisk oppdage rasen fra et fotografi. I denne oppgaven skal vi bruke transfer learning for å klassifisere bilder av ekte kjæledyr fra [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) kjæledyrdatasettet.

## Datasettet

Vi skal bruke det originale [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) kjæledyrdatasettet, som inneholder 35 forskjellige raser av hunder og katter.

For å laste ned datasettet, bruk denne kodebiten:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Starte Notebook

Start laben ved å åpne [OxfordPets.ipynb](OxfordPets.ipynb)

## Læringspunkt

Transfer learning og forhåndstrente nettverk gjør det mulig å løse reelle bildeklassifiseringsproblemer relativt enkelt. Likevel fungerer forhåndstrente nettverk best på bilder av lignende type, og hvis vi begynner å klassifisere veldig forskjellige bilder (f.eks. medisinske bilder), er det sannsynlig at vi får mye dårligere resultater.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.