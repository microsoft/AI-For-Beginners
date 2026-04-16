# Hoofddetectie met behulp van Hollywood Heads Dataset

Practicumopdracht uit de [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Opdracht

Het tellen van het aantal mensen op een videobewakingsstroom is een belangrijke taak die ons in staat stelt om het aantal bezoekers in winkels, drukke uren in een restaurant, enz. te schatten. Om deze taak op te lossen, moeten we in staat zijn om menselijke hoofden vanuit verschillende hoeken te detecteren. Om een objectdetectiemodel te trainen dat menselijke hoofden kan detecteren, kunnen we gebruik maken van de [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## De Dataset

De [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) bevat 369.846 menselijke hoofden die zijn geannoteerd in 224.740 filmframes uit Hollywoodfilms. Het wordt geleverd in [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC)-formaat, waarbij voor elke afbeelding ook een XML-beschrijvingsbestand aanwezig is dat er als volgt uitziet:

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

In deze dataset is er slechts één klasse van objecten, `head`, en voor elk hoofd krijg je de coördinaten van de begrenzingsvak. Je kunt XML parseren met behulp van Python-bibliotheken, of je kunt [deze bibliotheek](https://pypi.org/project/pascal-voc/) gebruiken om direct met het PASCAL VOC-formaat te werken.

## Objectdetectie trainen

Je kunt een objectdetectiemodel trainen met een van de volgende methoden:

* Gebruik maken van [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) en de Python API om het model in de cloud programmeerbaar te trainen. Custom Vision kan niet meer dan een paar honderd afbeeldingen gebruiken om het model te trainen, dus je moet mogelijk de dataset beperken.
* Gebruik maken van het voorbeeld uit de [Keras-tutorial](https://keras.io/examples/vision/retinanet/) om een RetunaNet-model te trainen.
* Gebruik maken van de [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) ingebouwde module in torchvision.

## Belangrijkste punten

Objectdetectie is een taak die vaak vereist is in de industrie. Hoewel er enkele diensten zijn die kunnen worden gebruikt om objectdetectie uit te voeren (zoals [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), is het belangrijk om te begrijpen hoe objectdetectie werkt en om in staat te zijn je eigen modellen te trainen.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, willen we u erop wijzen dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.