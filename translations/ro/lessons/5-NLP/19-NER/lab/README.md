# NER

Temă de laborator din [Curriculum AI pentru Începători](https://github.com/microsoft/ai-for-beginners).

## Sarcina

În acest laborator, trebuie să antrenezi un model de recunoaștere a entităților numite (NER) pentru termeni medicali.

## Setul de date

Pentru a antrena un model NER, avem nevoie de un set de date etichetat corespunzător cu entități medicale. [Setul de date BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) conține entități etichetate de boli și substanțe chimice din peste 1500 de lucrări. Poți descărca setul de date după ce te înregistrezi pe site-ul lor.

Setul de date BC5CDR arată astfel:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

În acest set de date, titlul și rezumatul lucrării sunt în primele două linii, iar apoi urmează entitățile individuale, cu pozițiile de început și sfârșit în cadrul blocului titlu+rezumat. În plus față de tipul entității, primești ID-ul ontologic al acestei entități în cadrul unei ontologii medicale.

Va trebui să scrii ceva cod Python pentru a converti acest set de date în format BIO.

## Rețeaua

Prima încercare de NER poate fi realizată folosind o rețea LSTM, așa cum ai văzut în exemplul din lecție. Totuși, în sarcinile NLP, [arhitectura transformer](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), și în special [modelele de limbaj BERT](https://en.wikipedia.org/wiki/BERT_(language_model)) oferă rezultate mult mai bune. Modelele BERT pre-antrenate înțeleg structura generală a unei limbi și pot fi ajustate pentru sarcini specifice cu seturi de date relativ mici și costuri computaționale reduse.

Deoarece intenționăm să aplicăm NER într-un scenariu medical, are sens să utilizăm un model BERT antrenat pe texte medicale. Microsoft Research a lansat un model pre-antrenat numit [PubMedBERT][PubMedBERT] ([publicație][PubMedBERT-Pub]), care a fost ajustat folosind texte din depozitul [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

Standardul *de facto* pentru antrenarea modelelor transformer este biblioteca [Hugging Face Transformers](https://huggingface.co/). Aceasta conține și un depozit de modele pre-antrenate întreținute de comunitate, inclusiv PubMedBERT. Pentru a încărca și utiliza acest model, avem nevoie doar de câteva linii de cod:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Aceasta ne oferă `model`-ul propriu-zis, construit pentru sarcina de clasificare a tokenilor folosind `classes` numărul de clase, precum și obiectul `tokenizer` care poate împărți textul de intrare în tokeni. Va trebui să convertești setul de date în format BIO, ținând cont de tokenizarea PubMedBERT. Poți folosi [acest fragment de cod Python](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) ca inspirație.

## Concluzie

Această sarcină este foarte apropiată de sarcina reală pe care este probabil să o ai dacă dorești să obții mai multe informații din volume mari de texte în limbaj natural. În cazul nostru, putem aplica modelul antrenat pe [setul de date al lucrărilor legate de COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) și să vedem ce informații putem obține. [Această postare pe blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) și [acest articol](https://www.mdpi.com/2504-2289/6/1/4) descriu cercetările care pot fi realizate pe acest corpus de lucrări folosind NER.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.