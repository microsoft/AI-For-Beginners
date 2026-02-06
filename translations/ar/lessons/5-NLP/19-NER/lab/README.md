# التعرف على الكيانات المسماة (NER)

مهمة معملية من [منهج الذكاء الاصطناعي للمبتدئين](https://github.com/microsoft/ai-for-beginners).

## المهمة

في هذا المعمل، تحتاج إلى تدريب نموذج للتعرف على الكيانات المسماة للمصطلحات الطبية.

## مجموعة البيانات

لتدريب نموذج NER، نحتاج إلى مجموعة بيانات مُعلمة بشكل صحيح تحتوي على الكيانات الطبية. [مجموعة بيانات BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) تحتوي على كيانات الأمراض والمواد الكيميائية المعلمة من أكثر من 1500 ورقة بحثية. يمكنك تنزيل مجموعة البيانات بعد التسجيل في موقعهم.

تبدو مجموعة بيانات BC5CDR كما يلي:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

في هذه المجموعة، توجد عناوين الأوراق البحثية والملخصات في السطرين الأولين، ثم تظهر الكيانات الفردية مع مواضع البداية والنهاية داخل كتلة العنوان + الملخص. بالإضافة إلى نوع الكيان، تحصل على معرف الأنطولوجيا لهذا الكيان ضمن أنطولوجيا طبية معينة.

ستحتاج إلى كتابة بعض الأكواد بلغة Python لتحويل هذه البيانات إلى ترميز BIO.

## الشبكة

يمكن إجراء المحاولة الأولى للتعرف على الكيانات المسماة باستخدام شبكة LSTM، كما رأيت في المثال أثناء الدرس. ومع ذلك، في مهام معالجة اللغة الطبيعية، تظهر [بنية المحولات](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))، وخاصة [نماذج BERT اللغوية](https://en.wikipedia.org/wiki/BERT_(language_model))، نتائج أفضل بكثير. النماذج المدربة مسبقًا من BERT تفهم البنية العامة للغة، ويمكن تحسينها لمهام محددة باستخدام مجموعات بيانات صغيرة نسبيًا وتكاليف حسابية منخفضة.

نظرًا لأننا نخطط لتطبيق NER في سيناريو طبي، فمن المنطقي استخدام نموذج BERT مدرب على نصوص طبية. أصدرت Microsoft Research نموذجًا مدربًا مسبقًا يسمى [PubMedBERT][PubMedBERT] ([النشر][PubMedBERT-Pub])، والذي تم تحسينه باستخدام نصوص من مستودع [PubMed](https://pubmed.ncbi.nlm.nih.gov/).

المعيار الفعلي لتدريب نماذج المحولات هو مكتبة [Hugging Face Transformers](https://huggingface.co/). تحتوي هذه المكتبة أيضًا على مستودع للنماذج المدربة مسبقًا التي يتم صيانتها من قبل المجتمع، بما في ذلك PubMedBERT. لتحميل واستخدام هذا النموذج، نحتاج فقط إلى بضعة أسطر من الكود:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

هذا يوفر لنا `model` نفسه، المصمم لمهمة تصنيف الرموز باستخدام عدد `classes` من الفئات، بالإضافة إلى كائن `tokenizer` الذي يمكنه تقسيم النص المدخل إلى رموز. ستحتاج إلى تحويل مجموعة البيانات إلى تنسيق BIO، مع أخذ تقسيم الرموز الخاص بـ PubMedBERT في الاعتبار. يمكنك استخدام [هذا الجزء من كود Python](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) كمصدر إلهام.

## الخلاصة

هذه المهمة قريبة جدًا من المهمة الفعلية التي من المحتمل أن تواجهها إذا كنت ترغب في الحصول على رؤى أعمق من كميات كبيرة من النصوص الطبيعية. في حالتنا، يمكننا تطبيق النموذج المدرب على [مجموعة بيانات الأوراق البحثية المتعلقة بـ COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) ورؤية الأفكار التي يمكننا استخراجها. [هذا المنشور](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) و[هذه الورقة البحثية](https://www.mdpi.com/2504-2289/6/1/4) يصفان الأبحاث التي يمكن إجراؤها على هذا المجموع من الأوراق باستخدام NER.

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.