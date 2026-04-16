# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) இல் இருந்து ஆய்வகப் பணிக்கான ஒதுக்கீடு.

## பணிக்குறிப்பு

இந்த ஆய்வகத்தில், மருத்துவ சொற்களுக்கான பெயரிடப்பட்ட பொருள் அடையாளம் காணும் (NER) மாதிரியை பயிற்சி செய்ய வேண்டும்.

## தரவுத்தொகுப்பு

NER மாதிரியை பயிற்சி செய்ய, மருத்துவ பொருட்களுடன் சரியாக குறிக்கப்பட்ட தரவுத்தொகுப்பு தேவை. [BC5CDR dataset](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) 1500-க்கும் மேற்பட்ட ஆவணங்களில் இருந்து குறிக்கப்பட்ட நோய்கள் மற்றும் இரசாயன பொருட்களை கொண்டுள்ளது. அவர்களின் இணையதளத்தில் பதிவு செய்த பிறகு, நீங்கள் இந்த தரவுத்தொகுப்பை பதிவிறக்கம் செய்யலாம்.

BC5CDR Dataset இவ்வாறு தோற்றமளிக்கிறது:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

இந்த தரவுத்தொகுப்பில், முதல் இரண்டு வரிகளில் ஆவணத்தின் தலைப்பு மற்றும் சுருக்கம் உள்ளது, பின்னர் தனிப்பட்ட பொருட்கள், தலைப்பு+சுருக்கம் தொகுதியில் தொடக்கம் மற்றும் முடிவு இடங்களுடன் உள்ளது. பொருள் வகை தவிர, இந்த பொருளின் மருத்துவ ஒன்டாலஜியில் உள்ள ஒன்டாலஜி ஐடியையும் பெறலாம்.

இந்த தரவுத்தொகுப்பை BIO குறியாக்கமாக மாற்ற Python குறியீட்டை எழுத வேண்டும்.

## நெட்வொர்க்

NER-க்கு முதல் முயற்சியாக, பாடத்தில் நீங்கள் பார்த்த உதாரணத்தைப் போல LSTM நெட்வொர்க் பயன்படுத்தலாம். ஆனால், NLP பணிகளில், [transformer architecture](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) மற்றும் குறிப்பாக [BERT language models](https://en.wikipedia.org/wiki/BERT_(language_model)) மிகவும் சிறந்த முடிவுகளை வழங்குகிறது. முன்பே பயிற்சி செய்யப்பட்ட BERT மாதிரிகள் ஒரு மொழியின் பொதுவான அமைப்பை புரிந்துகொள்கின்றன, மேலும் குறிப்பிட்ட பணிகளுக்கு சிறிய தரவுத்தொகுப்புகள் மற்றும் கணினி செலவுகளுடன் நன்றாகச் சரிசெய்யப்படலாம்.

மருத்துவ சூழலுக்கு NER ஐ பயன்படுத்த திட்டமிடுவதால், மருத்துவ உரைகளில் பயிற்சி செய்யப்பட்ட BERT மாதிரியைப் பயன்படுத்துவது பொருத்தமாக இருக்கும். Microsoft Research [PubMedBERT][PubMedBERT] ([publication][PubMedBERT-Pub]) என்ற முன்பே பயிற்சி செய்யப்பட்ட மாதிரியை வெளியிட்டுள்ளது, இது [PubMed](https://pubmed.ncbi.nlm.nih.gov/) களஞ்சியத்தில் இருந்து உரைகளைப் பயன்படுத்தி நன்றாகச் சரிசெய்யப்பட்டது.

Transformer மாதிரிகளைப் பயிற்சி செய்யும் *de facto* தரநிலை [Hugging Face Transformers](https://huggingface.co/) நூலகம் ஆகும். இது PubMedBERT உட்பட சமூகத்தால் பராமரிக்கப்படும் முன்பே பயிற்சி செய்யப்பட்ட மாதிரிகளின் களஞ்சியத்தையும் கொண்டுள்ளது. இந்த மாதிரியை ஏற்றவும் பயன்படுத்தவும், சில வரிகளின் குறியீடு மட்டுமே தேவை:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

இது `model` ஐ வழங்குகிறது, இது `classes` வகைகளின் எண்ணிக்கையைப் பயன்படுத்தி token classification பணிக்காக உருவாக்கப்பட்டது, மேலும் `tokenizer` பொருள், உள்ளீட்டு உரையை token-களாகப் பிரிக்க உதவுகிறது. நீங்கள் தரவுத்தொகுப்பை BIO வடிவமாக மாற்ற வேண்டும், PubMedBERT tokenization ஐ கருத்தில் கொண்டு. [இந்த Python குறியீட்டு பகுதியை](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) ஒரு ஊக்கமாகப் பயன்படுத்தலாம்.

## முக்கியக் கருத்து

இந்தப் பணி, இயற்கை மொழி உரைகளின் பெரிய தொகுதிகளில் மேலும் தகவல்களைப் பெற விரும்பினால் நீங்கள் எதிர்கொள்ளக்கூடிய உண்மையான பணிக்கு மிகவும் அருகில் உள்ளது. எங்கள் நிலைமையில், [COVID தொடர்பான ஆவணங்களின் தரவுத்தொகுப்பை](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) எங்கள் பயிற்சி செய்யப்பட்ட மாதிரியில் பயன்படுத்தி, எவ்வகையான தகவல்களைப் பெற முடியும் என்பதைப் பார்க்கலாம். [இந்த வலைப்பதிவு](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) மற்றும் [இந்த ஆவணம்](https://www.mdpi.com/2504-2289/6/1/4) NER ஐப் பயன்படுத்தி இந்த ஆவண தொகுப்பில் செய்யக்கூடிய ஆராய்ச்சியை விவரிக்கிறது.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் தரச்செயல்முறையை உறுதிப்படுத்த முயற்சிக்கிறோம், ஆனால் தானியக்க மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்கக்கூடும் என்பதை கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.