<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-24T09:39:49+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "de"
}
-->
# Einführung in Neuronale Netze. Mehrschichtiger Perzeptron

Im vorherigen Abschnitt hast du das einfachste Modell eines neuronalen Netzes kennengelernt – den einlagigen Perzeptron, ein lineares Klassifikationsmodell für zwei Klassen.

In diesem Abschnitt erweitern wir dieses Modell zu einem flexibleren Framework, das uns ermöglicht:

* **Mehrklassenklassifikation** zusätzlich zur Zweiklassenklassifikation durchzuführen
* **Regressionsprobleme** zusätzlich zur Klassifikation zu lösen
* Klassen zu trennen, die nicht linear separierbar sind

Wir werden außerdem unser eigenes modulares Framework in Python entwickeln, mit dem wir verschiedene Architekturen neuronaler Netze erstellen können.

## [Quiz vor der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Formalisierung des maschinellen Lernens

Beginnen wir mit der Formalisierung des Problems des maschinellen Lernens. Angenommen, wir haben einen Trainingsdatensatz **X** mit Labels **Y**, und wir müssen ein Modell *f* erstellen, das möglichst genaue Vorhersagen trifft. Die Qualität der Vorhersagen wird durch die **Verlustfunktion** ℒ gemessen. Die folgenden Verlustfunktionen werden häufig verwendet:

* Für Regressionsprobleme, bei denen wir eine Zahl vorhersagen müssen, können wir den **absoluten Fehler** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| oder den **quadratischen Fehler** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup> verwenden.
* Für Klassifikationen verwenden wir den **0-1-Verlust** (der im Wesentlichen der **Genauigkeit** des Modells entspricht) oder den **logistischen Verlust**.

Für den einlagigen Perzeptron wurde die Funktion *f* als lineare Funktion definiert: *f(x)=wx+b* (hierbei ist *w* die Gewichtsmatrix, *x* der Vektor der Eingabefeatures und *b* der Bias-Vektor). Für verschiedene Architekturen neuronaler Netze kann diese Funktion eine komplexere Form annehmen.

> Im Fall der Klassifikation ist es oft wünschenswert, Wahrscheinlichkeiten der entsprechenden Klassen als Ausgabe des Netzes zu erhalten. Um beliebige Zahlen in Wahrscheinlichkeiten umzuwandeln (z. B. um die Ausgabe zu normalisieren), verwenden wir oft die **Softmax-Funktion** σ, und die Funktion *f* wird zu *f(x)=σ(wx+b)*.

In der obigen Definition von *f* werden *w* und *b* als **Parameter** θ=⟨*w,b*⟩ bezeichnet. Gegeben den Datensatz ⟨**X**,**Y**⟩, können wir den Gesamterror für den gesamten Datensatz als Funktion der Parameter θ berechnen.

> ✅ **Das Ziel des Trainings eines neuronalen Netzes ist es, den Fehler durch Variation der Parameter θ zu minimieren.**

## Gradient-Descent-Optimierung

Es gibt eine bekannte Methode zur Optimierung von Funktionen, die als **Gradient Descent** bezeichnet wird. Die Idee ist, dass wir eine Ableitung (im mehrdimensionalen Fall als **Gradient** bezeichnet) der Verlustfunktion in Bezug auf die Parameter berechnen und die Parameter so variieren können, dass der Fehler abnimmt. Dies kann wie folgt formalisiert werden:

* Initialisiere die Parameter mit zufälligen Werten w<sup>(0)</sup>, b<sup>(0)</sup>
* Wiederhole die folgenden Schritte viele Male:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Während des Trainings sollten die Optimierungsschritte unter Berücksichtigung des gesamten Datensatzes berechnet werden (denk daran, dass der Verlust als Summe über alle Trainingsbeispiele berechnet wird). In der Praxis nehmen wir jedoch kleine Teile des Datensatzes, sogenannte **Minibatches**, und berechnen die Gradienten basierend auf einem Teil der Daten. Da der Teil jedes Mal zufällig ausgewählt wird, wird diese Methode als **stochastischer Gradient Descent** (SGD) bezeichnet.

## Mehrschichtige Perzeptrons und Backpropagation

Ein einlagiges Netzwerk, wie wir oben gesehen haben, ist in der Lage, linear separierbare Klassen zu klassifizieren. Um ein komplexeres Modell zu erstellen, können wir mehrere Schichten des Netzwerks kombinieren. Mathematisch bedeutet dies, dass die Funktion *f* eine komplexere Form annimmt und in mehreren Schritten berechnet wird:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Hierbei ist α eine **nichtlineare Aktivierungsfunktion**, σ eine Softmax-Funktion, und die Parameter θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Der Gradient-Descent-Algorithmus bleibt derselbe, aber die Berechnung der Gradienten wird schwieriger. Mithilfe der Kettenregel der Differentiation können wir die Ableitungen wie folgt berechnen:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Die Kettenregel der Differentiation wird verwendet, um die Ableitungen der Verlustfunktion in Bezug auf die Parameter zu berechnen.

Beachte, dass der linke Teil all dieser Ausdrücke identisch ist, und daher können wir die Ableitungen effizient berechnen, indem wir von der Verlustfunktion ausgehend "rückwärts" durch den Berechnungsgraphen gehen. Daher wird die Methode zum Trainieren eines mehrschichtigen Perzeptrons als **Backpropagation** oder 'Backprop' bezeichnet.

<img alt="Berechnungsgraph" src="images/ComputeGraphGrad.png"/>

> TODO: Bildnachweis

> ✅ Wir werden Backpropagation in unserem Notebook-Beispiel noch viel detaillierter behandeln.

## Fazit

In dieser Lektion haben wir unsere eigene Bibliothek für neuronale Netze erstellt und sie für eine einfache zweidimensionale Klassifikationsaufgabe verwendet.

## 🚀 Herausforderung

Im begleitenden Notebook wirst du dein eigenes Framework zur Erstellung und zum Training mehrschichtiger Perzeptrons implementieren. Du wirst im Detail sehen, wie moderne neuronale Netze funktionieren.

Gehe zum [OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) Notebook und arbeite es durch.

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Rückblick & Selbststudium

Backpropagation ist ein gängiger Algorithmus in KI und ML, der es wert ist, [im Detail](https://wikipedia.org/wiki/Backpropagation) studiert zu werden.

## [Aufgabe](lab/README.md)

In diesem Labor wirst du das Framework, das du in dieser Lektion erstellt hast, verwenden, um die Klassifikation handgeschriebener Ziffern aus dem MNIST-Datensatz zu lösen.

* [Anweisungen](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.