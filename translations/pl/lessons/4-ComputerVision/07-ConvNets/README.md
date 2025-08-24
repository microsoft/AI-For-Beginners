<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "088837b42b7d99198bf62db8a42411e0",
  "translation_date": "2025-08-24T10:29:45+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/README.md",
  "language_code": "pl"
}
-->
# Konwolucyjne Sieci Neuronowe

Wcześniej zauważyliśmy, że sieci neuronowe całkiem dobrze radzą sobie z obrazami, a nawet perceptron z jedną warstwą potrafi rozpoznawać odręczne cyfry z zestawu danych MNIST z zadowalającą dokładnością. Jednak zestaw danych MNIST jest wyjątkowy, ponieważ wszystkie cyfry są wyśrodkowane na obrazie, co upraszcza zadanie.

## [Quiz przed wykładem](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/107)

W rzeczywistości chcemy być w stanie rozpoznawać obiekty na zdjęciu niezależnie od ich dokładnej lokalizacji na obrazie. Wizja komputerowa różni się od ogólnej klasyfikacji, ponieważ gdy próbujemy znaleźć określony obiekt na zdjęciu, skanujemy obraz w poszukiwaniu specyficznych **wzorów** i ich kombinacji. Na przykład, szukając kota, najpierw możemy poszukiwać poziomych linii, które mogą tworzyć wąsy, a następnie określona kombinacja wąsów może wskazać, że to faktycznie zdjęcie kota. Ważna jest względna pozycja i obecność określonych wzorów, a nie ich dokładne położenie na obrazie.

Aby wyodrębnić wzory, użyjemy pojęcia **filtrów konwolucyjnych**. Jak wiadomo, obraz jest reprezentowany przez macierz 2D lub tensor 3D z głębią kolorów. Zastosowanie filtra oznacza, że bierzemy stosunkowo małą macierz **jądra filtra** i dla każdego piksela w oryginalnym obrazie obliczamy średnią ważoną z sąsiednich punktów. Możemy to sobie wyobrazić jako małe okno przesuwające się po całym obrazie i uśredniające wszystkie piksele zgodnie z wagami w macierzy jądra filtra.

![Filtr krawędzi pionowych](../../../../../lessons/4-ComputerVision/07-ConvNets/images/filter-vert.png) | ![Filtr krawędzi poziomych](../../../../../lessons/4-ComputerVision/07-ConvNets/images/filter-horiz.png)
----|----

> Obraz autorstwa Dmitry Soshnikov

Na przykład, jeśli zastosujemy filtry krawędzi pionowych i poziomych o rozmiarze 3x3 do cyfr z MNIST, możemy uzyskać wyróżnienia (np. wysokie wartości) tam, gdzie w oryginalnym obrazie występują krawędzie pionowe i poziome. Tak więc te dwa filtry mogą być używane do "wyszukiwania" krawędzi. Podobnie możemy projektować różne filtry, aby wyszukiwać inne wzory na niskim poziomie:

> Obraz [Leung-Malik Filter Bank](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

Jednak, podczas gdy możemy projektować filtry ręcznie, aby wyodrębniać pewne wzory, możemy również zaprojektować sieć w taki sposób, aby sama uczyła się wzorów automatycznie. To jedna z głównych idei stojących za CNN.

## Główne idee stojące za CNN

Działanie CNN opiera się na następujących ważnych założeniach:

* Filtry konwolucyjne mogą wyodrębniać wzory
* Możemy zaprojektować sieć w taki sposób, aby filtry były trenowane automatycznie
* Możemy użyć tego samego podejścia do znajdowania wzorów w cechach na wysokim poziomie, a nie tylko w oryginalnym obrazie. W ten sposób ekstrakcja cech w CNN działa na hierarchii cech, zaczynając od kombinacji pikseli na niskim poziomie, aż po kombinacje części obrazu na wyższym poziomie.

![Hierarchiczna Ekstrakcja Cech](../../../../../lessons/4-ComputerVision/07-ConvNets/images/FeatureExtractionCNN.png)

> Obraz z [artykułu Hislop-Lynch](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), opartego na [ich badaniach](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Ćwiczenia: Konwolucyjne Sieci Neuronowe

Kontynuujmy eksplorację działania konwolucyjnych sieci neuronowych i dowiedzmy się, jak możemy osiągnąć trenowalne filtry, pracując z odpowiednimi notatnikami:

* [Konwolucyjne Sieci Neuronowe - PyTorch](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb)
* [Konwolucyjne Sieci Neuronowe - TensorFlow](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)

## Architektura Piramidy

Większość CNN używanych do przetwarzania obrazów stosuje tak zwaną architekturę piramidy. Pierwsza warstwa konwolucyjna zastosowana do oryginalnych obrazów zazwyczaj ma stosunkowo niewielką liczbę filtrów (8-16), które odpowiadają różnym kombinacjom pikseli, takim jak poziome/pionowe linie lub kreski. Na następnym poziomie zmniejszamy wymiar przestrzenny sieci i zwiększamy liczbę filtrów, co odpowiada większej liczbie możliwych kombinacji prostych cech. Z każdą warstwą, w miarę zbliżania się do końcowego klasyfikatora, wymiary przestrzenne obrazu maleją, a liczba filtrów rośnie.

Na przykład, spójrzmy na architekturę VGG-16, sieci, która osiągnęła 92,7% dokładności w klasyfikacji top-5 ImageNet w 2014 roku:

![Warstwy ImageNet](../../../../../lessons/4-ComputerVision/07-ConvNets/images/vgg-16-arch1.jpg)

![Piramida ImageNet](../../../../../lessons/4-ComputerVision/07-ConvNets/images/vgg-16-arch.jpg)

> Obraz z [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## Najbardziej Znane Architektury CNN

[Kontynuuj naukę o najbardziej znanych architekturach CNN](CNN_Architectures.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby zapewnić poprawność tłumaczenia, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.