<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-24T10:30:56+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "pl"
}
-->
# Klasyfikacja Twarzy Zwierząt Domowych

Zadanie laboratoryjne z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Zadanie

Wyobraź sobie, że musisz stworzyć aplikację dla przedszkola dla zwierząt, która kataloguje wszystkie zwierzęta. Jedną z świetnych funkcji takiej aplikacji byłoby automatyczne rozpoznawanie rasy na podstawie fotografii. Można to skutecznie osiągnąć za pomocą sieci neuronowych.

Twoim zadaniem jest wytrenowanie konwolucyjnej sieci neuronowej do klasyfikacji różnych ras kotów i psów, korzystając z zestawu danych **Pet Faces**.

## Zestaw Danych

Użyjemy zestawu danych **Pet Faces**, który pochodzi z [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) pets dataset. Zawiera on 35 różnych ras psów i kotów.

![Zestaw danych, z którym będziemy pracować](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/images/data.png)

Aby pobrać zestaw danych, użyj tego fragmentu kodu:

```python
!wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Rozpoczęcie Pracy z Notebookiem

Rozpocznij pracę z laboratorium, otwierając [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb)

## Wnioski

Rozwiązałeś stosunkowo złożony problem klasyfikacji obrazów od podstaw! Było całkiem sporo klas, a mimo to udało Ci się osiągnąć rozsądną dokładność! Warto również zmierzyć top-k accuracy, ponieważ łatwo pomylić niektóre klasy, które nawet dla ludzi nie są wyraźnie różne.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić poprawność tłumaczenia, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.