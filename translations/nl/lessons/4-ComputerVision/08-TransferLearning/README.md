<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "717775c4050ccbffbe0c961ad8bf7bf7",
  "translation_date": "2025-08-28T19:26:52+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/README.md",
  "language_code": "nl"
}
-->
# Voorgetrainde Netwerken en Transfer Learning

Het trainen van CNN's kan veel tijd kosten en vereist vaak een grote hoeveelheid data. Veel van de tijd wordt besteed aan het leren van de beste laag-niveau filters die een netwerk kan gebruiken om patronen uit afbeeldingen te halen. Een logische vraag is: kunnen we een neuraal netwerk dat op één dataset is getraind gebruiken en aanpassen om andere afbeeldingen te classificeren zonder het volledige trainingsproces opnieuw te doorlopen?

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/15)

Deze aanpak wordt **transfer learning** genoemd, omdat we kennis overdragen van het ene neurale netwerkmodel naar het andere. Bij transfer learning beginnen we meestal met een voorgetraind model, dat is getraind op een grote afbeeldingsdataset, zoals **ImageNet**. Deze modellen kunnen al goed verschillende kenmerken uit generieke afbeeldingen halen, en in veel gevallen kan het bouwen van een classifier bovenop deze geëxtraheerde kenmerken al goede resultaten opleveren.

> ✅ Transfer Learning is een term die je ook in andere academische velden tegenkomt, zoals Onderwijs. Het verwijst naar het proces waarbij kennis uit het ene domein wordt toegepast in een ander domein.

## Voorgetrainde Modellen als Kenmerkextractoren

De convolutionele netwerken die we in de vorige sectie hebben besproken, bevatten een aantal lagen die elk bepaalde kenmerken uit een afbeelding moeten halen. Dit begint bij laag-niveau pixelcombinaties (zoals horizontale/verticale lijnen of strepen) en gaat tot hogere niveau combinaties van kenmerken, zoals een oog van een vlam. Als we een CNN trainen op een voldoende grote dataset met generieke en diverse afbeeldingen, zou het netwerk moeten leren om deze gemeenschappelijke kenmerken te extraheren.

Zowel Keras als PyTorch bevatten functies om eenvoudig voorgetrainde neurale netwerkgewichten te laden voor enkele veelgebruikte architecturen, waarvan de meeste zijn getraind op ImageNet-afbeeldingen. De meest gebruikte modellen worden beschreven op de pagina [CNN Architectures](../07-ConvNets/CNN_Architectures.md) uit de vorige les. In het bijzonder kun je overwegen een van de volgende te gebruiken:

* **VGG-16/VGG-19**, relatief eenvoudige modellen die toch goede nauwkeurigheid bieden. Vaak is het gebruik van VGG als eerste poging een goede keuze om te zien hoe transfer learning werkt.
* **ResNet**, een familie van modellen voorgesteld door Microsoft Research in 2015. Deze hebben meer lagen en vereisen daardoor meer middelen.
* **MobileNet**, een familie van modellen met een kleinere omvang, geschikt voor mobiele apparaten. Gebruik deze als je weinig middelen hebt en een beetje nauwkeurigheid kunt opofferen.

Hier zijn voorbeeldkenmerken die door het VGG-16-netwerk uit een afbeelding van een kat zijn geëxtraheerd:

![Kenmerken geëxtraheerd door VGG-16](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.nl.png)

## Dataset Katten versus Honden

In dit voorbeeld gebruiken we een dataset van [Katten en Honden](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), die erg lijkt op een realistische afbeeldingsclassificatiesituatie.

## ✍️ Oefening: Transfer Learning

Laten we transfer learning in actie zien in de bijbehorende notebooks:

* [Transfer Learning - PyTorch](TransferLearningPyTorch.ipynb)
* [Transfer Learning - TensorFlow](TransferLearningTF.ipynb)

## Visualiseren van Adversariële Kat

Een voorgetraind neuraal netwerk bevat verschillende patronen in zijn *brein*, waaronder ideeën van een **ideale kat** (evenals een ideale hond, ideale zebra, enz.). Het zou interessant zijn om dit beeld op de een of andere manier **te visualiseren**. Dit is echter niet eenvoudig, omdat patronen verspreid zijn over de netwerkgewichten en ook georganiseerd zijn in een hiërarchische structuur.

Een aanpak die we kunnen nemen, is beginnen met een willekeurige afbeelding en vervolgens proberen de afbeelding aan te passen met behulp van de techniek **gradient descent optimalisatie**, zodat het netwerk begint te denken dat het een kat is.

![Afbeeldingsoptimalisatielus](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.nl.png)

Als we dit doen, krijgen we echter iets dat erg lijkt op willekeurige ruis. Dit komt omdat *er veel manieren zijn om een netwerk te laten denken dat de invoerafbeelding een kat is*, inclusief enkele die visueel geen zin hebben. Hoewel deze afbeeldingen veel patronen bevatten die typisch zijn voor een kat, is er niets dat hen dwingt visueel onderscheidend te zijn.

Om het resultaat te verbeteren, kunnen we een andere term toevoegen aan de verliesfunctie, genaamd **variatieverlies**. Dit is een maatstaf die laat zien hoe vergelijkbaar naburige pixels van de afbeelding zijn. Het minimaliseren van variatieverlies maakt de afbeelding gladder en verwijdert ruis, waardoor meer visueel aantrekkelijke patronen zichtbaar worden. Hier is een voorbeeld van dergelijke "ideale" afbeeldingen, die met hoge waarschijnlijkheid als kat en als zebra worden geclassificeerd:

![Ideale Kat](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.nl.png) | ![Ideale Zebra](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.nl.png)
-----|-----
 *Ideale Kat* | *Ideale Zebra*

Een vergelijkbare aanpak kan worden gebruikt om zogenaamde **adversariële aanvallen** op een neuraal netwerk uit te voeren. Stel dat we een neuraal netwerk willen misleiden en een hond eruit willen laten zien als een kat. Als we een afbeelding van een hond nemen, die door een netwerk als hond wordt herkend, kunnen we deze een beetje aanpassen met behulp van gradient descent optimalisatie, totdat het netwerk deze begint te classificeren als een kat:

![Afbeelding van een Hond](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.nl.png) | ![Afbeelding van een hond geclassificeerd als een kat](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.nl.png)
-----|-----
*Originele afbeelding van een hond* | *Afbeelding van een hond geclassificeerd als een kat*

Zie de code om de bovenstaande resultaten te reproduceren in het volgende notebook:

* [Ideale en Adversariële Kat - TensorFlow](AdversarialCat_TF.ipynb)

## Conclusie

Met transfer learning kun je snel een classifier samenstellen voor een aangepaste objectclassificatietaak en een hoge nauwkeurigheid bereiken. Je ziet dat complexere taken die we nu oplossen meer rekenkracht vereisen en niet eenvoudig op de CPU kunnen worden uitgevoerd. In de volgende eenheid proberen we een lichtere implementatie te gebruiken om hetzelfde model te trainen met minder rekenmiddelen, wat resulteert in slechts iets lagere nauwkeurigheid.

## 🚀 Uitdaging

In de bijbehorende notebooks staan notities onderaan over hoe transferkennis het beste werkt met enigszins vergelijkbare trainingsdata (bijvoorbeeld een nieuw type dier). Experimenteer met volledig nieuwe soorten afbeeldingen om te zien hoe goed of slecht je transferkennis-modellen presteren.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Herziening & Zelfstudie

Lees [TrainingTricks.md](TrainingTricks.md) door om je kennis te verdiepen over andere manieren om je modellen te trainen.

## [Opdracht](lab/README.md)

In dit lab gebruiken we de real-life [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) huisdierendataset met 35 rassen van katten en honden, en bouwen we een transfer learning classifier.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.