<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0c37770bba4fff3c71dc00eb261ee61b",
  "translation_date": "2025-08-24T10:42:35+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "pl"
}
-->
# Wprowadzenie do sieci neuronowych: Perceptron

## [Quiz przed wykładem](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Jedną z pierwszych prób stworzenia czegoś na wzór współczesnej sieci neuronowej podjął Frank Rosenblatt z Cornell Aeronautical Laboratory w 1957 roku. Była to implementacja sprzętowa o nazwie "Mark-1", zaprojektowana do rozpoznawania prostych figur geometrycznych, takich jak trójkąty, kwadraty i koła.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Obrazy [z Wikipedii](https://en.wikipedia.org/wiki/Perceptron)

Obraz wejściowy był reprezentowany przez matrycę fotokomórek o wymiarach 20x20, co oznaczało, że sieć neuronowa miała 400 wejść i jedno wyjście binarne. Prosta sieć zawierała jeden neuron, nazywany również **jednostką logiczną progową**. Wagi sieci neuronowej działały jak potencjometry, które wymagały ręcznego dostosowania podczas fazy uczenia.

> ✅ Potencjometr to urządzenie, które pozwala użytkownikowi regulować opór w obwodzie.

> The New York Times pisał o perceptronie w tamtym czasie: *zalążek elektronicznego komputera, który [Marynarka Wojenna] spodziewa się, że będzie mógł chodzić, mówić, widzieć, pisać, reprodukować się i być świadomy swojego istnienia.*

## Model perceptronu

Załóżmy, że nasz model ma N cech, w takim przypadku wektor wejściowy będzie miał rozmiar N. Perceptron to model klasyfikacji **binarny**, czyli taki, który potrafi rozróżniać między dwiema klasami danych wejściowych. Przyjmiemy, że dla każdego wektora wejściowego x wyjście perceptronu będzie wynosić +1 lub -1, w zależności od klasy. Wyjście obliczane jest za pomocą wzoru:

y(x) = f(w<sup>T</sup>x)

gdzie f to funkcja aktywacji typu schodkowego

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Trenowanie perceptronu

Aby wytrenować perceptron, musimy znaleźć wektor wag w, który klasyfikuje większość wartości poprawnie, czyli minimalizuje **błąd**. Błąd E definiowany jest przez **kryterium perceptronu** w następujący sposób:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

gdzie:

* suma obejmuje te punkty danych treningowych i, które zostały błędnie sklasyfikowane,
* x<sub>i</sub> to dane wejściowe, a t<sub>i</sub> wynosi -1 lub +1 dla odpowiednio negatywnych i pozytywnych przykładów.

To kryterium traktowane jest jako funkcja wag w, którą musimy zminimalizować. Często stosuje się metodę zwaną **spadkiem gradientu**, w której zaczynamy od początkowych wag w<sup>(0)</sup>, a następnie na każdym kroku aktualizujemy wagi zgodnie ze wzorem:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Tutaj η to tzw. **współczynnik uczenia się**, a ∇E(w) oznacza **gradient** funkcji E. Po obliczeniu gradientu otrzymujemy:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algorytm w Pythonie wygląda następująco:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Podsumowanie

W tej lekcji nauczyłeś się, czym jest perceptron, czyli model klasyfikacji binarnej, oraz jak go trenować, używając wektora wag.

## 🚀 Wyzwanie

Jeśli chcesz spróbować stworzyć własny perceptron, wypróbuj [to laboratorium na Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), które korzysta z [projektanta Azure ML](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Quiz po wykładzie](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Przegląd i samodzielna nauka

Aby zobaczyć, jak można użyć perceptronu do rozwiązania prostych problemów oraz problemów rzeczywistych, i kontynuować naukę, przejdź do notatnika [Perceptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb).

Oto ciekawy [artykuł o perceptronach](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Zadanie](lab/README.md)

W tej lekcji zaimplementowaliśmy perceptron do zadania klasyfikacji binarnej i użyliśmy go do rozróżniania dwóch cyfr pisanych ręcznie. W tym laboratorium masz za zadanie rozwiązać problem klasyfikacji cyfr w całości, czyli określić, która cyfra najprawdopodobniej odpowiada danemu obrazowi.

* [Instrukcje](lab/README.md)
* [Notatnik](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.