# NER

Лабораторно упражнение от [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Задача

В това упражнение трябва да обучите модел за разпознаване на именувани обекти (NER) за медицински термини.

## Датасетът

За да обучим NER модел, ни е необходим правилно етикетиран датасет с медицински обекти. [BC5CDR датасетът](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) съдържа етикетирани заболявания и химически обекти от над 1500 статии. Можете да изтеглите датасета след регистрация на техния уебсайт.

BC5CDR датасетът изглежда така:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

В този датасет заглавието и резюмето на статията са в първите два реда, а след това са изброени индивидуалните обекти с начални и крайни позиции в блока заглавие+резюме. Освен типа на обекта, получавате и онтологичния ID на този обект в рамките на някоя медицинска онтология.

Ще трябва да напишете малко Python код, за да го конвертирате в BIO кодиране.

## Мрежата

Първият опит за NER може да бъде направен с помощта на LSTM мрежа, както в примера, който видяхте по време на урока. Въпреки това, при задачи в областта на обработката на естествен език (NLP), [архитектурата на трансформър](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), и по-специално [BERT езиковите модели](https://en.wikipedia.org/wiki/BERT_(language_model)), показват много по-добри резултати. Предварително обучените BERT модели разбират общата структура на езика и могат да бъдат донастроени за специфични задачи с относително малки датасети и ниски изчислителни разходи.

Тъй като планираме да приложим NER в медицински сценарий, има смисъл да използваме BERT модел, обучен върху медицински текстове. Microsoft Research пусна предварително обучен модел, наречен [PubMedBERT][PubMedBERT] ([публикация][PubMedBERT-Pub]), който е донастроен с текстове от хранилището [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

Стандартът *de facto* за обучение на трансформър модели е библиотеката [Hugging Face Transformers](https://huggingface.co/). Тя също така съдържа хранилище с предварително обучени модели, поддържани от общността, включително PubMedBERT. За да заредим и използваме този модел, са ни нужни само няколко реда код:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Това ни дава самия `model`, създаден за задача за класификация на токени с използване на `classes` брой класове, както и обект `tokenizer`, който може да разделя входния текст на токени. Ще трябва да конвертирате датасета в BIO формат, като вземете предвид токенизацията на PubMedBERT. Можете да използвате [този Python код](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) като вдъхновение.

## Изводи

Тази задача е много близка до реалната задача, която вероятно ще имате, ако искате да получите повече прозрения от големи обеми текстове на естествен език. В нашия случай можем да приложим обучен модел към [датасет от статии, свързани с COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) и да видим какви прозрения можем да извлечем. [Тази публикация в блог](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) и [тази статия](https://www.mdpi.com/2504-2289/6/1/4) описват изследванията, които могат да бъдат направени върху този корпус от статии с помощта на NER.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.