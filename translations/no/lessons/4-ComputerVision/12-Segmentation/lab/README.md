# Segmentering av menneskekroppen

Laboppgave fra [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Oppgave

I videoproduksjon, for eksempel i værmeldinger, trenger vi ofte å klippe ut et bilde av en person fra kameraet og plassere det oppå annet materiale. Dette gjøres vanligvis ved hjelp av **chroma key**-teknikker, der en person filmes foran en ensfarget bakgrunn som deretter fjernes. I denne laben skal vi trene en nevralt nettverksmodell til å klippe ut silhuetten av en person.

## Datasettet

Vi skal bruke [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) fra Kaggle. Last ned datasettet manuelt fra Kaggle.

## Startnotatbok

Start laben ved å åpne [BodySegmentation.ipynb](BodySegmentation.ipynb)

## Læringspunkt

Segmentering av menneskekroppen er bare én av de vanlige oppgavene vi kan utføre med bilder av mennesker. Andre viktige oppgaver inkluderer **skjelettdeteksjon** og **posisjonsdeteksjon**. Sjekk ut [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)-biblioteket for å se hvordan disse oppgavene kan implementeres.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.