# Kännedomsigenkänning

Hittills har vi mest fokuserat på en NLP-uppgift - klassificering. Det finns dock även andra NLP-uppgifter som kan utföras med neurala nätverk. En av dessa uppgifter är **[Kännedomsigenkänning](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), som handlar om att känna igen specifika enheter inom text, såsom platser, personnamn, datum- och tidsintervall, kemiska formler och så vidare.

## [Förläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## Exempel på att använda NER

Anta att du vill utveckla en naturlig språk-chattbot, liknande Amazon Alexa eller Google Assistant. Sättet som intelligenta chattbotar fungerar på är att *förstå* vad användaren vill genom att göra textklassificering på den inmatade meningen. Resultatet av denna klassificering kallas **avsikt**, vilket avgör vad en chattbot ska göra.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Bild av författaren

Men en användare kan ange vissa parametrar som en del av frasen. Till exempel, när hon frågar efter vädret, kan hon specificera en plats eller ett datum. En bot bör kunna förstå dessa enheter och fylla i parameterplatserna i enlighet med detta innan den utför åtgärden. Det är precis här som NER kommer in.

> ✅ Ett annat exempel skulle vara [analys av vetenskapliga medicinska artiklar](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). En av de viktigaste sakerna vi behöver leta efter är specifika medicinska termer, såsom sjukdomar och medicinska ämnen. Medan ett litet antal sjukdomar troligen kan extraheras med hjälp av delsträngsökning, behöver mer komplexa enheter, såsom kemiska föreningar och medicinernamn, en mer komplex metod.

## NER som tokenklassificering

NER-modeller är i grunden **tokenklassificeringsmodeller**, eftersom vi för varje inmatad token måste avgöra om den tillhör en enhet eller inte, och om den gör det - till vilken enhetsklass.

Överväg följande artikelrubrik:

**Trikuspidalventilinsufficiens** och **litiumkarbonat** **toxicitet** hos ett nyfött barn.

Enheterna här är:

* Trikuspidalventilinsufficiens är en sjukdom (`DIS`)
* Litiumkarbonat är ett kemiskt ämne (`CHEM`)
* Toxicitet är också en sjukdom (`DIS`)

Observera att en enhet kan sträcka sig över flera tokens. Och, som i detta fall, behöver vi särskilja mellan två på varandra följande enheter. Därför är det vanligt att använda två klasser för varje enhet - en som specificerar den första token av enheten (ofta används `B-` prefixet, för **b**örjan), och en annan - fortsättningen av en enhet (`I-`, för **i**nner token). Vi använder också `O` som en klass för att representera alla **o**tra tokens. Sådan tokenmärkning kallas [BIO-märkning](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (eller IOB). När den är märkt ser vår rubrik ut så här:

Token | Tag
------|-----
Trikuspidal | B-DIS
ventil | I-DIS
insufficiens | I-DIS
och | O
litium | B-CHEM
karbonat | I-CHEM
toxicitet | B-DIS
hos | O
ett | O
nyfött | O
barn | O
. | O

Eftersom vi behöver bygga en en-till-en-koppling mellan tokens och klasser, kan vi träna en högra **många-till-många** neurala nätverksmodell från denna bild:

![Bild som visar vanliga mönster för återkommande neurala nätverk.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.sw.jpg)

> *Bild från [detta blogginlägg](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) av [Andrej Karpathy](http://karpathy.github.io/). NER-tokenklassificeringsmodeller motsvarar den högra nätverksarkitekturen på denna bild.*

## Träning av NER-modeller

Eftersom en NER-modell i grunden är en tokenklassificeringsmodell, kan vi använda RNN:er som vi redan är bekanta med för denna uppgift. I det här fallet kommer varje block av det återkommande nätverket att returnera token-ID. Det följande exempelnotebooket visar hur man tränar LSTM för tokenklassificering.

## ✍️ Exempelnotebookar: NER

Fortsätt ditt lärande i följande notebook:

* [NER med TensorFlow](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Slutsats

En NER-modell är en **tokenklassificeringsmodell**, vilket innebär att den kan användas för att utföra tokenklassificering. Detta är en mycket vanlig uppgift inom NLP, som hjälper till att känna igen specifika enheter inom text inklusive platser, namn, datum och mer.

## 🚀 Utmaning

Slutför uppgiften som länkas nedan för att träna en modell för kännedomsigenkänning av medicinska termer, och prova sedan på en annan dataset.

## [Efterläsningsquiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Granskning & Självstudie

Läs igenom bloggen [Den orimliga effektiviteten av återkommande neurala nätverk](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) och följ med i avsnittet Fördjupad läsning i den artikeln för att fördjupa din kunskap.

## [Uppgift](lab/README.md)

I uppgiften för denna lektion kommer du att behöva träna en modell för medicinsk enhetsigenkänning. Du kan börja med att träna en LSTM-modell som beskrivs i denna lektion, och fortsätta med att använda BERT-transformermodellen. Läs [instruktionerna](lab/README.md) för att få alla detaljer.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår på grund av användningen av denna översättning.