# Einführung in Neuronale Netzwerke. Mehrschichtiger Perzeptron

Im vorherigen Abschnitt haben Sie das einfachste Modell eines neuronalen Netzwerks kennengelernt - den einlagigen Perzeptron, ein lineares Klassifikationsmodell für zwei Klassen.

In diesem Abschnitt werden wir dieses Modell zu einem flexibleren Rahmen erweitern, der es uns ermöglicht:

* **Mehrklassenklassifikation** zusätzlich zur Zwei-Klassen-Klassifikation durchzuführen
* **Regressionsprobleme** zusätzlich zur Klassifikation zu lösen
* Klassen zu trennen, die nicht linear separierbar sind

Wir werden auch unser eigenes modulares Framework in Python entwickeln, das es uns ermöglicht, verschiedene Architekturen neuronaler Netzwerke zu konstruieren.

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/104)

## Formalisierung des Maschinellen Lernens

Lassen Sie uns mit der Formalisierung des Problems des Maschinellen Lernens beginnen. Angenommen, wir haben einen Trainingsdatensatz **X** mit Labels **Y**, und wir müssen ein Modell *f* erstellen, das die genauesten Vorhersagen trifft. Die Qualität der Vorhersagen wird durch die **Verlustfunktion** ℒ gemessen. Folgende Verlustfunktionen werden häufig verwendet:

* Für das Regressionsproblem, wenn wir eine Zahl vorhersagen müssen, können wir den **absoluten Fehler** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| oder den **quadratischen Fehler** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup> verwenden
* Für die Klassifikation verwenden wir den **0-1 Fehler** (der im Wesentlichen dasselbe wie die **Genauigkeit** des Modells ist) oder den **logistischen Fehler**.

Für den einlagigen Perzeptron wurde die Funktion *f* als lineare Funktion *f(x)=wx+b* definiert (hier ist *w* die Gewichtsmatrix, *x* der Vektor der Eingangsmerkmale und *b* der Bias-Vektor). Für verschiedene Architekturen neuronaler Netzwerke kann diese Funktion komplexere Formen annehmen.

> Im Falle der Klassifikation ist es oft wünschenswert, Wahrscheinlichkeiten der entsprechenden Klassen als Netzwerk-Ausgabe zu erhalten. Um willkürliche Zahlen in Wahrscheinlichkeiten umzuwandeln (z.B. um die Ausgabe zu normalisieren), verwenden wir oft die **Softmax**-Funktion σ, und die Funktion *f* wird zu *f(x)=σ(wx+b)*

In der obigen Definition von *f* werden *w* und *b* als **Parameter** θ=⟨*w,b*⟩ bezeichnet. Gegebenen den Datensatz ⟨**X**,**Y**⟩ können wir einen Gesamter Fehler über den gesamten Datensatz als Funktion der Parameter θ berechnen.

> ✅ **Das Ziel des Trainings eines neuronalen Netzwerks besteht darin, den Fehler durch Variieren der Parameter θ zu minimieren.**

## Gradientabstieg-Optimierung

Es gibt eine bekannte Methode zur Optimierung von Funktionen, die als **Gradientenabstieg** bezeichnet wird. Die Idee ist, dass wir die Ableitung (im mehrdimensionalen Fall als **Gradient** bezeichnet) der Verlustfunktion bezüglich der Parameter berechnen und die Parameter so variieren, dass der Fehler sinkt. Dies kann wie folgt formalisiert werden:

* Initialisieren Sie die Parameter mit zufälligen Werten w<sup>(0)</sup>, b<sup>(0)</sup>
* Wiederholen Sie den folgenden Schritt viele Male:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Während des Trainings sollen die Optimierungsschritte unter Berücksichtigung des gesamten Datensatzes berechnet werden (denken Sie daran, dass der Verlust als Summe über alle Trainingsproben berechnet wird). In der Praxis nehmen wir jedoch kleine Portionen des Datensatzes, die als **Minibatches** bezeichnet werden, und berechnen die Gradienten basierend auf einer Teilmenge von Daten. Da die Teilmenge jedes Mal zufällig ausgewählt wird, wird diese Methode als **stochastischer Gradientabstieg** (SGD) bezeichnet.

## Mehrschichtige Perzeptrons und Rückpropagation

Das einlagige Netzwerk, wie wir oben gesehen haben, ist in der Lage, linear separierbare Klassen zu klassifizieren. Um ein reichhaltigeres Modell zu erstellen, können wir mehrere Schichten des Netzwerks kombinieren. Mathematisch würde das bedeuten, dass die Funktion *f* eine komplexere Form annehmen würde und in mehreren Schritten berechnet wird:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Hier ist α eine **nicht-lineare Aktivierungsfunktion**, σ ist eine Softmax-Funktion, und die Parameter sind θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Der Gradientabstiegsalgorithmus bleibt derselbe, aber es wird schwieriger, die Gradienten zu berechnen. Gegebenen der Kettenregel für Ableitungen können wir die Ableitungen wie folgt berechnen:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Die Kettenregel wird verwendet, um die Ableitungen der Verlustfunktion bezüglich der Parameter zu berechnen.

Beachten Sie, dass der linkeste Teil all dieser Ausdrücke gleich ist, und somit können wir die Ableitungen effektiv berechnen, indem wir von der Verlustfunktion ausgehen und "rückwärts" durch den Berechnungsgraphen gehen. Daher wird die Methode zum Trainieren eines mehrschichtigen Perzeptrons als **Rückpropagation** oder 'Backprop' bezeichnet.

<img alt="Berechnungsgraph" src="images/ComputeGraphGrad.png"/>

> TODO: Bildnachweis

> ✅ Wir werden die Rückpropagation in unserem Notizbuchbeispiel viel detaillierter behandeln.  

## Fazit

In dieser Lektion haben wir unsere eigene Bibliothek für neuronale Netzwerke erstellt und sie für eine einfache zweidimensionale Klassifikationsaufgabe verwendet.

## 🚀 Herausforderung

Im begleitenden Notizbuch werden Sie Ihr eigenes Framework zur Erstellung und zum Training von mehrschichtigen Perzeptrons implementieren. Sie werden im Detail sehen, wie moderne neuronale Netzwerke funktionieren.

Gehen Sie zum Notizbuch [OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) und arbeiten Sie es durch.

## [Nachvorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/204)

## Überprüfung & Selbststudium

Rückpropagation ist ein gängiger Algorithmus, der in KI und ML verwendet wird und es wert ist, [im Detail](https://wikipedia.org/wiki/Backpropagation) studiert zu werden.

## [Aufgabe](lab/README.md)

In diesem Labor werden Sie gebeten, das Framework, das Sie in dieser Lektion erstellt haben, zu verwenden, um die Klassifikation handgeschriebener Ziffern im MNIST-Datensatz zu lösen.

* [Anleitungen](lab/README.md)
* [Notizbuch](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)

**Haftungsausschluss**:  
Dieses Dokument wurde mit Hilfe von KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.