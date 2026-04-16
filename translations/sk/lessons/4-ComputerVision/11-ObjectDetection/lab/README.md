# Detekcia hláv pomocou datasetu Hollywood Heads

Laboratórna úloha z [kurzu AI pre začiatočníkov](https://github.com/microsoft/ai-for-beginners).

## Úloha

Počítanie počtu ľudí na videozázname z bezpečnostnej kamery je dôležitá úloha, ktorá nám umožňuje odhadnúť počet návštevníkov v obchodoch, vyťažené hodiny v reštauráciách a podobne. Na vyriešenie tejto úlohy musíme byť schopní detegovať ľudské hlavy z rôznych uhlov. Na natrénovanie modelu na detekciu objektov, ktorý dokáže rozpoznať ľudské hlavy, môžeme použiť [dataset Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/).

## Dataset

[Dataset Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) obsahuje 369 846 ľudských hláv anotovaných v 224 740 filmových snímkach z hollywoodskych filmov. Je poskytnutý vo formáte [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), kde pre každý obrázok existuje aj XML súbor s popisom, ktorý vyzerá takto:

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

V tomto datasete existuje iba jedna trieda objektov `head` (hlava) a pre každú hlavu sú uvedené súradnice ohraničujúceho rámčeka. XML súbory môžete spracovať pomocou knižníc v Pythone alebo použiť [túto knižnicu](https://pypi.org/project/pascal-voc/) na prácu priamo s formátom PASCAL VOC.

## Tréning detekcie objektov

Model na detekciu objektov môžete natrénovať jedným z nasledujúcich spôsobov:

* Použitím [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) a jeho Python API na programatické trénovanie modelu v cloude. Custom Vision nedokáže použiť viac ako niekoľko stoviek obrázkov na trénovanie modelu, takže možno budete musieť dataset obmedziť.
* Použitím príkladu z [Keras tutoriálu](https://keras.io/examples/vision/retinanet/) na natrénovanie modelu RetinaNet.
* Použitím vstavaného modulu [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) v knižnici torchvision.

## Zhrnutie

Detekcia objektov je úloha, ktorá je často potrebná v priemysle. Aj keď existujú služby, ktoré umožňujú vykonávať detekciu objektov (napríklad [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), je dôležité pochopiť, ako detekcia objektov funguje, a byť schopný natrénovať vlastné modely.

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.