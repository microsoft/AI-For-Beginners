# Introduktion till Neurala Nätverk: Perceptron

## [För-lärare quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Ett av de första försöken att implementera något liknande ett modernt neuralt nätverk gjordes av Frank Rosenblatt från Cornell Aeronautical Laboratory år 1957. Det var en hårdvaruimplementation kallad "Mark-1", designad för att känna igen primitiva geometriska figurer, såsom trianglar, fyrkanter och cirklar.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Bilder [från Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

En ingångsbild representerades av en 20x20 fotocell-array, så det neurala nätverket hade 400 ingångar och en binär utgång. Ett enkelt nätverk innehöll en neuron, även kallad en **tröskellogik-enhet**. Vikterna i det neurala nätverket fungerade som potentiometrar som krävde manuell justering under träningsfasen.

> ✅ En potentiometer är en enhet som låter användaren justera motståndet i en krets.

> The New York Times skrev om perceptron vid den tiden: *embryot av en elektronisk dator som [marinen] förväntar sig kommer att kunna gå, prata, se, skriva, reproducera sig själv och vara medveten om sin existens.*

## Perceptronmodell

Anta att vi har N egenskaper i vår modell, i vilket fall ingångsvektorn skulle vara en vektor av storlek N. En perceptron är en **binär klassificerings**modell, dvs. den kan särskilja mellan två klasser av ingångsdata. Vi antar att för varje ingångsvektor x skulle utgången av vår perceptron vara antingen +1 eller -1, beroende på klassen. Utgången beräknas med hjälp av formeln:

y(x) = f(w<sup>T</sup>x)

där f är en stegaktiveringsfunktion

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Träning av Perceptron

För att träna en perceptron behöver vi hitta en viktvektor w som klassificerar de flesta värdena korrekt, dvs. ger den minsta **felet**. Detta fel E definieras av **perceptron-kriteriet** på följande sätt:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

där:

* summan tas över de träningsdata punkterna i som resulterar i felaktig klassificering
* x<sub>i</sub> är ingångsdata, och t<sub>i</sub> är antingen -1 eller +1 för negativa och positiva exempel respektive.

Detta kriterium betraktas som en funktion av vikterna w, och vi behöver minimera det. Ofta används en metod som kallas **gradientnedstigning**, där vi börjar med några initiala vikter w<sup>(0)</sup>, och sedan uppdaterar vikterna vid varje steg enligt formeln:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Här är η den så kallade **inlärningshastigheten**, och ∇E(w) betecknar **gradienten** av E. Efter att vi har beräknat gradienten får vi

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritmen i Python ser ut så här:

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

## Slutsats

I denna lektion har du lärt dig om en perceptron, som är en binär klassificeringsmodell, och hur man tränar den med hjälp av en viktvektor.

## 🚀 Utmaning

Om du vill försöka bygga din egen perceptron, prova [detta labb på Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) som använder [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Efter-lärare quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Granskning & Självstudie

För att se hur vi kan använda perceptron för att lösa ett leksaksproblem såväl som verkliga problem, och för att fortsätta lära oss - gå till [Perceptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb) anteckningsbok.

Här är en intressant [artikel om perceptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590
) också.

## [Uppgift](lab/README.md)

I denna lektion har vi implementerat en perceptron för en binär klassificeringsuppgift, och vi har använt den för att klassificera mellan två handskrivna siffror. I detta labb ombeds du att helt lösa problemet med sifferklassificering, dvs. att avgöra vilken siffra som mest sannolikt motsvarar en given bild.

* [Instruktioner](lab/README.md)
* [Anteckningsbok](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.