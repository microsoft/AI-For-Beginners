# Generative Adversarial Networks

Im vorherigen Abschnitt haben wir über **generative Modelle** gelernt: Modelle, die neue Bilder erzeugen können, die den Bildern im Trainingsdatensatz ähnlich sind. VAE war ein gutes Beispiel für ein generatives Modell.

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

Wenn wir jedoch versuchen, etwas wirklich Sinnvolles zu generieren, wie ein Gemälde in angemessener Auflösung, mit VAE, werden wir feststellen, dass das Training nicht gut konvergiert. Für diesen Anwendungsfall sollten wir über eine andere Architektur lernen, die speziell auf generative Modelle abzielt - **Generative Adversarial Networks**, oder GANs.

Die Hauptidee eines GANs besteht darin, zwei neuronale Netzwerke zu haben, die gegeneinander trainiert werden:

<img src="images/gan_architecture.png" width="70%"/>

> Bild von [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Ein kleines Vokabular:
> * **Generator** ist ein Netzwerk, das einen zufälligen Vektor nimmt und als Ergebnis das Bild erzeugt
> * **Discriminator** ist ein Netzwerk, das ein Bild nimmt und feststellen sollte, ob es sich um ein echtes Bild (aus dem Trainingsdatensatz) handelt oder ob es von einem Generator erzeugt wurde. Es ist im Wesentlichen ein Bildklassifizierer.

### Discriminator

Die Architektur des Discriminators unterscheidet sich nicht von einem gewöhnlichen Bildklassifizierungsnetzwerk. Im einfachsten Fall kann es ein vollständig verbundener Klassifizierer sein, aber höchstwahrscheinlich wird es ein [konvolutionales Netzwerk](../07-ConvNets/README.md) sein.

> ✅ Ein auf konvolutionalen Netzwerken basierendes GAN wird als [DCGAN](https://arxiv.org/pdf/1511.06434.pdf) bezeichnet.

Ein CNN-Discriminator besteht aus den folgenden Schichten: mehreren Faltungen+Pooling (mit abnehmender räumlicher Größe) und einer oder mehreren vollständig verbundenen Schichten, um den "Merkmalsvektor" zu erhalten, und einem endgültigen binären Klassifizierer.

> ✅ Ein 'Pooling' in diesem Kontext ist eine Technik, die die Größe des Bildes reduziert. "Pooling-Schichten reduzieren die Dimensionen der Daten, indem sie die Ausgaben von Neuronengruppen in einer Schicht in ein einzelnes Neuron in der nächsten Schicht kombinieren." - [Quelle](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generator

Ein Generator ist etwas kniffliger. Man kann ihn als umgekehrten Discriminator betrachten. Ausgehend von einem latenten Vektor (anstatt eines Merkmalsvektors) hat er eine vollständig verbundene Schicht, um ihn in die erforderliche Größe/Form zu konvertieren, gefolgt von Dekonvolutionen+Hochskalierung. Dies ähnelt dem *Decoder*-Teil eines [Autoencoders](../09-Autoencoders/README.md).

> ✅ Da die Faltungsschicht als linearer Filter implementiert ist, der das Bild durchläuft, ist die Dekonvolution im Wesentlichen ähnlich wie die Faltung und kann mit derselben Schichtlogik implementiert werden.

<img src="images/gan_arch_detail.png" width="70%"/>

> Bild von [Dmitry Soshnikov](http://soshnikov.com)

### Training des GAN

GANs werden als **adversarial** bezeichnet, weil es einen ständigen Wettbewerb zwischen dem Generator und dem Discriminator gibt. Während dieses Wettbewerbs verbessern sich sowohl der Generator als auch der Discriminator, sodass das Netzwerk lernt, immer bessere Bilder zu erzeugen.

Das Training erfolgt in zwei Phasen:

* **Training des Discriminators**. Diese Aufgabe ist ziemlich einfach: Wir erzeugen eine Charge von Bildern mit dem Generator, kennzeichnen sie mit 0, was für ein gefälschtes Bild steht, und nehmen eine Charge von Bildern aus dem Eingabedatensatz (mit dem Label 1, echtes Bild). Wir erhalten einen *Discriminator-Verlust* und führen die Rückpropagation durch.
* **Training des Generators**. Dies ist etwas kniffliger, da wir den erwarteten Ausgang für den Generator nicht direkt kennen. Wir nehmen das gesamte GAN-Netzwerk, das aus einem Generator gefolgt von einem Discriminator besteht, füttern es mit einigen zufälligen Vektoren und erwarten, dass das Ergebnis 1 ist (entsprechend echten Bildern). Dann frieren wir die Parameter des Discriminators ein (wir möchten nicht, dass er in diesem Schritt trainiert wird) und führen die Rückpropagation durch.

Während dieses Prozesses sinken die Verluste von sowohl Generator als auch Discriminator nicht signifikant. In der idealen Situation sollten sie oszillieren, was bedeutet, dass beide Netzwerke ihre Leistung verbessern.

## ✍️ Übungen: GANs

* [GAN-Notebook in TensorFlow/Keras](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [GAN-Notebook in PyTorch](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### Probleme beim Training von GANs

Es ist bekannt, dass GANs besonders schwierig zu trainieren sind. Hier sind einige Probleme:

* **Mode Collapse**. Mit diesem Begriff meinen wir, dass der Generator lernt, ein erfolgreiches Bild zu erzeugen, das den Discriminator täuscht, und nicht eine Vielzahl unterschiedlicher Bilder.
* **Empfindlichkeit gegenüber Hyperparametern**. Oft sieht man, dass ein GAN überhaupt nicht konvergiert, und dann plötzlich der Lernrate sinkt, was zur Konvergenz führt.
* Den **Ausgleich** zwischen Generator und Discriminator halten. In vielen Fällen kann der Discriminator-Verlust relativ schnell auf null sinken, was dazu führt, dass der Generator nicht weiter trainiert werden kann. Um dies zu überwinden, können wir versuchen, unterschiedliche Lernraten für den Generator und den Discriminator festzulegen oder das Training des Discriminators zu überspringen, wenn der Verlust bereits zu niedrig ist.
* Training für **hohe Auflösung**. Dies spiegelt dasselbe Problem wie bei Autoencodern wider; dieses Problem wird ausgelöst, weil das Rekonstruieren zu vieler Schichten eines konvolutionalen Netzwerks zu Artefakten führt. Dieses Problem wird typischerweise mit dem sogenannten **progressiven Wachsen** gelöst, bei dem zunächst einige Schichten mit niedrig aufgelösten Bildern trainiert werden und dann Schichten "freigeschaltet" oder hinzugefügt werden. Eine andere Lösung wäre, zusätzliche Verbindungen zwischen den Schichten hinzuzufügen und mehrere Auflösungen gleichzeitig zu trainieren - siehe dazu das [Multi-Scale Gradient GANs-Papier](https://arxiv.org/abs/1903.06048) für weitere Details.

## Stiltransfer

GANs sind eine großartige Möglichkeit, künstlerische Bilder zu generieren. Eine weitere interessante Technik ist der sogenannte **Stiltransfer**, bei dem ein **Inhaltsbild** genommen und in einem anderen Stil neu gezeichnet wird, indem Filter aus einem **Stilbild** angewendet werden.

So funktioniert es:
* Wir beginnen mit einem Bild aus zufälligem Rauschen (oder mit einem Inhaltsbild, aber um es besser zu verstehen, ist es einfacher, mit zufälligem Rauschen zu beginnen)
* Unser Ziel wäre es, ein solches Bild zu erstellen, das sowohl dem Inhaltsbild als auch dem Stilbild nahekommt. Dies würde durch zwei Verlustfunktionen bestimmt:
   - **Inhaltsverlust** wird basierend auf den Merkmalen berechnet, die von der CNN in einigen Schichten aus dem aktuellen Bild und dem Inhaltsbild extrahiert werden
   - **Stilverlust** wird auf clevere Weise zwischen dem aktuellen Bild und dem Stilbild unter Verwendung von Gram-Matrizen berechnet (weitere Details im [Beispiel-Notebook](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb))
* Um das Bild glatter zu machen und Rauschen zu entfernen, führen wir auch einen **Variationsverlust** ein, der die durchschnittliche Distanz zwischen benachbarten Pixeln berechnet
* Die Hauptoptimierungsschleife passt das aktuelle Bild unter Verwendung von Gradientenabstieg (oder einem anderen Optimierungsalgorithmus) an, um den Gesamtschaden zu minimieren, der eine gewichtete Summe aller drei Verluste ist.

## ✍️ Beispiel: [Stiltransfer](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Nachlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## Fazit

In dieser Lektion haben Sie über GANs gelernt und wie man sie trainiert. Sie haben auch über die speziellen Herausforderungen gelernt, mit denen dieser Typ von neuronalen Netzwerken konfrontiert sein kann, sowie über einige Strategien, um darüber hinwegzukommen.

## 🚀 Herausforderung

Durchlaufen Sie das [Stiltransfer-Notebook](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) mit Ihren eigenen Bildern.

## Überprüfung & Selbststudium

Zur Referenz lesen Sie mehr über GANs in diesen Ressourcen:

* Marco Pasini, [10 Lektionen, die ich beim Training von GANs für ein Jahr gelernt habe](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), eine *de facto* GAN-Architektur, die in Betracht gezogen werden sollte
* [Erstellung generativer Kunst mit GANs auf Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Aufgabe

Überarbeiten Sie eines der beiden Notebooks, die mit dieser Lektion verbunden sind, und trainieren Sie das GAN mit Ihren eigenen Bildern neu. Was können Sie erschaffen?

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Originalsprache sollte als die maßgebliche Quelle angesehen werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Verantwortung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.