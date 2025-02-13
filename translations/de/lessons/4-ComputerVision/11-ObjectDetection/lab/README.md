# Kopfdetektion mit dem Hollywood Heads Dataset

Laboraufgabe aus dem [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Aufgabe

Die Zählung der Anzahl von Personen im Videoüberwachungs-Kamerastream ist eine wichtige Aufgabe, die es uns ermöglicht, die Anzahl der Besucher in Geschäften, Stoßzeiten in einem Restaurant usw. zu schätzen. Um diese Aufgabe zu lösen, müssen wir in der Lage sein, menschliche Köpfe aus verschiedenen Blickwinkeln zu erkennen. Um ein Objekt-Erkennungsmodell zur Erkennung menschlicher Köpfe zu trainieren, können wir das [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/) verwenden.

## Das Dataset

Das [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) enthält 369.846 menschliche Köpfe, die in 224.740 Filmframes aus Hollywood-Filmen annotiert sind. Es wird im [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) Format bereitgestellt, wobei für jedes Bild auch eine XML-Beschreibungsdatei vorhanden ist, die so aussieht:

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

In diesem Dataset gibt es nur eine Klasse von Objekten `head`, und für jeden Kopf erhältst du die Koordinaten des Begrenzungsrahmens. Du kannst XML mit Python-Bibliotheken parsen oder [diese Bibliothek](https://pypi.org/project/pascal-voc/) verwenden, um direkt mit dem PASCAL VOC-Format zu arbeiten.

## Training der Objekterkennung

Du kannst ein Objekt-Erkennungsmodell auf eine der folgenden Arten trainieren:

* Verwende [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) und dessen Python-API, um das Modell programmgesteuert in der Cloud zu trainieren. Die benutzerdefinierte Vision kann nicht mehr als einige hundert Bilder für das Training des Modells verwenden, daher musst du das Dataset möglicherweise einschränken.
* Verwende das Beispiel aus dem [Keras-Tutorial](https://keras.io/examples/vision/retinanet/), um das RetunaNet-Modell zu trainieren.
* Verwende das eingebaute Modul [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) in torchvision.

## Fazit

Die Objekterkennung ist eine Aufgabe, die in der Industrie häufig erforderlich ist. Während es einige Dienste gibt, die zur Durchführung der Objekterkennung verwendet werden können (wie [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), ist es wichtig zu verstehen, wie Objekterkennung funktioniert und in der Lage zu sein, eigene Modelle zu trainieren.

**Haftungsausschluss**:  
Dieses Dokument wurde mit maschinellen KI-Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als die maßgebliche Quelle angesehen werden. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Verantwortung für Missverständnisse oder Fehlinterpretationen, die aus der Verwendung dieser Übersetzung entstehen.