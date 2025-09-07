<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-28T15:53:31+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "da"
}
-->
# Sprogsmodellering

Semantiske indlejringer, såsom Word2Vec og GloVe, er faktisk et første skridt mod **sprogsmodellering** - at skabe modeller, der på en eller anden måde *forstår* (eller *repræsenterer*) sprogets natur.

## [Quiz før lektionen](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

Hovedideen bag sprogsmodellering er at træne dem på ulabelerede datasæt på en usuperviseret måde. Dette er vigtigt, fordi vi har enorme mængder ulabeleret tekst tilgængelig, mens mængden af labeleret tekst altid vil være begrænset af den indsats, vi kan bruge på at labelere. Oftest kan vi bygge sprogsmodeller, der kan **forudsige manglende ord** i teksten, fordi det er nemt at maskere et tilfældigt ord i teksten og bruge det som en træningsprøve.

## Træning af indlejringer

I vores tidligere eksempler brugte vi fortrænede semantiske indlejringer, men det er interessant at se, hvordan disse indlejringer kan trænes. Der er flere mulige idéer, der kan bruges:

* **N-Gram** sprogsmodellering, hvor vi forudsiger et token ved at kigge på N tidligere tokens (N-gram).
* **Continuous Bag-of-Words** (CBoW), hvor vi forudsiger det midterste token $W_0$ i en token-sekvens $W_{-N}$, ..., $W_N$.
* **Skip-gram**, hvor vi forudsiger et sæt af nabotokens {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} ud fra det midterste token $W_0$.

![billede fra artikel om konvertering af ord til vektorer](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.da.png)

> Billede fra [denne artikel](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Eksempel Notebooks: Træning af CBoW-model

Fortsæt din læring i følgende notebooks:

* [Træning af CBoW Word2Vec med TensorFlow](CBoW-TF.ipynb)
* [Træning af CBoW Word2Vec med PyTorch](CBoW-PyTorch.ipynb)

## Konklusion

I den tidligere lektion har vi set, at ordindlejringer virker som magi! Nu ved vi, at træning af ordindlejringer ikke er en særlig kompleks opgave, og vi bør være i stand til at træne vores egne ordindlejringer til domænespecifik tekst, hvis det er nødvendigt.

## [Quiz efter lektionen](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Gennemgang & Selvstudie

* [Officiel PyTorch-tutorial om sprogsmodellering](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Officiel TensorFlow-tutorial om træning af Word2Vec-model](https://www.TensorFlow.org/tutorials/text/word2vec).
* Brug af **gensim**-frameworket til at træne de mest almindeligt anvendte indlejringer med få linjer kode er beskrevet [i denne dokumentation](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Opgave: Træn Skip-Gram Model](lab/README.md)

I laboratoriet udfordrer vi dig til at ændre koden fra denne lektion for at træne en skip-gram model i stedet for CBoW. [Læs detaljerne](lab/README.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.