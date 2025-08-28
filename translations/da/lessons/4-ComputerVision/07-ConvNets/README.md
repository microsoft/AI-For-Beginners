<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "088837b42b7d99198bf62db8a42411e0",
  "translation_date": "2025-08-28T15:12:29+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/README.md",
  "language_code": "da"
}
-->
# Konvolutionelle Neurale Netværk

Vi har tidligere set, at neurale netværk er ret gode til at arbejde med billeder, og selv en enkeltlags perceptron kan genkende håndskrevne cifre fra MNIST-datasættet med rimelig nøjagtighed. MNIST-datasættet er dog meget specielt, da alle cifre er centreret i billedet, hvilket gør opgaven enklere.

## [Quiz før forelæsning](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/107)

I virkeligheden ønsker vi at kunne genkende objekter på et billede uanset deres præcise placering i billedet. Computer vision adskiller sig fra generisk klassifikation, fordi vi, når vi forsøger at finde et bestemt objekt på et billede, scanner billedet for at finde specifikke **mønstre** og deres kombinationer. For eksempel, når vi leder efter en kat, kan vi først kigge efter horisontale linjer, som kan danne knurhår, og derefter kan en bestemt kombination af knurhår fortælle os, at det faktisk er et billede af en kat. Den relative position og tilstedeværelsen af visse mønstre er vigtig, og ikke deres præcise placering på billedet.

For at udtrække mønstre vil vi bruge begrebet **konvolutionelle filtre**. Som du ved, repræsenteres et billede af en 2D-matrix eller en 3D-tensor med farvedybde. At anvende et filter betyder, at vi tager en relativt lille **filterkerne**-matrix, og for hver pixel i det originale billede beregner vi det vægtede gennemsnit med nabopunkter. Vi kan se dette som et lille vindue, der glider over hele billedet og udjævner alle pixels i henhold til vægtene i filterkernematrixen.

![Vertikalt Kantfilter](../../../../../translated_images/filter-vert.b7148390ca0bc356ddc7e55555d2481819c1e86ddde9dce4db5e71a69d6f887f.da.png) | ![Horisontalt Kantfilter](../../../../../translated_images/filter-horiz.59b80ed4feb946efbe201a7fe3ca95abb3364e266e6fd90820cb893b4d3a6dda.da.png)
----|----

> Billede af Dmitry Soshnikov

For eksempel, hvis vi anvender 3x3 vertikale og horisontale kantfiltre på MNIST-cifre, kan vi fremhæve (f.eks. høje værdier), hvor der er vertikale og horisontale kanter i vores originale billede. Således kan disse to filtre bruges til at "lede efter" kanter. På samme måde kan vi designe forskellige filtre til at lede efter andre lavniveau-mønstre:

> Billede af [Leung-Malik Filter Bank](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

Men selvom vi kan designe filtrene manuelt til at udtrække nogle mønstre, kan vi også designe netværket på en måde, så det automatisk lærer mønstrene. Det er en af de vigtigste ideer bag CNN.

## Hovedideer bag CNN

Måden CNN'er fungerer på, er baseret på følgende vigtige ideer:

* Konvolutionelle filtre kan udtrække mønstre
* Vi kan designe netværket, så filtrene trænes automatisk
* Vi kan bruge samme tilgang til at finde mønstre i højere niveauer af funktioner, ikke kun i det originale billede. CNN's funktionsekstraktion arbejder således på en hierarki af funktioner, der starter med lavniveau-pixelkombinationer og går op til højere niveau-kombinationer af billeddele.

![Hierarkisk Funktionsekstraktion](../../../../../translated_images/FeatureExtractionCNN.d9b456cbdae7cb643fde3032b81b2940e3cf8be842e29afac3f482725ba7f95c.da.png)

> Billede fra [en artikel af Hislop-Lynch](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), baseret på [deres forskning](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Øvelser: Konvolutionelle Neurale Netværk

Lad os fortsætte med at udforske, hvordan konvolutionelle neurale netværk fungerer, og hvordan vi kan opnå trænbare filtre, ved at arbejde igennem de tilhørende notebooks:

* [Konvolutionelle Neurale Netværk - PyTorch](ConvNetsPyTorch.ipynb)
* [Konvolutionelle Neurale Netværk - TensorFlow](ConvNetsTF.ipynb)

## Pyramidearkitektur

De fleste CNN'er, der bruges til billedbehandling, følger en såkaldt pyramidearkitektur. Det første konvolutionelle lag, der anvendes på de originale billeder, har typisk et relativt lavt antal filtre (8-16), som svarer til forskellige pixelkombinationer, såsom horisontale/vertikale linjer eller streger. På det næste niveau reducerer vi netværkets rumlige dimension og øger antallet af filtre, hvilket svarer til flere mulige kombinationer af simple funktioner. Med hvert lag, når vi bevæger os mod den endelige klassifikator, mindskes de rumlige dimensioner af billedet, og antallet af filtre vokser.

Som et eksempel, lad os se på arkitekturen af VGG-16, et netværk der opnåede 92,7% nøjagtighed i ImageNet's top-5 klassifikation i 2014:

![ImageNet Lag](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.da.jpg)

![ImageNet Pyramide](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.da.jpg)

> Billede fra [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## Bedst Kendte CNN Arkitekturer

[Fortsæt din læring om de bedst kendte CNN-arkitekturer](CNN_Architectures.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.