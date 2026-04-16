# Detekcija glava koristeći Hollywood Heads Dataset

Laboratorijska vježba iz [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Zadatak

Brojanje broja ljudi na video nadzornim kamerama važan je zadatak koji nam omogućuje procjenu broja posjetitelja u trgovinama, najprometnijih sati u restoranima itd. Kako bismo riješili ovaj zadatak, potrebno je moći detektirati ljudske glave iz različitih kutova. Za treniranje modela za detekciju objekata koji prepoznaje ljudske glave, možemo koristiti [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Dataset

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) sadrži 369,846 ljudskih glava označenih u 224,740 filmskih okvira iz holivudskih filmova. Dataset je dostupan u formatu [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), gdje za svaku sliku postoji i XML datoteka s opisom koja izgleda ovako:

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

U ovom datasetu postoji samo jedna klasa objekata `head`, a za svaku glavu dobivate koordinate okvira (bounding box). XML datoteke možete parsirati koristeći Python biblioteke ili koristiti [ovu biblioteku](https://pypi.org/project/pascal-voc/) za direktan rad s PASCAL VOC formatom.

## Treniranje modela za detekciju objekata

Model za detekciju objekata možete trenirati na jedan od sljedećih načina:

* Koristeći [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) i njegov Python API za programatsko treniranje modela u oblaku. Custom Vision neće moći koristiti više od nekoliko stotina slika za treniranje modela, pa ćete možda morati ograničiti dataset.
* Koristeći primjer iz [Keras tutoriala](https://keras.io/examples/vision/retinanet/) za treniranje RetunaNet modela.
* Koristeći [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) ugrađeni modul u torchvision.

## Zaključak

Detekcija objekata je zadatak koji se često zahtijeva u industriji. Iako postoje usluge koje se mogu koristiti za detekciju objekata (kao što je [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), važno je razumjeti kako detekcija objekata funkcionira i biti sposoban trenirati vlastite modele.

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.