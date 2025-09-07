<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-28T20:00:08+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "nl"
}
-->
# Taalmodellering

Semantische embeddings, zoals Word2Vec en GloVe, vormen eigenlijk een eerste stap richting **taalmodellering** - het creëren van modellen die op een bepaalde manier de aard van taal *begrijpen* (of *weergeven*).

## [Quiz vóór de les](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

Het belangrijkste idee achter taalmodellering is om modellen te trainen op niet-gelabelde datasets op een onbegeleide manier. Dit is belangrijk omdat we enorme hoeveelheden niet-gelabelde tekst beschikbaar hebben, terwijl de hoeveelheid gelabelde tekst altijd beperkt zal zijn door de inspanning die nodig is om deze te labelen. Meestal kunnen we taalmodellen bouwen die **ontbrekende woorden** in de tekst kunnen voorspellen, omdat het eenvoudig is om een willekeurig woord in een tekst te maskeren en dit als trainingsvoorbeeld te gebruiken.

## Embeddings trainen

In onze eerdere voorbeelden hebben we gebruik gemaakt van voorgetrainde semantische embeddings, maar het is interessant om te zien hoe deze embeddings getraind kunnen worden. Er zijn verschillende mogelijke ideeën die kunnen worden gebruikt:

* **N-Gram** taalmodellering, waarbij we een token voorspellen door te kijken naar de N voorgaande tokens (N-gram).
* **Continuous Bag-of-Words** (CBoW), waarbij we de middelste token $W_0$ voorspellen in een reeks tokens $W_{-N}$, ..., $W_N$.
* **Skip-gram**, waarbij we een set van naburige tokens {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} voorspellen vanuit de middelste token $W_0$.

![afbeelding uit een paper over het omzetten van woorden naar vectoren](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.nl.png)

> Afbeelding uit [deze paper](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Voorbeeld Notebooks: CBoW-model trainen

Ga verder met leren in de volgende notebooks:

* [CBoW Word2Vec trainen met TensorFlow](CBoW-TF.ipynb)
* [CBoW Word2Vec trainen met PyTorch](CBoW-PyTorch.ipynb)

## Conclusie

In de vorige les hebben we gezien dat woordembeddings bijna magisch werken! Nu weten we dat het trainen van woordembeddings geen heel complexe taak is, en we zouden in staat moeten zijn om onze eigen woordembeddings te trainen voor domeinspecifieke teksten indien nodig.

## [Quiz na de les](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Herhaling & Zelfstudie

* [Officiële PyTorch-tutorial over taalmodellering](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Officiële TensorFlow-tutorial over het trainen van een Word2Vec-model](https://www.TensorFlow.org/tutorials/text/word2vec).
* Het gebruik van het **gensim**-framework om de meest gebruikte embeddings te trainen in slechts een paar regels code wordt beschreven [in deze documentatie](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Opdracht: Train Skip-Gram Model](lab/README.md)

In het lab dagen we je uit om de code uit deze les aan te passen om een skip-gram model te trainen in plaats van CBoW. [Lees de details](lab/README.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.