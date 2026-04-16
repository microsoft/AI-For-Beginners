# Språkmodellering

Semantiska inbäddningar, såsom Word2Vec och GloVe, är faktiskt ett första steg mot **språkmodellering** – att skapa modeller som på något sätt *förstår* (eller *representerar*) språkets natur.

## [Quiz före föreläsningen](https://ff-quizzes.netlify.app/en/ai/quiz/29)

Huvudidén bakom språkmodellering är att träna dem på oetiketterade dataset på ett osuperviserat sätt. Detta är viktigt eftersom vi har enorma mängder oetiketterad text tillgänglig, medan mängden etiketterad text alltid skulle vara begränsad av den tid och ansträngning vi kan lägga på att etikettera. Oftast kan vi bygga språkmodeller som kan **förutsäga saknade ord** i texten, eftersom det är enkelt att maskera ett slumpmässigt ord i texten och använda det som ett träningsprov.

## Träning av inbäddningar

I våra tidigare exempel använde vi förtränade semantiska inbäddningar, men det är intressant att se hur dessa inbäddningar kan tränas. Det finns flera möjliga idéer som kan användas:

* **N-Gram** språkmodellering, där vi förutspår en token genom att titta på N föregående tokens (N-gram).
* **Continuous Bag-of-Words** (CBoW), där vi förutspår den mittersta token $W_0$ i en sekvens av tokens $W_{-N}$, ..., $W_N$.
* **Skip-gram**, där vi förutspår en uppsättning närliggande tokens {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} från den mittersta token $W_0$.

![bild från artikel om att konvertera ord till vektorer](../../../../../translated_images/sv/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> Bild från [denna artikel](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Exempel på Notebooks: Träning av CBoW-modell

Fortsätt ditt lärande i följande notebooks:

* [Träning av CBoW Word2Vec med TensorFlow](CBoW-TF.ipynb)
* [Träning av CBoW Word2Vec med PyTorch](CBoW-PyTorch.ipynb)

## Slutsats

I den föregående lektionen såg vi att ordinbäddningar fungerar som magi! Nu vet vi att träning av ordinbäddningar inte är en särskilt komplex uppgift, och vi borde kunna träna våra egna ordinbäddningar för domänspecifik text om det behövs.

## [Quiz efter föreläsningen](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Granskning & Självstudier

* [Officiell PyTorch-handledning om språkmodellering](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Officiell TensorFlow-handledning om att träna Word2Vec-modell](https://www.TensorFlow.org/tutorials/text/word2vec).
* Användning av **gensim**-ramverket för att träna de mest använda inbäddningarna med några få kodrader beskrivs [i denna dokumentation](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Uppgift: Träna Skip-Gram-modell](lab/README.md)

I labbet utmanar vi dig att modifiera koden från denna lektion för att träna en skip-gram-modell istället för CBoW. [Läs detaljerna](lab/README.md)

---

