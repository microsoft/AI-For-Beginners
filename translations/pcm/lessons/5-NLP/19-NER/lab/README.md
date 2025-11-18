<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "032bda5068f543d6c1fcb30c34231461",
  "translation_date": "2025-11-18T18:40:45+00:00",
  "source_file": "lessons/5-NLP/19-NER/lab/README.md",
  "language_code": "pcm"
}
-->
# NER

Lab Assignment wey come from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

For dis lab, you go train named entity recognition model wey go sabi medical terms.

## The Dataset

To train NER model, we need dataset wey dem don label well well with medical entities. [BC5CDR dataset](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) get labeled diseases and chemicals entities wey dem collect from more than 1500 papers. You fit download di dataset after you register for dia website.

BC5CDR Dataset dey look like dis:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

For dis dataset, di first two lines na di paper title and abstract, and after dat, you go see di individual entities, with di beginning and end positions inside di title+abstract block. Apart from di entity type, you go also get di ontology ID of di entity inside one medical ontology.

You go need write Python code wey go convert dis into BIO encoding.

## The Network

Di first try for NER fit use LSTM network, like di example wey you don see for di lesson. But for NLP tasks, [transformer architecture](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), and especially [BERT language models](https://en.wikipedia.org/wiki/BERT_(language_model)) dey show better results. Pre-trained BERT models sabi di general structure of language, and dem fit fine-tune am for specific tasks with small datasets and low computational costs.

Since we wan use NER for medical scenario, e make sense to use BERT model wey dem don train with medical texts. Microsoft Research don release one pre-trained model wey dem call [PubMedBERT][PubMedBERT] ([publication][PubMedBERT-Pub]), wey dem fine-tune using texts from [PubMed](https://pubmed.ncbi.nlm.nih.gov/) repository.

Di *de facto* standard for training transformer models na [Hugging Face Transformers](https://huggingface.co/) library. E also get repository of community-maintained pre-trained models, including PubMedBERT. To load and use dis model, you just need small lines of code:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Dis go give us di `model` itself, wey dem build for token classification task using `classes` number of classes, plus di `tokenizer` object wey fit split input text into tokens. You go need convert di dataset into BIO format, make e follow PubMedBERT tokenization. You fit use [dis Python code](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) as inspiration.

## Takeaway

Dis task dey very close to di kind task wey you fit get if you wan sabi more about large volumes of natural language texts. For our case, we fit use di trained model for [dataset of COVID-related papers](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) and see wetin we fit learn. [Dis blog post](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) and [dis paper](https://www.mdpi.com/2504-2289/6/1/4) dey describe di research wey fit happen on dis corpus of papers using NER.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even though we dey try make am accurate, abeg make you sabi say automatik transleshion fit get mistake or no dey 100% correct. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important informashon, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong meaning wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->