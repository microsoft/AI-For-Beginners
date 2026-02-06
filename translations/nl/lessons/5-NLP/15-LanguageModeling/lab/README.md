# Skip-Gram Model Trainen

Labopdracht uit [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Taak

In deze lab dagen we je uit om een Word2Vec-model te trainen met behulp van de Skip-Gram techniek. Train een netwerk met embeddings om naburige woorden te voorspellen in een Skip-Gram venster van $N$ tokens breed. Je kunt de [code uit deze les](../CBoW-TF.ipynb) gebruiken en deze licht aanpassen.

## De Dataset

Je mag elk boek gebruiken. Je kunt veel gratis teksten vinden op [Project Gutenberg](https://www.gutenberg.org/), bijvoorbeeld via deze directe link naar [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt)) van Lewis Carroll. Of je kunt de toneelstukken van Shakespeare gebruiken, die je kunt verkrijgen met de volgende code:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Verken!

Als je tijd hebt en dieper in het onderwerp wilt duiken, probeer dan de volgende dingen te onderzoeken:

* Hoe beïnvloedt de grootte van de embedding de resultaten?
* Hoe beïnvloeden verschillende tekststijlen het resultaat?
* Neem enkele zeer verschillende soorten woorden en hun synoniemen, verkrijg hun vectorrepresentaties, pas PCA toe om de dimensies te reduceren naar 2, en plot ze in een 2D-ruimte. Zie je patronen?

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.