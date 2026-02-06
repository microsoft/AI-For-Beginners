# NER

Laboratorní úkol z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Úkol

V tomto laboratorním úkolu je vaším cílem natrénovat model rozpoznávání pojmenovaných entit (NER) pro lékařské termíny.

## Dataset

Pro trénování modelu NER potřebujeme správně označený dataset s lékařskými entitami. [Dataset BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) obsahuje označené entity nemocí a chemických látek z více než 1500 článků. Dataset si můžete stáhnout po registraci na jejich webových stránkách.

Dataset BC5CDR vypadá takto:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

V tomto datasetu jsou v prvních dvou řádcích uvedeny názvy článků a abstrakty, a poté následují jednotlivé entity s počátečními a koncovými pozicemi v bloku názvu+abstraktu. Kromě typu entity získáte také ID této entity v rámci určité lékařské ontologie.

Budete muset napsat nějaký Python kód, který dataset převede do BIO kódování.

## Síť

První pokus o NER lze provést pomocí LSTM sítě, jak jste viděli v našem příkladu během lekce. Nicméně u úloh zpracování přirozeného jazyka (NLP) [transformerová architektura](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), a konkrétně [BERT jazykové modely](https://en.wikipedia.org/wiki/BERT_(language_model)), poskytují mnohem lepší výsledky. Předtrénované BERT modely rozumí obecné struktuře jazyka a mohou být doladěny pro specifické úlohy s relativně malými datovými sadami a nízkými výpočetními náklady.

Vzhledem k tomu, že plánujeme aplikovat NER na lékařský scénář, má smysl použít BERT model natrénovaný na lékařských textech. Microsoft Research vydal předtrénovaný model nazvaný [PubMedBERT][PubMedBERT] ([publikace][PubMedBERT-Pub]), který byl doladěn pomocí textů z repozitáře [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

Standardem pro trénování transformerových modelů je knihovna [Hugging Face Transformers](https://huggingface.co/). Obsahuje také repozitář komunitně spravovaných předtrénovaných modelů, včetně PubMedBERT. Pro načtení a použití tohoto modelu stačí jen pár řádků kódu:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Tím získáme samotný `model`, vytvořený pro úlohu klasifikace tokenů s použitím `classes` počtu tříd, a také objekt `tokenizer`, který dokáže rozdělit vstupní text na tokeny. Budete muset dataset převést do BIO formátu, přičemž vezmete v úvahu tokenizaci PubMedBERT. Jako inspiraci můžete použít [tento kousek Python kódu](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88).

## Závěr

Tento úkol je velmi blízký skutečné práci, kterou pravděpodobně budete mít, pokud chcete získat více poznatků z velkých objemů textů v přirozeném jazyce. V našem případě můžeme aplikovat náš natrénovaný model na [dataset článků souvisejících s COVIDem](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) a zjistit, jaké poznatky budeme schopni získat. [Tento blogový příspěvek](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) a [tento článek](https://www.mdpi.com/2504-2289/6/1/4) popisují výzkum, který lze provést na tomto korpusu článků pomocí NER.

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.