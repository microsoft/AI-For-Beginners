# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) থেকে ল্যাব অ্যাসাইনমেন্ট।

## কাজ

এই ল্যাবে, আপনাকে মেডিক্যাল টার্মের জন্য একটি নামযুক্ত সত্তা সনাক্তকরণ (NER) মডেল প্রশিক্ষণ দিতে হবে।

## ডেটাসেট

NER মডেল প্রশিক্ষণের জন্য, আমাদের মেডিক্যাল সত্তাগুলির সঠিকভাবে লেবেলযুক্ত ডেটাসেট প্রয়োজন। [BC5CDR ডেটাসেট](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) ১৫০০ এর বেশি পেপার থেকে লেবেলযুক্ত রোগ এবং রাসায়নিক সত্তাগুলি ধারণ করে। আপনি তাদের ওয়েবসাইটে নিবন্ধন করার পর ডেটাসেটটি ডাউনলোড করতে পারবেন।

BC5CDR ডেটাসেট দেখতে এরকম:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

এই ডেটাসেটে, প্রথম দুটি লাইনে পেপারের শিরোনাম এবং সারাংশ থাকে, এবং তারপর পৃথক সত্তাগুলি থাকে, যার শুরুর এবং শেষ অবস্থান শিরোনাম+সারাংশ ব্লকের মধ্যে দেওয়া থাকে। সত্তার প্রকার ছাড়াও, আপনি এই সত্তার মেডিক্যাল অন্টোলজির মধ্যে অন্টোলজি আইডি পাবেন।

আপনাকে এটি BIO এনকোডিংয়ে রূপান্তর করতে কিছু Python কোড লিখতে হবে।

## নেটওয়ার্ক

NER-এর প্রথম প্রচেষ্টা LSTM নেটওয়ার্ক ব্যবহার করে করা যেতে পারে, যেমন আপনি পাঠে উদাহরণে দেখেছেন। তবে, NLP কাজগুলিতে, [ট্রান্সফর্মার আর্কিটেকচার](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) এবং বিশেষভাবে [BERT ভাষার মডেল](https://en.wikipedia.org/wiki/BERT_(language_model)) অনেক ভালো ফলাফল দেখায়। প্রি-ট্রেইনড BERT মডেলগুলি একটি ভাষার সাধারণ গঠন বুঝতে পারে এবং তুলনামূলকভাবে ছোট ডেটাসেট এবং কম্পিউটেশনাল খরচ দিয়ে নির্দিষ্ট কাজের জন্য ফাইন-টিউন করা যায়।

যেহেতু আমরা মেডিক্যাল পরিস্থিতিতে NER প্রয়োগ করতে যাচ্ছি, তাই মেডিক্যাল টেক্সটের উপর প্রশিক্ষিত BERT মডেল ব্যবহার করাটা যুক্তিযুক্ত। Microsoft Research একটি প্রি-ট্রেইনড মডেল প্রকাশ করেছে যার নাম [PubMedBERT][PubMedBERT] ([প্রকাশনা][PubMedBERT-Pub]), যা [PubMed](https://pubmed.ncbi.nlm.nih.gov/) রিপোজিটরির টেক্সট ব্যবহার করে ফাইন-টিউন করা হয়েছে।

ট্রান্সফর্মার মডেল প্রশিক্ষণের জন্য *de facto* স্ট্যান্ডার্ড হলো [Hugging Face Transformers](https://huggingface.co/) লাইব্রেরি। এটি কমিউনিটি-রক্ষণাবেক্ষিত প্রি-ট্রেইনড মডেলের একটি রিপোজিটরি ধারণ করে, যার মধ্যে PubMedBERT অন্তর্ভুক্ত। এই মডেল লোড এবং ব্যবহার করতে আমাদের মাত্র কয়েকটি লাইনের কোড প্রয়োজন:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

এটি আমাদের `model` প্রদান করে, যা টোকেন ক্লাসিফিকেশন কাজের জন্য `classes` সংখ্যক ক্লাস ব্যবহার করে তৈরি করা হয়েছে, এবং `tokenizer` অবজেক্ট প্রদান করে যা ইনপুট টেক্সটকে টোকেনে বিভক্ত করতে পারে। আপনাকে ডেটাসেটটি BIO ফরম্যাটে রূপান্তর করতে হবে, PubMedBERT টোকেনাইজেশন বিবেচনায় রেখে। আপনি [এই Python কোডের অংশ](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) অনুপ্রেরণা হিসেবে ব্যবহার করতে পারেন।

## মূল বিষয়

এই কাজটি প্রকৃত কাজের খুব কাছাকাছি, যা আপনি সম্ভবত করবেন যদি আপনি প্রাকৃতিক ভাষার টেক্সটের বৃহৎ পরিমাণে আরও অন্তর্দৃষ্টি অর্জন করতে চান। আমাদের ক্ষেত্রে, আমরা আমাদের প্রশিক্ষিত মডেলটি [COVID-সম্পর্কিত পেপারের ডেটাসেটে](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) প্রয়োগ করতে পারি এবং দেখতে পারি আমরা কী অন্তর্দৃষ্টি অর্জন করতে পারি। [এই ব্লগ পোস্ট](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) এবং [এই পেপার](https://www.mdpi.com/2504-2289/6/1/4) বর্ণনা করে যে NER ব্যবহার করে এই পেপারের কর্পাসে কী গবেষণা করা যেতে পারে।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য সঠিক অনুবাদের চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। নথিটির মূল ভাষায় থাকা আসল সংস্করণটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।