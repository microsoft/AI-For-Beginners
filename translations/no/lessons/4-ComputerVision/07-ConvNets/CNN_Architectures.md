# Velkjente CNN-arkitekturer

### VGG-16

VGG-16 er et nettverk som oppnådde 92,7 % nøyaktighet i ImageNet top-5 klassifisering i 2014. Det har følgende lagstruktur:

![ImageNet Layers](../../../../../translated_images/no/vgg-16-arch1.d901a5583b3a51ba.webp)

Som du kan se, følger VGG en tradisjonell pyramidearkitektur, som er en sekvens av konvolusjons- og pooling-lag.

![ImageNet Pyramid](../../../../../translated_images/no/vgg-16-arch.64ff2137f50dd49f.webp)

> Bilde fra [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet er en familie av modeller foreslått av Microsoft Research i 2015. Hovedideen bak ResNet er å bruke **residualblokker**:

<img src="../../../../../translated_images/no/resnet-block.aba4ccbcc0944434.webp" width="300"/>

> Bilde fra [denne artikkelen](https://arxiv.org/pdf/1512.03385.pdf)

Grunnen til å bruke identitets-passering er at laget skal forutsi **forskjellen** mellom resultatet fra et tidligere lag og utgangen fra residualblokken - derav navnet *residual*. Disse blokkene er mye enklere å trene, og man kan konstruere nettverk med flere hundre slike blokker (de vanligste variantene er ResNet-52, ResNet-101 og ResNet-152).

Du kan også tenke på dette nettverket som i stand til å justere kompleksiteten til datasettet. I starten, når du begynner å trene nettverket, er vektverdiene små, og mesteparten av signalet går gjennom identitetslagene. Etter hvert som treningen skrider frem og vektene blir større, øker betydningen av nettverksparametrene, og nettverket tilpasser seg for å oppnå nødvendig uttrykkskraft for å klassifisere treningsbildene korrekt.

### Google Inception

Google Inception-arkitekturen tar denne ideen et steg videre og bygger hvert nettverkslag som en kombinasjon av flere forskjellige veier:

<img src="../../../../../translated_images/no/inception.a6605b85bcbc6f52.webp" width="400"/>

> Bilde fra [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Her må vi fremheve rollen til 1x1-konvolusjoner, fordi de ved første øyekast ikke gir mening. Hvorfor skulle vi trenge å kjøre gjennom bildet med et 1x1-filter? Men du må huske at konvolusjonsfiltre også fungerer med flere dybdekanaler (opprinnelig - RGB-farger, i påfølgende lag - kanaler for forskjellige filtre), og 1x1-konvolusjon brukes til å blande disse inngangskanalene sammen ved hjelp av forskjellige trenbare vekter. Det kan også ses som nedsampling (pooling) over kanaldimensjonen.

Her er [en god bloggpost](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) om emnet, og [den originale artikkelen](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

MobileNet er en familie av modeller med redusert størrelse, egnet for mobile enheter. Bruk dem hvis du har begrensede ressurser og kan ofre litt nøyaktighet. Hovedideen bak dem er såkalte **depthwise separable convolution**, som gjør det mulig å representere konvolusjonsfiltre som en sammensetning av romlige konvolusjoner og 1x1-konvolusjon over dybdekanaler. Dette reduserer antall parametere betydelig, noe som gjør nettverket mindre i størrelse og også enklere å trene med mindre data.

Her er [en god bloggpost om MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Konklusjon

I denne enheten har du lært hovedkonseptet bak nevrale nettverk for datamaskinsyn - konvolusjonsnettverk. Virkelige arkitekturer som driver bildeklassifisering, objektdeteksjon og til og med bildegenereringsnettverk er alle basert på CNN-er, bare med flere lag og noen ekstra treningsmetoder.

## 🚀 Utfordring

I de medfølgende notatbøkene er det notater nederst om hvordan man kan oppnå høyere nøyaktighet. Gjør noen eksperimenter for å se om du kan oppnå bedre resultater.

## [Quiz etter forelesning](https://ff-quizzes.netlify.app/en/ai/quiz/14)

## Gjennomgang og selvstudium

Selv om CNN-er oftest brukes til oppgaver innen datamaskinsyn, er de generelt gode til å trekke ut mønstre av fast størrelse. For eksempel, hvis vi jobber med lyd, kan vi også bruke CNN-er til å lete etter spesifikke mønstre i lydsignalet - i så fall vil filtrene være 1-dimensjonale (og dette CNN-et vil kalles 1D-CNN). Noen ganger brukes også 3D-CNN til å trekke ut funksjoner i et multidimensjonalt rom, som visse hendelser som skjer på video - CNN kan fange visse mønstre av funksjonsendringer over tid. Gjør litt gjennomgang og selvstudium om andre oppgaver som kan utføres med CNN-er.

## [Oppgave](lab/README.md)

I denne laben skal du klassifisere forskjellige katteraser og hunderaser. Disse bildene er mer komplekse enn MNIST-datasettet og har høyere dimensjoner, og det er mer enn 10 klasser.

---

