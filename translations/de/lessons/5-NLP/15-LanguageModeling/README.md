# Sprachmodellierung

Semantische Einbettungen wie Word2Vec und GloVe sind tatsächlich ein erster Schritt in Richtung **Sprachmodellierung** – Modelle zu erstellen, die irgendwie die *Natur* der Sprache *verstehen* (oder *repräsentieren*).

## [Quiz vor der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/29)

Die Hauptidee hinter der Sprachmodellierung besteht darin, Modelle auf nicht gekennzeichneten Datensätzen in einer unüberwachten Weise zu trainieren. Das ist wichtig, da wir riesige Mengen an unbeschriftetem Text zur Verfügung haben, während die Menge an beschriftetem Text immer durch den Aufwand begrenzt wäre, den wir für die Beschriftung aufbringen können. Meistens können wir Sprachmodelle erstellen, die **fehlende Wörter** im Text vorhersagen, da es einfach ist, ein zufälliges Wort im Text auszublenden und es als Trainingsbeispiel zu verwenden.

## Training von Einbettungen

In unseren vorherigen Beispielen haben wir vortrainierte semantische Einbettungen verwendet, aber es ist interessant zu sehen, wie diese Einbettungen trainiert werden können. Es gibt mehrere mögliche Ansätze, die verwendet werden können:

* **N-Gramm**-Sprachmodellierung, bei der wir ein Token vorhersagen, indem wir auf die N vorherigen Tokens schauen (N-Gramm).
* **Continuous Bag-of-Words** (CBoW), bei der wir das mittlere Token $W_0$ in einer Token-Sequenz $W_{-N}$, ..., $W_N$ vorhersagen.
* **Skip-Gramm**, bei dem wir eine Menge benachbarter Tokens {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} aus dem mittleren Token $W_0$ vorhersagen.

![Bild aus einer Arbeit über die Umwandlung von Wörtern in Vektoren](../../../../../translated_images/de/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> Bild aus [dieser Arbeit](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Beispiel-Notebooks: Training eines CBoW-Modells

Setze dein Lernen mit den folgenden Notebooks fort:

* [Training von CBoW Word2Vec mit TensorFlow](CBoW-TF.ipynb)
* [Training von CBoW Word2Vec mit PyTorch](CBoW-PyTorch.ipynb)

## Fazit

In der vorherigen Lektion haben wir gesehen, dass Wort-Einbettungen wie Magie funktionieren! Jetzt wissen wir, dass das Training von Wort-Einbettungen keine sehr komplexe Aufgabe ist, und wir sollten in der Lage sein, unsere eigenen Wort-Einbettungen für domänenspezifische Texte zu trainieren, falls erforderlich.

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Wiederholung & Selbststudium

* [Offizielles PyTorch-Tutorial zur Sprachmodellierung](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Offizielles TensorFlow-Tutorial zum Training eines Word2Vec-Modells](https://www.TensorFlow.org/tutorials/text/word2vec).
* Die Verwendung des **gensim**-Frameworks, um die am häufigsten verwendeten Einbettungen mit wenigen Codezeilen zu trainieren, wird [in dieser Dokumentation](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html) beschrieben.

## 🚀 [Aufgabe: Skip-Gramm-Modell trainieren](lab/README.md)

Im Labor fordern wir dich heraus, den Code aus dieser Lektion zu ändern, um ein Skip-Gramm-Modell anstelle von CBoW zu trainieren. [Lies die Details](lab/README.md)

---

