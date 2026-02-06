# Kopferkennung mit dem Hollywood Heads Dataset

Laboraufgabe aus dem [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Aufgabe

Das Zählen der Anzahl von Personen in einem Videoüberwachungsstream ist eine wichtige Aufgabe, die es uns ermöglicht, die Anzahl der Besucher in Geschäften, Stoßzeiten in Restaurants usw. zu schätzen. Um diese Aufgabe zu lösen, müssen wir in der Lage sein, menschliche Köpfe aus verschiedenen Blickwinkeln zu erkennen. Um ein Objekterkennungsmodell zu trainieren, das menschliche Köpfe erkennt, können wir das [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/) verwenden.

## Das Dataset

Das [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) enthält 369.846 menschliche Köpfe, die in 224.740 Filmframes aus Hollywood-Filmen annotiert sind. Es wird im [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC)-Format bereitgestellt, bei dem es zu jedem Bild auch eine XML-Beschreibungsdatei gibt, die so aussieht:

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

In diesem Datensatz gibt es nur eine Objektklasse `head`, und für jeden Kopf erhält man die Koordinaten des Begrenzungsrahmens. Sie können XML mit Python-Bibliotheken analysieren oder [diese Bibliothek](https://pypi.org/project/pascal-voc/) verwenden, um direkt mit dem PASCAL VOC-Format zu arbeiten.

## Training der Objekterkennung

Sie können ein Objekterkennungsmodell auf eine der folgenden Arten trainieren:

* Mit [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) und dessen Python-API, um das Modell programmgesteuert in der Cloud zu trainieren. Custom Vision kann jedoch nicht mehr als ein paar hundert Bilder für das Training des Modells verwenden, sodass Sie den Datensatz möglicherweise begrenzen müssen.
* Mit dem Beispiel aus dem [Keras-Tutorial](https://keras.io/examples/vision/retinanet/), um ein RetunaNet-Modell zu trainieren.
* Mit dem [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)-Modul, das in torchvision integriert ist.

## Fazit

Die Objekterkennung ist eine Aufgabe, die in der Industrie häufig benötigt wird. Während es einige Dienste gibt, die zur Durchführung der Objekterkennung verwendet werden können (wie z. B. [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), ist es wichtig zu verstehen, wie Objekterkennung funktioniert, und in der Lage zu sein, eigene Modelle zu trainieren.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.