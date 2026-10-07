# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) se lab assignment.

## Task

Is lab mein, aapko medical terms ke liye ek Named Entity Recognition (NER) model train karna hai.

## Dataset

NER model ko train karne ke liye, humein medical entities ke saath sahi tarah se labeled dataset chahiye. [BC5CDR dataset](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) mein 1500 se zyada papers se diseases aur chemicals ki labeled entities shaamil hain. Aap unki website par register karne ke baad yeh dataset download kar sakte hain.

BC5CDR dataset aisa dikhta hai:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

Is dataset mein, pehli do lines mein paper ka title aur abstract hota hai, aur phir individual entities hoti hain, jinke start aur end positions title+abstract block ke andar hote hain. Entity type ke alawa, aapko is entity ka kisi medical ontology mein ontology ID bhi milta hai.

Aapko ise BIO encoding mein convert karne ke liye kuch Python code likhna hoga.

## Network

NER ke liye pehla attempt LSTM network use karke kiya ja sakta hai, jaisa aapne lesson ke dauran hamare example mein dekha hai. Halaanki, NLP tasks mein, [transformer architecture](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) aur khaas taur par [BERT language models](https://en.wikipedia.org/wiki/BERT_(language_model)) kahin behtar results dikhate hain. Pre-trained BERT models language ki general structure samajhte hain aur relatively chhote datasets aur kam computational cost ke saath specific tasks ke liye fine-tune kiye ja sakte hain.

Kyunki hum NER ko medical scenario mein apply karne ki plan bana rahe hain, isliye medical text par train kiye gaye BERT model ko use karna samajhdaari hogi. Microsoft Research ne [PubMedBERT][PubMedBERT] ([publication][PubMedBERT-Pub]) naam ka ek pre-trained model release kiya hai, jise [PubMed](https://pubmed.ncbi.nlm.nih.gov/) repository ke text ka use karke fine-tune kiya gaya tha.

Transformer models ko train karne ke liye *de facto* standard [Hugging Face Transformers](https://huggingface.co/) library hai. Isme community dwara banaye gaye pre-trained models ki repository bhi shaamil hai, jisme PubMedBERT bhi hai. Is model ko load aur use karne ke liye, humein sirf kuch lines of code chahiye:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

Yeh humein `model` deta hai, jo token classification task ke liye `classes` ki sankhya ke saath banaya gaya hai, aur `tokenizer` object jo input text ko tokens mein split kar sakta hai. Aapko dataset ko BIO format mein convert karna hoga, PubMedBERT tokenization ko dhyan mein rakhte hue. Aap [is Python code snippet](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) ko inspiration ke roop mein use kar sakte hain.

## Conclusion

Yeh task real task ke bahut kareeb hai, jo aapko bade paimane par natural language text analyze karne ke liye karna pad sakta hai. Hamare case mein, hum apne trained model ko [COVID se related papers ke dataset](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) par apply kar sakte hain aur dekh sakte hain ki hum kaunsi-kaunsi insights nikaal sakte hain. [Yeh blog post](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) aur [yeh paper](https://www.mdpi.com/2504-2289/6/1/4) papers ke is corpus par NER use karke ki gayi research ka description dete hain.

---

<!-- HINGLISH NOTE START -->
**Note**:
Yeh document Hindi translation ko Hinglish (Roman script) mein convert karke banaya gaya hai, taaki padhna aur samajhna aasaan ho.
Isme kuch galtiyan ya anuvaad ki kamiyan ho sakti hain. Sabse sahi jaankari ke liye original English document ko hi authoritative source maanein.
<!-- HINGLISH NOTE END -->
