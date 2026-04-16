# Training eines Skip-Gram-Modells

Laboraufgabe aus dem [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Aufgabe

In diesem Labor fordern wir Sie heraus, ein Word2Vec-Modell mit der Skip-Gram-Technik zu trainieren. Trainieren Sie ein Netzwerk mit Embedding, um benachbarte Wörter in einem $N$-Tokens-breiten Skip-Gram-Fenster vorherzusagen. Sie können den [Code aus dieser Lektion](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) verwenden und leicht anpassen.

## Der Datensatz

Sie können jedes beliebige Buch verwenden. Viele kostenlose Texte finden Sie bei [Project Gutenberg](https://www.gutenberg.org/), zum Beispiel gibt es hier einen direkten Link zu [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt)) von Lewis Carroll. Alternativ können Sie auch die Stücke von Shakespeare verwenden, die Sie mit folgendem Code abrufen können:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Erkunden Sie!

Wenn Sie Zeit haben und tiefer in das Thema eintauchen möchten, versuchen Sie, mehrere Dinge zu erforschen:

* Wie beeinflusst die Größe des Embeddings die Ergebnisse?
* Wie beeinflussen unterschiedliche Textstile das Ergebnis?
* Nehmen Sie mehrere sehr unterschiedliche Worttypen und deren Synonyme, erhalten Sie deren Vektorrepräsentationen, wenden Sie PCA an, um die Dimensionen auf 2 zu reduzieren, und plotten Sie sie im 2D-Raum. Erkennen Sie irgendwelche Muster?

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.