# Обнаружение голов с использованием набора данных Hollywood Heads

Лабораторная работа из [Курса AI для начинающих](https://github.com/microsoft/ai-for-beginners).

## Задача

Подсчет количества людей на потоке видеонаблюдения — это важная задача, которая позволит нам оценить количество посетителей в магазинах, часы пик в ресторане и т. д. Для решения этой задачи нам нужно уметь обнаруживать человеческие головы под разными углами. Чтобы обучить модель обнаружения объектов для выявления человеческих голов, мы можем использовать [набор данных Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/).

## Набор данных

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) содержит 369,846 аннотированных человеческих голов в 224,740 кадрах фильмов из Голливуда. Он представлен в формате [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), где для каждого изображения также есть XML файл описания, который выглядит следующим образом:

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

В этом наборе данных есть только один класс объектов `head`, и для каждой головы вы получаете координаты ограничивающего прямоугольника. Вы можете разобрать XML с помощью библиотек Python или использовать [эту библиотеку](https://pypi.org/project/pascal-voc/), чтобы работать непосредственно с форматом PASCAL VOC.

## Обучение обнаружения объектов

Вы можете обучить модель обнаружения объектов одним из следующих способов:

* Используя [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) и его Python API для программного обучения модели в облаке. Custom Vision не сможет использовать более нескольких сотен изображений для обучения модели, поэтому вам может потребоваться ограничить набор данных.
* Используя пример из [учебника Keras](https://keras.io/examples/vision/retinanet/) для обучения модели RetinaNet.
* Используя встроенный модуль [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) в torchvision.

## Основные выводы

Обнаружение объектов — это задача, которая часто требуется в промышленности. Хотя существуют некоторые сервисы, которые можно использовать для выполнения обнаружения объектов (такие как [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), важно понимать, как работает обнаружение объектов и уметь обучать собственные модели.

**Отказ от ответственности**:  
Этот документ был переведен с использованием услуг машинного перевода на основе ИИ. Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на родном языке должен считаться авторитетным источником. Для критически важной информации рекомендуется профессиональный человеческий перевод. Мы не несем ответственности за любые недоразумения или неверные истолкования, возникающие в результате использования этого перевода.