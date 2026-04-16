<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "032bda5068f543d6c1fcb30c34231461",
  "translation_date": "2025-08-31T17:59:24+00:00",
  "source_file": "lessons/5-NLP/19-NER/lab/README.md",
  "language_code": "en"
}
-->
# NER

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

In this lab, your goal is to train a named entity recognition (NER) model for medical terms.

## The Dataset

To train an NER model, we need a properly labeled dataset containing medical entities. The [BC5CDR dataset](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) includes labeled entities for diseases and chemicals extracted from over 1,500 research papers. You can download the dataset after registering on their website.

The BC5CDR dataset is structured as follows:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

In this dataset, the first two lines contain the paper's title and abstract. Following that, individual entities are listed along with their start and end positions within the combined title+abstract text block. Additionally, the dataset provides the entity type and its ontology ID within a specific medical ontology.

You will need to write Python code to convert this dataset into BIO encoding.

## The Network

A first attempt at NER can be made using an LSTM network, as demonstrated in the example from the lesson. However, in NLP tasks, the [transformer architecture](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)), and specifically [BERT language models](https://en.wikipedia.org/wiki/BERT_(language_model)), tend to deliver significantly better results. Pre-trained BERT models already understand the general structure of a language and can be fine-tuned for specific tasks with relatively small datasets and computational resources.

Since we aim to apply NER in a medical context, it is logical to use a BERT model pre-trained on medical texts. Microsoft Research has released a pre-trained model called [PubMedBERT][PubMedBERT] ([publication][PubMedBERT-Pub]), which has been fine-tuned using texts from the [PubMed](https://pubmed.ncbi.nlm.nih.gov/) repository.

The *de facto* standard for training transformer models is the [Hugging Face Transformers](https://huggingface.co/) library. This library also hosts a repository of community-maintained pre-trained models, including PubMedBERT. Loading and using this model requires just a few lines of code:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

This code provides the `model`, designed for token classification tasks with `classes` number of classes, and the `tokenizer` object, which splits input text into tokens. You will need to convert the dataset into BIO format while considering PubMedBERT's tokenization. [This Python code snippet](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) can serve as inspiration.

## Takeaway

This task closely resembles real-world scenarios where you might need to extract insights from large volumes of natural language text. In our case, we can apply the trained model to the [dataset of COVID-related papers](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) to uncover valuable insights. [This blog post](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) and [this paper](https://www.mdpi.com/2504-2289/6/1/4) illustrate the kind of research that can be conducted on such a corpus of papers using NER.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.