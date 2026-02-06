# Triki w trenowaniu głębokich sieci neuronowych

Wraz z pogłębianiem się sieci neuronowych, proces ich trenowania staje się coraz bardziej wymagający. Jednym z głównych problemów są tzw. [zanikające gradienty](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) lub [eksplodujące gradienty](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Ten artykuł](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) dobrze wprowadza w te zagadnienia.

Aby uczynić trenowanie głębokich sieci bardziej efektywnym, można zastosować kilka technik.

## Utrzymywanie wartości w rozsądnym zakresie

Aby zapewnić stabilność obliczeń numerycznych, należy upewnić się, że wszystkie wartości w sieci neuronowej mieszczą się w rozsądnym zakresie, zazwyczaj [-1..1] lub [0..1]. Nie jest to bardzo rygorystyczny wymóg, ale natura obliczeń zmiennoprzecinkowych sprawia, że wartości o różnych rzędach wielkości nie mogą być dokładnie przetwarzane razem. Na przykład, jeśli dodamy 10<sup>-10</sup> i 10<sup>10</sup>, prawdopodobnie otrzymamy 10<sup>10</sup>, ponieważ mniejsza wartość zostanie "przekształcona" do tego samego rzędu co większa, co spowoduje utratę mantysy.

Większość funkcji aktywacji ma nieliniowości w zakresie [-1..1], dlatego sensowne jest skalowanie wszystkich danych wejściowych do zakresu [-1..1] lub [0..1].

## Inicjalizacja wag

Idealnie, chcemy, aby wartości pozostawały w tym samym zakresie po przejściu przez warstwy sieci. Dlatego ważne jest, aby inicjalizować wagi w taki sposób, aby zachować rozkład wartości.

Rozkład normalny **N(0,1)** nie jest dobrym pomysłem, ponieważ jeśli mamy *n* wejść, odchylenie standardowe wyjścia wynosiłoby *n*, a wartości prawdopodobnie wyjdą poza zakres [0..1].

Często stosowane inicjalizacje to:

 * Rozkład jednostajny -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** gwarantuje, że dla wejść o średniej zero i odchyleniu standardowym równym 1, te same parametry zostaną zachowane
 * **N(0,√2/(n_in+n_out))** -- tzw. **inicjalizacja Xaviera** (`glorot`), która pomaga utrzymać sygnały w zakresie zarówno podczas propagacji w przód, jak i wstecz

## Normalizacja wsadowa

Nawet przy odpowiedniej inicjalizacji wag, wagi mogą podczas trenowania przyjmować dowolnie duże lub małe wartości, co powoduje, że sygnały wychodzą poza właściwy zakres. Możemy przywrócić sygnały do odpowiedniego zakresu, stosując jedną z technik **normalizacji**. Chociaż istnieje kilka takich technik (normalizacja wag, normalizacja warstwowa), najczęściej stosowana jest normalizacja wsadowa.

Idea **normalizacji wsadowej** polega na uwzględnieniu wszystkich wartości w minibatchu i przeprowadzeniu normalizacji (tj. odjęciu średniej i podzieleniu przez odchylenie standardowe) na podstawie tych wartości. Jest to implementowane jako warstwa sieci, która wykonuje tę normalizację po zastosowaniu wag, ale przed funkcją aktywacji. W rezultacie możemy uzyskać wyższą końcową dokładność i szybsze trenowanie.

Oto [oryginalny artykuł](https://arxiv.org/pdf/1502.03167.pdf) na temat normalizacji wsadowej, [wyjaśnienie na Wikipedii](https://en.wikipedia.org/wiki/Batch_normalization) oraz [dobry wprowadzający artykuł](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (i [wersja po rosyjsku](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** to ciekawa technika, która usuwa pewien procent losowych neuronów podczas trenowania. Jest to również implementowane jako warstwa z jednym parametrem (procent neuronów do usunięcia, zazwyczaj 10%-50%), a podczas trenowania zeruje losowe elementy wektora wejściowego przed przekazaniem go do kolejnej warstwy.

Choć może to brzmieć dziwnie, efekt dropout można zobaczyć podczas trenowania klasyfikatora cyfr MNIST w notatniku [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb). Przyspiesza on trenowanie i pozwala osiągnąć wyższą dokładność w mniejszej liczbie epok.

Efekt ten można wyjaśnić na kilka sposobów:

 * Można to uznać za losowy czynnik szokujący dla modelu, który wyprowadza optymalizację z lokalnego minimum
 * Można to traktować jako *implicit model averaging*, ponieważ można powiedzieć, że podczas dropout trenujemy nieco inny model

> *Niektórzy twierdzą, że gdy osoba pod wpływem alkoholu próbuje się czegoś nauczyć, zapamięta to lepiej następnego ranka w porównaniu z osobą trzeźwą, ponieważ mózg z pewnymi "niedziałającymi" neuronami lepiej dostosowuje się do uchwycenia sensu. Nigdy nie testowaliśmy tego sami, czy to prawda.*

## Zapobieganie przeuczeniu

Jednym z bardzo ważnych aspektów głębokiego uczenia jest umiejętność zapobiegania [przeuczeniu](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Chociaż może być kuszące użycie bardzo potężnego modelu sieci neuronowej, zawsze należy zrównoważyć liczbę parametrów modelu z liczbą próbek treningowych.

> Upewnij się, że rozumiesz koncepcję [przeuczenia](../../3-NeuralNetworks/05-Frameworks/Overfitting.md), którą wcześniej omówiliśmy!

Istnieje kilka sposobów zapobiegania przeuczeniu:

 * Wczesne zatrzymanie -- ciągłe monitorowanie błędu na zbiorze walidacyjnym i zatrzymanie trenowania, gdy błąd walidacyjny zaczyna rosnąć.
 * Jawne zanikanie wag / Regularizacja -- dodanie dodatkowej kary do funkcji straty za wysokie wartości bezwzględne wag, co zapobiega uzyskiwaniu przez model bardzo niestabilnych wyników
 * Uśrednianie modeli -- trenowanie kilku modeli i następnie uśrednianie wyników. Pomaga to zminimalizować wariancję.
 * Dropout (Implicit Model Averaging)

## Optymalizatory / Algorytmy trenowania

Kolejnym ważnym aspektem trenowania jest wybór odpowiedniego algorytmu trenowania. Chociaż klasyczny **gradient descent** jest rozsądnym wyborem, czasami może być zbyt wolny lub prowadzić do innych problemów.

W głębokim uczeniu stosujemy **Stochastic Gradient Descent** (SGD), czyli gradient descent stosowany do minibatchy, losowo wybranych ze zbioru treningowego. Wagi są dostosowywane za pomocą tego wzoru:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

W **momentum SGD** przechowujemy część gradientu z poprzednich kroków. Jest to podobne do sytuacji, gdy poruszamy się z bezwładnością, a następnie otrzymujemy impuls w innym kierunku – nasza trajektoria nie zmienia się natychmiast, ale zachowuje część pierwotnego ruchu. Wprowadzamy tutaj dodatkowy wektor v, który reprezentuje *prędkość*:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Parametr γ wskazuje, w jakim stopniu uwzględniamy bezwładność: γ=0 odpowiada klasycznemu SGD; γ=1 to czysta równanie ruchu.

### Adam, Adagrad, itd.

Ponieważ w każdej warstwie mnożymy sygnały przez pewną macierz W<sub>i</sub>, w zależności od ||W<sub>i</sub>|| gradient może albo zanikać i być bliski 0, albo rosnąć w nieskończoność. To istota problemu eksplodujących/zanikających gradientów.

Jednym z rozwiązań tego problemu jest użycie jedynie kierunku gradientu w równaniu, ignorując jego wartość bezwzględną, tj.

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), gdzie ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Ten algorytm nazywa się **Adagrad**. Inne algorytmy wykorzystujące podobną ideę: **RMSProp**, **Adam**

> **Adam** jest uważany za bardzo efektywny algorytm w wielu zastosowaniach, więc jeśli nie jesteś pewien, którego użyć - wybierz Adam.

### Gradient clipping

Gradient clipping to rozszerzenie powyższej idei. Gdy ||∇ℒ|| ≤ θ, uwzględniamy oryginalny gradient w optymalizacji wag, a gdy ||∇ℒ|| > θ - dzielimy gradient przez jego normę. Tutaj θ to parametr, w większości przypadków możemy przyjąć θ=1 lub θ=10.

### Zmniejszanie współczynnika uczenia

Sukces trenowania często zależy od parametru współczynnika uczenia η. Logiczne jest założenie, że większe wartości η prowadzą do szybszego trenowania, co jest pożądane na początku procesu, a następnie mniejsze wartości η pozwalają na dopracowanie sieci. Dlatego w większości przypadków chcemy zmniejszać η w trakcie trenowania.

Można to zrobić, mnożąc η przez pewną liczbę (np. 0,98) po każdej epoce trenowania lub stosując bardziej skomplikowany **harmonogram współczynnika uczenia**.

## Różne architektury sieci

Wybór odpowiedniej architektury sieci dla danego problemu może być trudny. Zazwyczaj wybieramy architekturę, która sprawdziła się w naszym konkretnym zadaniu (lub podobnym). Oto [dobry przegląd](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) architektur sieci neuronowych dla wizji komputerowej.

> Ważne jest, aby wybrać architekturę, która będzie wystarczająco potężna dla liczby dostępnych próbek treningowych. Wybór zbyt potężnego modelu może prowadzić do [przeuczenia](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Innym dobrym podejściem jest użycie architektury, która automatycznie dostosowuje się do wymaganej złożoności. Do pewnego stopnia architektury takie jak **ResNet** i **Inception** są samodostosowujące. [Więcej o architekturach wizji komputerowej](../07-ConvNets/CNN_Architectures.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.