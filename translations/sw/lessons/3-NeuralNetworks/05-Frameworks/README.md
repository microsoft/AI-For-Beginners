# Neural Network Frameworks

Som vi redan har lärt oss, för att effektivt kunna träna neurala nätverk behöver vi göra två saker:

* Att arbeta med tensorer, t.ex. att multiplicera, addera och beräkna vissa funktioner som sigmoid eller softmax
* Att beräkna gradienter för alla uttryck, för att kunna utföra gradientnedstigning

## [För-lektion quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/105)

Medan `numpy` biblioteket kan hantera den första delen, behöver vi någon mekanism för att beräkna gradienter. I [vårt ramverk](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) som vi utvecklade i föregående avsnitt var vi tvungna att manuellt programmera alla derivatfunktioner inuti `backward` metoden, som gör backpropagation. Idealiskt sett bör ett ramverk ge oss möjlighet att beräkna gradienter av *vilket uttryck som helst* som vi kan definiera.

En annan viktig aspekt är att kunna utföra beräkningar på GPU, eller andra specialiserade beräkningsenheter, såsom [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). Träning av djupa neurala nätverk kräver *mycket* beräkningar, och att kunna parallellisera dessa beräkningar på GPU:er är mycket viktigt.

> ✅ Termen 'parallellisera' betyder att fördela beräkningarna över flera enheter.

För närvarande är de två mest populära neurala ramverken: [TensorFlow](http://TensorFlow.org) och [PyTorch](https://pytorch.org/). Båda erbjuder ett lågnivå-API för att arbeta med tensorer både på CPU och GPU. Ovanpå lågnivå-API:et finns också ett högre API, som kallas [Keras](https://keras.io/) och [PyTorch Lightning](https://pytorchlightning.ai/) respektive.

Lågnivå-API | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
--------------|-------------------------------------|--------------------------------
Högnivå-API| [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**Lågnivå-API:er** i båda ramverken låter dig bygga så kallade **beräkningsgrafer**. Denna graf definierar hur man beräknar utdata (vanligtvis förlustfunktionen) med givna indata, och kan skickas för beräkning på GPU, om det är tillgängligt. Det finns funktioner för att differentiera denna beräkningsgraf och beräkna gradienter, som sedan kan användas för att optimera modellparametrar.

**Högnivå-API:er** betraktar i stort sett neurala nätverk som en **sekvens av lager**, och gör konstruktionen av de flesta neurala nätverk mycket enklare. Att träna modellen kräver vanligtvis att man förbereder data och sedan anropar en `fit` funktion för att utföra jobbet.

Högnivå-API:et gör att du snabbt kan konstruera typiska neurala nätverk utan att behöva oroa dig för många detaljer. Samtidigt erbjuder lågnivå-API:t mycket mer kontroll över träningsprocessen, och därför används de ofta inom forskningen, när man hanterar nya arkitekturer för neurala nätverk.

Det är också viktigt att förstå att du kan använda båda API:erna tillsammans, t.ex. kan du utveckla din egen nätverkslagerarkitektur med lågnivå-API:t, och sedan använda den i det större nätverk som konstruerats och tränats med högnivå-API:t. Eller så kan du definiera ett nätverk med högnivå-API:t som en sekvens av lager, och sedan använda din egen lågnivå träningsloop för att utföra optimering. Båda API:erna använder samma grundläggande koncept och är designade för att fungera bra tillsammans.

## Lärande

I den här kursen erbjuder vi det mesta av innehållet både för PyTorch och TensorFlow. Du kan välja ditt föredragna ramverk och bara gå igenom motsvarande anteckningar. Om du är osäker på vilket ramverk du ska välja, läs några diskussioner på internet angående **PyTorch vs. TensorFlow**. Du kan också titta på båda ramverken för att få en bättre förståelse.

Där det är möjligt kommer vi att använda Högnivå-API:er för enkelhetens skull. Men vi anser att det är viktigt att förstå hur neurala nätverk fungerar från grunden, så i början börjar vi med att arbeta med lågnivå-API och tensorer. Men om du vill komma igång snabbt och inte vill spendera mycket tid på att lära dig dessa detaljer, kan du hoppa över dem och gå direkt till högnivå-API anteckningarna.

## ✍️ Övningar: Ramverk

Fortsätt ditt lärande i följande anteckningar:

Lågnivå-API | [TensorFlow+Keras Anteckning](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [PyTorch](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)
--------------|-------------------------------------|--------------------------------
Högnivå-API| [Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) | *PyTorch Lightning*

Efter att ha bemästrat ramverken, låt oss sammanfatta begreppet överanpassning.

# Överanpassning

Överanpassning är ett extremt viktigt begrepp inom maskininlärning, och det är mycket viktigt att få det rätt!

Överväg följande problem med att approximera 5 punkter (representerade av `x` på graferna nedan):

![linear](../../../../../translated_images/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.sw.jpg) | ![overfit](../../../../../translated_images/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.sw.jpg)
-------------------------|--------------------------
**Linjär modell, 2 parametrar** | **Icke-linjär modell, 7 parametrar**
Träningsfel = 5.3 | Träningsfel = 0
Valideringsfel = 5.1 | Valideringsfel = 20

* Till vänster ser vi en bra rak linje approximation. Eftersom antalet parametrar är adekvat, förstår modellen idén bakom punktfördelningen korrekt.
* Till höger är modellen för kraftfull. Eftersom vi bara har 5 punkter och modellen har 7 parametrar, kan den justera sig på ett sätt som gör att den går genom alla punkter, vilket gör träningsfelet till 0. Men detta hindrar modellen från att förstå det korrekta mönstret bakom datan, vilket gör att valideringsfelet blir mycket högt.

Det är mycket viktigt att hitta en korrekt balans mellan modellens rikedom (antal parametrar) och antalet träningsprover.

## Varför överanpassning inträffar

  * Inte tillräckligt med träningsdata
  * För kraftfull modell
  * För mycket brus i indata

## Hur man upptäcker överanpassning

Som du kan se från grafen ovan kan överanpassning upptäckas genom ett mycket lågt träningsfel och ett högt valideringsfel. Normalt under träning kommer vi att se både tränings- och valideringsfel börja minska, och sedan vid en viss punkt kan valideringsfelet sluta minska och börja öka. Detta kommer att vara ett tecken på överanpassning, och en indikator på att vi troligen bör sluta träna vid denna punkt (eller åtminstone göra en snapshot av modellen).

![overfitting](../../../../../translated_images/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.sw.png)

## Hur man förhindrar överanpassning

Om du ser att överanpassning inträffar kan du göra något av följande:

 * Öka mängden träningsdata
 * Minska modellens komplexitet
 * Använda någon [regulariseringsteknik](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), såsom [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), som vi kommer att överväga senare.

## Överanpassning och Bias-Varians Tradeoff

Överanpassning är faktiskt ett fall av ett mer generellt problem inom statistik som kallas [Bias-Varians Tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Om vi överväger de möjliga källorna till fel i vår modell kan vi se två typer av fel:

* **Biasfel** orsakas av att vår algoritm inte kan fånga relationen mellan träningsdata korrekt. Det kan bero på att vår modell inte är tillräckligt kraftfull (**underanpassning**).
* **Variansfel**, som orsakas av att modellen approximera brus i indata istället för meningsfulla relationer (**överanpassning**).

Under träning minskar biasfelet (när vår modell lär sig att approximera datan), och variansfelet ökar. Det är viktigt att stoppa träningen - antingen manuellt (när vi upptäcker överanpassning) eller automatiskt (genom att införa regularisering) - för att förhindra överanpassning.

## Slutsats

I den här lektionen lärde du dig om skillnaderna mellan de olika API:erna för de två mest populära AI-ramverken, TensorFlow och PyTorch. Dessutom lärde du dig om ett mycket viktigt ämne, överanpassning.

## 🚀 Utmaning

I de medföljande anteckningarna hittar du 'uppgifter' längst ner; arbeta igenom anteckningarna och slutför uppgifterna.

## [Efter-lektion quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/205)

## Granskning & Självstudie

Gör lite forskning om följande ämnen:

- TensorFlow
- PyTorch
- Överanpassning

Ställ dig själv följande frågor:

- Vad är skillnaden mellan TensorFlow och PyTorch?
- Vad är skillnaden mellan överanpassning och underanpassning?

## [Uppgift](lab/README.md)

I detta laboratorium ombeds du att lösa två klassificeringsproblem med hjälp av enkel- och flerlagerade fullt anslutna nätverk med PyTorch eller TensorFlow.

* [Instruktioner](lab/README.md)
* [Anteckning](../../../../../lessons/3-NeuralNetworks/05-Frameworks/lab/LabFrameworks.ipynb)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.