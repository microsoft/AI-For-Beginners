# Trene Skip-Gram-modell

Laboppgave fra [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Oppgave

I denne labben utfordrer vi deg til å trene en Word2Vec-modell ved hjelp av Skip-Gram-teknikken. Tren et nettverk med embedding for å forutsi nabordene i et $N$-tokens bredt Skip-Gram-vindu. Du kan bruke [koden fra denne leksjonen](../CBoW-TF.ipynb) og gjøre små endringer.

## Datasettet

Du kan bruke hvilken som helst bok. Du finner mange gratis tekster på [Project Gutenberg](https://www.gutenberg.org/), for eksempel her er en direkte lenke til [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt)) av Lewis Carroll. Eller, du kan bruke Shakespeares skuespill, som du kan hente med følgende kode:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Utforsk!

Hvis du har tid og ønsker å gå dypere inn i emnet, prøv å utforske flere ting:

* Hvordan påvirker størrelsen på embedding resultatene?
* Hvordan påvirker ulike tekststiler resultatet?
* Ta flere veldig forskjellige typer ord og deres synonymer, skaff deres vektorrepresentasjoner, bruk PCA for å redusere dimensjonene til 2, og plott dem i et 2D-rom. Ser du noen mønstre?

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.