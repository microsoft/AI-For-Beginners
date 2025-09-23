<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b544f20b796402507fb05a0df893323",
  "translation_date": "2025-08-28T15:40:43+00:00",
  "source_file": "lessons/3-NeuralNetworks/05-Frameworks/README.md",
  "language_code": "da"
}
-->
# Neurale Netværksrammer

Som vi allerede har lært, skal vi gøre to ting for effektivt at træne neurale netværk:

* Arbejde med tensorer, f.eks. multiplicere, addere og beregne funktioner som sigmoid eller softmax
* Beregne gradienter af alle udtryk for at udføre gradient descent-optimering

## [Quiz før lektionen](https://ff-quizzes.netlify.app/en/ai/quiz/9)

Mens `numpy`-biblioteket kan håndtere den første del, har vi brug for en mekanisme til at beregne gradienter. I [vores rammeværk](../04-OwnFramework/OwnFramework.ipynb), som vi udviklede i det forrige afsnit, var vi nødt til manuelt at programmere alle afledte funktioner i `backward`-metoden, som udfører backpropagation. Ideelt set bør et rammeværk give os mulighed for at beregne gradienter af *ethvert udtryk*, vi kan definere.

En anden vigtig ting er at kunne udføre beregninger på GPU eller andre specialiserede beregningsenheder, såsom [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). Træning af dybe neurale netværk kræver *meget* beregning, og det er meget vigtigt at kunne parallelisere disse beregninger på GPU'er.

> ✅ Udtrykket 'parallelisere' betyder at fordele beregningerne over flere enheder.

De to mest populære neurale rammeværk i øjeblikket er: [TensorFlow](http://TensorFlow.org) og [PyTorch](https://pytorch.org/). Begge tilbyder et lavniveau-API til at arbejde med tensorer på både CPU og GPU. Oven på lavniveau-API'en findes der også højere niveau-API'er, kaldet [Keras](https://keras.io/) og [PyTorch Lightning](https://pytorchlightning.ai/) henholdsvis.

Lavniveau-API | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
--------------|-------------------------------------|--------------------------------
Højniveau-API | [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**Lavniveau-API'er** i begge rammeværk giver dig mulighed for at bygge såkaldte **beregningsgrafer**. Denne graf definerer, hvordan outputtet (normalt tab-funktionen) beregnes med givne inputparametre og kan sendes til beregning på GPU, hvis den er tilgængelig. Der findes funktioner til at differentiere denne beregningsgraf og beregne gradienter, som derefter kan bruges til at optimere modelparametre.

**Højniveau-API'er** betragter stort set neurale netværk som en **sekvens af lag** og gør konstruktionen af de fleste neurale netværk meget lettere. Træning af modellen kræver normalt, at man forbereder dataene og derefter kalder en `fit`-funktion for at udføre arbejdet.

Højniveau-API'en giver dig mulighed for hurtigt at konstruere typiske neurale netværk uden at bekymre dig om mange detaljer. Samtidig giver lavniveau-API'en meget mere kontrol over træningsprocessen og bruges derfor ofte i forskning, når man arbejder med nye neurale netværksarkitekturer.

Det er også vigtigt at forstå, at du kan bruge begge API'er sammen, f.eks. kan du udvikle din egen netværkslagsarkitektur ved hjælp af lavniveau-API'en og derefter bruge den i et større netværk, der er konstrueret og trænet med højniveau-API'en. Eller du kan definere et netværk ved hjælp af højniveau-API'en som en sekvens af lag og derefter bruge din egen lavniveau-træningssløjfe til at udføre optimering. Begge API'er bruger de samme grundlæggende underliggende koncepter og er designet til at fungere godt sammen.

## Læring

I dette kursus tilbyder vi det meste af indholdet både for PyTorch og TensorFlow. Du kan vælge dit foretrukne rammeværk og kun gennemgå de tilsvarende notebooks. Hvis du ikke er sikker på, hvilket rammeværk du skal vælge, kan du læse nogle diskussioner på internettet om **PyTorch vs. TensorFlow**. Du kan også kigge på begge rammeværk for at få en bedre forståelse.

Hvor det er muligt, vil vi bruge højniveau-API'er for enkelhedens skyld. Vi mener dog, at det er vigtigt at forstå, hvordan neurale netværk fungerer fra bunden, så i begyndelsen starter vi med at arbejde med lavniveau-API'er og tensorer. Hvis du dog ønsker at komme hurtigt i gang og ikke vil bruge meget tid på at lære disse detaljer, kan du springe dem over og gå direkte til notebooks med højniveau-API'er.

## ✍️ Øvelser: Rammeværk

Fortsæt din læring i følgende notebooks:

Lavniveau-API | [TensorFlow+Keras Notebook](IntroKerasTF.ipynb) | [PyTorch](IntroPyTorch.ipynb)
--------------|-------------------------------------|--------------------------------
Højniveau-API | [Keras](IntroKeras.ipynb) | *PyTorch Lightning*

Efter at have mestret rammeværkene, lad os genopfriske begrebet overfitting.

# Overfitting

Overfitting er et ekstremt vigtigt begreb inden for maskinlæring, og det er meget vigtigt at forstå det korrekt!

Overvej følgende problem med at tilnærme 5 punkter (repræsenteret ved `x` på graferne nedenfor):

![linear](../../../../../translated_images/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.da.jpg) | ![overfit](../../../../../translated_images/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.da.jpg)
-------------------------|--------------------------
**Lineær model, 2 parametre** | **Ikke-lineær model, 7 parametre**
Træningsfejl = 5,3 | Træningsfejl = 0
Valideringsfejl = 5,1 | Valideringsfejl = 20

* Til venstre ser vi en god ret linje-tilnærmelse. Fordi antallet af parametre er passende, forstår modellen punktfordelingen korrekt.
* Til højre er modellen for kraftfuld. Fordi vi kun har 5 punkter, og modellen har 7 parametre, kan den justere sig, så den passer gennem alle punkter, hvilket gør træningsfejlen til 0. Dette forhindrer dog modellen i at forstå det korrekte mønster bag dataene, og derfor er valideringsfejlen meget høj.

Det er meget vigtigt at finde den rette balance mellem modellens kompleksitet (antal parametre) og antallet af træningsprøver.

## Hvorfor opstår overfitting

  * Ikke nok træningsdata
  * For kraftfuld model
  * For meget støj i inputdata

## Hvordan opdager man overfitting

Som du kan se på grafen ovenfor, kan overfitting opdages ved en meget lav træningsfejl og en høj valideringsfejl. Normalt vil vi under træning se både trænings- og valideringsfejl begynde at falde, og derefter kan valideringsfejlen på et tidspunkt stoppe med at falde og begynde at stige. Dette vil være et tegn på overfitting og en indikator for, at vi sandsynligvis bør stoppe træningen på dette tidspunkt (eller i det mindste tage et snapshot af modellen).

![overfitting](../../../../../translated_images/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.da.png)

## Hvordan forhindrer man overfitting

Hvis du opdager, at overfitting opstår, kan du gøre en af følgende ting:

 * Øge mængden af træningsdata
 * Mindske modellens kompleksitet
 * Bruge en [regulariseringsteknik](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), såsom [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), som vi vil gennemgå senere.

## Overfitting og Bias-Variance Tradeoff

Overfitting er faktisk et tilfælde af et mere generelt problem inden for statistik kaldet [Bias-Variance Tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Hvis vi overvejer de mulige fejlkilder i vores model, kan vi se to typer fejl:

* **Bias-fejl** skyldes, at vores algoritme ikke er i stand til korrekt at fange forholdet mellem træningsdataene. Det kan skyldes, at vores model ikke er kraftfuld nok (**underfitting**).
* **Varians-fejl**, som skyldes, at modellen tilnærmer støj i inputdataene i stedet for meningsfulde sammenhænge (**overfitting**).

Under træning falder bias-fejlen (da vores model lærer at tilnærme dataene), og varians-fejlen stiger. Det er vigtigt at stoppe træningen - enten manuelt (når vi opdager overfitting) eller automatisk (ved at introducere regularisering) - for at forhindre overfitting.

## Konklusion

I denne lektion lærte du om forskellene mellem de forskellige API'er for de to mest populære AI-rammeværk, TensorFlow og PyTorch. Derudover lærte du om et meget vigtigt emne, overfitting.

## 🚀 Udfordring

I de tilhørende notebooks finder du 'opgaver' nederst; gennemgå notebooks og fuldfør opgaverne.

## [Quiz efter lektionen](https://ff-quizzes.netlify.app/en/ai/quiz/10)

## Gennemgang & Selvstudie

Undersøg følgende emner:

- TensorFlow
- PyTorch
- Overfitting

Spørg dig selv følgende spørgsmål:

- Hvad er forskellen mellem TensorFlow og PyTorch?
- Hvad er forskellen mellem overfitting og underfitting?

## [Opgave](lab/README.md)

I denne opgave skal du løse to klassifikationsproblemer ved hjælp af enkelt- og flerlags fuldt forbundne netværk med PyTorch eller TensorFlow.

* [Instruktioner](lab/README.md)
* [Notebook](lab/LabFrameworks.ipynb)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.