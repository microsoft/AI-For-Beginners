# Utambuzi wa Vichwa kwa Kutumia Hollywood Heads Dataset

Kazi ya Maabara kutoka [Mtaala wa AI kwa Kompyuta](https://github.com/microsoft/ai-for-beginners).

## Kazi

Kuhesabu idadi ya watu kwenye mkondo wa kamera ya ufuatiliaji ni kazi muhimu ambayo itatuwezesha kukadiria idadi ya wageni katika maduka, saa za shughuli nyingi kwenye mgahawa, n.k. Ili kutatua kazi hii, tunahitaji uwezo wa kutambua vichwa vya binadamu kutoka pembe tofauti. Ili kufundisha modeli ya utambuzi wa vitu kutambua vichwa vya binadamu, tunaweza kutumia [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Dataset

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) ina vichwa vya binadamu 369,846 vilivyotolewa maelezo katika fremu za filamu 224,740 kutoka filamu za Hollywood. Dataset hii inatolewa katika muundo wa [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), ambapo kwa kila picha kuna faili ya maelezo ya XML inayofanana na hii:

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

Katika dataset hii, kuna darasa moja tu la vitu `head`, na kwa kila kichwa, unapata maelezo ya mipaka ya kisanduku. Unaweza kuchambua XML kwa kutumia maktaba za Python, au kutumia [maktaba hii](https://pypi.org/project/pascal-voc/) kushughulikia moja kwa moja muundo wa PASCAL VOC.

## Mafunzo ya Utambuzi wa Vitu

Unaweza kufundisha modeli ya utambuzi wa vitu kwa kutumia mojawapo ya njia zifuatazo:

* Kutumia [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) na API yake ya Python kufundisha modeli kwa njia ya programu kwenye wingu. Custom Vision haitakuwa na uwezo wa kutumia zaidi ya picha chache kwa mafunzo ya modeli, kwa hivyo unaweza kuhitaji kupunguza dataset.
* Kutumia mfano kutoka [Keras tutorial](https://keras.io/examples/vision/retinanet/) kufundisha modeli ya RetunaNet.
* Kutumia [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) moduli iliyojengwa ndani ya torchvision.

## Muhimu

Utambuzi wa vitu ni kazi ambayo mara nyingi inahitajika katika sekta. Ingawa kuna huduma ambazo zinaweza kutumika kufanya utambuzi wa vitu (kama [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), ni muhimu kuelewa jinsi utambuzi wa vitu unavyofanya kazi na kuwa na uwezo wa kufundisha modeli zako mwenyewe.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.