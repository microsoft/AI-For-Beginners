<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-28T19:37:20+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "nl"
}
-->
# Generatieve Adversariële Netwerken

In de vorige sectie hebben we geleerd over **generatieve modellen**: modellen die nieuwe afbeeldingen kunnen genereren die lijken op de afbeeldingen in de trainingsdataset. VAE was een goed voorbeeld van een generatief model.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

Als we echter proberen iets echt betekenisvols te genereren, zoals een schilderij met een redelijke resolutie, met VAE, zullen we zien dat de training niet goed convergeert. Voor dit gebruiksdoel moeten we leren over een andere architectuur die specifiek gericht is op generatieve modellen - **Generatieve Adversariële Netwerken**, of GANs.

Het belangrijkste idee van een GAN is om twee neurale netwerken te hebben die tegen elkaar worden getraind:

<img src="images/gan_architecture.png" width="70%"/>

> Afbeelding door [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Een beetje vocabulaire:
> * **Generator** is een netwerk dat een willekeurige vector neemt en als resultaat een afbeelding produceert.
> * **Discriminator** is een netwerk dat een afbeelding neemt en moet bepalen of het een echte afbeelding is (uit de trainingsdataset) of dat het is gegenereerd door een generator. Het is in wezen een beeldclassificator.

### Discriminator

De architectuur van de discriminator verschilt niet van een gewoon beeldclassificatienetwerk. In het eenvoudigste geval kan het een volledig verbonden classificator zijn, maar hoogstwaarschijnlijk zal het een [convolutioneel netwerk](../07-ConvNets/README.md) zijn.

> ✅ Een GAN gebaseerd op convolutionele netwerken wordt een [DCGAN](https://arxiv.org/pdf/1511.06434.pdf) genoemd.

Een CNN-discriminator bestaat uit de volgende lagen: meerdere convoluties+poolings (met afnemende ruimtelijke grootte) en een of meer volledig verbonden lagen om een "feature vector" te verkrijgen, en een uiteindelijke binaire classificator.

> ✅ 'Pooling' in deze context is een techniek die de grootte van de afbeelding verkleint. "Pooling-lagen verkleinen de dimensies van gegevens door de outputs van neuronclusters in één laag te combineren tot een enkele neuron in de volgende laag." - [bron](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generator

Een Generator is iets ingewikkelder. Je kunt het beschouwen als een omgekeerde discriminator. Beginnend met een latente vector (in plaats van een feature vector), heeft het een volledig verbonden laag om het om te zetten naar de vereiste grootte/vorm, gevolgd door deconvoluties+opschaling. Dit is vergelijkbaar met het *decoder*-gedeelte van [autoencoder](../09-Autoencoders/README.md).

> ✅ Omdat de convolutielaag wordt geïmplementeerd als een lineair filter dat door de afbeelding beweegt, is deconvolutie in wezen vergelijkbaar met convolutie en kan het worden geïmplementeerd met dezelfde laaglogica.

<img src="images/gan_arch_detail.png" width="70%"/>

> Afbeelding door [Dmitry Soshnikov](http://soshnikov.com)

### Het trainen van de GAN

GANs worden **adversariële** netwerken genoemd omdat er een constante competitie is tussen de generator en de discriminator. Tijdens deze competitie verbeteren zowel de generator als de discriminator, waardoor het netwerk leert steeds betere afbeeldingen te produceren.

De training gebeurt in twee fasen:

* **Het trainen van de discriminator**. Deze taak is vrij eenvoudig: we genereren een batch afbeeldingen met de generator, labelen ze als 0, wat staat voor nepafbeeldingen, en nemen een batch afbeeldingen uit de inputdataset (met label 1, echte afbeeldingen). We verkrijgen een *discriminator loss* en voeren backprop uit.
* **Het trainen van de generator**. Dit is iets ingewikkelder, omdat we niet direct weten wat de verwachte output voor de generator is. We nemen het hele GAN-netwerk, bestaande uit een generator gevolgd door een discriminator, voeden het met willekeurige vectoren en verwachten dat het resultaat 1 is (overeenkomend met echte afbeeldingen). We bevriezen vervolgens de parameters van de discriminator (we willen niet dat deze wordt getraind in deze stap) en voeren backprop uit.

Tijdens dit proces dalen zowel de generator- als de discriminator-verliezen niet significant. In de ideale situatie zouden ze moeten oscilleren, wat overeenkomt met beide netwerken die hun prestaties verbeteren.

## ✍️ Oefeningen: GANs

* [GAN Notebook in TensorFlow/Keras](GANTF.ipynb)
* [GAN Notebook in PyTorch](GANPyTorch.ipynb)

### Problemen bij het trainen van GANs

GANs staan bekend om hun moeilijkheid om te trainen. Hier zijn een paar problemen:

* **Mode Collapse**. Hiermee bedoelen we dat de generator leert om één succesvolle afbeelding te produceren die de discriminator misleidt, en niet een verscheidenheid aan verschillende afbeeldingen.
* **Gevoeligheid voor hyperparameters**. Vaak zie je dat een GAN helemaal niet convergeert, en dan plotseling een verlaging van de leersnelheid leidt tot convergentie.
* Het behouden van een **balans** tussen de generator en de discriminator. In veel gevallen kan de discriminator-verlies relatief snel naar nul dalen, wat resulteert in dat de generator niet verder kan trainen. Om dit te overwinnen, kunnen we proberen verschillende leersnelheden in te stellen voor de generator en discriminator, of de training van de discriminator overslaan als het verlies al te laag is.
* Training voor **hoge resolutie**. Dit probleem, vergelijkbaar met dat van autoencoders, wordt veroorzaakt doordat het reconstrueren van te veel lagen van een convolutioneel netwerk leidt tot artefacten. Dit probleem wordt meestal opgelost met zogenaamde **progressive growing**, waarbij eerst een paar lagen worden getraind op afbeeldingen met lage resolutie, en vervolgens lagen worden "ontgrendeld" of toegevoegd. Een andere oplossing zou zijn om extra verbindingen tussen lagen toe te voegen en meerdere resoluties tegelijk te trainen - zie dit [Multi-Scale Gradient GANs paper](https://arxiv.org/abs/1903.06048) voor details.

## Stijltransfer

GANs zijn een geweldige manier om artistieke afbeeldingen te genereren. Een andere interessante techniek is de zogenaamde **stijltransfer**, waarbij één **inhoudsafbeelding** wordt genomen en opnieuw wordt getekend in een andere stijl, waarbij filters van een **stijlafbeelding** worden toegepast.

Hoe het werkt:
* We beginnen met een willekeurige ruisafbeelding (of met een inhoudsafbeelding, maar om het te begrijpen is het eenvoudiger om te beginnen met willekeurige ruis).
* Ons doel is om een afbeelding te creëren die dicht bij zowel de inhoudsafbeelding als de stijlafbeelding ligt. Dit wordt bepaald door twee verliesfuncties:
   - **Inhoudsverlies** wordt berekend op basis van de kenmerken die door de CNN worden geëxtraheerd op sommige lagen van de huidige afbeelding en de inhoudsafbeelding.
   - **Stijlverlies** wordt op een slimme manier berekend tussen de huidige afbeelding en de stijlafbeelding met behulp van Gram-matrices (meer details in het [voorbeeldnotebook](StyleTransfer.ipynb)).
* Om de afbeelding gladder te maken en ruis te verwijderen, introduceren we ook **Variatieverlies**, dat de gemiddelde afstand tussen naburige pixels berekent.
* De hoofdoptimalisatielus past de huidige afbeelding aan met behulp van gradient descent (of een ander optimalisatie-algoritme) om het totale verlies te minimaliseren, wat een gewogen som is van alle drie de verliezen.

## ✍️ Voorbeeld: [Stijltransfer](StyleTransfer.ipynb)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## Conclusie

In deze les heb je geleerd over GANs en hoe je ze kunt trainen. Je hebt ook geleerd over de specifieke uitdagingen waarmee dit type Neuraal Netwerk te maken kan krijgen, en enkele strategieën om deze te overwinnen.

## 🚀 Uitdaging

Doorloop het [Stijltransfer-notebook](StyleTransfer.ipynb) met je eigen afbeeldingen.

## Review & Zelfstudie

Lees meer over GANs in deze bronnen:

* Marco Pasini, [10 Lessons I Learned Training GANs for one Year](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), een *de facto* GAN-architectuur om te overwegen
* [Creating Generative Art using GANs on Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Opdracht

Herbekijk een van de twee notebooks die bij deze les horen en train de GAN opnieuw met je eigen afbeeldingen. Wat kun je creëren?

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.