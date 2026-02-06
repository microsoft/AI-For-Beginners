# Velkendte CNN-arkitekturer

### VGG-16

VGG-16 er et netværk, der opnåede 92,7% nøjagtighed i ImageNet top-5 klassifikation i 2014. Det har følgende lagstruktur:

![ImageNet Layers](../../../../../translated_images/da/vgg-16-arch1.d901a5583b3a51ba.webp)

Som du kan se, følger VGG en traditionel pyramidearkitektur, som er en sekvens af konvolutions- og pooling-lag.

![ImageNet Pyramid](../../../../../translated_images/da/vgg-16-arch.64ff2137f50dd49f.webp)

> Billede fra [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet er en familie af modeller foreslået af Microsoft Research i 2015. Hovedideen bag ResNet er brugen af **residualblokke**:

<img src="../../../../../translated_images/da/resnet-block.aba4ccbcc0944434.webp" width="300"/>

> Billede fra [denne artikel](https://arxiv.org/pdf/1512.03385.pdf)

Grunden til at bruge identitets-pass-through er, at laget skal forudsige **forskellen** mellem resultatet af et tidligere lag og outputtet fra residualblokken - deraf navnet *residual*. Disse blokke er meget lettere at træne, og man kan konstruere netværk med flere hundrede af disse blokke (de mest almindelige varianter er ResNet-52, ResNet-101 og ResNet-152).

Du kan også tænke på dette netværk som værende i stand til at justere sin kompleksitet til datasættet. I starten, når du begynder at træne netværket, er vægtværdierne små, og det meste af signalet går gennem identitetslagene. Efterhånden som træningen skrider frem, og vægtene bliver større, vokser betydningen af netværkets parametre, og netværket tilpasser sig for at opnå den nødvendige udtrykskraft til korrekt klassifikation af træningsbillederne.

### Google Inception

Google Inception-arkitekturen tager denne idé et skridt videre og bygger hvert netværkslag som en kombination af flere forskellige veje:

<img src="../../../../../translated_images/da/inception.a6605b85bcbc6f52.webp" width="400"/>

> Billede fra [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Her skal vi fremhæve rollen af 1x1-konvolutioner, fordi de ved første øjekast ikke giver mening. Hvorfor skulle vi have brug for at køre gennem billedet med et 1x1-filter? Men det er vigtigt at huske, at konvolutionsfiltre også arbejder med flere dybdekanaler (oprindeligt - RGB-farver, i efterfølgende lag - kanaler for forskellige filtre), og 1x1-konvolution bruges til at blande disse inputkanaler sammen ved hjælp af forskellige trænbare vægte. Det kan også ses som en form for nedsampling (pooling) over kanaldimensionen.

Her er [en god blogpost](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) om emnet og [den originale artikel](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

MobileNet er en familie af modeller med reduceret størrelse, der er velegnede til mobile enheder. Brug dem, hvis du har begrænsede ressourcer og kan acceptere en lille reduktion i nøjagtighed. Hovedideen bag dem er den såkaldte **depthwise separable convolution**, som gør det muligt at repræsentere konvolutionsfiltre som en sammensætning af rumlige konvolutioner og 1x1-konvolution over dybdekanaler. Dette reducerer antallet af parametre betydeligt, hvilket gør netværket mindre i størrelse og også lettere at træne med mindre data.

Her er [en god blogpost om MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Konklusion

I denne enhed har du lært hovedkonceptet bag neurale netværk til computer vision - konvolutionsnetværk. Virkelige arkitekturer, der driver billedklassifikation, objektgenkendelse og endda billedgenereringsnetværk, er alle baseret på CNN'er, blot med flere lag og nogle ekstra træningstricks.

## 🚀 Udfordring

I de medfølgende notebooks er der noter nederst om, hvordan man opnår større nøjagtighed. Lav nogle eksperimenter for at se, om du kan opnå højere nøjagtighed.

## [Quiz efter forelæsning](https://ff-quizzes.netlify.app/en/ai/quiz/14)

## Gennemgang & Selvstudie

Selvom CNN'er oftest bruges til opgaver inden for computer vision, er de generelt gode til at udtrække mønstre af fast størrelse. For eksempel, hvis vi arbejder med lyde, kan vi også bruge CNN'er til at finde specifikke mønstre i lydsignaler - i dette tilfælde ville filtrene være 1-dimensionelle (og dette CNN ville blive kaldt 1D-CNN). Nogle gange bruges også 3D-CNN til at udtrække funktioner i et multidimensionelt rum, såsom visse begivenheder, der sker på video - CNN kan fange visse mønstre af funktioner, der ændrer sig over tid. Lav en gennemgang og selvstudie om andre opgaver, der kan udføres med CNN'er.

## [Opgave](lab/README.md)

I denne lab skal du klassificere forskellige katte- og hunderacer. Disse billeder er mere komplekse end MNIST-datasættet og har højere dimensioner, og der er mere end 10 klasser.

---

