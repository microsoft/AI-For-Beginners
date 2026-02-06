# NER

Labøvelse fra [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Opgave

I denne øvelse skal du træne en model til genkendelse af navngivne enheder (NER) for medicinske termer.

## Datasættet

For at træne en NER-model har vi brug for et korrekt mærket datasæt med medicinske enheder. [BC5CDR-datasættet](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) indeholder mærkede sygdoms- og kemikalieenheder fra mere end 1500 artikler. Du kan downloade datasættet efter registrering på deres hjemmeside.

BC5CDR-datasættet ser sådan ud:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

I dette datasæt er der en artikeloverskrift og et abstrakt på de første to linjer, og derefter er der individuelle enheder med start- og slutpositioner inden for overskrift+abstrakt-blokken. Ud over enhedstypen får du også enhedens ontologi-ID inden for en medicinsk ontologi.

Du skal skrive noget Python-kode for at konvertere dette til BIO-kodning.

## Netværket

Et første forsøg på NER kan udføres ved hjælp af et LSTM-netværk, som i vores eksempel, du har set under lektionen. Men inden for NLP-opgaver viser [transformer-arkitekturen](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) og specifikt [BERT-sproglige modeller](https://en.wikipedia.org/wiki/BERT_(language_model)) langt bedre resultater. Forudtrænede BERT-modeller forstår den generelle struktur af et sprog og kan finjusteres til specifikke opgaver med relativt små datasæt og lave beregningsomkostninger.

Da vi planlægger at anvende NER i en medicinsk kontekst, giver det mening at bruge en BERT-model, der er trænet på medicinske tekster. Microsoft Research har udgivet en forudtrænet model kaldet [PubMedBERT][PubMedBERT] ([publikation][PubMedBERT-Pub]), som er finjusteret ved hjælp af tekster fra [PubMed](https://pubmed.ncbi.nlm.nih.gov/) repository.

Den *de facto* standard for træning af transformer-modeller er [Hugging Face Transformers](https://huggingface.co/) biblioteket. Det indeholder også et repository med fællesskabsvedligeholdte forudtrænede modeller, inklusive PubMedBERT. For at indlæse og bruge denne model skal vi blot bruge et par linjer kode:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Dette giver os selve `model`, bygget til token-klassifikationsopgaver med `classes` antal klasser, samt `tokenizer`-objektet, der kan opdele inputtekst i tokens. Du skal konvertere datasættet til BIO-format og tage PubMedBERT-tokenisering i betragtning. Du kan bruge [denne Python-kode](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) som inspiration.

## Konklusion

Denne opgave ligger meget tæt på den faktiske opgave, du sandsynligvis vil have, hvis du ønsker at få mere indsigt i store mængder af naturlige sproglige tekster. I vores tilfælde kan vi anvende vores trænet model på [datasættet med COVID-relaterede artikler](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) og se, hvilke indsigter vi kan opnå. [Denne blogpost](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) og [denne artikel](https://www.mdpi.com/2504-2289/6/1/4) beskriver den forskning, der kan udføres på dette korpus af artikler ved hjælp af NER.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at opnå nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.