# Zaznavanje glav z uporabo Hollywood Heads Dataset

Laboratorijska naloga iz [učnega načrta AI za začetnike](https://github.com/microsoft/ai-for-beginners).

## Naloga

Štetje števila ljudi na video nadzornih posnetkih je pomembna naloga, ki nam omogoča oceno števila obiskovalcev v trgovinah, določitev najbolj obremenjenih ur v restavracijah itd. Za rešitev te naloge moramo biti sposobni zaznati človeške glave iz različnih kotov. Za treniranje modela za zaznavanje objektov, ki zaznava človeške glave, lahko uporabimo [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Podatkovni niz

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) vsebuje 369.846 človeških glav, označenih v 224.740 filmskih okvirjih iz hollywoodskih filmov. Na voljo je v formatu [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), kjer ima vsaka slika tudi XML opisno datoteko, ki izgleda takole:

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

V tem podatkovnem nizu obstaja samo en razred objektov `head`, za vsako glavo pa so podane koordinate okvirja (bounding box). XML lahko obdelate z uporabo Python knjižnic ali pa uporabite [to knjižnico](https://pypi.org/project/pascal-voc/), ki omogoča neposredno delo s formatom PASCAL VOC.

## Treniranje modela za zaznavanje objektov

Model za zaznavanje objektov lahko trenirate na enega od naslednjih načinov:

* Z uporabo [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) in njegovega Python API-ja za programatično treniranje modela v oblaku. Custom Vision ne omogoča uporabe več kot nekaj sto slik za treniranje modela, zato boste morda morali omejiti podatkovni niz.
* Z uporabo primera iz [Keras vadnice](https://keras.io/examples/vision/retinanet/) za treniranje modela RetunaNet.
* Z uporabo vgrajenega modula [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) v knjižnici torchvision.

## Ključne ugotovitve

Zaznavanje objektov je naloga, ki je pogosto potrebna v industriji. Čeprav obstajajo storitve, ki omogočajo zaznavanje objektov (kot je [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), je pomembno razumeti, kako zaznavanje objektov deluje, in biti sposoben trenirati lastne modele.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.