# این ای آر

[اے آئی فار بیگنرز کریکولم](https://github.com/microsoft/ai-for-beginners) سے لیب اسائنمنٹ۔

## کام

اس لیب میں، آپ کو طبی اصطلاحات کے لیے نییمڈ اینٹیٹی ریکگنیشن ماڈل کو تربیت دینا ہے۔

## ڈیٹا سیٹ

این ای آر ماڈل کو تربیت دینے کے لیے، ہمیں طبی اینٹیٹیز کے ساتھ مناسب طور پر لیبل شدہ ڈیٹا سیٹ کی ضرورت ہے۔ [بی سی 5 سی ڈی آر ڈیٹا سیٹ](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) میں 1500 سے زیادہ پیپرز سے لیبل شدہ بیماریوں اور کیمیکل اینٹیٹیز شامل ہیں۔ آپ ان کی ویب سائٹ پر رجسٹریشن کے بعد ڈیٹا سیٹ ڈاؤن لوڈ کر سکتے ہیں۔

بی سی 5 سی ڈی آر ڈیٹا سیٹ کچھ اس طرح نظر آتا ہے:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

اس ڈیٹا سیٹ میں، پہلے دو لائنوں میں پیپر کا عنوان اور خلاصہ ہوتا ہے، اور اس کے بعد انفرادی اینٹیٹیز ہوتی ہیں، جن کے آغاز اور اختتام کی پوزیشنز عنوان+خلاصہ بلاک کے اندر دی گئی ہوتی ہیں۔ اینٹیٹی کی قسم کے علاوہ، آپ کو اس اینٹیٹی کا اونٹولوجی آئی ڈی بھی ملتا ہے جو کسی طبی اونٹولوجی کے اندر موجود ہوتا ہے۔

آپ کو اس ڈیٹا کو بائیو انکوڈنگ میں تبدیل کرنے کے لیے کچھ پائتھون کوڈ لکھنا ہوگا۔

## نیٹ ورک

این ای آر کے لیے پہلا تجربہ ایل ایس ٹی ایم نیٹ ورک کے ذریعے کیا جا سکتا ہے، جیسا کہ آپ نے سبق کے دوران مثال میں دیکھا۔ تاہم، این ایل پی کے کاموں میں، [ٹرانسفارمر آرکیٹیکچر](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))، اور خاص طور پر [بی ای آر ٹی لینگویج ماڈلز](https://en.wikipedia.org/wiki/BERT_(language_model)) کہیں بہتر نتائج دکھاتے ہیں۔ پہلے سے تربیت یافتہ بی ای آر ٹی ماڈلز زبان کی عمومی ساخت کو سمجھتے ہیں اور انہیں مخصوص کاموں کے لیے نسبتاً چھوٹے ڈیٹا سیٹس اور کم کمپیوٹیشنل لاگت کے ساتھ فائن ٹیون کیا جا سکتا ہے۔

چونکہ ہم طبی منظرنامے پر این ای آر کو لاگو کرنے کا ارادہ رکھتے ہیں، اس لیے یہ سمجھ میں آتا ہے کہ طبی متون پر تربیت یافتہ بی ای آر ٹی ماڈل استعمال کیا جائے۔ مائیکروسافٹ ریسرچ نے ایک پہلے سے تربیت یافتہ ماڈل جاری کیا ہے جسے [پب میڈ بی ای آر ٹی][PubMedBERT] ([اشاعت][PubMedBERT-Pub]) کہا جاتا ہے، جو [پب میڈ](https://pubmed.ncbi.nlm.nih.gov/) ریپوزٹری کے متون کا استعمال کرتے ہوئے فائن ٹیون کیا گیا تھا۔

ٹرانسفارمر ماڈلز کو تربیت دینے کے لیے *ڈی فیکٹو* معیار [ہگنگ فیس ٹرانسفارمرز](https://huggingface.co/) لائبریری ہے۔ اس میں کمیونٹی کی طرف سے برقرار رکھے گئے پہلے سے تربیت یافتہ ماڈلز کا ایک ریپوزٹری بھی شامل ہے، جس میں پب میڈ بی ای آر ٹی بھی شامل ہے۔ اس ماڈل کو لوڈ اور استعمال کرنے کے لیے، ہمیں صرف چند لائنز کوڈ کی ضرورت ہے:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

یہ ہمیں `ماڈل` فراہم کرتا ہے، جو ٹوکن کلاسیفکیشن کے کام کے لیے بنایا گیا ہے اور `کلاسز` کی تعداد کے ساتھ، نیز `ٹوکنائزر` آبجیکٹ جو ان پٹ ٹیکسٹ کو ٹوکنز میں تقسیم کر سکتا ہے۔ آپ کو ڈیٹا سیٹ کو بائیو فارمیٹ میں تبدیل کرنا ہوگا، پب میڈ بی ای آر ٹی ٹوکنائزیشن کو مدنظر رکھتے ہوئے۔ آپ [اس پائتھون کوڈ کے ٹکڑے](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) کو بطور تحریک استعمال کر سکتے ہیں۔

## نتیجہ

یہ کام اصل کام کے بہت قریب ہے جو آپ کو ممکنہ طور پر کرنا ہوگا اگر آپ قدرتی زبان کے بڑے متون میں مزید بصیرت حاصل کرنا چاہتے ہیں۔ ہمارے معاملے میں، ہم اپنے تربیت یافتہ ماڈل کو [کووڈ سے متعلق پیپرز کے ڈیٹا سیٹ](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) پر لاگو کر سکتے ہیں اور دیکھ سکتے ہیں کہ ہم کون سی بصیرت حاصل کر سکتے ہیں۔ [یہ بلاگ پوسٹ](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) اور [یہ مقالہ](https://www.mdpi.com/2504-2289/6/1/4) اس کارپس آف پیپرز پر این ای آر کا استعمال کرتے ہوئے کی جانے والی تحقیق کو بیان کرتے ہیں۔

**ڈسکلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے پوری کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔