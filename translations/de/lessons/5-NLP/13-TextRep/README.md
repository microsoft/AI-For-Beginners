<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4522e22e150be0845e03aa41209a39d5",
  "translation_date": "2025-08-24T09:31:28+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "de"
}
-->
# Darstellung von Text als Tensoren

## [Quiz vor der Vorlesung](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Textklassifikation

Im ersten Teil dieses Abschnitts konzentrieren wir uns auf die Aufgabe der **Textklassifikation**. Wir verwenden das [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset)-Datenset, das Nachrichtenartikel wie den folgenden enthält:

* Kategorie: Wissenschaft/Technik  
* Titel: Ky. Unternehmen erhält Zuschuss zur Erforschung von Peptiden (AP)  
* Inhalt: AP - Ein Unternehmen, das von einem Chemieforscher der Universität von Louisville gegründet wurde, erhielt einen Zuschuss zur Entwicklung...

Unser Ziel wird es sein, die Nachricht basierend auf dem Text einer der Kategorien zuzuordnen.

## Darstellung von Text

Wenn wir Aufgaben der natürlichen Sprachverarbeitung (NLP) mit neuronalen Netzwerken lösen wollen, benötigen wir eine Methode, um Text als Tensoren darzustellen. Computer stellen Zeichen bereits als Zahlen dar, die mithilfe von Codierungen wie ASCII oder UTF-8 auf die Schriftarten auf Ihrem Bildschirm abgebildet werden.

<img alt="Bild zeigt ein Diagramm, das ein Zeichen einer ASCII- und binären Darstellung zuordnet" src="images/ascii-character-map.png" width="50%"/>

> [Bildquelle](https://www.seobility.net/en/wiki/ASCII)

Als Menschen verstehen wir, was jeder Buchstabe **repräsentiert** und wie alle Zeichen zusammenkommen, um die Wörter eines Satzes zu bilden. Computer hingegen haben von sich aus kein solches Verständnis, und ein neuronales Netzwerk muss die Bedeutung während des Trainings lernen.

Daher können wir verschiedene Ansätze verwenden, um Text darzustellen:

* **Zeichenbasierte Darstellung**, bei der wir Text darstellen, indem wir jedes Zeichen als Zahl behandeln. Angenommen, wir haben *C* verschiedene Zeichen in unserem Textkorpus, dann würde das Wort *Hello* durch einen 5x*C*-Tensor dargestellt. Jedes Zeichen würde einer Spalte im Tensor in One-Hot-Codierung entsprechen.  
* **Wortbasierte Darstellung**, bei der wir ein **Vokabular** aller Wörter in unserem Text erstellen und dann Wörter mithilfe von One-Hot-Codierung darstellen. Dieser Ansatz ist in gewisser Weise besser, da jedes Zeichen für sich genommen nicht viel Bedeutung hat. Durch die Verwendung höherer semantischer Konzepte – Wörter – vereinfachen wir die Aufgabe für das neuronale Netzwerk. Aufgrund der großen Wörterbuchgröße müssen wir jedoch mit hochdimensionalen, spärlichen Tensoren umgehen.

Unabhängig von der Darstellung müssen wir den Text zunächst in eine Sequenz von **Tokens** umwandeln, wobei ein Token entweder ein Zeichen, ein Wort oder manchmal sogar ein Teil eines Wortes ist. Anschließend konvertieren wir das Token in eine Zahl, typischerweise mithilfe eines **Vokabulars**, und diese Zahl kann mithilfe von One-Hot-Codierung in ein neuronales Netzwerk eingespeist werden.

## N-Gramme

In der natürlichen Sprache kann die genaue Bedeutung von Wörtern nur im Kontext bestimmt werden. Zum Beispiel haben *neuronales Netzwerk* und *Fischernetz* völlig unterschiedliche Bedeutungen. Eine Möglichkeit, dies zu berücksichtigen, besteht darin, unser Modell auf Wortpaaren aufzubauen und Wortpaare als separate Vokabular-Tokens zu betrachten. Auf diese Weise wird der Satz *Ich gehe gerne angeln* durch die folgende Sequenz von Tokens dargestellt: *Ich gehe*, *gehe gerne*, *gerne angeln*. Das Problem bei diesem Ansatz ist, dass die Wörterbuchgröße erheblich wächst und Kombinationen wie *gerne angeln* und *gerne einkaufen* durch unterschiedliche Tokens dargestellt werden, die trotz des gleichen Verbs keine semantische Ähnlichkeit teilen.

In einigen Fällen können wir auch Tri-Gramme – Kombinationen aus drei Wörtern – in Betracht ziehen. Daher wird dieser Ansatz oft als **n-Gramme** bezeichnet. Es macht auch Sinn, n-Gramme mit zeichenbasierter Darstellung zu verwenden, wobei n-Gramme in diesem Fall grob verschiedenen Silben entsprechen.

## Bag-of-Words und TF/IDF

Bei Aufgaben wie der Textklassifikation müssen wir in der Lage sein, Text durch einen festen Vektor darzustellen, den wir als Eingabe für den abschließenden dichten Klassifikator verwenden. Eine der einfachsten Möglichkeiten, dies zu tun, besteht darin, alle einzelnen Wortdarstellungen zu kombinieren, z. B. indem wir sie addieren. Wenn wir die One-Hot-Codierungen jedes Wortes addieren, erhalten wir einen Frequenzvektor, der zeigt, wie oft jedes Wort im Text vorkommt. Eine solche Darstellung von Text wird als **Bag-of-Words** (BoW) bezeichnet.

<img src="images/bow.png" width="90%"/>

> Bild vom Autor

Ein BoW zeigt im Wesentlichen, welche Wörter im Text vorkommen und in welchen Mengen, was tatsächlich ein guter Hinweis darauf sein kann, worum es im Text geht. Ein Nachrichtenartikel über Politik enthält beispielsweise wahrscheinlich Wörter wie *Präsident* und *Land*, während eine wissenschaftliche Veröffentlichung Begriffe wie *Kollider*, *entdeckt* usw. enthalten könnte. Daher können Wortfrequenzen in vielen Fällen ein guter Indikator für den Textinhalt sein.

Das Problem bei BoW ist, dass bestimmte häufige Wörter wie *und*, *ist* usw. in den meisten Texten vorkommen und die höchsten Frequenzen aufweisen, wodurch die wirklich wichtigen Wörter in den Hintergrund treten. Wir können die Bedeutung dieser Wörter verringern, indem wir die Häufigkeit berücksichtigen, mit der Wörter in der gesamten Dokumentensammlung vorkommen. Dies ist die Hauptidee hinter dem TF/IDF-Ansatz, der in den zu dieser Lektion gehörenden Notebooks ausführlicher behandelt wird.

Allerdings können keine dieser Ansätze die **Semantik** des Textes vollständig berücksichtigen. Dafür benötigen wir leistungsstärkere neuronale Netzwerkmodelle, die wir später in diesem Abschnitt besprechen werden.

## ✍️ Übungen: Textdarstellung

Setzen Sie Ihr Lernen in den folgenden Notebooks fort:

* [Textdarstellung mit PyTorch](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb)  
* [Textdarstellung mit TensorFlow](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)

## Fazit

Bisher haben wir Techniken untersucht, die Frequenzgewichte für verschiedene Wörter hinzufügen können. Sie sind jedoch nicht in der Lage, Bedeutung oder Reihenfolge darzustellen. Wie der berühmte Linguist J. R. Firth 1935 sagte: "Die vollständige Bedeutung eines Wortes ist immer kontextabhängig, und keine Untersuchung der Bedeutung ohne Kontext kann ernst genommen werden." Später im Kurs werden wir lernen, wie man kontextuelle Informationen aus Text mithilfe von Sprachmodellen erfasst.

## 🚀 Herausforderung

Probieren Sie einige andere Übungen mit Bag-of-Words und verschiedenen Datenmodellen aus. Vielleicht inspiriert Sie dieser [Wettbewerb auf Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words).

## [Quiz nach der Vorlesung](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Wiederholung & Selbststudium

Üben Sie Ihre Fähigkeiten mit Text-Embeddings und Bag-of-Words-Techniken auf [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste).

## [Aufgabe: Notebooks](assignment.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.