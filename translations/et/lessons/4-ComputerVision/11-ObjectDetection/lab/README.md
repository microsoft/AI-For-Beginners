# Peade tuvastamine Hollywood Heads andmestiku abil

Laboriülesanne [AI algajatele õppekavast](https://github.com/microsoft/ai-for-beginners).

## Ülesanne

Inimeste arvu lugemine videovalvekaamera voogesituse kaudu on oluline ülesanne, mis võimaldab meil hinnata külastajate arvu poodides, restoranide tipptunde jne. Selle ülesande lahendamiseks peame suutma tuvastada inimpead erinevatest nurkadest. Inimpeade tuvastamiseks objekti tuvastamise mudeli treenimiseks saame kasutada [Hollywood Heads andmestikku](https://www.di.ens.fr/willow/research/headdetection/).

## Andmestik

[Hollywood Heads andmestik](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) sisaldab 369,846 inimpead, mis on märgistatud 224,740 Hollywoodi filmikaadris. See on esitatud [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) formaadis, kus iga pildi kohta on ka XML-kirjeldusfail, mis näeb välja selline:

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

Selles andmestikus on ainult üks objektiklass `head`, ja iga pea kohta antakse piirava kasti koordinaadid. XML-i saab parsida Python'i teekide abil või kasutada [seda teeki](https://pypi.org/project/pascal-voc/), et töötada otse PASCAL VOC formaadiga.

## Objekti tuvastamise treenimine

Objekti tuvastamise mudelit saab treenida ühel järgmistest viisidest:

* Kasutades [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) ja selle Python API-d, et mudelit pilves programmiliselt treenida. Custom Vision ei suuda kasutada rohkem kui paarisadat pilti mudeli treenimiseks, seega võib olla vajalik andmestikku piirata.
* Kasutades näidet [Keras õpetusest](https://keras.io/examples/vision/retinanet/), et treenida RetunaNet mudelit.
* Kasutades [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) sisseehitatud moodulit torchvision'is.

## Õppetunnid

Objekti tuvastamine on ülesanne, mida tööstuses sageli vajatakse. Kuigi on olemas teenuseid, mida saab kasutada objekti tuvastamiseks (näiteks [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), on oluline mõista, kuidas objekti tuvastamine töötab ja osata treenida omaenda mudeleid.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.