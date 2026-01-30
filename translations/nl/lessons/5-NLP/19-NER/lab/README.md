# NER

Labopdracht uit [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Taak

In deze labopdracht moet je een model voor named entity recognition (NER) trainen voor medische termen.

## De Dataset

Om een NER-model te trainen, hebben we een goed gelabelde dataset nodig met medische entiteiten. De [BC5CDR dataset](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) bevat gelabelde ziektes en chemische entiteiten uit meer dan 1500 papers. Je kunt de dataset downloaden nadat je je hebt geregistreerd op hun website.

De BC5CDR dataset ziet er als volgt uit:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

In deze dataset staan de titel en samenvatting van een paper op de eerste twee regels, gevolgd door individuele entiteiten met begin- en eindposities binnen het titel+samenvatting-blok. Naast het type entiteit krijg je ook het ontologie-ID van deze entiteit binnen een medische ontologie.

Je zult wat Python-code moeten schrijven om dit om te zetten naar BIO-encoding.

## Het Netwerk

Een eerste poging tot NER kan worden gedaan met behulp van een LSTM-netwerk, zoals in ons voorbeeld dat je tijdens de les hebt gezien. Echter, bij NLP-taken laten [transformer-architecturen](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), en specifiek [BERT-taalmodellen](https://en.wikipedia.org/wiki/BERT_(language_model)), veel betere resultaten zien. Voorgetrainde BERT-modellen begrijpen de algemene structuur van een taal en kunnen met relatief kleine datasets en lage rekenkosten worden aangepast voor specifieke taken.

Aangezien we van plan zijn NER toe te passen in een medische context, is het logisch om een BERT-model te gebruiken dat is getraind op medische teksten. Microsoft Research heeft een voorgetraind model uitgebracht genaamd [PubMedBERT][PubMedBERT] ([publicatie][PubMedBERT-Pub]), dat is getraind met teksten uit de [PubMed](https://pubmed.ncbi.nlm.nih.gov/) repository.

De *de facto* standaard voor het trainen van transformer-modellen is de [Hugging Face Transformers](https://huggingface.co/) bibliotheek. Deze bevat ook een repository met door de community onderhouden voorgetrainde modellen, waaronder PubMedBERT. Om dit model te laden en te gebruiken, zijn slechts een paar regels code nodig:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Dit geeft ons het `model` zelf, gebouwd voor een token-classificatietaak met `classes` aantal klassen, evenals een `tokenizer` object dat invoertekst in tokens kan splitsen. Je zult de dataset moeten omzetten naar BIO-formaat, rekening houdend met de tokenisatie van PubMedBERT. Je kunt [dit stukje Python-code](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) als inspiratie gebruiken.

## Belangrijkste Leerpunten

Deze taak lijkt sterk op de daadwerkelijke taken die je waarschijnlijk zult tegenkomen als je meer inzichten wilt verkrijgen uit grote hoeveelheden natuurlijke taalteksten. In ons geval kunnen we ons getrainde model toepassen op de [dataset van COVID-gerelateerde papers](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) en zien welke inzichten we kunnen verkrijgen. [Deze blogpost](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) en [dit artikel](https://www.mdpi.com/2504-2289/6/1/4) beschrijven het onderzoek dat kan worden uitgevoerd op deze verzameling papers met behulp van NER.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.