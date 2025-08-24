<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58bf4adb210aab53e8f78c8082040e7c",
  "translation_date": "2025-08-24T09:29:56+00:00",
  "source_file": "lessons/5-NLP/16-RNN/README.md",
  "language_code": "de"
}
-->
# Rekurrente Neuronale Netze

## [Quiz vor der Vorlesung](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/116)

In den vorherigen Abschnitten haben wir reichhaltige semantische Repräsentationen von Text und einen einfachen linearen Klassifikator auf den Einbettungen verwendet. Diese Architektur erfasst die aggregierte Bedeutung der Wörter in einem Satz, berücksichtigt jedoch nicht die **Reihenfolge** der Wörter, da die Aggregationsoperation auf den Einbettungen diese Information aus dem ursprünglichen Text entfernt hat. Da diese Modelle die Wortreihenfolge nicht modellieren können, sind sie nicht in der Lage, komplexere oder mehrdeutige Aufgaben wie Textgenerierung oder Beantwortung von Fragen zu lösen.

Um die Bedeutung einer Textsequenz zu erfassen, müssen wir eine andere Architektur neuronaler Netze verwenden, die als **rekurrentes neuronales Netz** oder RNN bezeichnet wird. Im RNN führen wir unseren Satz ein Symbol nach dem anderen durch das Netzwerk, und das Netzwerk erzeugt einen **Zustand**, den wir dann mit dem nächsten Symbol erneut in das Netzwerk einspeisen.

![RNN](../../../../../lessons/5-NLP/16-RNN/images/rnn.png)

> Bild vom Autor

Angenommen, wir haben eine Eingabesequenz von Token X<sub>0</sub>,...,X<sub>n</sub>, erstellt RNN eine Sequenz von neuronalen Netzwerkblöcken und trainiert diese Sequenz end-to-end mittels Backpropagation. Jeder Netzwerkblock nimmt ein Paar (X<sub>i</sub>,S<sub>i</sub>) als Eingabe und erzeugt S<sub>i+1</sub> als Ergebnis. Der finale Zustand S<sub>n</sub> oder (Ausgabe Y<sub>n</sub>) wird in einen linearen Klassifikator eingespeist, um das Ergebnis zu erzeugen. Alle Netzwerkblöcke teilen sich die gleichen Gewichte und werden end-to-end mit einem Backpropagation-Durchlauf trainiert.

Da die Zustandsvektoren S<sub>0</sub>,...,S<sub>n</sub> durch das Netzwerk weitergegeben werden, kann es die sequentiellen Abhängigkeiten zwischen Wörtern lernen. Zum Beispiel, wenn das Wort *nicht* irgendwo in der Sequenz erscheint, kann es lernen, bestimmte Elemente im Zustandsvektor zu negieren, was zu einer Verneinung führt.

> ✅ Da die Gewichte aller RNN-Blöcke im obigen Bild geteilt werden, kann dasselbe Bild als ein Block (rechts) mit einer rekurrenten Rückkopplungsschleife dargestellt werden, die den Ausgabestatus des Netzwerks zurück an die Eingabe weitergibt.

## Anatomie einer RNN-Zelle

Schauen wir uns an, wie eine einfache RNN-Zelle organisiert ist. Sie akzeptiert den vorherigen Zustand S<sub>i-1</sub> und das aktuelle Symbol X<sub>i</sub> als Eingaben und muss den Ausgabestatus S<sub>i</sub> erzeugen (und manchmal sind wir auch an einer anderen Ausgabe Y<sub>i</sub> interessiert, wie im Fall von generativen Netzwerken).

Eine einfache RNN-Zelle hat zwei Gewichtsmatrizen: eine transformiert ein Eingabesymbol (wir nennen sie W), und eine andere transformiert einen Eingabezustand (H). In diesem Fall wird die Ausgabe des Netzwerks als σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b) berechnet, wobei σ die Aktivierungsfunktion ist und b ein zusätzlicher Bias.

<img alt="Anatomie einer RNN-Zelle" src="images/rnn-anatomy.png" width="50%"/>

> Bild vom Autor

In vielen Fällen werden Eingabetoken vor dem Eintritt in das RNN durch die Einbettungsschicht geleitet, um die Dimensionalität zu reduzieren. In diesem Fall, wenn die Dimension der Eingabevektoren *emb_size* ist und der Zustandsvektor *hid_size* ist - beträgt die Größe von W *emb_size*×*hid_size*, und die Größe von H ist *hid_size*×*hid_size*.

## Long Short Term Memory (LSTM)

Eines der Hauptprobleme klassischer RNNs ist das sogenannte **Vanishing-Gradients-Problem**. Da RNNs end-to-end in einem Backpropagation-Durchlauf trainiert werden, fällt es ihnen schwer, Fehler an die ersten Schichten des Netzwerks weiterzuleiten, und das Netzwerk kann daher keine Beziehungen zwischen weit entfernten Token lernen. Eine Möglichkeit, dieses Problem zu vermeiden, besteht darin, eine **explizite Zustandsverwaltung** durch sogenannte **Gates** einzuführen. Es gibt zwei bekannte Architekturen dieser Art: **Long Short Term Memory** (LSTM) und **Gated Relay Unit** (GRU).

![Bild eines Beispiels einer Long Short Term Memory-Zelle](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Bildquelle TBD

Das LSTM-Netzwerk ist ähnlich wie ein RNN organisiert, aber es gibt zwei Zustände, die von Schicht zu Schicht weitergegeben werden: den tatsächlichen Zustand C und den versteckten Vektor H. In jeder Einheit wird der versteckte Vektor H<sub>i</sub> mit der Eingabe X<sub>i</sub> verkettet, und sie steuern, was mit dem Zustand C über **Gates** geschieht. Jedes Gate ist ein neuronales Netzwerk mit Sigmoid-Aktivierung (Ausgabe im Bereich [0,1]), das als bitweises Maskieren betrachtet werden kann, wenn es mit dem Zustandsvektor multipliziert wird. Es gibt die folgenden Gates (von links nach rechts im obigen Bild):

* Das **Vergessens-Gate** nimmt einen versteckten Vektor und bestimmt, welche Komponenten des Vektors C wir vergessen und welche wir durchlassen müssen.
* Das **Eingabe-Gate** nimmt einige Informationen aus den Eingabe- und versteckten Vektoren und fügt sie in den Zustand ein.
* Das **Ausgabe-Gate** transformiert den Zustand über eine lineare Schicht mit *tanh*-Aktivierung und wählt dann einige seiner Komponenten mithilfe eines versteckten Vektors H<sub>i</sub> aus, um einen neuen Zustand C<sub>i+1</sub> zu erzeugen.

Komponenten des Zustands C können als Flags betrachtet werden, die ein- und ausgeschaltet werden können. Zum Beispiel, wenn wir in der Sequenz den Namen *Alice* finden, könnten wir annehmen, dass es sich um eine weibliche Figur handelt, und das Flag im Zustand setzen, dass wir ein weibliches Substantiv im Satz haben. Wenn wir später die Phrase *und Tom* finden, setzen wir das Flag, dass wir ein Plural-Substantiv haben. Durch die Manipulation des Zustands können wir also möglicherweise die grammatikalischen Eigenschaften von Satzteilen verfolgen.

> ✅ Eine ausgezeichnete Ressource, um die Interna von LSTM zu verstehen, ist dieser großartige Artikel [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) von Christopher Olah.

## Bidirektionale und mehrschichtige RNNs

Wir haben rekurrente Netzwerke besprochen, die in eine Richtung arbeiten, vom Anfang einer Sequenz bis zum Ende. Das erscheint natürlich, da es der Art und Weise ähnelt, wie wir lesen und Sprache hören. Da wir jedoch in vielen praktischen Fällen zufälligen Zugriff auf die Eingabesequenz haben, könnte es sinnvoll sein, die rekurrente Berechnung in beide Richtungen auszuführen. Solche Netzwerke werden als **bidirektionale** RNNs bezeichnet. Bei der Arbeit mit einem bidirektionalen Netzwerk benötigen wir zwei versteckte Zustandsvektoren, einen für jede Richtung.

Ein rekurrentes Netzwerk, sei es eindirektional oder bidirektional, erfasst bestimmte Muster innerhalb einer Sequenz und kann diese in einem Zustandsvektor speichern oder in die Ausgabe weitergeben. Wie bei konvolutionalen Netzwerken können wir eine weitere rekurrente Schicht auf die erste aufbauen, um höherstufige Muster zu erfassen und aus den von der ersten Schicht extrahierten niedrigstufigen Mustern aufzubauen. Dies führt uns zum Konzept eines **mehrschichtigen RNN**, das aus zwei oder mehr rekurrenten Netzwerken besteht, wobei die Ausgabe der vorherigen Schicht als Eingabe an die nächste Schicht weitergegeben wird.

![Bild eines mehrschichtigen Long-Short-Term-Memory-RNNs](../../../../../lessons/5-NLP/16-RNN/images/multi-layer-lstm.jpg)

*Bild aus [diesem wunderbaren Beitrag](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) von Fernando López*

## ✍️ Übungen: Einbettungen

Setzen Sie Ihr Lernen in den folgenden Notebooks fort:

* [RNNs mit PyTorch](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [RNNs mit TensorFlow](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## Fazit

In dieser Einheit haben wir gesehen, dass RNNs für die Sequenzklassifikation verwendet werden können, aber tatsächlich können sie viele weitere Aufgaben bewältigen, wie Textgenerierung, maschinelle Übersetzung und mehr. Diese Aufgaben werden wir in der nächsten Einheit betrachten.

## 🚀 Herausforderung

Lesen Sie einige Literatur über LSTMs und überlegen Sie sich deren Anwendungen:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Quiz nach der Vorlesung](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/216)

## Wiederholung & Selbststudium

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) von Christopher Olah.

## [Aufgabe: Notebooks](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.