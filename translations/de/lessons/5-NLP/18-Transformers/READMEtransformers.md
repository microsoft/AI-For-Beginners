# Aufmerksamkeitsmechanismen und Transformer

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/118)

Eines der wichtigsten Probleme im Bereich der NLP ist die **maschinelle Übersetzung**, eine grundlegende Aufgabe, die Tools wie Google Translate zugrunde liegt. In diesem Abschnitt konzentrieren wir uns auf maschinelle Übersetzung oder, allgemeiner, auf jede *Sequenz-zu-Sequenz*-Aufgabe (die auch als **Satztransduktion** bezeichnet wird).

Bei RNNs wird Sequenz-zu-Sequenz durch zwei rekursive Netzwerke implementiert, wobei ein Netzwerk, der **Encoder**, eine Eingabesequenz in einen verborgenen Zustand zusammenfasst, während ein anderes Netzwerk, der **Decoder**, diesen verborgenen Zustand in ein übersetztes Ergebnis entfaltet. Es gibt einige Probleme mit diesem Ansatz:

* Der endgültige Zustand des Encoder-Netzwerks hat Schwierigkeiten, sich an den Anfang eines Satzes zu erinnern, was zu einer schlechten Modellqualität bei langen Sätzen führt.
* Alle Wörter in einer Sequenz haben den gleichen Einfluss auf das Ergebnis. In der Realität haben jedoch bestimmte Wörter in der Eingabesequenz oft einen größeren Einfluss auf die sequenziellen Ausgaben als andere.

**Aufmerksamkeitsmechanismen** bieten ein Mittel, um den kontextuellen Einfluss jedes Eingangsvektors auf jede Vorhersageausgabe des RNN zu gewichten. Die Implementierung erfolgt durch die Schaffung von Abkürzungen zwischen den Zwischenzuständen des Eingangs-RNN und dem Ausgangs-RNN. Auf diese Weise berücksichtigen wir beim Generieren des Ausgabesymbols y<sub>t</sub> alle Eingangsversteckzustände h<sub>i</sub> mit unterschiedlichen Gewichtungskoeffizienten α<sub>t,i</sub>.

![Bild, das ein Encoder/Decoder-Modell mit einer additiven Aufmerksamkeitschicht zeigt](../../../../../translated_images/encoder-decoder-attention.7a726296894fb567aa2898c94b17b3289087f6705c11907df8301df9e5eeb3de.de.png)

> Das Encoder-Decoder-Modell mit dem additiven Aufmerksamkeitsmechanismus in [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf), zitiert aus [diesem Blogbeitrag](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)

Die Aufmerksamkeitsmatrix {α<sub>i,j</sub>} würde den Grad darstellen, in dem bestimmte Eingabewörter an der Generierung eines bestimmten Wortes in der Ausgabesequenz beteiligt sind. Im Folgenden finden Sie ein Beispiel für eine solche Matrix:

![Bild, das eine Beispielausrichtung zeigt, die von RNNsearch-50 gefunden wurde, entnommen von Bahdanau - arviz.org](../../../../../translated_images/bahdanau-fig3.09ba2d37f202a6af11de6c82d2d197830ba5f4528d9ea430eb65fd3a75065973.de.png)

> Abbildung aus [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf) (Fig.3)

Aufmerksamkeitsmechanismen sind für einen Großteil des aktuellen oder nahezu aktuellen Stands der Technik im NLP verantwortlich. Die Hinzufügung von Aufmerksamkeit erhöht jedoch erheblich die Anzahl der Modellparameter, was zu Skalierungsproblemen bei RNNs führte. Eine wichtige Einschränkung bei der Skalierung von RNNs ist, dass die rekursive Natur der Modelle es schwierig macht, das Training zu batchen und zu parallelisieren. In einem RNN muss jedes Element einer Sequenz in sequentieller Reihenfolge verarbeitet werden, was bedeutet, dass es nicht leicht parallelisiert werden kann.

![Encoder Decoder mit Aufmerksamkeit](../../../../../lessons/5-NLP/18-Transformers/images/EncDecAttention.gif)

> Abbildung aus [Google's Blog](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)

Die Einführung von Aufmerksamkeitsmechanismen in Kombination mit dieser Einschränkung führte zur Schaffung der heutigen State-of-the-Art-Transformer-Modelle, die wir kennen und verwenden, wie BERT und Open-GPT3.

## Transformermodelle

Eine der Hauptideen hinter Transformern ist es, die sequentielle Natur von RNNs zu vermeiden und ein Modell zu schaffen, das während des Trainings parallelisierbar ist. Dies wird erreicht, indem zwei Ideen implementiert werden:

* Positionskodierung
* Verwendung des Selbstaufmerksamkeitsmechanismus zur Erfassung von Mustern anstelle von RNNs (oder CNNs) (deshalb heißt das Papier, das Transformer einführt, *[Attention is all you need](https://arxiv.org/abs/1706.03762)*)

### Positionskodierung/Einbettung

Die Idee der Positionskodierung ist die folgende. 
1. Bei der Verwendung von RNNs wird die relative Position der Tokens durch die Anzahl der Schritte dargestellt und muss daher nicht explizit dargestellt werden. 
2. Sobald wir jedoch zu Aufmerksamkeit wechseln, müssen wir die relativen Positionen der Tokens innerhalb einer Sequenz kennen. 
3. Um die Positionskodierung zu erhalten, erweitern wir unsere Sequenz von Tokens um eine Sequenz von Tokenpositionen in der Sequenz (d.h. eine Sequenz von Zahlen 0,1, ...).
4. Wir mischen dann die Tokenposition mit einem Token-Einbettungsvektor. Um die Position (ganzzahlig) in einen Vektor zu transformieren, können wir verschiedene Ansätze verwenden:

* Trainierbare Einbettung, ähnlich wie bei der Token-Einbettung. Dies ist der Ansatz, den wir hier betrachten. Wir wenden Einbettungsschichten auf sowohl die Tokens als auch ihre Positionen an, was zu Einbettungsvektoren der gleichen Dimensionen führt, die wir dann zusammenaddieren.
* Feste Positionskodierungsfunktion, wie im ursprünglichen Papier vorgeschlagen.

<img src="images/pos-embedding.png" width="50%"/>

> Bild des Autors

Das Ergebnis, das wir mit der Positions-Einbettung erhalten, bettet sowohl das ursprüngliche Token als auch seine Position innerhalb einer Sequenz ein.

### Multi-Head Selbstaufmerksamkeit

Als Nächstes müssen wir einige Muster innerhalb unserer Sequenz erfassen. Dazu verwenden Transformer einen **Selbstaufmerksamkeits**mechanismus, der im Wesentlichen Aufmerksamkeit auf die gleiche Sequenz anwendet, die als Eingabe und Ausgabe dient. Die Anwendung von Selbstaufmerksamkeit ermöglicht es uns, den **Kontext** innerhalb des Satzes zu berücksichtigen und zu sehen, welche Wörter miteinander in Beziehung stehen. Zum Beispiel ermöglicht es uns zu sehen, welche Wörter durch Kofe referenziert werden, wie *es*, und auch den Kontext zu berücksichtigen:

![](../../../../../translated_images/CoreferenceResolution.861924d6d384a7d68d8d0039d06a71a151f18a796b8b1330239d3590bd4947eb.de.png)

> Bild aus dem [Google Blog](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)

In Transformern verwenden wir **Multi-Head Attention**, um dem Netzwerk die Fähigkeit zu geben, mehrere verschiedene Arten von Abhängigkeiten zu erfassen, z.B. langfristige vs. kurzfristige Wortbeziehungen, Kofeferenz vs. etwas anderes usw.

[TensorFlow Notebook](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb) enthält weitere Details zur Implementierung von Transformerschichten.

### Encoder-Decoder-Aufmerksamkeit

In Transformern wird Aufmerksamkeit an zwei Stellen verwendet:

* Um Muster innerhalb des Eingabetextes mit Selbstaufmerksamkeit zu erfassen
* Um die Sequenzübersetzung durchzuführen - es ist die Aufmerksamkeitschicht zwischen Encoder und Decoder.

Die Encoder-Decoder-Aufmerksamkeit ähnelt sehr dem Aufmerksamkeitsmechanismus, der in RNNs verwendet wird, wie zu Beginn dieses Abschnitts beschrieben. Dieses animierte Diagramm erklärt die Rolle der Encoder-Decoder-Aufmerksamkeit.

![Animiertes GIF, das zeigt, wie die Bewertungen in Transformermodellen durchgeführt werden.](../../../../../lessons/5-NLP/18-Transformers/images/transformer-animated-explanation.gif)

Da jede Eingabeposition unabhängig auf jede Ausgabeposition abgebildet wird, können Transformer besser parallelisieren als RNNs, was viel größere und ausdrucksstärkere Sprachmodelle ermöglicht. Jeder Aufmerksamkeitskopf kann verwendet werden, um verschiedene Beziehungen zwischen Wörtern zu lernen, die nachgelagerte Aufgaben der natürlichen Sprachverarbeitung verbessern.

## BERT

**BERT** (Bidirektionale Encoder-Darstellungen von Transformern) ist ein sehr großes, mehrschichtiges Transformernetzwerk mit 12 Schichten für *BERT-base* und 24 für *BERT-large*. Das Modell wird zunächst auf einem großen Korpus von Textdaten (Wikipedia + Bücher) mit unüberwachtem Training (Vorhersage maskierter Wörter in einem Satz) vortrainiert. Während des Vortrainings absorbiert das Modell erhebliche Niveaus des Sprachverständnisses, die dann mit anderen Datensätzen durch Feinabstimmung genutzt werden können. Dieser Prozess wird als **Transferlernen** bezeichnet.

![Bild von http://jalammar.github.io/illustrated-bert/](../../../../../translated_images/jalammarBERT-language-modeling-masked-lm.34f113ea5fec4362e39ee4381aab7cad06b5465a0b5f053a0f2aa05fbe14e746.de.png)

> Bild [Quelle](http://jalammar.github.io/illustrated-bert/)

## ✍️ Übungen: Transformer

Setzen Sie Ihr Lernen in den folgenden Notebooks fort:

* [Transformers in PyTorch](../../../../../lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb)
* [Transformers in TensorFlow](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb)

## Fazit

In dieser Lektion haben Sie über Transformer und Aufmerksamkeitsmechanismen gelernt, alles wesentliche Werkzeuge im NLP-Toolkit. Es gibt viele Variationen von Transformer-Architekturen, darunter BERT, DistilBERT, BigBird, OpenGPT3 und mehr, die feinabgestimmt werden können. Das [HuggingFace-Paket](https://github.com/huggingface/) bietet ein Repository zum Trainieren vieler dieser Architekturen sowohl mit PyTorch als auch mit TensorFlow.

## 🚀 Herausforderung

## [Nachlesequiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/218)

## Überprüfung & Selbststudium

* [Blogbeitrag](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/), der das klassische [Attention is all you need](https://arxiv.org/abs/1706.03762) Papier über Transformer erklärt.
* [Eine Reihe von Blogbeiträgen](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452) über Transformer, die die Architektur im Detail erklären.

## [Aufgabe](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, bitten wir zu beachten, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.