# NER

Laboriülesanne [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) kursusest.

## Ülesanne

Selles laboris tuleb treenida nimelise üksuse tuvastamise (NER) mudelit meditsiiniliste terminite jaoks.

## Andmestik

NER mudeli treenimiseks vajame korrektselt märgistatud andmestikku meditsiiniliste üksustega. [BC5CDR andmestik](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) sisaldab märgistatud haiguste ja kemikaalide üksusi enam kui 1500 artiklist. Andmestiku saab alla laadida pärast registreerimist nende veebilehel.

BC5CDR andmestik näeb välja selline:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Selles andmestikus on artikli pealkiri ja kokkuvõte esimesel kahel real ning seejärel individuaalsed üksused, mille algus- ja lõppasendid on pealkiri+kokkuvõte plokis. Lisaks üksuse tüübile on saadaval ka selle üksuse ontoloogia ID mõnes meditsiinilises ontoloogias.

Peate kirjutama Python koodi, et konverteerida see BIO kodeeringusse.

## Võrgustik

Esimene katse NER-i jaoks võib olla tehtud LSTM-võrgustiku abil, nagu nägite meie näites tunni ajal. Kuid NLP ülesannetes näitavad [transformer arhitektuur](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) ja eriti [BERT keelemudelid](https://en.wikipedia.org/wiki/BERT_(language_model)) palju paremaid tulemusi. Eeltreenitud BERT mudelid mõistavad keele üldist struktuuri ja neid saab kohandada konkreetsete ülesannete jaoks suhteliselt väikeste andmestike ja arvutusressurssidega.

Kuna plaanime rakendada NER-i meditsiinilises kontekstis, on mõistlik kasutada BERT mudelit, mis on treenitud meditsiiniliste tekstide põhjal. Microsoft Research on avaldanud eeltreenitud mudeli nimega [PubMedBERT][PubMedBERT] ([publikatsioon][PubMedBERT-Pub]), mis on kohandatud [PubMed](https://pubmed.ncbi.nlm.nih.gov/) repository tekstide abil.

Transformer mudelite treenimise *de facto* standardiks on [Hugging Face Transformers](https://huggingface.co/) teek. See sisaldab ka kogukonna hallatavaid eeltreenitud mudeleid, sealhulgas PubMedBERT. Selle mudeli laadimiseks ja kasutamiseks on vaja vaid paar rida koodi:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

See annab meile `model` objekti, mis on ehitatud tokenite klassifitseerimise ülesande jaoks, kasutades `classes` klasside arvu, samuti `tokenizer` objekti, mis suudab sisendteksti jagada tokeniteks. Peate konverteerima andmestiku BIO formaati, arvestades PubMedBERT tokeniseerimist. Inspiratsiooniks võite kasutada [seda Python koodi](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88).

## Õppetunnid

See ülesanne on väga lähedane tegelikule ülesandele, millega tõenäoliselt kokku puutute, kui soovite saada rohkem teadmisi suurtest loodusliku keele tekstimahudest. Meie puhul saame rakendada treenitud mudelit [COVID-teemaliste artiklite andmestikule](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) ja vaadata, milliseid teadmisi suudame sealt saada. [See blogipostitus](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) ja [see artikkel](https://www.mdpi.com/2504-2289/6/1/4) kirjeldavad uurimistööd, mida saab teha selle artiklite korpuse põhjal NER-i abil.

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.