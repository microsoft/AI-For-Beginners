# NER

Лабораторна робота з [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Завдання

У цій лабораторній роботі вам потрібно навчити модель розпізнавання іменованих сутностей (NER) для медичних термінів.

## Набір даних

Для навчання моделі NER нам потрібен правильно розмічений набір даних із медичними сутностями. [Набір даних BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) містить розмічені сутності хвороб і хімічних речовин з понад 1500 наукових статей. Ви можете завантажити цей набір даних після реєстрації на їхньому вебсайті.

Набір даних BC5CDR виглядає так:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

У цьому наборі даних перші два рядки містять заголовок статті та анотацію, а далі йдуть окремі сутності з початковими та кінцевими позиціями в межах блоку "заголовок+анотація". Окрім типу сутності, ви отримуєте ідентифікатор онтології цієї сутності в межах певної медичної онтології.

Вам потрібно буде написати трохи коду на Python, щоб перетворити ці дані у формат BIO.

## Мережа

Першу спробу створення NER можна зробити за допомогою мережі LSTM, як у прикладі, який ви бачили під час уроку. Однак у завданнях обробки природної мови [архітектура трансформерів](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), а особливо [мовні моделі BERT](https://en.wikipedia.org/wiki/BERT_(language_model)), демонструють набагато кращі результати. Попередньо навчені моделі BERT розуміють загальну структуру мови і можуть бути донавчені для конкретних завдань з відносно невеликими наборами даних і обчислювальними витратами.

Оскільки ми плануємо застосовувати NER у медичному контексті, логічно використовувати модель BERT, навчану на медичних текстах. Дослідницький підрозділ Microsoft випустив попередньо навчену модель під назвою [PubMedBERT][PubMedBERT] ([публікація][PubMedBERT-Pub]), яка була донавчена на текстах із репозиторію [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

Де-факто стандартом для навчання моделей трансформерів є бібліотека [Hugging Face Transformers](https://huggingface.co/). Вона також містить репозиторій попередньо навчених моделей, підтримуваних спільнотою, включаючи PubMedBERT. Щоб завантажити та використовувати цю модель, нам потрібно лише кілька рядків коду:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Це надає нам саму `model`, побудовану для завдання класифікації токенів із використанням `classes` кількості класів, а також об'єкт `tokenizer`, який може розбивати вхідний текст на токени. Вам потрібно буде перетворити набір даних у формат BIO, враховуючи токенізацію PubMedBERT. Ви можете використати [цей фрагмент коду на Python](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) як натхнення.

## Висновок

Це завдання дуже близьке до реальних завдань, які вам, ймовірно, доведеться виконувати, якщо ви хочете отримати більше знань із великих обсягів текстів природною мовою. У нашому випадку ми можемо застосувати нашу навчану модель до [набору даних статей, пов’язаних із COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge), і подивитися, які висновки ми зможемо отримати. [Цей блог](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) і [ця стаття](https://www.mdpi.com/2504-2289/6/1/4) описують дослідження, які можна провести на цьому корпусі статей за допомогою NER.

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, зверніть увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критичної інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.