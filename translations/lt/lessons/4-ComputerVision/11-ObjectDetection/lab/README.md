# Galvų aptikimas naudojant Hollywood Heads duomenų rinkinį

Laboratorinis darbas iš [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Užduotis

Žmonių skaičiavimas vaizdo stebėjimo kamerų sraute yra svarbi užduotis, leidžianti įvertinti lankytojų skaičių parduotuvėse, užimtumo valandas restoranuose ir pan. Norint išspręsti šią užduotį, reikia sugebėti aptikti žmonių galvas iš skirtingų kampų. Norint apmokyti objektų aptikimo modelį, kuris aptiktų žmonių galvas, galima naudoti [Hollywood Heads duomenų rinkinį](https://www.di.ens.fr/willow/research/headdetection/).

## Duomenų rinkinys

[Hollywood Heads duomenų rinkinys](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) apima 369,846 žmonių galvas, pažymėtas 224,740 filmų kadruose iš Holivudo filmų. Jis pateikiamas [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) formatu, kur kiekvienam vaizdui yra XML aprašymo failas, kuris atrodo taip:

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

Šiame duomenų rinkinyje yra tik viena objektų klasė `head`, o kiekvienai galvai pateikiamos ribojančio langelio koordinatės. XML failus galima analizuoti naudojant Python bibliotekas arba naudoti [šią biblioteką](https://pypi.org/project/pascal-voc/), kad tiesiogiai dirbtumėte su PASCAL VOC formatu.

## Objektų aptikimo mokymas

Objektų aptikimo modelį galite apmokyti vienu iš šių būdų:

* Naudojant [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) ir jo Python API, kad programiškai apmokytumėte modelį debesyje. Custom Vision negalės naudoti daugiau nei kelių šimtų vaizdų modelio mokymui, todėl gali tekti apriboti duomenų rinkinį.
* Naudojant pavyzdį iš [Keras pamokos](https://keras.io/examples/vision/retinanet/) RetunaNet modelio mokymui.
* Naudojant [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) įmontuotą modulį torchvision bibliotekoje.

## Išvada

Objektų aptikimas yra užduotis, kuri dažnai reikalinga pramonėje. Nors yra paslaugų, kurias galima naudoti objektų aptikimui (pvz., [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), svarbu suprasti, kaip veikia objektų aptikimas ir gebėti apmokyti savo modelius.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.