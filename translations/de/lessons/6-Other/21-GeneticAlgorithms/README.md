# Genetische Algorithmen

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Genetische Algorithmen** (GA) basieren auf einem **evolutionären Ansatz** für KI, bei dem Methoden der Evolution einer Population verwendet werden, um eine optimale Lösung für ein gegebenes Problem zu finden. Sie wurden 1975 von [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland) vorgeschlagen.

Genetische Algorithmen beruhen auf den folgenden Ideen:

* Gültige Lösungen für das Problem können als **Gene** dargestellt werden.
* **Crossover** ermöglicht es uns, zwei Lösungen zu kombinieren, um eine neue gültige Lösung zu erhalten.
* **Selektion** wird verwendet, um optimalere Lösungen mithilfe einer **Fitnessfunktion** auszuwählen.
* **Mutationen** werden eingeführt, um die Optimierung zu destabilisieren und uns aus dem lokalen Minimum herauszuholen.

Wenn Sie einen genetischen Algorithmus implementieren möchten, benötigen Sie Folgendes:

* Eine Methode zu finden, um unsere Problemlösungen mit **Genen** g∈Γ zu codieren.
* Auf der Menge der Gene Γ müssen wir eine **Fitnessfunktion** fit: Γ→**R** definieren. Kleinere Funktionswerte entsprechen besseren Lösungen.
* Einen **Crossover**-Mechanismus zu definieren, um zwei Gene zu kombinieren, um eine neue gültige Lösung zu erhalten: crossover: Γ<sup>2</sub>→Γ.
* Einen **Mutations**-Mechanismus zu definieren: mutate: Γ→Γ.

In vielen Fällen sind Crossover und Mutation recht einfache Algorithmen, um Gene als numerische Sequenzen oder Bitvektoren zu manipulieren.

Die spezifische Implementierung eines genetischen Algorithmus kann von Fall zu Fall variieren, aber die allgemeine Struktur ist wie folgt:

1. Wählen Sie eine Anfangspopulation G⊂Γ aus.
2. Wählen Sie zufällig eine der Operationen aus, die in diesem Schritt durchgeführt werden: Crossover oder Mutation.
3. **Crossover**:
   * Wählen Sie zufällig zwei Gene g<sub>1</sub>, g<sub>2</sub> ∈ G aus.
   * Berechnen Sie das Crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>).
   * Wenn fit(g)<fit(g<sub>1</sub>) oder fit(g)<fit(g<sub>2</sub>) - ersetzen Sie das entsprechende Gen in der Population durch g.
4. **Mutation** - wählen Sie ein zufälliges Gen g∈G aus und ersetzen Sie es durch mutate(g).
5. Wiederholen Sie Schritt 2, bis wir einen ausreichend kleinen Wert für fit erhalten oder bis die Grenze für die Anzahl der Schritte erreicht ist.

## Typische Aufgaben

Typische Aufgaben, die durch genetische Algorithmen gelöst werden, umfassen:

1. Terminoptimierung
1. Optimale Verpackung
1. Optimales Schneiden
1. Beschleunigung der exhaustiven Suche

## ✍️ Übungen: Genetische Algorithmen

Setzen Sie Ihr Lernen in den folgenden Notebooks fort:

Gehen Sie zu [diesem Notebook](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb), um zwei Beispiele für die Verwendung genetischer Algorithmen zu sehen:

1. Gerechte Aufteilung von Schätzen
1. 8-Damen-Problem

## Fazit

Genetische Algorithmen werden verwendet, um viele Probleme zu lösen, einschließlich Logistik- und Suchprobleme. Das Feld ist inspiriert von Forschungen, die Themen aus Psychologie und Informatik zusammengeführt haben.

## 🚀 Herausforderung

"Genetische Algorithmen sind einfach zu implementieren, aber ihr Verhalten ist schwer zu verstehen." [Quelle](https://wikipedia.org/wiki/Genetic_algorithm) Machen Sie einige Recherchen, um eine Implementierung eines genetischen Algorithmus zu finden, wie z.B. das Lösen eines Sudoku-Rätsels, und erklären Sie, wie es funktioniert, als Skizze oder Flussdiagramm.

## [Nachvorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Überprüfung & Selbststudium

Sehen Sie sich [dieses großartige Video](https://www.youtube.com/watch?v=qv6UVOQ0F44) an, das darüber spricht, wie Computer lernen können, Super Mario mit Hilfe von neuronalen Netzwerken zu spielen, die durch genetische Algorithmen trainiert wurden. Wir werden mehr darüber lernen, wie Computer Spiele wie dieses spielen [im nächsten Abschnitt](../22-DeepRL/README.md).

## [Aufgabe: Diophantische Gleichung](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Ihr Ziel ist es, die sogenannte **diophantische Gleichung** zu lösen - eine Gleichung mit ganzzahligen Wurzeln. Betrachten Sie zum Beispiel die Gleichung a+2b+3c+4d=30. Sie müssen die ganzzahligen Wurzeln finden, die diese Gleichung erfüllen.

*Diese Aufgabe ist inspiriert von [diesem Beitrag](https://habr.com/post/128704/).*

Hinweise:

1. Sie können die Wurzeln im Intervall [0;30] betrachten.
1. Verwenden Sie als Gen die Liste der Wurzelwerte.

Verwenden Sie [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) als Ausgangspunkt.

**Haftungsausschluss**:  
Dieses Dokument wurde mit Hilfe von maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung resultieren.