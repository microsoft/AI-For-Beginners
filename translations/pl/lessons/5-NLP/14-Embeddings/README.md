<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e40b47ac3fd48f71304ede1474e66293",
  "translation_date": "2025-08-24T10:13:41+00:00",
  "source_file": "lessons/5-NLP/14-Embeddings/README.md",
  "language_code": "pl"
}
-->
# Osadzenia

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ai/quiz/27)

Podczas trenowania klasyfikatorów opartych na BoW lub TF/IDF operowaliśmy na wektorach worka słów o wysokiej wymiarowości o długości `vocab_size`, a także jawnie konwertowaliśmy z wektorów reprezentacji pozycyjnej o niskiej wymiarowości na rzadkie wektory one-hot. Jednakże, reprezentacja one-hot nie jest efektywna pod względem pamięci. Dodatkowo, każde słowo jest traktowane niezależnie od innych, tzn. wektory zakodowane one-hot nie wyrażają żadnego podobieństwa semantycznego między słowami.

Pomysł **osadzenia** polega na reprezentowaniu słów za pomocą gęstych wektorów o niższej wymiarowości, które w pewien sposób odzwierciedlają semantyczne znaczenie słowa. Później omówimy, jak budować znaczące osadzenia słów, ale na razie pomyślmy o osadzeniach jako o sposobie na zmniejszenie wymiarowości wektora słowa.

Warstwa osadzenia przyjmuje słowo jako wejście i generuje wektor wyjściowy o określonym `embedding_size`. W pewnym sensie jest to bardzo podobne do warstwy `Linear`, ale zamiast przyjmować wektor zakodowany one-hot, może przyjąć numer słowa jako wejście, co pozwala uniknąć tworzenia dużych wektorów zakodowanych one-hot.

Używając warstwy osadzenia jako pierwszej warstwy w naszej sieci klasyfikatora, możemy przejść od modelu worka słów do modelu **embedding bag**, w którym najpierw konwertujemy każde słowo w naszym tekście na odpowiadające mu osadzenie, a następnie obliczamy pewną funkcję agregującą dla wszystkich tych osadzeń, taką jak `sum`, `average` lub `max`.  

![Obraz przedstawiający klasyfikator osadzeń dla pięciu słów w sekwencji.](../../../../../lessons/5-NLP/14-Embeddings/images/embedding-classifier-example.png)

> Obraz autorstwa autora

## ✍️ Ćwiczenia: Osadzenia

Kontynuuj naukę w poniższych notatnikach:
* [Osadzenia z PyTorch](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb)
* [Osadzenia z TensorFlow](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)

## Semantyczne osadzenia: Word2Vec

Chociaż warstwa osadzenia nauczyła się mapować słowa na reprezentacje wektorowe, to jednak ta reprezentacja niekoniecznie miała wiele wspólnego z semantyką. Byłoby dobrze nauczyć się reprezentacji wektorowej, w której podobne słowa lub synonimy odpowiadają wektorom bliskim sobie pod względem pewnej odległości wektorowej (np. odległości euklidesowej).

Aby to osiągnąć, musimy wstępnie wytrenować nasz model osadzeń na dużym zbiorze tekstów w określony sposób. Jednym ze sposobów trenowania semantycznych osadzeń jest metoda [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Opiera się ona na dwóch głównych architekturach używanych do tworzenia rozproszonych reprezentacji słów:

 - **Ciągły worek słów** (CBoW) — w tej architekturze trenujemy model, aby przewidywał słowo na podstawie otaczającego kontekstu. Mając n-gram $(W_{-2},W_{-1},W_0,W_1,W_2)$, celem modelu jest przewidzenie $W_0$ na podstawie $(W_{-2},W_{-1},W_1,W_2)$.
 - **Ciągły skip-gram** jest odwrotnością CBoW. Model używa otaczającego okna słów kontekstowych, aby przewidzieć bieżące słowo.

CBoW jest szybszy, podczas gdy skip-gram jest wolniejszy, ale lepiej radzi sobie z reprezentowaniem rzadkich słów.

![Obraz przedstawiający algorytmy CBoW i Skip-Gram do konwersji słów na wektory.](../../../../../lessons/5-NLP/14-Embeddings/images/example-algorithms-for-converting-words-to-vectors.png)

> Obraz z [tego artykułu](https://arxiv.org/pdf/1301.3781.pdf)

Wstępnie wytrenowane osadzenia Word2Vec (jak również inne podobne modele, takie jak GloVe) mogą być również używane zamiast warstwy osadzenia w sieciach neuronowych. Musimy jednak poradzić sobie ze słownikami, ponieważ słownik używany do wstępnego trenowania Word2Vec/GloVe prawdopodobnie różni się od słownika w naszym korpusie tekstowym. Zajrzyj do powyższych notatników, aby zobaczyć, jak można rozwiązać ten problem.

## Kontekstowe osadzenia

Jednym z kluczowych ograniczeń tradycyjnych wstępnie wytrenowanych reprezentacji osadzeń, takich jak Word2Vec, jest problem rozróżniania znaczeń słów. Chociaż wstępnie wytrenowane osadzenia mogą uchwycić część znaczenia słów w kontekście, każde możliwe znaczenie słowa jest zakodowane w tym samym osadzeniu. Może to powodować problemy w modelach końcowych, ponieważ wiele słów, takich jak słowo „play”, ma różne znaczenia w zależności od kontekstu, w jakim jest używane.

Na przykład słowo „play” w tych dwóch zdaniach ma zupełnie inne znaczenie:

- Poszedłem na **sztukę** do teatru.
- John chce się **bawić** z przyjaciółmi.

Wstępnie wytrenowane osadzenia reprezentują oba te znaczenia słowa „play” w tym samym osadzeniu. Aby przezwyciężyć to ograniczenie, musimy budować osadzenia oparte na **modelu językowym**, który jest trenowany na dużym korpusie tekstów i *wie*, jak słowa mogą być używane w różnych kontekstach. Omówienie kontekstowych osadzeń wykracza poza zakres tego samouczka, ale wrócimy do nich, gdy będziemy omawiać modele językowe w dalszej części kursu.

## Podsumowanie

W tej lekcji dowiedziałeś się, jak budować i używać warstw osadzeń w TensorFlow i PyTorch, aby lepiej odzwierciedlać semantyczne znaczenia słów.

## 🚀 Wyzwanie

Word2Vec został wykorzystany w ciekawych zastosowaniach, takich jak generowanie tekstów piosenek i poezji. Zajrzyj do [tego artykułu](https://www.politetype.com/blog/word2vec-color-poems), który opisuje, jak autor użył Word2Vec do generowania poezji. Obejrzyj również [ten film Dana Shiffmanna](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain), aby poznać inne wyjaśnienie tej techniki. Następnie spróbuj zastosować te techniki do własnego korpusu tekstowego, być może pochodzącego z Kaggle.

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ai/quiz/28)

## Przegląd i samodzielna nauka

Przeczytaj ten artykuł o Word2Vec: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [Zadanie: Notatniki](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić poprawność tłumaczenia, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.