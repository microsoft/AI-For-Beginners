<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e40b47ac3fd48f71304ede1474e66293",
  "translation_date": "2025-08-24T09:30:31+00:00",
  "source_file": "lessons/5-NLP/14-Embeddings/README.md",
  "language_code": "de"
}
-->
# Einbettungen

## [Quiz vor der Vorlesung](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/114)

Beim Training von Klassifikatoren basierend auf BoW oder TF/IDF arbeiteten wir mit hochdimensionalen Bag-of-Words-Vektoren der Länge `vocab_size` und konvertierten explizit von niedrigdimensionalen Positionsdarstellungsvektoren in spärliche One-Hot-Darstellungen. Diese One-Hot-Darstellung ist jedoch nicht speichereffizient. Außerdem wird jedes Wort unabhängig von den anderen behandelt, d. h. One-Hot-codierte Vektoren drücken keine semantische Ähnlichkeit zwischen Wörtern aus.

Die Idee der **Einbettung** besteht darin, Wörter durch niedrigdimensionale dichte Vektoren darzustellen, die irgendwie die semantische Bedeutung eines Wortes widerspiegeln. Später werden wir besprechen, wie man sinnvolle Wort-Einbettungen erstellt, aber vorerst betrachten wir Einbettungen einfach als eine Möglichkeit, die Dimensionalität eines Wortvektors zu reduzieren.

Die Einbettungsschicht würde also ein Wort als Eingabe nehmen und einen Ausgabesektor mit einer bestimmten `embedding_size` erzeugen. In gewisser Weise ist sie einer `Linear`-Schicht sehr ähnlich, aber anstatt einen One-Hot-codierten Vektor zu verwenden, kann sie eine Wortnummer als Eingabe akzeptieren, wodurch wir große One-Hot-codierte Vektoren vermeiden können.

Durch die Verwendung einer Einbettungsschicht als erste Schicht in unserem Klassifikator-Netzwerk können wir von einem Bag-of-Words-Modell zu einem **Embedding-Bag-Modell** wechseln, bei dem wir zunächst jedes Wort in unserem Text in die entsprechende Einbettung umwandeln und dann eine Aggregatfunktion über alle diese Einbettungen berechnen, wie z. B. `sum`, `average` oder `max`.

![Bild, das einen Einbettungsklassifikator für fünf Sequenzwörter zeigt.](../../../../../lessons/5-NLP/14-Embeddings/images/embedding-classifier-example.png)

> Bild vom Autor

## ✍️ Übungen: Einbettungen

Setze dein Lernen in den folgenden Notebooks fort:
* [Einbettungen mit PyTorch](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb)
* [Einbettungen TensorFlow](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)

## Semantische Einbettungen: Word2Vec

Während die Einbettungsschicht gelernt hat, Wörter in Vektordarstellungen zu überführen, hat diese Darstellung jedoch nicht unbedingt eine große semantische Bedeutung. Es wäre wünschenswert, eine Vektordarstellung zu lernen, bei der ähnliche Wörter oder Synonyme Vektoren entsprechen, die in Bezug auf eine Vektordistanz (z. B. euklidische Distanz) nahe beieinander liegen.

Um dies zu erreichen, müssen wir unser Einbettungsmodell auf einer großen Textsammlung in einer bestimmten Weise vortrainieren. Eine Methode, um semantische Einbettungen zu trainieren, wird [Word2Vec](https://en.wikipedia.org/wiki/Word2vec) genannt. Sie basiert auf zwei Hauptarchitekturen, die verwendet werden, um eine verteilte Darstellung von Wörtern zu erzeugen:

 - **Continuous Bag-of-Words** (CBoW) — In dieser Architektur trainieren wir das Modell, ein Wort aus dem umgebenden Kontext vorherzusagen. Gegeben das ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$, ist das Ziel des Modells, $W_0$ aus $(W_{-2},W_{-1},W_1,W_2)$ vorherzusagen.
 - **Continuous Skip-Gram** ist das Gegenteil von CBoW. Das Modell verwendet das umgebende Fenster von Kontextwörtern, um das aktuelle Wort vorherzusagen.

CBoW ist schneller, während Skip-Gram langsamer ist, aber eine bessere Darstellung von seltenen Wörtern liefert.

![Bild, das sowohl CBoW- als auch Skip-Gram-Algorithmen zur Umwandlung von Wörtern in Vektoren zeigt.](../../../../../lessons/5-NLP/14-Embeddings/images/example-algorithms-for-converting-words-to-vectors.png)

> Bild aus [diesem Paper](https://arxiv.org/pdf/1301.3781.pdf)

Word2Vec vortrainierte Einbettungen (sowie andere ähnliche Modelle wie GloVe) können auch anstelle der Einbettungsschicht in neuronalen Netzwerken verwendet werden. Allerdings müssen wir mit Vokabularen umgehen, da das Vokabular, das zum Vortrainieren von Word2Vec/GloVe verwendet wurde, wahrscheinlich von dem Vokabular in unserem Textkorpus abweicht. Schau dir die oben genannten Notebooks an, um zu sehen, wie dieses Problem gelöst werden kann.

## Kontextuelle Einbettungen

Eine zentrale Einschränkung traditioneller vortrainierter Einbettungsdarstellungen wie Word2Vec ist das Problem der Wortbedeutungsunterscheidung. Während vortrainierte Einbettungen einen Teil der Bedeutung von Wörtern im Kontext erfassen können, wird jede mögliche Bedeutung eines Wortes in derselben Einbettung kodiert. Dies kann in nachgelagerten Modellen Probleme verursachen, da viele Wörter, wie das Wort 'play', je nach Kontext unterschiedliche Bedeutungen haben.

Zum Beispiel hat das Wort 'play' in diesen beiden Sätzen eine ganz unterschiedliche Bedeutung:

- Ich ging zu einem **Theaterstück**.
- John möchte mit seinen Freunden **spielen**.

Die oben genannten vortrainierten Einbettungen repräsentieren beide Bedeutungen des Wortes 'play' in derselben Einbettung. Um diese Einschränkung zu überwinden, müssen wir Einbettungen basierend auf dem **Sprachmodell** erstellen, das auf einem großen Textkorpus trainiert wurde und *weiß*, wie Wörter in verschiedenen Kontexten zusammengefügt werden können. Die Diskussion über kontextuelle Einbettungen liegt außerhalb des Rahmens dieses Tutorials, aber wir werden darauf zurückkommen, wenn wir später im Kurs über Sprachmodelle sprechen.

## Fazit

In dieser Lektion hast du gelernt, wie man Einbettungsschichten in TensorFlow und PyTorch erstellt und verwendet, um die semantische Bedeutung von Wörtern besser widerzuspiegeln.

## 🚀 Herausforderung

Word2Vec wurde für einige interessante Anwendungen verwendet, einschließlich der Generierung von Songtexten und Gedichten. Schau dir [diesen Artikel](https://www.politetype.com/blog/word2vec-color-poems) an, der erklärt, wie der Autor Word2Vec verwendet hat, um Gedichte zu generieren. Sieh dir auch [dieses Video von Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) an, um eine andere Erklärung dieser Technik zu entdecken. Versuche dann, diese Techniken auf deinen eigenen Textkorpus anzuwenden, vielleicht aus Kaggle.

## [Quiz nach der Vorlesung](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/214)

## Wiederholung & Selbststudium

Lies dieses Paper über Word2Vec: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [Aufgabe: Notebooks](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.