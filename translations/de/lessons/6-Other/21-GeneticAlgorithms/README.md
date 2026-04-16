# Genetische Algorithmen

## [Quiz vor der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/41)

**Genetische Algorithmen** (GA) basieren auf einem **evolutionären Ansatz** der KI, bei dem Methoden der Evolution einer Population genutzt werden, um eine optimale Lösung für ein gegebenes Problem zu finden. Sie wurden 1975 von [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland) vorgeschlagen.

Genetische Algorithmen basieren auf den folgenden Ideen:

* Gültige Lösungen des Problems können als **Gene** dargestellt werden.
* Durch **Crossover** können zwei Lösungen kombiniert werden, um eine neue gültige Lösung zu erhalten.
* **Selektion** wird verwendet, um mithilfe einer **Fitnessfunktion** optimalere Lösungen auszuwählen.
* **Mutationen** werden eingeführt, um die Optimierung zu destabilisieren und uns aus lokalen Minima herauszuführen.

Wenn Sie einen genetischen Algorithmus implementieren möchten, benötigen Sie Folgendes:

* Eine Methode, um Problemlösungen mithilfe von **Genen** g∈Γ zu kodieren.
* Auf der Menge der Gene Γ muss eine **Fitnessfunktion** fit: Γ→**R** definiert werden. Kleinere Funktionswerte entsprechen besseren Lösungen.
* Einen **Crossover-Mechanismus**, um zwei Gene zu kombinieren und eine neue gültige Lösung zu erhalten: crossover: Γ²→Γ.
* Einen **Mutationsmechanismus**: mutate: Γ→Γ.

In vielen Fällen sind Crossover und Mutation recht einfache Algorithmen, die Gene als Zahlenfolgen oder Bitvektoren manipulieren.

Die spezifische Implementierung eines genetischen Algorithmus kann je nach Fall variieren, aber die allgemeine Struktur ist wie folgt:

1. Wählen Sie eine Anfangspopulation G⊆Γ.
2. Wählen Sie zufällig eine der Operationen aus, die in diesem Schritt ausgeführt werden sollen: Crossover oder Mutation.
3. **Crossover**:
   * Wählen Sie zufällig zwei Gene g₁, g₂ ∈ G.
   * Berechnen Sie das Crossover g=crossover(g₁, g₂).
   * Wenn fit(g)<fit(g₁) oder fit(g)<fit(g₂), ersetzen Sie das entsprechende Gen in der Population durch g.
4. **Mutation** - Wählen Sie ein zufälliges Gen g∈G und ersetzen Sie es durch mutate(g).
5. Wiederholen Sie ab Schritt 2, bis ein ausreichend kleiner Wert von fit erreicht ist oder bis das Limit der Schrittanzahl erreicht ist.

## Typische Aufgaben

Aufgaben, die typischerweise mit genetischen Algorithmen gelöst werden, umfassen:

1. Optimierung von Zeitplänen
1. Optimales Packen
1. Optimales Schneiden
1. Beschleunigung von erschöpfenden Suchverfahren

## ✍️ Übungen: Genetische Algorithmen

Setzen Sie Ihr Lernen in den folgenden Notebooks fort:

Gehen Sie zu [diesem Notebook](Genetic.ipynb), um zwei Beispiele für die Verwendung genetischer Algorithmen zu sehen:

1. Gerechte Aufteilung eines Schatzes
1. 8-Damen-Problem

## Fazit

Genetische Algorithmen werden verwendet, um viele Probleme zu lösen, einschließlich Logistik- und Suchprobleme. Dieses Feld ist inspiriert von Forschung, die Themen aus der Psychologie und der Informatik miteinander verbindet.

## 🚀 Herausforderung

"Genetische Algorithmen sind einfach zu implementieren, aber ihr Verhalten ist schwer zu verstehen." [Quelle](https://wikipedia.org/wiki/Genetic_algorithm) Recherchieren Sie eine Implementierung eines genetischen Algorithmus, z. B. zur Lösung eines Sudoku-Puzzles, und erklären Sie, wie er funktioniert, als Skizze oder Flussdiagramm.

## [Quiz nach der Vorlesung](https://ff-quizzes.netlify.app/en/ai/quiz/42)

## Rückblick & Selbststudium

Sehen Sie sich [dieses großartige Video](https://www.youtube.com/watch?v=qv6UVOQ0F44) an, das zeigt, wie ein Computer lernen kann, Super Mario zu spielen, indem neuronale Netzwerke mit genetischen Algorithmen trainiert werden. Wir werden mehr darüber lernen, wie Computer lernen, solche Spiele zu spielen, [im nächsten Abschnitt](../22-DeepRL/README.md).

## [Aufgabe: Diophantische Gleichung](Diophantine.ipynb)

Ihr Ziel ist es, die sogenannte **diophantische Gleichung** zu lösen – eine Gleichung mit ganzzahligen Lösungen. Betrachten Sie zum Beispiel die Gleichung a+2b+3c+4d=30. Sie müssen die ganzzahligen Lösungen finden, die diese Gleichung erfüllen.

*Diese Aufgabe ist inspiriert von [diesem Beitrag](https://habr.com/post/128704/).*

Hinweise:

1. Sie können Lösungen im Intervall [0;30] betrachten.
1. Verwenden Sie als Gen die Liste der Lösungswerte.

Nutzen Sie [Diophantine.ipynb](Diophantine.ipynb) als Ausgangspunkt.

---

