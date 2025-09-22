<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-28T15:36:39+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "sv"
}
-->
# Introduktion till neurala nätverk. Multi-Layered Perceptron

I föregående avsnitt lärde du dig om den enklaste modellen för neurala nätverk - enlagers perceptron, en linjär tvåklassklassificeringsmodell.

I detta avsnitt kommer vi att utöka denna modell till en mer flexibel ram, vilket gör det möjligt för oss att:

* utföra **multiklassklassificering** utöver tvåklassklassificering
* lösa **regressionsproblem** utöver klassificering
* separera klasser som inte är linjärt separerbara

Vi kommer också att utveckla vår egen modulära ram i Python som gör det möjligt för oss att konstruera olika arkitekturer för neurala nätverk.

## [Förtest inför föreläsning](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Formalisering av maskininlärning

Låt oss börja med att formalisera problemet med maskininlärning. Anta att vi har ett träningsdataset **X** med etiketter **Y**, och vi behöver bygga en modell *f* som gör de mest exakta förutsägelserna. Kvaliteten på förutsägelserna mäts med hjälp av en **förlustfunktion** ℒ. Följande förlustfunktioner används ofta:

* För regressionsproblem, när vi behöver förutsäga ett tal, kan vi använda **absolut fel** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, eller **kvadratiskt fel** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* För klassificering använder vi **0-1-förlust** (som i princip är detsamma som modellens **noggrannhet**) eller **logistisk förlust**.

För enlagers perceptron definierades funktionen *f* som en linjär funktion *f(x)=wx+b* (här är *w* viktmatrisen, *x* är vektorn av indatafunktioner, och *b* är biasvektorn). För olika arkitekturer av neurala nätverk kan denna funktion anta en mer komplex form.

> Vid klassificering är det ofta önskvärt att få sannolikheter för motsvarande klasser som nätverkets output. För att konvertera godtyckliga tal till sannolikheter (t.ex. för att normalisera outputen) använder vi ofta **softmax**-funktionen σ, och funktionen *f* blir *f(x)=σ(wx+b)*

I definitionen av *f* ovan kallas *w* och *b* för **parametrar** θ=⟨*w,b*⟩. Givet datasetet ⟨**X**,**Y**⟩ kan vi beräkna ett övergripande fel för hela datasetet som en funktion av parametrarna θ.

> ✅ **Målet med träning av neurala nätverk är att minimera felet genom att variera parametrarna θ**

## Optimering med gradientnedstigning

Det finns en välkänd metod för funktionsoptimering som kallas **gradientnedstigning**. Idén är att vi kan beräkna en derivata (i flerdimensionella fall kallad **gradient**) av förlustfunktionen med avseende på parametrarna och variera parametrarna på ett sätt som minskar felet. Detta kan formaliseras enligt följande:

* Initiera parametrarna med några slumpmässiga värden w<sup>(0)</sup>, b<sup>(0)</sup>
* Upprepa följande steg många gånger:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Under träningen ska optimeringsstegen beräknas med hänsyn till hela datasetet (kom ihåg att förlusten beräknas som en summa genom alla träningsprover). Men i verkligheten tar vi små delar av datasetet som kallas **minibatcher**, och beräknar gradienter baserat på en delmängd av data. Eftersom delmängden tas slumpmässigt varje gång kallas en sådan metod för **stokastisk gradientnedstigning** (SGD).

## Multi-Layered Perceptrons och backpropagation

Ett enlagers nätverk, som vi har sett ovan, kan klassificera linjärt separerbara klasser. För att bygga en rikare modell kan vi kombinera flera lager i nätverket. Matematiskt skulle det innebära att funktionen *f* får en mer komplex form och beräknas i flera steg:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Här är α en **icke-linjär aktiveringsfunktion**, σ är en softmax-funktion, och parametrarna är θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradientnedstigningsalgoritmen skulle förbli densamma, men det skulle vara svårare att beräkna gradienterna. Med hjälp av kedjeregeln för derivator kan vi beräkna derivator som:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Kedjeregeln används för att beräkna derivator av förlustfunktionen med avseende på parametrarna.

Observera att den vänstra delen av alla dessa uttryck är densamma, och därför kan vi effektivt beräkna derivator genom att börja från förlustfunktionen och gå "bakåt" genom beräkningsgrafen. Därför kallas metoden för att träna ett flerskiktat perceptron för **backpropagation**, eller 'backprop'.

<img alt="beräkningsgraf" src="images/ComputeGraphGrad.png"/>

> TODO: bildcitering

> ✅ Vi kommer att gå igenom backpropagation mycket mer detaljerat i vårt exempel i notebooken.  

## Slutsats

I denna lektion har vi byggt vårt eget bibliotek för neurala nätverk och använt det för en enkel tvådimensionell klassificeringsuppgift.

## 🚀 Utmaning

I den medföljande notebooken kommer du att implementera din egen ram för att bygga och träna flerskiktade perceptrons. Du kommer att kunna se i detalj hur moderna neurala nätverk fungerar.

Gå vidare till [OwnFramework](OwnFramework.ipynb) notebooken och arbeta igenom den.

## [Eftertest efter föreläsning](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Granskning och självstudier

Backpropagation är en vanlig algoritm som används inom AI och ML, värd att studera [mer i detalj](https://wikipedia.org/wiki/Backpropagation)

## [Uppgift](lab/README.md)

I detta labb ombeds du använda den ram du konstruerade i denna lektion för att lösa klassificeringen av handskrivna siffror i MNIST.

* [Instruktioner](lab/README.md)
* [Notebook](lab/MyFW_MNIST.ipynb)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som kan uppstå vid användning av denna översättning.