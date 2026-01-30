# Hoveddetektion ved brug af Hollywood Heads Dataset

Lab-opgave fra [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Opgave

At tælle antallet af personer på en videoovervågningsstrøm er en vigtig opgave, der gør det muligt for os at estimere antallet af besøgende i butikker, travle timer i en restaurant osv. For at løse denne opgave skal vi kunne detektere menneskehovedet fra forskellige vinkler. For at træne en objektdetekteringsmodel til at finde menneskehovedet kan vi bruge [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Datasættet

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) indeholder 369.846 menneskehoved-annoteringer i 224.740 filmrammer fra Hollywood-film. Det leveres i [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC)-format, hvor der for hvert billede også er en XML-beskrivelsesfil, der ser sådan ud:

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

I dette datasæt er der kun én klasse af objekter, `head`, og for hvert hoved får du koordinaterne for afgrænsningsboksen. Du kan parse XML ved hjælp af Python-biblioteker eller bruge [dette bibliotek](https://pypi.org/project/pascal-voc/) til at arbejde direkte med PASCAL VOC-formatet.

## Træning af objektdetektering

Du kan træne en objektdetekteringsmodel ved hjælp af en af følgende metoder:

* Brug [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) og dets Python API til programmatisk at træne modellen i skyen. Custom Vision vil ikke kunne bruge mere end et par hundrede billeder til at træne modellen, så du kan være nødt til at begrænse datasættet.
* Brug eksemplet fra [Keras tutorial](https://keras.io/examples/vision/retinanet/) til at træne RetunaNet-modellen.
* Brug [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) indbygget modul i torchvision.

## Læringspunkt

Objektdetektering er en opgave, der ofte kræves i industrien. Selvom der findes nogle tjenester, der kan bruges til at udføre objektdetektering (såsom [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), er det vigtigt at forstå, hvordan objektdetektering fungerer, og at kunne træne dine egne modeller.

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.