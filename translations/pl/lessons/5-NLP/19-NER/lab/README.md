# NER

Zadanie laboratoryjne z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Zadanie

W tym laboratorium musisz wytrenować model rozpoznawania nazwanych jednostek (NER) dla terminów medycznych.

## Zbiór danych

Aby wytrenować model NER, potrzebujemy odpowiednio oznaczonego zbioru danych z jednostkami medycznymi. [Zbiór danych BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) zawiera oznaczone jednostki chorób i substancji chemicznych z ponad 1500 publikacji. Możesz pobrać ten zbiór danych po zarejestrowaniu się na ich stronie internetowej.

Zbiór danych BC5CDR wygląda tak:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

W tym zbiorze danych znajdują się tytuł i abstrakt publikacji w pierwszych dwóch liniach, a następnie poszczególne jednostki z określonymi pozycjami początkowymi i końcowymi w bloku tytuł+abstrakt. Oprócz typu jednostki, otrzymujesz identyfikator ontologii tej jednostki w ramach określonej ontologii medycznej.

Będziesz musiał napisać trochę kodu w Pythonie, aby przekonwertować to na kodowanie BIO.

## Sieć

Pierwsze podejście do NER można zrealizować za pomocą sieci LSTM, jak pokazano w naszym przykładzie podczas lekcji. Jednak w zadaniach NLP [architektura transformera](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), a w szczególności [modele językowe BERT](https://en.wikipedia.org/wiki/BERT_(language_model)), osiągają znacznie lepsze wyniki. Wstępnie wytrenowane modele BERT rozumieją ogólną strukturę języka i mogą być dostosowane do konkretnych zadań przy stosunkowo małych zbiorach danych i niskich kosztach obliczeniowych.

Ponieważ planujemy zastosować NER w scenariuszu medycznym, warto użyć modelu BERT wytrenowanego na tekstach medycznych. Microsoft Research udostępnił wstępnie wytrenowany model o nazwie [PubMedBERT][PubMedBERT] ([publikacja][PubMedBERT-Pub]), który został dostosowany za pomocą tekstów z repozytorium [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

Standardem w trenowaniu modeli transformera jest biblioteka [Hugging Face Transformers](https://huggingface.co/). Zawiera ona również repozytorium modeli wstępnie wytrenowanych przez społeczność, w tym PubMedBERT. Aby załadować i używać tego modelu, wystarczy kilka linijek kodu:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

To daje nam sam `model`, zbudowany do zadania klasyfikacji tokenów przy użyciu `classes` liczby klas, oraz obiekt `tokenizer`, który może dzielić tekst wejściowy na tokeny. Będziesz musiał przekonwertować zbiór danych na format BIO, uwzględniając tokenizację PubMedBERT. Możesz skorzystać z [tego fragmentu kodu w Pythonie](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) jako inspiracji.

## Wnioski

To zadanie jest bardzo zbliżone do rzeczywistego zadania, które możesz mieć, jeśli chcesz uzyskać więcej informacji z dużych ilości tekstów w języku naturalnym. W naszym przypadku możemy zastosować wytrenowany model do [zbioru danych dotyczącego publikacji związanych z COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) i sprawdzić, jakie wnioski uda nam się wyciągnąć. [Ten wpis na blogu](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) oraz [ten artykuł](https://www.mdpi.com/2504-2289/6/1/4) opisują badania, które można przeprowadzić na tym korpusie publikacji za pomocą NER.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.