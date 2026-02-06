# تشخیص موجودیت‌های نام‌گذاری‌شده (NER)

تمرین آزمایشگاهی از [برنامه درسی هوش مصنوعی برای مبتدیان](https://github.com/microsoft/ai-for-beginners).

## وظیفه

در این آزمایشگاه، شما باید یک مدل تشخیص موجودیت‌های نام‌گذاری‌شده برای اصطلاحات پزشکی آموزش دهید.

## مجموعه داده

برای آموزش مدل NER، به یک مجموعه داده با برچسب‌گذاری مناسب برای موجودیت‌های پزشکی نیاز داریم. مجموعه داده [BC5CDR](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) شامل موجودیت‌های برچسب‌گذاری‌شده بیماری‌ها و مواد شیمیایی از بیش از ۱۵۰۰ مقاله است. شما می‌توانید این مجموعه داده را پس از ثبت‌نام در وب‌سایت آن‌ها دانلود کنید.

مجموعه داده BC5CDR به این شکل است:

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

در این مجموعه داده، عنوان مقاله و چکیده در دو خط اول قرار دارند و سپس موجودیت‌های جداگانه با موقعیت شروع و پایان در بلوک عنوان+چکیده مشخص شده‌اند. علاوه بر نوع موجودیت، شناسه آنتولوژی این موجودیت در یک آنتولوژی پزشکی نیز ارائه می‌شود.

شما باید مقداری کد پایتون بنویسید تا این داده‌ها را به فرمت BIO تبدیل کنید.

## شبکه

اولین تلاش برای NER می‌تواند با استفاده از شبکه LSTM انجام شود، همان‌طور که در مثال ارائه‌شده در درس مشاهده کردید. با این حال، در وظایف پردازش زبان طبیعی، [معماری ترنسفورمر](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model)) و به‌ویژه [مدل‌های زبانی BERT](https://en.wikipedia.org/wiki/BERT_(language_model)) نتایج بسیار بهتری نشان می‌دهند. مدل‌های از پیش آموزش‌دیده BERT ساختار کلی زبان را درک می‌کنند و می‌توانند با مجموعه داده‌های نسبتاً کوچک و هزینه‌های محاسباتی کم برای وظایف خاص تنظیم شوند.

از آنجا که قصد داریم NER را در سناریوی پزشکی اعمال کنیم، منطقی است که از مدل BERT آموزش‌دیده بر روی متون پزشکی استفاده کنیم. مایکروسافت ریسرچ یک مدل از پیش آموزش‌دیده به نام [PubMedBERT][PubMedBERT] ([مقاله][PubMedBERT-Pub]) منتشر کرده است که با استفاده از متون موجود در مخزن [PubMed](https://pubmed.ncbi.nlm.nih.gov/) تنظیم شده است.

استاندارد *de facto* برای آموزش مدل‌های ترنسفورمر، کتابخانه [Hugging Face Transformers](https://huggingface.co/) است. این کتابخانه همچنین شامل یک مخزن از مدل‌های از پیش آموزش‌دیده توسط جامعه، از جمله PubMedBERT، می‌باشد. برای بارگذاری و استفاده از این مدل، تنها به چند خط کد نیاز دارید:

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

این کد به ما `model` را می‌دهد که برای وظیفه طبقه‌بندی توکن با استفاده از تعداد `classes` کلاس ساخته شده است، و همچنین شیء `tokenizer` که می‌تواند متن ورودی را به توکن‌ها تقسیم کند. شما باید مجموعه داده را به فرمت BIO تبدیل کنید و توکن‌سازی PubMedBERT را در نظر بگیرید. می‌توانید از [این قطعه کد پایتون](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) به‌عنوان الهام استفاده کنید.

## نتیجه‌گیری

این وظیفه بسیار نزدیک به وظایف واقعی است که احتمالاً در صورت تمایل به کسب بینش بیشتر از حجم زیادی از متون زبان طبیعی با آن مواجه خواهید شد. در مورد ما، می‌توانیم مدل آموزش‌دیده خود را بر روی [مجموعه داده مقالات مرتبط با COVID](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge) اعمال کنیم و ببینیم چه بینش‌هایی می‌توانیم به دست آوریم. [این پست وبلاگ](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) و [این مقاله](https://www.mdpi.com/2504-2289/6/1/4) تحقیقاتی را که می‌توان بر روی این مجموعه مقالات با استفاده از NER انجام داد، توصیف می‌کنند.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.