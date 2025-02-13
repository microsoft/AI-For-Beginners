# Förtränade Nätverk och Överföringsinlärning

Att träna CNN:er kan ta mycket tid, och en stor mängd data krävs för den uppgiften. Mycket av tiden går åt till att lära sig de bästa lågnivåfiltrena som ett nätverk kan använda för att extrahera mönster från bilder. En naturlig fråga uppstår - kan vi använda ett neuralt nätverk som har tränats på en dataset och anpassa det för att klassificera olika bilder utan att behöva en fullständig träningsprocess?

## [För-föreläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/108)

Denna metod kallas **överföringsinlärning**, eftersom vi överför viss kunskap från en neuralt nätverksmodell till en annan. Vid överföringsinlärning börjar vi vanligtvis med en förtränad modell, som har tränats på en stor bilddataset, såsom **ImageNet**. Dessa modeller kan redan göra ett bra jobb med att extrahera olika egenskaper från generiska bilder, och i många fall kan det att bara bygga en klassificerare ovanpå dessa extraherade egenskaper ge ett bra resultat.

> ✅ Överföringsinlärning är ett begrepp som du hittar inom andra akademiska områden, såsom utbildning. Det hänvisar till processen att ta kunskap från ett område och tillämpa den på ett annat.

## Förtränade Modeller som Funktionsextraktorer

De konvolutionella nätverken som vi har pratat om i den föregående sektionen innehöll ett antal lager, där varje lager är avsett att extrahera vissa egenskaper från bilden, som börjar med lågnivåpixelkombinationer (såsom horisontella/vertikala linjer eller streck), upp till högre nivåkombinationer av egenskaper, motsvarande saker som ett öga på en låga. Om vi tränar CNN på en tillräckligt stor dataset av generiska och mångsidiga bilder, bör nätverket lära sig att extrahera dessa gemensamma egenskaper.

Både Keras och PyTorch innehåller funktioner för att enkelt ladda förtränade neurala nätverksvikter för vissa vanliga arkitekturer, de flesta av vilka har tränats på bilder från ImageNet. De mest använda beskrivs på sidan [CNN Arkitekturer](../07-ConvNets/CNN_Architectures.md) från den tidigare lektionen. Specifikt kan du överväga att använda en av följande:

* **VGG-16/VGG-19** som är relativt enkla modeller som fortfarande ger bra noggrannhet. Att ofta använda VGG som ett första försök är ett bra val för att se hur överföringsinlärning fungerar.
* **ResNet** är en familj av modeller som föreslagits av Microsoft Research 2015. De har fler lager och tar därför mer resurser.
* **MobileNet** är en familj av modeller med minskad storlek, lämpliga för mobila enheter. Använd dem om du har ont om resurser och kan offra lite noggrannhet.

Här är exempel på egenskaper som extraherats från en bild av en katt av VGG-16-nätverket:

![Egenskaper extraherade av VGG-16](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.sw.png)

## Katter vs. Hundar Dataset

I det här exemplet kommer vi att använda en dataset av [Katter och Hundar](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), som ligger mycket nära ett verkligt bildklassificeringsscenario.

## ✍️ Övning: Överföringsinlärning

Låt oss se överföringsinlärning i praktiken i motsvarande anteckningsböcker:

* [Överföringsinlärning - PyTorch](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb)
* [Överföringsinlärning - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb)

## Visualisering av Fiendens Katt

Det förtränade neurala nätverket innehåller olika mönster inuti sin *hjärna*, inklusive begrepp om **ideal katt** (liksom ideal hund, ideal zebra, etc.). Det skulle vara intressant att på något sätt **visualisera denna bild**. Det är dock inte enkelt, eftersom mönster är spridda över nätverksvikterna och också organiserade i en hierarkisk struktur.

En metod vi kan använda är att börja med en slumpmässig bild och sedan försöka använda **gradientnedstigningsoptimering** för att justera den bilden på ett sätt så att nätverket börjar tro att det är en katt.

![Bildoptimeringsloop](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.sw.png)

Men om vi gör detta, kommer vi att få något som liknar slumpmässigt brus. Detta beror på att *det finns många sätt att få nätverket att tro att inmatningsbilden är en katt*, inklusive vissa som inte ger visuell mening. Medan dessa bilder innehåller många mönster som är typiska för en katt, finns det inget som begränsar dem att vara visuellt distinkta.

För att förbättra resultatet kan vi lägga till en annan term i förlustfunktionen, som kallas **variationsförlust**. Det är en metrisk som visar hur lika angränsande pixlar i bilden är. Att minimera variationsförlust gör bilden jämnare och blir av med brus - vilket avslöjar mer visuellt tilltalande mönster. Här är ett exempel på sådana "ideala" bilder, som klassificeras som katt och zebra med hög sannolikhet:

![Ideal Katt](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.sw.png) | ![Ideal Zebra](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.sw.png)
-----|-----
 *Ideal Katt* | *Ideal Zebra*

En liknande metod kan användas för att utföra så kallade **fiendens attacker** på ett neuralt nätverk. Anta att vi vill lura ett neuralt nätverk och få en hund att se ut som en katt. Om vi tar en bild av en hund, som nätverket känner igen som en hund, kan vi sedan justera den lite med hjälp av gradientnedstigningsoptimering, tills nätverket börjar klassificera den som en katt:

![Bild av en Hund](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.sw.png) | ![Bild av en hund klassificerad som en katt](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.sw.png)
-----|-----
*Originalbild av en hund* | *Bild av en hund klassificerad som en katt*

Se koden för att återskapa resultaten ovan i följande anteckningsbok:

* [Ideal och Fiendens Katt - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb)

## Slutsats

Genom att använda överföringsinlärning kan du snabbt sätta ihop en klassificerare för en anpassad objektklassificeringsuppgift och uppnå hög noggrannhet. Du kan se att mer komplexa uppgifter som vi löser nu kräver högre beräkningskraft och inte enkelt kan lösas på CPU:n. I nästa enhet kommer vi att försöka använda en mer lättviktsimplementation för att träna samma modell med lägre beräkningsresurser, vilket resulterar i något lägre noggrannhet.

## 🚀 Utmaning

I de medföljande anteckningsböckerna finns det anteckningar i botten om hur överförd kunskap fungerar bäst med något liknande träningsdata (kanske en ny typ av djur). Gör några experiment med helt nya typer av bilder för att se hur bra eller dåligt dina överförda kunskapsmodeller presterar.

## [Efter-föreläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Granskning & Självstudie

Läs igenom [TrainingTricks.md](TrainingTricks.md) för att fördjupa din kunskap om några andra sätt att träna dina modeller.

## [Uppgift](lab/README.md)

I detta labb kommer vi att använda verkliga [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) husdjursdataset med 35 raser av katter och hundar, och vi kommer att bygga en överföringsinlärningsklassificerare.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.