# Einbettungen

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/114)

Beim Training von Klassifikatoren, die auf BoW oder TF/IDF basieren, haben wir mit hochdimensionalen Bag-of-Words-Vektoren mit einer Länge von `vocab_size` gearbeitet und explizit von niedrigdimensionalen positionsbasierten Repräsentationsvektoren in spärliche One-Hot-Repräsentationen umgewandelt. Diese One-Hot-Repräsentation ist jedoch nicht speichereffizient. Darüber hinaus wird jedes Wort unabhängig voneinander behandelt, d.h. One-Hot-kodierte Vektoren drücken keine semantische Ähnlichkeit zwischen Wörtern aus.

Die Idee der **Einbettung** besteht darin, Wörter durch niederdimensionale dichte Vektoren darzustellen, die in gewisser Weise die semantische Bedeutung eines Wortes widerspiegeln. Wir werden später besprechen, wie man sinnvolle Wort-Einbettungen erstellt, aber für den Moment denken wir einfach an Einbettungen als eine Möglichkeit, die Dimensionalität eines Wortvektors zu verringern.

Die Einbettungsschicht würde ein Wort als Eingabe nehmen und einen Ausgabvektor der angegebenen `embedding_size` erzeugen. In gewissem Sinne ähnelt es einer `Linear`-Schicht, aber anstatt einen One-Hot-kodierten Vektor zu verwenden, kann es eine Wortnummer als Eingabe akzeptieren, was es uns ermöglicht, große One-Hot-kodierte Vektoren zu vermeiden.

Durch die Verwendung einer Einbettungsschicht als erste Schicht in unserem Klassifikator-Netzwerk können wir von einem Bag-of-Words- zu einem **Einbettungsbeutel**-Modell wechseln, bei dem wir zunächst jedes Wort in unserem Text in die entsprechende Einbettung umwandeln und dann eine aggregierte Funktion über all diese Einbettungen berechnen, wie z.B. `sum`, `average` oder `max`.  

![Bild, das einen Einbettungsklassifikator für fünf aufeinanderfolgende Wörter zeigt.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.de.png)

> Bild vom Autor

## ✍️ Übungen: Einbettungen

Setze dein Lernen in den folgenden Notebooks fort:
* [Einbettungen mit PyTorch](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb)
* [Einbettungen TensorFlow](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)

## Semantische Einbettungen: Word2Vec

Während die Einbettungsschicht gelernt hat, Wörter in Vektorrepräsentationen abzubilden, hatte diese Repräsentation nicht unbedingt viel semantische Bedeutung. Es wäre schön, eine Vektorrepräsentation zu lernen, sodass ähnliche Wörter oder Synonyme Vektoren entsprechen, die in Bezug auf eine bestimmte Vektordistanz (z.B. euklidische Distanz) nah beieinander liegen.

Um dies zu erreichen, müssen wir unser Einbettungsmodell auf eine bestimmte Weise auf einer großen Textsammlung vortrainieren. Eine Möglichkeit, semantische Einbettungen zu trainieren, nennt sich [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Es basiert auf zwei Hauptarchitekturen, die verwendet werden, um eine verteilte Repräsentation von Wörtern zu erzeugen:

 - **Kontinuierlicher Bag-of-Words** (CBoW) — In dieser Architektur trainieren wir das Modell, um ein Wort aus dem umgebenden Kontext vorherzusagen. Gegeben das ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$ besteht das Ziel des Modells darin, $W_0$ aus $(W_{-2},W_{-1},W_1,W_2)$ vorherzusagen.
 - **Kontinuierliches Skip-Gram** ist das Gegenteil von CBoW. Das Modell verwendet das umgebende Fenster von Kontextwörtern, um das aktuelle Wort vorherzusagen.

CBoW ist schneller, während Skip-Gram langsamer ist, aber eine bessere Darstellung seltener Wörter liefert.

![Bild, das sowohl CBoW- als auch Skip-Gram-Algorithmen zur Umwandlung von Wörtern in Vektoren zeigt.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.de.png)

> Bild aus [diesem Papier](https://arxiv.org/pdf/1301.3781.pdf)

Vortrainierte Word2Vec-Einbettungen (sowie andere ähnliche Modelle wie GloVe) können auch anstelle der Einbettungsschicht in neuronalen Netzwerken verwendet werden. Allerdings müssen wir uns mit Vokabularen auseinandersetzen, da das Vokabular, das zum Vortrainieren von Word2Vec/GloVe verwendet wird, wahrscheinlich von dem Vokabular in unserem Textkorpus abweicht. Sieh dir die oben genannten Notebooks an, um zu sehen, wie dieses Problem gelöst werden kann.

## Kontextuelle Einbettungen

Eine wesentliche Einschränkung traditioneller vortrainierter Einbettungsrepräsentationen wie Word2Vec ist das Problem der Mehrdeutigkeit von Wörtern. Während vortrainierte Einbettungen einige Bedeutungen von Wörtern im Kontext erfassen können, wird jede mögliche Bedeutung eines Wortes in der gleichen Einbettung kodiert. Dies kann Probleme in nachgelagerten Modellen verursachen, da viele Wörter, wie das Wort 'play', je nach verwendetem Kontext unterschiedliche Bedeutungen haben.

Zum Beispiel haben die Wörter 'play' in diesen beiden verschiedenen Sätzen eine ganz andere Bedeutung:

- Ich ging zu einem **Theaterstück**.
- John möchte mit seinen Freunden **spielen**.

Die vortrainierten Einbettungen oben repräsentieren beide Bedeutungen des Wortes 'play' in der gleichen Einbettung. Um diese Einschränkung zu überwinden, müssen wir Einbettungen auf der Grundlage des **Sprachmodells** erstellen, das auf einem großen Textkorpus trainiert wurde und *weiß*, wie Wörter in unterschiedlichen Kontexten zusammengefügt werden können. Die Diskussion über kontextuelle Einbettungen fällt außerhalb des Rahmens dieses Tutorials, aber wir werden später im Kurs darauf zurückkommen, wenn wir über Sprachmodelle sprechen.

## Fazit

In dieser Lektion hast du entdeckt, wie man Einbettungsschichten in TensorFlow und Pytorch erstellt und verwendet, um die semantischen Bedeutungen von Wörtern besser widerzuspiegeln.

## 🚀 Herausforderung

Word2Vec wurde für einige interessante Anwendungen verwendet, einschließlich der Generierung von Songtexten und Poesie. Schau dir [diesen Artikel](https://www.politetype.com/blog/word2vec-color-poems) an, der erklärt, wie der Autor Word2Vec zur Erstellung von Poesie verwendet hat. Schau dir auch [dieses Video von Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) an, um eine andere Erklärung dieser Technik zu entdecken. Versuche dann, diese Techniken auf deinen eigenen Textkorpus anzuwenden, vielleicht aus Kaggle.

## [Nachlese-Quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/214)

## Überprüfung & Selbststudium

Lies dir dieses Papier über Word2Vec durch: [Effiziente Schätzung von Wortdarstellungen im Vektorraum](https://arxiv.org/pdf/1301.3781.pdf)

## [Aufgabe: Notebooks](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.