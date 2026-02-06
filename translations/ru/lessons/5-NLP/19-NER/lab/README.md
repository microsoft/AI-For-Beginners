# NER

Лабораторная работа из [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Задача

В этой лабораторной работе вам нужно обучить модель распознавания именованных сущностей (NER) для медицинских терминов.

## Датасет

Для обучения модели NER нам нужен правильно размеченный датасет с медицинскими сущностями. [Датасет BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) содержит размеченные сущности заболеваний и химических веществ из более чем 1500 научных статей. Вы можете скачать этот датасет после регистрации на их сайте.

Датасет BC5CDR выглядит следующим образом:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

В этом датасете заголовок статьи и аннотация находятся в первых двух строках, а затем идут отдельные сущности с указанием начальной и конечной позиции в блоке заголовок+аннотация. Помимо типа сущности, предоставляется идентификатор онтологии этой сущности в рамках некоторой медицинской онтологии.

Вам нужно будет написать код на Python, чтобы преобразовать этот датасет в BIO-формат.

## Сеть

Первую попытку создания модели NER можно сделать с использованием сети LSTM, как в примере, который вы видели на уроке. Однако в задачах обработки естественного языка [архитектура трансформеров](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), и особенно [языковые модели BERT](https://en.wikipedia.org/wiki/BERT_(language_model)), показывают гораздо лучшие результаты. Предобученные модели BERT понимают общую структуру языка и могут быть дообучены для конкретных задач с относительно небольшими датасетами и вычислительными затратами.

Поскольку мы планируем применять NER в медицинском сценарии, имеет смысл использовать модель BERT, обученную на медицинских текстах. Исследовательский отдел Microsoft выпустил предобученную модель под названием [PubMedBERT][PubMedBERT] ([публикация][PubMedBERT-Pub]), которая была дообучена на текстах из репозитория [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

Стандартом де-факто для обучения моделей трансформеров является библиотека [Hugging Face Transformers](https://huggingface.co/). Она также содержит репозиторий предобученных моделей, поддерживаемых сообществом, включая PubMedBERT. Чтобы загрузить и использовать эту модель, нам нужно всего несколько строк кода:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Это дает нам сам `model`, построенный для задачи классификации токенов с использованием `classes` количества классов, а также объект `tokenizer`, который может разбивать входной текст на токены. Вам нужно будет преобразовать датасет в BIO-формат, учитывая токенизацию PubMedBERT. Вы можете использовать [этот пример кода на Python](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) в качестве вдохновения.

## Итог

Эта задача очень близка к реальной задаче, с которой вы, вероятно, столкнетесь, если захотите получить больше информации из больших объемов текстов на естественном языке. В нашем случае мы можем применить обученную модель к [датасету статей, связанных с COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) и посмотреть, какие выводы мы сможем сделать. [Этот пост в блоге](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) и [эта статья](https://www.mdpi.com/2504-2289/6/1/4) описывают исследования, которые можно провести на этом корпусе статей с использованием NER.

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Хотя мы стремимся к точности, пожалуйста, учитывайте, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.