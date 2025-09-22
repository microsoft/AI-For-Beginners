<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-24T09:34:36+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "de"
}
-->
# Generative Adversarial Networks

Im vorherigen Abschnitt haben wir über **generative Modelle** gelernt: Modelle, die neue Bilder erzeugen können, die den Bildern im Trainingsdatensatz ähneln. VAE war ein gutes Beispiel für ein generatives Modell.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/19)

Wenn wir jedoch versuchen, etwas wirklich Bedeutungsvolles zu generieren, wie ein Gemälde in vernünftiger Auflösung, werden wir feststellen, dass das Training mit VAE nicht gut konvergiert. Für diesen Anwendungsfall sollten wir eine andere Architektur kennenlernen, die speziell auf generative Modelle ausgerichtet ist - **Generative Adversarial Networks**, oder GANs.

Die Hauptidee eines GANs besteht darin, zwei neuronale Netzwerke zu haben, die gegeneinander trainiert werden:

<img src="images/gan_architecture.png" width="70%"/>

> Bild von [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Ein bisschen Vokabular:
> * **Generator** ist ein Netzwerk, das einen zufälligen Vektor nimmt und daraus ein Bild erzeugt.
> * **Discriminator** ist ein Netzwerk, das ein Bild nimmt und entscheiden soll, ob es sich um ein echtes Bild (aus dem Trainingsdatensatz) oder ein vom Generator erzeugtes Bild handelt. Es ist im Wesentlichen ein Bildklassifikator.

### Discriminator

Die Architektur des Discriminators unterscheidet sich nicht von einem gewöhnlichen Bildklassifikationsnetzwerk. Im einfachsten Fall kann es ein vollständig verbundenes Klassifikationsnetzwerk sein, aber höchstwahrscheinlich wird es ein [Convolutional Network](../07-ConvNets/README.md) sein.

> ✅ Ein GAN, das auf Convolutional Networks basiert, wird als [DCGAN](https://arxiv.org/pdf/1511.06434.pdf) bezeichnet.

Ein CNN-Discriminator besteht aus den folgenden Schichten: mehreren Convolutions+Poolings (mit abnehmender räumlicher Größe) und einer oder mehreren vollständig verbundenen Schichten, um einen "Feature-Vektor" zu erhalten, sowie einem abschließenden binären Klassifikator.

> ✅ Ein 'Pooling' in diesem Kontext ist eine Technik, die die Größe des Bildes reduziert. "Pooling-Schichten reduzieren die Dimensionen der Daten, indem sie die Ausgaben von Neuronenclustern in einer Schicht zu einem einzelnen Neuron in der nächsten Schicht kombinieren." - [Quelle](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generator

Ein Generator ist etwas komplizierter. Man kann ihn als umgekehrten Discriminator betrachten. Ausgehend von einem latenten Vektor (anstelle eines Feature-Vektors) hat er eine vollständig verbundene Schicht, um ihn in die erforderliche Größe/Form umzuwandeln, gefolgt von Deconvolutions+Upscaling. Dies ähnelt dem *Decoder*-Teil eines [Autoencoders](../09-Autoencoders/README.md).

> ✅ Da die Convolution-Schicht als linearer Filter implementiert ist, der das Bild durchläuft, ist Deconvolution im Wesentlichen ähnlich wie Convolution und kann mit derselben Schichtlogik implementiert werden.

<img src="images/gan_arch_detail.png" width="70%"/>

> Bild von [Dmitry Soshnikov](http://soshnikov.com)

### Training des GANs

GANs werden als **adversarial** bezeichnet, weil es einen ständigen Wettbewerb zwischen dem Generator und dem Discriminator gibt. Während dieses Wettbewerbs verbessern sich sowohl der Generator als auch der Discriminator, sodass das Netzwerk lernt, immer bessere Bilder zu erzeugen.

Das Training erfolgt in zwei Phasen:

* **Training des Discriminators**. Diese Aufgabe ist ziemlich einfach: Wir generieren eine Charge von Bildern mit dem Generator, kennzeichnen sie mit 0 (was für ein gefälschtes Bild steht), und nehmen eine Charge von Bildern aus dem Eingabedatensatz (mit dem Label 1, echtes Bild). Wir erhalten einen *Discriminator Loss* und führen Backpropagation durch.
* **Training des Generators**. Dies ist etwas komplizierter, da wir die erwartete Ausgabe für den Generator nicht direkt kennen. Wir nehmen das gesamte GAN-Netzwerk, das aus einem Generator und einem Discriminator besteht, füttern es mit zufälligen Vektoren und erwarten, dass das Ergebnis 1 ist (entsprechend echten Bildern). Dann frieren wir die Parameter des Discriminators ein (wir wollen ihn in diesem Schritt nicht trainieren) und führen Backpropagation durch.

Während dieses Prozesses sinken die Verluste des Generators und des Discriminators nicht signifikant. Im Idealfall sollten sie oszillieren, was darauf hinweist, dass beide Netzwerke ihre Leistung verbessern.

## ✍️ Übungen: GANs

* [GAN Notebook in TensorFlow/Keras](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [GAN Notebook in PyTorch](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### Probleme beim Training von GANs

GANs sind dafür bekannt, besonders schwierig zu trainieren zu sein. Hier sind einige Probleme:

* **Mode Collapse**. Damit ist gemeint, dass der Generator lernt, ein erfolgreiches Bild zu erzeugen, das den Discriminator täuscht, aber keine Vielfalt an verschiedenen Bildern produziert.
* **Empfindlichkeit gegenüber Hyperparametern**. Oft kann man beobachten, dass ein GAN überhaupt nicht konvergiert, und dann plötzlich durch eine Verringerung der Lernrate zur Konvergenz gelangt.
* Das **Gleichgewicht** zwischen Generator und Discriminator aufrechterhalten. In vielen Fällen kann der Verlust des Discriminators relativ schnell auf null sinken, was dazu führt, dass der Generator nicht weiter trainiert werden kann. Um dies zu überwinden, können wir versuchen, unterschiedliche Lernraten für Generator und Discriminator festzulegen oder das Training des Discriminators zu überspringen, wenn der Verlust bereits zu niedrig ist.
* Training für **hohe Auflösung**. Ähnlich wie bei Autoencodern tritt dieses Problem auf, weil das Rekonstruieren zu vieler Schichten eines Convolutional Networks zu Artefakten führt. Dieses Problem wird typischerweise durch sogenanntes **progressives Wachstum** gelöst, bei dem zunächst einige Schichten auf niedrig aufgelösten Bildern trainiert werden und dann Schichten "freigeschaltet" oder hinzugefügt werden. Eine andere Lösung wäre, zusätzliche Verbindungen zwischen den Schichten hinzuzufügen und mehrere Auflösungen gleichzeitig zu trainieren - siehe dieses [Multi-Scale Gradient GANs Paper](https://arxiv.org/abs/1903.06048) für Details.

## Style Transfer

GANs sind eine großartige Möglichkeit, künstlerische Bilder zu generieren. Eine weitere interessante Technik ist der sogenannte **Style Transfer**, bei dem ein **Inhaltsbild** genommen und in einem anderen Stil neu gezeichnet wird, indem Filter aus einem **Stilbild** angewendet werden.

So funktioniert es:
* Wir beginnen mit einem zufälligen Rauschbild (oder mit einem Inhaltsbild, aber der Einfachheit halber ist es leichter, mit zufälligem Rauschen zu beginnen).
* Unser Ziel ist es, ein Bild zu erstellen, das sowohl dem Inhaltsbild als auch dem Stilbild nahekommt. Dies wird durch zwei Verlustfunktionen bestimmt:
   - **Content Loss** wird basierend auf den Merkmalen berechnet, die von der CNN in einigen Schichten aus dem aktuellen Bild und dem Inhaltsbild extrahiert werden.
   - **Style Loss** wird zwischen dem aktuellen Bild und dem Stilbild auf clevere Weise unter Verwendung von Gram-Matrizen berechnet (mehr Details im [Beispiel-Notebook](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)).
* Um das Bild glatter zu machen und Rauschen zu entfernen, führen wir auch einen **Variation Loss** ein, der den durchschnittlichen Abstand zwischen benachbarten Pixeln berechnet.
* Die Hauptoptimierungsschleife passt das aktuelle Bild mithilfe von Gradient Descent (oder einem anderen Optimierungsalgorithmus) an, um den Gesamtabstand zu minimieren, der eine gewichtete Summe aller drei Verluste ist.

## ✍️ Beispiel: [Style Transfer](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/20)

## Fazit

In dieser Lektion haben Sie über GANs und deren Training gelernt. Sie haben auch die besonderen Herausforderungen kennengelernt, denen diese Art von neuronalen Netzwerken begegnen kann, und einige Strategien, wie man diese überwinden kann.

## 🚀 Herausforderung

Arbeiten Sie das [Style Transfer Notebook](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) mit Ihren eigenen Bildern durch.

## Wiederholung & Selbststudium

Zur Vertiefung lesen Sie mehr über GANs in diesen Ressourcen:

* Marco Pasini, [10 Lessons I Learned Training GANs for one Year](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), eine *de facto* GAN-Architektur, die man in Betracht ziehen sollte.
* [Creating Generative Art using GANs on Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Aufgabe

Besuchen Sie eines der beiden Notebooks zu dieser Lektion erneut und trainieren Sie das GAN mit Ihren eigenen Bildern. Was können Sie erschaffen?

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.