# Triki treningowe w głębokim uczeniu

W miarę pogłębiania się sieci neuronowych, proces ich treningu staje się coraz bardziej wymagający. Jednym z głównych problemów są tak zwane [znikające gradienty](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) lub [eksplodujące gradienty](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Ten wpis](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) daje dobre wprowadzenie do tych problemów.

Aby uczynić trening głębokich sieci bardziej efektywnym, istnieje kilka technik, które można zastosować.

## Utrzymywanie wartości w rozsądnym przedziale

Aby obliczenia numeryczne były bardziej stabilne, chcemy upewnić się, że wszystkie wartości w naszej sieci neuronowej mieszczą się w rozsądnym zakresie, typowo [-1..1] lub [0..1]. Nie jest to bardzo ścisły wymóg, ale natura obliczeń zmiennoprzecinkowych jest taka, że wartości o różnych wielkościach nie mogą być dokładnie manipulowane razem. Na przykład, jeśli dodamy 10<sup>-10</sup> i 10<sup>10</sup>, to najprawdopodobniej otrzymamy 10<sup>10</sup>, ponieważ mniejsza wartość zostanie „przekształcona” na ten sam rząd co większa i w ten sposób część mantysy zostanie utracona.

Większość funkcji aktywacji ma nieliniowości wokół [-1..1], więc sensowne jest skalowanie wszystkich danych wejściowych do przedziału [-1..1] lub [0..1].

## Inicjalizacja wag

Idealnie chcemy, aby wartości znajdowały się w tym samym zakresie po przejściu przez warstwy sieci. Dlatego ważne jest, aby inicjalizować wagi w taki sposób, aby zachować rozkład wartości.

Rozkład normalny **N(0,1)** nie jest dobrym pomysłem, ponieważ jeśli mamy *n* wejść, odchylenie standardowe na wyjściu wyniesie *&radic;n*, a wartości mogą wyjść poza przedział [0..1].

Często stosuje się następujące inicjalizacje:

 * Rozkład jednostajny -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** gwarantuje, że dla danych wejściowych o zerowej średniej i odchyleniu standardowym 1, średnia i odchylenie pozostaną takie same
 * **N(0,&radic;2/(n_in+n_out))** -- tzw. **inicjalizacja Xaviera** (`glorot`), pomaga utrzymać sygnały w zakresie podczas propagacji w przód i wstecz

## Normalizacja wsadowa

Nawet przy właściwej inicjalizacji wag, ich wartości mogą stać się bardzo duże lub bardzo małe podczas treningu, co powoduje wyjście sygnałów poza odpowiedni zakres. Możemy przywrócić sygnały do właściwego zakresu stosując jedną z technik **normalizacji**. Chociaż istnieje ich kilka (Weight normalization, Layer Normalization), najczęściej stosowana jest normalizacja wsadowa (Batch Normalization).

Idea **normalizacji wsadowej** polega na uwzględnieniu wszystkich wartości w minibatchu oraz wykonaniu normalizacji (tzn. odjęcia średniej i podzielenia przez odchylenie standardowe) na podstawie tych wartości. Jest ona zaimplementowana jako warstwa sieci wykonująca normalizację po zastosowaniu wag, ale przed funkcją aktywacji. W rezultacie zazwyczaj obserwujemy wyższą końcową dokładność i szybszy trening.

Oto [oryginalny artykuł](https://arxiv.org/pdf/1502.03167.pdf) o normalizacji wsadowej, [wyjaśnienie na Wikipedii](https://en.wikipedia.org/wiki/Batch_normalization) oraz [dobry wprowadzający wpis na blogu](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (oraz wersja [po rosyjsku](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** to ciekawa technika polegająca na usunięciu pewnego procentu losowych neuronów podczas treningu. Jest zaimplementowana jako warstwa z jednym parametrem (procent neuronów do usunięcia, zazwyczaj 10%-50%), która podczas treningu zeruje losowe elementy wektora wejściowego, zanim przekaże go dalej.

Choć może to brzmieć dziwnie, efekt dropout można zobaczyć na przykładzie klasyfikatora cyfr MNIST w notatniku [`Dropout.ipynb`](Dropout.ipynb). Przyspiesza on trening i pozwala osiągnąć wyższą dokładność w mniejszej liczbie epok.

Ten efekt da się wyjaśnić na kilka sposobów:

 * Można go uważać za losowy czynnik szokujący model, który wyciąga optymalizację z lokalnego minimum
 * Można go rozpatrywać jako *niejawne uśrednianie modelu*, ponieważ można powiedzieć, że podczas dropout trenujemy nieco inny model

> *Niektórzy mówią, że gdy pijany człowiek stara się czegoś nauczyć, rano zapamiętuje to lepiej niż trzeźwy, ponieważ mózg z częściowo niesprawnymi neuronami stara się lepiej przyswoić znaczenie. Sami nigdy tego nie testowaliśmy.*

## Zapobieganie przeuczeniu

Jednym z bardzo ważnych aspektów głębokiego uczenia jest możliwość zapobiegania [przeuczeniu](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Choć może kusić użycie bardzo potężnego modelu sieci neuronowej, zawsze powinniśmy wyważyć liczbę parametrów modelu z liczbą próbek treningowych.

> Upewnij się, że rozumiesz pojęcie [przeuczenia](../../3-NeuralNetworks/05-Frameworks/Overfitting.md), które przedstawiliśmy wcześniej!

Istnieje kilka sposobów zapobiegania przeuczeniu:

 * Wczesne zatrzymanie -- ciągłe monitorowanie błędu na zbiorze walidacyjnym i zatrzymanie treningu, gdy błąd walidacyjny zaczyna rosnąć.
 * Jawny rozkład wag / regularyzacja -- dodanie dodatkowej kary do funkcji straty za duże wartości wag, co zapobiega bardzo niestabilnym wynikom modelu
 * Uśrednianie modeli -- trenowanie kilku modeli i uśrednianie wyników. Pomaga to zminimalizować wariancję.
 * Dropout (niejawne uśrednianie modeli)

## Optymalizatory / Algorytmy treningowe

Kolejnym ważnym aspektem treningu jest wybór dobrego algorytmu trenowania. Klasyczny **spadek gradientu** jest rozsądnym wyborem, ale czasem może być zbyt wolny lub powodować inne problemy.

W głębokim uczeniu stosujemy **Stochastic Gradient Descent** (SGD), czyli spadek gradientu stosowany do minibatchy losowo wybranych ze zbioru treningowego. Wagi są aktualizowane według wzoru:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

W **momentum SGD** zachowujemy część gradientu z poprzednich kroków. Jest to podobne do ruchu z bezwładnością - jeśli idziemy w którąś stronę i dostajemy uderzenie z innej strony, nasza trajektoria nie zmienia się od razu, lecz zachowuje część pierwotnego ruchu. Wprowadzamy tutaj dodatkowy wektor v, reprezentujący *prędkość*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Parametr &gamma; wskazuje, w jakim stopniu bierzemy pod uwagę bezwładność: &gamma;=0 odpowiada klasycznemu SGD, &gamma;=1 to czyste równanie ruchu.

### Adam, Adagrad itd.

Ponieważ na każdej warstwie mnożymy sygnały przez macierz W<sub>i</sub>, w zależności od ||W<sub>i</sub>|| gradient może maleć i zbliżać się do 0 albo rosnąć w nieskończoność. To jest istota problemu Eksplodujących/Znikających gradientów.

Jednym z rozwiązań tego problemu jest używanie tylko kierunku gradientu w równaniu, zignorowanie wartości bezwzględnej, tzn.

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), gdzie ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Ten algorytm nazywa się **Adagrad**. Inne algorytmy stosujące tę samą ideę to: **RMSProp**, **Adam**

> **Adam** uważany jest za bardzo efektywny algorytm do wielu zastosowań, więc jeśli nie wiesz, którego użyć – skorzystaj z Adama.

### Ograniczanie gradientu

Ograniczanie gradientu jest rozszerzeniem powyższej idei. Gdy ||&nabla;&lagran;|| &le; &theta;, przyjmujemy oryginalny gradient do optymalizacji wag, a gdy ||&nabla;&lagran;|| > &theta;, dzielimy gradient przez jego normę. Parametr &theta; można zazwyczaj ustawić na 1 lub 10.

### Zmniejszanie współczynnika uczenia się

Sukces treningu często zależy od parametru współczynnika uczenia się &eta;. Logicznie można założyć, że większe wartości &eta; prowadzą do szybszego treningu, co jest zazwyczaj pożądane na początku, a następnie mniejsze wartości &eta; pozwalają na dokładniejsze dostrojenie sieci. Dlatego też najczęściej chcemy zmniejszać &eta; w trakcie treningu.

Można to zrobić, mnożąc &eta; przez pewną liczbę (np. 0.98) po każdej epoce treningu lub stosując bardziej skomplikowany **harmonogram zmiany współczynnika uczenia się**.

## Różne architektury sieci

Dobór odpowiedniej architektury sieci do problemu może być trudny. Zwykle wybierzemy architekturę, która sprawdziła się dla naszego konkretnego zadania (lub podobnego). Oto [dobry przegląd](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) architektur sieci neuronowych dla widzenia komputerowego.

> Ważne jest, aby wybrać architekturę, która będzie wystarczająco potężna dla liczby próbek treningowych, które mamy. Wybranie zbyt potężnego modelu może prowadzić do [przeuczenia](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Innym dobrym rozwiązaniem jest użycie architektury, która automatycznie dostosuje się do wymaganej złożoności. Do pewnego stopnia architektury **ResNet** i **Inception** są samodopasowujące się. [Więcej o architekturach do widzenia komputerowego](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->