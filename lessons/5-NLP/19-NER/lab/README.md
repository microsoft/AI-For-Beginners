# NER

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

In this lab, you need to train named entity recognition model for medical terms.

## The Dataset

To train NER model, we need properly labeled dataset with medical entities. [BC5CDR dataset](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) contains labeled diseases and chemicals entities from more than 1500 papers. You may download the dataset after registering at their web site.

BC5CDR Dataset looks like this:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

In this dataset, there are paper title and abstract in the first two lines, and then there are individual entities, with beginning and end positions within title+abstract block. In addition to entity type, you get the ontology ID of this entity within some medical ontology.

You will need to write some Python code to convert this into BIO encoding.

## The Network

First attempt at NER can be done by using LSTM network, as in our example you have seen during the lesson. However, in NLP tasks, [transformer architecture](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), and specifically [BERT language models](https://en.wikipedia.org/wiki/BERT_(language_model)) show much better results. Pre-trained BERT models understand the general structure of a language, and can be fine-tuned for specific tasks with relatively small datasets and computational costs.

Since we are planning to apply NER to medical scenario, it makes sense to use BERT model trained on medical texts. Microsoft Research has released a pre-trained a model called [PubMedBERT][PubMedBERT] ([publication][PubMedBERT-Pub]), which was fine-tuned using texts from [PubMed](https://pubmed.ncbi.nlm.nih.gov/) repository.

The *de facto* standard for training transformer models is [Hugging Face Transformers](https://huggingface.co/) library. It also contains a repository of community-maintained pre-trained models, including PubMedBERT. To load and use this model, we just need a couple of lines of code:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

This gives us the `model` itself, built for token classification task using `classes` number of classes, as well as `tokenizer` object that can split input text into tokens. You will need to convert the dataset into BIO format, taking PubMedBERT tokenization into account. You can use [this bit of Python code](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) as an inspiration.

## Takeaway

This task is very close to the actual task you are likely go have if you want to gain more insights into large volumes on natural language texts. In our case, we can apply our trained model to the [dataset of COVID-related papers](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) and see which insights we will be able to get. [This blog post](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) and [this paper](https://www.mdpi.com/2504-2289/6/1/4) describe the research the can be done on this corpus of papers using NER.
