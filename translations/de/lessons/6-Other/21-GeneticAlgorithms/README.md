<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "893aa368cb485da704b466a0f3775587",
  "translation_date": "2025-08-24T09:37:52+00:00",
  "source_file": "lessons/6-Other/21-GeneticAlgorithms/README.md",
  "language_code": "de"
}
-->
# Genetische Algorithmen

## [Quiz vor der Vorlesung](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/121)

**Genetische Algorithmen** (GA) basieren auf einem **evolutionären Ansatz** der KI, bei dem Methoden der Evolution einer Population genutzt werden, um eine optimale Lösung für ein gegebenes Problem zu finden. Sie wurden 1975 von [John Henry Holland](https://wikipedia.org/wiki/John_Henry_Holland) vorgeschlagen.

Genetische Algorithmen basieren auf den folgenden Ideen:

* Gültige Lösungen des Problems können als **Gene** dargestellt werden.
* Durch **Crossover** können zwei Lösungen kombiniert werden, um eine neue gültige Lösung zu erhalten.
* **Selektion** wird verwendet, um mithilfe einer **Fitnessfunktion** optimalere Lösungen auszuwählen.
* **Mutationen** werden eingeführt, um die Optimierung zu destabilisieren und aus lokalen Minima herauszukommen.

Wenn Sie einen genetischen Algorithmus implementieren möchten, benötigen Sie Folgendes:

 * Eine Methode, um Problemlösungen mithilfe von **Genen** g∈Γ zu kodieren.
 * Auf der Menge der Gene Γ muss eine **Fitnessfunktion** fit: Γ→**R** definiert werden. Kleinere Funktionswerte entsprechen besseren Lösungen.
 * Einen **Crossover-Mechanismus**, um zwei Gene zu kombinieren und eine neue gültige Lösung zu erhalten: crossover: Γ<sup>2</sub>→Γ.
 * Einen **Mutationsmechanismus**: mutate: Γ→Γ.

In vielen Fällen sind Crossover und Mutation recht einfache Algorithmen, die Gene als numerische Sequenzen oder Bitvektoren manipulieren.

Die spezifische Implementierung eines genetischen Algorithmus kann von Fall zu Fall variieren, aber die allgemeine Struktur ist wie folgt:

1. Wählen Sie eine Anfangspopulation G⊂Γ.
2. Wählen Sie zufällig eine der Operationen aus, die in diesem Schritt ausgeführt werden sollen: Crossover oder Mutation.
3. **Crossover**:
  * Wählen Sie zufällig zwei Gene g<sub>1</sub>, g<sub>2</sub> ∈ G aus.
  * Berechnen Sie den Crossover g=crossover(g<sub>1</sub>,g<sub>2</sub>).
  * Wenn fit(g)<fit(g<sub>1</sub>) oder fit(g)<fit(g<sub>2</sub>), ersetzen Sie das entsprechende Gen in der Population durch g.
4. **Mutation** - Wählen Sie ein zufälliges Gen g∈G aus und ersetzen Sie es durch mutate(g).
5. Wiederholen Sie ab Schritt 2, bis ein ausreichend kleiner Wert von fit erreicht ist oder das Limit der Schrittanzahl erreicht wurde.

## Typische Aufgaben

Typische Aufgaben, die mit genetischen Algorithmen gelöst werden, umfassen:

1. Optimierung von Zeitplänen
1. Optimales Packen
1. Optimales Schneiden
1. Beschleunigung von erschöpfenden Suchverfahren

## ✍️ Übungen: Genetische Algorithmen

Setzen Sie Ihr Lernen in den folgenden Notebooks fort:

Gehen Sie zu [diesem Notebook](../../../../../lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb), um zwei Beispiele für die Verwendung genetischer Algorithmen zu sehen:

1. Gerechte Aufteilung eines Schatzes
1. 8-Damen-Problem

## Fazit

Genetische Algorithmen werden verwendet, um viele Probleme zu lösen, einschließlich Logistik- und Suchprobleme. Das Feld ist inspiriert von Forschung, die Themen aus Psychologie und Informatik miteinander verbindet.

## 🚀 Herausforderung

"Genetische Algorithmen sind einfach zu implementieren, aber ihr Verhalten ist schwer zu verstehen." [Quelle](https://wikipedia.org/wiki/Genetic_algorithm) Recherchieren Sie eine Implementierung eines genetischen Algorithmus, z. B. zur Lösung eines Sudoku-Puzzles, und erklären Sie, wie er funktioniert, in Form einer Skizze oder eines Flussdiagramms.

## [Quiz nach der Vorlesung](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/221)

## Wiederholung & Selbststudium

Sehen Sie sich [dieses großartige Video](https://www.youtube.com/watch?v=qv6UVOQ0F44) an, das zeigt, wie ein Computer lernen kann, Super Mario zu spielen, indem neuronale Netzwerke mit genetischen Algorithmen trainiert werden. Wir werden mehr darüber lernen, wie Computer solche Spiele spielen können [im nächsten Abschnitt](../22-DeepRL/README.md).

## [Aufgabe: Diophantische Gleichung](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb)

Ihr Ziel ist es, die sogenannte **diophantische Gleichung** zu lösen – eine Gleichung mit ganzzahligen Wurzeln. Betrachten Sie zum Beispiel die Gleichung a+2b+3c+4d=30. Sie müssen die ganzzahligen Wurzeln finden, die diese Gleichung erfüllen.

*Diese Aufgabe ist inspiriert von [diesem Beitrag](https://habr.com/post/128704/).*

Hinweise:

1. Sie können Wurzeln im Intervall [0;30] betrachten.
1. Als Gen können Sie die Liste der Wurzelwerte verwenden.

Verwenden Sie [Diophantine.ipynb](../../../../../lessons/6-Other/21-GeneticAlgorithms/Diophantine.ipynb) als Ausgangspunkt.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.