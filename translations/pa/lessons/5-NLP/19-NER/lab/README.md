# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) ਤੋਂ ਲੈਬ ਅਸਾਈਨਮੈਂਟ।

## ਟਾਸਕ

ਇਸ ਲੈਬ ਵਿੱਚ, ਤੁਹਾਨੂੰ ਮੈਡੀਕਲ ਸ਼ਬਦਾਵਲੀ ਲਈ named entity recognition ਮਾਡਲ ਨੂੰ ਟ੍ਰੇਨ ਕਰਨਾ ਹੈ।

## ਡੇਟਾਸੈਟ

NER ਮਾਡਲ ਨੂੰ ਟ੍ਰੇਨ ਕਰਨ ਲਈ, ਸਾਨੂੰ ਮੈਡੀਕਲ ਐਂਟਿਟੀਜ਼ ਨਾਲ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਲੇਬਲ ਕੀਤਾ ਹੋਇਆ ਡੇਟਾਸੈਟ ਚਾਹੀਦਾ ਹੈ। [BC5CDR ਡੇਟਾਸੈਟ](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) ਵਿੱਚ 1500 ਤੋਂ ਵੱਧ ਪੇਪਰਾਂ ਵਿੱਚੋਂ ਲੇਬਲ ਕੀਤੀਆਂ ਬਿਮਾਰੀਆਂ ਅਤੇ ਰਸਾਇਣਕ ਐਂਟਿਟੀਜ਼ ਸ਼ਾਮਲ ਹਨ। ਤੁਸੀਂ ਉਨ੍ਹਾਂ ਦੀ ਵੈਬਸਾਈਟ 'ਤੇ ਰਜਿਸਟਰ ਕਰਨ ਤੋਂ ਬਾਅਦ ਡੇਟਾਸੈਟ ਡਾਊਨਲੋਡ ਕਰ ਸਕਦੇ ਹੋ।

BC5CDR ਡੇਟਾਸੈਟ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖਦਾ ਹੈ:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

ਇਸ ਡੇਟਾਸੈਟ ਵਿੱਚ, ਪਹਿਲੀਆਂ ਦੋ ਲਾਈਨਾਂ ਵਿੱਚ ਪੇਪਰ ਦਾ ਸਿਰਲੇਖ ਅਤੇ ਸਾਰ ਹੈ, ਅਤੇ ਫਿਰ ਵਿਅਕਤੀਗਤ ਐਂਟਿਟੀਜ਼ ਹਨ, ਜਿਨ੍ਹਾਂ ਦੇ ਸਿਰਲੇਖ+ਸਾਰ ਬਲਾਕ ਵਿੱਚ ਸ਼ੁਰੂ ਅਤੇ ਅੰਤ ਦੇ ਸਥਾਨ ਦਿੱਤੇ ਗਏ ਹਨ। ਐਂਟਿਟੀ ਦੀ ਕਿਸਮ ਦੇ ਇਲਾਵਾ, ਤੁਹਾਨੂੰ ਇਸ ਐਂਟਿਟੀ ਦਾ ਓਂਟੋਲੋਜੀ ID ਵੀ ਮਿਲਦਾ ਹੈ ਜੋ ਕਿਸੇ ਮੈਡੀਕਲ ਓਂਟੋਲੋਜੀ ਵਿੱਚ ਹੈ।

ਤੁਹਾਨੂੰ ਇਸਨੂੰ BIO ਐਨਕੋਡਿੰਗ ਵਿੱਚ ਕਨਵਰਟ ਕਰਨ ਲਈ ਕੁਝ Python ਕੋਡ ਲਿਖਣ ਦੀ ਲੋੜ ਹੋਵੇਗੀ।

## ਨੈਟਵਰਕ

NER ਲਈ ਪਹਿਲੀ ਕੋਸ਼ਿਸ਼ LSTM ਨੈਟਵਰਕ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤੀ ਜਾ ਸਕਦੀ ਹੈ, ਜਿਵੇਂ ਕਿ ਤੁਸੀਂ ਪਾਠ ਦੌਰਾਨ ਉਦਾਹਰਣ ਵਿੱਚ ਵੇਖਿਆ। ਹਾਲਾਂਕਿ, NLP ਟਾਸਕਾਂ ਵਿੱਚ, [ਟ੍ਰਾਂਸਫਾਰਮਰ ਆਰਕੀਟੈਕਚਰ](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) ਅਤੇ ਖਾਸ ਕਰਕੇ [BERT ਭਾਸ਼ਾ ਮਾਡਲ](https://en.wikipedia.org/wiki/BERT_(language_model)) ਬਹੁਤ ਹੀ ਵਧੀਆ ਨਤੀਜੇ ਦਿਖਾਉਂਦੇ ਹਨ। ਪ੍ਰੀ-ਟ੍ਰੇਨ ਕੀਤੇ BERT ਮਾਡਲ ਭਾਸ਼ਾ ਦੀ ਆਮ ਰਚਨਾ ਨੂੰ ਸਮਝਦੇ ਹਨ ਅਤੇ ਛੋਟੇ ਡੇਟਾਸੈਟ ਅਤੇ ਘੱਟ ਗਣਨਾਤਮਕ ਖਰਚਿਆਂ ਨਾਲ ਖਾਸ ਟਾਸਕਾਂ ਲਈ ਫਾਈਨ-ਟਿਊਨ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ।

ਕਿਉਂਕਿ ਅਸੀਂ ਮੈਡੀਕਲ ਸਥਿਤੀ ਵਿੱਚ NER ਲਾਗੂ ਕਰਨ ਦੀ ਯੋਜਨਾ ਬਣਾ ਰਹੇ ਹਾਂ, ਇਸ ਲਈ ਮੈਡੀਕਲ ਟੈਕਸਟਾਂ 'ਤੇ ਟ੍ਰੇਨ ਕੀਤੇ BERT ਮਾਡਲ ਦੀ ਵਰਤੋਂ ਕਰਨਾ ਸਹੀ ਹੈ। Microsoft Research ਨੇ ਇੱਕ ਪ੍ਰੀ-ਟ੍ਰੇਨ ਮਾਡਲ ਜਾਰੀ ਕੀਤਾ ਹੈ ਜਿਸਨੂੰ [PubMedBERT][PubMedBERT] ([ਪ੍ਰਕਾਸ਼ਨ][PubMedBERT-Pub]) ਕਿਹਾ ਜਾਂਦਾ ਹੈ, ਜੋ ਕਿ [PubMed](https://pubmed.ncbi.nlm.nih.gov/) ਰਿਪੋਜ਼ਟਰੀ ਦੇ ਟੈਕਸਟਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਫਾਈਨ-ਟਿਊਨ ਕੀਤਾ ਗਿਆ ਹੈ।

ਟ੍ਰਾਂਸਫਾਰਮਰ ਮਾਡਲਾਂ ਨੂੰ ਟ੍ਰੇਨ ਕਰਨ ਲਈ ਮਿਆਰੀ ਲਾਇਬ੍ਰੇਰੀ [Hugging Face Transformers](https://huggingface.co/) ਹੈ। ਇਸ ਵਿੱਚ ਕਈ ਪ੍ਰੀ-ਟ੍ਰੇਨ ਮਾਡਲਾਂ ਦਾ ਰਿਪੋਜ਼ਟਰੀ ਸ਼ਾਮਲ ਹੈ, ਜਿਸ ਵਿੱਚ PubMedBERT ਵੀ ਹੈ। ਇਸ ਮਾਡਲ ਨੂੰ ਲੋਡ ਅਤੇ ਵਰਤਣ ਲਈ ਸਾਨੂੰ ਸਿਰਫ ਕੁਝ ਲਾਈਨਾਂ ਦੇ ਕੋਡ ਦੀ ਲੋੜ ਹੈ:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

ਇਹ ਸਾਨੂੰ `model` ਦਿੰਦਾ ਹੈ, ਜੋ ਕਿ ਟੋਕਨ ਕਲਾਸੀਫਿਕੇਸ਼ਨ ਟਾਸਕ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ, ਜਿਸ ਵਿੱਚ `classes` ਦੀ ਗਿਣਤੀ ਹੈ, ਅਤੇ `tokenizer` ਆਬਜੈਕਟ ਜੋ ਇਨਪੁਟ ਟੈਕਸਟ ਨੂੰ ਟੋਕਨ ਵਿੱਚ ਵੰਡ ਸਕਦਾ ਹੈ। ਤੁਹਾਨੂੰ ਡੇਟਾਸੈਟ ਨੂੰ BIO ਫਾਰਮੈਟ ਵਿੱਚ ਕਨਵਰਟ ਕਰਨਾ ਹੋਵੇਗਾ, ਜਿਸ ਵਿੱਚ PubMedBERT ਟੋਕਨਾਈਜ਼ੇਸ਼ਨ ਨੂੰ ਧਿਆਨ ਵਿੱਚ ਰੱਖਣਾ ਹੋਵੇਗਾ। ਤੁਸੀਂ [ਇਸ Python ਕੋਡ](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) ਤੋਂ ਪ੍ਰੇਰਣਾ ਲੈ ਸਕਦੇ ਹੋ।

## ਸਿੱਖਿਆ

ਇਹ ਟਾਸਕ ਹਕੀਕਤ ਵਿੱਚ ਉਸ ਟਾਸਕ ਦੇ ਬਹੁਤ ਨੇੜੇ ਹੈ ਜੋ ਤੁਹਾਨੂੰ ਵੱਡੇ ਪੱਧਰ 'ਤੇ ਕੁਦਰਤੀ ਭਾਸ਼ਾ ਦੇ ਟੈਕਸਟਾਂ ਵਿੱਚ ਅਧਿਕ ਜਾਣਕਾਰੀ ਪ੍ਰਾਪਤ ਕਰਨ ਲਈ ਕਰਨਾ ਪਵੇਗਾ। ਸਾਡੇ ਕੇਸ ਵਿੱਚ, ਅਸੀਂ ਆਪਣੇ ਟ੍ਰੇਨ ਕੀਤੇ ਮਾਡਲ ਨੂੰ [COVID-ਸੰਬੰਧੀ ਪੇਪਰਾਂ ਦੇ ਡੇਟਾਸੈਟ](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) 'ਤੇ ਲਾਗੂ ਕਰ ਸਕਦੇ ਹਾਂ ਅਤੇ ਦੇਖ ਸਕਦੇ ਹਾਂ ਕਿ ਅਸੀਂ ਕਿਹੜੀਆਂ ਜਾਣਕਾਰੀਆਂ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਾਂ। [ਇਹ ਬਲੌਗ ਪੋਸਟ](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) ਅਤੇ [ਇਹ ਪੇਪਰ](https://www.mdpi.com/2504-2289/6/1/4) ਇਸ ਪੇਪਰਾਂ ਦੇ ਸੰਗ੍ਰਹਿ 'ਤੇ NER ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਕੀਤੀ ਗਈ ਖੋਜ ਦਾ ਵੇਰਵਾ ਦਿੰਦੇ ਹਨ।

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਣਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।