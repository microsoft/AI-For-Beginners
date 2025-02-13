# Inbäddningar

## [För-lektion quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/114)

När vi tränade klassificerare baserade på BoW eller TF/IDF, arbetade vi med högdimensionella bag-of-words-vektorer med längd `vocab_size`, och vi konverterade uttryckligen från lågdimensionella positionsrepresentationsvektorer till glesa en-hot-representationer. Denna en-hot-representation är dock inte minneseffektiv. Dessutom behandlas varje ord oberoende av varandra, dvs. en-hot-kodade vektorer uttrycker ingen semantisk likhet mellan orden.

Idén med **inbäddning** är att representera ord med lägre dimensionella täta vektorer, som på något sätt återspeglar det semantiska betydelsen av ett ord. Vi kommer senare att diskutera hur man bygger meningsfulla ordinbäddningar, men för nu kan vi tänka på inbäddningar som ett sätt att sänka dimensionaliteten av en ordvektor.

Så inbäddningslagret skulle ta ett ord som indata och producera en utdata-vektor av specificerad `embedding_size`. På ett sätt är det mycket likt ett `Linear`-lager, men istället för att ta en en-hot-kodad vektor, kan det ta ett ordnummer som indata, vilket gör att vi kan undvika att skapa stora en-hot-kodade vektorer.

Genom att använda ett inbäddningslager som det första lagret i vårt klassificeringsnätverk kan vi växla från en bag-of-words till **inbäddningsbag**-modell, där vi först konverterar varje ord i vår text till motsvarande inbäddning och sedan beräknar en viss aggregatfunktion över alla dessa inbäddningar, såsom `sum`, `average` eller `max`.

![Bild som visar en inbäddningsklassificerare för fem sekvensord.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.sw.png)

> Bild av författaren

## ✍️ Övningar: Inbäddningar

Fortsätt ditt lärande i följande anteckningsblock:
* [Inbäddningar med PyTorch](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb)
* [Inbäddningar TensorFlow](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)

## Semantiska Inbäddningar: Word2Vec

Medan inbäddningslagret lärde sig att kartlägga ord till vektorrepresentation, hade denna representation dock inte nödvändigtvis mycket semantisk betydelse. Det skulle vara bra att lära sig en vektorrepresentation så att liknande ord eller synonymer motsvarar vektorer som ligger nära varandra i termer av viss vektordistans (t.ex. euklidisk distans).

För att göra detta behöver vi förtränar vår inbäddningsmodell på en stor samling text på ett specifikt sätt. Ett sätt att träna semantiska inbäddningar kallas [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Det baseras på två huvudarkitekturer som används för att producera en distribuerad representation av ord:

 - **Kontinuerlig bag-of-words** (CBoW) — i denna arkitektur tränar vi modellen för att förutsäga ett ord från omgivande kontext. Givet ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$, är målet för modellen att förutsäga $W_0$ från $(W_{-2},W_{-1},W_1,W_2)$.
 - **Kontinuerlig skip-gram** är motsatsen till CBoW. Modellen använder omgivande fönster av kontextord för att förutsäga det aktuella ordet.

CBoW är snabbare, medan skip-gram är långsammare, men gör ett bättre jobb med att representera sällsynta ord.

![Bild som visar både CBoW och Skip-Gram-algoritmer för att konvertera ord till vektorer.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.sw.png)

> Bild från [denna artikel](https://arxiv.org/pdf/1301.3781.pdf)

Word2Vec förtränade inbäddningar (såväl som andra liknande modeller, såsom GloVe) kan också användas istället för inbäddningslagret i neurala nätverk. Men vi behöver hantera vokabulär, eftersom vokabulären som används för att förträna Word2Vec/GloVe sannolikt skiljer sig från vokabulären i vår textkorpus. Titta på ovanstående anteckningsblock för att se hur detta problem kan lösas.

## Kontextuella Inbäddningar

En viktig begränsning av traditionella förtränade inbäddningsrepresentationer som Word2Vec är problemet med ordsensdisambiguering. Medan förtränade inbäddningar kan fånga en del av betydelsen av ord i kontext, kodas varje möjlig betydelse av ett ord in i samma inbäddning. Detta kan orsaka problem i nedströmsmodeller, eftersom många ord, såsom ordet 'play', har olika betydelser beroende på den kontext de används i.

Till exempel har ordet 'play' i dessa två olika meningar ganska olika betydelser:

- Jag gick på en **teater**.
- John vill **leka** med sina vänner.

De förtränade inbäddningarna ovan representerar båda dessa betydelser av ordet 'play' i samma inbäddning. För att övervinna denna begränsning behöver vi bygga inbäddningar baserade på **språkmodellen**, som tränas på en stor textkorpus och *vet* hur ord kan sättas ihop i olika kontexter. Att diskutera kontextuella inbäddningar ligger utanför ramen för denna handledning, men vi kommer att återkomma till dem när vi pratar om språkmodeller senare i kursen.

## Slutsats

I denna lektion upptäckte du hur man bygger och använder inbäddningslager i TensorFlow och Pytorch för att bättre återspegla de semantiska betydelserna av ord.

## 🚀 Utmaning

Word2Vec har använts för några intressanta tillämpningar, inklusive att generera låttexter och poesi. Ta en titt på [denna artikel](https://www.politetype.com/blog/word2vec-color-poems) som går igenom hur författaren använde Word2Vec för att generera poesi. Titta också på [denna video av Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) för att upptäcka en annan förklaring av denna teknik. Försök sedan att tillämpa dessa tekniker på din egen textkorpus, kanske hämtad från Kaggle.

## [Efter-lektion quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/214)

## Granskning & Självstudie

Läs igenom denna artikel om Word2Vec: [Effektiv uppskattning av ordrepresentationer i vektorutrymme](https://arxiv.org/pdf/1301.3781.pdf)

## [Uppgift: Anteckningsblock](assignment.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller oegentligheter. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller felaktiga tolkningar som uppstår till följd av användningen av denna översättning.