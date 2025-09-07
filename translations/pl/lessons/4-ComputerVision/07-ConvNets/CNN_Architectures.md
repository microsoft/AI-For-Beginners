<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f7b97b375358cb51a1e098df306bf73",
  "translation_date": "2025-08-24T10:30:25+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md",
  "language_code": "pl"
}
-->
# Znane Architektury CNN

### VGG-16

VGG-16 to sieć, która osiągnęła 92,7% dokładności w klasyfikacji top-5 ImageNet w 2014 roku. Ma następującą strukturę warstw:

![ImageNet Layers](../../../../../lessons/4-ComputerVision/07-ConvNets/images/vgg-16-arch1.jpg)

Jak widać, VGG stosuje tradycyjną architekturę piramidy, która jest sekwencją warstw konwolucyjno-poolingowych.

![ImageNet Pyramid](../../../../../lessons/4-ComputerVision/07-ConvNets/images/vgg-16-arch.jpg)

> Obraz z [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet to rodzina modeli zaproponowanych przez Microsoft Research w 2015 roku. Główną ideą ResNet jest wykorzystanie **bloków resztkowych**:

<img src="images/resnet-block.png" width="300"/>

> Obraz z [tego artykułu](https://arxiv.org/pdf/1512.03385.pdf)

Powód zastosowania ścieżki tożsamości polega na tym, aby warstwa przewidywała **różnicę** między wynikiem poprzedniej warstwy a wyjściem bloku resztkowego - stąd nazwa *resztkowy*. Te bloki są znacznie łatwiejsze do trenowania, a sieci można budować z setkami takich bloków (najczęściej spotykane warianty to ResNet-52, ResNet-101 i ResNet-152).

Można również myśleć o tej sieci jako o zdolnej do dostosowywania swojej złożoności do zbioru danych. Na początku, gdy zaczynasz trenować sieć, wartości wag są małe, a większość sygnału przechodzi przez warstwy tożsamości. W miarę postępu treningu i wzrostu wag, znaczenie parametrów sieci rośnie, a sieć dostosowuje się, aby zapewnić wymaganą moc wyrażania, potrzebną do poprawnej klasyfikacji obrazów treningowych.

### Google Inception

Architektura Google Inception idzie o krok dalej i buduje każdą warstwę sieci jako kombinację kilku różnych ścieżek:

<img src="images/inception.png" width="400"/>

> Obraz z [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Tutaj należy podkreślić rolę konwolucji 1x1, ponieważ na pierwszy rzut oka mogą wydawać się bez sensu. Dlaczego mielibyśmy przetwarzać obraz za pomocą filtra 1x1? Jednak należy pamiętać, że filtry konwolucyjne działają również na kilku kanałach głębokości (początkowo - kolory RGB, w kolejnych warstwach - kanały dla różnych filtrów), a konwolucja 1x1 jest używana do mieszania tych kanałów wejściowych za pomocą różnych trenowalnych wag. Można to również postrzegać jako próbkowanie w dół (pooling) w wymiarze kanałów.

Oto [dobry wpis na blogu](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) na ten temat oraz [oryginalny artykuł](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

MobileNet to rodzina modeli o zmniejszonym rozmiarze, odpowiednia dla urządzeń mobilnych. Używaj ich, jeśli masz ograniczone zasoby i możesz poświęcić trochę dokładności. Główną ideą stojącą za nimi jest tzw. **konwolucja separowalna głębokościowo**, która pozwala reprezentować filtry konwolucyjne jako kompozycję konwolucji przestrzennych i konwolucji 1x1 w kanałach głębokości. Znacząco zmniejsza to liczbę parametrów, co sprawia, że sieć jest mniejsza i łatwiejsza do trenowania przy mniejszej ilości danych.

Oto [dobry wpis na blogu o MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Podsumowanie

W tej jednostce nauczyłeś się głównej koncepcji stojącej za sieciami neuronowymi do wizji komputerowej - sieci konwolucyjnych. Architektury stosowane w rzeczywistości, które napędzają klasyfikację obrazów, detekcję obiektów, a nawet generowanie obrazów, są oparte na CNN, tylko z większą liczbą warstw i dodatkowymi sztuczkami treningowymi.

## 🚀 Wyzwanie

W dołączonych notatnikach znajdują się uwagi na końcu dotyczące uzyskania większej dokładności. Przeprowadź eksperymenty, aby sprawdzić, czy możesz osiągnąć wyższą dokładność.

## [Quiz po wykładzie](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/207)

## Przegląd i Samodzielna Nauka

Chociaż CNN są najczęściej używane do zadań związanych z wizją komputerową, są one ogólnie dobre w wykrywaniu wzorców o stałym rozmiarze. Na przykład, jeśli mamy do czynienia z dźwiękami, możemy również chcieć użyć CNN do wyszukiwania określonych wzorców w sygnale audio - w takim przypadku filtry byłyby jednowymiarowe (a taka CNN nazywałaby się 1D-CNN). Czasami używa się również 3D-CNN do wyodrębniania cech w przestrzeni wielowymiarowej, takich jak określone zdarzenia występujące na wideo - CNN może uchwycić pewne wzorce zmiany cech w czasie. Przeprowadź przegląd i samodzielną naukę na temat innych zadań, które można wykonać za pomocą CNN.

## [Zadanie](lab/README.md)

W tym laboratorium Twoim zadaniem jest klasyfikacja różnych ras kotów i psów. Te obrazy są bardziej złożone niż zbiór danych MNIST, mają wyższe wymiary i więcej niż 10 klas.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.