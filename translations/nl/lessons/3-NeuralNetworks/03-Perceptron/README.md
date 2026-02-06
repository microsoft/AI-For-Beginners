# Introductie tot Neurale Netwerken: Perceptron

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Een van de eerste pogingen om iets te implementeren dat lijkt op een modern neuraal netwerk werd in 1957 gedaan door Frank Rosenblatt van het Cornell Aeronautical Laboratory. Het was een hardware-implementatie genaamd "Mark-1", ontworpen om primitieve geometrische figuren te herkennen, zoals driehoeken, vierkanten en cirkels.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/nl/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/nl/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='The Mark 1 Perceptron' />|

> Afbeeldingen [van Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Een invoerafbeelding werd weergegeven door een 20x20 fotocelarray, waardoor het neurale netwerk 400 ingangen had en één binaire uitvoer. Een eenvoudig netwerk bevatte één neuron, ook wel een **drempelloogica-eenheid** genoemd. De gewichten van het neurale netwerk fungeerden als potentiometers die handmatig moesten worden aangepast tijdens de trainingsfase.

> ✅ Een potentiometer is een apparaat waarmee de gebruiker de weerstand van een circuit kan aanpassen.

> De New York Times schreef destijds over de perceptron: *het embryo van een elektronische computer die [de marine] verwacht te kunnen laten lopen, praten, zien, schrijven, zichzelf reproduceren en zich bewust zijn van zijn bestaan.*

## Perceptronmodel

Stel dat we N kenmerken in ons model hebben, in welk geval de invoervector een vector van grootte N zou zijn. Een perceptron is een model voor **binaire classificatie**, wat betekent dat het onderscheid kan maken tussen twee klassen van invoergegevens. We gaan ervan uit dat voor elke invoervector x de uitvoer van ons perceptron ofwel +1 of -1 is, afhankelijk van de klasse. De uitvoer wordt berekend met de formule:

y(x) = f(w<sup>T</sup>x)

waarbij f een stap-activatiefunctie is

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/nl/activation-func.b4924007c7ce7764.webp"/>

## Het trainen van de Perceptron

Om een perceptron te trainen, moeten we een gewichtenvector w vinden die de meeste waarden correct classificeert, oftewel resulteert in de kleinste **fout**. Deze fout E wordt gedefinieerd door het **perceptroncriterium** op de volgende manier:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

waarbij:

* de som wordt genomen over die trainingsdatapunten i die resulteren in een verkeerde classificatie
* x<sub>i</sub> de invoergegevens zijn, en t<sub>i</sub> ofwel -1 of +1 is voor respectievelijk negatieve en positieve voorbeelden.

Dit criterium wordt beschouwd als een functie van de gewichten w, en we moeten het minimaliseren. Vaak wordt een methode genaamd **gradient descent** gebruikt, waarbij we beginnen met enkele initiële gewichten w<sup>(0)</sup>, en vervolgens bij elke stap de gewichten bijwerken volgens de formule:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Hierbij is &eta; de zogenaamde **leersnelheid**, en &nabla;E(w) de **gradiënt** van E. Na het berekenen van de gradiënt krijgen we:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Het algoritme in Python ziet er als volgt uit:

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

## Conclusie

In deze les heb je geleerd over een perceptron, een model voor binaire classificatie, en hoe je het kunt trainen met behulp van een gewichtenvector.

## 🚀 Uitdaging

Als je zelf een perceptron wilt bouwen, probeer dan [deze lab op Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), die gebruikmaakt van de [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Herziening & Zelfstudie

Om te zien hoe we een perceptron kunnen gebruiken om een eenvoudig probleem en ook echte problemen op te lossen, en om verder te leren - ga naar het [Perceptron](Perceptron.ipynb) notebook.

Hier is ook een interessant [artikel over perceptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Opdracht](lab/README.md)

In deze les hebben we een perceptron geïmplementeerd voor een binaire classificatietaak, en we hebben het gebruikt om onderscheid te maken tussen twee handgeschreven cijfers. In deze lab wordt je gevraagd om het probleem van cijferclassificatie volledig op te lossen, oftewel te bepalen welk cijfer het meest waarschijnlijk overeenkomt met een gegeven afbeelding.

* [Instructies](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)

---

