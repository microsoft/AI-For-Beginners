# NER

Laboppgave fra [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Oppgave

I denne labben skal du trene en modell for navngitt enhetsgjenkjenning (NER) for medisinske termer.

## Datasettet

For å trene en NER-modell trenger vi et korrekt merket datasett med medisinske enheter. [BC5CDR-datasettet](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) inneholder merket informasjon om sykdommer og kjemiske enheter fra mer enn 1500 artikler. Du kan laste ned datasettet etter å ha registrert deg på deres nettside.

BC5CDR-datasettet ser slik ut:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

I dette datasettet finner du artikkeltitler og sammendrag i de to første linjene, og deretter individuelle enheter med start- og sluttposisjoner innenfor tittel+sammendrag-blokken. I tillegg til enhetstype får du også ontologi-IDen til denne enheten innenfor en medisinsk ontologi.

Du må skrive noe Python-kode for å konvertere dette til BIO-koding.

## Nettverket

Første forsøk på NER kan gjøres ved å bruke et LSTM-nettverk, som i eksempelet du har sett under leksjonen. Men i NLP-oppgaver viser [transformer-arkitektur](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), og spesielt [BERT-språkmodeller](https://en.wikipedia.org/wiki/BERT_(language_model)), mye bedre resultater. Forhåndstrente BERT-modeller forstår den generelle strukturen i et språk og kan finjusteres for spesifikke oppgaver med relativt små datasett og lave beregningskostnader.

Siden vi planlegger å bruke NER i en medisinsk kontekst, gir det mening å bruke en BERT-modell trent på medisinske tekster. Microsoft Research har gitt ut en forhåndstrent modell kalt [PubMedBERT][PubMedBERT] ([publikasjon][PubMedBERT-Pub]), som ble finjustert ved bruk av tekster fra [PubMed](https://pubmed.ncbi.nlm.nih.gov/) arkivet.

Den *de facto* standarden for trening av transformer-modeller er [Hugging Face Transformers](https://huggingface.co/) biblioteket. Det inneholder også et arkiv med forhåndstrente modeller vedlikeholdt av fellesskapet, inkludert PubMedBERT. For å laste inn og bruke denne modellen trenger vi bare noen få linjer med kode:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Dette gir oss selve `model`, bygget for tokenklassifiseringsoppgaver med `classes` antall klasser, samt `tokenizer`-objektet som kan dele opp inputtekst i tokens. Du må konvertere datasettet til BIO-format, med hensyn til PubMedBERT-tokenisering. Du kan bruke [denne Python-koden](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) som inspirasjon.

## Oppsummering

Denne oppgaven er svært lik den faktiske oppgaven du sannsynligvis vil ha hvis du ønsker å få mer innsikt i store mengder naturlige språktekster. I vårt tilfelle kan vi bruke den trente modellen på [datasettet med COVID-relaterte artikler](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) og se hvilke innsikter vi kan få. [Denne bloggposten](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) og [denne artikkelen](https://www.mdpi.com/2504-2289/6/1/4) beskriver forskningen som kan gjøres på dette korpuset av artikler ved bruk av NER.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.