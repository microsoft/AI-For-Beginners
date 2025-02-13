# Att Representera Text som Tensors

## [För-lektionens quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Textklassificering

Under den första delen av denna sektion kommer vi att fokusera på uppgiften **textklassificering**. Vi kommer att använda [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset) dataset, som innehåller nyhetsartiklar som följande:

* Kategori: Sci/Tech
* Titel: Ky. Företag Vinner Bidrag för att Studera Peptider (AP)
* Innehåll: AP - Ett företag grundat av en kemiforskare vid University of Louisville vann ett bidrag för att utveckla...

Vårt mål kommer att vara att klassificera nyhetsartikeln i en av kategorierna baserat på texten.

## Representera text

Om vi vill lösa uppgifter inom Natural Language Processing (NLP) med neurala nätverk, behöver vi ett sätt att representera text som tensors. Datorer representerar redan texttecken som siffror som mappas till typsnitt på din skärm med hjälp av kodningar som ASCII eller UTF-8.

<img alt="Bild som visar diagram som mappar ett tecken till en ASCII- och binär representation" src="images/ascii-character-map.png" width="50%"/>

> [Bildkälla](https://www.seobility.net/en/wiki/ASCII)

Som människor förstår vi vad varje bokstav **representerar**, och hur alla tecken samverkar för att bilda orden i en mening. Datorer har dock inte en sådan förståelse av sig själva, och det neurala nätverket måste lära sig betydelsen under träningen.

Därför kan vi använda olika metoder när vi representerar text:

* **Tecken-nivå representation**, när vi representerar text genom att behandla varje tecken som en siffra. Givet att vi har *C* olika tecken i vår textkorpus, skulle ordet *Hello* representeras av en 5x*C* tensor. Varje bokstav skulle motsvara en tensor kolumn i one-hot encoding.
* **Ord-nivå representation**, där vi skapar ett **ordförråd** av alla ord i vår text, och sedan representerar orden med one-hot encoding. Denna metod är på något sätt bättre, eftersom varje bokstav i sig själv inte har mycket mening, och genom att använda högre semantiska begrepp - ord - förenklar vi uppgiften för det neurala nätverket. Men givet den stora storleken på ordförrådet måste vi hantera högdimensionella glesa tensors.

Oavsett representationen måste vi först konvertera texten till en sekvens av **tokens**, där en token kan vara antingen ett tecken, ett ord eller ibland till och med en del av ett ord. Sedan konverterar vi token till en siffra, vanligtvis med hjälp av **ordförråd**, och denna siffra kan matas in i ett neuralt nätverk med one-hot encoding.

## N-Grams

I naturligt språk kan den exakta betydelsen av ord endast bestämmas i kontext. Till exempel är betydelserna av *neural network* och *fishing network* helt olika. Ett av sätten att ta hänsyn till detta är att bygga vår modell på ordpar och betrakta ordpar som separata ordförrådstokens. På så sätt kommer meningen *I like to go fishing* att representeras av följande sekvens av tokens: *I like*, *like to*, *to go*, *go fishing*. Problemet med detta tillvägagångssätt är att ordförrådets storlek växer betydligt, och kombinationer som *go fishing* och *go shopping* representeras av olika tokens, som inte delar någon semantisk likhet trots att de har samma verb.

I vissa fall kan vi överväga att använda tri-grams -- kombinationer av tre ord -- också. Således kallas denna metod ofta för **n-grams**. Det är också meningsfullt att använda n-grams med tecken-nivå representation, i vilket fall n-grams ungefär motsvarar olika stavelser.

## Bag-of-Words och TF/IDF

När vi löser uppgifter som textklassificering, behöver vi kunna representera text med en fast storlek vektor, som vi kommer att använda som ingång till den slutliga täta klassificeraren. Ett av de enklaste sätten att göra detta är att kombinera alla individuella ordrepresentationer, t.ex. genom att addera dem. Om vi lägger till one-hot encodings av varje ord, kommer vi att få en frekvensvektor som visar hur många gånger varje ord förekommer i texten. En sådan representation av text kallas **bag of words** (BoW).

<img src="images/bow.png" width="90%"/>

> Bild av författaren

En BoW representerar i grunden vilka ord som förekommer i texten och i vilka mängder, vilket faktiskt kan vara en bra indikation på vad texten handlar om. Till exempel är en nyhetsartikel om politik sannolikt att innehålla ord som *president* och *land*, medan en vetenskaplig publikation skulle ha något som *collider*, *discovered*, etc. Således kan ordens frekvenser i många fall vara en bra indikator på textens innehåll.

Problemet med BoW är att vissa vanliga ord, som *and*, *is*, etc. förekommer i de flesta texter och har de högsta frekvenserna, vilket döljer de ord som verkligen är viktiga. Vi kan sänka vikten av dessa ord genom att ta hänsyn till frekvensen med vilken ord förekommer i hela dokumentkollektionen. Detta är den huvudsakliga idén bakom TF/IDF-metoden, som täcks mer detaljerat i anteckningarna kopplade till denna lektion.

Men ingen av dessa metoder kan helt ta hänsyn till **semantiken** i texten. Vi behöver mer kraftfulla modeller av neurala nätverk för att göra detta, vilket vi kommer att diskutera senare i denna sektion.

## ✍️ Övningar: Textrepresentation

Fortsätt din inlärning i följande anteckningar:

* [Textrepresentation med PyTorch](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb)
* [Textrepresentation med TensorFlow](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)

## Slutsats

Hittills har vi studerat tekniker som kan tilldela frekvensvikt till olika ord. De kan dock inte representera mening eller ordning. Som den berömda lingvisten J. R. Firth sa 1935, "Den fullständiga betydelsen av ett ord är alltid kontextuell, och ingen studie av betydelse bortom kontext kan tas på allvar." Vi kommer senare i kursen att lära oss hur man fångar kontextuell information från text genom språkmodellering.

## 🚀 Utmaning

Försök med några andra övningar som använder bag-of-words och olika datamodeller. Du kanske inspireras av denna [tävling på Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words)

## [Efter-lektionens quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Granskning & Självstudie

Öva dina färdigheter med textembedding och bag-of-words tekniker på [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Uppgift: Anteckningar](assignment.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.