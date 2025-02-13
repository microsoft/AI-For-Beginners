# Frameworks für Neuronale Netzwerke

Wie wir bereits gelernt haben, um neuronale Netzwerke effizient zu trainieren, müssen wir zwei Dinge tun:

* Mit Tensors arbeiten, z. B. multiplizieren, addieren und Funktionen wie Sigmoid oder Softmax berechnen
* Die Gradienten aller Ausdrücke berechnen, um die Optimierung durch Gradientenabstieg durchzuführen

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/105)

Während die `numpy` Bibliothek den ersten Teil erledigen kann, benötigen wir einen Mechanismus zur Berechnung von Gradienten. In [unserem Framework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb), das wir im vorherigen Abschnitt entwickelt haben, mussten wir alle Ableitungsfunktionen manuell innerhalb der `backward` Methode programmieren, die Backpropagation durchführt. Idealerweise sollte ein Framework uns die Möglichkeit geben, die Gradienten *jeden Ausdrucks* zu berechnen, den wir definieren können.

Ein weiterer wichtiger Aspekt ist die Fähigkeit, Berechnungen auf der GPU oder anderen spezialisierten Recheneinheiten wie [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit) durchzuführen. Das Training tiefer neuronaler Netzwerke erfordert *eine Menge* Berechnungen, und die Möglichkeit, diese Berechnungen auf GPUs zu parallelisieren, ist von großer Bedeutung.

> ✅ Der Begriff 'parallelisieren' bedeutet, die Berechnungen auf mehrere Geräte zu verteilen.

Derzeit sind die beiden beliebtesten neuronalen Frameworks: [TensorFlow](http://TensorFlow.org) und [PyTorch](https://pytorch.org/). Beide bieten eine Low-Level-API, um mit Tensors sowohl auf CPU als auch auf GPU zu arbeiten. Darüber hinaus gibt es eine höherstufige API, die entsprechend [Keras](https://keras.io/) und [PyTorch Lightning](https://pytorchlightning.ai/) genannt wird.

Low-Level API | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
--------------|-------------------------------------|--------------------------------
High-level API| [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**Low-Level APIs** in beiden Frameworks ermöglichen es Ihnen, sogenannte **Berechnungsgraphen** zu erstellen. Dieser Graph definiert, wie man die Ausgabe (normalerweise die Verlustfunktion) mit gegebenen Eingabeparametern berechnet und kann zur Berechnung auf der GPU verschoben werden, wenn diese verfügbar ist. Es gibt Funktionen, um diesen Berechnungsgraphen zu differenzieren und Gradienten zu berechnen, die dann zur Optimierung der Modellparameter verwendet werden können.

**High-Level APIs** betrachten neuronale Netzwerke im Wesentlichen als eine **Folge von Schichten** und erleichtern den Aufbau der meisten neuronalen Netzwerke erheblich. Das Training des Modells erfordert normalerweise die Vorbereitung der Daten und dann das Aufrufen einer `fit` Funktion, um die Arbeit zu erledigen.

Die hochgradige API ermöglicht es Ihnen, typische neuronale Netzwerke sehr schnell zu konstruieren, ohne sich um viele Details kümmern zu müssen. Gleichzeitig bieten Low-Level-APIs viel mehr Kontrolle über den Trainingsprozess, und daher werden sie häufig in der Forschung verwendet, wenn es darum geht, neue Architekturen neuronaler Netzwerke zu entwickeln.

Es ist auch wichtig zu verstehen, dass Sie beide APIs zusammen verwenden können, z. B. können Sie Ihre eigene Netzwerkarchitektur mit der Low-Level-API entwickeln und sie dann in das größere Netzwerk einfügen, das mit der High-Level-API konstruiert und trainiert wurde. Oder Sie können ein Netzwerk mit der High-Level-API als Folge von Schichten definieren und dann Ihre eigene Low-Level-Trainingsschleife verwenden, um die Optimierung durchzuführen. Beide APIs verwenden die gleichen grundlegenden zugrunde liegenden Konzepte und sind so gestaltet, dass sie gut zusammenarbeiten.

## Lernen

In diesem Kurs bieten wir den Großteil des Inhalts sowohl für PyTorch als auch für TensorFlow an. Sie können Ihr bevorzugtes Framework auswählen und nur die entsprechenden Notebooks durchgehen. Wenn Sie sich nicht sicher sind, welches Framework Sie wählen sollen, lesen Sie einige Diskussionen im Internet über **PyTorch vs. TensorFlow**. Sie können auch beide Frameworks betrachten, um ein besseres Verständnis zu bekommen.

Wo immer möglich, werden wir High-Level-APIs zur Vereinfachung verwenden. Wir glauben jedoch, dass es wichtig ist, zu verstehen, wie neuronale Netzwerke von Grund auf funktionieren, weshalb wir zu Beginn mit der Low-Level-API und Tensors arbeiten. Wenn Sie jedoch schnell vorankommen und nicht viel Zeit mit dem Lernen dieser Details verbringen möchten, können Sie diese überspringen und direkt zu den High-Level-API-Notebooks gehen.

## ✍️ Übungen: Frameworks

Setzen Sie Ihr Lernen in den folgenden Notebooks fort:

Low-Level API | [TensorFlow+Keras Notebook](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [PyTorch](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)
--------------|-------------------------------------|--------------------------------
High-level API| [Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) | *PyTorch Lightning*

Nachdem Sie die Frameworks gemeistert haben, lassen Sie uns das Konzept des Overfittings zusammenfassen.

# Overfitting

Overfitting ist ein äußerst wichtiges Konzept im maschinellen Lernen, und es ist sehr wichtig, es richtig zu verstehen!

Betrachten Sie das folgende Problem, 5 Punkte (dargestellt durch `x` in den Grafiken unten) zu approximieren:

![linear](../../../../../translated_images/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.de.jpg) | ![overfit](../../../../../translated_images/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.de.jpg)
-------------------------|--------------------------
**Lineares Modell, 2 Parameter** | **Nicht-lineares Modell, 7 Parameter**
Training Fehler = 5.3 | Training Fehler = 0
Validierungsfehler = 5.1 | Validierungsfehler = 20

* Links sehen wir eine gute gerade Linienapproximation. Da die Anzahl der Parameter angemessen ist, erfasst das Modell die Idee hinter der Punktverteilung gut.
* Rechts ist das Modell zu mächtig. Da wir nur 5 Punkte haben und das Modell 7 Parameter hat, kann es sich so anpassen, dass es durch alle Punkte verläuft, was den Trainingsfehler auf 0 reduziert. Dies hindert das Modell jedoch daran, das korrekte Muster hinter den Daten zu verstehen, sodass der Validierungsfehler sehr hoch ist.

Es ist sehr wichtig, ein korrektes Gleichgewicht zwischen der Komplexität des Modells (Anzahl der Parameter) und der Anzahl der Trainingsproben zu finden.

## Warum Overfitting auftritt

  * Nicht genügend Trainingsdaten
  * Zu mächtiges Modell
  * Zu viel Rauschen in den Eingabedaten

## Wie man Overfitting erkennt

Wie Sie aus dem obigen Diagramm sehen können, kann Overfitting durch einen sehr niedrigen Trainingsfehler und einen hohen Validierungsfehler erkannt werden. Normalerweise sehen wir während des Trainings, dass sowohl der Trainings- als auch der Validierungsfehler zu sinken beginnen, und dann kann der Validierungsfehler an einem bestimmten Punkt aufhören zu sinken und anfangen zu steigen. Dies wird ein Zeichen für Overfitting sein und der Hinweis, dass wir wahrscheinlich an dieser Stelle das Training stoppen sollten (oder zumindest einen Snapshot des Modells erstellen sollten).

![overfitting](../../../../../translated_images/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.de.png)

## Wie man Overfitting verhindert

Wenn Sie sehen, dass Overfitting auftritt, können Sie Folgendes tun:

 * Erhöhen Sie die Menge an Trainingsdaten
 * Verringern Sie die Komplexität des Modells
 * Verwenden Sie eine [Regularisierungstechnik](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), wie z. B. [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), die wir später betrachten werden.

## Overfitting und Bias-Varianz-Handel

Overfitting ist tatsächlich ein Fall eines allgemeineren Problems in der Statistik, das als [Bias-Varianz-Handel](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff) bekannt ist. Wenn wir die möglichen Fehlerquellen in unserem Modell betrachten, können wir zwei Arten von Fehlern sehen:

* **Bias-Fehler** entstehen, weil unser Algorithmus nicht in der Lage ist, die Beziehung zwischen den Trainingsdaten korrekt zu erfassen. Dies kann darauf zurückzuführen sein, dass unser Modell nicht mächtig genug ist (**Underfitting**).
* **Varianz-Fehler**, die entstehen, weil das Modell Rauschen in den Eingabedaten anstelle von bedeutungsvollen Beziehungen approximiert (**Overfitting**).

Während des Trainings nimmt der Bias-Fehler ab (da unser Modell lernt, die Daten zu approximieren), und der Varianz-Fehler nimmt zu. Es ist wichtig, das Training zu stoppen - entweder manuell (wenn wir Overfitting erkennen) oder automatisch (durch Einführung von Regularisierung) - um Overfitting zu verhindern.

## Fazit

In dieser Lektion haben Sie die Unterschiede zwischen den verschiedenen APIs der beiden beliebtesten KI-Frameworks, TensorFlow und PyTorch, kennengelernt. Darüber hinaus haben Sie ein sehr wichtiges Thema, Overfitting, behandelt.

## 🚀 Herausforderung

In den begleitenden Notebooks finden Sie am Ende 'Aufgaben'; arbeiten Sie die Notebooks durch und erfüllen Sie die Aufgaben.

## [Nachlesequiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/205)

## Überprüfung & Selbststudium

Recherchieren Sie zu den folgenden Themen:

- TensorFlow
- PyTorch
- Overfitting

Stellen Sie sich die folgenden Fragen:

- Was ist der Unterschied zwischen TensorFlow und PyTorch?
- Was ist der Unterschied zwischen Overfitting und Underfitting?

## [Aufgabe](lab/README.md)

In diesem Labor werden Sie gebeten, zwei Klassifikationsprobleme mit ein- und mehrschichtigen voll verbundenen Netzwerken mit PyTorch oder TensorFlow zu lösen.

* [Anweisungen](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/05-Frameworks/lab/LabFrameworks.ipynb)

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.