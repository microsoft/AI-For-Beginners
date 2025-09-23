<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9de7847385eeeda67cfdcce1640ab72",
  "translation_date": "2025-08-24T09:30:59+00:00",
  "source_file": "lessons/5-NLP/17-GenerativeNetworks/README.md",
  "language_code": "de"
}
-->
# Generative Netzwerke

## [Quiz vor der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/33)

Rekurrente Neuronale Netzwerke (RNNs) und ihre Varianten mit Gated Cells wie Long Short Term Memory Cells (LSTMs) und Gated Recurrent Units (GRUs) bieten einen Mechanismus für Sprachmodellierung, da sie die Wortreihenfolge lernen und Vorhersagen für das nächste Wort in einer Sequenz treffen können. Dies ermöglicht es uns, RNNs für **generative Aufgaben** zu nutzen, wie z. B. die Generierung von gewöhnlichem Text, maschinelle Übersetzung und sogar Bildbeschreibungen.

> ✅ Denke an all die Male, in denen du von generativen Aufgaben wie der automatischen Textvervollständigung profitiert hast. Recherchiere zu deinen Lieblingsanwendungen, um herauszufinden, ob sie RNNs verwendet haben.

In der RNN-Architektur, die wir in der vorherigen Einheit besprochen haben, erzeugte jede RNN-Einheit den nächsten versteckten Zustand als Ausgabe. Wir können jedoch auch eine weitere Ausgabe zu jeder rekurrenten Einheit hinzufügen, die es uns ermöglicht, eine **Sequenz** auszugeben (die genauso lang ist wie die ursprüngliche Sequenz). Darüber hinaus können wir RNN-Einheiten verwenden, die bei jedem Schritt keine Eingabe akzeptieren, sondern nur einen anfänglichen Zustandsvektor aufnehmen und dann eine Sequenz von Ausgaben erzeugen.

Dies ermöglicht verschiedene neuronale Architekturen, die im folgenden Bild dargestellt sind:

![Bild, das gängige Muster von rekurrenten neuronalen Netzwerken zeigt.](../../../../../lessons/5-NLP/17-GenerativeNetworks/images/unreasonable-effectiveness-of-rnn.jpg)

> Bild aus dem Blogpost [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) von [Andrej Karpaty](http://karpathy.github.io/)

* **One-to-one** ist ein traditionelles neuronales Netzwerk mit einer Eingabe und einer Ausgabe.
* **One-to-many** ist eine generative Architektur, die einen Eingabewert akzeptiert und eine Sequenz von Ausgabewerten erzeugt. Zum Beispiel, wenn wir ein **Bildbeschreibungsnetzwerk** trainieren möchten, das eine textuelle Beschreibung eines Bildes erzeugt, können wir ein Bild als Eingabe verwenden, es durch ein CNN leiten, um seinen versteckten Zustand zu erhalten, und dann eine rekurrente Kette Wort für Wort die Beschreibung generieren lassen.
* **Many-to-one** entspricht den RNN-Architekturen, die wir in der vorherigen Einheit beschrieben haben, wie z. B. Textklassifikation.
* **Many-to-many**, oder **Sequenz-zu-Sequenz**, entspricht Aufgaben wie der **maschinellen Übersetzung**, bei der ein erstes RNN alle Informationen aus der Eingabesequenz in den versteckten Zustand sammelt und eine andere RNN-Kette diesen Zustand in die Ausgabesequenz entfaltet.

In dieser Einheit konzentrieren wir uns auf einfache generative Modelle, die uns helfen, Text zu generieren. Der Einfachheit halber verwenden wir eine Tokenisierung auf Zeichenebene.

Wir werden dieses RNN trainieren, um Text Schritt für Schritt zu generieren. Bei jedem Schritt nehmen wir eine Zeichenfolge der Länge `nchars` und lassen das Netzwerk das nächste Zeichen für jedes Eingabezeichen generieren:

![Bild, das ein Beispiel für die RNN-Generierung des Wortes 'HELLO' zeigt.](../../../../../lessons/5-NLP/17-GenerativeNetworks/images/rnn-generate.png)

Beim Generieren von Text (während der Inferenz) beginnen wir mit einem **Prompt**, der durch die RNN-Zellen geleitet wird, um seinen Zwischenzustand zu erzeugen. Von diesem Zustand aus beginnt die Generierung. Wir generieren ein Zeichen nach dem anderen und übergeben den Zustand und das generierte Zeichen an eine weitere RNN-Zelle, um das nächste zu generieren, bis wir genügend Zeichen erzeugt haben.

<img src="images/rnn-generate-inf.png" width="60%"/>

> Bild vom Autor

## ✍️ Übungen: Generative Netzwerke

Setze dein Lernen in den folgenden Notebooks fort:

* [Generative Netzwerke mit PyTorch](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb)
* [Generative Netzwerke mit TensorFlow](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)

## Weiche Textgenerierung und Temperatur

Die Ausgabe jeder RNN-Zelle ist eine Wahrscheinlichkeitsverteilung von Zeichen. Wenn wir immer das Zeichen mit der höchsten Wahrscheinlichkeit als nächstes Zeichen im generierten Text auswählen, kann der Text oft in "Schleifen" geraten, in denen sich dieselben Zeichenfolgen immer wiederholen, wie in diesem Beispiel:

```
today of the second the company and a second the company ...
```

Wenn wir jedoch die Wahrscheinlichkeitsverteilung für das nächste Zeichen betrachten, könnte es sein, dass der Unterschied zwischen den höchsten Wahrscheinlichkeiten nicht groß ist, z. B. könnte ein Zeichen eine Wahrscheinlichkeit von 0,2 haben, ein anderes 0,19 usw. Zum Beispiel könnte das nächste Zeichen in der Sequenz '*play*' genauso gut ein Leerzeichen oder ein **e** sein (wie im Wort *player*).

Das führt uns zu der Erkenntnis, dass es nicht immer "fair" ist, das Zeichen mit der höchsten Wahrscheinlichkeit auszuwählen, da die Wahl des zweitwahrscheinlichsten Zeichens dennoch zu sinnvollem Text führen könnte. Es ist klüger, Zeichen aus der Wahrscheinlichkeitsverteilung zu **samplen**, die durch die Netzwerkausgabe gegeben ist. Wir können auch einen Parameter, die **Temperatur**, verwenden, um die Wahrscheinlichkeitsverteilung abzuflachen, falls wir mehr Zufälligkeit hinzufügen möchten, oder sie steiler machen, wenn wir uns stärker an die Zeichen mit der höchsten Wahrscheinlichkeit halten wollen.

Erforsche, wie diese weiche Textgenerierung in den oben verlinkten Notebooks implementiert ist.

## Fazit

Während die Textgenerierung an sich nützlich sein kann, liegen die Hauptvorteile in der Fähigkeit, Text mit RNNs aus einem anfänglichen Merkmalsvektor zu generieren. Zum Beispiel wird die Textgenerierung als Teil der maschinellen Übersetzung verwendet (Sequenz-zu-Sequenz, in diesem Fall wird der Zustandsvektor des *Encoders* verwendet, um die übersetzte Nachricht zu generieren oder zu *decodieren*), oder um eine textuelle Beschreibung eines Bildes zu erzeugen (in diesem Fall würde der Merkmalsvektor aus einem CNN-Extraktor stammen).

## 🚀 Herausforderung

Nimm an einigen Lektionen auf Microsoft Learn zu diesem Thema teil:

* Textgenerierung mit [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/34)

## Rückblick & Selbststudium

Hier sind einige Artikel, um dein Wissen zu erweitern:

* Verschiedene Ansätze zur Textgenerierung mit Markov-Ketten, LSTM und GPT-2: [Blogpost](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Beispiel zur Textgenerierung in der [Keras-Dokumentation](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Aufgabe](lab/README.md)

Wir haben gesehen, wie man Text Zeichen für Zeichen generiert. Im Labor wirst du die Textgenerierung auf Wortebene erkunden.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.