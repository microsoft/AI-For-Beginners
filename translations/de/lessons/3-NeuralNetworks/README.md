# Einführung in Neuronale Netzwerke

![Zusammenfassung des Inhalts zu Einführung in Neuronale Netzwerke in einem Doodle](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.de.png)

Wie wir in der Einführung besprochen haben, ist eine der Möglichkeiten, Intelligenz zu erreichen, ein **Computermodell** oder ein **künstliches Gehirn** zu trainieren. Seit der Mitte des 20. Jahrhunderts haben Forscher verschiedene mathematische Modelle ausprobiert, bis sich in den letzten Jahren diese Richtung als äußerst erfolgreich erwies. Solche mathematischen Modelle des Gehirns werden als **neuronale Netzwerke** bezeichnet.

> Manchmal werden neuronale Netzwerke als *Künstliche Neuronale Netzwerke* (ANNs) bezeichnet, um zu verdeutlichen, dass wir von Modellen und nicht von echten Netzwerken von Neuronen sprechen.

## Maschinelles Lernen

Neuronale Netzwerke sind ein Teil eines größeren Fachgebiets, das **Maschinelles Lernen** genannt wird, dessen Ziel es ist, Daten zu verwenden, um Computermodelle zu trainieren, die in der Lage sind, Probleme zu lösen. Maschinelles Lernen ist ein großer Teil der Künstlichen Intelligenz, jedoch behandeln wir klassisches ML in diesem Lehrplan nicht.

> Besuchen Sie unseren separaten **[Maschinelles Lernen für Anfänger](http://github.com/microsoft/ml-for-beginners)** Lehrplan, um mehr über klassisches Maschinelles Lernen zu erfahren.

Im Maschinellen Lernen nehmen wir an, dass wir einen Datensatz von Beispielen **X** und die entsprechenden Ausgabewerte **Y** haben. Beispiele sind oft N-dimensionale Vektoren, die aus **Merkmalen** bestehen, und Ausgaben werden als **Labels** bezeichnet.

Wir werden die zwei häufigsten Probleme des maschinellen Lernens betrachten:

* **Klassifikation**, bei der wir ein Eingabeobjekt in zwei oder mehr Klassen einordnen müssen.
* **Regression**, bei der wir eine numerische Zahl für jede der Eingabemuster vorhersagen müssen.

> Wenn Eingaben und Ausgaben als Tensoren dargestellt werden, ist der Eingabedatensatz eine Matrix der Größe M×N, wobei M die Anzahl der Proben und N die Anzahl der Merkmale ist. Die Ausgabelabel Y ist der Vektor der Größe M.

In diesem Lehrplan konzentrieren wir uns ausschließlich auf Modelle neuronaler Netzwerke.

## Ein Modell eines Neurons

Aus der Biologie wissen wir, dass unser Gehirn aus Nervenzellen besteht, von denen jede mehrere "Eingänge" (Axone) und einen Ausgang (Dendrit) hat. Axone und Dendriten können elektrische Signale leiten, und die Verbindungen zwischen Axonen und Dendriten können unterschiedliche Leitfähigkeiten aufweisen (gesteuert durch Neuromediatoren).

![Modell eines Neurons](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.de.jpg) | ![Modell eines Neurons](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.de.png)
----|----
Reales Neuron *([Bild](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) von Wikipedia)* | Künstliches Neuron *(Bild vom Autor)*

Somit enthält das einfachste mathematische Modell eines Neurons mehrere Eingänge X<sub>1</sub>, ..., X<sub>N</sub> und einen Ausgang Y sowie eine Reihe von Gewichten W<sub>1</sub>, ..., W<sub>N</sub>. Ein Ausgang wird berechnet als:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

wobei f eine nichtlineare **Aktivierungsfunktion** ist.

> Frühe Modelle von Neuronen wurden in dem klassischen Papier [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) von Warren McCullock und Walter Pitts im Jahr 1943 beschrieben. Donald Hebb schlug in seinem Buch "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" vor, wie diese Netzwerke trainiert werden können.

## In diesem Abschnitt

In diesem Abschnitt werden wir lernen über:
* [Perzeptron](03-Perceptron/README.md), eines der frühesten Modelle neuronaler Netzwerke für die Klassifikation in zwei Klassen
* [Mehrschichtige Netzwerke](04-OwnFramework/README.md) mit einem begleitenden Notizbuch [wie man unser eigenes Framework erstellt](../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)
* [Frameworks für Neuronale Netzwerke](05-Frameworks/README.md), mit diesen Notizbüchern: [PyTorch](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) und [Keras/Tensorflow](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)
* [Overfitting](../../../../lessons/3-NeuralNetworks/05-Frameworks)

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, bitten wir zu beachten, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.