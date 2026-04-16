# Introduktion till neurala nätverk: Perceptron

## [Quiz före föreläsning](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Ett av de första försöken att implementera något liknande ett modernt neuralt nätverk gjordes av Frank Rosenblatt från Cornell Aeronautical Laboratory år 1957. Det var en hårdvaruimplementation som kallades "Mark-1", designad för att känna igen enkla geometriska figurer, såsom trianglar, kvadrater och cirklar.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/sv/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/sv/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='The Mark 1 Perceptron' />|

> Bilder [från Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

En inmatningsbild representerades av en 20x20 fotocellmatris, vilket innebar att det neurala nätverket hade 400 ingångar och en binär utgång. Ett enkelt nätverk innehöll en neuron, även kallad en **tröskellogikenhet**. Vikterna i det neurala nätverket fungerade som potentiometrar som behövde justeras manuellt under träningsfasen.

> ✅ En potentiometer är en enhet som gör det möjligt att justera motståndet i en krets.

> The New York Times skrev om perceptron vid den tiden: *embryot till en elektronisk dator som [marinen] förväntar sig ska kunna gå, prata, se, skriva, reproducera sig själv och vara medveten om sin existens.*

## Perceptronmodell

Anta att vi har N funktioner i vår modell, vilket innebär att inmatningsvektorn skulle vara en vektor av storlek N. Ett perceptron är en modell för **binär klassificering**, det vill säga den kan skilja mellan två klasser av indata. Vi antar att för varje inmatningsvektor x kommer utgången från vårt perceptron att vara antingen +1 eller -1, beroende på klassen. Utgången beräknas med formeln:

y(x) = f(w<sup>T</sup>x)

där f är en stegaktiveringsfunktion

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/sv/activation-func.b4924007c7ce7764.webp"/>

## Träning av perceptron

För att träna ett perceptron behöver vi hitta en viktvektor w som klassificerar de flesta värden korrekt, det vill säga resulterar i det minsta **felet**. Detta fel E definieras av **perceptronkriteriet** på följande sätt:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

där:

* summan tas över de träningsdatapunkter i som resulterar i fel klassificering
* x<sub>i</sub> är indata, och t<sub>i</sub> är antingen -1 eller +1 för negativa respektive positiva exempel.

Detta kriterium betraktas som en funktion av vikterna w, och vi behöver minimera det. Ofta används en metod som kallas **gradientnedstigning**, där vi börjar med några initiala vikter w<sup>(0)</sup>, och sedan vid varje steg uppdaterar vikterna enligt formeln:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Här är &eta; den så kallade **inlärningshastigheten**, och &nabla;E(w) betecknar **gradienten** av E. Efter att vi har beräknat gradienten får vi:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

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

I denna lektion lärde du dig om ett perceptron, som är en modell för binär klassificering, och hur man tränar det genom att använda en viktvektor.

## 🚀 Utmaning

Om du vill prova att bygga ditt eget perceptron, testa [detta labb på Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) som använder [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Quiz efter föreläsning](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Granskning & Självstudier

För att se hur vi kan använda perceptron för att lösa ett enkelt problem samt verkliga problem, och för att fortsätta lära dig - gå till [Perceptron](Perceptron.ipynb)-notebook.

Här är en intressant [artikel om perceptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Uppgift](lab/README.md)

I denna lektion har vi implementerat ett perceptron för en binär klassificeringsuppgift, och vi har använt det för att klassificera mellan två handskrivna siffror. I detta labb ombeds du att lösa problemet med sifferklassificering helt och hållet, det vill säga att avgöra vilken siffra som mest sannolikt motsvarar en given bild.

* [Instruktioner](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)

---

