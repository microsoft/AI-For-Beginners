# Виявлення голів за допомогою набору даних Hollywood Heads

Лабораторна робота з [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Завдання

Підрахунок кількості людей на відеопотоці з камер спостереження є важливим завданням, яке дозволяє оцінити кількість відвідувачів у магазинах, години найбільшого завантаження в ресторанах тощо. Для вирішення цього завдання необхідно вміти виявляти людські голови з різних ракурсів. Щоб навчити модель для виявлення об'єктів розпізнавати людські голови, можна використовувати [набір даних Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/).

## Набір даних

[Набір даних Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) містить 369,846 людських голів, анотованих у 224,740 кадрах із голлівудських фільмів. Він надається у форматі [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), де для кожного зображення є XML-файл опису, який виглядає так:

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

У цьому наборі даних є лише один клас об'єктів `head`, і для кожної голови вказуються координати обмежувального прямокутника. Ви можете обробляти XML за допомогою бібліотек Python або скористатися [цією бібліотекою](https://pypi.org/project/pascal-voc/) для роботи безпосередньо з форматом PASCAL VOC.

## Навчання моделі для виявлення об'єктів

Ви можете навчити модель для виявлення об'єктів одним із наступних способів:

* Використовуючи [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) та його Python API для програмного навчання моделі в хмарі. Custom Vision не зможе використовувати більше кількох сотень зображень для навчання моделі, тому, можливо, доведеться обмежити набір даних.
* Використовуючи приклад із [Keras tutorial](https://keras.io/examples/vision/retinanet/) для навчання моделі RetunaNet.
* Використовуючи вбудований модуль [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) у torchvision.

## Висновок

Виявлення об'єктів — це завдання, яке часто зустрічається в індустрії. Хоча існують сервіси, які можна використовувати для виявлення об'єктів (наприклад, [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), важливо розуміти, як працює виявлення об'єктів, і вміти навчати власні моделі.

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, зверніть увагу, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ на його рідній мові слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний людський переклад. Ми не несемо відповідальності за будь-які непорозуміння або неправильні тлумачення, що виникли внаслідок використання цього перекладу.