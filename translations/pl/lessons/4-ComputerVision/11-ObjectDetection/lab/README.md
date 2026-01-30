# Wykrywanie głów za pomocą zbioru danych Hollywood Heads

Zadanie laboratoryjne z [Kursu AI dla początkujących](https://github.com/microsoft/ai-for-beginners).

## Zadanie

Liczenie liczby osób na strumieniu z kamery monitoringu to ważne zadanie, które pozwala oszacować liczbę odwiedzających w sklepach, godziny szczytu w restauracjach itp. Aby rozwiązać to zadanie, musimy być w stanie wykrywać ludzkie głowy z różnych kątów. Do trenowania modelu wykrywającego obiekty, który potrafi rozpoznawać ludzkie głowy, możemy wykorzystać [zbiór danych Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/).

## Zbiór danych

[Zbiór danych Hollywood Heads](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) zawiera 369 846 ludzkich głów oznaczonych na 224 740 klatkach filmowych z hollywoodzkich filmów. Dane są dostarczone w formacie [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), gdzie dla każdego obrazu dostępny jest również plik XML, który wygląda tak:

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

W tym zbiorze danych istnieje tylko jedna klasa obiektów `head`, a dla każdej głowy podane są współrzędne ramki ograniczającej. Możesz analizować pliki XML za pomocą bibliotek Pythona lub skorzystać z [tej biblioteki](https://pypi.org/project/pascal-voc/), aby bezpośrednio pracować z formatem PASCAL VOC.

## Trenowanie modelu wykrywającego obiekty

Możesz trenować model wykrywający obiekty na jeden z następujących sposobów:

* Korzystając z [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) i jego API dla Pythona, aby programowo trenować model w chmurze. Custom Vision nie pozwala na użycie więcej niż kilkuset obrazów do trenowania modelu, więc może być konieczne ograniczenie zbioru danych.
* Korzystając z przykładu z [samouczka Keras](https://keras.io/examples/vision/retinanet/), aby wytrenować model RetunaNet.
* Korzystając z wbudowanego modułu [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) w torchvision.

## Wnioski

Wykrywanie obiektów to zadanie często wymagane w przemyśle. Chociaż istnieją usługi, które można wykorzystać do wykrywania obiektów (takie jak [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), ważne jest, aby zrozumieć, jak działa wykrywanie obiektów i być w stanie trenować własne modele.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.