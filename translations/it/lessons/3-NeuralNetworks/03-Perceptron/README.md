# Introduzione alle Reti Neurali: Perceptron

## [Quiz pre-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/5)

Uno dei primi tentativi di implementare qualcosa di simile a una rete neurale moderna fu realizzato da Frank Rosenblatt del Cornell Aeronautical Laboratory nel 1957. Si trattava di un'implementazione hardware chiamata "Mark-1", progettata per riconoscere figure geometriche primitive, come triangoli, quadrati e cerchi.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/it/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/it/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='Il Perceptron Mark 1' />|

> Immagini [da Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Un'immagine di input era rappresentata da una matrice di fotocellule 20x20, quindi la rete neurale aveva 400 ingressi e un'uscita binaria. Una rete semplice conteneva un solo neurone, chiamato anche **threshold logic unit**. I pesi della rete neurale funzionavano come potenziometri che richiedevano regolazioni manuali durante la fase di addestramento.

> ✅ Un potenziometro è un dispositivo che consente all'utente di regolare la resistenza di un circuito.

> Il New York Times scrisse del perceptron in quel periodo: *l'embrione di un computer elettronico che [la Marina] si aspetta sarà in grado di camminare, parlare, vedere, scrivere, riprodursi e essere consapevole della propria esistenza.*

## Modello del Perceptron

Supponiamo di avere N caratteristiche nel nostro modello, nel qual caso il vettore di input sarebbe un vettore di dimensione N. Un perceptron è un modello di **classificazione binaria**, cioè può distinguere tra due classi di dati di input. Supponiamo che per ogni vettore di input x l'output del nostro perceptron sia +1 o -1, a seconda della classe. L'output sarà calcolato utilizzando la formula:

y(x) = f(w<sup>T</sup>x)

dove f è una funzione di attivazione a gradino

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/it/activation-func.b4924007c7ce7764.webp"/>

## Addestramento del Perceptron

Per addestrare un perceptron, dobbiamo trovare un vettore di pesi w che classifichi correttamente la maggior parte dei valori, cioè che produca il **minimo errore**. Questo errore E è definito dal **criterio del perceptron** nel seguente modo:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

dove:

* la somma è calcolata sui punti di dati di addestramento i che risultano classificati in modo errato
* x<sub>i</sub> è il dato di input, e t<sub>i</sub> è -1 o +1 per esempi negativi e positivi rispettivamente.

Questo criterio è considerato una funzione dei pesi w, e dobbiamo minimizzarlo. Spesso si utilizza un metodo chiamato **discesa del gradiente**, in cui si parte da un vettore di pesi iniziale w<sup>(0)</sup>, e poi a ogni passo si aggiornano i pesi secondo la formula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Qui &eta; è il cosiddetto **tasso di apprendimento**, e &nabla;E(w) denota il **gradiente** di E. Dopo aver calcolato il gradiente, otteniamo:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

L'algoritmo in Python appare così:

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

## Conclusione

In questa lezione, hai imparato cos'è un perceptron, un modello di classificazione binaria, e come addestrarlo utilizzando un vettore di pesi.

## 🚀 Sfida

Se vuoi provare a costruire il tuo perceptron, prova [questo laboratorio su Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) che utilizza il [designer di Azure ML](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Quiz post-lezione](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Revisione e Studio Autonomo

Per vedere come possiamo utilizzare il perceptron per risolvere un problema semplice e problemi reali, e per continuare a imparare, vai al notebook [Perceptron](Perceptron.ipynb).

Ecco un interessante [articolo sui perceptron](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Compito](lab/README.md)

In questa lezione, abbiamo implementato un perceptron per un compito di classificazione binaria e lo abbiamo utilizzato per classificare tra due cifre scritte a mano. In questo laboratorio, ti viene chiesto di risolvere completamente il problema della classificazione delle cifre, cioè determinare quale cifra corrisponde più probabilmente a una data immagine.

* [Istruzioni](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)

---

