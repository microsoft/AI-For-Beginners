# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) से प्रयोगशाला असाइनमेंट।

## कार्य

इस प्रयोगशाला में, आपको चिकित्सा शब्दों के लिए नामित इकाई पहचान मॉडल को प्रशिक्षित करना होगा।

## डेटासेट

NER मॉडल को प्रशिक्षित करने के लिए, हमें चिकित्सा इकाइयों के साथ उचित रूप से लेबल किया गया डेटासेट चाहिए। [BC5CDR डेटासेट](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) में 1500 से अधिक पत्रों से लेबल किए गए रोगों और रसायनों की इकाइयाँ शामिल हैं। आप उनकी वेबसाइट पर पंजीकरण करने के बाद डेटासेट डाउनलोड कर सकते हैं।

BC5CDR डेटासेट इस तरह दिखता है:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

इस डेटासेट में, पहले दो पंक्तियों में पत्र का शीर्षक और सारांश है, और फिर व्यक्तिगत इकाइयाँ हैं, जिनमें शीर्षक+सारांश ब्लॉक के भीतर प्रारंभ और अंत स्थिति होती है। इकाई के प्रकार के अलावा, आपको इस इकाई का ओंटोलॉजी आईडी भी मिलता है, जो कुछ चिकित्सा ओंटोलॉजी के भीतर होता है।

आपको इसे BIO एन्कोडिंग में परिवर्तित करने के लिए कुछ पायथन कोड लिखने की आवश्यकता होगी।

## नेटवर्क

NER पर पहला प्रयास LSTM नेटवर्क का उपयोग करके किया जा सकता है, जैसा कि आपने पाठ के दौरान देखा। हालाँकि, NLP कार्यों में, [ट्रांसफार्मर आर्किटेक्चर](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) और विशेष रूप से [BERT भाषा मॉडल](https://en.wikipedia.org/wiki/BERT_(language_model)) बहुत बेहतर परिणाम दिखाते हैं। पूर्व-प्रशिक्षित BERT मॉडल एक भाषा की सामान्य संरचना को समझते हैं, और विशेष कार्यों के लिए अपेक्षाकृत छोटे डेटासेट और कम्प्यूटेशनल लागत के साथ फाइन-ट्यून किया जा सकता है।

चूंकि हम चिकित्सा परिदृश्य में NER लागू करने की योजना बना रहे हैं, इसलिए चिकित्सा पाठों पर प्रशिक्षित BERT मॉडल का उपयोग करना समझ में आता है। Microsoft Research ने एक पूर्व-प्रशिक्षित मॉडल जारी किया है जिसे [PubMedBERT][PubMedBERT] ([प्रकाशन][PubMedBERT-Pub]) कहा जाता है, जिसे [PubMed](https://pubmed.ncbi.nlm.nih.gov/) रिपॉजिटरी से पाठों का उपयोग करके फाइन-ट्यून किया गया था।

ट्रांसफार्मर मॉडल को प्रशिक्षित करने के लिए *de facto* मानक [Hugging Face Transformers](https://huggingface.co/) पुस्तकालय है। इसमें समुदाय द्वारा बनाए गए पूर्व-प्रशिक्षित मॉडलों का एक रिपॉजिटरी भी शामिल है, जिसमें PubMedBERT भी है। इस मॉडल को लोड और उपयोग करने के लिए, हमें केवल कुछ पंक्तियों के कोड की आवश्यकता है:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

यह हमें `model` itself, built for token classification task using `classes` number of classes, as well as `tokenizer` वस्तु देता है जो इनपुट पाठ को टोकनों में विभाजित कर सकता है। आपको डेटासेट को BIO प्रारूप में परिवर्तित करने की आवश्यकता होगी, जिसमें PubMedBERT टोकनाइजेशन का ध्यान रखा जाएगा। आप [इस पायथन कोड के टुकड़े](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) का उपयोग प्रेरणा के रूप में कर सकते हैं।

## निष्कर्ष

यह कार्य वास्तव में उस कार्य के बहुत करीब है जो आपके पास तब होगा जब आप प्राकृतिक भाषा के पाठों की बड़ी मात्रा में अधिक अंतर्दृष्टि प्राप्त करना चाहेंगे। हमारे मामले में, हम अपने प्रशिक्षित मॉडल को [COVID-संबंधित पत्रों के डेटासेट](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) पर लागू कर सकते हैं और देख सकते हैं कि हम कौन सी अंतर्दृष्टियाँ प्राप्त कर सकते हैं। [यह ब्लॉग पोस्ट](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) और [यह पेपर](https://www.mdpi.com/2504-2289/6/1/4) इस डेटासेट पर NER का उपयोग करके किए जा सकने वाले अनुसंधान का वर्णन करते हैं।

**अस्वीकृति**:  
यह दस्तावेज़ मशीन-आधारित एआई अनुवाद सेवाओं का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को उसकी मूल भाषा में प्राधिकृत स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।