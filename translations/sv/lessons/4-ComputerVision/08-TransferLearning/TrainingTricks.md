# Träningsknep för djupinlärning

När neurala nätverk blir djupare blir processen att träna dem alltmer utmanande. Ett stort problem är de så kallade [försvinnande gradienterna](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) eller [exploderande gradienter](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Det här inlägget](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) ger en bra introduktion till dessa problem.

För att göra träningen av djupa nätverk mer effektiv finns det några tekniker som kan användas.

## Hålla värden inom rimliga intervall

För att göra numeriska beräkningar mer stabila vill vi säkerställa att alla värden inom vårt neurala nätverk ligger inom en rimlig skala, vanligtvis [-1..1] eller [0..1]. Det är inte ett strikt krav, men naturen hos flyttalsberäkningar är sådan att värden med olika magnituder inte kan manipuleras exakt tillsammans. Till exempel, om vi adderar 10<sup>-10</sup> och 10<sup>10</sup>, kommer vi sannolikt att få 10<sup>10</sup>, eftersom det mindre värdet "konverteras" till samma storleksordning som det större, och mantissan går förlorad.

De flesta aktiveringsfunktioner har icke-linjäriteter runt [-1..1], och därför är det vettigt att skala all indata till intervallet [-1..1] eller [0..1].

## Initial viktinitiering

Idealiskt vill vi att värdena ska ligga inom samma intervall efter att ha passerat genom nätverkslager. Därför är det viktigt att initiera vikterna på ett sätt som bevarar värdefördelningen.

Normalfördelning **N(0,1)** är inte en bra idé, eftersom om vi har *n* ingångar, skulle standardavvikelsen för utgången vara *n*, och värdena skulle sannolikt hoppa ut ur intervallet [0..1].

Följande initieringar används ofta:

 * Uniform fördelning -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** garanterar att för ingångar med medelvärde noll och standardavvikelse 1 kommer samma medelvärde/standardavvikelse att förbli
 * **N(0,√2/(n_in+n_out))** -- så kallad **Xavier-initiering** (`glorot`), den hjälper till att hålla signalerna inom intervallet under både framåt- och bakåtpropagering

## Batchnormalisering

Även med korrekt viktinitiering kan vikterna bli godtyckligt stora eller små under träningen, vilket gör att signalerna hamnar utanför rätt intervall. Vi kan återföra signalerna genom att använda en av **normaliseringsteknikerna**. Även om det finns flera (viktnormalisering, lagernormalisering), är den mest använda batchnormalisering.

Idén med **batchnormalisering** är att ta hänsyn till alla värden över minibatchen och utföra normalisering (dvs. subtrahera medelvärdet och dela med standardavvikelsen) baserat på dessa värden. Det implementeras som ett nätverkslager som gör denna normalisering efter att vikterna har applicerats, men innan aktiveringsfunktionen. Resultatet är att vi sannolikt ser högre slutlig noggrannhet och snabbare träning.

Här är [den ursprungliga artikeln](https://arxiv.org/pdf/1502.03167.pdf) om batchnormalisering, [förklaringen på Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), och [ett bra introducerande blogginlägg](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (och ett [på ryska](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** är en intressant teknik som tar bort en viss procentandel av slumpmässiga neuroner under träningen. Det implementeras också som ett lager med en parameter (procentandel neuroner att ta bort, vanligtvis 10%-50%), och under träningen nollställs slumpmässiga element i ingångsvektorn innan den skickas till nästa lager.

Även om detta kan låta som en märklig idé kan du se effekten av dropout på träningen av MNIST-sifferklassificeraren i notebook-filen [`Dropout.ipynb`](Dropout.ipynb). Det påskyndar träningen och gör att vi kan uppnå högre noggrannhet på färre träningsomgångar.

Denna effekt kan förklaras på flera sätt:

 * Det kan ses som en slumpmässig chockfaktor för modellen, som tar optimeringen ur lokala minima
 * Det kan ses som *implicit modellmedelvärde*, eftersom vi kan säga att under dropout tränar vi en något annorlunda modell

> *Vissa säger att när en berusad person försöker lära sig något, kommer han att komma ihåg det bättre nästa morgon jämfört med en nykter person, eftersom en hjärna med några felaktiga neuroner försöker anpassa sig bättre för att förstå innebörden. Vi har aldrig testat själva om detta är sant eller inte*

## Förhindra överanpassning

En av de mycket viktiga aspekterna av djupinlärning är att kunna förhindra [överanpassning](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Även om det kan vara frestande att använda en mycket kraftfull modell för neurala nätverk, bör vi alltid balansera antalet modellparametrar med antalet träningsprover.

> Se till att du förstår konceptet [överanpassning](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) som vi har introducerat tidigare!

Det finns flera sätt att förhindra överanpassning:

 * Tidigt stopp -- övervaka kontinuerligt felet på valideringsuppsättningen och stoppa träningen när valideringsfelet börjar öka.
 * Explicit viktminskning / regularisering -- lägga till en extra straff till förlustfunktionen för höga absoluta värden på vikterna, vilket förhindrar att modellen ger mycket instabila resultat
 * Modellmedelvärde -- träna flera modeller och sedan medelvärdesbilda resultatet. Detta hjälper till att minimera variansen.
 * Dropout (Implicit modellmedelvärde)

## Optimerare / Träningsalgoritmer

En annan viktig aspekt av träningen är att välja en bra träningsalgoritm. Även om klassisk **gradientnedstigning** är ett rimligt val, kan det ibland vara för långsamt eller leda till andra problem.

Inom djupinlärning använder vi **Stokastisk gradientnedstigning** (SGD), vilket är en gradientnedstigning som tillämpas på minibatcher, slumpmässigt valda från träningsuppsättningen. Vikterna justeras med denna formel:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

I **momentum SGD** behåller vi en del av gradienten från tidigare steg. Det liknar när vi rör oss någonstans med tröghet, och vi får en knuff i en annan riktning; vår bana ändras inte omedelbart utan behåller en del av den ursprungliga rörelsen. Här introducerar vi en annan vektor v för att representera *hastigheten*:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Här anger parametern γ i vilken utsträckning vi tar hänsyn till tröghet: γ=0 motsvarar klassisk SGD; γ=1 är en ren rörelseekvation.

### Adam, Adagrad, etc.

Eftersom vi i varje lager multiplicerar signaler med någon matris W<sub>i</sub>, beroende på ||W<sub>i</sub>||, kan gradienten antingen minska och vara nära 0, eller stiga oändligt. Detta är kärnan i problemet med exploderande/försvinnande gradienter.

En lösning på detta problem är att endast använda gradientens riktning i ekvationen och ignorera det absoluta värdet, dvs.

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), där ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Denna algoritm kallas **Adagrad**. Andra algoritmer som använder samma idé: **RMSProp**, **Adam**

> **Adam** anses vara en mycket effektiv algoritm för många tillämpningar, så om du är osäker på vilken du ska använda - använd Adam.

### Gradientklippning

Gradientklippning är en utvidgning av idén ovan. När ||∇ℒ|| ≤ θ, använder vi den ursprungliga gradienten i viktoptimeringen, och när ||∇ℒ|| > θ - delar vi gradienten med dess norm. Här är θ en parameter, i de flesta fall kan vi ta θ=1 eller θ=10.

### Minskning av inlärningshastighet

Träningsframgång beror ofta på parametern för inlärningshastighet η. Det är logiskt att anta att större värden på η resulterar i snabbare träning, vilket är något vi vanligtvis vill ha i början av träningen, och sedan tillåter mindre värden på η oss att finjustera nätverket. Därför vill vi i de flesta fall minska η under träningens gång.

Detta kan göras genom att multiplicera η med ett tal (t.ex. 0,98) efter varje träningsomgång, eller genom att använda en mer komplicerad **schema för inlärningshastighet**.

## Olika nätverksarkitekturer

Att välja rätt nätverksarkitektur för ditt problem kan vara knepigt. Normalt skulle vi välja en arkitektur som har visat sig fungera för vår specifika uppgift (eller en liknande). Här är en [bra översikt](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) över neurala nätverksarkitekturer för datorseende.

> Det är viktigt att välja en arkitektur som är tillräckligt kraftfull för antalet träningsprover vi har. Att välja en för kraftfull modell kan leda till [överanpassning](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Ett annat bra sätt skulle vara att använda en arkitektur som automatiskt anpassar sig till den nödvändiga komplexiteten. Till viss del är **ResNet**-arkitekturen och **Inception** självjusterande. [Mer om arkitekturer för datorseende](../07-ConvNets/CNN_Architectures.md)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.