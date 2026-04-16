# ہیڈ ڈیٹیکشن ہالی ووڈ ہیڈز ڈیٹاسیٹ کے ذریعے

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) سے لیب اسائنمنٹ۔

## کام

ویڈیو سرویلنس کیمرا اسٹریم پر لوگوں کی تعداد گننا ایک اہم کام ہے، جو ہمیں دکانوں میں آنے والے وزیٹرز کی تعداد، ریسٹورنٹ کے مصروف اوقات وغیرہ کا اندازہ لگانے میں مدد دے سکتا ہے۔ اس کام کو حل کرنے کے لیے، ہمیں مختلف زاویوں سے انسانی سروں کو ڈیٹیکٹ کرنے کے قابل ہونا چاہیے۔ انسانی سروں کو ڈیٹیکٹ کرنے کے لیے آبجیکٹ ڈیٹیکشن ماڈل کو تربیت دینے کے لیے، ہم [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/) استعمال کر سکتے ہیں۔

## ڈیٹاسیٹ

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) میں 369,846 انسانی سروں کی اینوٹیشنز شامل ہیں، جو ہالی ووڈ فلموں کے 224,740 فریمز پر مشتمل ہیں۔ یہ [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) فارمیٹ میں فراہم کیا گیا ہے، جہاں ہر تصویر کے ساتھ ایک XML تفصیل فائل بھی موجود ہوتی ہے، جو کچھ اس طرح نظر آتی ہے:

```xml
<annotation>
	<folder>HollywoodHeads</folder>
	<filename>mov_021_149390.jpeg</filename>
	<source>
		<database>HollywoodHeads 2015 Database</database>
		<annotation>HollywoodHeads 2015</annotation>
		<image>WILLOW</image>
	</source>
	<size>
		<width>608</width>
		<height>320</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>head</name>
		<bndbox>
			<xmin>201</xmin>
			<ymin>1</ymin>
			<xmax>480</xmax>
			<ymax>263</ymax>
		</bndbox>
		<difficult>0</difficult>
	</object>
	<object>
		<name>head</name>
		<bndbox>
			<xmin>3</xmin>
			<ymin>4</ymin>
			<xmax>241</xmax>
			<ymax>285</ymax>
		</bndbox>
		<difficult>0</difficult>
	</object>
</annotation>
```

اس ڈیٹاسیٹ میں صرف ایک قسم کی آبجیکٹ کلاس `head` ہے، اور ہر سر کے لیے آپ کو باؤنڈنگ باکس کے کوآرڈینیٹس ملتے ہیں۔ آپ XML کو Python لائبریریز کے ذریعے پارس کر سکتے ہیں، یا [اس لائبریری](https://pypi.org/project/pascal-voc/) کا استعمال کر سکتے ہیں جو PASCAL VOC فارمیٹ کے ساتھ براہ راست کام کرنے کے لیے ہے۔

## آبجیکٹ ڈیٹیکشن کی تربیت

آپ آبجیکٹ ڈیٹیکشن ماڈل کو درج ذیل طریقوں میں سے کسی ایک کے ذریعے تربیت دے سکتے ہیں:

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) اور اس کے Python API کا استعمال کرتے ہوئے کلاؤڈ میں ماڈل کو پروگرام کے ذریعے تربیت دیں۔ Custom Vision چند سو تصاویر سے زیادہ ڈیٹاسیٹ کو تربیت دینے کے لیے استعمال نہیں کر سکتا، اس لیے آپ کو ڈیٹاسیٹ کو محدود کرنا پڑ سکتا ہے۔
* [Keras tutorial](https://keras.io/examples/vision/retinanet/) کی مثال کا استعمال کرتے ہوئے RetunaNet ماڈل کو تربیت دیں۔
* [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) کے torchvision میں موجود بلٹ ان ماڈیول کا استعمال کریں۔

## نتیجہ

آبجیکٹ ڈیٹیکشن ایک ایسا کام ہے جو صنعت میں اکثر درکار ہوتا ہے۔ اگرچہ کچھ سروسز موجود ہیں جو آبجیکٹ ڈیٹیکشن انجام دینے کے لیے استعمال کی جا سکتی ہیں (جیسے [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste))، یہ سمجھنا ضروری ہے کہ آبجیکٹ ڈیٹیکشن کیسے کام کرتا ہے اور اپنے ماڈلز کو تربیت دینے کے قابل ہونا چاہیے۔

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ ہم درستگی کے لیے کوشش کرتے ہیں، لیکن براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگی ہو سکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔