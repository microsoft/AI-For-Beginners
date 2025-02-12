# NER

Laborationsuppgift från [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Uppgift

I denna laboration behöver du träna en modell för namngiven entitetsigenkänning för medicinska termer.

## Datasetet

För att träna NER-modellen behöver vi ett korrekt märkt dataset med medicinska entiteter. [BC5CDR dataset](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) innehåller märkta sjukdomar och kemiska entiteter från mer än 1500 artiklar. Du kan ladda ner datasetet efter att ha registrerat dig på deras webbplats.

BC5CDR Dataset ser ut så här:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

I detta dataset finns artikeltitel och abstrakt i de två första raderna, och sedan finns individuella entiteter, med start- och slutpositioner inom titel+abstrakt blocket. Förutom entitetstyp får du ontologin ID för denna entitet inom en viss medicinsk ontologi.

Du behöver skriva lite Python-kod för att konvertera detta till BIO-encoding.

## Nätverket

Första försöket med NER kan göras genom att använda LSTM-nätverk, som i vårt exempel som du har sett under lektionen. Men i NLP-uppgifter visar [transformerarkitektur](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), och specifikt [BERT-språkmodeller](https://en.wikipedia.org/wiki/BERT_(language_model)), mycket bättre resultat. Förtränade BERT-modeller förstår den allmänna strukturen i ett språk och kan finjusteras för specifika uppgifter med relativt små dataset och beräkningskostnader.

Eftersom vi planerar att tillämpa NER på medicinska scenarier, är det logiskt att använda BERT-modellen som är tränad på medicinska texter. Microsoft Research har släppt en förtränad modell som kallas [PubMedBERT][PubMedBERT] ([publicering][PubMedBERT-Pub]), som har finjusterats med texter från [PubMed](https://pubmed.ncbi.nlm.nih.gov/) arkivet.

Den *de facto* standarden för att träna transformer-modeller är [Hugging Face Transformers](https://huggingface.co/) biblioteket. Det innehåller också ett arkiv med gemenskapsunderhållna förtränade modeller, inklusive PubMedBERT. För att ladda och använda denna modell behöver vi bara ett par rader kod:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Detta ger oss `model` itself, built for token classification task using `classes` number of classes, as well as `tokenizer` objektet som kan dela upp inmatningstexten i tokens. Du behöver konvertera datasetet till BIO-format, med hänsyn till PubMedBERT-tokenisering. Du kan använda [denna bit av Python-kod](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) som inspiration.

## Sammanfattning

Denna uppgift ligger mycket nära den faktiska uppgift du sannolikt kommer att ha om du vill få mer insikter i stora volymer av texter på naturligt språk. I vårt fall kan vi tillämpa vår tränade modell på [datasetet med COVID-relaterade artiklar](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) och se vilka insikter vi kommer att kunna få. [Detta blogginlägg](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) och [denna artikel](https://www.mdpi.com/2504-2289/6/1/4) beskriver forskningen som kan göras på detta corpus av artiklar med hjälp av NER.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller inkonsekvenser. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.