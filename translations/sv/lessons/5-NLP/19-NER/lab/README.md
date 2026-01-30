# NER

Labuppgift från [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Uppgift

I denna labb ska du träna en modell för igenkänning av namngivna entiteter (NER) för medicinska termer.

## Datasetet

För att träna en NER-modell behöver vi ett korrekt märkt dataset med medicinska entiteter. [BC5CDR dataset](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) innehåller märkta sjukdoms- och kemikalieentiteter från mer än 1500 artiklar. Du kan ladda ner datasetet efter att ha registrerat dig på deras webbplats.

BC5CDR-datasetet ser ut så här:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

I detta dataset finns artikelns titel och abstrakt på de två första raderna, och därefter individuella entiteter med start- och slutpositioner inom titel+abstrakt-blocket. Förutom entitetstypen får du även ontologi-ID för denna entitet inom en medicinsk ontologi.

Du kommer behöva skriva lite Python-kod för att konvertera detta till BIO-kodning.

## Nätverket

Ett första försök med NER kan göras med hjälp av ett LSTM-nätverk, som i vårt exempel som du har sett under lektionen. Men inom NLP-uppgifter visar [transformer-arkitekturen](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), och specifikt [BERT-språkmodeller](https://en.wikipedia.org/wiki/BERT_(language_model)), mycket bättre resultat. Förtränade BERT-modeller förstår den generella strukturen av ett språk och kan finjusteras för specifika uppgifter med relativt små dataset och beräkningskostnader.

Eftersom vi planerar att tillämpa NER på medicinska scenarier är det logiskt att använda en BERT-modell som är tränad på medicinska texter. Microsoft Research har släppt en förtränad modell som heter [PubMedBERT][PubMedBERT] ([publikation][PubMedBERT-Pub]), som har finjusterats med texter från [PubMed](https://pubmed.ncbi.nlm.nih.gov/) repository.

Den *de facto* standarden för att träna transformer-modeller är biblioteket [Hugging Face Transformers](https://huggingface.co/). Det innehåller också ett arkiv med förtränade modeller som underhålls av communityn, inklusive PubMedBERT. För att ladda och använda denna modell behöver vi bara några få rader kod:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Detta ger oss själva `model`, byggd för tokenklassificeringsuppgifter med `classes` antal klasser, samt `tokenizer`-objektet som kan dela upp inmatad text i tokens. Du kommer behöva konvertera datasetet till BIO-format, med hänsyn till PubMedBERT-tokenisering. Du kan använda [denna bit Python-kod](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) som inspiration.

## Slutsats

Denna uppgift ligger mycket nära den faktiska uppgift du sannolikt kommer att ha om du vill få mer insikter från stora mängder naturliga språktexter. I vårt fall kan vi tillämpa vår tränade modell på [datasetet med COVID-relaterade artiklar](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) och se vilka insikter vi kan få. [Detta blogginlägg](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) och [denna artikel](https://www.mdpi.com/2504-2289/6/1/4) beskriver forskningen som kan göras på denna samling av artiklar med hjälp av NER.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.