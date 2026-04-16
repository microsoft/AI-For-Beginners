# Fejdetektálás a Hollywood Heads Dataset segítségével

Laborfeladat az [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) anyagából.

## Feladat

Az emberek számának megszámlálása egy videómegfigyelő kamera képén fontos feladat, amely lehetővé teszi például a boltok látogatószámának becslését vagy az éttermek forgalmas időszakainak meghatározását. Ennek a feladatnak a megoldásához képesnek kell lennünk különböző szögekből felismerni az emberi fejeket. Az objektumfelismerő modell betanításához, amely képes az emberi fejek detektálására, használhatjuk a [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/) adathalmazt.

## Az adathalmaz

A [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) 369,846 emberi fejet tartalmaz, amelyek 224,740 hollywoodi filmkockán vannak megjelölve. Az adathalmaz a [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) formátumban érhető el, ahol minden képhez tartozik egy XML leíró fájl, amely így néz ki:

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

Ebben az adathalmazban csak egyetlen objektumosztály létezik, a `head`, és minden fejhez megkapjuk a határoló doboz koordinátáit. Az XML fájlokat Python könyvtárakkal lehet feldolgozni, vagy használhatjuk [ezt a könyvtárat](https://pypi.org/project/pascal-voc/), amely közvetlenül a PASCAL VOC formátummal dolgozik.

## Objektumfelismerés betanítása

Az objektumfelismerő modell betanításához az alábbi módszerek egyikét használhatjuk:

* Az [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) és annak Python API-jának használata, hogy programozottan betanítsuk a modellt a felhőben. A Custom Vision csak néhány száz képet tud használni a modell betanításához, így lehet, hogy korlátoznunk kell az adathalmaz méretét.
* A [Keras tutorial](https://keras.io/examples/vision/retinanet/) példájának használata a RetunaNet modell betanításához.
* A [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) beépített moduljának használata a torchvision könyvtárban.

## Tanulság

Az objektumfelismerés egy olyan feladat, amelyre gyakran szükség van az iparban. Bár léteznek szolgáltatások, amelyekkel objektumfelismerést végezhetünk (például az [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), fontos megérteni, hogyan működik az objektumfelismerés, és képesnek lenni saját modellek betanítására.

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.