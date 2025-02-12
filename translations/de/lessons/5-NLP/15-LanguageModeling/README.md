# Sprachmodellierung

Semantische Einbettungen, wie Word2Vec und GloVe, sind in der Tat ein erster Schritt in Richtung **Sprachmodellierung** - Modelle zu erstellen, die irgendwie die Natur der Sprache *verstehen* (oder *darstellen*).

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

Die Hauptidee hinter der Sprachmodellierung besteht darin, sie auf unlabeled Datensätzen auf unüberwachtem Weg zu trainieren. Dies ist wichtig, da wir große Mengen an unlabeled Text zur Verfügung haben, während die Menge an labeled Text immer durch den Aufwand, den wir für das Labeling aufwenden können, begrenzt ist. Oft können wir Sprachmodelle erstellen, die **fehlende Wörter** im Text vorhersagen, da es einfach ist, ein zufälliges Wort im Text zu maskieren und es als Trainingsbeispiel zu verwenden.

## Einbettungen trainieren

In unseren vorherigen Beispielen haben wir vortrainierte semantische Einbettungen verwendet, aber es ist interessant zu sehen, wie diese Einbettungen trainiert werden können. Es gibt mehrere mögliche Ansätze, die verwendet werden können:

* **N-Gram** Sprachmodellierung, wenn wir ein Token vorhersagen, indem wir auf N vorherige Tokens (N-gram) schauen.
* **Continuous Bag-of-Words** (CBoW), wenn wir das mittlere Token $W_0$ in einer Token-Sequenz $W_{-N}$, ..., $W_N$ vorhersagen.
* **Skip-gram**, wo wir eine Menge benachbarter Tokens {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} aus dem mittleren Token $W_0$ vorhersagen.

![Bild aus dem Papier zur Umwandlung von Wörtern in Vektoren](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.de.png)

> Bild aus [diesem Papier](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Beispiel-Notebooks: CBoW-Modell trainieren

Setzen Sie Ihr Lernen in den folgenden Notebooks fort:

* [Training CBoW Word2Vec mit TensorFlow](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [Training CBoW Word2Vec mit PyTorch](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Fazit

In der vorherigen Lektion haben wir gesehen, dass Wort-Einbettungen wie Magie funktionieren! Jetzt wissen wir, dass das Trainieren von Wort-Einbettungen keine sehr komplexe Aufgabe ist und wir in der Lage sein sollten, unsere eigenen Wort-Einbettungen für domänenspezifischen Text zu trainieren, falls erforderlich.

## [Nachlese-Quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Überprüfung & Selbststudium

* [Offizielles PyTorch-Tutorial zur Sprachmodellierung](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Offizielles TensorFlow-Tutorial zum Training des Word2Vec-Modells](https://www.TensorFlow.org/tutorials/text/word2vec).
* Die Verwendung des **gensim**-Frameworks, um die am häufigsten verwendeten Einbettungen in wenigen Codezeilen zu trainieren, wird [in dieser Dokumentation](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html) beschrieben.

## 🚀 [Aufgabe: Trainiere Skip-Gram-Modell](lab/README.md)

Im Labor fordern wir Sie heraus, den Code aus dieser Lektion zu ändern, um ein Skip-Gram-Modell anstelle von CBoW zu trainieren. [Lesen Sie die Details](lab/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle angesehen werden. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.