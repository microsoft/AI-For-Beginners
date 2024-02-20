# Introducción a las redes neuronales: perceptrón

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Uno de los primeros intentos de implementar algo similar a una red neuronal moderna lo realizó Frank Rosenblatt del Laboratorio Aeronáutico de Cornell en 1957. Se trataba de una implementación de hardware llamada "Mark-1", diseñada para reconocer figuras geométricas primitivas, como triángulos, cuadrados. y círculos.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Images [from Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Una imagen de entrada estaba representada por una matriz de fotocélulas de 20x20, por lo que la red neuronal tenía 400 entradas y una salida binaria. Una red simple contenía una neurona, también llamada **unidad lógica de umbral**. Los pesos de las redes neuronales actuaron como potenciómetros que requirieron ajuste manual durante la fase de entrenamiento.

> ✅ Un potenciómetro es un dispositivo que permite al usuario ajustar la resistencia de un circuito.

> El New York Times escribió en aquella época sobre el perceptrón: *el embrión de una computadora electrónica que [la Marina] espera que pueda caminar, hablar, ver, escribir, reproducirse y ser consciente de su existencia.*

## Modelo de perceptrón

Supongamos que tenemos N características en nuestro modelo, en cuyo caso el vector de entrada sería un vector de tamaño N. Un perceptrón es un modelo de **clasificación binaria**, es decir, puede distinguir entre dos clases de datos de entrada. Supondremos que para cada vector de entrada x la salida de nuestro perceptrón sería +1 o -1, dependiendo de la clase. La salida se calculará mediante la fórmula:

y(x) = f(w<sup>T</sup>x)

donde f es una función de activación escalonada

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Entrenando el perceptrón

Para entrenar un perceptrón necesitamos encontrar un vector de pesos w que clasifique la mayoría de los valores correctamente, es decir, que dé como resultado el **error** más pequeño. Este error se define mediante el **criterio de perceptrón** de la siguiente manera:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

dónde:

* la suma se toma de aquellos puntos de datos de entrenamiento i que resultan en una clasificación incorrecta
* x<sub>i</sub> son los datos de entrada y t<sub>i</sub> es -1 o +1 para ejemplos negativos y positivos, respectivamente.

Este criterio se considera en función de los pesos w y debemos minimizarlo. A menudo, se utiliza un método llamado **descenso de gradiente**, en el que comenzamos con algunos pesos iniciales w<sup>(0)</sup> y luego, en cada paso, actualizamos los pesos de acuerdo con la fórmula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Aquí &eta; es la llamada **tasa de aprendizaje**, y &nabla;E(w) denota el **gradiente** de E. Después de calcular el gradiente, terminamos con

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

El algoritmo en Python se ve así:

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

## Conclusión

En esta lección, aprendió sobre un perceptrón, que es un modelo de clasificación binaria, y cómo entrenarlo usando un vector de pesos.

## 🚀 Desafío

Si desea intentar construir su propio perceptrón, intente [this lab on Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) que utiliza el [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Revisión y autoestudio

Para ver cómo podemos usar el perceptrón para resolver un problema de juguete, así como problemas de la vida real, y continuar aprendiendo, vaya a [Perceptron](Perceptron.ipynb) notebook.

Aquí hay un interesante [article about perceptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590
) también.

## [Assignment](lab/README.md)

En esta lección, hemos implementado un perceptrón para tareas de clasificación binaria y lo hemos usado para clasificar entre dos dígitos escritos a mano. En esta práctica de laboratorio, se le pedirá que resuelva por completo el problema de clasificación de dígitos, es decir, que determine qué dígito tiene más probabilidades de corresponder a una imagen determinada.

* [Instructions](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)
