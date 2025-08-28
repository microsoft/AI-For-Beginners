<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58bf4adb210aab53e8f78c8082040e7c",
  "translation_date": "2025-08-28T20:06:06+00:00",
  "source_file": "lessons/5-NLP/16-RNN/README.md",
  "language_code": "nl"
}
-->
# Recurrent Neural Networks

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/116)

In eerdere secties hebben we gebruik gemaakt van rijke semantische representaties van tekst en een eenvoudige lineaire classifier bovenop de embeddings. Wat deze architectuur doet, is de geaggregeerde betekenis van woorden in een zin vastleggen, maar het houdt geen rekening met de **volgorde** van woorden, omdat de aggregatiebewerking bovenop de embeddings deze informatie uit de oorspronkelijke tekst verwijdert. Omdat deze modellen niet in staat zijn om de volgorde van woorden te modelleren, kunnen ze geen complexere of dubbelzinnige taken oplossen, zoals tekstgeneratie of vraag-antwoord systemen.

Om de betekenis van een tekstvolgorde vast te leggen, moeten we een andere neurale netwerkarchitectuur gebruiken, genaamd een **recurrent neural network**, of RNN. In een RNN voeren we onze zin één symbool tegelijk door het netwerk, en het netwerk produceert een bepaalde **toestand**, die we vervolgens samen met het volgende symbool opnieuw aan het netwerk doorgeven.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.nl.png)

> Afbeelding door de auteur

Gegeven de invoervolgorde van tokens X<sub>0</sub>,...,X<sub>n</sub>, creëert een RNN een reeks neurale netwerkblokken en traint deze reeks end-to-end met behulp van backpropagation. Elk netwerkblok neemt een paar (X<sub>i</sub>,S<sub>i</sub>) als invoer en produceert S<sub>i+1</sub> als resultaat. De uiteindelijke toestand S<sub>n</sub> of (uitvoer Y<sub>n</sub>) gaat naar een lineaire classifier om het resultaat te produceren. Alle netwerkblokken delen dezelfde gewichten en worden end-to-end getraind met één backpropagation-pass.

Omdat toestandsvectoren S<sub>0</sub>,...,S<sub>n</sub> door het netwerk worden doorgegeven, kan het de sequentiële afhankelijkheden tussen woorden leren. Bijvoorbeeld, wanneer het woord *niet* ergens in de volgorde verschijnt, kan het leren om bepaalde elementen binnen de toestandsvector te negateren, wat resulteert in ontkenning.

> ✅ Omdat de gewichten van alle RNN-blokken in de bovenstaande afbeelding worden gedeeld, kan dezelfde afbeelding worden weergegeven als één blok (rechts) met een recurrente feedbacklus, die de uitvoerstatus van het netwerk teruggeeft aan de invoer.

## Anatomie van een RNN-cel

Laten we eens kijken hoe een eenvoudige RNN-cel is georganiseerd. Het accepteert de vorige toestand S<sub>i-1</sub> en het huidige symbool X<sub>i</sub> als invoer en moet de uitvoerstatus S<sub>i</sub> produceren (en soms zijn we ook geïnteresseerd in een andere uitvoer Y<sub>i</sub>, zoals in het geval van generatieve netwerken).

Een eenvoudige RNN-cel heeft twee gewichts-matrices binnenin: één transformeert een invoersymbool (laten we het W noemen), en een andere transformeert een invoerstatus (H). In dit geval wordt de uitvoer van het netwerk berekend als σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b), waarbij σ de activatiefunctie is en b een extra bias is.

<img alt="RNN Cell Anatomy" src="images/rnn-anatomy.png" width="50%"/>

> Afbeelding door de auteur

In veel gevallen worden invoertokens door de embeddinglaag geleid voordat ze de RNN binnenkomen om de dimensionaliteit te verlagen. In dit geval, als de dimensie van de invoervectoren *emb_size* is, en de toestandsvector *hid_size* is - dan is de grootte van W *emb_size*×*hid_size*, en de grootte van H is *hid_size*×*hid_size*.

## Long Short Term Memory (LSTM)

Een van de belangrijkste problemen van klassieke RNN's is het zogenaamde **vanishing gradients**-probleem. Omdat RNN's end-to-end worden getraind in één backpropagation-pass, is het moeilijk om fouten door te geven aan de eerste lagen van het netwerk, waardoor het netwerk geen relaties tussen verre tokens kan leren. Een van de manieren om dit probleem te vermijden, is door **expliciet toestandsbeheer** te introduceren met behulp van zogenaamde **gates**. Er zijn twee bekende architecturen van dit type: **Long Short Term Memory** (LSTM) en **Gated Relay Unit** (GRU).

![Afbeelding van een voorbeeld van een long short term memory-cel](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Afbeeldingsbron TBD

Het LSTM-netwerk is georganiseerd op een manier die lijkt op een RNN, maar er zijn twee toestanden die van laag naar laag worden doorgegeven: de werkelijke toestand C en de verborgen vector H. Bij elke eenheid wordt de verborgen vector H<sub>i</sub> samengevoegd met invoer X<sub>i</sub>, en zij bepalen wat er met de toestand C gebeurt via **gates**. Elke gate is een neuraal netwerk met sigmoid-activatie (uitvoer in het bereik [0,1]), die kan worden gezien als een bitmasker wanneer vermenigvuldigd met de toestandsvector. Er zijn de volgende gates (van links naar rechts op de bovenstaande afbeelding):

* De **forget gate** neemt een verborgen vector en bepaalt welke componenten van de vector C we moeten vergeten en welke we moeten doorgeven.
* De **input gate** neemt wat informatie van de invoer- en verborgen vectoren en voegt deze in de toestand in.
* De **output gate** transformeert de toestand via een lineaire laag met *tanh*-activatie en selecteert vervolgens enkele van de componenten met behulp van een verborgen vector H<sub>i</sub> om een nieuwe toestand C<sub>i+1</sub> te produceren.

Componenten van de toestand C kunnen worden gezien als vlaggen die aan- en uitgezet kunnen worden. Bijvoorbeeld, wanneer we een naam zoals *Alice* in de volgorde tegenkomen, willen we misschien aannemen dat het verwijst naar een vrouwelijk personage en de vlag in de toestand verhogen dat we een vrouwelijk zelfstandig naamwoord in de zin hebben. Wanneer we verder zinnen zoals *en Tom* tegenkomen, zullen we de vlag verhogen dat we een meervoudig zelfstandig naamwoord hebben. Door de toestand te manipuleren, kunnen we dus verondersteld grammaticale eigenschappen van zinsdelen bijhouden.

> ✅ Een uitstekende bron om de interne werking van LSTM te begrijpen, is dit geweldige artikel [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) van Christopher Olah.

## Bidirectionele en Meerdere Lagen RNN's

We hebben recurrente netwerken besproken die in één richting werken, van het begin van een volgorde tot het einde. Dit lijkt natuurlijk, omdat het lijkt op de manier waarop we lezen en luisteren naar spraak. Echter, aangezien we in veel praktische gevallen willekeurige toegang hebben tot de invoervolgorde, kan het zinvol zijn om de recurrente berekening in beide richtingen uit te voeren. Dergelijke netwerken worden **bidirectionele** RNN's genoemd. Bij het werken met een bidirectioneel netwerk hebben we twee verborgen toestandsvectoren nodig, één voor elke richting.

Een recurrent netwerk, of het nu eenrichtingsverkeer of bidirectioneel is, legt bepaalde patronen binnen een volgorde vast en kan deze opslaan in een toestandsvector of doorgeven aan de uitvoer. Net als bij convolutionele netwerken kunnen we een andere recurrente laag bovenop de eerste bouwen om patronen van een hoger niveau vast te leggen en te bouwen op basis van de patronen van een lager niveau die door de eerste laag zijn geëxtraheerd. Dit leidt ons tot het concept van een **multi-layer RNN**, die bestaat uit twee of meer recurrente netwerken, waarbij de uitvoer van de vorige laag als invoer naar de volgende laag wordt doorgegeven.

![Afbeelding van een multilayer long-short-term-memory RNN](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.nl.jpg)

*Afbeelding uit [dit geweldige artikel](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) van Fernando López*

## ✍️ Oefeningen: Embeddings

Ga verder met leren in de volgende notebooks:

* [RNNs met PyTorch](RNNPyTorch.ipynb)
* [RNNs met TensorFlow](RNNTF.ipynb)

## Conclusie

In deze eenheid hebben we gezien dat RNN's kunnen worden gebruikt voor sequentieclassificatie, maar in feite kunnen ze veel meer taken aan, zoals tekstgeneratie, machinale vertaling en meer. We zullen die taken in de volgende eenheid bespreken.

## 🚀 Uitdaging

Lees enkele literatuur over LSTMs en overweeg hun toepassingen:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/216)

## Review & Zelfstudie

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) van Christopher Olah.

## [Opdracht: Notebooks](assignment.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, willen we u erop wijzen dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.