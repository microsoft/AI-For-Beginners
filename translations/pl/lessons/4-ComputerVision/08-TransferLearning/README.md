<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "717775c4050ccbffbe0c961ad8bf7bf7",
  "translation_date": "2025-08-24T10:33:13+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/README.md",
  "language_code": "pl"
}
-->
# Wstępnie Wytrenowane Sieci i Transfer Learning

Trenowanie CNN-ów może zająć dużo czasu i wymaga dużej ilości danych. Jednak większość czasu poświęca się na naukę najlepszych filtrów niskiego poziomu, które sieć może wykorzystać do wyodrębniania wzorców z obrazów. Naturalnie nasuwa się pytanie – czy możemy użyć sieci neuronowej wytrenowanej na jednym zbiorze danych i dostosować ją do klasyfikacji innych obrazów bez konieczności pełnego procesu trenowania?

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ai/quiz/15)

To podejście nazywa się **transfer learning**, ponieważ przenosimy pewną wiedzę z jednego modelu sieci neuronowej do innego. W transfer learning zazwyczaj zaczynamy od wstępnie wytrenowanego modelu, który został wytrenowany na dużym zbiorze obrazów, takim jak **ImageNet**. Modele te potrafią już dobrze wyodrębniać różne cechy z ogólnych obrazów, a w wielu przypadkach zbudowanie klasyfikatora na podstawie tych wyodrębnionych cech może przynieść dobre rezultaty.

> ✅ Transfer Learning to termin, który można znaleźć w innych dziedzinach akademickich, takich jak edukacja. Odnosi się do procesu przenoszenia wiedzy z jednej dziedziny i stosowania jej w innej.

## Wstępnie Wytrenowane Modele jako Ekstraktory Cech

Sieci konwolucyjne, o których mówiliśmy w poprzedniej sekcji, zawierają wiele warstw, z których każda ma za zadanie wyodrębniać pewne cechy z obrazu, zaczynając od kombinacji pikseli niskiego poziomu (takich jak linie poziome/pionowe czy kreski), aż po bardziej złożone kombinacje cech, odpowiadające np. oku płomienia. Jeśli wytrenujemy CNN na wystarczająco dużym zbiorze ogólnych i zróżnicowanych obrazów, sieć powinna nauczyć się wyodrębniać te wspólne cechy.

Zarówno Keras, jak i PyTorch zawierają funkcje umożliwiające łatwe załadowanie wstępnie wytrenowanych wag sieci neuronowych dla niektórych popularnych architektur, z których większość została wytrenowana na obrazach z ImageNet. Najczęściej używane z nich są opisane na stronie [Architektury CNN](../07-ConvNets/CNN_Architectures.md) z poprzedniej lekcji. W szczególności warto rozważyć użycie jednego z następujących modeli:

* **VGG-16/VGG-19** – stosunkowo proste modele, które nadal dają dobrą dokładność. Często użycie VGG jako pierwszej próby to dobry wybór, aby zobaczyć, jak działa transfer learning.
* **ResNet** – rodzina modeli zaproponowanych przez Microsoft Research w 2015 roku. Mają więcej warstw, a zatem wymagają więcej zasobów.
* **MobileNet** – rodzina modeli o zmniejszonym rozmiarze, odpowiednia dla urządzeń mobilnych. Używaj ich, jeśli masz ograniczone zasoby i możesz poświęcić trochę dokładności.

Oto przykładowe cechy wyodrębnione z obrazu kota przez sieć VGG-16:

![Cechy wyodrębnione przez VGG-16](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/features.png)

## Zbiór Danych Koty vs. Psy

W tym przykładzie użyjemy zbioru danych [Koty i Psy](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), który jest bardzo zbliżony do rzeczywistego scenariusza klasyfikacji obrazów.

## ✍️ Ćwiczenie: Transfer Learning

Zobaczmy transfer learning w praktyce w odpowiednich notebookach:

* [Transfer Learning - PyTorch](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb)
* [Transfer Learning - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb)

## Wizualizacja Adwersarialnego Kota

Wstępnie wytrenowana sieć neuronowa zawiera różne wzorce w swoim *mózgu*, w tym pojęcia **idealnego kota** (jak również idealnego psa, idealnej zebry itd.). Byłoby interesujące jakoś **zwizualizować ten obraz**. Nie jest to jednak proste, ponieważ wzorce są rozproszone po wagach sieci i zorganizowane w hierarchiczną strukturę.

Jednym z podejść, które możemy zastosować, jest rozpoczęcie od losowego obrazu, a następnie próba użycia techniki **optymalizacji metodą gradientu prostego**, aby dostosować ten obraz w taki sposób, aby sieć zaczęła myśleć, że to kot.

![Pętla optymalizacji obrazu](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/ideal-cat-loop.png)

Jednak jeśli to zrobimy, otrzymamy coś bardzo podobnego do losowego szumu. Dzieje się tak, ponieważ *istnieje wiele sposobów, aby sieć uznała obraz wejściowy za kota*, w tym takie, które wizualnie nie mają sensu. Chociaż te obrazy zawierają wiele wzorców typowych dla kota, nic nie zmusza ich do bycia wizualnie rozpoznawalnymi.

Aby poprawić wynik, możemy dodać kolejny składnik do funkcji straty, zwany **stratą wariacji**. Jest to metryka pokazująca, jak podobne są sąsiadujące piksele obrazu. Minimalizowanie straty wariacji sprawia, że obraz staje się gładszy i pozbawiony szumu – ujawniając bardziej wizualnie atrakcyjne wzorce. Oto przykład takich "idealnych" obrazów, które są klasyfikowane jako kot i zebra z wysokim prawdopodobieństwem:

![Idealny Kot](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/ideal-cat.png) | ![Idealna Zebra](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/ideal-zebra.png)
-----|-----
*Idealny Kot* | *Idealna Zebra*

Podobne podejście można zastosować do przeprowadzania tzw. **ataków adwersarialnych** na sieć neuronową. Załóżmy, że chcemy oszukać sieć neuronową i sprawić, by pies wyglądał jak kot. Jeśli weźmiemy obraz psa, który jest rozpoznawany przez sieć jako pies, możemy go nieco zmodyfikować za pomocą optymalizacji metodą gradientu prostego, aż sieć zacznie klasyfikować go jako kota:

![Obraz psa](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/original-dog.png) | ![Obraz psa klasyfikowany jako kot](../../../../../lessons/4-ComputerVision/08-TransferLearning/images/adversarial-dog.png)
-----|-----
*Oryginalny obraz psa* | *Obraz psa klasyfikowany jako kot*

Zobacz kod, aby odtworzyć powyższe wyniki w następującym notebooku:

* [Idealny i Adwersarialny Kot - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb)

## Podsumowanie

Dzięki transfer learning możesz szybko stworzyć klasyfikator do zadania klasyfikacji obiektów niestandardowych i osiągnąć wysoką dokładność. Widać, że bardziej złożone zadania, które teraz rozwiązujemy, wymagają większej mocy obliczeniowej i nie mogą być łatwo rozwiązane na CPU. W następnej jednostce spróbujemy użyć bardziej lekkiej implementacji, aby wytrenować ten sam model przy użyciu mniejszych zasobów obliczeniowych, co skutkuje tylko nieznacznie niższą dokładnością.

## 🚀 Wyzwanie

W towarzyszących notebookach znajdują się notatki na końcu dotyczące tego, jak transfer wiedzy działa najlepiej z nieco podobnymi danymi treningowymi (np. nowy rodzaj zwierzęcia). Przeprowadź eksperymenty z zupełnie nowymi typami obrazów, aby zobaczyć, jak dobrze lub źle działają Twoje modele transfer learning.

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Przegląd i Samodzielna Nauka

Przeczytaj [TrainingTricks.md](TrainingTricks.md), aby pogłębić swoją wiedzę na temat innych sposobów trenowania modeli.

## [Zadanie](lab/README.md)

W tym laboratorium użyjemy rzeczywistego zbioru danych [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) zawierającego 35 ras kotów i psów, i zbudujemy klasyfikator transfer learning.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.