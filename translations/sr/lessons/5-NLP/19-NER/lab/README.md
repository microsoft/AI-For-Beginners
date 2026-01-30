# NER

Задатак из лабораторијске вежбе у оквиру [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Задатак

У овој лабораторијској вежби, потребно је да обучите модел за препознавање именованих ентитета (NER) за медицинске термине.

## Скуп података

За обуку NER модела, потребан је правилно означен скуп података са медицинским ентитетима. [BC5CDR скуп података](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) садржи означене ентитете болести и хемикалија из више од 1500 научних радова. Можете преузети овај скуп података након регистрације на њиховом сајту.

BC5CDR скуп података изгледа овако:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

У овом скупу података, на прве две линије налазе се наслов и апстракт рада, а затим следе појединачни ентитети са почетним и завршним позицијама унутар блока наслов+апстракт. Поред типа ентитета, добијате и онтолошки ID тог ентитета унутар неке медицинске онтологије.

Потребно је да напишете Python код који ће овај скуп података конвертовати у BIO кодирање.

## Мрежа

Први покушај за NER може се урадити коришћењем LSTM мреже, као у примеру који сте видели током предавања. Међутим, у задацима обраде природног језика, [трансформер архитектура](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), а посебно [BERT језички модели](https://en.wikipedia.org/wiki/BERT_(language_model)) показују много боље резултате. Унапред обучени BERT модели разумеју општу структуру језика и могу се додатно обучити за специфичне задатке уз релативно мале скупове података и рачунарске ресурсе.

Пошто планирамо да применимо NER у медицинском сценарију, логично је користити BERT модел обучен на медицинским текстовима. Microsoft Research је објавио унапред обучени модел под називом [PubMedBERT][PubMedBERT] ([публикација][PubMedBERT-Pub]), који је додатно обучен коришћењем текстова из [PubMed](https://pubmed.ncbi.nlm.nih.gov/) репозиторијума.

Де факто стандард за обуку трансформер модела је библиотека [Hugging Face Transformers](https://huggingface.co/). Она такође садржи репозиторијум унапред обучених модела које одржава заједница, укључујући PubMedBERT. Да бисмо учитали и користили овај модел, потребно је само неколико линија кода:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Ово нам даје сам `model`, направљен за задатак класификације токена користећи `classes` број класа, као и `tokenizer` објекат који може да подели улазни текст на токене. Потребно је да конвертујете скуп података у BIO формат, узимајући у обзир PubMedBERT токенизацију. Можете користити [овај Python код](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) као инспирацију.

## Закључак

Овај задатак је веома сличан стварним задацима које ћете вероватно имати ако желите да стекнете дубљи увид у велике количине текстова на природном језику. У нашем случају, можемо применити наш обучени модел на [скуп података о радовима везаним за COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) и видети које увиде можемо добити. [Овај блог пост](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) и [овај рад](https://www.mdpi.com/2504-2289/6/1/4) описују истраживања која се могу спровести на овом корпусу радова користећи NER.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.