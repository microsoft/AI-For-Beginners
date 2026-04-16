# تشخیص سر با استفاده از مجموعه داده Hollywood Heads

تمرین آزمایشگاهی از [برنامه درسی AI for Beginners](https://github.com/microsoft/ai-for-beginners).

## وظیفه

شمارش تعداد افراد در جریان دوربین نظارتی یک وظیفه مهم است که به ما امکان می‌دهد تعداد بازدیدکنندگان در فروشگاه‌ها، ساعات شلوغی در رستوران‌ها و غیره را تخمین بزنیم. برای حل این وظیفه، باید بتوانیم سر انسان را از زوایای مختلف تشخیص دهیم. برای آموزش مدل تشخیص اشیا برای تشخیص سر انسان، می‌توانیم از [مجموعه داده Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/) استفاده کنیم.

## مجموعه داده

[مجموعه داده Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) شامل 369,846 سر انسان است که در 224,740 فریم فیلم‌های هالیوودی علامت‌گذاری شده‌اند. این مجموعه داده در قالب [PASCAL VOC](https://host.robots.ox.ac.uk/pascal/VOC/) ارائه شده است، که برای هر تصویر یک فایل توضیحات XML نیز وجود دارد که به این شکل است:

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

در این مجموعه داده، فقط یک کلاس از اشیا وجود دارد `head`، و برای هر سر، مختصات جعبه محدودکننده ارائه می‌شود. شما می‌توانید فایل‌های XML را با استفاده از کتابخانه‌های پایتون تجزیه کنید، یا از [این کتابخانه](https://pypi.org/project/pascal-voc/) برای کار مستقیم با قالب PASCAL VOC استفاده کنید.

## آموزش مدل تشخیص اشیا

شما می‌توانید مدل تشخیص اشیا را به یکی از روش‌های زیر آموزش دهید:

* استفاده از [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) و API پایتون آن برای آموزش مدل به صورت برنامه‌ریزی شده در فضای ابری. Custom Vision نمی‌تواند از بیش از چند صد تصویر برای آموزش مدل استفاده کند، بنابراین ممکن است نیاز باشد مجموعه داده را محدود کنید.
* استفاده از مثال موجود در [آموزش Keras](https://keras.io/examples/vision/retinanet/) برای آموزش مدل RetunaNet.
* استفاده از ماژول داخلی [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) در torchvision.

## نتیجه‌گیری

تشخیص اشیا یک وظیفه است که اغلب در صنعت مورد نیاز است. در حالی که برخی خدمات وجود دارند که می‌توانند برای انجام تشخیص اشیا استفاده شوند (مانند [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste))، مهم است که درک کنید چگونه تشخیص اشیا کار می‌کند و بتوانید مدل‌های خود را آموزش دهید.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.