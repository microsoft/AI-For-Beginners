<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-24T10:26:14+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "pl"
}
-->
# Segmentacja

Wcześniej poznaliśmy Wykrywanie Obiektów, które pozwala nam lokalizować obiekty na obrazie poprzez przewidywanie ich *ramki ograniczającej* (bounding box). Jednak w niektórych zadaniach potrzebujemy nie tylko ramek ograniczających, ale także bardziej precyzyjnej lokalizacji obiektów. To zadanie nazywa się **segmentacją**.

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ai/quiz/23)

Segmentację można postrzegać jako **klasyfikację pikseli**, gdzie dla **każdego** piksela obrazu musimy przewidzieć jego klasę (*tło* jest jedną z klas). Istnieją dwa główne algorytmy segmentacji:

* **Segmentacja semantyczna** określa jedynie klasę piksela i nie rozróżnia różnych obiektów tej samej klasy.
* **Segmentacja instancji** dzieli klasy na różne instancje.

W przypadku segmentacji instancji te owce są różnymi obiektami, ale w segmentacji semantycznej wszystkie owce są reprezentowane jako jedna klasa.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Obraz z [tego wpisu na blogu](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Istnieją różne architektury sieci neuronowych do segmentacji, ale wszystkie mają podobną strukturę. W pewnym sensie przypomina to autoenkoder, o którym wcześniej się uczyliśmy, ale zamiast dekonstruować oryginalny obraz, naszym celem jest dekonstruowanie **maski**. W związku z tym sieć segmentacyjna składa się z następujących części:

* **Enkoder** wyodrębnia cechy z obrazu wejściowego.
* **Dekoder** przekształca te cechy w **obraz maski**, o tym samym rozmiarze i liczbie kanałów odpowiadającej liczbie klas.

<img src="images/segm.png" width="80%">

> Obraz z [tej publikacji](https://arxiv.org/pdf/2001.05566.pdf)

Warto szczególnie wspomnieć o funkcji straty używanej w segmentacji. W przypadku klasycznych autoenkoderów musimy mierzyć podobieństwo między dwoma obrazami i możemy do tego użyć średniego błędu kwadratowego (MSE). W segmentacji każdy piksel w docelowym obrazie maski reprezentuje numer klasy (zakodowany w formacie one-hot wzdłuż trzeciego wymiaru), więc musimy używać funkcji straty specyficznych dla klasyfikacji - straty krzyżowej entropii, uśrednionej dla wszystkich pikseli. Jeśli maska jest binarna, stosuje się **stratę binarnej krzyżowej entropii** (BCE).

> ✅ Kodowanie one-hot to sposób kodowania etykiety klasy w wektor o długości równej liczbie klas. Zobacz [ten artykuł](https://datagy.io/sklearn-one-hot-encode/), aby dowiedzieć się więcej o tej technice.

## Segmentacja w obrazowaniu medycznym

W tej lekcji zobaczymy segmentację w praktyce, trenując sieć do rozpoznawania znamion (znanych również jako pieprzyki) na obrazach medycznych. Będziemy korzystać z <a href="https://www.fc.up.pt/addi/ph2%20database.html">bazy danych PH<sup>2</sup></a> obrazów dermoskopowych jako źródła obrazów. Ten zbiór danych zawiera 200 obrazów trzech klas: typowe znamię, atypowe znamię i czerniak. Wszystkie obrazy zawierają również odpowiadającą im **maskę**, która obrysowuje znamię.

> ✅ Ta technika jest szczególnie odpowiednia dla tego typu obrazowania medycznego, ale jakie inne zastosowania w rzeczywistym świecie możesz sobie wyobrazić?

<img alt="navi" src="images/navi.png"/>

> Obraz z bazy danych PH<sup>2</sup>

Wytrenujemy model do segmentacji dowolnego znamienia z jego tła.

## ✍️ Ćwiczenia: Segmentacja semantyczna

Otwórz poniższe notatniki, aby dowiedzieć się więcej o różnych architekturach segmentacji semantycznej, poćwiczyć pracę z nimi i zobaczyć je w działaniu.

* [Segmentacja semantyczna w Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Segmentacja semantyczna w TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ai/quiz/24)

## Podsumowanie

Segmentacja to bardzo potężna technika klasyfikacji obrazów, która wykracza poza ramki ograniczające, umożliwiając klasyfikację na poziomie pikseli. Jest to technika stosowana w obrazowaniu medycznym i wielu innych zastosowaniach.

## 🚀 Wyzwanie

Segmentacja ciała to tylko jedno z powszechnych zadań, jakie możemy wykonywać z obrazami ludzi. Inne ważne zadania obejmują **wykrywanie szkieletu** i **wykrywanie pozycji**. Wypróbuj bibliotekę [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose), aby zobaczyć, jak można wykorzystać wykrywanie pozycji.

## Przegląd i samodzielna nauka

Ten [artykuł na Wikipedii](https://wikipedia.org/wiki/Image_segmentation) oferuje dobry przegląd różnych zastosowań tej techniki. Dowiedz się więcej na własną rękę o poddziedzinach segmentacji instancji i segmentacji panoptycznej w tej dziedzinie badań.

## [Zadanie](lab/README.md)

W tym laboratorium spróbuj **segmentacji ciała ludzkiego** przy użyciu [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) z Kaggle.

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.