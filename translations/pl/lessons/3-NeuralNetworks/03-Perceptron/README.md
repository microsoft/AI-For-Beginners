# Wprowadzenie do sieci neuronowych: Perceptron

## [Quiz przed wykładem](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Jednym z pierwszych prób stworzenia czegoś podobnego do współczesnej sieci neuronowej był projekt Franka Rosenblatta z Cornell Aeronautical Laboratory w 1957 roku. Była to implementacja sprzętowa nazwana "Mark-1", zaprojektowana do rozpoznawania prostych figur geometrycznych, takich jak trójkąty, kwadraty i koła.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/pl/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/pl/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='The Mark 1 Perceptron' />|

> Obrazy [z Wikipedii](https://en.wikipedia.org/wiki/Perceptron)

Obraz wejściowy był reprezentowany przez matrycę fotokomórek o wymiarach 20x20, co oznaczało, że sieć neuronowa miała 400 wejść i jedno binarne wyjście. Prosta sieć zawierała jeden neuron, nazywany również **jednostką logiczną progową**. Wagi sieci neuronowej działały jak potencjometry, które wymagały ręcznego dostosowania podczas fazy treningowej.

> ✅ Potencjometr to urządzenie, które pozwala użytkownikowi regulować opór w obwodzie.

> The New York Times pisał o perceptronie w tamtym czasie: *zarodek elektronicznego komputera, który [Marynarka Wojenna] oczekuje, że będzie mógł chodzić, mówić, widzieć, pisać, reprodukować się i być świadomy swojego istnienia.*

## Model perceptronu

Załóżmy, że mamy N cech w naszym modelu, w takim przypadku wektor wejściowy będzie miał rozmiar N. Perceptron to model **klasyfikacji binarnej**, czyli potrafi rozróżniać między dwoma klasami danych wejściowych. Zakładamy, że dla każdego wektora wejściowego x wyjście perceptronu będzie wynosić +1 lub -1, w zależności od klasy. Wyjście będzie obliczane według wzoru:

y(x) = f(w<sup>T</sup>x)

gdzie f to funkcja aktywacji typu schodkowego

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/pl/activation-func.b4924007c7ce7764.webp"/>

## Trenowanie perceptronu

Aby wytrenować perceptron, musimy znaleźć wektor wag w, który klasyfikuje większość wartości poprawnie, czyli prowadzi do najmniejszego **błędu**. Ten błąd E jest definiowany przez **kryterium perceptronu** w następujący sposób:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

gdzie:

* suma jest obliczana dla tych punktów danych treningowych i, które są błędnie klasyfikowane
* x<sub>i</sub> to dane wejściowe, a t<sub>i</sub> wynosi -1 lub +1 dla odpowiednio negatywnych i pozytywnych przykładów.

To kryterium jest traktowane jako funkcja wag w, którą musimy zminimalizować. Często stosuje się metodę **gradientu prostego**, w której zaczynamy od początkowych wag w<sup>(0)</sup>, a następnie na każdym kroku aktualizujemy wagi według wzoru:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Tutaj &eta; to tak zwana **szybkość uczenia**, a &nabla;E(w) oznacza **gradient** funkcji E. Po obliczeniu gradientu otrzymujemy:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

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

W tej lekcji nauczyłeś się o perceptronie, który jest modelem klasyfikacji binarnej, oraz jak go trenować, używając wektora wag.

## 🚀 Wyzwanie

Jeśli chcesz spróbować zbudować własny perceptron, wypróbuj [to laboratorium na Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), które korzysta z [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Quiz po wykładzie](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Przegląd i samodzielna nauka

Aby zobaczyć, jak można użyć perceptronu do rozwiązania prostego problemu oraz problemów z życia codziennego, i aby kontynuować naukę - przejdź do notatnika [Perceptron](Perceptron.ipynb).

Oto interesujący [artykuł o perceptronach](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Zadanie](lab/README.md)

W tej lekcji zaimplementowaliśmy perceptron do zadania klasyfikacji binarnej i użyliśmy go do klasyfikacji dwóch cyfr pisanych ręcznie. W tym laboratorium masz za zadanie rozwiązać problem klasyfikacji cyfr w całości, czyli określić, która cyfra najprawdopodobniej odpowiada danemu obrazowi.

* [Instrukcje](lab/README.md)
* [Notatnik](lab/PerceptronMultiClass.ipynb)

---

