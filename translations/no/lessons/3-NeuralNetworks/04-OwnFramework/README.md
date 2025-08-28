<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-28T15:37:32+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "no"
}
-->
# Introduksjon til nevrale nettverk. Multi-lags perceptron

I forrige seksjon lærte du om den enkleste modellen for nevrale nettverk - enlags perceptron, en lineær to-klasse klassifikasjonsmodell.

I denne seksjonen vil vi utvide denne modellen til et mer fleksibelt rammeverk som lar oss:

* utføre **multi-klasse klassifikasjon** i tillegg til to-klasse
* løse **regresjonsproblemer** i tillegg til klassifikasjon
* skille klasser som ikke er lineært separerbare

Vi vil også utvikle vårt eget modulære rammeverk i Python som lar oss konstruere ulike arkitekturer for nevrale nettverk.

## [Quiz før forelesning](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/104)

## Formalisering av maskinlæring

La oss starte med å formalisere problemet innen maskinlæring. Anta at vi har et treningsdatasett **X** med etiketter **Y**, og vi trenger å bygge en modell *f* som gir de mest nøyaktige prediksjonene. Kvaliteten på prediksjonene måles ved hjelp av en **tapfunksjon** ℒ. Følgende tapfunksjoner brukes ofte:

* For regresjonsproblemer, når vi trenger å forutsi et tall, kan vi bruke **absolutt feil** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, eller **kvadratisk feil** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* For klassifikasjon bruker vi **0-1 tap** (som i hovedsak er det samme som **nøyaktighet** til modellen), eller **logistisk tap**.

For enlags perceptron ble funksjonen *f* definert som en lineær funksjon *f(x)=wx+b* (her er *w* vektormatrise, *x* er vektoren av inngangsfunksjoner, og *b* er bias-vektor). For ulike arkitekturer av nevrale nettverk kan denne funksjonen ta en mer kompleks form.

> I tilfelle klassifikasjon er det ofte ønskelig å få sannsynligheter for de tilsvarende klassene som nettverksutgang. For å konvertere vilkårlige tall til sannsynligheter (f.eks. for å normalisere utgangen), bruker vi ofte **softmax**-funksjonen σ, og funksjonen *f* blir *f(x)=σ(wx+b)*

I definisjonen av *f* ovenfor kalles *w* og *b* **parametere** θ=⟨*w,b*⟩. Gitt datasettet ⟨**X**,**Y**⟩, kan vi beregne en samlet feil for hele datasettet som en funksjon av parametrene θ.

> ✅ **Målet med trening av nevrale nettverk er å minimere feilen ved å variere parametrene θ**

## Gradientnedstigningsoptimalisering

Det finnes en velkjent metode for funksjonsoptimalisering kalt **gradientnedstigning**. Ideen er at vi kan beregne en deriverte (i flerdimensjonale tilfeller kalt **gradient**) av tapfunksjonen med hensyn til parametrene, og variere parametrene slik at feilen reduseres. Dette kan formaliseres som følger:

* Initialiser parametrene med noen tilfeldige verdier w<sup>(0)</sup>, b<sup>(0)</sup>
* Gjenta følgende steg mange ganger:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Under treningen skal optimaliseringsstegene beregnes med tanke på hele datasettet (husk at tapet beregnes som en sum gjennom alle treningsprøver). I praksis tar vi imidlertid små deler av datasettet kalt **minibatcher**, og beregner gradienter basert på et delsett av data. Fordi delsettet velges tilfeldig hver gang, kalles en slik metode **stokastisk gradientnedstigning** (SGD).

## Multi-lags perceptron og backpropagation

Ettlags nettverk, som vi har sett ovenfor, er i stand til å klassifisere lineært separerbare klasser. For å bygge en rikere modell kan vi kombinere flere lag i nettverket. Matematisk betyr dette at funksjonen *f* vil ha en mer kompleks form og beregnes i flere steg:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Her er α en **ikke-lineær aktiveringsfunksjon**, σ er en softmax-funksjon, og parametrene θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradientnedstigningsalgoritmen forblir den samme, men det blir mer utfordrende å beregne gradientene. Ved hjelp av kjederegelen for derivasjon kan vi beregne derivatene som:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Kjederegelen for derivasjon brukes til å beregne derivater av tapfunksjonen med hensyn til parametrene.

Merk at den venstre delen av alle disse uttrykkene er den samme, og derfor kan vi effektivt beregne derivatene ved å starte fra tapfunksjonen og gå "bakover" gjennom beregningsgrafen. Dermed kalles metoden for å trene et multi-lags perceptron **backpropagation**, eller 'backprop'.

<img alt="beregningsgraf" src="images/ComputeGraphGrad.png"/>

> TODO: bildehenvisning

> ✅ Vi vil dekke backpropagation i mye større detalj i vårt notatbokeksempel.  

## Konklusjon

I denne leksjonen har vi bygget vårt eget bibliotek for nevrale nettverk, og vi har brukt det til en enkel todimensjonal klassifikasjonsoppgave.

## 🚀 Utfordring

I den medfølgende notatboken vil du implementere ditt eget rammeverk for å bygge og trene multi-lags perceptron. Du vil kunne se i detalj hvordan moderne nevrale nettverk fungerer.

Gå videre til [OwnFramework](OwnFramework.ipynb)-notatboken og arbeid deg gjennom den.

## [Quiz etter forelesning](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/204)

## Gjennomgang og selvstudium

Backpropagation er en vanlig algoritme brukt i AI og maskinlæring, og det er verdt å studere [mer i detalj](https://wikipedia.org/wiki/Backpropagation)

## [Oppgave](lab/README.md)

I denne laben blir du bedt om å bruke rammeverket du konstruerte i denne leksjonen til å løse MNIST-håndskrevet sifferklassifikasjon.

* [Instruksjoner](lab/README.md)
* [Notatbok](lab/MyFW_MNIST.ipynb)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.