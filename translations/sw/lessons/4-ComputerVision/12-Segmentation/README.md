# Segmentering

Vi har tidigare lärt oss om Objektigenkänning, som gör det möjligt för oss att lokalisera objekt i bilden genom att förutsäga deras *ramar*. Men för vissa uppgifter behöver vi inte bara ramar, utan också mer exakt lokalisering av objekt. Denna uppgift kallas för **segmentering**.

## [För-lärare quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

Segmentering kan ses som **pixelkategorisering**, där vi för **varje** pixel i bilden måste förutsäga dess klass (*bakgrund* är en av klasserna). Det finns två huvudalgoritmer för segmentering:

* **Semantisk segmentering** berättar endast pixelns klass och gör ingen åtskillnad mellan olika objekt av samma klass.
* **Instanssegmentering** delar klasser i olika instanser.

För instanssegmentering är dessa får olika objekt, men för semantisk segmentering representeras alla får av en klass.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Bild från [detta blogginlägg](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Det finns olika neurala arkitekturer för segmentering, men de har alla samma struktur. På ett sätt liknar det autoencodern du lärde dig om tidigare, men istället för att dekonstruera den ursprungliga bilden, är vårt mål att dekonstruera en **mask**. Således har ett segmenteringsnätverk följande delar:

* **Encoder** extraherar funktioner från inmatningsbilden.
* **Decoder** omvandlar dessa funktioner till **maskbilden**, med samma storlek och antal kanaler motsvarande antalet klasser.

<img src="images/segm.png" width="80%">

> Bild från [denna publikation](https://arxiv.org/pdf/2001.05566.pdf)

Vi bör särskilt nämna förlustfunktionen som används för segmentering. När vi använder klassiska autoencoders behöver vi mäta likheten mellan två bilder, och vi kan använda medelkvadratfel (MSE) för att göra det. Vid segmentering representerar varje pixel i målmaskbilden klassnumret (one-hot-kodad längs den tredje dimensionen), så vi behöver använda förlustfunktioner specifika för klassificering - korsentropiförlust, genomsnittlig över alla pixlar. Om masken är binär - används **binär korsentropiförlust** (BCE).

> ✅ One-hot-kodning är ett sätt att koda en klassetikett till en vektor av längd som är lika med antalet klasser. Ta en titt på [denna artikel](https://datagy.io/sklearn-one-hot-encode/) om denna teknik.

## Segmentering för Medicinsk Avbildning

I denna lektion kommer vi att se segmentering i praktiken genom att träna nätverket att känna igen mänskliga nevi (även kända som födelsemärken) på medicinska bilder. Vi kommer att använda <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> Databas</a> av dermatoskopibilder som bildkälla. Denna dataset innehåller 200 bilder av tre klasser: typiskt nevus, atypiskt nevus och melanom. Alla bilder innehåller också en motsvarande **mask** som omger nevuset.

> ✅ Denna teknik är särskilt lämplig för denna typ av medicinsk avbildning, men vilka andra verkliga tillämpningar kan du föreställa dig?

<img alt="navi" src="images/navi.png"/>

> Bild från PH<sup>2</sup> Databas

Vi kommer att träna en modell för att segmentera vilket nevus som helst från dess bakgrund.

## ✍️ Övningar: Semantisk Segmentering

Öppna anteckningarna nedan för att lära dig mer om olika arkitekturer för semantisk segmentering, öva på att arbeta med dem och se dem i aktion.

* [Semantisk Segmentering Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Semantisk Segmentering TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Efter-lärare quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Slutsats

Segmentering är en mycket kraftfull teknik för bildklassificering, som går bortom ramar till klassificering på pixelnivå. Det är en teknik som används inom medicinsk avbildning, bland andra tillämpningar.

## 🚀 Utmaning

Kroppsegmentering är bara en av de vanliga uppgifterna vi kan utföra med bilder av människor. Andra viktiga uppgifter inkluderar **skelettdetektion** och **ställningsdetektion**. Prova [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) biblioteket för att se hur ställningsdetektion kan användas.

## Granskning & Självstudie

Denna [wikipediaartikel](https://wikipedia.org/wiki/Image_segmentation) erbjuder en bra översikt över de olika tillämpningarna av denna teknik. Lär dig mer på egen hand om underområdena för instanssegmentering och panoptisk segmentering inom detta forskningsområde.

## [Uppgift](lab/README.md)

I detta laboratorium, prova **segmentering av människokroppen** med [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) från Kaggle.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.