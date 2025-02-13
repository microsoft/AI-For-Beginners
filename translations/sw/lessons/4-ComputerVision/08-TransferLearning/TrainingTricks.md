# Djupinlärningstricks för träning

När neurala nätverk blir djupare blir träningsprocessen mer och mer utmanande. Ett stort problem är så kallade [försvinnande gradienter](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) eller [exploderande gradienter](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Detta inlägg](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) ger en bra introduktion till dessa problem.

För att göra träningen av djupa nätverk mer effektiv finns det några tekniker som kan användas.

## Hålla värden inom rimligt intervall

För att göra numeriska beräkningar mer stabila vill vi säkerställa att alla värden inom vårt neurala nätverk ligger inom ett rimligt intervall, typiskt [-1..1] eller [0..1]. Det är inte ett mycket strikt krav, men naturen av flyttalsberäkningar är sådan att värden av olika magnituder inte kan manipuleras tillsammans på ett exakt sätt. Till exempel, om vi lägger till 10<sup>-10</sup> och 10<sup>10</sup>, är vi troligen att få 10<sup>10</sup>, eftersom det mindre värdet skulle "konverteras" till samma ordning som det större, och därmed skulle mantissan gå förlorad.

De flesta aktiveringsfunktioner har icke-linjäriteter runt [-1..1], och därför är det rimligt att skala all indata till [-1..1] eller [0..1] intervall.

## Initial Viktinitialisering

Idealiskt vill vi att värdena ska ligga inom samma intervall efter att ha passerat genom nätverkslager. Därför är det viktigt att initiera vikterna på ett sätt som bevarar värdesfördelningen.

Normalfördelning **N(0,1)** är inte en bra idé, eftersom om vi har *n* ingångar, skulle standardavvikelsen av utdata vara *n*, och värden är troligen att hoppa utanför [0..1] intervallet.

Följande initialiseringar används ofta:

 * Uniform fördelning -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** garanterar att för ingångar med noll medelvärde och standardavvikelse 1, skulle samma medelvärde/standardavvikelse förbli
 * **N(0,√2/(n_in+n_out))** -- så kallad **Xavier-initialisering** (`glorot`), det hjälper till att hålla signalerna inom intervallet under både framåt- och bakåtspridning

## Batchnormalisering

Även med korrekt viktinitialisering kan vikterna bli godtyckligt stora eller små under träningen, och de kommer att föra signaler utanför rätt intervall. Vi kan föra tillbaka signalerna genom att använda en av **normaliseringsteknikerna**. Medan det finns flera av dem (Viktnormalisering, Lagernormalisering), är den mest använda Batchnormalisering.

Idén med **batchnormalisering** är att ta hänsyn till alla värden över minibatchen och utföra normalisering (dvs. subtrahera medelvärde och dela med standardavvikelse) baserat på dessa värden. Det implementeras som ett nätverkslager som gör denna normalisering efter att vikterna har tillämpats, men före aktiveringsfunktionen. Som ett resultat är vi troligen att se högre slutlig noggrannhet och snabbare träning.

Här är den [ursprungliga artikeln](https://arxiv.org/pdf/1502.03167.pdf) om batchnormalisering, [förklaringen på Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), och [ett bra introducerande blogginlägg](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (och den [på ryska](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** är en intressant teknik som tar bort en viss procentandel av slumpmässiga neuroner under träningen. Det implementeras också som ett lager med en parameter (procentandel av neuroner att ta bort, typiskt 10%-50%), och under träningen nollställer det slumpmässiga element av ingångsvektorn innan den skickas till nästa lager.

Även om detta kan låta som en konstig idé, kan du se effekten av dropout på träningen av MNIST-sifferklassificeraren i [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb) anteckningen. Det påskyndar träningen och gör att vi kan uppnå högre noggrannhet på färre träningsomgångar.

Denna effekt kan förklaras på flera sätt:

 * Det kan ses som en slumpmässig chockerande faktor för modellen, som tar optimering ut ur lokala minimum
 * Det kan ses som *implicit modellgenomsnitt*, eftersom vi kan säga att under dropout tränar vi en något annan modell

> *Vissa människor säger att när en berusad person försöker lära sig något, kommer han att minnas detta bättre nästa morgon, jämfört med en nykter person, eftersom en hjärna med vissa defekta neuroner försöker anpassa sig bättre för att förstå betydelsen. Vi har aldrig testat oss själva om detta är sant eller inte*

## Förhindra överanpassning

En av de mycket viktiga aspekterna av djupinlärning är att kunna förhindra [överanpassning](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Även om det kan vara frestande att använda en mycket kraftfull neurala nätverksmodell, bör vi alltid balansera antalet modellparametrar med antalet träningsprover.

> Se till att du förstår konceptet [överanpassning](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) som vi har introducerat tidigare!

Det finns flera sätt att förhindra överanpassning:

 * Tidig stoppning -- kontinuerligt övervaka fel på valideringsuppsättningen och stoppa träningen när valideringsfelet börjar öka.
 * Explicit Viktavklingning / Regularisering -- lägga till en extra straffavgift till förlustfunktionen för höga absoluta värden av vikterna, vilket förhindrar att modellen får mycket instabila resultat
 * Modellgenomsnitt -- träna flera modeller och sedan genomsnitt resultatet. Detta hjälper till att minimera variansen.
 * Dropout (Implicit Modellgenomsnitt)

## Optimerare / Träningsalgoritmer

En annan viktig aspekt av träning är att välja en bra träningsalgoritm. Medan klassisk **gradientnedstigning** är ett rimligt val, kan det ibland vara för långsamt eller resultera i andra problem.

Inom djupinlärning använder vi **Stokastisk Gradientnedstigning** (SGD), som är en gradientnedstigning tillämpad på minibatcher, slumpmässigt valda från träningsuppsättningen. Vikterna justeras med hjälp av denna formel:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

I **momentum SGD**, behåller vi en del av en gradient från tidigare steg. Det är liknande som när vi rör oss någonstans med tröghet, och vi får ett slag i en annan riktning, vår bana ändras inte omedelbart, utan behåller en del av den ursprungliga rörelsen. Här introducerar vi en annan vektor v för att representera *hastighet*:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Här indikerar parametern γ i vilken utsträckning vi tar hänsyn till tröghet: γ=0 motsvarar klassisk SGD; γ=1 är en ren rörelseekvation.

### Adam, Adagrad, etc.

Eftersom vi i varje lager multiplicerar signaler med en viss matris W<sub>i</sub>, beroende på ||W<sub>i</sub>||, kan gradienten antingen minska och vara nära 0, eller stiga oändligt. Det är essensen av problemet med Exploderande/Försvinnande Gradienter.

En av lösningarna på detta problem är att endast använda riktningen av gradienten i ekvationen och ignorera det absoluta värdet, dvs.

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), där ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Denna algoritm kallas **Adagrad**. Andra algoritmer som använder samma idé: **RMSProp**, **Adam**

> **Adam** anses vara en mycket effektiv algoritm för många tillämpningar, så om du är osäker på vilken du ska använda - använd Adam.

### Gradientklippning

Gradientklippning är en förlängning av idén ovan. När ||∇ℒ|| ≤ θ, beaktar vi den ursprungliga gradienten i viktoptimeringen, och när ||∇ℒ|| > θ - delar vi gradienten med sin norm. Här är θ en parameter, i de flesta fall kan vi ta θ=1 eller θ=10.

### Inlärningshastighetsavtagning

Träningsframgång beror ofta på inlärningshastighetsparametern η. Det är logiskt att anta att större värden av η resulterar i snabbare träning, vilket är något vi typiskt vill i början av träningen, och sedan mindre värde av η gör att vi kan finjustera nätverket. Därför vill vi i de flesta fall minska η under träningsprocessen.

Detta kan göras genom att multiplicera η med något nummer (t.ex. 0.98) efter varje träningsomgång, eller genom att använda en mer komplicerad **inlärningshastighetsplan**.

## Olika nätverksarkitekturer

Att välja rätt nätverksarkitektur för ditt problem kan vara knepigt. Normalt skulle vi ta en arkitektur som har visat sig fungera för vår specifika uppgift (eller en liknande). Här är en [bra översikt](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) av neurala nätverksarkitekturer för datorvision.

> Det är viktigt att välja en arkitektur som är tillräckligt kraftfull för det antal träningsprover vi har. Att välja en för kraftfull modell kan resultera i [överanpassning](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Ett annat bra sätt skulle vara att använda en arkitektur som automatiskt justerar sig till den erforderliga komplexiteten. I viss utsträckning är **ResNet**-arkitekturen och **Inception** självjusterande. [Mer om datorvisionsarkitekturer](../07-ConvNets/CNN_Architectures.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller felaktiga tolkningar som uppstår till följd av användningen av denna översättning.