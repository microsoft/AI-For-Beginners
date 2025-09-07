<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4522e22e150be0845e03aa41209a39d5",
  "translation_date": "2025-08-24T10:15:35+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "pl"
}
-->
# Reprezentacja tekstu jako tensory

## [Quiz przed wykładem](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Klasyfikacja tekstu

W pierwszej części tego rozdziału skupimy się na zadaniu **klasyfikacji tekstu**. Wykorzystamy zbiór danych [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset), który zawiera artykuły prasowe, takie jak poniższy przykład:

* Kategoria: Nauka/Technologia  
* Tytuł: Firma z Kentucky zdobywa grant na badania nad peptydami (AP)  
* Treść: AP - Firma założona przez badacza chemii z Uniwersytetu w Louisville zdobyła grant na rozwój...

Naszym celem będzie sklasyfikowanie artykułu prasowego do jednej z kategorii na podstawie tekstu.

## Reprezentacja tekstu

Aby rozwiązywać zadania z zakresu przetwarzania języka naturalnego (NLP) za pomocą sieci neuronowych, musimy znaleźć sposób na reprezentację tekstu jako tensory. Komputery już teraz reprezentują znaki tekstowe jako liczby, które są mapowane na czcionki na ekranie, używając kodowań takich jak ASCII czy UTF-8.

<img alt="Obraz przedstawiający diagram mapujący znak na reprezentację ASCII i binarną" src="images/ascii-character-map.png" width="50%"/>

> [Źródło obrazu](https://www.seobility.net/en/wiki/ASCII)

Jako ludzie rozumiemy, co każdy znak **reprezentuje**, i jak wszystkie znaki łączą się, tworząc słowa w zdaniu. Jednak komputery same w sobie nie mają takiego zrozumienia, a sieć neuronowa musi nauczyć się znaczenia podczas treningu.

Dlatego możemy używać różnych podejść do reprezentacji tekstu:

* **Reprezentacja na poziomie znaków**, gdzie traktujemy każdy znak jako liczbę. Zakładając, że mamy *C* różnych znaków w naszym korpusie tekstowym, słowo *Hello* byłoby reprezentowane jako tensor o wymiarach 5x*C*. Każda litera odpowiadałaby kolumnie tensora w kodowaniu one-hot.  
* **Reprezentacja na poziomie słów**, w której tworzymy **słownik** wszystkich słów w naszym tekście, a następnie reprezentujemy słowa za pomocą kodowania one-hot. To podejście jest nieco lepsze, ponieważ pojedyncze litery same w sobie nie mają dużego znaczenia, a używając wyższych poziomów semantycznych - słów - upraszczamy zadanie dla sieci neuronowej. Jednak ze względu na dużą wielkość słownika musimy radzić sobie z tensorami o wysokiej wymiarowości i dużej rzadkości.

Niezależnie od wybranej reprezentacji, najpierw musimy przekształcić tekst w sekwencję **tokenów**, gdzie jeden token to znak, słowo lub czasami nawet część słowa. Następnie konwertujemy token na liczbę, zazwyczaj używając **słownika**, a ta liczba może być wprowadzona do sieci neuronowej za pomocą kodowania one-hot.

## N-Gramy

W języku naturalnym precyzyjne znaczenie słów można określić tylko w kontekście. Na przykład znaczenia *neural network* i *fishing network* są zupełnie różne. Jednym ze sposobów uwzględnienia tego jest budowanie modelu na podstawie par słów i traktowanie par słów jako oddzielnych tokenów słownika. W ten sposób zdanie *I like to go fishing* będzie reprezentowane przez następującą sekwencję tokenów: *I like*, *like to*, *to go*, *go fishing*. Problem z tym podejściem polega na tym, że rozmiar słownika znacznie rośnie, a kombinacje takie jak *go fishing* i *go shopping* są reprezentowane przez różne tokeny, które nie dzielą żadnego podobieństwa semantycznego, mimo że zawierają to samo czasownik.

W niektórych przypadkach możemy rozważyć użycie tri-gramów — kombinacji trzech słów. Dlatego podejście to często nazywane jest **n-gramami**. Sensowne jest również użycie n-gramów w reprezentacji na poziomie znaków, gdzie n-gramy będą mniej więcej odpowiadać różnym sylabom.

## Bag-of-Words i TF/IDF

Podczas rozwiązywania zadań takich jak klasyfikacja tekstu musimy być w stanie reprezentować tekst za pomocą jednego wektora o stałym rozmiarze, który będzie używany jako wejście do końcowego klasyfikatora gęstego. Jednym z najprostszych sposobów na to jest połączenie wszystkich indywidualnych reprezentacji słów, np. przez ich dodanie. Jeśli dodamy kodowania one-hot każdego słowa, otrzymamy wektor częstotliwości, pokazujący, ile razy każde słowo pojawia się w tekście. Taka reprezentacja tekstu nazywana jest **bag of words** (BoW).

<img src="images/bow.png" width="90%"/>

> Obraz autora

BoW zasadniczo reprezentuje, które słowa pojawiają się w tekście i w jakich ilościach, co może być dobrym wskaźnikiem tego, o czym jest tekst. Na przykład artykuł prasowy o polityce prawdopodobnie zawiera słowa takie jak *prezydent* i *kraj*, podczas gdy publikacja naukowa może zawierać słowa takie jak *zderzacz*, *odkryto* itp. Dlatego częstotliwości słów mogą w wielu przypadkach być dobrym wskaźnikiem treści tekstu.

Problem z BoW polega na tym, że pewne powszechne słowa, takie jak *i*, *jest* itp., pojawiają się w większości tekstów i mają najwyższe częstotliwości, maskując słowa, które są naprawdę ważne. Możemy obniżyć znaczenie tych słów, biorąc pod uwagę częstotliwość ich występowania w całej kolekcji dokumentów. To główna idea podejścia TF/IDF, które jest omówione bardziej szczegółowo w notatnikach dołączonych do tej lekcji.

Jednak żadne z tych podejść nie jest w stanie w pełni uwzględnić **semantyki** tekstu. Do tego potrzebujemy bardziej zaawansowanych modeli sieci neuronowych, które omówimy później w tym rozdziale.

## ✍️ Ćwiczenia: Reprezentacja tekstu

Kontynuuj naukę w poniższych notatnikach:

* [Reprezentacja tekstu z PyTorch](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb)  
* [Reprezentacja tekstu z TensorFlow](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)

## Podsumowanie

Jak dotąd poznaliśmy techniki, które mogą dodać wagę częstotliwości do różnych słów. Nie są one jednak w stanie reprezentować znaczenia ani kolejności. Jak powiedział słynny językoznawca J. R. Firth w 1935 roku: "Pełne znaczenie słowa zawsze jest kontekstowe, a żadna analiza znaczenia poza kontekstem nie może być traktowana poważnie." W dalszej części kursu nauczymy się, jak uchwycić informacje kontekstowe z tekstu za pomocą modelowania języka.

## 🚀 Wyzwanie

Spróbuj innych ćwiczeń z użyciem bag-of-words i różnych modeli danych. Możesz zainspirować się tą [konkursem na Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words)

## [Quiz po wykładzie](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Przegląd i samodzielna nauka

Ćwicz swoje umiejętności z technikami osadzania tekstu i bag-of-words na [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Zadanie: Notatniki](assignment.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.