# Træning af Skip-Gram Model

Laboratorieopgave fra [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Opgave

I denne opgave udfordrer vi dig til at træne en Word2Vec-model ved hjælp af Skip-Gram-teknikken. Træn et netværk med embedding til at forudsige naboord i et $N$-tokens-bredt Skip-Gram-vindue. Du kan bruge [koden fra denne lektion](../CBoW-TF.ipynb) og foretage små ændringer.

## Datasættet

Du er velkommen til at bruge enhver bog. Du kan finde mange gratis tekster på [Project Gutenberg](https://www.gutenberg.org/), for eksempel er her et direkte link til [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt)) af Lewis Carroll. Eller du kan bruge Shakespeares skuespil, som du kan hente ved hjælp af følgende kode:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Udforsk!

Hvis du har tid og ønsker at gå dybere ind i emnet, så prøv at udforske flere ting:

* Hvordan påvirker embedding-størrelsen resultaterne?
* Hvordan påvirker forskellige tekststile resultatet?
* Tag flere meget forskellige typer ord og deres synonymer, opnå deres vektorrepræsentationer, anvend PCA for at reducere dimensionerne til 2, og plot dem i et 2D-rum. Ser du nogle mønstre?

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.