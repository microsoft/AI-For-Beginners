# Hodedeteksjon ved bruk av Hollywood Heads Dataset

Laboppgave fra [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Oppgave

Å telle antall personer på videostrøm fra overvåkningskamera er en viktig oppgave som lar oss estimere antall besøkende i butikker, travle timer på en restaurant, osv. For å løse denne oppgaven må vi kunne oppdage menneskehoder fra ulike vinkler. For å trene en objektgjenkjenningsmodell til å oppdage menneskehoder, kan vi bruke [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Datasettet

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) inneholder 369,846 menneskehoder annotert i 224,740 filmrammer fra Hollywood-filmer. Det er levert i [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC)-format, hvor det for hvert bilde også finnes en XML-beskrivelsesfil som ser slik ut:

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

I dette datasettet er det kun én klasse av objekter, `head`, og for hvert hode får du koordinatene til avgrensningsboksen. Du kan analysere XML ved hjelp av Python-biblioteker, eller bruke [dette biblioteket](https://pypi.org/project/pascal-voc/) for å jobbe direkte med PASCAL VOC-formatet.

## Trening av objektgjenkjenning

Du kan trene en objektgjenkjenningsmodell ved hjelp av en av følgende metoder:

* Bruke [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) og dens Python-API for å programmere treningen av modellen i skyen. Custom Vision vil ikke kunne bruke mer enn noen få hundre bilder til å trene modellen, så du må kanskje begrense datasettet.
* Bruke eksempelet fra [Keras tutorial](https://keras.io/examples/vision/retinanet/) for å trene RetunaNet-modellen.
* Bruke [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html), en innebygd modul i torchvision.

## Lærdom

Objektgjenkjenning er en oppgave som ofte er nødvendig i industrien. Selv om det finnes tjenester som kan brukes til å utføre objektgjenkjenning (som [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), er det viktig å forstå hvordan objektgjenkjenning fungerer og å kunne trene dine egne modeller.

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.