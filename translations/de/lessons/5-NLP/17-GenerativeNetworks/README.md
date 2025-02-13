# Generative Netzwerke

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/117)

Recurrent Neural Networks (RNNs) und ihre gated Cell-Varianten wie Long Short Term Memory Cells (LSTMs) und Gated Recurrent Units (GRUs) bieten einen Mechanismus für das Sprachmodellieren, da sie die Wortreihenfolge lernen und Vorhersagen für das nächste Wort in einer Sequenz machen können. Dies ermöglicht es uns, RNNs für **generative Aufgaben** zu verwenden, wie zum Beispiel die gewöhnliche Textgenerierung, maschinelle Übersetzung und sogar Bildbeschriftung.

> ✅ Denk darüber nach, wie oft du von generativen Aufgaben wie der Textvervollständigung beim Tippen profitiert hast. Recherchiere deine Lieblingsanwendungen, um zu sehen, ob sie RNNs genutzt haben.

In der RNN-Architektur, die wir in der vorherigen Einheit besprochen haben, erzeugte jede RNN-Einheit den nächsten verborgenen Zustand als Ausgabe. Wir können jedoch auch eine weitere Ausgabe zu jeder rekurrenten Einheit hinzufügen, die es uns ermöglichen würde, eine **Sequenz** auszugeben (die in der Länge der ursprünglichen Sequenz entspricht). Darüber hinaus können wir RNN-Einheiten verwenden, die nicht bei jedem Schritt eine Eingabe akzeptieren, sondern einfach einen anfänglichen Zustandsvektor nehmen und dann eine Sequenz von Ausgaben erzeugen.

Dies ermöglicht verschiedene neuronale Architekturen, die im Bild unten gezeigt sind:

![Bild, das gängige Muster rekurrenter neuronaler Netzwerke zeigt.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.de.jpg)

> Bild aus dem Blogbeitrag [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) von [Andrej Karpaty](http://karpathy.github.io/)

* **Eins-zu-eins** ist ein traditionelles neuronales Netzwerk mit einer Eingabe und einer Ausgabe
* **Eins-zu-viele** ist eine generative Architektur, die einen Eingabewert akzeptiert und eine Sequenz von Ausgabewerten erzeugt. Wenn wir beispielsweise ein **Bildbeschriftungs**-Netzwerk trainieren möchten, das eine textuelle Beschreibung eines Bildes erzeugt, können wir ein Bild als Eingabe nehmen, es durch ein CNN leiten, um seinen verborgenen Zustand zu erhalten, und dann eine rekursive Kette verwenden, um die Beschriftung Wort für Wort zu generieren
* **Viele-zu-eins** entspricht den RNN-Architekturen, die wir in der vorherigen Einheit beschrieben haben, wie z.B. der Textklassifikation
* **Viele-zu-viele**, oder **Sequenz-zu-Sequenz**, entspricht Aufgaben wie **maschineller Übersetzung**, bei denen wir zuerst ein RNN haben, das alle Informationen aus der Eingabesequenz in den verborgenen Zustand aufnimmt, und eine andere RNN-Kette diesen Zustand in die Ausgabesequenz entrollt.

In dieser Einheit werden wir uns auf einfache generative Modelle konzentrieren, die uns helfen, Text zu generieren. Zur Vereinfachung verwenden wir die Zeichenebene Tokenisierung.

Wir werden dieses RNN trainieren, um Text Schritt für Schritt zu generieren. Bei jedem Schritt nehmen wir eine Sequenz von Zeichen der Länge `nchars` und bitten das Netzwerk, das nächste Ausgabesymbol für jedes Eingabesymbol zu generieren:

![Bild, das ein Beispiel für die RNN-Generierung des Wortes 'HELLO' zeigt.](../../../../../translated_images/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.de.png)

Beim Generieren von Text (während der Inferenz) beginnen wir mit einem **Prompt**, der durch RNN-Zellen geleitet wird, um seinen Zwischenzustand zu erzeugen, und dann beginnt die Generierung von diesem Zustand. Wir generieren ein Zeichen nach dem anderen und übergeben den Zustand und das generierte Zeichen an eine andere RNN-Zelle, um das nächste zu generieren, bis wir genügend Zeichen generiert haben.

<img src="images/rnn-generate-inf.png" width="60%"/>

> Bild vom Autor

## ✍️ Übungen: Generative Netzwerke

Setze dein Lernen in den folgenden Notebooks fort:

* [Generative Netzwerke mit PyTorch](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb)
* [Generative Netzwerke mit TensorFlow](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)

## Sanfte Textgenerierung und Temperatur

Die Ausgabe jeder RNN-Zelle ist eine Wahrscheinlichkeitsverteilung von Zeichen. Wenn wir immer das Zeichen mit der höchsten Wahrscheinlichkeit als nächstes Zeichen im generierten Text nehmen, kann der Text oft zwischen denselben Zeichenfolgen "zyklisch" werden, wie in diesem Beispiel:

```
today of the second the company and a second the company ...
```

Wenn wir jedoch die Wahrscheinlichkeitsverteilung für das nächste Zeichen betrachten, könnte es sein, dass der Unterschied zwischen den höchsten Wahrscheinlichkeiten nicht groß ist, z.B. könnte ein Zeichen eine Wahrscheinlichkeit von 0.2 haben, ein anderes - 0.19, usw. Wenn wir nach dem nächsten Zeichen in der Sequenz '*play*' suchen, könnte das nächste Zeichen ebenso gut ein Leerzeichen oder **e** (wie im Wort *player*) sein.

Dies führt uns zu dem Schluss, dass es nicht immer "fair" ist, das Zeichen mit der höheren Wahrscheinlichkeit auszuwählen, da die Wahl des zweithöchsten uns immer noch zu bedeutungsvollem Text führen könnte. Es ist klüger, Zeichen aus der Wahrscheinlichkeitsverteilung zu **sample**n, die durch die Netzwerkausgabe gegeben wird. Wir können auch einen Parameter, **Temperatur**, verwenden, der die Wahrscheinlichkeitsverteilung abflacht, falls wir mehr Zufälligkeit hinzufügen möchten, oder sie steiler machen, wenn wir uns mehr an den Zeichen mit der höchsten Wahrscheinlichkeit orientieren möchten.

Erforsche, wie diese sanfte Textgenerierung in den oben verlinkten Notebooks implementiert ist.

## Fazit

Obwohl die Textgenerierung an sich nützlich sein kann, kommen die größten Vorteile von der Fähigkeit, Text mithilfe von RNNs aus einem anfänglichen Merkmalsvektor zu generieren. Zum Beispiel wird die Textgenerierung als Teil der maschinellen Übersetzung verwendet (Sequenz-zu-Sequenz, in diesem Fall wird der Zustandsvektor aus dem *Encoder* verwendet, um die übersetzte Nachricht zu generieren oder *zu dekodieren*), oder um eine textuelle Beschreibung eines Bildes zu erzeugen (in diesem Fall würde der Merkmalsvektor aus dem CNN-Extractor stammen).

## 🚀 Herausforderung

Nehmt an einigen Lektionen auf Microsoft Learn zu diesem Thema teil

* Textgenerierung mit [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Nachlesequiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/217)

## Überprüfung & Selbststudium

Hier sind einige Artikel, um dein Wissen zu erweitern

* Verschiedene Ansätze zur Textgenerierung mit Markov-Kette, LSTM und GPT-2: [Blogbeitrag](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Textgenerierungsbeispiel in der [Keras-Dokumentation](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Aufgabe](lab/README.md)

Wir haben gesehen, wie man Text Zeichen für Zeichen generiert. Im Labor wirst du die Textgenerierung auf Wortebene erkunden.

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.