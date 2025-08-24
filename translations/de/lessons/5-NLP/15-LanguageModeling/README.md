<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-24T09:31:56+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "de"
}
-->
# Sprachmodellierung

Semantische Einbettungen wie Word2Vec und GloVe sind tatsächlich ein erster Schritt in Richtung **Sprachmodellierung** – Modelle zu erstellen, die die Natur der Sprache irgendwie *verstehen* (oder *repräsentieren*).

## [Quiz vor der Vorlesung](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

Die Hauptidee hinter der Sprachmodellierung besteht darin, Modelle auf unbeschrifteten Datensätzen in einer unüberwachten Weise zu trainieren. Das ist wichtig, da uns riesige Mengen an unbeschriftetem Text zur Verfügung stehen, während die Menge an beschriftetem Text immer durch den Aufwand begrenzt ist, den wir für die Beschriftung aufbringen können. Meistens können wir Sprachmodelle erstellen, die **fehlende Wörter** im Text vorhersagen, da es einfach ist, ein zufälliges Wort im Text auszublenden und es als Trainingsbeispiel zu verwenden.

## Training von Einbettungen

In unseren bisherigen Beispielen haben wir vortrainierte semantische Einbettungen verwendet, aber es ist interessant zu sehen, wie diese Einbettungen trainiert werden können. Es gibt mehrere mögliche Ansätze, die verwendet werden können:

* **N-Gramm**-Sprachmodellierung, bei der wir ein Token vorhersagen, indem wir auf die N vorherigen Tokens (N-Gramm) schauen.
* **Continuous Bag-of-Words** (CBoW), bei dem wir das mittlere Token $W_0$ in einer Token-Sequenz $W_{-N}$, ..., $W_N$ vorhersagen.
* **Skip-Gram**, bei dem wir eine Menge benachbarter Tokens {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} aus dem mittleren Token $W_0$ vorhersagen.

![Bild aus einem Paper über die Umwandlung von Wörtern in Vektoren](../../../../../lessons/5-NLP/14-Embeddings/images/example-algorithms-for-converting-words-to-vectors.png)

> Bild aus [diesem Paper](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Beispiel-Notebooks: Training eines CBoW-Modells

Setze dein Lernen in den folgenden Notebooks fort:

* [Training von CBoW Word2Vec mit TensorFlow](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [Training von CBoW Word2Vec mit PyTorch](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Fazit

In der vorherigen Lektion haben wir gesehen, dass Wort-Einbettungen wie Magie funktionieren! Jetzt wissen wir, dass das Training von Wort-Einbettungen keine sehr komplexe Aufgabe ist, und wir sollten in der Lage sein, unsere eigenen Wort-Einbettungen für textspezifische Domänen zu trainieren, falls erforderlich.

## [Quiz nach der Vorlesung](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Rückblick & Selbststudium

* [Offizielles PyTorch-Tutorial zur Sprachmodellierung](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Offizielles TensorFlow-Tutorial zum Training eines Word2Vec-Modells](https://www.TensorFlow.org/tutorials/text/word2vec).
* Die Verwendung des **gensim**-Frameworks, um die am häufigsten verwendeten Einbettungen mit nur wenigen Codezeilen zu trainieren, wird [in dieser Dokumentation](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html) beschrieben.

## 🚀 [Aufgabe: Trainiere ein Skip-Gram-Modell](lab/README.md)

Im Labor fordern wir dich heraus, den Code aus dieser Lektion zu modifizieren, um ein Skip-Gram-Modell anstelle von CBoW zu trainieren. [Lies die Details](lab/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.