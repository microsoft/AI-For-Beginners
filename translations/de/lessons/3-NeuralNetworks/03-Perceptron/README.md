# Einführung in Neuronale Netze: Perzeptron

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Einer der ersten Versuche, etwas Ähnliches wie ein modernes neuronales Netzwerk zu implementieren, wurde 1957 von Frank Rosenblatt vom Cornell Aeronautical Laboratory unternommen. Es handelte sich um eine Hardware-Implementierung namens "Mark-1", die darauf ausgelegt war, primitive geometrische Figuren wie Dreiecke, Quadrate und Kreise zu erkennen.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='Das Mark 1 Perzeptron' />|

> Bilder [von Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Ein Eingabebild wurde durch ein 20x20-Photodetektor-Array dargestellt, sodass das neuronale Netzwerk 400 Eingaben und eine binäre Ausgabe hatte. Ein einfaches Netzwerk bestand aus einem Neuron, das auch als **Schwellwertlogikeinheit** bezeichnet wird. Die Gewichte des neuronalen Netzwerks wirkten wie Potentiometer, die während der Trainingsphase manuell angepasst werden mussten.

> ✅ Ein Potentiometer ist ein Gerät, das es dem Benutzer ermöglicht, den Widerstand eines Schaltkreises anzupassen.

> Die New York Times schrieb zu dieser Zeit über das Perzeptron: *der Embryo eines elektronischen Computers, von dem [die Marine] erwartet, dass er gehen, sprechen, sehen, schreiben, sich selbst reproduzieren und sich seiner Existenz bewusst sein wird.*

## Perzeptron-Modell

Angenommen, wir haben N Merkmale in unserem Modell, in diesem Fall wäre der Eingangsvektor ein Vektor der Größe N. Ein Perzeptron ist ein **binäres Klassifikations**modell, d.h. es kann zwischen zwei Klassen von Eingabedaten unterscheiden. Wir nehmen an, dass für jeden Eingangsvektor x die Ausgabe unseres Perzeptrons entweder +1 oder -1 beträgt, je nach Klasse. Die Ausgabe wird mit der Formel berechnet:

y(x) = f(w<sup>T</sup>x)

wobei f eine Schritt-Aktivierungsfunktion ist.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Training des Perzeptrons

Um ein Perzeptron zu trainieren, müssen wir einen Gewichtungsvektor w finden, der die meisten Werte korrekt klassifiziert, d.h. der den kleinsten **Fehler** ergibt. Dieser Fehler E wird durch das **Perzeptron-Kriterium** wie folgt definiert:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

wobei:

* die Summe über die Trainingsdatenpunkte i genommen wird, die zu einer falschen Klassifikation führen
* x<sub>i</sub> die Eingabedaten sind und t<sub>i</sub> für negative und positive Beispiele entsprechend -1 oder +1 ist.

Dieses Kriterium wird als Funktion der Gewichte w betrachtet, und wir müssen es minimieren. Oft wird eine Methode namens **Gradientenabstieg** verwendet, bei der wir mit einigen Anfangsgewichten w<sup>(0)</sup> beginnen und dann bei jedem Schritt die Gewichte gemäß der Formel aktualisieren:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Hierbei ist η die sogenannte **Lernrate**, und ∇E(w) bezeichnet den **Gradienten** von E. Nachdem wir den Gradienten berechnet haben, erhalten wir

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Der Algorithmus in Python sieht so aus:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Fazit

In dieser Lektion haben Sie über ein Perzeptron gelernt, das ein binäres Klassifikationsmodell ist, und wie man es mit einem Gewichtungsvektor trainiert.

## 🚀 Herausforderung

Wenn Sie versuchen möchten, Ihr eigenes Perzeptron zu bauen, probieren Sie [dieses Labor auf Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), das den [Azure ML Designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste) verwendet.

## [Nachlese-Quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Überprüfung & Selbststudium

Um zu sehen, wie wir das Perzeptron zur Lösung eines Spielzeugsproblems sowie realer Probleme verwenden können und um weiter zu lernen - gehen Sie zum [Perzeptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb) Notizbuch.

Hier ist ein interessanter [Artikel über Perzeptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590
) ebenfalls.

## [Aufgabe](lab/README.md)

In dieser Lektion haben wir ein Perzeptron für die binäre Klassifizierungsaufgabe implementiert und es verwendet, um zwischen zwei handgeschriebenen Ziffern zu klassifizieren. In diesem Labor sind Sie aufgefordert, das Problem der Ziffernklassifizierung vollständig zu lösen, d.h. zu bestimmen, welche Ziffer am wahrscheinlichsten einem gegebenen Bild entspricht.

* [Anleitungen](lab/README.md)
* [Notizbuch](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.