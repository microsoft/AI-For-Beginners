# Benannte Entitätenerkennung

Bis jetzt haben wir uns hauptsächlich auf eine NLP-Aufgabe - Klassifikation - konzentriert. Es gibt jedoch auch andere NLP-Aufgaben, die mit neuronalen Netzwerken durchgeführt werden können. Eine dieser Aufgaben ist die **[Benannte Entitätenerkennung](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), die sich mit der Erkennung spezifischer Entitäten innerhalb von Texten befasst, wie z.B. Orte, Personennamen, Zeiträume, chemische Formeln und so weiter.

## [Vorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## Beispiel für die Verwendung von NER

Angenommen, Sie möchten einen Chatbot für natürliche Sprache entwickeln, ähnlich wie Amazon Alexa oder Google Assistant. Die Funktionsweise intelligenter Chatbots besteht darin, zu *verstehen*, was der Benutzer möchte, indem sie eine Textklassifikation auf dem eingegebenen Satz durchführen. Das Ergebnis dieser Klassifikation ist die sogenannte **Intention**, die bestimmt, was ein Chatbot tun sollte.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Bild vom Autor

Ein Benutzer kann jedoch einige Parameter als Teil des Satzes angeben. Wenn sie beispielsweise nach dem Wetter fragt, kann sie einen Ort oder ein Datum angeben. Ein Bot sollte in der Lage sein, diese Entitäten zu verstehen und die Parameter entsprechend auszufüllen, bevor er die Aktion ausführt. Genau hier kommt NER ins Spiel.

> ✅ Ein weiteres Beispiel wäre [die Analyse wissenschaftlicher medizinischer Arbeiten](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Eine der Hauptsachen, auf die wir achten müssen, sind spezifische medizinische Begriffe, wie Krankheiten und medizinische Substanzen. Während eine kleine Anzahl von Krankheiten wahrscheinlich mit Substring-Suche extrahiert werden kann, erfordern komplexere Entitäten, wie chemische Verbindungen und Medikamentennamen, einen komplexeren Ansatz.

## NER als Token-Klassifikation

NER-Modelle sind im Wesentlichen **Token-Klassifikationsmodelle**, da wir für jedes der Eingabetokens entscheiden müssen, ob es zu einer Entität gehört oder nicht, und wenn ja - zu welcher Entitätsklasse.

Betrachten Sie den folgenden Titel einer Arbeit:

**Trikuspidalklappeninsuffizienz** und **Lithiumcarbonat** **Toxizität** bei einem Neugeborenen.

Die Entitäten hier sind:

* Trikuspidalklappeninsuffizienz ist eine Krankheit (`DIS`)
* Lithiumcarbonat ist eine chemische Substanz (`CHEM`)
* Toxizität ist ebenfalls eine Krankheit (`DIS`)

Beachten Sie, dass eine Entität mehrere Tokens umfassen kann. Und, wie in diesem Fall, müssen wir zwischen zwei aufeinanderfolgenden Entitäten unterscheiden. Daher ist es üblich, zwei Klassen für jede Entität zu verwenden - eine, die das erste Token der Entität angibt (häufig wird das `B-`-Präfix verwendet, für **b**eginning), und eine andere - die Fortsetzung einer Entität (`I-`, für **i**nner token). Wir verwenden auch `O` als Klasse, um alle **o**ther Tokens darzustellen. Solches Token-Tagging wird als [BIO-Tagging](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (oder IOB) bezeichnet. Wenn wir unseren Titel taggen, sieht er folgendermaßen aus:

Token | Tag
------|-----
Trikuspidal | B-DIS
klappe | I-DIS
insuffizienz | I-DIS
und | O
lithium | B-CHEM
carbonat | I-CHEM
toxizität | B-DIS
bei | O
einem | O
neugeborenen | O
. | O

Da wir eine Eins-zu-eins-Zuordnung zwischen Tokens und Klassen herstellen müssen, können wir ein rechtsseitiges **viele-zu-viele** neuronales Netzwerkmodell aus diesem Bild trainieren:

![Bild zeigt gängige Muster wiederkehrender neuronaler Netzwerke.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.de.jpg)

> *Bild aus [diesem Blogbeitrag](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) von [Andrej Karpathy](http://karpathy.github.io/). NER-Token-Klassifikationsmodelle entsprechen der ganz rechts stehenden Netzwerkarchitektur in diesem Bild.*

## Training von NER-Modellen

Da ein NER-Modell im Wesentlichen ein Token-Klassifikationsmodell ist, können wir RNNs verwenden, mit denen wir bereits vertraut sind. In diesem Fall gibt jeder Block des rekurrenten Netzwerks die Token-ID zurück. Das folgende Beispiel-Notebook zeigt, wie man LSTM für die Token-Klassifikation trainiert.

## ✍️ Beispiel-Notebooks: NER

Setzen Sie Ihr Lernen im folgenden Notebook fort:

* [NER mit TensorFlow](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Fazit

Ein NER-Modell ist ein **Token-Klassifikationsmodell**, was bedeutet, dass es zur Durchführung der Token-Klassifikation verwendet werden kann. Dies ist eine sehr gängige Aufgabe im NLP, die hilft, spezifische Entitäten innerhalb von Texten zu erkennen, einschließlich Orte, Namen, Daten und mehr.

## 🚀 Herausforderung

Schließen Sie die unten verlinkte Aufgabe ab, um ein Modell zur Benannten Entitätenerkennung für medizinische Begriffe zu trainieren, und testen Sie es dann an einem anderen Datensatz.

## [Nachvorlesungsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Überprüfung & Selbststudium

Lesen Sie den Blog [Die unangemessene Effektivität von rekurrenten neuronalen Netzwerken](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) und folgen Sie dem Abschnitt Weiterführende Literatur in diesem Artikel, um Ihr Wissen zu vertiefen.

## [Aufgabe](lab/README.md)

In der Aufgabe für diese Lektion müssen Sie ein Modell zur Erkennung medizinischer Entitäten trainieren. Sie können mit dem Training eines LSTM-Modells beginnen, wie in dieser Lektion beschrieben, und dann das BERT-Transformator-Modell verwenden. Lesen Sie [die Anweisungen](lab/README.md), um alle Details zu erhalten.

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.