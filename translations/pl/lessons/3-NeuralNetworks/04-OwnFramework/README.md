# Wprowadzenie do sieci neuronowych. Wielowarstwowy perceptron

W poprzedniej sekcji poznaliśmy najprostszy model sieci neuronowej - jednowarstwowy perceptron, liniowy model klasyfikacji dla dwóch klas.

W tej sekcji rozszerzymy ten model, tworząc bardziej elastyczne ramy, które pozwolą nam:

* przeprowadzać **klasyfikację wieloklasową** oprócz klasyfikacji dwuklasowej,
* rozwiązywać **problemy regresji** oprócz klasyfikacji,
* rozdzielać klasy, które nie są liniowo separowalne.

Dodatkowo stworzymy własne modułowe ramy w Pythonie, które umożliwią konstruowanie różnych architektur sieci neuronowych.

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Formalizacja uczenia maszynowego

Zacznijmy od formalizacji problemu uczenia maszynowego. Załóżmy, że mamy zbiór danych treningowych **X** z etykietami **Y**, i musimy zbudować model *f*, który będzie generował jak najdokładniejsze przewidywania. Jakość przewidywań mierzymy za pomocą **funkcji straty** &lagran;. Często stosowane funkcje straty to:

* W przypadku problemu regresji, gdy musimy przewidzieć wartość liczbową, możemy użyć **błędu absolutnego** &sum;<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| lub **błędu kwadratowego** &sum;<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>.
* W przypadku klasyfikacji stosujemy **0-1 loss** (który zasadniczo odpowiada **dokładności** modelu) lub **logistyczną funkcję straty**.

Dla jednowarstwowego perceptronu funkcja *f* była zdefiniowana jako funkcja liniowa *f(x)=wx+b* (gdzie *w* to macierz wag, *x* to wektor cech wejściowych, a *b* to wektor przesunięcia). W przypadku różnych architektur sieci neuronowych funkcja ta może przyjmować bardziej złożoną formę.

> W przypadku klasyfikacji często pożądane jest uzyskanie prawdopodobieństw odpowiadających klasom jako wynik sieci. Aby przekształcić dowolne liczby w prawdopodobieństwa (np. znormalizować wynik), często używamy funkcji **softmax** &sigma;, a funkcja *f* staje się *f(x)=&sigma;(wx+b)*.

W powyższej definicji *f*, *w* i *b* nazywane są **parametrami** &theta;=⟨*w,b*⟩. Mając zbiór danych ⟨**X**,**Y**⟩, możemy obliczyć całkowity błąd dla całego zbioru danych jako funkcję parametrów &theta;.

> ✅ **Celem treningu sieci neuronowej jest minimalizacja błędu poprzez zmienianie parametrów &theta;**

## Optymalizacja metodą gradientu prostego

Istnieje dobrze znana metoda optymalizacji funkcji zwana **gradientem prostym**. Polega ona na obliczeniu pochodnej (w przypadku wielowymiarowym zwanej **gradientem**) funkcji straty względem parametrów i zmienianiu parametrów w taki sposób, aby błąd się zmniejszał. Można to sformalizować w następujący sposób:

* Zainicjalizuj parametry losowymi wartościami w<sup>(0)</sup>, b<sup>(0)</sup>.
* Powtarzaj następujący krok wiele razy:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-&eta;&part;&lagran;/&part;w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-&eta;&part;&lagran;/&part;b

Podczas treningu kroki optymalizacji powinny być obliczane z uwzględnieniem całego zbioru danych (pamiętajmy, że strata jest obliczana jako suma dla wszystkich próbek treningowych). Jednak w praktyce bierzemy małe porcje zbioru danych, zwane **minibatchami**, i obliczamy gradienty na podstawie podzbioru danych. Ponieważ podzbiór jest wybierany losowo za każdym razem, taka metoda nazywana jest **stochastycznym gradientem prostym** (SGD).

## Wielowarstwowe perceptrony i propagacja wsteczna

Jednowarstwowa sieć, jak widzieliśmy powyżej, jest zdolna do klasyfikacji klas liniowo separowalnych. Aby zbudować bardziej zaawansowany model, możemy połączyć kilka warstw sieci. Matematycznie oznaczałoby to, że funkcja *f* przyjmie bardziej złożoną formę i będzie obliczana w kilku krokach:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>&alpha;(z<sub>1</sub>)+b<sub>2</sub>
* f = &sigma;(z<sub>2</sub>)

Tutaj &alpha; to **nieliniowa funkcja aktywacji**, &sigma; to funkcja softmax, a parametry &theta;=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algorytm gradientu prostego pozostanie taki sam, ale obliczanie gradientów będzie bardziej skomplikowane. Zgodnie z regułą różniczkowania łańcuchowego możemy obliczyć pochodne jako:

* &part;&lagran;/&part;w<sub>2</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;w<sub>2</sub>)
* &part;&lagran;/&part;w<sub>1</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;&alpha;)(&part;&alpha;/&part;z<sub>1</sub>)(&part;z<sub>1</sub>/&part;w<sub>1</sub>)

> ✅ Reguła różniczkowania łańcuchowego jest używana do obliczania pochodnych funkcji straty względem parametrów.

Zauważ, że lewa część wszystkich tych wyrażeń jest taka sama, dzięki czemu możemy efektywnie obliczać pochodne, zaczynając od funkcji straty i przechodząc "wstecz" przez graf obliczeniowy. Dlatego metoda treningu wielowarstwowego perceptronu nazywana jest **propagacją wsteczną**, lub 'backprop'.

<img alt="graf obliczeniowy" src="../../../../../translated_images/pl/ComputeGraphGrad.4626252c0de03507.webp"/>

> Image by [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Omówimy propagację wsteczną znacznie bardziej szczegółowo w naszym przykładzie w notebooku.  

## Podsumowanie

W tej lekcji stworzyliśmy własną bibliotekę sieci neuronowych i użyliśmy jej do prostego zadania klasyfikacji dwuwymiarowej.

## 🚀 Wyzwanie

W dołączonym notebooku zaimplementujesz własne ramy do budowy i treningu wielowarstwowych perceptronów. Będziesz mógł szczegółowo zobaczyć, jak działają nowoczesne sieci neuronowe.

Przejdź do notebooka [OwnFramework](OwnFramework.ipynb) i wykonaj zadania.

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Przegląd i samodzielna nauka

Propagacja wsteczna to powszechny algorytm stosowany w AI i ML, warto go [zgłębić](https://wikipedia.org/wiki/Backpropagation).

## [Zadanie](lab/README.md)

W tym laboratorium masz za zadanie użyć ram, które stworzyłeś w tej lekcji, do rozwiązania problemu klasyfikacji ręcznie pisanych cyfr MNIST.

* [Instrukcje](lab/README.md)
* [Notebook](lab/MyFW_MNIST.ipynb)

---

