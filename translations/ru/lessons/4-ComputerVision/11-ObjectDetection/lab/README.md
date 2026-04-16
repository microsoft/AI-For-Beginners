# Определение голов с использованием набора данных Hollywood Heads

Лабораторное задание из [курса "Искусственный интеллект для начинающих"](https://github.com/microsoft/ai-for-beginners).

## Задача

Подсчет количества людей на видеопотоке с камер наблюдения — важная задача, которая позволяет оценить количество посетителей в магазинах, часы пик в ресторанах и т.д. Для решения этой задачи необходимо уметь определять человеческие головы с разных ракурсов. Чтобы обучить модель обнаружения объектов для определения человеческих голов, можно использовать [набор данных Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/).

## Набор данных

[Набор данных Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) содержит 369,846 аннотированных человеческих голов в 224,740 кадрах из голливудских фильмов. Он предоставляется в формате [PASCAL VOC](https://host.robots.ox.ac.uk/pascal/VOC/), где для каждого изображения также есть XML-файл описания, который выглядит следующим образом:

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

В этом наборе данных есть только один класс объектов — `head`, и для каждой головы указаны координаты ограничивающего прямоугольника. Вы можете анализировать XML с помощью библиотек Python или использовать [эту библиотеку](https://pypi.org/project/pascal-voc/) для работы напрямую с форматом PASCAL VOC.

## Обучение модели обнаружения объектов

Вы можете обучить модель обнаружения объектов одним из следующих способов:

* Используя [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) и его Python API для программного обучения модели в облаке. Custom Vision не сможет использовать более нескольких сотен изображений для обучения модели, поэтому, возможно, вам придется ограничить набор данных.
* Используя пример из [Keras tutorial](https://keras.io/examples/vision/retinanet/) для обучения модели RetunaNet.
* Используя встроенный модуль [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) в torchvision.

## Выводы

Обнаружение объектов — это задача, которая часто требуется в промышленности. Хотя существуют сервисы, которые можно использовать для выполнения обнаружения объектов (например, [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), важно понимать, как работает обнаружение объектов, и уметь обучать собственные модели.

**Отказ от ответственности**:  
Этот документ был переведен с использованием сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия обеспечить точность, автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.