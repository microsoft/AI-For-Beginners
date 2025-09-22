<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b544f20b796402507fb05a0df893323",
  "translation_date": "2025-08-24T09:40:17+00:00",
  "source_file": "lessons/3-NeuralNetworks/05-Frameworks/README.md",
  "language_code": "de"
}
-->
# Neuronale Netzwerk-Frameworks

Wie wir bereits gelernt haben, müssen wir zwei Dinge tun, um neuronale Netzwerke effizient trainieren zu können:

* Mit Tensoren arbeiten, z. B. multiplizieren, addieren und Funktionen wie Sigmoid oder Softmax berechnen
* Gradienten aller Ausdrücke berechnen, um die Gradientenabstiegsoptimierung durchzuführen

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/9)

Während die Bibliothek `numpy` den ersten Teil übernehmen kann, benötigen wir einen Mechanismus, um Gradienten zu berechnen. In [unserem Framework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb), das wir im vorherigen Abschnitt entwickelt haben, mussten wir alle Ableitungsfunktionen manuell im `backward`-Methodenprogrammieren, die die Rückwärtspropagation durchführt. Idealerweise sollte ein Framework uns die Möglichkeit geben, Gradienten für *jeden Ausdruck* zu berechnen, den wir definieren können.

Ein weiterer wichtiger Punkt ist die Möglichkeit, Berechnungen auf der GPU oder anderen spezialisierten Recheneinheiten wie [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit) durchzuführen. Das Training tiefer neuronaler Netzwerke erfordert *sehr viele* Berechnungen, und die Möglichkeit, diese Berechnungen auf GPUs zu parallelisieren, ist von großer Bedeutung.

> ✅ Der Begriff 'parallelisieren' bedeutet, die Berechnungen auf mehrere Geräte zu verteilen.

Derzeit sind die beiden beliebtesten neuronalen Frameworks: [TensorFlow](http://TensorFlow.org) und [PyTorch](https://pytorch.org/). Beide bieten eine Low-Level-API, um mit Tensoren sowohl auf der CPU als auch auf der GPU zu arbeiten. Zusätzlich zur Low-Level-API gibt es auch eine High-Level-API, die entsprechend [Keras](https://keras.io/) und [PyTorch Lightning](https://pytorchlightning.ai/) genannt wird.

Low-Level API | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
--------------|-------------------------------------|--------------------------------
High-Level API| [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**Low-Level-APIs** in beiden Frameworks ermöglichen es, sogenannte **Rechengraphen** zu erstellen. Dieser Graph definiert, wie die Ausgabe (normalerweise die Verlustfunktion) mit gegebenen Eingabeparametern berechnet wird, und kann zur Berechnung auf die GPU übertragen werden, falls verfügbar. Es gibt Funktionen, um diesen Rechengraphen zu differenzieren und Gradienten zu berechnen, die dann zur Optimierung der Modellparameter verwendet werden können.

**High-Level-APIs** betrachten neuronale Netzwerke im Wesentlichen als eine **Abfolge von Schichten** und erleichtern den Aufbau der meisten neuronalen Netzwerke erheblich. Das Training des Modells erfordert in der Regel die Vorbereitung der Daten und dann das Aufrufen einer `fit`-Funktion, um die Arbeit zu erledigen.

Die High-Level-API ermöglicht es, typische neuronale Netzwerke sehr schnell zu erstellen, ohne sich um viele Details kümmern zu müssen. Gleichzeitig bieten Low-Level-APIs viel mehr Kontrolle über den Trainingsprozess und werden daher häufig in der Forschung verwendet, wenn man mit neuen Architekturen neuronaler Netzwerke arbeitet.

Es ist auch wichtig zu verstehen, dass beide APIs zusammen verwendet werden können, z. B. kann man eine eigene Netzwerkschichtarchitektur mit der Low-Level-API entwickeln und diese dann in einem größeren Netzwerk verwenden, das mit der High-Level-API erstellt und trainiert wurde. Oder man definiert ein Netzwerk mit der High-Level-API als Abfolge von Schichten und verwendet dann eine eigene Low-Level-Trainingsschleife zur Optimierung. Beide APIs basieren auf denselben grundlegenden Konzepten und sind so konzipiert, dass sie gut zusammenarbeiten.

## Lernen

In diesem Kurs bieten wir die meisten Inhalte sowohl für PyTorch als auch für TensorFlow an. Sie können Ihr bevorzugtes Framework auswählen und nur die entsprechenden Notebooks durchgehen. Wenn Sie sich nicht sicher sind, welches Framework Sie wählen sollen, lesen Sie einige Diskussionen im Internet über **PyTorch vs. TensorFlow**. Sie können sich auch beide Frameworks ansehen, um ein besseres Verständnis zu bekommen.

Wo möglich, verwenden wir High-Level-APIs der Einfachheit halber. Wir glauben jedoch, dass es wichtig ist, zu verstehen, wie neuronale Netzwerke von Grund auf funktionieren. Daher beginnen wir zunächst mit der Arbeit mit Low-Level-APIs und Tensoren. Wenn Sie jedoch schnell loslegen möchten und nicht viel Zeit mit diesen Details verbringen möchten, können Sie diese überspringen und direkt zu den High-Level-API-Notebooks wechseln.

## ✍️ Übungen: Frameworks

Setzen Sie Ihr Lernen in den folgenden Notebooks fort:

Low-Level API | [TensorFlow+Keras Notebook](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [PyTorch](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)
--------------|-------------------------------------|--------------------------------
High-Level API| [Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) | *PyTorch Lightning*

Nachdem Sie die Frameworks gemeistert haben, lassen Sie uns das Konzept des Overfittings rekapitulieren.

# Overfitting

Overfitting ist ein äußerst wichtiges Konzept im maschinellen Lernen, und es ist sehr wichtig, es richtig zu verstehen!

Betrachten Sie das folgende Problem der Annäherung an 5 Punkte (dargestellt durch `x` in den untenstehenden Diagrammen):

![linear](../../../../../lessons/3-NeuralNetworks/images/overfit1.jpg) | ![overfit](../../../../../lessons/3-NeuralNetworks/images/overfit2.jpg)
-------------------------|--------------------------
**Lineares Modell, 2 Parameter** | **Nicht-lineares Modell, 7 Parameter**
Trainingsfehler = 5.3 | Trainingsfehler = 0
Validierungsfehler = 5.1 | Validierungsfehler = 20

* Links sehen wir eine gute lineare Annäherung. Da die Anzahl der Parameter angemessen ist, erfasst das Modell die Verteilung der Punkte korrekt.
* Rechts ist das Modell zu mächtig. Da wir nur 5 Punkte haben und das Modell 7 Parameter hat, kann es sich so anpassen, dass es durch alle Punkte verläuft, wodurch der Trainingsfehler 0 wird. Dies verhindert jedoch, dass das Modell das richtige Muster hinter den Daten versteht, was zu einem sehr hohen Validierungsfehler führt.

Es ist sehr wichtig, ein korrektes Gleichgewicht zwischen der Komplexität des Modells (Anzahl der Parameter) und der Anzahl der Trainingsbeispiele zu finden.

## Warum Overfitting auftritt

  * Zu wenig Trainingsdaten
  * Zu mächtiges Modell
  * Zu viel Rauschen in den Eingabedaten

## Wie man Overfitting erkennt

Wie Sie aus dem obigen Diagramm sehen können, kann Overfitting durch einen sehr niedrigen Trainingsfehler und einen hohen Validierungsfehler erkannt werden. Normalerweise sehen wir während des Trainings, dass sowohl der Trainings- als auch der Validierungsfehler zunächst abnehmen. An einem bestimmten Punkt könnte der Validierungsfehler jedoch aufhören zu sinken und anfangen zu steigen. Dies ist ein Zeichen für Overfitting und ein Hinweis darauf, dass wir das Training an diesem Punkt wahrscheinlich stoppen sollten (oder zumindest einen Schnappschuss des Modells machen sollten).

![overfitting](../../../../../lessons/3-NeuralNetworks/images/Overfitting.png)

## Wie man Overfitting verhindert

Wenn Sie feststellen, dass Overfitting auftritt, können Sie Folgendes tun:

 * Die Menge der Trainingsdaten erhöhen
 * Die Komplexität des Modells verringern
 * Eine [Regularisierungstechnik](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md) verwenden, wie z. B. [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), die wir später betrachten werden.

## Overfitting und Bias-Varianz-Abwägung

Overfitting ist tatsächlich ein Fall eines allgemeineren Problems in der Statistik, das als [Bias-Varianz-Abwägung](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff) bezeichnet wird. Wenn wir die möglichen Fehlerquellen in unserem Modell betrachten, können wir zwei Arten von Fehlern erkennen:

* **Bias-Fehler** entstehen dadurch, dass unser Algorithmus die Beziehung zwischen den Trainingsdaten nicht korrekt erfassen kann. Dies kann darauf zurückzuführen sein, dass unser Modell nicht mächtig genug ist (**Underfitting**).
* **Varianz-Fehler**, die dadurch entstehen, dass das Modell Rauschen in den Eingabedaten anstelle einer sinnvollen Beziehung approximiert (**Overfitting**).

Während des Trainings nimmt der Bias-Fehler ab (da unser Modell lernt, die Daten zu approximieren), und der Varianz-Fehler nimmt zu. Es ist wichtig, das Training zu stoppen - entweder manuell (wenn wir Overfitting erkennen) oder automatisch (durch Einführung von Regularisierung) -, um Overfitting zu verhindern.

## Fazit

In dieser Lektion haben Sie die Unterschiede zwischen den verschiedenen APIs der beiden beliebtesten KI-Frameworks, TensorFlow und PyTorch, kennengelernt. Außerdem haben Sie ein sehr wichtiges Thema, Overfitting, behandelt.

## 🚀 Herausforderung

In den begleitenden Notebooks finden Sie 'Aufgaben' am Ende; arbeiten Sie die Notebooks durch und lösen Sie die Aufgaben.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/10)

## Überprüfung & Selbststudium

Recherchieren Sie zu den folgenden Themen:

- TensorFlow
- PyTorch
- Overfitting

Stellen Sie sich die folgenden Fragen:

- Was ist der Unterschied zwischen TensorFlow und PyTorch?
- Was ist der Unterschied zwischen Overfitting und Underfitting?

## [Aufgabe](lab/README.md)

In diesem Labor sollen Sie zwei Klassifikationsprobleme mit ein- und mehrschichtigen vollständig verbundenen Netzwerken mithilfe von PyTorch oder TensorFlow lösen.

* [Anleitung](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/05-Frameworks/lab/LabFrameworks.ipynb)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.