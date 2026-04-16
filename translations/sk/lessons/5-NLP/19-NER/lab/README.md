# NER

Laboratórna úloha z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Úloha

V tejto úlohe musíte natrénovať model na rozpoznávanie pomenovaných entít (NER) pre medicínske termíny.

## Dataset

Na natrénovanie NER modelu potrebujeme správne označený dataset s medicínskymi entitami. [BC5CDR dataset](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) obsahuje označené choroby a chemické entity z viac ako 1500 článkov. Dataset si môžete stiahnuť po registrácii na ich webovej stránke.

Dataset BC5CDR vyzerá takto:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

V tomto datasete sú názov článku a abstrakt v prvých dvoch riadkoch, a potom nasledujú jednotlivé entity s počiatočnými a koncovými pozíciami v rámci bloku názov+abstrakt. Okrem typu entity získate aj ID tejto entity v rámci určitej medicínskej ontológie.

Budete musieť napísať nejaký Python kód na konverziu tohto datasetu do BIO kódovania.

## Sieť

Prvý pokus o NER môže byť realizovaný pomocou LSTM siete, ako ste videli v našom príklade počas lekcie. Avšak pri úlohách NLP [transformer architektúra](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), a konkrétne [BERT jazykové modely](https://en.wikipedia.org/wiki/BERT_(language_model)) dosahujú oveľa lepšie výsledky. Predtrénované BERT modely rozumejú všeobecnej štruktúre jazyka a môžu byť doladené pre konkrétne úlohy s relatívne malými datasetmi a nízkymi výpočtovými nákladmi.

Keďže plánujeme aplikovať NER na medicínsky scenár, má zmysel použiť BERT model natrénovaný na medicínskych textoch. Microsoft Research vydal predtrénovaný model nazvaný [PubMedBERT][PubMedBERT] ([publikácia][PubMedBERT-Pub]), ktorý bol doladený pomocou textov z repozitára [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

Štandard pre trénovanie transformer modelov je knižnica [Hugging Face Transformers](https://huggingface.co/). Obsahuje aj repozitár komunitou udržiavaných predtrénovaných modelov, vrátane PubMedBERT. Na načítanie a použitie tohto modelu potrebujeme len pár riadkov kódu:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Týmto získame samotný `model`, ktorý je určený na úlohu klasifikácie tokenov pomocou `classes` počtu tried, ako aj objekt `tokenizer`, ktorý dokáže rozdeliť vstupný text na tokeny. Budete musieť konvertovať dataset do BIO formátu, pričom zohľadníte tokenizáciu PubMedBERT. Môžete použiť [tento kúsok Python kódu](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) ako inšpiráciu.

## Záver

Táto úloha je veľmi blízka skutočnej úlohe, ktorú pravdepodobne budete mať, ak chcete získať viac poznatkov z veľkých objemov textov v prirodzenom jazyku. V našom prípade môžeme aplikovať náš natrénovaný model na [dataset článkov súvisiacich s COVID-om](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) a zistiť, aké poznatky dokážeme získať. [Tento blogový príspevok](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) a [tento článok](https://www.mdpi.com/2504-2289/6/1/4) opisujú výskum, ktorý je možné vykonať na tomto korpuse článkov pomocou NER.

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.