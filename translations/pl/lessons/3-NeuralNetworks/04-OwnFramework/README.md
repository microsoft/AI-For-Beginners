<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-24T10:40:26+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "pl"
}
-->
# Wprowadzenie do Sieci Neuronowych. Perceptron Wielowarstwowy

W poprzedniej sekcji nauczyłeś się o najprostszym modelu sieci neuronowej - perceptronie jednowarstwowym, będącym liniowym modelem klasyfikacji dwuklasowej.

W tej sekcji rozszerzymy ten model do bardziej elastycznego frameworka, który pozwoli nam:

* wykonywać **klasyfikację wieloklasową** oprócz dwuklasowej
* rozwiązywać **problemy regresji** oprócz klasyfikacji
* rozdzielać klasy, które nie są liniowo separowalne

Stworzymy również własny modułowy framework w Pythonie, który umożliwi nam budowanie różnych architektur sieci neuronowych.

## [Quiz przed wykładem](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/104)

## Formalizacja Uczenia Maszynowego

Zacznijmy od formalizacji problemu Uczenia Maszynowego. Załóżmy, że mamy zbiór danych treningowych **X** z etykietami **Y**, i musimy zbudować model *f*, który będzie dokonywał jak najdokładniejszych przewidywań. Jakość przewidywań mierzymy za pomocą **funkcji straty** ℒ. Często używane funkcje straty to:

* W przypadku problemu regresji, gdy musimy przewidzieć liczbę, możemy użyć **błędu bezwzględnego** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| lub **błędu kwadratowego** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* W przypadku klasyfikacji używamy **straty 0-1** (która jest zasadniczo tym samym co **dokładność** modelu) lub **straty logistycznej**.

Dla perceptronu jednowarstwowego funkcja *f* była zdefiniowana jako funkcja liniowa *f(x)=wx+b* (gdzie *w* to macierz wag, *x* to wektor cech wejściowych, a *b* to wektor przesunięcia). Dla różnych architektur sieci neuronowych funkcja ta może przyjmować bardziej złożoną formę.

> W przypadku klasyfikacji często pożądane jest uzyskanie prawdopodobieństw odpowiadających klas jako wyjścia sieci. Aby przekształcić dowolne liczby na prawdopodobieństwa (np. znormalizować wyjście), często używamy funkcji **softmax** σ, a funkcja *f* staje się *f(x)=σ(wx+b)*

W definicji *f* powyżej, *w* i *b* nazywane są **parametrami** θ=⟨*w,b*⟩. Mając zbiór danych ⟨**X**,**Y**⟩, możemy obliczyć całkowity błąd dla całego zbioru danych jako funkcję parametrów θ.

> ✅ **Celem trenowania sieci neuronowej jest minimalizacja błędu poprzez modyfikację parametrów θ**

## Optymalizacja za pomocą Gradientu Prostego

Istnieje dobrze znana metoda optymalizacji funkcji zwana **gradientem prostym**. Idea polega na tym, że możemy obliczyć pochodną (w przypadku wielowymiarowym nazywaną **gradientem**) funkcji straty względem parametrów i zmieniać parametry w taki sposób, aby błąd malał. Można to sformalizować w następujący sposób:

* Inicjalizuj parametry losowymi wartościami w<sup>(0)</sup>, b<sup>(0)</sup>
* Powtarzaj następujący krok wiele razy:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Podczas treningu kroki optymalizacji powinny być obliczane z uwzględnieniem całego zbioru danych (pamiętaj, że strata jest obliczana jako suma dla wszystkich próbek treningowych). Jednak w praktyce bierzemy małe porcje zbioru danych zwane **minipaczkami** i obliczamy gradienty na podstawie podzbioru danych. Ponieważ podzbiór jest wybierany losowo za każdym razem, taka metoda nazywana jest **stochastycznym gradientem prostym** (SGD).

## Perceptrony Wielowarstwowe i Wsteczna Propagacja

Sieć jednowarstwowa, jak widzieliśmy powyżej, jest w stanie klasyfikować klasy liniowo separowalne. Aby zbudować bogatszy model, możemy połączyć kilka warstw sieci. Matematycznie oznaczałoby to, że funkcja *f* przyjmie bardziej złożoną formę i będzie obliczana w kilku krokach:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Tutaj α to **nieliniowa funkcja aktywacji**, σ to funkcja softmax, a parametry θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Algorytm gradientu prostego pozostanie taki sam, ale obliczanie gradientów będzie trudniejsze. Zgodnie z regułą różniczkowania łańcuchowego możemy obliczyć pochodne jako:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Reguła różniczkowania łańcuchowego jest używana do obliczania pochodnych funkcji straty względem parametrów.

Zauważ, że lewa część wszystkich tych wyrażeń jest taka sama, dzięki czemu możemy efektywnie obliczać pochodne, zaczynając od funkcji straty i idąc "wstecz" przez graf obliczeniowy. Dlatego metoda trenowania perceptronu wielowarstwowego nazywana jest **wsteczną propagacją**, lub 'backprop'.

<img alt="compute graph" src="images/ComputeGraphGrad.png"/>

> TODO: cytowanie obrazu

> ✅ Omówimy wsteczną propagację znacznie bardziej szczegółowo w naszym przykładzie w notatniku.  

## Podsumowanie

W tej lekcji stworzyliśmy własną bibliotekę sieci neuronowych i użyliśmy jej do prostego zadania klasyfikacji dwuwymiarowej.

## 🚀 Wyzwanie

W dołączonym notatniku zaimplementujesz własny framework do budowania i trenowania perceptronów wielowarstwowych. Będziesz mógł zobaczyć szczegółowo, jak działają nowoczesne sieci neuronowe.

Przejdź do notatnika [OwnFramework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) i przepracuj go.

## [Quiz po wykładzie](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/204)

## Przegląd i Samodzielna Nauka

Wsteczna propagacja to powszechny algorytm używany w AI i ML, warto go [zgłębić bardziej szczegółowo](https://wikipedia.org/wiki/Backpropagation)

## [Zadanie](lab/README.md)

W tym laboratorium zostaniesz poproszony o użycie frameworka stworzonego w tej lekcji do rozwiązania problemu klasyfikacji ręcznie pisanych cyfr MNIST.

* [Instrukcje](lab/README.md)
* [Notatnik](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/lab/MyFW_MNIST.ipynb)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.