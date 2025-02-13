# Rekurrente Neuronale Netze

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/116)

In den vorherigen Abschnitten haben wir reichhaltige semantische Darstellungen von Texten und einen einfachen linearen Klassifikator auf den Embeddings verwendet. Was diese Architektur tut, ist, die aggregierte Bedeutung von Wörtern in einem Satz zu erfassen, jedoch berücksichtigt sie nicht die **Reihenfolge** der Wörter, da die Aggregationsoperation über den Embeddings diese Information aus dem ursprünglichen Text entfernt hat. Da diese Modelle nicht in der Lage sind, die Wortreihenfolge zu modellieren, können sie komplexere oder mehrdeutige Aufgaben wie Textgenerierung oder Fragenbeantwortung nicht lösen.

Um die Bedeutung einer Textsequenz zu erfassen, müssen wir eine andere Architektur neuronaler Netze verwenden, die als **rekurrentes neuronales Netz** oder RNN bezeichnet wird. Im RNN leiten wir unseren Satz symbolweise durch das Netzwerk, und das Netzwerk erzeugt einen **Zustand**, den wir dann erneut mit dem nächsten Symbol an das Netzwerk übergeben.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.de.png)

> Bild vom Autor

Gegeben die Eingabesequenz von Token X<sub>0</sub>,...,X<sub>n</sub> erstellt das RNN eine Sequenz von neuronalen Netzwerkblöcken und trainiert diese Sequenz End-to-End mithilfe von Rückpropagation. Jeder Netzwerkblock nimmt ein Paar (X<sub>i</sub>,S<sub>i</sub>) als Eingabe und produziert S<sub>i+1</sub> als Ergebnis. Der endgültige Zustand S<sub>n</sub> oder (Ausgabe Y<sub>n</sub>) geht in einen linearen Klassifikator, um das Ergebnis zu produzieren. Alle Netzwerkblöcke teilen sich die gleichen Gewichte und werden End-to-End mit einem Rückpropagationsdurchlauf trainiert.

Da Zustandsvektoren S<sub>0</sub>,...,S<sub>n</sub> durch das Netzwerk geleitet werden, ist es in der Lage, die sequentiellen Abhängigkeiten zwischen Wörtern zu lernen. Zum Beispiel, wenn das Wort *not* irgendwo in der Sequenz erscheint, kann es lernen, bestimmte Elemente innerhalb des Zustandsvektors zu negieren, was zu einer Negation führt.

> ✅ Da die Gewichte aller RNN-Blöcke im obigen Bild geteilt werden, kann dasselbe Bild als ein Block (rechts) mit einer rekurrenten Rückkopplungsschleife dargestellt werden, die den Ausgangszustand des Netzwerks zurück an den Eingang übergibt.

## Anatomie einer RNN-Zelle

Schauen wir uns an, wie eine einfache RNN-Zelle organisiert ist. Sie akzeptiert den vorherigen Zustand S<sub>i-1</sub> und das aktuelle Symbol X<sub>i</sub> als Eingaben und muss den Ausgangszustand S<sub>i</sub> produzieren (und manchmal interessieren wir uns auch für eine andere Ausgabe Y<sub>i</sub>, wie im Fall von generativen Netzwerken).

Eine einfache RNN-Zelle hat zwei Gewichtsmatrizen: eine transformiert ein Eingabesymbol (nennen wir sie W) und eine andere transformiert einen Eingabestatus (H). In diesem Fall wird der Ausgang des Netzwerks als σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b) berechnet, wobei σ die Aktivierungsfunktion ist und b der zusätzliche Bias.

<img alt="Anatomie einer RNN-Zelle" src="images/rnn-anatomy.png" width="50%"/>

> Bild vom Autor

In vielen Fällen werden Eingabetoken vor dem Eintritt in das RNN durch die Embedding-Schicht geleitet, um die Dimensionalität zu reduzieren. In diesem Fall, wenn die Dimension der Eingangsvektoren *emb_size* beträgt und der Zustandsvektor *hid_size* - die Größe von W ist *emb_size*×*hid_size* und die Größe von H ist *hid_size*×*hid_size*.

## Langzeit-Kurzzeitgedächtnis (LSTM)

Eines der Hauptprobleme klassischer RNNs ist das sogenannte **verschwinden der Gradienten**-Problem. Da RNNs End-to-End in einem Rückpropagationsdurchlauf trainiert werden, hat es Schwierigkeiten, den Fehler auf die ersten Schichten des Netzwerks zu propagieren, und daher kann das Netzwerk keine Beziehungen zwischen weit entfernten Token lernen. Eine Möglichkeit, dieses Problem zu vermeiden, besteht darin, eine **explizite Zustandsverwaltung** durch die Verwendung sogenannter **Tore** einzuführen. Es gibt zwei bekannte Architekturen dieser Art: **Langzeit-Kurzzeitgedächtnis** (LSTM) und **Gated Relay Unit** (GRU).

![Bild, das ein Beispiel für eine Langzeit-Kurzzeitgedächtniszelle zeigt](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Bildquelle TBD

Das LSTM-Netzwerk ist ähnlich wie das RNN organisiert, aber es gibt zwei Zustände, die von Schicht zu Schicht übergeben werden: den aktuellen Zustand C und den versteckten Vektor H. An jeder Einheit wird der versteckte Vektor H<sub>i</sub> mit dem Eingabevektor X<sub>i</sub> verknüpft, und sie steuern, was mit dem Zustand C über die **Tore** geschieht. Jedes Tor ist ein neuronales Netzwerk mit sigmoidaler Aktivierung (Ausgabe im Bereich [0,1]), das als bitweiser Maske betrachtet werden kann, wenn es mit dem Zustandsvektor multipliziert wird. Es gibt die folgenden Tore (von links nach rechts im obigen Bild):

* Das **Vergessenstor** nimmt einen versteckten Vektor und bestimmt, welche Komponenten des Vektors C wir vergessen müssen und welche durchgelassen werden sollen.
* Das **Eingangstor** nimmt einige Informationen aus den Eingabe- und versteckten Vektoren und fügt sie in den Zustand ein.
* Das **Ausgangstor** transformiert den Zustand über eine lineare Schicht mit *tanh*-Aktivierung und wählt dann einige seiner Komponenten unter Verwendung eines versteckten Vektors H<sub>i</sub> aus, um einen neuen Zustand C<sub>i+1</sub> zu erzeugen.

Die Komponenten des Zustands C können als einige Flags betrachtet werden, die ein- und ausgeschaltet werden können. Wenn wir zum Beispiel im Verlauf der Sequenz auf einen Namen wie *Alice* stoßen, möchten wir vielleicht annehmen, dass es sich um eine weibliche Figur handelt, und das Flag im Zustand erhöhen, dass wir ein weibliches Substantiv im Satz haben. Wenn wir dann auf die Phrasen *und Tom* stoßen, heben wir das Flag, dass wir ein Pluralnoun haben. So können wir durch die Manipulation des Zustands angeblich die grammatikalischen Eigenschaften von Satzteilen im Auge behalten.

> ✅ Eine hervorragende Ressource zum Verständnis der Interna von LSTM ist dieser großartige Artikel [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) von Christopher Olah.

## Bidirektionale und mehrschichtige RNNs

Wir haben rekurrente Netze besprochen, die in eine Richtung arbeiten, vom Anfang einer Sequenz bis zum Ende. Das wirkt natürlich, da es der Art und Weise ähnelt, wie wir lesen und Sprache hören. Da wir jedoch in vielen praktischen Fällen zufälligen Zugriff auf die Eingabesequenz haben, kann es sinnvoll sein, die rekursive Berechnung in beide Richtungen auszuführen. Solche Netzwerke werden **bidirektionale** RNNs genannt. Bei der Arbeit mit einem bidirektionalen Netzwerk benötigen wir zwei versteckte Zustandsvektoren, einen für jede Richtung.

Ein rekurrentes Netzwerk, ob einseitig oder bidirektional, erfasst bestimmte Muster innerhalb einer Sequenz und kann sie in einem Zustandsvektor speichern oder in die Ausgabe übergeben. Wie bei konvolutionalen Netzwerken können wir eine weitere rekursive Schicht über der ersten aufbauen, um höhere Muster zu erfassen und von den von der ersten Schicht extrahierten niederwertigen Mustern aufzubauen. Dies führt uns zum Begriff eines **mehrschichtigen RNN**, das aus zwei oder mehr rekurrenten Netzwerken besteht, wobei die Ausgabe der vorherigen Schicht als Eingabe an die nächste Schicht übergeben wird.

![Bild, das ein mehrschichtiges Langzeit-Kurzzeitgedächtnis-RNN zeigt](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.de.jpg)

*Bild von [diesem wunderbaren Beitrag](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) von Fernando López*

## ✍️ Übungen: Embeddings

Setze dein Lernen in den folgenden Notebooks fort:

* [RNNs mit PyTorch](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [RNNs mit TensorFlow](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## Fazit

In dieser Einheit haben wir gesehen, dass RNNs für die Sequenzklassifizierung verwendet werden können, aber tatsächlich können sie viele weitere Aufgaben bewältigen, wie Textgenerierung, maschinelle Übersetzung und mehr. Diese Aufgaben werden wir in der nächsten Einheit betrachten.

## 🚀 Herausforderung

Lies einige Literatur über LSTMs und ziehe deren Anwendungen in Betracht:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Nachlesequiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/216)

## Überprüfung & Selbststudium

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) von Christopher Olah.

## [Aufgabe: Notebooks](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, sollten Sie sich bewusst sein, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Originalsprache sollte als die maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.