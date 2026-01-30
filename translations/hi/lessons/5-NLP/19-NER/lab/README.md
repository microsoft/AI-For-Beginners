# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) से लैब असाइनमेंट।

## कार्य

इस लैब में, आपको मेडिकल शब्दों के लिए एक नामित इकाई पहचान (NER) मॉडल को प्रशिक्षित करना है।

## डेटासेट

NER मॉडल को प्रशिक्षित करने के लिए, हमें मेडिकल इकाइयों के साथ सही तरीके से लेबल किया गया डेटासेट चाहिए। [BC5CDR डेटासेट](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) में 1500 से अधिक पेपर्स से बीमारियों और रसायनों की लेबल की गई इकाइयाँ शामिल हैं। आप उनके वेबसाइट पर रजिस्टर करने के बाद इस डेटासेट को डाउनलोड कर सकते हैं।

BC5CDR डेटासेट इस प्रकार दिखता है:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

इस डेटासेट में, पहले दो लाइनों में पेपर का शीर्षक और सारांश होता है, और फिर व्यक्तिगत इकाइयाँ होती हैं, जिनमें शीर्षक+सारांश ब्लॉक के भीतर आरंभ और समाप्ति स्थान होते हैं। इकाई के प्रकार के अलावा, आपको इस इकाई का किसी मेडिकल ऑंटोलॉजी में ऑंटोलॉजी आईडी भी मिलता है।

आपको इसे BIO एन्कोडिंग में बदलने के लिए कुछ Python कोड लिखने की आवश्यकता होगी।

## नेटवर्क

NER के लिए पहला प्रयास LSTM नेटवर्क का उपयोग करके किया जा सकता है, जैसा कि आपने पाठ के दौरान हमारे उदाहरण में देखा है। हालांकि, NLP कार्यों में, [ट्रांसफॉर्मर आर्किटेक्चर](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) और विशेष रूप से [BERT भाषा मॉडल्स](https://en.wikipedia.org/wiki/BERT_(language_model)) कहीं बेहतर परिणाम दिखाते हैं। प्री-ट्रेंड BERT मॉडल भाषा की सामान्य संरचना को समझते हैं और अपेक्षाकृत छोटे डेटासेट और कम कंप्यूटेशनल लागत के साथ विशिष्ट कार्यों के लिए फाइन-ट्यून किए जा सकते हैं।

चूंकि हम NER को मेडिकल परिदृश्य में लागू करने की योजना बना रहे हैं, इसलिए मेडिकल टेक्स्ट पर प्रशिक्षित BERT मॉडल का उपयोग करना समझदारी होगी। Microsoft Research ने [PubMedBERT][PubMedBERT] ([प्रकाशन][PubMedBERT-Pub]) नामक एक प्री-ट्रेंड मॉडल जारी किया है, जिसे [PubMed](https://pubmed.ncbi.nlm.nih.gov/) रिपॉजिटरी के टेक्स्ट का उपयोग करके फाइन-ट्यून किया गया था।

ट्रांसफॉर्मर मॉडल को प्रशिक्षित करने के लिए *डि फैक्टो* मानक [Hugging Face Transformers](https://huggingface.co/) लाइब्रेरी है। इसमें सामुदायिक रूप से बनाए गए प्री-ट्रेंड मॉडल्स का रिपॉजिटरी भी शामिल है, जिसमें PubMedBERT भी है। इस मॉडल को लोड और उपयोग करने के लिए, हमें केवल कुछ लाइनों के कोड की आवश्यकता है:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

यह हमें `model` देता है, जो टोकन वर्गीकरण कार्य के लिए `classes` की संख्या के साथ बनाया गया है, और `tokenizer` ऑब्जेक्ट जो इनपुट टेक्स्ट को टोकन में विभाजित कर सकता है। आपको डेटासेट को BIO फॉर्मेट में बदलने की आवश्यकता होगी, PubMedBERT टोकनाइजेशन को ध्यान में रखते हुए। आप [इस Python कोड के टुकड़े](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) को प्रेरणा के रूप में उपयोग कर सकते हैं।

## निष्कर्ष

यह कार्य वास्तविक कार्य के बहुत करीब है, जो आपको बड़े पैमाने पर प्राकृतिक भाषा टेक्स्ट का विश्लेषण करने के लिए करना पड़ सकता है। हमारे मामले में, हम अपने प्रशिक्षित मॉडल को [COVID से संबंधित पेपर्स के डेटासेट](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) पर लागू कर सकते हैं और देख सकते हैं कि हम कौन-कौन सी जानकारियाँ प्राप्त कर सकते हैं। [यह ब्लॉग पोस्ट](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) और [यह पेपर](https://www.mdpi.com/2504-2289/6/1/4) इस कॉर्पस ऑफ पेपर्स पर NER का उपयोग करके किए गए शोध का वर्णन करते हैं।

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियां या अशुद्धियां हो सकती हैं। मूल भाषा में उपलब्ध मूल दस्तावेज़ को प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।