# Детекција глава уз помоћ Hollywood Heads Dataset-а

Лабораторијски задатак из [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Задатак

Бројање људи на видео стриму са надзорних камера је важан задатак који нам омогућава да проценимо број посетилаца у продавницама, најпрометније сате у ресторану, итд. Да бисмо решили овај задатак, потребно је да будемо у могућности да детектујемо људске главе из различитих углова. За тренирање модела за детекцију објеката који детектује људске главе, можемо користити [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## О датасету

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) садржи 369,846 људских глава означених у 224,740 кадрова из холивудских филмова. Датасет је доступан у формату [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), где за сваку слику постоји XML датотека са описом која изгледа овако:

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

У овом датасету постоји само једна класа објеката `head`, и за сваку главу добијате координате оквирне кутије (bounding box). XML можете парсирати уз помоћ Python библиотека, или користити [ову библиотеку](https://pypi.org/project/pascal-voc/) за директан рад са PASCAL VOC форматом.

## Тренирање модела за детекцију објеката

Можете тренирати модел за детекцију објеката на један од следећих начина:

* Уз помоћ [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) и његовог Python API-ја за програмско тренирање модела у облаку. Custom Vision неће моћи да користи више од неколико стотина слика за тренирање модела, па ћете можда морати да ограничите датасет.
* Уз помоћ примера из [Keras туторијала](https://keras.io/examples/vision/retinanet/) за тренирање RetinaNet модела.
* Уз помоћ [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) уграђеног модула у torchvision.

## Закључак

Детекција објеката је задатак који се често захтева у индустрији. Иако постоје услуге које се могу користити за извршавање детекције објеката (као што је [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), важно је разумети како детекција објеката функционише и бити у могућности да тренирате сопствене моделе.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.