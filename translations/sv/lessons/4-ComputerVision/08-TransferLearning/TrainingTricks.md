# Djupa inlärnings-tricks

När neurala nätverk blir djupare blir deras träningsprocess allt mer utmanande. Ett stort problem är så kallade [försvinnande gradienter](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) eller [exploderande gradienter](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Det här inlägget](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) ger en bra introduktion till dessa problem.

För att göra träningen av djupa nätverk mer effektiv finns det några tekniker som kan användas.

## Att hålla värden inom rimligt intervall

För att göra numeriska beräkningar mer stabila vill vi försäkra oss om att alla värden inom vårt neurala nätverk ligger inom en rimlig skala, typiskt [-1..1] eller [0..1]. Det är inte ett strikt krav, men naturen hos flyttalsberäkningar är sådan att värden med olika storleksordningar inte kan manipuleras korrekt tillsammans. Till exempel, om vi lägger till 10<sup>-10</sup> och 10<sup>10</sup> kommer vi troligen få 10<sup>10</sup>, eftersom det mindre värdet "konverteras" till samma storleksordning som det större, och mantissan går förlorad.

De flesta aktiveringsfunktioner har icke-lineariteter runt [-1..1], så det är vettigt att skala all indata till [-1..1] eller [0..1]-intervallet.

## Initial viktinitiering

Helst vill vi att värdena ska ligga i samma intervall efter att ha passerat genom nätverkslagren. Därför är det viktigt att initiera vikterna på ett sätt som bevarar fördelningen av värdena.

Normalfördelning **N(0,1)** är inte en bra idé, för om vi har *n* indata, skulle standardavvikelsen för utdata bli *&radic;n*, och värdena riskerar att hamna utanför [0..1]-intervallet.

Följande initialiseringar används ofta:

 * Uniform fördelning -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** garanterar att för indatavärden med noll medelvärde och standardavvikelse 1 så bibehålls samma medelvärde/standardavvikelse
 * **N(0,&radic;2/(n_in+n_out))** -- så kallad **Xavier-initialisering** (`glorot`), den hjälper till att hålla signalerna inom rätt intervall under både framåt- och bakåtpåverkan

## Batchnormalisering

Även med korrekt viktinitiering kan vikter bli godtyckligt stora eller små under träningen och driva signaler utanför rätt intervall. Vi kan få tillbaka signaler inom rätt område genom att använda någon av **normaliseringsteknikerna**. Utöver vikt-normalisering och lagsnormalisering är batchnormalisering den mest använda.

Idén med **batchnormalisering** är att ta hänsyn till alla värden över minibatchen och utföra normalisering (dvs. subtrahera medelvärde och dela med standardavvikelse) baserat på dessa värden. Det implementeras som ett nätverkslager som gör denna normalisering efter vikterna har applicerats men innan aktiveringsfunktionen. Resultatet blir ofta högre slutlig noggrannhet och snabbare träning.

Här är [ursprungspappret](https://arxiv.org/pdf/1502.03167.pdf) om batchnormalisering, [förklaringen på Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), och [ett bra introduktionsblogginlägg](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (och [ett på ryska](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** är en intressant teknik som tar bort en viss procentandel av slumpmässiga neuroner under träningen. Det implementeras också som ett lager med en parameter (procent av neuroner att ta bort, vanligtvis 10%-50%), och under träningen sätts slumpmässiga element i indata vektorn till noll innan de skickas vidare till nästa lager.

Även om detta kan låta som en konstig idé, kan du se effekten av dropout på träningen av en MNIST-sifferklassificerare i [`Dropout.ipynb`](Dropout.ipynb) notebook. Det snabbar upp träningen och gör att vi kan uppnå högre noggrannhet på färre tränings-epoker.

Denna effekt kan förklaras på flera sätt:

 * Det kan ses som en slumpmässig chockfaktor för modellen, vilket tar optimeringen bort från lokala minima
 * Det kan ses som *implicit modell-averagering*, eftersom vi kan säga att under dropout tränar vi en något annorlunda modell

> *Vissa säger att när en berusad person försöker lära sig något, kommer hen att minnas det bättre nästa morgon än en nykter person, eftersom hjärnan med några icke-fungerande neuroner försöker anpassa sig bättre för att förstå innebörden. Vi har aldrig testat om detta är sant eller inte*

## Att förebygga överanpassning

En mycket viktig aspekt inom djupinlärning är att kunna förhindra [överanpassning](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Även om det kan vara frestande att använda en mycket kraftfull nätverksmodell, bör vi alltid balansera antalet modellparametrar med antalet träningsprov.

> Se till att du förstår begreppet [överanpassning](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) som vi introducerade tidigare!

Det finns flera sätt att förhindra överanpassning:

 * Tidig stoppning -- övervaka kontinuerligt felet på valideringsset och stoppa träningen när valideringsfelet börjar öka.
 * Explicit viktavtagning / regularisering -- lägga till en extra straffterm till förlustfunktionen för höga absoluta värden på vikter, vilket förhindrar att modellen blir mycket instabil
 * Modell-averagering -- träna flera modeller och sedan ta medelvärdet av resultaten. Detta hjälper till att minimera varians.
 * Dropout (Implicit modell-averagering)

## Optimerare / träningsalgoritmer

En annan viktig aspekt av träningen är att välja bra träningsalgoritm. Även om klassisk **gradientnedstigning** är ett rimligt val kan den ibland vara för långsam eller leda till andra problem.

Inom djupinlärning använder vi **stokastisk gradientnedstigning** (SGD), som är gradientnedstigning tillämpad på minibatcher som slumpmässigt väljs ur träningssetet. Vikterna uppdateras enligt följande formel:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

I **momentum SGD** behåller vi en del av gradienten från tidigare steg. Det liknar när vi rör oss någonstans med tröghet, och får en knuff i en annan riktning – vår bana ändras inte omedelbart utan bevarar en del av den ursprungliga rörelsen. Här inför vi en annan vektor v för hastighet:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Här indikerar parametern &gamma; i vilken utsträckning vi tar hänsyn till tröghet: &gamma;=0 motsvarar klassisk SGD; &gamma;=1 är en ren rörelseekvation.

### Adam, Adagrad, osv.

Eftersom vi i varje lager multiplicerar signaler med någon matris W<sub>i</sub>, beroende på ||W<sub>i</sub>|| kan gradienten antingen avta och närma sig 0, eller växa obegränsat. Detta är kärnan i problemet med exploderande/försvinnande gradienter.

En lösning på detta problem är att använda enbart gradientens riktning i ekvationen och ignorera dess absoluta värde, dvs.

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), där ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Denna algoritm kallas **Adagrad**. Andra algoritmer som använder samma idé är **RMSProp**, **Adam**

> **Adam** anses vara en mycket effektiv algoritm för många tillämpningar, så om du är osäker på vilken du ska använda - använd Adam.

### Gradientklippning

Gradientklippning är en utvidgning av ovanstående idé. När ||&nabla;&lagran;|| &le; &theta; använder vi originalgradienten i viktoptimeringen, och när ||&nabla;&lagran;|| > &theta; delar vi gradienten med dess norm. Här är &theta; en parameter, i de flesta fall kan vi ta &theta;=1 eller &theta;=10.

### Inlärningstaktens förfall

Framgång i träning beror ofta på inlärningsparametern &eta;. Det är logiskt att anta att större värden på &eta; ger snabbare träning, vilket vi vanligtvis vill ha i början av träningen, och sedan tillåter mindre värden på &eta; oss att finjustera nätverket. Därför vill vi i de flesta fall minska &eta; under träningens gång.

Detta kan göras genom att multiplicera &eta; med ett tal (t.ex. 0,98) efter varje tränings-epok, eller genom att använda mer komplicerade **schema för inlärningstakt**.

## Olika nätverksarkitekturer

Att välja rätt nätverksarkitektur för ditt problem kan vara knepigt. Normalt väljer vi en arkitektur som har visat sig fungera för vår specifika uppgift (eller liknande). Här är en [bra översikt](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) över neurala nätverksarkitekturer för datorseende.

> Det är viktigt att välja en arkitektur som är tillräckligt kraftfull för det antal träningsprov vi har. Att välja en alltför kraftfull modell kan leda till [överanpassning](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Ett annat bra tillvägagångssätt är att använda en arkitektur som automatiskt anpassar sig till den erforderliga komplexiteten. Till en viss del är **ResNet**-arkitekturen och **Inception** självjusterande. [Mer om datorseendearkitekturer](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->