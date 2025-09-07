<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "717775c4050ccbffbe0c961ad8bf7bf7",
  "translation_date": "2025-08-28T15:14:34+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/README.md",
  "language_code": "sv"
}
-->
# Förtränade nätverk och transferinlärning

Att träna CNNs kan ta mycket tid, och det krävs en stor mängd data för den uppgiften. Dock spenderas mycket av tiden på att lära sig de bästa låg-nivå filtren som ett nätverk kan använda för att extrahera mönster från bilder. En naturlig fråga uppstår - kan vi använda ett neuralt nätverk som tränats på ett dataset och anpassa det för att klassificera andra bilder utan att behöva genomföra en fullständig träningsprocess?

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/108)

Denna metod kallas **transferinlärning**, eftersom vi överför viss kunskap från en neuralt nätverksmodell till en annan. Vid transferinlärning börjar vi vanligtvis med en förtränad modell, som har tränats på ett stort bilddataset, såsom **ImageNet**. Dessa modeller kan redan göra ett bra jobb med att extrahera olika funktioner från generiska bilder, och i många fall kan man bygga en klassificerare ovanpå dessa extraherade funktioner för att uppnå ett bra resultat.

> ✅ Transferinlärning är ett begrepp som du även hittar inom andra akademiska områden, såsom utbildning. Det hänvisar till processen att ta kunskap från ett område och tillämpa det på ett annat.

## Förtränade modeller som funktionsutvinnare

De konvolutionella nätverk som vi har pratat om i föregående avsnitt innehåller ett antal lager, där varje lager är avsett att extrahera vissa funktioner från bilden, från låg-nivå pixelkombinationer (såsom horisontella/vertikala linjer eller streck) till högre nivå kombinationer av funktioner, som motsvarar saker som ett öga eller en flamma. Om vi tränar CNN på ett tillräckligt stort dataset med generiska och varierande bilder, bör nätverket lära sig att extrahera dessa vanliga funktioner.

Både Keras och PyTorch innehåller funktioner för att enkelt ladda förtränade neurala nätverksvikter för vissa vanliga arkitekturer, varav de flesta har tränats på ImageNet-bilder. De mest använda beskrivs på sidan [CNN Architectures](../07-ConvNets/CNN_Architectures.md) från föregående lektion. I synnerhet kan du överväga att använda en av följande:

* **VGG-16/VGG-19** som är relativt enkla modeller som fortfarande ger bra noggrannhet. Att använda VGG som ett första försök är ofta ett bra val för att se hur transferinlärning fungerar.
* **ResNet** är en familj av modeller som föreslogs av Microsoft Research 2015. De har fler lager och kräver därför mer resurser.
* **MobileNet** är en familj av modeller med reducerad storlek, lämpliga för mobila enheter. Använd dem om du har begränsade resurser och kan offra lite noggrannhet.

Här är exempel på funktioner som extraherats från en bild av en katt med VGG-16-nätverket:

![Features extracted by VGG-16](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.sv.png)

## Dataset för katter och hundar

I detta exempel kommer vi att använda ett dataset med [Katter och Hundar](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), vilket är mycket nära ett verkligt scenario för bildklassificering.

## ✍️ Övning: Transferinlärning

Låt oss se transferinlärning i praktiken i motsvarande notebooks:

* [Transfer Learning - PyTorch](TransferLearningPyTorch.ipynb)
* [Transfer Learning - TensorFlow](TransferLearningTF.ipynb)

## Visualisera en "idealkatt"

Ett förtränat neuralt nätverk innehåller olika mönster i sitt *"hjärna"*, inklusive föreställningar om **idealkatt** (samt idealhund, idealzebra, etc.). Det skulle vara intressant att på något sätt **visualisera denna bild**. Dock är det inte enkelt, eftersom mönstren är spridda över nätverkets vikter och dessutom organiserade i en hierarkisk struktur.

En metod vi kan använda är att börja med en slumpmässig bild och sedan försöka använda **gradientnedstigningsoptimering** för att justera den bilden på ett sådant sätt att nätverket börjar tro att det är en katt.

![Image Optimization Loop](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.sv.png)

Men om vi gör detta kommer vi att få något som liknar slumpmässigt brus. Detta beror på att *det finns många sätt att få nätverket att tro att inmatningsbilden är en katt*, inklusive några som inte är visuellt meningsfulla. Även om dessa bilder innehåller många mönster som är typiska för en katt, finns det inget som begränsar dem till att vara visuellt distinkta.

För att förbättra resultatet kan vi lägga till en annan term i förlustfunktionen, som kallas **variationsförlust**. Det är ett mått som visar hur lika angränsande pixlar i bilden är. Genom att minimera variationsförlusten görs bilden mjukare och bruset tas bort - vilket avslöjar mer visuellt tilltalande mönster. Här är ett exempel på sådana "ideala" bilder, som klassificeras som katt och zebra med hög sannolikhet:

![Ideal Cat](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.sv.png) | ![Ideal Zebra](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.sv.png)
-----|-----
 *Idealkatt* | *Idealzebra*

En liknande metod kan användas för att utföra så kallade **adversariala attacker** på ett neuralt nätverk. Anta att vi vill lura ett neuralt nätverk och få en hund att se ut som en katt. Om vi tar en hundbild, som nätverket känner igen som en hund, kan vi sedan justera den lite med hjälp av gradientnedstigningsoptimering tills nätverket börjar klassificera den som en katt:

![Picture of a Dog](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.sv.png) | ![Picture of a dog classified as a cat](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.sv.png)
-----|-----
*Originalbild av en hund* | *Bild av en hund klassificerad som en katt*

Se koden för att reproducera resultaten ovan i följande notebook:

* [Ideal and Adversarial Cat - TensorFlow](AdversarialCat_TF.ipynb)

## Slutsats

Med hjälp av transferinlärning kan du snabbt sätta ihop en klassificerare för en anpassad objektklassificeringsuppgift och uppnå hög noggrannhet. Du kan se att mer komplexa uppgifter som vi löser nu kräver högre beräkningskraft och inte enkelt kan lösas på en CPU. I nästa enhet kommer vi att försöka använda en mer lättviktig implementation för att träna samma modell med lägre beräkningsresurser, vilket resulterar i bara något lägre noggrannhet.

## 🚀 Utmaning

I de medföljande notebooks finns det anteckningar längst ner om hur transferkunskap fungerar bäst med något liknande träningsdata (en ny typ av djur, kanske). Gör lite experiment med helt nya typer av bilder för att se hur bra eller dåligt dina transferkunskapsmodeller presterar.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Granskning & Självstudier

Läs igenom [TrainingTricks.md](TrainingTricks.md) för att fördjupa din kunskap om andra sätt att träna dina modeller.

## [Uppgift](lab/README.md)

I detta labb kommer vi att använda det verkliga [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) husdjursdatasetet med 35 raser av katter och hundar, och vi kommer att bygga en transferinlärningsklassificerare.

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.