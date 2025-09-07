<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-28T19:35:47+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "nl"
}
-->
# Segmentatie

We hebben eerder geleerd over Objectdetectie, waarmee we objecten in een afbeelding kunnen lokaliseren door hun *omsluitende kaders* te voorspellen. Voor sommige taken hebben we echter niet alleen omsluitende kaders nodig, maar ook een nauwkeurigere lokalisatie van objecten. Deze taak wordt **segmentatie** genoemd.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

Segmentatie kan worden gezien als **pixelclassificatie**, waarbij we voor **elke** pixel in de afbeelding de klasse moeten voorspellen (*achtergrond* is een van de klassen). Er zijn twee hoofdtypen segmentatie-algoritmen:

* **Semantische segmentatie** geeft alleen de klasse van de pixel aan en maakt geen onderscheid tussen verschillende objecten van dezelfde klasse.
* **Instance segmentatie** verdeelt klassen in verschillende objecten (instanties).

Bij instance segmentatie zijn deze schapen verschillende objecten, maar bij semantische segmentatie worden alle schapen weergegeven als één klasse.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Afbeelding afkomstig van [deze blogpost](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Er zijn verschillende neurale architecturen voor segmentatie, maar ze hebben allemaal dezelfde structuur. Op een bepaalde manier lijkt het op de auto-encoder waar je eerder over hebt geleerd, maar in plaats van de originele afbeelding te reconstrueren, is ons doel om een **masker** te reconstrueren. Een segmentatienetwerk heeft dus de volgende onderdelen:

* **Encoder** haalt kenmerken uit de invoerafbeelding.
* **Decoder** zet die kenmerken om in de **maskerafbeelding**, met dezelfde grootte en een aantal kanalen dat overeenkomt met het aantal klassen.

<img src="images/segm.png" width="80%">

> Afbeelding afkomstig van [deze publicatie](https://arxiv.org/pdf/2001.05566.pdf)

We moeten vooral de verliesfunctie noemen die wordt gebruikt voor segmentatie. Bij klassieke auto-encoders moeten we de gelijkenis tussen twee afbeeldingen meten, en daarvoor kunnen we de mean square error (MSE) gebruiken. Bij segmentatie vertegenwoordigt elke pixel in de doelmaskerafbeelding het klassenummer (one-hot-gecodeerd langs de derde dimensie), dus moeten we verliesfuncties gebruiken die specifiek zijn voor classificatie - cross-entropy loss, gemiddeld over alle pixels. Als het masker binair is, wordt **binaire cross-entropy loss** (BCE) gebruikt.

> ✅ One-hot encoding is een manier om een klasse-label te coderen in een vector met een lengte die gelijk is aan het aantal klassen. Bekijk [dit artikel](https://datagy.io/sklearn-one-hot-encode/) over deze techniek.

## Segmentatie voor Medische Beeldvorming

In deze les zullen we segmentatie in actie zien door een netwerk te trainen om menselijke naevi (ook wel moedervlekken genoemd) te herkennen op medische afbeeldingen. We zullen gebruik maken van de <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> Database</a> van dermoscopie-afbeeldingen als beeldbron. Deze dataset bevat 200 afbeeldingen van drie klassen: typische naevus, atypische naevus en melanoom. Alle afbeeldingen bevatten ook een bijbehorend **masker** dat de naevus omlijnt.

> ✅ Deze techniek is bijzonder geschikt voor dit type medische beeldvorming, maar welke andere toepassingen in de echte wereld kun je bedenken?

<img alt="navi" src="images/navi.png"/>

> Afbeelding afkomstig van de PH<sup>2</sup> Database

We zullen een model trainen om elke naevus te segmenteren van de achtergrond.

## ✍️ Oefeningen: Semantische Segmentatie

Open de onderstaande notebooks om meer te leren over verschillende semantische segmentatie-architecturen, ermee te oefenen en ze in actie te zien.

* [Semantic Segmentation Pytorch](SemanticSegmentationPytorch.ipynb)
* [Semantic Segmentation TensorFlow](SemanticSegmentationTF.ipynb)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Conclusie

Segmentatie is een zeer krachtige techniek voor beeldclassificatie, die verder gaat dan omsluitende kaders naar classificatie op pixelniveau. Het is een techniek die wordt gebruikt in medische beeldvorming, naast andere toepassingen.

## 🚀 Uitdaging

Lichaamssegmentatie is slechts een van de veelvoorkomende taken die we kunnen uitvoeren met afbeeldingen van mensen. Andere belangrijke taken zijn onder andere **skeletdetectie** en **posedetectie**. Probeer de [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)-bibliotheek uit om te zien hoe posedetectie kan worden gebruikt.

## Review & Zelfstudie

Dit [Wikipedia-artikel](https://wikipedia.org/wiki/Image_segmentation) biedt een goed overzicht van de verschillende toepassingen van deze techniek. Leer meer over de subdomeinen van Instance segmentatie en Panoptische segmentatie binnen dit onderzoeksgebied.

## [Opdracht](lab/README.md)

Probeer in dit lab **menselijke lichaamssegmentatie** met behulp van de [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) van Kaggle.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.