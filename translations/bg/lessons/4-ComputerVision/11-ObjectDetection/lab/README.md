# Откриване на глави с помощта на Hollywood Heads Dataset

Лабораторно упражнение от [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Задача

Броенето на хора в потока от видеонаблюдение е важна задача, която ни позволява да оценим броя на посетителите в магазини, натоварените часове в ресторанти и др. За да решим тази задача, трябва да можем да откриваме човешки глави от различни ъгли. За да обучим модел за откриване на обекти, който да разпознава човешки глави, можем да използваме [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Данните

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) съдържа 369,846 човешки глави, анотирани в 224,740 кадъра от холивудски филми. Данните са предоставени във формат [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), където за всяко изображение има XML файл с описание, който изглежда така:

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

В този набор от данни има само един клас обекти `head`, и за всяка глава се предоставят координатите на ограничителната кутия. Можете да парсирате XML с помощта на Python библиотеки или да използвате [тази библиотека](https://pypi.org/project/pascal-voc/), за да работите директно с формата PASCAL VOC.

## Обучение на модел за откриване на обекти

Можете да обучите модел за откриване на обекти по един от следните начини:

* С помощта на [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) и неговия Python API, за да обучите модела програмно в облака. Custom Vision няма да може да използва повече от няколкостотин изображения за обучение на модела, така че може да се наложи да ограничите набора от данни.
* С помощта на примера от [Keras tutorial](https://keras.io/examples/vision/retinanet/), за да обучите модел RetunaNet.
* С помощта на вградения модул [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) в torchvision.

## Изводи

Откриването на обекти е задача, която често се изисква в индустрията. Въпреки че съществуват услуги, които могат да се използват за откриване на обекти (като [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), е важно да разберем как работи откриването на обекти и да можем да обучаваме собствени модели.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI услуга за превод [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за недоразумения или погрешни интерпретации, произтичащи от използването на този превод.