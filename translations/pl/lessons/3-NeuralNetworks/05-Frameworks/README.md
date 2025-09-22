<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b544f20b796402507fb05a0df893323",
  "translation_date": "2025-08-24T10:41:31+00:00",
  "source_file": "lessons/3-NeuralNetworks/05-Frameworks/README.md",
  "language_code": "pl"
}
-->
# Frameworky Sieci Neuronowych

Jak już się nauczyliśmy, aby efektywnie trenować sieci neuronowe, musimy zrobić dwie rzeczy:

* Operować na tensorach, np. mnożyć, dodawać i obliczać funkcje takie jak sigmoid czy softmax  
* Obliczać gradienty wszystkich wyrażeń, aby przeprowadzać optymalizację metodą gradientu prostego  

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ai/quiz/9)

Podczas gdy biblioteka `numpy` może realizować pierwszą część, potrzebujemy mechanizmu do obliczania gradientów. W [naszym frameworku](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb), który opracowaliśmy w poprzedniej sekcji, musieliśmy ręcznie programować wszystkie funkcje pochodne w metodzie `backward`, która realizuje propagację wsteczną. Idealnie byłoby, gdyby framework umożliwiał obliczanie gradientów *dowolnego wyrażenia*, które możemy zdefiniować.

Kolejną ważną rzeczą jest możliwość wykonywania obliczeń na GPU lub innych wyspecjalizowanych jednostkach obliczeniowych, takich jak [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). Trenowanie głębokich sieci neuronowych wymaga *ogromnej* liczby obliczeń, a możliwość ich równoległego przetwarzania na GPU jest niezwykle istotna.

> ✅ Termin 'równoległość' oznacza rozdzielenie obliczeń na wiele urządzeń.

Obecnie dwa najpopularniejsze frameworki sieci neuronowych to: [TensorFlow](http://TensorFlow.org) i [PyTorch](https://pytorch.org/). Oba oferują niskopoziomowe API do operowania na tensorach zarówno na CPU, jak i GPU. Na bazie niskopoziomowego API istnieją również wyższopoziomowe API, takie jak [Keras](https://keras.io/) i [PyTorch Lightning](https://pytorchlightning.ai/).

Low-Level API | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)  
--------------|-------------------------------------|--------------------------------  
High-level API| [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)  

**Niskopoziomowe API** w obu frameworkach pozwalają na budowanie tzw. **grafów obliczeniowych**. Graf ten definiuje, jak obliczyć wynik (zazwyczaj funkcję straty) dla danych parametrów wejściowych i może być przesłany do obliczeń na GPU, jeśli jest dostępne. Istnieją funkcje do różniczkowania tego grafu obliczeniowego i obliczania gradientów, które następnie mogą być użyte do optymalizacji parametrów modelu.

**Wysokopoziomowe API** traktują sieci neuronowe jako **sekwencję warstw**, co znacznie ułatwia budowanie większości sieci neuronowych. Trenowanie modelu zazwyczaj wymaga przygotowania danych, a następnie wywołania funkcji `fit`, która wykonuje całą pracę.

Wysokopoziomowe API pozwala na szybkie konstruowanie typowych sieci neuronowych bez martwienia się o wiele szczegółów. Jednocześnie niskopoziomowe API oferuje znacznie większą kontrolę nad procesem trenowania, dlatego jest często używane w badaniach, gdy pracujemy z nowymi architekturami sieci neuronowych.

Warto również zrozumieć, że można używać obu API razem, np. można opracować własną architekturę warstwy sieci za pomocą niskopoziomowego API, a następnie użyć jej w większej sieci skonstruowanej i trenowanej za pomocą wysokopoziomowego API. Można też zdefiniować sieć za pomocą wysokopoziomowego API jako sekwencję warstw, a następnie użyć własnej pętli trenowania opartej na niskopoziomowym API do przeprowadzenia optymalizacji. Oba API opierają się na tych samych podstawowych koncepcjach i są zaprojektowane tak, aby dobrze ze sobą współpracowały.

## Nauka

W tym kursie oferujemy większość treści zarówno dla PyTorch, jak i TensorFlow. Możesz wybrać preferowany framework i przejść tylko przez odpowiednie notatniki. Jeśli nie jesteś pewien, który framework wybrać, przeczytaj dyskusje w internecie na temat **PyTorch vs. TensorFlow**. Możesz również zapoznać się z oboma frameworkami, aby lepiej je zrozumieć.

Tam, gdzie to możliwe, będziemy używać wysokopoziomowych API dla uproszczenia. Jednak uważamy, że ważne jest zrozumienie, jak działają sieci neuronowe od podstaw, dlatego na początku zaczynamy od pracy z niskopoziomowym API i tensorami. Jeśli jednak chcesz szybko zacząć i nie chcesz poświęcać dużo czasu na naukę tych szczegółów, możesz je pominąć i od razu przejść do notatników z wysokopoziomowym API.

## ✍️ Ćwiczenia: Frameworky

Kontynuuj naukę w poniższych notatnikach:

Low-Level API | [TensorFlow+Keras Notebook](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [PyTorch](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)  
--------------|-------------------------------------|--------------------------------  
High-level API| [Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) | *PyTorch Lightning*  

Po opanowaniu frameworków, przypomnijmy sobie pojęcie nadmiernego dopasowania.

# Nadmierne dopasowanie (Overfitting)

Nadmierne dopasowanie to niezwykle ważne pojęcie w uczeniu maszynowym i bardzo ważne jest, aby je dobrze zrozumieć!

Rozważmy następujący problem aproksymacji 5 punktów (reprezentowanych przez `x` na poniższych wykresach):

![linear](../../../../../lessons/3-NeuralNetworks/images/overfit1.jpg) | ![overfit](../../../../../lessons/3-NeuralNetworks/images/overfit2.jpg)  
-------------------------|--------------------------  
**Model liniowy, 2 parametry** | **Model nieliniowy, 7 parametrów**  
Błąd treningowy = 5.3 | Błąd treningowy = 0  
Błąd walidacyjny = 5.1 | Błąd walidacyjny = 20  

* Po lewej widzimy dobrą aproksymację liniową. Ponieważ liczba parametrów jest odpowiednia, model poprawnie odczytuje rozkład punktów.  
* Po prawej model jest zbyt potężny. Ponieważ mamy tylko 5 punktów, a model ma 7 parametrów, może dostosować się tak, aby przechodzić przez wszystkie punkty, co sprawia, że błąd treningowy wynosi 0. Jednak uniemożliwia to modelowi zrozumienie prawidłowego wzorca w danych, co skutkuje bardzo wysokim błędem walidacyjnym.  

Bardzo ważne jest znalezienie odpowiedniej równowagi między złożonością modelu (liczbą parametrów) a liczbą próbek treningowych.

## Dlaczego występuje nadmierne dopasowanie

  * Zbyt mało danych treningowych  
  * Zbyt potężny model  
  * Zbyt dużo szumu w danych wejściowych  

## Jak wykryć nadmierne dopasowanie

Jak widać na powyższym wykresie, nadmierne dopasowanie można wykryć poprzez bardzo niski błąd treningowy i wysoki błąd walidacyjny. Zazwyczaj podczas treningu widzimy, jak zarówno błędy treningowe, jak i walidacyjne zaczynają maleć, a następnie w pewnym momencie błąd walidacyjny może przestać maleć i zacząć rosnąć. To będzie oznaka nadmiernego dopasowania i wskazówka, że powinniśmy prawdopodobnie zatrzymać trening w tym momencie (lub przynajmniej zapisać stan modelu).

![overfitting](../../../../../lessons/3-NeuralNetworks/images/Overfitting.png)

## Jak zapobiegać nadmiernemu dopasowaniu

Jeśli zauważysz, że występuje nadmierne dopasowanie, możesz zrobić jedno z poniższych:

 * Zwiększyć ilość danych treningowych  
 * Zmniejszyć złożoność modelu  
 * Użyć jakiejś [techniki regularyzacji](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), takiej jak [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), którą omówimy później.  

## Nadmierne dopasowanie a kompromis między błędem a wariancją

Nadmierne dopasowanie to w rzeczywistości przypadek bardziej ogólnego problemu w statystyce, zwanego [kompromisem między błędem a wariancją](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Jeśli rozważymy możliwe źródła błędu w naszym modelu, możemy wyróżnić dwa rodzaje błędów:

* **Błędy wynikające z uprzedzeń (bias errors)** są spowodowane tym, że nasz algorytm nie jest w stanie poprawnie uchwycić relacji w danych treningowych. Może to wynikać z faktu, że nasz model nie jest wystarczająco potężny (**niedopasowanie**).  
* **Błędy wynikające z wariancji (variance errors)**, które są spowodowane tym, że model aproksymuje szum w danych wejściowych zamiast znaczących relacji (**nadmierne dopasowanie**).  

Podczas treningu błąd wynikający z uprzedzeń maleje (gdy nasz model uczy się aproksymować dane), a błąd wynikający z wariancji rośnie. Ważne jest, aby zatrzymać trening - albo ręcznie (gdy wykryjemy nadmierne dopasowanie), albo automatycznie (poprzez wprowadzenie regularyzacji) - aby zapobiec nadmiernemu dopasowaniu.

## Podsumowanie

W tej lekcji dowiedziałeś się o różnicach między różnymi API dla dwóch najpopularniejszych frameworków AI, TensorFlow i PyTorch. Ponadto nauczyłeś się o bardzo ważnym temacie, jakim jest nadmierne dopasowanie.

## 🚀 Wyzwanie

W towarzyszących notatnikach znajdziesz 'zadania' na końcu; przejdź przez notatniki i wykonaj zadania.

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ai/quiz/10)

## Przegląd i samodzielna nauka

Zrób badania na następujące tematy:

- TensorFlow  
- PyTorch  
- Nadmierne dopasowanie  

Zadaj sobie następujące pytania:

- Jaka jest różnica między TensorFlow a PyTorch?  
- Jaka jest różnica między nadmiernym dopasowaniem a niedopasowaniem?  

## [Zadanie](lab/README.md)

W tym laboratorium masz za zadanie rozwiązać dwa problemy klasyfikacyjne, używając jedno- i wielowarstwowych sieci w pełni połączonych, korzystając z PyTorch lub TensorFlow.

* [Instrukcje](lab/README.md)  
* [Notatnik](../../../../../lessons/3-NeuralNetworks/05-Frameworks/lab/LabFrameworks.ipynb)  

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.