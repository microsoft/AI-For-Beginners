# Rilevamento delle teste usando il dataset Hollywood Heads

Compito del laboratorio tratto dal [Curriculum AI for Beginners](https://github.com/microsoft/ai-for-beginners).

## Compito

Contare il numero di persone in un flusso video di una telecamera di sorveglianza è un compito importante che ci permette di stimare il numero di visitatori in negozi, le ore di punta in un ristorante, ecc. Per risolvere questo compito, dobbiamo essere in grado di rilevare le teste umane da diverse angolazioni. Per addestrare un modello di rilevamento degli oggetti per identificare le teste umane, possiamo utilizzare il [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Il Dataset

Il [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) contiene 369.846 teste umane annotate in 224.740 fotogrammi di film di Hollywood. È fornito nel formato [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC), dove per ogni immagine c'è anche un file di descrizione XML che appare così:

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

In questo dataset, c'è solo una classe di oggetti `head`, e per ogni testa vengono forniti i coordinati della bounding box. Puoi analizzare i file XML usando librerie Python, oppure utilizzare [questa libreria](https://pypi.org/project/pascal-voc/) per gestire direttamente il formato PASCAL VOC.

## Addestramento del modello di rilevamento degli oggetti

Puoi addestrare un modello di rilevamento degli oggetti utilizzando uno dei seguenti metodi:

* Utilizzando [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) e la sua API Python per addestrare il modello nel cloud in modo programmatico. Custom Vision non sarà in grado di utilizzare più di qualche centinaio di immagini per addestrare il modello, quindi potrebbe essere necessario limitare il dataset.
* Utilizzando l'esempio del [tutorial di Keras](https://keras.io/examples/vision/retinanet/) per addestrare il modello RetunaNet.
* Utilizzando il modulo integrato [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) in torchvision.

## Conclusione

Il rilevamento degli oggetti è un compito frequentemente richiesto nell'industria. Sebbene esistano alcuni servizi che possono essere utilizzati per eseguire il rilevamento degli oggetti (come [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), è importante comprendere come funziona il rilevamento degli oggetti e saper addestrare i propri modelli.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.