# Introduction aux réseaux neuronaux : Perceptron

## [Quiz pré-conférence](https://ff-quizzes.netlify.app/en/ai/quiz/5)

L'une des premières tentatives pour mettre en œuvre quelque chose de similaire à un réseau neuronal moderne a été réalisée par Frank Rosenblatt du Cornell Aeronautical Laboratory en 1957. Il s'agissait d'une implémentation matérielle appelée "Mark-1", conçue pour reconnaître des figures géométriques primitives, telles que des triangles, des carrés et des cercles.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/fr/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/fr/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='Le Perceptron Mark 1' />|

> Images [tirées de Wikipédia](https://en.wikipedia.org/wiki/Perceptron)

Une image d'entrée était représentée par un tableau de 20x20 photorécepteurs, ce qui signifie que le réseau neuronal avait 400 entrées et une sortie binaire. Un réseau simple contenait un seul neurone, également appelé une **unité logique seuil**. Les poids du réseau neuronal fonctionnaient comme des potentiomètres nécessitant un réglage manuel pendant la phase d'entraînement.

> ✅ Un potentiomètre est un dispositif qui permet à l'utilisateur d'ajuster la résistance d'un circuit.

> Le New York Times écrivait à propos du perceptron à l'époque : *l'embryon d'un ordinateur électronique que [la Marine] espère capable de marcher, parler, voir, écrire, se reproduire et être conscient de son existence.*

## Modèle de Perceptron

Supposons que nous ayons N caractéristiques dans notre modèle, auquel cas le vecteur d'entrée serait un vecteur de taille N. Un perceptron est un modèle de **classification binaire**, c'est-à-dire qu'il peut distinguer entre deux classes de données d'entrée. Nous supposerons que pour chaque vecteur d'entrée x, la sortie de notre perceptron sera soit +1, soit -1, selon la classe. La sortie sera calculée à l'aide de la formule :

y(x) = f(w<sup>T</sup>x)

où f est une fonction d'activation en escalier.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/fr/activation-func.b4924007c7ce7764.webp"/>

## Entraînement du Perceptron

Pour entraîner un perceptron, nous devons trouver un vecteur de poids w qui classe correctement la plupart des valeurs, c'est-à-dire qui minimise l'**erreur**. Cette erreur E est définie par le **critère du perceptron** de la manière suivante :

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

où :

* la somme est effectuée sur les points de données d'entraînement i qui entraînent une mauvaise classification,
* x<sub>i</sub> est la donnée d'entrée, et t<sub>i</sub> est soit -1, soit +1 pour les exemples négatifs et positifs respectivement.

Ce critère est considéré comme une fonction des poids w, et nous devons le minimiser. Souvent, une méthode appelée **descente de gradient** est utilisée, dans laquelle nous commençons avec des poids initiaux w<sup>(0)</sup>, puis à chaque étape, nous mettons à jour les poids selon la formule :

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Ici, &eta; est le **taux d'apprentissage**, et &nabla;E(w) désigne le **gradient** de E. Après avoir calculé le gradient, nous obtenons :

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

L'algorithme en Python ressemble à ceci :

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

## Conclusion

Dans cette leçon, vous avez appris ce qu'est un perceptron, un modèle de classification binaire, et comment l'entraîner en utilisant un vecteur de poids.

## 🚀 Défi

Si vous souhaitez essayer de construire votre propre perceptron, essayez [ce laboratoire sur Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) qui utilise le [concepteur Azure ML](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Quiz post-conférence](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Révision & Auto-apprentissage

Pour voir comment nous pouvons utiliser un perceptron pour résoudre un problème simple ainsi que des problèmes réels, et pour continuer à apprendre, consultez le notebook [Perceptron](Perceptron.ipynb).

Voici également un [article intéressant sur les perceptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Devoir](lab/README.md)

Dans cette leçon, nous avons implémenté un perceptron pour une tâche de classification binaire, et nous l'avons utilisé pour classifier entre deux chiffres manuscrits. Dans ce laboratoire, vous êtes invité à résoudre entièrement le problème de classification des chiffres, c'est-à-dire déterminer quel chiffre correspond le plus probablement à une image donnée.

* [Instructions](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)

---

