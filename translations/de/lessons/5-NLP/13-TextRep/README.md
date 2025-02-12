# Text als Tensoren darstellen

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Textklassifikation

Im ersten Teil dieses Abschnitts konzentrieren wir uns auf die Aufgabe der **Textklassifikation**. Wir verwenden den [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset) Datensatz, der Nachrichtenartikel wie die folgenden enthält:

* Kategorie: Sci/Tech
* Titel: Ky. Unternehmen gewinnt Zuschuss zur Untersuchung von Peptiden (AP)
* Text: AP - Ein Unternehmen, das von einem Chemieforscher an der Universität von Louisville gegründet wurde, hat einen Zuschuss erhalten, um...

Unser Ziel wird es sein, den Nachrichtenartikel basierend auf dem Text in eine der Kategorien einzuordnen.

## Text darstellen

Wenn wir Aufgaben der Verarbeitung natürlicher Sprache (NLP) mit neuronalen Netzwerken lösen wollen, benötigen wir eine Möglichkeit, Text als Tensoren darzustellen. Computer stellen bereits textuelle Zeichen als Zahlen dar, die auf Schriftarten auf Ihrem Bildschirm mithilfe von Kodierungen wie ASCII oder UTF-8 abgebildet werden.

<img alt="Bild, das ein Diagramm zeigt, das ein Zeichen einer ASCII- und binären Darstellung zuordnet" src="images/ascii-character-map.png" width="50%"/>

> [Bildquelle](https://www.seobility.net/en/wiki/ASCII)

Als Menschen verstehen wir, was jeder Buchstabe **darstellt**, und wie alle Zeichen zusammenkommen, um die Wörter eines Satzes zu bilden. Computer hingegen haben ein solches Verständnis nicht, und neuronale Netzwerke müssen die Bedeutung während des Trainings lernen.

Daher können wir verschiedene Ansätze zur Darstellung von Text verwenden:

* **Zeichenebene Darstellung**, bei der wir Text darstellen, indem wir jedes Zeichen als eine Zahl behandeln. Angenommen, wir haben *C* verschiedene Zeichen in unserem Textkorpus, würde das Wort *Hallo* durch einen 5x*C* Tensor dargestellt. Jeder Buchstabe würde einer Tensor-Spalte in der One-Hot-Kodierung entsprechen.
* **Wortebene Darstellung**, bei der wir ein **Wörterbuch** aller Wörter in unserem Text erstellen und dann Wörter mithilfe von One-Hot-Kodierung darstellen. Dieser Ansatz ist in gewisser Weise besser, da jeder Buchstabe für sich genommen nicht viel Bedeutung hat, und indem wir somit höherwertige semantische Konzepte - Wörter - verwenden, vereinfachen wir die Aufgabe für das neuronale Netzwerk. Aufgrund der großen Wörterbuchgröße müssen wir jedoch mit hochdimensionalen spärlichen Tensoren umgehen.

Unabhängig von der Darstellung müssen wir den Text zunächst in eine Sequenz von **Tokens** umwandeln, wobei ein Token entweder ein Zeichen, ein Wort oder manchmal sogar ein Teil eines Wortes ist. Dann wandeln wir das Token in eine Zahl um, typischerweise unter Verwendung eines **Wörterbuchs**, und diese Zahl kann über One-Hot-Kodierung in ein neuronales Netzwerk eingespeist werden.

## N-Gramme

In der natürlichen Sprache kann die genaue Bedeutung von Wörtern nur im Kontext bestimmt werden. Zum Beispiel sind die Bedeutungen von *neuronales Netzwerk* und *Fischernetz* völlig unterschiedlich. Eine Möglichkeit, dies zu berücksichtigen, besteht darin, unser Modell auf Wortpaaren aufzubauen und Wortpaare als separate Wörterbuch-Token zu betrachten. Auf diese Weise wird der Satz *Ich gehe gerne angeln* durch die folgende Token-Sequenz dargestellt: *Ich gehe*, *gehe gerne*, *gerne angeln*. Das Problem mit diesem Ansatz ist, dass die Wörterbuchgröße erheblich wächst und Kombinationen wie *gehe angeln* und *gehe einkaufen* durch unterschiedliche Tokens dargestellt werden, die trotz des gleichen Verbs keine semantische Ähnlichkeit aufweisen.

In einigen Fällen können wir auch Tri-Gramme - Kombinationen von drei Wörtern - in Betracht ziehen. Daher wird dieser Ansatz oft als **n-Gramme** bezeichnet. Es macht auch Sinn, n-Gramme mit der Zeichenebene Darstellung zu verwenden, wobei n-Gramme grob unterschiedlichen Silben entsprechen.

## Bag-of-Words und TF/IDF

Bei der Lösung von Aufgaben wie der Textklassifikation müssen wir in der Lage sein, Text durch einen festgelegten Vektor fester Größe darzustellen, den wir als Eingabe für den abschließenden dichten Klassifizierer verwenden. Eine der einfachsten Möglichkeiten, dies zu tun, besteht darin, alle individuellen Wortdarstellungen zu kombinieren, z.B. indem wir sie addieren. Wenn wir die One-Hot-Kodierungen jedes Wortes addieren, erhalten wir einen Vektor von Frequenzen, der zeigt, wie oft jedes Wort im Text erscheint. Eine solche Textdarstellung wird als **Bag of Words** (BoW) bezeichnet.

<img src="images/bow.png" width="90%"/>

> Bild vom Autor

Ein BoW stellt im Wesentlichen dar, welche Wörter im Text erscheinen und in welchen Mengen, was tatsächlich ein guter Hinweis darauf sein kann, worum es im Text geht. Zum Beispiel enthält ein Nachrichtenartikel über Politik wahrscheinlich Wörter wie *Präsident* und *Land*, während eine wissenschaftliche Publikation etwas wie *Collider*, *entdeckt* usw. enthalten würde. Daher können Wortfrequenzen in vielen Fällen ein guter Indikator für den Textinhalt sein.

Das Problem mit BoW ist, dass bestimmte häufige Wörter, wie *und*, *ist* usw., in den meisten Texten erscheinen und die höchsten Frequenzen aufweisen, wodurch die Wörter, die wirklich wichtig sind, in den Hintergrund gedrängt werden. Wir können die Bedeutung dieser Wörter verringern, indem wir die Häufigkeit berücksichtigen, mit der Wörter in der gesamten Dokumentensammlung auftreten. Dies ist die Hauptidee hinter dem TF/IDF-Ansatz, der in den Notebooks, die zu dieser Lektion gehören, detaillierter behandelt wird.

Allerdings können keine dieser Ansätze die **Semantik** des Textes vollständig berücksichtigen. Wir benötigen leistungsfähigere Modelle neuronaler Netzwerke, um dies zu tun, was wir später in diesem Abschnitt besprechen werden.

## ✍️ Übungen: Textdarstellung

Setzen Sie Ihr Lernen in den folgenden Notebooks fort:

* [Textdarstellung mit PyTorch](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb)
* [Textdarstellung mit TensorFlow](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)

## Fazit

Bis jetzt haben wir Techniken untersucht, die Frequenzgewichtungen für verschiedene Wörter hinzufügen können. Sie sind jedoch nicht in der Lage, Bedeutung oder Reihenfolge darzustellen. Wie der berühmte Linguist J. R. Firth 1935 sagte: "Die vollständige Bedeutung eines Wortes ist immer kontextabhängig, und kein Studium der Bedeutung, das vom Kontext getrennt ist, kann ernst genommen werden." Wir werden später im Kurs lernen, wie man kontextuelle Informationen aus Text mithilfe von Sprachmodellen erfasst.

## 🚀 Herausforderung

Versuchen Sie einige andere Übungen mit Bag-of-Words und verschiedenen Datenmodellen. Sie könnten inspiriert werden von diesem [Wettbewerb auf Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words)

## [Nach dem Vortrag Quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Überprüfung & Selbststudium

Üben Sie Ihre Fähigkeiten mit Text-Embeddings und Bag-of-Words-Techniken auf [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Aufgabe: Notebooks](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.