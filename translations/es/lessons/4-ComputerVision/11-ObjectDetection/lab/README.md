# Detección de Cabezas usando el Conjunto de Datos de Hollywood

Tarea del [Currículo de IA para Principiantes](https://github.com/microsoft/ai-for-beginners).

## Tarea

Contar el número de personas en el flujo de cámaras de vigilancia es una tarea importante que nos permitirá estimar el número de visitantes en tiendas, horas pico en un restaurante, etc. Para resolver esta tarea, necesitamos ser capaces de detectar cabezas humanas desde diferentes ángulos. Para entrenar un modelo de detección de objetos que detecte cabezas humanas, podemos utilizar el [Conjunto de Datos de Hollywood](https://www.di.ens.fr/willow/research/headdetection/).

## El Conjunto de Datos

El [Conjunto de Datos de Hollywood](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) contiene 369,846 cabezas humanas anotadas en 224,740 fotogramas de películas de Hollywood. Se proporciona en formato [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), donde para cada imagen también hay un archivo de descripción XML que se ve así:

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

En este conjunto de datos, solo hay una clase de objetos `head`, y para cada cabeza, obtienes las coordenadas de la caja delimitadora. Puedes analizar XML usando bibliotecas de Python, o usar [esta biblioteca](https://pypi.org/project/pascal-voc/) para trabajar directamente con el formato PASCAL VOC.

## Entrenamiento de Detección de Objetos

Puedes entrenar un modelo de detección de objetos usando una de las siguientes maneras:

* Usando [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) y su API de Python para entrenar programáticamente el modelo en la nube. La visión personalizada no podrá usar más de unas pocas centenas de imágenes para entrenar el modelo, por lo que es posible que necesites limitar el conjunto de datos.
* Usando el ejemplo del [tutorial de Keras](https://keras.io/examples/vision/retinanet/) para entrenar el modelo RetinaNet.
* Usando el módulo integrado [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) en torchvision.

## Conclusión

La detección de objetos es una tarea que se requiere con frecuencia en la industria. Aunque hay algunos servicios que se pueden utilizar para realizar la detección de objetos (como [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), es importante entender cómo funciona la detección de objetos y poder entrenar tus propios modelos.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.