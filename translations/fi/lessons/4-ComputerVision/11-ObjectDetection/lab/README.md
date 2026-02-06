# Pään tunnistus Hollywood Heads -datastolla

Lab-tehtävä [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) -materiaalista.

## Tehtävä

Ihmisten laskeminen videovalvontakameran streamista on tärkeä tehtävä, joka mahdollistaa esimerkiksi kaupan kävijämäärän arvioinnin tai ravintolan ruuhka-aikojen tunnistamisen. Tämän tehtävän ratkaisemiseksi meidän täytyy pystyä tunnistamaan ihmisten päät eri kulmista. Jotta voimme kouluttaa objektintunnistusmallin tunnistamaan ihmisten päät, voimme käyttää [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/) -datastoa.

## Datasetti

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) sisältää 369,846 ihmisen päätä, jotka on merkitty 224,740 Hollywood-elokuvien kuvakehykseen. Datasetti on saatavilla [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) -formaatissa, jossa jokaiselle kuvalle on myös XML-kuvaustiedosto, joka näyttää tältä:

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

Tässä datasetissä on vain yksi objektiluokka, `head`, ja jokaiselle päälle annetaan rajauslaatikon koordinaatit. Voit käsitellä XML-tiedostoja Python-kirjastojen avulla tai käyttää [tätä kirjastoa](https://pypi.org/project/pascal-voc/) suoraan PASCAL VOC -formaatin käsittelyyn.

## Objektintunnistuksen kouluttaminen

Voit kouluttaa objektintunnistusmallin jollakin seuraavista tavoista:

* Käyttämällä [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) -palvelua ja sen Python-rajapintaa mallin ohjelmalliseen kouluttamiseen pilvessä. Custom Vision ei pysty käyttämään kuin muutamia satoja kuvia mallin kouluttamiseen, joten datasettiä voi olla tarpeen rajata.
* Käyttämällä esimerkkiä [Keras-tutoriaalista](https://keras.io/examples/vision/retinanet/) RetunaNet-mallin kouluttamiseen.
* Käyttämällä [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) -moduulia, joka on sisäänrakennettu torchvisioniin.

## Yhteenveto

Objektintunnistus on tehtävä, jota tarvitaan usein teollisuudessa. Vaikka on olemassa palveluita, joita voidaan käyttää objektintunnistuksen suorittamiseen (kuten [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), on tärkeää ymmärtää, miten objektintunnistus toimii ja osata kouluttaa omia malleja.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.