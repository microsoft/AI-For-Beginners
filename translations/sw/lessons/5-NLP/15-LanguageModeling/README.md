# Språkmodellering

Semantiska inbäddningar, såsom Word2Vec och GloVe, är faktiskt ett första steg mot **språkmodellering** - att skapa modeller som på något sätt *förstår* (eller *representerar*) språkets natur.

## [För-lärare quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

Den huvudsakliga idén bakom språkmodellering är att träna dem på oetiketterade dataset på ett icke övervakat sätt. Detta är viktigt eftersom vi har stora mängder oetiketterad text tillgänglig, medan mängden etiketterad text alltid skulle vara begränsad av den insats vi kan lägga på att märka. Oftast kan vi bygga språkmodeller som kan **förutsäga saknade ord** i texten, eftersom det är enkelt att maskera ett slumpmässigt ord i texten och använda det som ett träningsprov.

## Träning av inbäddningar

I våra tidigare exempel använde vi förtränade semantiska inbäddningar, men det är intressant att se hur dessa inbäddningar kan tränas. Det finns flera möjliga idéer som kan användas:

* **N-Gram** språkmodellering, när vi förutsäger en token genom att titta på N föregående tokens (N-gram)
* **Kontinuerlig Bag-of-Words** (CBoW), när vi förutsäger den mittersta token $W_0$ i en tokensekvens $W_{-N}$, ..., $W_N$.
* **Skip-gram**, där vi förutsäger en uppsättning granntokens {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} från den mittersta token $W_0$.

![bild från artikel om att omvandla ord till vektorer](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.sw.png)

> Bild från [denna artikel](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Exempel Notebooks: Träning av CBoW-modell

Fortsätt din inlärning i följande notebooks:

* [Träning av CBoW Word2Vec med TensorFlow](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [Träning av CBoW Word2Vec med PyTorch](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Slutsats

I den föregående lektionen har vi sett att ordinbäddningar fungerar som magi! Nu vet vi att träning av ordinbäddningar inte är en särskilt komplex uppgift, och vi borde kunna träna våra egna ordinbäddningar för domänspecifik text om det behövs.

## [Efter-lärare quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Översyn & Självstudie

* [Officiell PyTorch-handledning om språkmodellering](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Officiell TensorFlow-handledning om träning av Word2Vec-modell](https://www.TensorFlow.org/tutorials/text/word2vec).
* Att använda **gensim**-ramverket för att träna de mest använda inbäddningarna på några få rader kod beskrivs [i denna dokumentation](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Uppgift: Träna Skip-Gram-modell](lab/README.md)

I labbet utmanar vi dig att modifiera koden från denna lektion för att träna skip-gram-modellen istället för CBoW. [Läs detaljerna](lab/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller oegentligheter. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller felaktiga tolkningar som uppstår till följd av användningen av denna översättning.