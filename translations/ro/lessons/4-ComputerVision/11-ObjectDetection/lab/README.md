# Detectarea capetelor folosind Hollywood Heads Dataset

Temă de laborator din [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Sarcina

Numărarea numărului de persoane pe fluxul unei camere de supraveghere video este o sarcină importantă care ne permite să estimăm numărul de vizitatori într-un magazin, orele aglomerate într-un restaurant etc. Pentru a rezolva această sarcină, trebuie să fim capabili să detectăm capetele umane din diferite unghiuri. Pentru a antrena un model de detectare a obiectelor care să identifice capetele umane, putem folosi [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Dataset-ul

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) conține 369.846 de capete umane adnotate în 224.740 de cadre din filme de la Hollywood. Este furnizat în format [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), unde pentru fiecare imagine există și un fișier XML descriptiv care arată astfel:

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

În acest dataset există o singură clasă de obiecte, `head`, iar pentru fiecare cap se oferă coordonatele casetei de delimitare. Poți analiza fișierele XML folosind biblioteci Python sau poți folosi [această bibliotecă](https://pypi.org/project/pascal-voc/) pentru a lucra direct cu formatul PASCAL VOC.

## Antrenarea modelului de detectare a obiectelor

Poți antrena un model de detectare a obiectelor folosind una dintre următoarele metode:

* Folosind [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) și API-ul său Python pentru a antrena modelul programatic în cloud. Custom Vision nu va putea folosi mai mult de câteva sute de imagini pentru antrenarea modelului, așa că poate fi necesar să limitezi dataset-ul.
* Folosind exemplul din [tutorialul Keras](https://keras.io/examples/vision/retinanet/) pentru a antrena modelul RetunaNet.
* Folosind modulul integrat [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) din torchvision.

## Concluzii

Detectarea obiectelor este o sarcină frecvent necesară în industrie. Deși există servicii care pot fi utilizate pentru a efectua detectarea obiectelor (cum ar fi [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), este important să înțelegem cum funcționează detectarea obiectelor și să fim capabili să ne antrenăm propriile modele.

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.