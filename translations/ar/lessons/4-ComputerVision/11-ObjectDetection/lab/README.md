# الكشف عن الرؤوس باستخدام مجموعة بيانات Hollywood Heads

مهمة مختبر من [منهج الذكاء الاصطناعي للمبتدئين](https://github.com/microsoft/ai-for-beginners).

## المهمة

عدّ عدد الأشخاص في بث كاميرا المراقبة هو مهمة مهمة تتيح لنا تقدير عدد الزوار في المتاجر، وساعات الذروة في المطاعم، وما إلى ذلك. لحل هذه المهمة، نحتاج إلى القدرة على الكشف عن رؤوس البشر من زوايا مختلفة. لتدريب نموذج الكشف عن الكائنات للكشف عن رؤوس البشر، يمكننا استخدام [مجموعة بيانات Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/).

## مجموعة البيانات

[مجموعة بيانات Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) تحتوي على 369,846 رأسًا بشريًا تم وضع علامات عليها في 224,740 إطارًا من أفلام هوليوود. يتم تقديمها بتنسيق [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC)، حيث لكل صورة يوجد أيضًا ملف وصف XML يبدو كالتالي:

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

في هذه المجموعة، هناك فئة واحدة فقط من الكائنات وهي `head`، ولكل رأس تحصل على إحداثيات صندوق الإحاطة. يمكنك تحليل ملفات XML باستخدام مكتبات Python، أو استخدام [هذه المكتبة](https://pypi.org/project/pascal-voc/) للتعامل مباشرة مع تنسيق PASCAL VOC.

## تدريب نموذج الكشف عن الكائنات

يمكنك تدريب نموذج الكشف عن الكائنات باستخدام إحدى الطرق التالية:

* استخدام [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) وواجهة برمجة التطبيقات الخاصة به في Python لتدريب النموذج برمجيًا في السحابة. لن يتمكن Custom Vision من استخدام أكثر من بضع مئات من الصور لتدريب النموذج، لذا قد تحتاج إلى تقليل حجم مجموعة البيانات.
* استخدام المثال من [دليل Keras](https://keras.io/examples/vision/retinanet/) لتدريب نموذج RetunaNet.
* استخدام [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) الوحدة المدمجة في مكتبة torchvision.

## الخلاصة

الكشف عن الكائنات هو مهمة مطلوبة بشكل متكرر في الصناعة. بينما توجد بعض الخدمات التي يمكن استخدامها لتنفيذ الكشف عن الكائنات (مثل [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste))، من المهم فهم كيفية عمل الكشف عن الكائنات والقدرة على تدريب نماذجك الخاصة.

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الموثوق. للحصول على معلومات حساسة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.