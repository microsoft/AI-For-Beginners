# NER

Laboraufgabe aus dem [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Aufgabe

In diesem Labor müssen Sie ein Modell zur Erkennung benannter Entitäten (NER) für medizinische Begriffe trainieren.

## Der Datensatz

Um ein NER-Modell zu trainieren, benötigen wir einen korrekt gekennzeichneten Datensatz mit medizinischen Entitäten. Der [BC5CDR-Datensatz](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) enthält gekennzeichnete Krankheits- und Chemikalienentitäten aus mehr als 1500 wissenschaftlichen Artikeln. Sie können den Datensatz nach der Registrierung auf deren Website herunterladen.

Der BC5CDR-Datensatz sieht wie folgt aus:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

In diesem Datensatz befinden sich der Titel und die Zusammenfassung des Artikels in den ersten beiden Zeilen, gefolgt von den einzelnen Entitäten mit Anfangs- und Endpositionen innerhalb des Titel+Zusammenfassungsblocks. Zusätzlich zur Entitätstyp erhalten Sie die Ontologie-ID dieser Entität innerhalb einer medizinischen Ontologie.

Sie müssen etwas Python-Code schreiben, um dies in BIO-Codierung umzuwandeln.

## Das Netzwerk

Ein erster Versuch mit NER kann mit einem LSTM-Netzwerk durchgeführt werden, wie Sie es in unserem Beispiel während der Lektion gesehen haben. Allerdings zeigen bei NLP-Aufgaben die [Transformer-Architektur](https://de.wikipedia.org/wiki/Transformer_(machine_learning_model)) und speziell [BERT-Sprachmodelle](https://de.wikipedia.org/wiki/BERT_(language_model)) deutlich bessere Ergebnisse. Vorgefertigte BERT-Modelle verstehen die allgemeine Struktur einer Sprache und können mit relativ kleinen Datensätzen und geringem Rechenaufwand für spezifische Aufgaben feinabgestimmt werden.

Da wir planen, NER in einem medizinischen Szenario anzuwenden, macht es Sinn, ein BERT-Modell zu verwenden, das auf medizinischen Texten trainiert wurde. Microsoft Research hat ein vortrainiertes Modell namens [PubMedBERT][PubMedBERT] ([Publikation][PubMedBERT-Pub]) veröffentlicht, das mit Texten aus dem [PubMed](https://pubmed.ncbi.nlm.nih.gov/) Repository feinabgestimmt wurde.

Der *de facto* Standard für das Training von Transformer-Modellen ist die [Hugging Face Transformers](https://huggingface.co/) Bibliothek. Sie enthält auch ein Repository mit von der Community gepflegten vortrainierten Modellen, einschließlich PubMedBERT. Um dieses Modell zu laden und zu verwenden, benötigen wir nur ein paar Zeilen Code:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Dies liefert uns das `model` selbst, das für die Token-Klassifikationsaufgabe mit `classes` Anzahl von Klassen gebaut wurde, sowie das `tokenizer`-Objekt, das den Eingabetext in Tokens aufteilen kann. Sie müssen den Datensatz in BIO-Format umwandeln und dabei die Tokenisierung von PubMedBERT berücksichtigen. Sie können [dieses Stück Python-Code](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) als Inspiration verwenden.

## Fazit

Diese Aufgabe ist der tatsächlichen Arbeit sehr nahe, die Sie wahrscheinlich durchführen werden, wenn Sie tiefere Einblicke in große Mengen an natürlichen Sprachtexten gewinnen möchten. In unserem Fall können wir unser trainiertes Modell auf den [Datensatz von COVID-bezogenen Artikeln](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) anwenden und sehen, welche Erkenntnisse wir daraus gewinnen können. [Dieser Blogbeitrag](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) und [dieses Paper](https://www.mdpi.com/2504-2289/6/1/4) beschreiben die Forschung, die mit diesem Korpus von Artikeln unter Verwendung von NER durchgeführt werden kann.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.