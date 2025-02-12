# Training Skip-Gram Modell

Laboraufgabe aus dem [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Aufgabe

In diesem Labor fordern wir dich heraus, ein Word2Vec-Modell mit der Skip-Gram-Technik zu trainieren. Trainiere ein Netzwerk mit Einbettungen, um benachbarte Wörter in einem $N$-Tokens-breiten Skip-Gram-Fenster vorherzusagen. Du kannst [den Code aus dieser Lektion](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) verwenden und ihn leicht anpassen.

## Der Datensatz

Du kannst jedes Buch verwenden. Viele kostenlose Texte findest du bei [Project Gutenberg](https://www.gutenberg.org/), zum Beispiel hier ist ein direkter Link zu [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt) von Lewis Carroll. Oder du kannst die Stücke von Shakespeare verwenden, die du mit dem folgenden Code erhalten kannst:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Erforschen!

Wenn du Zeit hast und tiefer in das Thema eintauchen möchtest, versuche mehrere Dinge zu erkunden:

* Wie beeinflusst die Größe der Einbettung die Ergebnisse?
* Wie beeinflussen verschiedene Textstile das Ergebnis?
* Nimm mehrere sehr unterschiedliche Wortarten und deren Synonyme, erhalte ihre Vektordarstellungen, wende PCA an, um die Dimensionen auf 2 zu reduzieren, und plotiere sie im 2D-Raum. Siehst du irgendwelche Muster?

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, sollten Sie sich bewusst sein, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als autoritative Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.