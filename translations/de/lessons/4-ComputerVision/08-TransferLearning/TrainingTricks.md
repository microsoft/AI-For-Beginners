# Deep Learning Training Tricks

Je tiefer neuronale Netzwerke werden, desto herausfordernder wird ihr Training. Ein Hauptproblem sind die sogenannten [verschwindenden Gradienten](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) oder [explodierenden Gradienten](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Dieser Artikel](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) bietet eine gute Einführung in diese Probleme.

Um das Training tiefer Netzwerke effizienter zu gestalten, gibt es einige Techniken, die angewendet werden können.

## Werte in einem vernünftigen Bereich halten

Um numerische Berechnungen stabiler zu machen, sollten alle Werte innerhalb des neuronalen Netzwerks in einem vernünftigen Bereich liegen, typischerweise [-1..1] oder [0..1]. Dies ist keine strikte Anforderung, aber die Natur von Gleitkomma-Berechnungen ist so, dass Werte unterschiedlicher Größenordnungen nicht genau zusammen verarbeitet werden können. Zum Beispiel, wenn wir 10<sup>-10</sup> und 10<sup>10</sup> addieren, erhalten wir wahrscheinlich 10<sup>10</sup>, da der kleinere Wert auf die gleiche Größenordnung wie der größere "umgerechnet" wird und somit die Mantisse verloren geht.

Die meisten Aktivierungsfunktionen haben Nichtlinearitäten im Bereich von [-1..1], daher macht es Sinn, alle Eingabedaten auf den Bereich [-1..1] oder [0..1] zu skalieren.

## Initialisierung der Gewichte

Idealerweise sollten die Werte nach dem Durchlaufen der Netzwerkschichten im gleichen Bereich bleiben. Daher ist es wichtig, die Gewichte so zu initialisieren, dass die Verteilung der Werte erhalten bleibt.

Eine Normalverteilung **N(0,1)** ist keine gute Idee, da bei *n* Eingaben die Standardabweichung der Ausgabe *n* wäre und die Werte wahrscheinlich aus dem Bereich [0..1] herausfallen.

Die folgenden Initialisierungen werden häufig verwendet:

 * Gleichverteilung -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** garantiert, dass für Eingaben mit einem Mittelwert von 0 und einer Standardabweichung von 1 der gleiche Mittelwert/Standardabweichung erhalten bleibt
 * **N(0,√2/(n_in+n_out))** -- die sogenannte **Xavier-Initialisierung** (`glorot`), die hilft, die Signale während der Vorwärts- und Rückwärtsausbreitung im Bereich zu halten

## Batch-Normalisierung

Selbst bei ordnungsgemäßer Initialisierung der Gewichte können diese während des Trainings beliebig groß oder klein werden und die Signale aus dem richtigen Bereich bringen. Wir können die Signale mit einer der **Normalisierungstechniken** wieder in den Bereich bringen. Während es mehrere davon gibt (Gewichtsnormierung, Schichtnormierung), wird am häufigsten die Batch-Normalisierung verwendet.

Die Idee der **Batch-Normalisierung** besteht darin, alle Werte innerhalb des Minibatches zu berücksichtigen und eine Normalisierung (d. h. Mittelwert abziehen und durch Standardabweichung teilen) basierend auf diesen Werten durchzuführen. Sie wird als Netzwerkschicht implementiert, die diese Normalisierung nach der Anwendung der Gewichte, aber vor der Aktivierungsfunktion durchführt. Dadurch erreichen wir in der Regel eine höhere Endgenauigkeit und schnelleres Training.

Hier ist das [Originalpapier](https://arxiv.org/pdf/1502.03167.pdf) zur Batch-Normalisierung, die [Erklärung auf Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization) und [ein guter einführender Blogbeitrag](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (und einer [auf Russisch](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** ist eine interessante Technik, bei der ein bestimmter Prozentsatz zufälliger Neuronen während des Trainings entfernt wird. Es wird ebenfalls als Schicht mit einem Parameter (Prozentsatz der zu entfernenden Neuronen, typischerweise 10%-50%) implementiert, und während des Trainings werden zufällige Elemente des Eingabevektors auf null gesetzt, bevor sie an die nächste Schicht weitergegeben werden.

Auch wenn dies seltsam klingen mag, können Sie die Wirkung von Dropout beim Training eines MNIST-Ziffernklassifikators im [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb)-Notebook sehen. Es beschleunigt das Training und ermöglicht es uns, in weniger Trainingsepochen eine höhere Genauigkeit zu erreichen.

Dieser Effekt kann auf verschiedene Weise erklärt werden:

 * Es kann als zufälliger Schockfaktor für das Modell betrachtet werden, der die Optimierung aus einem lokalen Minimum herausführt
 * Es kann als *implizites Modellmittelwertbilden* betrachtet werden, da man sagen kann, dass während des Dropouts leicht unterschiedliche Modelle trainiert werden

> *Manche Leute sagen, dass eine betrunkene Person, die versucht, etwas zu lernen, sich dies am nächsten Morgen besser merken kann als eine nüchterne Person, weil ein Gehirn mit einigen fehlerhaften Neuronen besser versucht, den Sinn zu erfassen. Wir haben nie getestet, ob das stimmt oder nicht.*

## Überanpassung verhindern

Ein sehr wichtiger Aspekt des Deep Learnings ist es, [Überanpassung](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) zu verhindern. Auch wenn es verlockend sein mag, ein sehr leistungsstarkes neuronales Netzwerkmodell zu verwenden, sollten wir die Anzahl der Modellparameter immer mit der Anzahl der Trainingsbeispiele in Einklang bringen.

> Stellen Sie sicher, dass Sie das Konzept der [Überanpassung](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) verstanden haben, das wir zuvor eingeführt haben!

Es gibt mehrere Möglichkeiten, Überanpassung zu verhindern:

 * Frühes Stoppen -- kontinuierliches Überwachen des Fehlers auf dem Validierungsdatensatz und Beenden des Trainings, wenn der Validierungsfehler zu steigen beginnt.
 * Expliziter Gewichtsrückgang / Regularisierung -- Hinzufügen einer zusätzlichen Strafe zur Verlustfunktion für hohe absolute Werte der Gewichte, was verhindert, dass das Modell sehr instabile Ergebnisse liefert
 * Modellmittelwertbildung -- Training mehrerer Modelle und anschließendes Mitteln der Ergebnisse. Dies hilft, die Varianz zu minimieren.
 * Dropout (implizite Modellmittelwertbildung)

## Optimierer / Trainingsalgorithmen

Ein weiterer wichtiger Aspekt des Trainings ist die Wahl eines guten Trainingsalgorithmus. Während der klassische **Gradientenabstieg** eine vernünftige Wahl ist, kann er manchmal zu langsam sein oder andere Probleme verursachen.

Im Deep Learning verwenden wir den **stochastischen Gradientenabstieg** (SGD), der ein Gradientenabstieg ist, der auf Minibatches angewendet wird, die zufällig aus dem Trainingssatz ausgewählt werden. Die Gewichte werden mit dieser Formel angepasst:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

Beim **Momentum-SGD** behalten wir einen Teil des Gradienten aus vorherigen Schritten bei. Es ist ähnlich wie bei einer Bewegung mit Trägheit: Wenn wir in eine Richtung unterwegs sind und einen Stoß in eine andere Richtung erhalten, ändert sich unsere Flugbahn nicht sofort, sondern behält einen Teil der ursprünglichen Bewegung bei. Hier führen wir einen weiteren Vektor v ein, um die *Geschwindigkeit* darzustellen:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Hier gibt der Parameter γ an, in welchem Maße wir die Trägheit berücksichtigen: γ=0 entspricht dem klassischen SGD; γ=1 ist eine reine Bewegungsgleichung.

### Adam, Adagrad, etc.

Da in jeder Schicht Signale mit einer Matrix W<sub>i</sub> multipliziert werden, kann der Gradient je nach ||W<sub>i</sub>|| entweder verschwinden und nahe 0 sein oder unbegrenzt ansteigen. Dies ist das Wesen des Exploding/Vanishing-Gradients-Problems.

Eine Lösung für dieses Problem besteht darin, in der Gleichung nur die Richtung des Gradienten zu verwenden und den absoluten Wert zu ignorieren, d. h.

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), wobei ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Dieser Algorithmus wird **Adagrad** genannt. Andere Algorithmen, die dieselbe Idee verwenden: **RMSProp**, **Adam**

> **Adam** gilt als ein sehr effizienter Algorithmus für viele Anwendungen. Wenn Sie sich nicht sicher sind, welchen Sie verwenden sollen, nehmen Sie Adam.

### Gradient Clipping

Gradient Clipping ist eine Erweiterung der obigen Idee. Wenn ||∇ℒ|| ≤ θ, verwenden wir den ursprünglichen Gradienten in der Gewichtsoptimierung, und wenn ||∇ℒ|| > θ, teilen wir den Gradienten durch seine Norm. Hier ist θ ein Parameter, in den meisten Fällen können wir θ=1 oder θ=10 wählen.

### Lernratenabnahme

Der Erfolg des Trainings hängt oft vom Lernratenparameter η ab. Es ist logisch anzunehmen, dass größere Werte von η zu schnellerem Training führen, was wir typischerweise zu Beginn des Trainings wollen, und dass kleinere Werte von η es uns ermöglichen, das Netzwerk fein abzustimmen. Daher möchten wir in den meisten Fällen η im Verlauf des Trainings verringern.

Dies kann erreicht werden, indem η nach jeder Epoche des Trainings mit einer Zahl (z. B. 0,98) multipliziert wird, oder durch die Verwendung eines komplizierteren **Lernratenplans**.

## Verschiedene Netzwerkarchitekturen

Die Auswahl der richtigen Netzwerkarchitektur für Ihr Problem kann knifflig sein. Normalerweise würden wir eine Architektur wählen, die sich für unsere spezifische Aufgabe (oder eine ähnliche) bewährt hat. Hier ist ein [guter Überblick](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) über neuronale Netzwerkarchitekturen für Computer Vision.

> Es ist wichtig, eine Architektur zu wählen, die leistungsstark genug für die Anzahl der Trainingsbeispiele ist, die wir haben. Eine zu leistungsstarke Modellwahl kann zu [Überanpassung](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) führen.

Eine weitere gute Möglichkeit wäre die Verwendung einer Architektur, die sich automatisch an die erforderliche Komplexität anpasst. Bis zu einem gewissen Grad sind die **ResNet**-Architektur und **Inception** selbstanpassend. [Mehr zu Computer-Vision-Architekturen](../07-ConvNets/CNN_Architectures.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.