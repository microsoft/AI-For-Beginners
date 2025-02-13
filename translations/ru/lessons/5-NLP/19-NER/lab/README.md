# NER

Лабораторное задание из [Курса по ИИ для начинающих](https://github.com/microsoft/ai-for-beginners).

## Задача

В этой лабораторной работе вам нужно обучить модель распознавания именованных сущностей для медицинских терминов.

## Датасет

Для обучения модели NER нам нужен правильно размеченный датасет с медицинскими сущностями. [Датасет BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) содержит размеченные сущности заболеваний и химических веществ из более чем 1500 статей. Вы можете скачать датасет после регистрации на их сайте.

Датасет BC5CDR выглядит так:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

В этом датасете первые две строки содержат название статьи и аннотацию, а затем идут отдельные сущности с начальной и конечной позициями в блоке название+аннотация. В дополнение к типу сущности, вы получаете идентификатор онтологии этой сущности в рамках какой-либо медицинской онтологии.

Вам нужно будет написать немного кода на Python, чтобы преобразовать это в кодировку BIO.

## Сеть

Первую попытку распознавания именованных сущностей можно сделать с помощью сети LSTM, как вы видели в нашем примере во время урока. Однако в задачах обработки естественного языка архитектура [трансформеров](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), а конкретно [языковые модели BERT](https://en.wikipedia.org/wiki/BERT_(language_model)), показывают гораздо лучшие результаты. Предобученные модели BERT понимают общую структуру языка и могут быть дообучены для конкретных задач с относительно небольшими наборами данных и вычислительными затратами.

Поскольку мы планируем применять NER в медицинском сценарии, имеет смысл использовать модель BERT, обученную на медицинских текстах. Исследовательская группа Microsoft выпустила предобученную модель под названием [PubMedBERT][PubMedBERT] ([публикация][PubMedBERT-Pub]), которая была дообучена с использованием текстов из репозитория [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

*de facto* стандартом для обучения моделей трансформеров является библиотека [Hugging Face Transformers](https://huggingface.co/). Она также содержит репозиторий предобученных моделей, поддерживаемых сообществом, включая PubMedBERT. Чтобы загрузить и использовать эту модель, нам нужно всего лишь несколько строк кода:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Это дает нам объект `model` itself, built for token classification task using `classes` number of classes, as well as `tokenizer`, который может разбивать входной текст на токены. Вам нужно будет преобразовать датасет в формат BIO, учитывая токенизацию PubMedBERT. Вы можете использовать [этот фрагмент кода на Python](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) в качестве вдохновения.

## Вывод

Эта задача очень близка к той, с которой вам, вероятно, предстоит столкнуться, если вы хотите получить больше информации о больших объемах текстов на естественном языке. В нашем случае мы можем применить нашу обученную модель к [датасету статей, связанных с COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge), и посмотреть, какие выводы мы сможем сделать. [Этот блог-пост](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) и [эта статья](https://www.mdpi.com/2504-2289/6/1/4) описывают исследования, которые можно провести на этом корпусе статей с использованием NER.

**Отказ от ответственности**:  
Этот документ был переведен с использованием машинных AI-сервисов перевода. Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на родном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный человеческий перевод. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникающие в результате использования этого перевода.