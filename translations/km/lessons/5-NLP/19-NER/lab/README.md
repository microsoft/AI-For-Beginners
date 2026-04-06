# NER

ការប្រឡងមួយពី [កម្មវិធីសិក្សា AI សម្រាប់អ្នកចាប់ផ្តើម](https://github.com/microsoft/ai-for-beginners)។

## បេសកកម្ម

ក្នុងការប្រឡងនេះ អ្នកត្រូវតែបណ្តុះបណ្តាលម៉ូដែលសម្គាល់អង្គភាពដែលមានឈ្មោះសម្រាប់ពាក្យវេជ្ជសាស្រ្ត។

## ឈុតទិន្នន័យ

ដើម្បីបណ្តុះម៉ូដែល NER អ្នកត្រូវការឈុតទិន្នន័យដែលបានស្លាកសញ្ញាត្រឹមត្រូវជាមួយអង្គភាពវេជ្ជសាស្រ្ត។ [ឈុតទិន្នន័យ BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) មានអង្គភាពជំងឺ និងគីមីទិន្នន័យដែលបានស្លាកពីស្នាដៃច្រើនជាង ១៥០០។ អ្នកអាចទាញយកឈុតទិន្នន័យបន្ទាប់ពីចុះឈ្មោះនៅគេហទំព័ររបស់ពួកគេ។

ឈុតទិន្នន័យ BC5CDR មើលទៅដូចនេះ៖

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

ក្នុងឈុតទិន្នន័យនេះ មានចំណងជើង និងសេចក្ដីសង្ខេបកាស្នាដៃក្នុងបន្ទាត់ពីរដំបូង ហើយបន្ទាប់មក មានអង្គភាពឯករាជ្យៗ ជាមួយនិងទីតាំងចាប់ផ្ដើម និងធ្វើបញ្ចប់នៅក្នុងប្លុកចំណងជើង+សេចក្ដីសង្ខេប។ បន្ថែមពីនេះ លើសពីប្រភេទអង្គភាព អ្នកនឹងទទួលបានអត្តសញ្ញាណនិមិត្តរបស់អង្គភាពនេះក្នុងរាងវេជ្ជសាស្រ្តមួយ។

អ្នកត្រូវតែសរសេរកូដ Python ខ្លះ ដើម្បីបម្លែងអត្ថបទនេះទៅជា encoding BIO។

## បណ្តាញ

ការព្យាយាមដំបូងសម្រាប់ NER អាចធ្វើបានដោយប្រើបណ្តាញ LSTM ដូចដែលអ្នកបានឃើញក្នុងឧទាហរណ៍នៅក្នុងមេរៀន។ ទោះជាយ៉ាងណាក៏ដោយ នៅក្នុងភារកិច្ច NLP [រចនាសម្ព័ន្ធ transformer](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) និងជាទូទៅ [ម៉ូដែលភាសា BERT](https://en.wikipedia.org/wiki/BERT_(language_model)) បង្ហាញលទ្ធផលល្អជាងគេ។ ម៉ូដែល BERT ដែលបានបណ្តុះមកហើយយូរប្រែប្រួលយល់ដឹងពីរចនាសម្ព័ន្ធទូទៅនៃភាសា ហើយអាចធ្វើការកែប្រែត្រៀមសម្រាប់ភារកិច្ចជាក់លាក់ជាមួយឈុតទិន្នន័យតូច និងការចំណាយគណនាប្រសើរ។

ដោយសារយើងកំពុងផែនការដើម្បីអនុវត្ត NER ទៅលើស្ថានการณ์វេជ្ជសាស្រ្ត វាមានហេតុផលផ្តល់អត្ថប្រយោជន៍ក្នុងការប្រើម៉ូដែល BERT ដែលបានបណ្តុះលើអត្ថបទវេជ្ជសាស្រ្ត។ ការស្រាវជ្រាវ Microsoft បានចេញផ្សាយម៉ូដែលដែលបានបណ្តុះមួយឈ្មោះ [PubMedBERT][PubMedBERT] ([ការចេញផ្សាយ][PubMedBERT-Pub]) ដែលបានកែប្រែបន្ថែមដោយប្រើអត្ថបទពីឃ្លាំង [PubMed](https://pubmed.ncbi.nlm.nih.gov/)។

ស្តង់ដារដែលពេញនិយមសម្រាប់បណ្ដុះម៉ូដែល transformer គឺបណ្ណាល័យ [Hugging Face Transformers](https://huggingface.co/)។ វានៅក្នុងនោះមានឃ្លាំងនៃម៉ូដែលដែលបានបណ្តុះដោយសហគមន៍រួមទាំង PubMedBERT។ ដើម្បីបង្ហោះ និងប្រើម៉ូដែលនេះ អ្នកគ្រាន់តែត្រូវតែមានបន្ទាត់កូដពីរបីប៉ុណ្ណោះ៖

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # ចំនួនថ្នាក់៖ 2*អង្គភាព+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

នេះផ្តល់ឲ្យយើង `model` មួយ ដែលបង្កើតសម្រាប់ភារកិច្ចកំណត់ប្រភេទ token ជាមួយ និងចំនួន `classes` និងវត្ថុ `tokenizer` ដែលអាចបំបែកអត្ថបទបញ្ចូលទៅជាកំណត់ត្រា។ អ្នកត្រូវបម្លែងឈុតទិន្នន័យទៅជា BIO ទ្រង់ទ្រាយដោយគិតគូរពី tokenization របស់ PubMedBERT។ អ្នកអាចប្រើ [កូដ Python នេះ](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) ជាការប្រមូលចំណេះដឹង។

## ជំហានក្រោយ

ភារកិច្ចនេះជិតស្និទ្ធជាមួយភារកិច្ចពិតប្រាកដដែលអ្នកអាចមាន ប្រសិនបើអ្នកចង់ទទួលបានការយល់ដឹងបន្ថែមពីអត្ថបទភាសាធម្មជាតិនៅចំណុះធំ។ នៅករណីរបស់យើង អ្នកអាចអនុវត្តម៉ូដែលដែលបានបណ្តុះទៅលើ [ឈុតទិន្នន័យស្នាដៃ COVID-19](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) ហើយមើលថាតើយើងអាចទទួលបានការយល់ដឹងអ្វីខ្លះ។ [អត្ថបទប្លុកនេះ](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) និង [សៀវភៅនេះ](https://www.mdpi.com/2504-2289/6/1/4) ពិពណ៌នាអំពីការស្រាវជ្រាវដែលអាចធ្វើបានលើឯកសារស្នាដៃនេះដោយប្រើ NER។

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ នៅពេលដែលយើងខិតខំប្រឹងប្រែងដើម្បីឱ្យបានភាពត្រឹមត្រូវ សូមដឹងថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬភាពមិនត្រឹមត្រូវទៅវិញ។ ឯកសារដើមក្នុងភាសាដើមគួរត្រូវបានពិចារណាថាជាអ្នកផ្គត់ផ្គង់ព័ត៌មានផ្លូវការជាចម្បង។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយអ្នកជំនាញមនុស្សគឺត្រូវបានណែនាំ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកស្រាយមិនត្រឹមត្រូវណាមួយដែលកើតឡើងដោយសារការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->