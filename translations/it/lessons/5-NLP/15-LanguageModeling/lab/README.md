# Addestramento del Modello Skip-Gram

Compito del laboratorio tratto dal [Curriculum AI for Beginners](https://github.com/microsoft/ai-for-beginners).

## Compito

In questo laboratorio, ti sfidiamo a addestrare un modello Word2Vec utilizzando la tecnica Skip-Gram. Addestra una rete con embedding per prevedere le parole vicine in una finestra Skip-Gram di $N$ token. Puoi utilizzare il [codice di questa lezione](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) e modificarlo leggermente.

## Il Dataset

Puoi utilizzare qualsiasi libro. Puoi trovare molti testi gratuiti su [Project Gutenberg](https://www.gutenberg.org/), ad esempio, ecco un link diretto a [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt) di Lewis Carroll. Oppure, puoi utilizzare le opere di Shakespeare, che puoi ottenere con il seguente codice:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Esplora!

Se hai tempo e vuoi approfondire l'argomento, prova a esplorare diversi aspetti:

* Come influisce la dimensione dell'embedding sui risultati?
* Come influiscono gli stili di testo diversi sui risultati?
* Prendi diversi tipi di parole molto differenti e i loro sinonimi, ottieni le loro rappresentazioni vettoriali, applica PCA per ridurre le dimensioni a 2 e tracciale in uno spazio 2D. Riesci a vedere qualche schema?

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un esperto umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.