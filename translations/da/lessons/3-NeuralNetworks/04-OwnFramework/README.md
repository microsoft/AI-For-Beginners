<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-28T15:37:09+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "da"
}
-->
# Introduktion til Neurale Netværk. Multi-Layered Perceptron

I det forrige afsnit lærte du om den simpleste model for neurale netværk - enlaget perceptron, en lineær to-klasse klassifikationsmodel.

I dette afsnit vil vi udvide denne model til en mere fleksibel ramme, der giver os mulighed for at:

* udføre **multi-klasse klassifikation** ud over to-klasse
* løse **regressionsproblemer** ud over klassifikation
* adskille klasser, der ikke er lineært separable

Vi vil også udvikle vores egen modulære ramme i Python, som giver os mulighed for at konstruere forskellige arkitekturer for neurale netværk.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/104)

## Formalisering af Maskinlæring

Lad os starte med at formalisere problemet med maskinlæring. Antag, at vi har et træningsdatasæt **X** med labels **Y**, og vi skal bygge en model *f*, der giver de mest præcise forudsigelser. Kvaliteten af forudsigelserne måles ved **tab-funktionen** ℒ. Følgende tab-funktioner bruges ofte:

* For regressionsproblemer, hvor vi skal forudsige et tal, kan vi bruge **absolut fejl** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| eller **kvadreret fejl** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* For klassifikation bruger vi **0-1 tab** (som i bund og grund er det samme som **modellens nøjagtighed**) eller **logistisk tab**.

For enlaget perceptron blev funktionen *f* defineret som en lineær funktion *f(x)=wx+b* (her er *w* vægtmatricen, *x* er vektoren af inputfunktioner, og *b* er bias-vektoren). For forskellige arkitekturer af neurale netværk kan denne funktion antage en mere kompleks form.

> I tilfælde af klassifikation er det ofte ønskeligt at få sandsynligheder for de tilsvarende klasser som netværkets output. For at konvertere vilkårlige tal til sandsynligheder (f.eks. for at normalisere output) bruger vi ofte **softmax**-funktionen σ, og funktionen *f* bliver *f(x)=σ(wx+b)*

I definitionen af *f* ovenfor kaldes *w* og *b* **parametre** θ=⟨*w,b*⟩. Givet datasættet ⟨**X**,**Y**⟩ kan vi beregne en samlet fejl på hele datasættet som en funktion af parametrene θ.

> ✅ **Målet med træning af neurale netværk er at minimere fejlen ved at variere parametrene θ**

## Gradient Descent Optimering

Der findes en velkendt metode til optimering af funktioner kaldet **gradient descent**. Ideen er, at vi kan beregne en afledt (i det multidimensionelle tilfælde kaldet **gradient**) af tab-funktionen med hensyn til parametrene og variere parametrene på en måde, så fejlen mindskes. Dette kan formaliseres som følger:

* Initialiser parametrene med nogle tilfældige værdier w<sup>(0)</sup>, b<sup>(0)</sup>
* Gentag følgende trin mange gange:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Under træning skal optimeringstrinnene beregnes med hensyn til hele datasættet (husk, at tab beregnes som en sum gennem alle træningsprøver). Men i praksis tager vi små portioner af datasættet kaldet **minibatches** og beregner gradienter baseret på en delmængde af data. Fordi delmængden vælges tilfældigt hver gang, kaldes denne metode **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons og Backpropagation

Et enlaget netværk, som vi har set ovenfor, er i stand til at klassificere lineært separable klasser. For at bygge en rigere model kan vi kombinere flere lag i netværket. Matematisk betyder det, at funktionen *f* vil have en mere kompleks form og vil blive beregnet i flere trin:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Her er α en **ikke-lineær aktiveringsfunktion**, σ er en softmax-funktion, og parametrene θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradient descent-algoritmen forbliver den samme, men det bliver mere kompliceret at beregne gradienter. Ved hjælp af kæderegel for differentiation kan vi beregne afledte som:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Kæderegel for differentiation bruges til at beregne afledte af tab-funktionen med hensyn til parametrene.

Bemærk, at den venstre del af alle disse udtryk er den samme, og derfor kan vi effektivt beregne afledte ved at starte fra tab-funktionen og gå "baglæns" gennem beregningsgrafen. Derfor kaldes metoden til træning af en multi-layered perceptron **backpropagation**, eller 'backprop'.

<img alt="compute graph" src="images/ComputeGraphGrad.png"/>

> TODO: billedhenvisning

> ✅ Vi vil dække backpropagation meget mere detaljeret i vores notebook-eksempel.  

## Konklusion

I denne lektion har vi bygget vores egen bibliotek for neurale netværk, og vi har brugt det til en simpel todimensional klassifikationsopgave.

## 🚀 Udfordring

I den medfølgende notebook vil du implementere din egen ramme for at bygge og træne multi-layered perceptrons. Du vil kunne se i detaljer, hvordan moderne neurale netværk fungerer.

Gå videre til [OwnFramework](OwnFramework.ipynb) notebook og arbejd dig igennem den.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/204)

## Gennemgang & Selvstudie

Backpropagation er en almindelig algoritme, der bruges i AI og ML, og det er værd at studere [mere detaljeret](https://wikipedia.org/wiki/Backpropagation)

## [Opgave](lab/README.md)

I dette laboratorium bliver du bedt om at bruge den ramme, du har konstrueret i denne lektion, til at løse MNIST-håndskrevne cifre klassifikation.

* [Instruktioner](lab/README.md)
* [Notebook](lab/MyFW_MNIST.ipynb)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.