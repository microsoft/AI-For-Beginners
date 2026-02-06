# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) मधील प्रयोगशाळा कार्य.

## कार्य

या प्रयोगशाळेत, तुम्हाला वैद्यकीय संज्ञांसाठी नामित घटक ओळख (NER) मॉडेल प्रशिक्षण द्यायचे आहे.

## डेटासेट

NER मॉडेल प्रशिक्षणासाठी, वैद्यकीय घटकांसह योग्यरित्या लेबल केलेला डेटासेट आवश्यक आहे. [BC5CDR डेटासेट](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) मध्ये 1500 हून अधिक पेपरमधील लेबल केलेले आजार आणि रसायनांचे घटक आहेत. तुम्ही त्यांच्या वेबसाइटवर नोंदणी केल्यानंतर हा डेटासेट डाउनलोड करू शकता.

BC5CDR डेटासेट असे दिसते:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

या डेटासेटमध्ये, पहिल्या दोन ओळींमध्ये पेपरचे शीर्षक आणि सारांश असतो, आणि नंतर वैयक्तिक घटक असतात, जे शीर्षक+सारांश ब्लॉकमधील सुरुवात आणि शेवटच्या स्थानांसह दिलेले असतात. घटक प्रकाराशिवाय, तुम्हाला या घटकाचा काही वैद्यकीय ऑंटोलॉजीमधील ऑंटोलॉजी आयडी देखील मिळतो.

तुम्हाला हे BIO एन्कोडिंगमध्ये रूपांतरित करण्यासाठी काही Python कोड लिहावा लागेल.

## नेटवर्क

NER साठी पहिला प्रयत्न LSTM नेटवर्क वापरून केला जाऊ शकतो, जसे की तुम्ही धड्यादरम्यान पाहिले आहे. तथापि, NLP कार्यांमध्ये, [ट्रान्सफॉर्मर आर्किटेक्चर](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) आणि विशेषतः [BERT भाषा मॉडेल्स](https://en.wikipedia.org/wiki/BERT_(language_model)) खूप चांगले परिणाम दाखवतात. पूर्व-प्रशिक्षित BERT मॉडेल्स भाषेची सामान्य रचना समजतात आणि तुलनेने लहान डेटासेट्स आणि कमी संगणकीय खर्चासह विशिष्ट कार्यांसाठी ट्यून केले जाऊ शकतात.

आपण वैद्यकीय परिस्थितीत NER लागू करण्याची योजना आखत असल्याने, वैद्यकीय मजकुरांवर प्रशिक्षण दिलेले BERT मॉडेल वापरणे योग्य ठरेल. Microsoft Research ने [PubMedBERT][PubMedBERT] ([प्रकाशन][PubMedBERT-Pub]) नावाचे पूर्व-प्रशिक्षित मॉडेल जारी केले आहे, जे [PubMed](https://pubmed.ncbi.nlm.nih.gov/) रिपॉझिटरीमधील मजकुरांचा वापर करून ट्यून केले गेले आहे.

ट्रान्सफॉर्मर मॉडेल्स प्रशिक्षणासाठी *de facto* मानक म्हणजे [Hugging Face Transformers](https://huggingface.co/) लायब्ररी आहे. यात समुदाय-देखरेखीखालील पूर्व-प्रशिक्षित मॉडेल्सचा रिपॉझिटरी देखील आहे, ज्यामध्ये PubMedBERT समाविष्ट आहे. हे मॉडेल लोड आणि वापरण्यासाठी, आपल्याला फक्त काही ओळींचा कोड आवश्यक आहे:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

हे आपल्याला `model` प्रदान करते, जे `classes` वर्गांच्या संख्येसह टोकन वर्गीकरण कार्यासाठी तयार केले गेले आहे, तसेच `tokenizer` ऑब्जेक्ट प्रदान करते, जो इनपुट मजकूर टोकनमध्ये विभाजित करू शकतो. तुम्हाला डेटासेटला BIO स्वरूपात रूपांतरित करावे लागेल, PubMedBERT टोकनायझेशन लक्षात घेऊन. [या Python कोडच्या तुकड्याचा](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) प्रेरणेसाठी वापर करू शकता.

## मुख्य मुद्दे

हे कार्य वास्तविक कार्याशी खूप जवळ आहे, जे तुम्हाला मोठ्या प्रमाणातील नैसर्गिक भाषेतील मजकुरांवर अधिक अंतर्दृष्टी मिळवायची असल्यास करावे लागेल. आपल्या बाबतीत, आपण प्रशिक्षित मॉडेल [COVID-संबंधित पेपरांच्या डेटासेटवर](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) लागू करू शकतो आणि आपण कोणती अंतर्दृष्टी मिळवू शकतो ते पाहू शकतो. [हा ब्लॉग पोस्ट](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) आणि [हा पेपर](https://www.mdpi.com/2504-2289/6/1/4) NER वापरून या पेपरांच्या संग्रहावर केलेल्या संशोधनाचे वर्णन करतात.

**अस्वीकरण**:  
हा दस्तऐवज AI भाषांतर सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून भाषांतरित करण्यात आला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित भाषांतरांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज हा अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी, व्यावसायिक मानवी भाषांतराची शिफारस केली जाते. या भाषांतराचा वापर केल्यामुळे उद्भवणाऱ्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.