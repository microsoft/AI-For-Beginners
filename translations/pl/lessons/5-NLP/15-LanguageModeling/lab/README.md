# Trenowanie modelu Skip-Gram

Zadanie laboratoryjne z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Zadanie

W tym laboratorium wyzwaniem dla Ciebie jest wytrenowanie modelu Word2Vec przy użyciu techniki Skip-Gram. Wytrenuj sieć z osadzaniem (embedding), aby przewidywać sąsiadujące słowa w oknie Skip-Gram o szerokości $N$ tokenów. Możesz użyć [kodu z tej lekcji](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) i nieco go zmodyfikować.

## Zbiór danych

Możesz użyć dowolnej książki. Wiele darmowych tekstów znajdziesz na stronie [Project Gutenberg](https://www.gutenberg.org/), na przykład tutaj jest bezpośredni link do [Alicji w Krainie Czarów](https://www.gutenberg.org/files/11/11-0.txt) Lewisa Carrolla. Możesz też skorzystać z dramatów Szekspira, które możesz pobrać za pomocą poniższego kodu:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Eksploruj!

Jeśli masz czas i chcesz zgłębić temat, spróbuj zbadać kilka kwestii:

* Jak rozmiar osadzania wpływa na wyniki?
* Jak różne style tekstu wpływają na rezultat?
* Weź kilka bardzo różnych typów słów i ich synonimy, uzyskaj ich reprezentacje wektorowe, zastosuj PCA, aby zredukować wymiary do 2, i przedstaw je na wykresie w przestrzeni 2D. Czy widzisz jakieś wzorce?

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.