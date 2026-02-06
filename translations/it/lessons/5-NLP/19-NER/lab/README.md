# NER

Compito del laboratorio tratto dal [Curriculum AI for Beginners](https://github.com/microsoft/ai-for-beginners).

## Compito

In questo laboratorio, devi addestrare un modello di riconoscimento di entità nominate (NER) per termini medici.

## Il Dataset

Per addestrare un modello NER, abbiamo bisogno di un dataset etichettato correttamente con entità mediche. Il [dataset BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) contiene entità etichettate di malattie e sostanze chimiche tratte da oltre 1500 articoli. Puoi scaricare il dataset registrandoti sul loro sito web.

Il dataset BC5CDR si presenta così:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

In questo dataset, ci sono il titolo e l'abstract dell'articolo nelle prime due righe, seguiti dalle singole entità con le posizioni di inizio e fine all'interno del blocco titolo+abstract. Oltre al tipo di entità, viene fornito l'ID ontologico di questa entità all'interno di una specifica ontologia medica.

Dovrai scrivere del codice Python per convertire questi dati nel formato BIO.

## La Rete

Un primo tentativo di NER può essere fatto utilizzando una rete LSTM, come nell'esempio che hai visto durante la lezione. Tuttavia, nei compiti di NLP, l'[architettura transformer](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), e in particolare i [modelli linguistici BERT](https://en.wikipedia.org/wiki/BERT_(language_model)), mostrano risultati molto migliori. I modelli BERT pre-addestrati comprendono la struttura generale di una lingua e possono essere ottimizzati per compiti specifici con dataset relativamente piccoli e costi computazionali contenuti.

Poiché intendiamo applicare il NER a uno scenario medico, ha senso utilizzare un modello BERT addestrato su testi medici. Microsoft Research ha rilasciato un modello pre-addestrato chiamato [PubMedBERT][PubMedBERT] ([pubblicazione][PubMedBERT-Pub]), ottimizzato utilizzando testi dal repository [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

Lo standard *de facto* per l'addestramento di modelli transformer è la libreria [Hugging Face Transformers](https://huggingface.co/). Contiene anche un repository di modelli pre-addestrati mantenuti dalla comunità, incluso PubMedBERT. Per caricare e utilizzare questo modello, bastano poche righe di codice:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Questo ci fornisce il `model` stesso, costruito per il compito di classificazione dei token utilizzando un numero di `classes` classi, oltre all'oggetto `tokenizer` che può suddividere il testo di input in token. Dovrai convertire il dataset nel formato BIO, tenendo conto della tokenizzazione di PubMedBERT. Puoi utilizzare [questo frammento di codice Python](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) come ispirazione.

## Conclusione

Questo compito è molto vicino a quello reale che potresti affrontare se desideri ottenere maggiori informazioni da grandi volumi di testi in linguaggio naturale. Nel nostro caso, possiamo applicare il nostro modello addestrato al [dataset di articoli relativi al COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) e vedere quali informazioni possiamo ricavare. [Questo post sul blog](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) e [questo articolo](https://www.mdpi.com/2504-2289/6/1/4) descrivono le ricerche che possono essere condotte su questo corpus di articoli utilizzando il NER.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.