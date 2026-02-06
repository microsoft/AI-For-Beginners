# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) बाट ल्याब असाइनमेन्ट।

## कार्य

यस ल्याबमा, तपाईंले मेडिकल शब्दहरूको लागि नामित इकाई पहिचान (NER) मोडेल प्रशिक्षण गर्नुपर्नेछ।

## डेटासेट

NER मोडेल प्रशिक्षण गर्न, हामीलाई मेडिकल इकाईहरू सहित सही रूपमा लेबल गरिएको डेटासेट आवश्यक छ। [BC5CDR डेटासेट](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) ले १५०० भन्दा बढी पेपरहरूबाट लेबल गरिएको रोग र रसायन इकाईहरू समावेश गर्दछ। तपाईंले उनीहरूको वेबसाइटमा दर्ता गरेपछि डेटासेट डाउनलोड गर्न सक्नुहुन्छ।

BC5CDR डेटासेट यस प्रकार देखिन्छ:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

यस डेटासेटमा, पहिलो दुई लाइनमा पेपरको शीर्षक र सारांश हुन्छ, त्यसपछि व्यक्तिगत इकाईहरू हुन्छन्, जसको सुरुवात र अन्त्य स्थान शीर्षक+सारांश ब्लकभित्र हुन्छ। इकाई प्रकारको अतिरिक्त, तपाईंले केही मेडिकल ओन्टोलोजीभित्र यस इकाईको ओन्टोलोजी आईडी प्राप्त गर्नुहुन्छ।

तपाईंले यसलाई BIO एन्कोडिङमा रूपान्तरण गर्न केही Python कोड लेख्नुपर्नेछ।

## नेटवर्क

NER को पहिलो प्रयास LSTM नेटवर्क प्रयोग गरेर गर्न सकिन्छ, जस्तै तपाईंले पाठको समयमा देख्नुभएको उदाहरणमा। तर NLP कार्यहरूमा, [ट्रान्सफर्मर आर्किटेक्चर](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) र विशेष गरी [BERT भाषा मोडेलहरू](https://en.wikipedia.org/wiki/BERT_(language_model)) ले धेरै राम्रो परिणाम देखाउँछन्। प्रि-ट्रेन गरिएको BERT मोडेलहरूले भाषाको सामान्य संरचना बुझ्छन्, र विशिष्ट कार्यहरूको लागि तुलनात्मक रूपमा सानो डेटासेट र कम्प्युटेशनल लागतको साथ फाइन-ट्युन गर्न सकिन्छ।

किनकि हामी मेडिकल परिदृश्यमा NER लागू गर्ने योजना बनाउँदैछौं, मेडिकल पाठहरूमा प्रशिक्षित BERT मोडेल प्रयोग गर्नु उपयुक्त हुन्छ। Microsoft Research ले [PubMedBERT][PubMedBERT] ([publication][PubMedBERT-Pub]) नामक प्रि-ट्रेन गरिएको मोडेल जारी गरेको छ, जुन [PubMed](https://pubmed.ncbi.nlm.nih.gov/) रिपोजिटरीका पाठहरू प्रयोग गरेर फाइन-ट्युन गरिएको थियो।

ट्रान्सफर्मर मोडेलहरू प्रशिक्षणको लागि *de facto* मानक [Hugging Face Transformers](https://huggingface.co/) लाइब्रेरी हो। यसमा PubMedBERT सहित समुदायद्वारा व्यवस्थापन गरिएको प्रि-ट्रेन गरिएको मोडेलहरूको रिपोजिटरी पनि समावेश छ। यो मोडेल लोड गर्न र प्रयोग गर्न हामीलाई केही लाइन कोड मात्र आवश्यक छ:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

यसले हामीलाई `model` प्रदान गर्दछ, जुन `classes` को संख्या प्रयोग गरेर टोकन वर्गीकरण कार्यको लागि निर्माण गरिएको छ, साथै `tokenizer` वस्तु जसले इनपुट पाठलाई टोकनहरूमा विभाजन गर्न सक्छ। तपाईंले डेटासेटलाई BIO ढाँचामा रूपान्तरण गर्नुपर्नेछ, PubMedBERT टोकनाइजेशनलाई ध्यानमा राख्दै। तपाईं [यस Python कोडको टुक्रा](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) प्रेरणाको रूपमा प्रयोग गर्न सक्नुहुन्छ।

## मुख्य कुरा

यो कार्य वास्तविक कार्यसँग धेरै नजिक छ जुन तपाईंले ठूलो मात्रामा प्राकृतिक भाषा पाठहरूमा थप जानकारी प्राप्त गर्न चाहनुहुन्छ भने गर्नुपर्नेछ। हाम्रो केसमा, हामीले प्रशिक्षित मोडेललाई [COVID-सम्बन्धित पेपरहरूको डेटासेट](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) मा लागू गर्न सक्छौं र हामीले के जानकारी प्राप्त गर्न सक्छौं हेर्न सक्छौं। [यो ब्लग पोस्ट](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) र [यो पेपर](https://www.mdpi.com/2504-2289/6/1/4) ले NER प्रयोग गरेर यस पेपरहरूको संग्रहमा गर्न सकिने अनुसन्धान वर्णन गर्दछ।

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी यथासम्भव शुद्धताको प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा अशुद्धताहरू हुन सक्छन्। यसको मूल भाषामा रहेको मूल दस्तावेज़लाई आधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुने छैनौं।