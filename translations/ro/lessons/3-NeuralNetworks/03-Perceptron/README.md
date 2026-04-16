# Introducere în Rețele Neuronale: Perceptron

## [Chestionar înainte de lecție](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Una dintre primele încercări de a implementa ceva similar cu o rețea neuronală modernă a fost realizată de Frank Rosenblatt de la Cornell Aeronautical Laboratory în 1957. A fost o implementare hardware numită "Mark-1", concepută pentru a recunoaște figuri geometrice primitive, cum ar fi triunghiuri, pătrate și cercuri.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/ro/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/ro/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='The Mark 1 Perceptron' />|

> Imagini [de pe Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

O imagine de intrare era reprezentată de o matrice de fotocelule de 20x20, astfel încât rețeaua neuronală avea 400 de intrări și o ieșire binară. O rețea simplă conținea un singur neuron, numit și **unitate logică de prag**. Greutățile rețelei neuronale funcționau ca potențiometre care necesitau ajustare manuală în timpul fazei de antrenare.

> ✅ Un potențiometru este un dispozitiv care permite utilizatorului să ajusteze rezistența unui circuit.

> The New York Times a scris despre perceptron la acea vreme: *embrionul unui computer electronic pe care [Marina] se așteaptă să fie capabil să meargă, să vorbească, să vadă, să scrie, să se reproducă și să fie conștient de propria existență.*

## Modelul Perceptron

Să presupunem că avem N caracteristici în modelul nostru, caz în care vectorul de intrare ar fi un vector de dimensiune N. Un perceptron este un model de **clasificare binară**, adică poate distinge între două clase de date de intrare. Vom presupune că pentru fiecare vector de intrare x, ieșirea perceptronului nostru va fi fie +1, fie -1, în funcție de clasă. Ieșirea va fi calculată folosind formula:

y(x) = f(w<sup>T</sup>x)

unde f este o funcție de activare de tip treaptă.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/ro/activation-func.b4924007c7ce7764.webp"/>

## Antrenarea Perceptronului

Pentru a antrena un perceptron, trebuie să găsim un vector de greutăți w care clasifică corect majoritatea valorilor, adică rezultă în cea mai mică **eroare**. Această eroare E este definită prin **criteriul perceptronului** în următorul mod:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

unde:

* suma este luată pentru acele puncte de date de antrenament i care duc la clasificarea greșită
* x<sub>i</sub> este datele de intrare, iar t<sub>i</sub> este fie -1, fie +1 pentru exemplele negative și pozitive, respectiv.

Acest criteriu este considerat ca o funcție a greutăților w, și trebuie să îl minimizăm. Adesea, se folosește o metodă numită **descendentă pe gradient**, în care începem cu niște greutăți inițiale w<sup>(0)</sup>, și apoi la fiecare pas actualizăm greutățile conform formulei:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Aici &eta; este așa-numita **rată de învățare**, iar &nabla;E(w) denotă **gradientul** lui E. După ce calculăm gradientul, ajungem la:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Algoritmul în Python arată astfel:

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

## Concluzie

În această lecție, ai învățat despre perceptron, care este un model de clasificare binară, și cum să îl antrenezi folosind un vector de greutăți.

## 🚀 Provocare

Dacă dorești să încerci să construiești propriul perceptron, încearcă [acest laborator pe Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), care folosește [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Chestionar după lecție](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Recapitulare & Studiu Individual

Pentru a vedea cum putem folosi perceptronul pentru a rezolva o problemă simplă, precum și probleme din viața reală, și pentru a continua să înveți - accesează notebook-ul [Perceptron](Perceptron.ipynb).

Iată un articol interesant despre [perceptroni](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Temă](lab/README.md)

În această lecție, am implementat un perceptron pentru o sarcină de clasificare binară și l-am folosit pentru a clasifica între două cifre scrise de mână. În acest laborator, ți se cere să rezolvi problema clasificării cifrelor în întregime, adică să determini care cifră corespunde cel mai probabil unei imagini date.

* [Instrucțiuni](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)

---

