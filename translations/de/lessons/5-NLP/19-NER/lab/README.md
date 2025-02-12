# NER

Laboraufgabe aus dem [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Aufgabe

In diesem Labor müssen Sie ein Modell zur Erkennung benannter Entitäten für medizinische Begriffe trainieren.

## Der Datensatz

Um das NER-Modell zu trainieren, benötigen wir einen richtig beschrifteten Datensatz mit medizinischen Entitäten. Der [BC5CDR-Datensatz](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) enthält beschriftete Krankheiten und chemische Entitäten aus mehr als 1500 Arbeiten. Sie können den Datensatz herunterladen, nachdem Sie sich auf ihrer Website registriert haben.

Der BC5CDR-Datensatz sieht folgendermaßen aus:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

In diesem Datensatz befinden sich der Titel und die Zusammenfassung der Arbeit in den ersten beiden Zeilen, gefolgt von einzelnen Entitäten mit Anfangs- und Endpositionen im Titel+Zusammenfassungsblock. Zusätzlich zum Entitätstyp erhalten Sie die Ontologie-ID dieser Entität innerhalb einer medizinischen Ontologie.

Sie müssen einige Python-Codes schreiben, um dies in BIO-Codierung umzuwandeln.

## Das Netzwerk

Der erste Versuch zur NER kann unter Verwendung eines LSTM-Netzwerks erfolgen, wie in unserem Beispiel, das Sie während der Lektion gesehen haben. In NLP-Aufgaben zeigen jedoch [Transformator-Architekturen](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) und insbesondere [BERT-Sprachmodelle](https://en.wikipedia.org/wiki/BERT_(language_model)) deutlich bessere Ergebnisse. Vorgefertigte BERT-Modelle verstehen die allgemeine Struktur einer Sprache und können mit relativ kleinen Datensätzen und geringen Rechenkosten für spezifische Aufgaben feinabgestimmt werden.

Da wir planen, NER im medizinischen Szenario anzuwenden, ist es sinnvoll, ein BERT-Modell zu verwenden, das auf medizinischen Texten trainiert wurde. Microsoft Research hat ein vortrainiertes Modell namens [PubMedBERT][PubMedBERT] ([Veröffentlichung][PubMedBERT-Pub]) veröffentlicht, das mithilfe von Texten aus dem [PubMed](https://pubmed.ncbi.nlm.nih.gov/) Repository feinabgestimmt wurde.

Der *de facto* Standard für das Training von Transformator-Modellen ist die [Hugging Face Transformers](https://huggingface.co/) Bibliothek. Sie enthält auch ein Repository von von der Community gewarteten vortrainierten Modellen, einschließlich PubMedBERT. Um dieses Modell zu laden und zu verwenden, benötigen wir nur ein paar Zeilen Code:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Dies gibt uns das `model` itself, built for token classification task using `classes` number of classes, as well as `tokenizer`-Objekt, das den Eingabetext in Tokens aufteilen kann. Sie müssen den Datensatz in das BIO-Format umwandeln und dabei die Tokenisierung von PubMedBERT berücksichtigen. Sie können [diesen Python-Code](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) als Inspiration verwenden.

## Fazit

Diese Aufgabe ist sehr nah an der tatsächlichen Aufgabe, die Sie wahrscheinlich haben werden, wenn Sie mehr Einblicke in große Mengen an Texten in natürlicher Sprache gewinnen möchten. In unserem Fall können wir unser trainiertes Modell auf den [Datensatz von COVID-bezogenen Arbeiten](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) anwenden und sehen, welche Erkenntnisse wir gewinnen können. [Dieser Blogbeitrag](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) und [dieses Papier](https://www.mdpi.com/2504-2289/6/1/4) beschreiben die Forschung, die an diesem Korpus von Arbeiten unter Verwendung von NER durchgeführt werden kann.

**Haftungsausschluss**:  
Dieses Dokument wurde mit Hilfe von KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Originalsprache sollte als maßgebliche Quelle betrachtet werden. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.