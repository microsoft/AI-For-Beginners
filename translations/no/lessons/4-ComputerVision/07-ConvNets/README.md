<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "088837b42b7d99198bf62db8a42411e0",
  "translation_date": "2025-08-28T15:12:47+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/README.md",
  "language_code": "no"
}
-->
# Konvolusjonelle Nevrale Nettverk

Vi har tidligere sett at nevrale nettverk er ganske gode til å håndtere bilder, og til og med et ett-lags perseptron kan gjenkjenne håndskrevne sifre fra MNIST-datasettet med rimelig nøyaktighet. MNIST-datasettet er imidlertid veldig spesielt, og alle sifrene er sentrert i bildet, noe som gjør oppgaven enklere.

## [Quiz før forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/13)

I virkeligheten ønsker vi å kunne gjenkjenne objekter i et bilde uavhengig av deres eksakte plassering i bildet. Datamaskinsyn skiller seg fra generell klassifisering, fordi når vi prøver å finne et bestemt objekt i bildet, skanner vi bildet på jakt etter spesifikke **mønstre** og deres kombinasjoner. For eksempel, når vi ser etter en katt, kan vi først se etter horisontale linjer som kan danne værhår, og deretter kan en viss kombinasjon av værhår fortelle oss at det faktisk er et bilde av en katt. Relativ posisjon og tilstedeværelse av visse mønstre er viktig, og ikke deres eksakte plassering i bildet.

For å trekke ut mønstre bruker vi begrepet **konvolusjonsfiltre**. Som du vet, representeres et bilde av en 2D-matrise, eller en 3D-tensor med fargedybde. Å bruke et filter betyr at vi tar en relativt liten **filterkjerne**-matrise, og for hver piksel i det originale bildet beregner vi det vektede gjennomsnittet med nabopunktene. Vi kan se på dette som et lite vindu som glir over hele bildet og jevner ut alle pikslene i henhold til vektene i filterkjernematrisa.

![Vertikalt kantfilter](../../../../../translated_images/filter-vert.b7148390ca0bc356ddc7e55555d2481819c1e86ddde9dce4db5e71a69d6f887f.no.png) | ![Horisontalt kantfilter](../../../../../translated_images/filter-horiz.59b80ed4feb946efbe201a7fe3ca95abb3364e266e6fd90820cb893b4d3a6dda.no.png)
----|----

> Bilde av Dmitry Soshnikov

For eksempel, hvis vi bruker 3x3 vertikale og horisontale kantfiltre på MNIST-sifrene, kan vi fremheve (f.eks. høye verdier) der det er vertikale og horisontale kanter i vårt originale bilde. Dermed kan disse to filtrene brukes til å "se etter" kanter. På samme måte kan vi designe forskjellige filtre for å se etter andre lavnivåmønstre:

> Bilde av [Leung-Malik Filter Bank](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

Men selv om vi kan designe filtrene manuelt for å trekke ut noen mønstre, kan vi også designe nettverket slik at det lærer mønstrene automatisk. Dette er en av hovedidéene bak CNN.

## Hovedidéer bak CNN

Måten CNN-er fungerer på er basert på følgende viktige ideer:

* Konvolusjonsfiltre kan trekke ut mønstre
* Vi kan designe nettverket slik at filtrene trenes automatisk
* Vi kan bruke samme tilnærming for å finne mønstre i høyere nivå-funksjoner, ikke bare i det originale bildet. Dermed fungerer CNN-funksjonsekstraksjon på et hierarki av funksjoner, fra lavnivå pikselkombinasjoner til høyere nivå kombinasjoner av bildeelementer.

![Hierarkisk funksjonsekstraksjon](../../../../../translated_images/FeatureExtractionCNN.d9b456cbdae7cb643fde3032b81b2940e3cf8be842e29afac3f482725ba7f95c.no.png)

> Bilde fra [en artikkel av Hislop-Lynch](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), basert på [deres forskning](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Øvelser: Konvolusjonelle Nevrale Nettverk

La oss fortsette å utforske hvordan konvolusjonelle nevrale nettverk fungerer, og hvordan vi kan oppnå trenbare filtre, ved å jobbe gjennom de tilhørende notatbøkene:

* [Konvolusjonelle Nevrale Nettverk - PyTorch](ConvNetsPyTorch.ipynb)
* [Konvolusjonelle Nevrale Nettverk - TensorFlow](ConvNetsTF.ipynb)

## Pyramidearkitektur

De fleste CNN-er som brukes til bildebehandling følger en såkalt pyramidearkitektur. Det første konvolusjonslaget som brukes på de originale bildene, har vanligvis et relativt lavt antall filtre (8-16), som tilsvarer forskjellige pikselkombinasjoner, som horisontale/vertikale linjer eller strøk. På neste nivå reduserer vi de romlige dimensjonene til nettverket og øker antallet filtre, som tilsvarer flere mulige kombinasjoner av enkle funksjoner. For hvert lag, når vi beveger oss mot den endelige klassifiseringen, reduseres de romlige dimensjonene til bildet, og antallet filtre øker.

Som et eksempel, la oss se på arkitekturen til VGG-16, et nettverk som oppnådde 92,7 % nøyaktighet i ImageNets topp-5 klassifisering i 2014:

![ImageNet-lag](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.no.jpg)

![ImageNet-pyramide](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.no.jpg)

> Bilde fra [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## Mest Kjente CNN-arkitekturer

[Fortsett studiet om de mest kjente CNN-arkitekturene](CNN_Architectures.md)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.