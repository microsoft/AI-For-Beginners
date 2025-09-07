<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-24T10:16:32+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "pl"
}
-->
# Modelowanie języka

Semantyczne osadzenia, takie jak Word2Vec i GloVe, to w rzeczywistości pierwszy krok w kierunku **modelowania języka** – tworzenia modeli, które w pewien sposób *rozumieją* (lub *reprezentują*) naturę języka.

## [Quiz przed wykładem](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

Główna idea modelowania języka polega na trenowaniu modeli na niezlabelowanych zbiorach danych w sposób nienadzorowany. Jest to istotne, ponieważ mamy dostęp do ogromnych ilości niezlabelowanego tekstu, podczas gdy ilość tekstu zlabelowanego zawsze będzie ograniczona wysiłkiem, jaki możemy poświęcić na jego oznaczanie. Najczęściej możemy budować modele językowe, które potrafią **przewidywać brakujące słowa** w tekście, ponieważ łatwo jest zamaskować losowe słowo w tekście i użyć go jako próbki treningowej.

## Trenowanie osadzeń

W poprzednich przykładach korzystaliśmy z wcześniej wytrenowanych semantycznych osadzeń, ale warto zobaczyć, jak można trenować takie osadzenia samodzielnie. Istnieje kilka możliwych podejść:

* **Modelowanie języka N-Gram**, gdzie przewidujemy token, patrząc na N poprzednich tokenów (N-gramy).
* **Continuous Bag-of-Words** (CBoW), gdzie przewidujemy środkowy token $W_0$ w sekwencji tokenów $W_{-N}$, ..., $W_N$.
* **Skip-gram**, gdzie przewidujemy zestaw sąsiednich tokenów {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} na podstawie środkowego tokena $W_0$.

![obraz z artykułu o konwersji słów na wektory](../../../../../lessons/5-NLP/14-Embeddings/images/example-algorithms-for-converting-words-to-vectors.png)

> Obraz z [tego artykułu](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Przykładowe notatniki: Trenowanie modelu CBoW

Kontynuuj naukę, korzystając z poniższych notatników:

* [Trenowanie CBoW Word2Vec z TensorFlow](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [Trenowanie CBoW Word2Vec z PyTorch](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Podsumowanie

W poprzedniej lekcji widzieliśmy, że osadzenia słów działają jak magia! Teraz wiemy, że trenowanie osadzeń słów nie jest bardzo skomplikowanym zadaniem i powinniśmy być w stanie wytrenować własne osadzenia słów dla tekstów specyficznych dla danej dziedziny, jeśli zajdzie taka potrzeba.

## [Quiz po wykładzie](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Przegląd i samodzielna nauka

* [Oficjalny samouczek PyTorch dotyczący modelowania języka](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Oficjalny samouczek TensorFlow dotyczący trenowania modelu Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* Użycie frameworka **gensim** do trenowania najczęściej używanych osadzeń w kilku liniach kodu opisano [w tej dokumentacji](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Zadanie: Wytrenuj model Skip-Gram](lab/README.md)

W laboratorium zachęcamy Cię do zmodyfikowania kodu z tej lekcji, aby wytrenować model skip-gram zamiast CBoW. [Przeczytaj szczegóły](lab/README.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.