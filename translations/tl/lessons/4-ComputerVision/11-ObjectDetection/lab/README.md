# Pagtukoy ng Ulo gamit ang Hollywood Heads Dataset

Gawain sa Lab mula sa [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Gawain

Ang pagbibilang ng bilang ng mga tao sa video surveillance camera stream ay isang mahalagang gawain na makakatulong sa atin upang matantya ang bilang ng mga bisita sa mga tindahan, mga oras ng kasagsagan sa isang restawran, at iba pa. Upang maisagawa ang gawaing ito, kailangan nating matutong tukuyin ang mga ulo ng tao mula sa iba't ibang anggulo. Upang sanayin ang isang object detection model na makakakita ng mga ulo ng tao, maaari nating gamitin ang [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Ang Dataset

Ang [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) ay naglalaman ng 369,846 ulo ng tao na may anotasyon sa 224,740 mga frame mula sa mga pelikula sa Hollywood. Ito ay ibinibigay sa [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) na format, kung saan para sa bawat imahe ay may kasamang XML na file ng deskripsyon na ganito ang hitsura:

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

Sa dataset na ito, mayroon lamang isang klase ng mga bagay, `head`, at para sa bawat ulo, makakakuha ka ng mga koordinado ng bounding box. Maaari mong i-parse ang XML gamit ang mga Python library, o gamitin ang [library na ito](https://pypi.org/project/pascal-voc/) upang direktang makipagtrabaho sa PASCAL VOC format.

## Pagsasanay ng Object Detection

Maaari kang magsanay ng isang object detection model gamit ang isa sa mga sumusunod na paraan:

* Gamit ang [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) at ang Python API nito upang programatikong sanayin ang modelo sa cloud. Ang Custom Vision ay maaaring gumamit lamang ng ilang daang imahe para sa pagsasanay ng modelo, kaya maaaring kailanganin mong limitahan ang dataset.
* Gamit ang halimbawa mula sa [Keras tutorial](https://keras.io/examples/vision/retinanet/) upang sanayin ang RetunaNet model.
* Gamit ang [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) na built-in na module sa torchvision.

## Mahalagang Aral

Ang object detection ay isang gawain na madalas na kinakailangan sa industriya. Bagama't may ilang mga serbisyo na maaaring gamitin upang magsagawa ng object detection (tulad ng [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), mahalagang maunawaan kung paano gumagana ang object detection at magkaroon ng kakayahang sanayin ang sarili mong mga modelo.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.