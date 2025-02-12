# Introduktion till Neurala Nätverk. Flerlagers Perceptron

I den föregående sektionen lärde du dig om den enklaste modellen för neurala nätverk - enlagers perceptron, en linjär klassificeringsmodell för två klasser.

I denna sektion kommer vi att utvidga denna modell till ett mer flexibelt ramverk, vilket gör att vi kan:

* utföra **flerklassklassificering** utöver tvåklasstillstånd
* lösa **regressionsproblem** utöver klassificering
* separera klasser som inte är linjärt separerbara

Vi kommer också att utveckla vårt eget modulära ramverk i Python som gör att vi kan konstruera olika arkitekturer för neurala nätverk.

## [För-lärare quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/104)

## Formalisering av Maskininlärning

Låt oss börja med att formalisera problemet inom Maskininlärning. Anta att vi har en träningsdataset **X** med etiketter **Y**, och vi behöver bygga en modell *f* som kommer att ge de mest exakta förutsägelserna. Kvaliteten på förutsägelserna mäts av **Förlustfunktion** ℒ. Följande förlustfunktioner används ofta:

* För regressionsproblem, när vi behöver förutsäga ett tal, kan vi använda **absolut fel** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, eller **kvadrerat fel** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* För klassificering använder vi **0-1 förlust** (som i huvudsak är detsamma som **noggrannheten** hos modellen), eller **logistisk förlust**.

För en enlags perceptron definierades funktionen *f* som en linjär funktion *f(x)=wx+b* (här är *w* viktmatrisen, *x* är vektorn av ingångsegenskaper, och *b* är biasvektorn). För olika arkitekturer av neurala nätverk kan denna funktion anta en mer komplex form.

> I fallet med klassificering är det ofta önskvärt att få sannolikheter för motsvarande klasser som nätverksutgång. För att konvertera godtyckliga tal till sannolikheter (t.ex. för att normalisera utgången) använder vi ofta **softmax** funktionen σ, och funktionen *f* blir *f(x)=σ(wx+b)*

I definitionen av *f* ovan kallas *w* och *b* för **parametrar** θ=⟨*w,b*⟩. Givet datasetet ⟨**X**,**Y**⟩ kan vi beräkna ett totalt fel på hela datasetet som en funktion av parametrarna θ.

> ✅ **Målet med träningen av det neurala nätverket är att minimera felet genom att variera parametrarna θ**

## Gradientnedstigning Optimering

Det finns en välkänd metod för funktionsoptimering som kallas **gradientnedstigning**. Idén är att vi kan beräkna en derivata (i flerdimensionellt fall kallad **gradient**) av förlustfunktionen med avseende på parametrarna, och variera parametrarna på ett sätt så att felet minskar. Detta kan formaliseras som följer:

* Initiera parametrar med några slumpmässiga värden w<sup>(0)</sup>, b<sup>(0)</sup>
* Upprepa följande steg många gånger:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Under träningen förväntas optimeringsstegen beräknas med hänsyn till hela datasetet (kom ihåg att förlusten beräknas som en summa över alla träningsprover). Men i verkligheten tar vi små portioner av datasetet som kallas **minibatcher**, och beräknar gradienter baserat på en delmängd av data. Eftersom delmängden tas slumpmässigt varje gång, kallas denna metod **stokastisk gradientnedstigning** (SGD).

## Flerlagers Perceptron och Backpropagation

En enlags nätverk, som vi har sett ovan, kan klassificera linjärt separerbara klasser. För att bygga en rikare modell kan vi kombinera flera lager av nätverket. Matematiskt skulle det innebära att funktionen *f* skulle ha en mer komplex form och beräknas i flera steg:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Här är α en **icke-linjär aktiveringsfunktion**, σ är en softmax-funktion, och parametrarna θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>* >.

Gradientnedstigningsalgoritmen skulle förbli densamma, men det skulle bli svårare att beräkna gradienter. Givet kedjederiveringsregeln kan vi beräkna derivator som:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Kedjederiveringsregeln används för att beräkna derivator av förlustfunktionen med avseende på parametrar.

Observera att den vänstra delen av alla dessa uttryck är densamma, och vi kan därför effektivt beräkna derivator som börjar från förlustfunktionen och går "bakåt" genom den beräkningsmässiga grafen. Därför kallas metoden för att träna en flerlagers perceptron för **backpropagation**, eller 'backprop'.

<img alt="beräkningsgraf" src="images/ComputeGraphGrad.png"/>

> TODO: bildcitat

> ✅ Vi kommer att täcka backprop i mycket mer detalj i vårt notebook-exempel.

## Slutsats

I denna lektion har vi byggt vårt eget bibliotek för neurala nätverk, och vi har använt det för en enkel tvådimensionell klassificeringsuppgift.

## 🚀 Utmaning

I den medföljande notebooken kommer du att implementera ditt eget ramverk för att bygga och träna flerlagers perceptron. Du kommer att kunna se i detalj hur moderna neurala nätverk fungerar.

Gå till [OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) notebooken och arbeta igenom den.

## [Efter-lärare quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/204)

## Granskning & Självstudie

Backpropagation är en vanlig algoritm som används inom AI och ML, värd att studera [i mer detalj](https://wikipedia.org/wiki/Backpropagation)

## [Uppgift](lab/README.md)

I detta labb ombeds du att använda det ramverk du konstruerade i denna lektion för att lösa klassificeringen av handskrivna siffror från MNIST.

* [Instruktioner](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiserade översättningar kan innehålla fel eller inkonsekvenser. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.