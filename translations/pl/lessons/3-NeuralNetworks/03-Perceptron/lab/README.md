<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7336583e4630220c835335da640016db",
  "translation_date": "2025-08-24T10:43:02+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/lab/README.md",
  "language_code": "pl"
}
-->
# Klasyfikacja wieloklasowa za pomocą perceptronu

Zadanie laboratoryjne z [Kursu AI dla Początkujących](https://github.com/microsoft/ai-for-beginners).

## Zadanie

Korzystając z kodu opracowanego w tej lekcji do binarnej klasyfikacji ręcznie pisanych cyfr MNIST, stwórz klasyfikator wieloklasowy, który będzie w stanie rozpoznać dowolną cyfrę. Oblicz dokładność klasyfikacji na zbiorze treningowym i testowym oraz wyświetl macierz pomyłek.

## Wskazówki

1. Dla każdej cyfry stwórz zbiór danych do binarnej klasyfikacji "ta cyfra vs. wszystkie inne cyfry".
1. Wytrenuj 10 różnych perceptronów do binarnej klasyfikacji (po jednym dla każdej cyfry).
1. Zdefiniuj funkcję, która będzie klasyfikować wprowadzone cyfry.

> **Wskazówka**: Jeśli połączymy wagi wszystkich 10 perceptronów w jedną macierz, będziemy mogli zastosować wszystkie 10 perceptronów do wprowadzonych cyfr za pomocą jednego mnożenia macierzy. Najbardziej prawdopodobną cyfrę można wtedy znaleźć, stosując operację `argmax` na wynikach.

## Notebook startowy

Rozpocznij zadanie, otwierając [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.