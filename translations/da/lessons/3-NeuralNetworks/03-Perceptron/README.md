# Introduktion til Neurale Netværk: Perceptron

## [Quiz før lektionen](https://ff-quizzes.netlify.app/en/ai/quiz/5)

En af de første forsøg på at implementere noget, der minder om et moderne neuralt netværk, blev udført af Frank Rosenblatt fra Cornell Aeronautical Laboratory i 1957. Det var en hardware-implementering kaldet "Mark-1", designet til at genkende primitive geometriske figurer som trekanter, firkanter og cirkler.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/da/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/da/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='The Mark 1 Perceptron' />|

> Billeder [fra Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Et inputbillede blev repræsenteret af et 20x20 fotocelle-array, så det neurale netværk havde 400 input og én binær output. Et simpelt netværk indeholdt én neuron, også kaldet en **threshold logic unit**. Vægtene i det neurale netværk fungerede som potentiometre, der krævede manuel justering under træningsfasen.

> ✅ Et potentiometer er en enhed, der gør det muligt for brugeren at justere modstanden i et kredsløb.

> The New York Times skrev dengang om perceptronen: *embryoet til en elektronisk computer, som [flåden] forventer vil kunne gå, tale, se, skrive, reproducere sig selv og være bevidst om sin eksistens.*

## Perceptron-modellen

Antag, at vi har N funktioner i vores model, i hvilket tilfælde inputvektoren vil være en vektor af størrelse N. En perceptron er en **binær klassifikationsmodel**, dvs. den kan skelne mellem to klasser af inputdata. Vi antager, at for hver inputvektor x vil outputtet fra vores perceptron være enten +1 eller -1, afhængigt af klassen. Outputtet beregnes ved hjælp af formlen:

y(x) = f(w<sup>T</sup>x)

hvor f er en step-aktiveringsfunktion

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/da/activation-func.b4924007c7ce7764.webp"/>

## Træning af Perceptron

For at træne en perceptron skal vi finde en vægtvektor w, der klassificerer de fleste værdier korrekt, dvs. resulterer i den mindste **fejl**. Denne fejl E defineres ved **perceptron-kriteriet** på følgende måde:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

hvor:

* summen tages over de træningsdatapunkter i, der resulterer i en forkert klassifikation
* x<sub>i</sub> er inputdata, og t<sub>i</sub> er enten -1 eller +1 for henholdsvis negative og positive eksempler.

Dette kriterium betragtes som en funktion af vægtene w, og vi skal minimere det. Ofte bruges en metode kaldet **gradient descent**, hvor vi starter med nogle indledende vægte w<sup>(0)</sup>, og derefter opdaterer vægtene ved hvert trin ifølge formlen:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Her er &eta; den såkaldte **læringsrate**, og &nabla;E(w) betegner **gradienten** af E. Efter at vi har beregnet gradienten, ender vi med:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Algoritmen i Python ser sådan ud:

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

## Konklusion

I denne lektion lærte du om en perceptron, som er en binær klassifikationsmodel, og hvordan man træner den ved hjælp af en vægtvektor.

## 🚀 Udfordring

Hvis du vil prøve at bygge din egen perceptron, kan du prøve [dette lab på Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), som bruger [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Quiz efter lektionen](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Gennemgang & Selvstudie

For at se, hvordan vi kan bruge perceptron til at løse et simpelt problem såvel som virkelige problemer, og for at fortsætte med at lære - gå til [Perceptron](Perceptron.ipynb)-notebooken.

Her er en interessant [artikel om perceptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Opgave](lab/README.md)

I denne lektion har vi implementeret en perceptron til en binær klassifikationsopgave, og vi har brugt den til at klassificere mellem to håndskrevne cifre. I dette lab bliver du bedt om at løse problemet med cifergenkendelse fuldstændigt, dvs. bestemme hvilket ciffer, der sandsynligvis svarer til et givet billede.

* [Instruktioner](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)

---

