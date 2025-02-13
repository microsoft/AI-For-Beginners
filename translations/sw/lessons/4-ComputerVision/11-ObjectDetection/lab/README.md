# Huvuddetektering med Hollywood Heads Dataset

Laborationsuppgift från [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Uppgift

Att räkna antalet personer på en videoövervakningskamerastream är en viktig uppgift som gör att vi kan uppskatta antalet besökare i butiker, hektiska timmar på en restaurang, osv. För att lösa denna uppgift behöver vi kunna detektera mänskliga huvuden från olika vinklar. För att träna en objektdetekteringsmodell för att upptäcka mänskliga huvuden kan vi använda [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Datasetet

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) innehåller 369,846 mänskliga huvuden annoterade i 224,740 filmrutor från Hollywood-filmer. Det tillhandahålls i [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) format, där det för varje bild också finns en XML-beskrivningsfil som ser ut så här:

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

I detta dataset finns det endast en klass av objekt `head`, och för varje huvud får du koordinaterna för bounding box. Du kan analysera XML med hjälp av Python-bibliotek, eller använda [detta bibliotek](https://pypi.org/project/pascal-voc/) för att hantera PASCAL VOC-formatet direkt.

## Träning av Objektdetektion

Du kan träna en objektdetekteringsmodell på följande sätt:

* Använda [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) och dess Python-API för att programmera träningen av modellen i molnet. Custom Vision kommer inte att kunna använda mer än några hundra bilder för att träna modellen, så du kan behöva begränsa datasetet.
* Använda exemplet från [Keras tutorial](https://keras.io/examples/vision/retinanet/) för att träna RetunaNet-modellen.
* Använda [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) inbyggda modul i torchvision.

## Sammanfattning

Objektdetektion är en uppgift som ofta krävs inom industrin. Även om det finns vissa tjänster som kan användas för att utföra objektdetektion (såsom [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), är det viktigt att förstå hur objektdetektion fungerar och att kunna träna sina egna modeller.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.