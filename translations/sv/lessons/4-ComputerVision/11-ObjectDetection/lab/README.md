# Huvuddetektion med Hollywood Heads Dataset

Labuppgift från [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Uppgift

Att räkna antalet personer på en videoström från övervakningskameror är en viktig uppgift som gör det möjligt att uppskatta antalet besökare i butiker, rusningstider på restauranger, etc. För att lösa denna uppgift behöver vi kunna detektera mänskliga huvuden från olika vinklar. För att träna en objektidentifieringsmodell att detektera mänskliga huvuden kan vi använda [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Datasetet

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) innehåller 369,846 mänskliga huvuden annoterade i 224,740 filmrutor från Hollywoodfilmer. Det tillhandahålls i [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC)-format, där det för varje bild också finns en XML-beskrivningsfil som ser ut så här:

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

I detta dataset finns det endast en klass av objekt, `head`, och för varje huvud får du koordinaterna för begränsningsrutan. Du kan analysera XML med Python-bibliotek, eller använda [detta bibliotek](https://pypi.org/project/pascal-voc/) för att direkt hantera PASCAL VOC-formatet.

## Träning av objektidentifiering

Du kan träna en objektidentifieringsmodell på något av följande sätt:

* Använda [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) och dess Python-API för att programmera träningen av modellen i molnet. Custom Vision kan inte använda mer än några hundra bilder för att träna modellen, så du kan behöva begränsa datasetet.
* Använda exemplet från [Keras tutorial](https://keras.io/examples/vision/retinanet/) för att träna RetunaNet-modellen.
* Använda [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) inbyggd modul i torchvision.

## Slutsats

Objektidentifiering är en uppgift som ofta krävs inom industrin. Även om det finns tjänster som kan användas för att utföra objektidentifiering (såsom [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), är det viktigt att förstå hur objektidentifiering fungerar och att kunna träna sina egna modeller.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.