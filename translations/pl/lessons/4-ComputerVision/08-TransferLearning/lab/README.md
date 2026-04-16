# Klasyfikacja zwierząt domowych z Oxfordu za pomocą transferu uczenia

Zadanie laboratoryjne z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Zadanie

Wyobraź sobie, że musisz stworzyć aplikację dla przedszkola dla zwierząt, która kataloguje wszystkie zwierzęta. Jedną z świetnych funkcji takiej aplikacji byłoby automatyczne rozpoznawanie rasy na podstawie fotografii. W tym zadaniu użyjemy transferu uczenia, aby klasyfikować zdjęcia zwierząt domowych z rzeczywistego życia, korzystając z zestawu danych [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## Zestaw danych

Użyjemy oryginalnego zestawu danych [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), który zawiera 35 różnych ras psów i kotów.

Aby pobrać zestaw danych, użyj tego fragmentu kodu:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Rozpoczęcie pracy z notebookiem

Rozpocznij laboratorium, otwierając [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Wnioski

Transfer uczenia i sieci wstępnie wytrenowane pozwalają nam stosunkowo łatwo rozwiązywać rzeczywiste problemy klasyfikacji obrazów. Jednak sieci wstępnie wytrenowane działają dobrze na obrazach podobnego rodzaju, a jeśli zaczniemy klasyfikować bardzo różne obrazy (np. obrazy medyczne), prawdopodobnie uzyskamy znacznie gorsze wyniki.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.