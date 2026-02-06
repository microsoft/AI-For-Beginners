# Multi-klasseklassifisering med Perceptron

Laboppgave fra [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Oppgave

Ved å bruke koden vi har utviklet i denne leksjonen for binær klassifisering av MNIST-håndskrevne sifre, lag en multi-klasseklassifisering som kan gjenkjenne ethvert siffer. Beregn klassifiseringsnøyaktigheten på trenings- og testdatasettet, og skriv ut forvirringsmatrisen.

## Tips

1. For hvert siffer, opprett et datasett for binær klassifisering av "dette sifferet vs. alle andre sifre".
1. Tren 10 forskjellige perceptroner for binær klassifisering (ett for hvert siffer).
1. Definer en funksjon som kan klassifisere et inngangssiffer.

> **Hint**: Hvis vi kombinerer vektene til alle 10 perceptronene i én matrise, bør vi kunne bruke alle 10 perceptronene på inngangssifrene ved én matriseoperasjon. Det mest sannsynlige sifferet kan deretter finnes ved å bruke `argmax`-operasjonen på utdataene.

## Startnotatbok

Start laben ved å åpne [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.