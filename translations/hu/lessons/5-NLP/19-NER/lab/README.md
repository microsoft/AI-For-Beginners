# NER

Laboratóriumi feladat az [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) anyagából.

## Feladat

Ebben a laborban egy névfelismerő modellt kell betanítanod orvosi kifejezésekre.

## Az Adathalmaz

Ahhoz, hogy NER modellt tudjunk tanítani, megfelelően címkézett adathalmazra van szükségünk, amely tartalmazza az orvosi entitásokat. A [BC5CDR adathalmaz](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) több mint 1500 tudományos cikkből származó, betegségeket és vegyi anyagokat tartalmazó címkézett entitásokat foglal magában. Az adathalmaz letöltéséhez regisztrálnod kell a weboldalukon.

A BC5CDR adathalmaz így néz ki:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Ebben az adathalmazban az első két sor a cikk címe és absztraktja, majd az egyes entitások következnek, amelyek kezdő- és végpozícióját a cím+absztrakt blokkban adják meg. Az entitás típusán kívül megkapod az adott entitás ontológiai azonosítóját is egy orvosi ontológiában.

Python kódot kell írnod, hogy ezt az adathalmazt BIO kódolású formátumba alakítsd.

## A Hálózat

Az első próbálkozás a NER modellre egy LSTM hálózat használata lehet, ahogy az órán látott példában is szerepelt. Azonban az NLP feladatokban a [transformer architektúra](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), különösen a [BERT nyelvi modellek](https://en.wikipedia.org/wiki/BERT_(language_model)) sokkal jobb eredményeket mutatnak. Az előre betanított BERT modellek megértik a nyelv általános szerkezetét, és viszonylag kis adathalmazokkal és számítási költségekkel finomhangolhatók specifikus feladatokra.

Mivel az NER modellt orvosi környezetben szeretnénk alkalmazni, érdemes olyan BERT modellt használni, amelyet orvosi szövegeken tanítottak be. A Microsoft Research kiadott egy előre betanított modellt, amelyet [PubMedBERT][PubMedBERT]-nek neveznek ([publikáció][PubMedBERT-Pub]), és amelyet a [PubMed](https://pubmed.ncbi.nlm.nih.gov/) adattár szövegein finomhangoltak.

A *de facto* szabvány a transformer modellek tanítására a [Hugging Face Transformers](https://huggingface.co/) könyvtár. Ez a könyvtár egy közösség által karbantartott előre betanított modellek gyűjteményét is tartalmazza, beleértve a PubMedBERT-et. A modell betöltéséhez és használatához mindössze néhány sor kódra van szükség:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Ez biztosítja számunkra a `model` objektumot, amelyet tokenosztályozási feladatra építettek `classes` számú osztállyal, valamint a `tokenizer` objektumot, amely a bemeneti szöveget tokenekre bontja. Az adathalmazt BIO formátumba kell konvertálnod, figyelembe véve a PubMedBERT tokenizálását. [Ez a Python kódrészlet](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) inspirációként szolgálhat.

## Összegzés

Ez a feladat nagyon közel áll ahhoz, amit valószínűleg el kell végezned, ha nagy mennyiségű természetes nyelvű szöveg elemzésével szeretnél mélyebb betekintést nyerni. A mi esetünkben a betanított modellt alkalmazhatjuk a [COVID-hoz kapcsolódó cikkek adathalmazára](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge), és megnézhetjük, milyen következtetéseket tudunk levonni. [Ez a blogbejegyzés](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) és [ez a tanulmány](https://www.mdpi.com/2504-2289/6/1/4) bemutatja, milyen kutatásokat lehet végezni ezen a cikkgyűjteményen NER segítségével.

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.