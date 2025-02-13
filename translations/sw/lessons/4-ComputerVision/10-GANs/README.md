# Generativa Motståndsnätverk

I den föregående sektionen lärde vi oss om **generativa modeller**: modeller som kan skapa nya bilder som liknar de i träningsdatasetet. VAE var ett bra exempel på en generativ modell.

## [Förläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

Men om vi försöker skapa något verkligt meningsfullt, som en målning med rimlig upplösning, med VAE, kommer vi att se att träningen inte konvergerar bra. För detta användningsfall bör vi lära oss om en annan arkitektur som är specifikt inriktad på generativa modeller - **Generativa Motståndsnätverk**, eller GANs.

Huvudidén med en GAN är att ha två neurala nätverk som kommer att tränas mot varandra:

<img src="images/gan_architecture.png" width="70%"/>

> Bild av [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Lite vokabulär:
> * **Generator** är ett nätverk som tar en slumpmässig vektor och producerar en bild som resultat
> * **Diskriminator** är ett nätverk som tar en bild och ska avgöra om det är en verklig bild (från träningsdatasetet) eller om den har genererats av en generator. Det är i grunden en bildklassificerare.

### Diskriminator

Arkitekturen för diskriminatorn skiljer sig inte från ett vanligt bildklassificeringsnätverk. I det enklaste fallet kan det vara en fullt ansluten klassificerare, men mest sannolikt kommer det att vara ett [konvolutionellt nätverk](../07-ConvNets/README.md).

> ✅ En GAN baserad på konvolutionella nätverk kallas en [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

En CNN-diskriminator består av följande lager: flera konvolutioner+pooling (med minskande spatial storlek) och ett eller flera fullt anslutna lager för att få "funktionsvektor", slutlig binär klassificerare.

> ✅ En 'pooling' i detta sammanhang är en teknik som minskar storleken på bilden. "Pooling-lager minskar dimensionerna av data genom att kombinera utgångarna från neuronkluster i ett lager till en enda neuron i nästa lager." - [källa](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generator

En generator är något mer komplicerad. Du kan betrakta den som en omvänd diskriminator. Med utgångspunkt från en latent vektor (i stället för en funktionsvektor), har den ett fullt anslutet lager för att omvandla det till den erforderliga storleken/formen, följt av dekonvolutioner+uppskalning. Detta liknar *avkodar* delen av [autoencoder](../09-Autoencoders/README.md).

> ✅ Eftersom konvolutionslagret implementeras som ett linjärt filter som rör sig över bilden, är dekonvolution i grunden liknande konvolution och kan implementeras med samma lagerlogik.

<img src="images/gan_arch_detail.png" width="70%"/>

> Bild av [Dmitry Soshnikov](http://soshnikov.com)

### Träning av GAN

GANs kallas **motståndsnätverk** eftersom det finns en konstant tävling mellan generatorn och diskriminatorn. Under denna tävling förbättras både generatorn och diskriminatorn, vilket gör att nätverket lär sig att producera bättre och bättre bilder.

Träningen sker i två steg:

* **Träning av diskriminatorn**. Denna uppgift är ganska rak på sak: vi genererar en batch av bilder med generatorn, märker dem med 0, som står för falsk bild, och tar en batch av bilder från inmatningsdatasetet (med etikett 1, verklig bild). Vi får en viss *diskriminatorförlust* och utför backprop.
* **Träning av generatorn**. Detta är något mer komplicerat, eftersom vi inte vet det förväntade resultatet för generatorn direkt. Vi tar hela GAN-nätverket bestående av en generator följd av en diskriminator, matar in den med några slumpmässiga vektorer och förväntar oss att resultatet ska vara 1 (som motsvarar verkliga bilder). Vi fryser sedan parametrarna för diskriminatorn (vi vill inte att den ska tränas i detta steg) och utför backprop.

Under denna process minskar varken generatorns eller diskriminatorns förluster signifikant. I den ideala situationen bör de oscillera, vilket motsvarar att båda nätverken förbättrar sin prestanda.

## ✍️ Övningar: GANs

* [GAN Notebook i TensorFlow/Keras](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [GAN Notebook i PyTorch](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### Problem med GAN-träning

GANs är kända för att vara särskilt svåra att träna. Här är några problem:

* **Mode Collapse**. Med denna term menar vi att generatorn lär sig att producera en framgångsrik bild som lurar diskriminatorn, och inte en variation av olika bilder.
* **Känslighet för hyperparametrar**. Ofta kan du se att en GAN inte konvergerar alls, och plötsligt minskar inlärningshastigheten vilket leder till konvergens.
* Att hålla en **balans** mellan generatorn och diskriminatorn. I många fall kan diskriminatorförlusten snabbt sjunka till noll, vilket resulterar i att generatorn inte kan tränas vidare. För att övervinna detta kan vi försöka sätta olika inlärningshastigheter för generatorn och diskriminatorn, eller hoppa över träningen av diskriminatorn om förlusten redan är för låg.
* Träning för **hög upplösning**. Detta problem speglar samma problem som med autoencoders, och utlöses eftersom rekonstruktionen av för många lager i det konvolutionella nätverket leder till artefakter. Detta problem löses vanligtvis med så kallad **progressiv tillväxt**, där först några lager tränas på låguppskattade bilder, och sedan lager "avblockeras" eller läggs till. En annan lösning skulle vara att lägga till extra kopplingar mellan lager och träna flera upplösningar samtidigt - se detta [Multi-Scale Gradient GANs-papper](https://arxiv.org/abs/1903.06048) för detaljer.

## Stilöverföring

GANs är ett utmärkt sätt att generera konstnärliga bilder. En annan intressant teknik är så kallad **stilöverföring**, som tar en **innehållsbild** och återtecknar den i en annan stil, genom att applicera filter från **stilbilden**.

Så här fungerar det:
* Vi börjar med en slumpmässig brusbild (eller med en innehållsbild, men för att förstå det är det lättare att börja med slumpmässigt brus)
* Vårt mål är att skapa en bild som ligger nära både innehållsbilden och stilbilden. Detta skulle bestämmas av två förlustfunktioner:
   - **Innehållsförlust** beräknas baserat på de funktioner som extraherats av CNN vid vissa lager från den aktuella bilden och innehållsbilden
   - **Stilförlust** beräknas mellan den aktuella bilden och stilbilden på ett smart sätt med hjälp av Gram-matriser (mer detaljer i [exempelnotebooken](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb))
* För att göra bilden jämnare och ta bort brus introducerar vi också **Variationsförlust**, som beräknar det genomsnittliga avståndet mellan närliggande pixlar
* Den huvudsakliga optimeringsloopen justerar den aktuella bilden med hjälp av gradientnedstigning (eller något annat optimeringsalgoritm) för att minimera den totala förlusten, som är en viktad summa av alla tre förluster. 

## ✍️ Exempel: [Stilöverföring](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Efterläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## Slutsats

I den här lektionen lärde du dig om GANs och hur man tränar dem. Du lärde dig också om de speciella utmaningar som denna typ av neuralt nätverk kan möta, och några strategier för hur man kan övervinna dem.

## 🚀 Utmaning

Gå igenom [Stilöverföringsnotebooken](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) med dina egna bilder.

## Granskning & Självstudier

För referens, läs mer om GANs i dessa resurser:

* Marco Pasini, [10 Lektioner Jag Lärde Mig När Jag Tränade GANs i Ett År](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), en *de facto* GAN-arkitektur att överväga
* [Skapa Generativ Konst med GANs på Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Uppgift

Återbesök en av de två notebookar som är kopplade till denna lektion och träna GAN på dina egna bilder. Vad kan du skapa?

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.