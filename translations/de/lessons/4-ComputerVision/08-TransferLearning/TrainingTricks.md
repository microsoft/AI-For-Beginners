# Tricks für das Training von Deep Learning

Mit zunehmender Tiefe von neuronalen Netzwerken wird der Trainingsprozess immer herausfordernder. Ein großes Problem sind die sogenannten [verschwindenen Gradienten](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) oder [explodierenden Gradienten](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Dieser Beitrag](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) bietet eine gute Einführung in diese Probleme.

Um das Training tiefer Netzwerke effizienter zu gestalten, können einige Techniken verwendet werden.

## Werte in einem angemessenen Intervall halten

Um numerische Berechnungen stabiler zu machen, möchten wir sicherstellen, dass alle Werte in unserem neuronalen Netzwerk innerhalb eines angemessenen Bereichs liegen, typischerweise [-1..1] oder [0..1]. Dies ist keine sehr strenge Anforderung, aber die Natur der Gleitkomma-Berechnungen ist so, dass Werte unterschiedlicher Größenordnung nicht genau zusammen manipuliert werden können. Wenn wir beispielsweise 10<sup>-10</sup> und 10<sup>10</sup> addieren, erhalten wir wahrscheinlich 10<sup>10</sup>, weil der kleinere Wert "in die gleiche Größenordnung" wie der größere umgewandelt wird, und somit die Mantisse verloren geht.

Die meisten Aktivierungsfunktionen haben Nichtlinearitäten im Bereich von [-1..1], daher macht es Sinn, alle Eingabedaten auf den Intervall [-1..1] oder [0..1] zu skalieren.

## Initiale Gewichtsinitalisierung

Idealerweise möchten wir, dass die Werte nach dem Durchlaufen der Netzwerkebenen im gleichen Bereich liegen. Daher ist es wichtig, die Gewichte so zu initialisieren, dass die Verteilung der Werte erhalten bleibt.

Eine normale Verteilung **N(0,1)** ist keine gute Idee, denn wenn wir *n* Eingaben haben, wäre die Standardabweichung des Outputs *n*, und die Werte würden wahrscheinlich aus dem Intervall [0..1] herausspringen.

Die folgenden Initialisierungen werden häufig verwendet:

 * Gleichverteilung -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** garantiert, dass für Eingaben mit einem Mittelwert von null und einer Standardabweichung von 1 der gleiche Mittelwert/die gleiche Standardabweichung erhalten bleibt.
 * **N(0,√2/(n_in+n_out))** -- die sogenannte **Xavier-Initalisierung** (`glorot`), sie hilft, die Signale während der Vorwärts- und Rückwärtspropagation im Bereich zu halten.

## Batch-Normalisierung

Selbst bei einer ordnungsgemäßen Gewichtsinitalisierung können die Gewichte während des Trainings willkürlich groß oder klein werden, was dazu führt, dass die Signale aus dem richtigen Bereich herauskommen. Wir können die Signale zurückbringen, indem wir eine der **Normalisierung**-Techniken verwenden. Während es mehrere davon gibt (Gewichtsnormierung, Schichtnormalisierung), wird die am häufigsten verwendete Batch-Normalisierung.

Die Idee der **Batch-Normalisierung** besteht darin, alle Werte über das Minibatch hinweg zu berücksichtigen und die Normalisierung (d.h. Mittelwert subtrahieren und durch die Standardabweichung teilen) auf der Grundlage dieser Werte durchzuführen. Sie wird als Netzwerkschicht implementiert, die diese Normalisierung nach der Anwendung der Gewichte, aber vor der Aktivierungsfunktion durchführt. Infolgedessen sehen wir wahrscheinlich eine höhere endgültige Genauigkeit und ein schnelleres Training.

Hier ist das [ursprüngliche Papier](https://arxiv.org/pdf/1502.03167.pdf) zur Batch-Normalisierung, die [Erklärung auf Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization) und [ein guter einführender Blogbeitrag](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (und der [auf Russisch](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** ist eine interessante Technik, die während des Trainings einen bestimmten Prozentsatz zufälliger Neuronen entfernt. Sie wird ebenfalls als Schicht mit einem Parameter (Prozentsatz der zu entfernenden Neuronen, typischerweise 10%-50%) implementiert, und während des Trainings werden zufällige Elemente des Eingangsvektors auf null gesetzt, bevor sie an die nächste Schicht weitergegeben werden.

Obwohl dies seltsam erscheinen mag, können Sie den Effekt von Dropout auf das Training eines MNIST-Ziffernklassifikators im [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb) Notizbuch sehen. Es beschleunigt das Training und ermöglicht es uns, in weniger Trainings-Epochen eine höhere Genauigkeit zu erreichen.

Dieser Effekt kann auf verschiedene Weise erklärt werden:

 * Es kann als ein zufälliger Schockfaktor für das Modell betrachtet werden, der die Optimierung aus dem lokalen Minimum herausnimmt.
 * Es kann als *implizite Modellmittelung* betrachtet werden, weil wir sagen können, dass wir während des Dropouts ein leicht anderes Modell trainieren.

> *Einige Leute sagen, dass wenn eine betrunkene Person versucht, etwas zu lernen, sie sich am nächsten Morgen besser daran erinnert als eine nüchterne Person, weil das Gehirn mit einigen defekten Neuronen versucht, sich besser anzupassen, um den Sinn zu erfassen. Wir haben nie getestet, ob das wahr ist oder nicht.*

## Überanpassung verhindern

Ein sehr wichtiger Aspekt des Deep Learning ist die Fähigkeit, [Überanpassung](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) zu verhindern. Obwohl es verlockend sein könnte, ein sehr leistungsstarkes neuronales Netzwerkmodell zu verwenden, sollten wir immer die Anzahl der Modellparameter mit der Anzahl der Trainingsproben in Einklang bringen.

> Stellen Sie sicher, dass Sie das Konzept der [Überanpassung](../../3-NeuralNetworks/05-Frameworks/Overfitting.md), das wir zuvor eingeführt haben, verstehen!

Es gibt mehrere Möglichkeiten, Überanpassung zu verhindern:

 * Frühes Stoppen -- kontinuierliche Überwachung des Fehlers im Validierungsdatensatz und das Stoppen des Trainings, wenn der Validierungsfehler zu steigen beginnt.
 * Explizite Gewichtsnormierung / Regularisierung -- Hinzufügen einer zusätzlichen Strafe zur Verlustfunktion für hohe absolute Werte der Gewichte, was verhindert, dass das Modell sehr instabile Ergebnisse erzielt.
 * Modellmittelung -- Training mehrerer Modelle und anschließendes Mittelung des Ergebnisses. Dies hilft, die Varianz zu minimieren.
 * Dropout (implizite Modellmittelung).

## Optimierer / Trainingsalgorithmen

Ein weiterer wichtiger Aspekt des Trainings ist die Wahl eines guten Trainingsalgorithmus. Während der klassische **Gradientenabstieg** eine vernünftige Wahl ist, kann er manchmal zu langsam sein oder andere Probleme verursachen.

Im Deep Learning verwenden wir **Stochastic Gradient Descent** (SGD), was ein Gradientabstieg ist, der auf Minibatches angewendet wird, die zufällig aus dem Trainingssatz ausgewählt werden. Die Gewichte werden mit dieser Formel angepasst:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

Im **Momentum SGD** behalten wir einen Teil des Gradienten aus vorherigen Schritten bei. Es ist ähnlich, als würden wir uns mit Trägheit bewegen und einen Stoß in eine andere Richtung erhalten; unsere Trajektorie ändert sich nicht sofort, sondern behält einen Teil der ursprünglichen Bewegung bei. Hier führen wir einen weiteren Vektor v ein, um die *Geschwindigkeit* darzustellen:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup> + v<sup>t+1</sup>

Hier gibt der Parameter γ an, inwieweit wir die Trägheit berücksichtigen: γ=0 entspricht dem klassischen SGD; γ=1 ist eine reine Bewegungsgleichung.

### Adam, Adagrad usw.

Da wir in jeder Schicht Signale mit einer Matrix W<sub>i</sub> multiplizieren, kann der Gradient je nach ||W<sub>i</sub>|| entweder abnehmen und nahe bei 0 sein oder unbegrenzt steigen. Dies ist das Wesen des Problems der explodierenden/verschwindenen Gradienten.

Eine der Lösungen für dieses Problem besteht darin, nur die Richtung des Gradienten in der Gleichung zu verwenden und den absoluten Wert zu ignorieren, d.h.

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), wobei ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Dieser Algorithmus wird **Adagrad** genannt. Weitere Algorithmen, die dieselbe Idee verwenden: **RMSProp**, **Adam**.

> **Adam** gilt als sehr effizienter Algorithmus für viele Anwendungen, also wenn Sie sich nicht sicher sind, welchen Sie verwenden sollen - verwenden Sie Adam.

### Gradientenbeschneidung

Gradientenbeschneidung ist eine Erweiterung der obigen Idee. Wenn ||∇ℒ|| ≤ θ, berücksichtigen wir den ursprünglichen Gradienten bei der Gewichtoptimierung, und wenn ||∇ℒ|| > θ - teilen wir den Gradienten durch seine Norm. Hier ist θ ein Parameter, in den meisten Fällen können wir θ=1 oder θ=10 wählen.

### Lernratenverfall

Der Erfolg des Trainings hängt oft vom Lernratenparameter η ab. Es ist logisch anzunehmen, dass größere Werte von η zu schnellerem Training führen, was wir typischerweise zu Beginn des Trainings wollen, und dann kleinere Werte von η uns ermöglichen, das Netzwerk fein abzustimmen. Daher möchten wir in den meisten Fällen η während des Trainings verringern.

Dies kann erreicht werden, indem η nach jeder Trainings-Epoche mit einer bestimmten Zahl (z.B. 0,98) multipliziert wird oder durch die Verwendung eines komplizierteren **Lernratenplans**.

## Verschiedene Netzwerkarchitekturen

Die Auswahl der richtigen Netzwerkarchitektur für Ihr Problem kann knifflig sein. Normalerweise würden wir eine Architektur wählen, die sich für unsere spezifische Aufgabe (oder eine ähnliche) bewährt hat. Hier ist eine [gute Übersicht](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) über neuronale Netzwerkarchitekturen für die Computer Vision.

> Es ist wichtig, eine Architektur auszuwählen, die leistungsfähig genug für die Anzahl der Trainingsproben ist, die wir haben. Eine zu leistungsstarke Modellwahl kann zu [Überanpassung](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) führen.

Ein weiterer guter Weg wäre, eine Architektur zu verwenden, die sich automatisch an die erforderliche Komplexität anpasst. Bis zu einem gewissen Grad sind die Architekturen **ResNet** und **Inception** selbstanpassend. [Mehr zu Architekturen der Computer Vision](../07-ConvNets/CNN_Architectures.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ausgangssprache sollte als die maßgebliche Quelle betrachtet werden. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Verantwortung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.