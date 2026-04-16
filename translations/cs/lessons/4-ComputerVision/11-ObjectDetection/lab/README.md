# Detekce hlav pomocí Hollywood Heads Dataset

Laboratorní úkol z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Úkol

Počítání počtu lidí na záznamu z kamerového systému je důležitý úkol, který nám umožní odhadnout počet návštěvníků v obchodech, rušné hodiny v restauracích apod. Abychom tento úkol vyřešili, musíme být schopni detekovat lidské hlavy z různých úhlů. Pro natrénování modelu detekce objektů na detekci lidských hlav můžeme použít [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Dataset

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) obsahuje 369 846 lidských hlav anotovaných ve 224 740 filmových snímcích z hollywoodských filmů. Je poskytován ve formátu [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), kde pro každý obrázek existuje také XML soubor s popisem, který vypadá takto:

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

V tomto datasetu existuje pouze jedna třída objektů `head`, a pro každou hlavu získáte souřadnice ohraničujícího boxu. XML soubory můžete parsovat pomocí Python knihoven, nebo použít [tuto knihovnu](https://pypi.org/project/pascal-voc/) pro práci přímo s formátem PASCAL VOC.

## Trénování detekce objektů 

Model detekce objektů můžete natrénovat jedním z následujících způsobů:

* Použitím [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) a jeho Python API pro programatické trénování modelu v cloudu. Custom Vision nebude schopný použít více než několik stovek obrázků pro trénování modelu, takže možná budete muset dataset omezit.
* Použitím příkladu z [Keras tutorialu](https://keras.io/examples/vision/retinanet/) pro natrénování modelu RetunaNet.
* Použitím vestavěného modulu [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) v knihovně torchvision.

## Závěr

Detekce objektů je úkol, který je často vyžadován v průmyslu. I když existují služby, které lze použít k provádění detekce objektů (například [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), je důležité pochopit, jak detekce objektů funguje, a být schopný natrénovat vlastní modely.

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.