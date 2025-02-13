# Introducción a las Redes Neuronales: Perceptrón

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

Uno de los primeros intentos de implementar algo similar a una red neuronal moderna fue realizado por Frank Rosenblatt del Laboratorio Aeronáutico de Cornell en 1957. Fue una implementación de hardware llamada "Mark-1", diseñada para reconocer figuras geométricas primitivas, como triángulos, cuadrados y círculos.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='El Perceptrón Mark 1' />|

> Imágenes [de Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Una imagen de entrada se representaba mediante una matriz de fotoceldas de 20x20, por lo que la red neuronal tenía 400 entradas y una salida binaria. Una red simple contenía una neurona, también llamada **unidad lógica de umbral**. Los pesos de la red neuronal funcionaban como potenciómetros que requerían ajuste manual durante la fase de entrenamiento.

> ✅ Un potenciómetro es un dispositivo que permite al usuario ajustar la resistencia de un circuito.

> El New York Times escribió sobre el perceptrón en ese momento: *el embrión de una computadora electrónica que [la Marina] espera que pueda caminar, hablar, ver, escribir, reproducirse y ser consciente de su existencia.*

## Modelo de Perceptrón

Supongamos que tenemos N características en nuestro modelo, en cuyo caso el vector de entrada sería un vector de tamaño N. Un perceptrón es un modelo de **clasificación binaria**, es decir, puede distinguir entre dos clases de datos de entrada. Asumiremos que para cada vector de entrada x, la salida de nuestro perceptrón será ya sea +1 o -1, dependiendo de la clase. La salida se calculará utilizando la fórmula:

y(x) = f(w<sup>T</sup>x)

donde f es una función de activación de escalón.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Entrenamiento del Perceptrón

Para entrenar un perceptrón, necesitamos encontrar un vector de pesos w que clasifique correctamente la mayoría de los valores, es decir, que resulte en el menor **error**. Este error E se define por el **criterio del perceptrón** de la siguiente manera:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

donde:

* la suma se toma sobre aquellos puntos de datos de entrenamiento i que resultan en una clasificación incorrecta
* x<sub>i</sub> es el dato de entrada, y t<sub>i</sub> es ya sea -1 o +1 para ejemplos negativos y positivos respectivamente.

Este criterio se considera como una función de los pesos w, y necesitamos minimizarlo. A menudo, se utiliza un método llamado **descenso de gradiente**, en el que comenzamos con algunos pesos iniciales w<sup>(0)</sup>, y luego en cada paso actualizamos los pesos de acuerdo con la fórmula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Aquí η es la llamada **tasa de aprendizaje**, y ∇E(w) denota el **gradiente** de E. Después de calcular el gradiente, terminamos con

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

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

En esta lección, aprendiste sobre un perceptrón, que es un modelo de clasificación binaria, y cómo entrenarlo utilizando un vector de pesos.

## 🚀 Desafío

Si deseas intentar construir tu propio perceptrón, prueba [este laboratorio en Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) que utiliza el [diseñador de Azure ML](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Revisión y Autoestudio

Para ver cómo podemos utilizar el perceptrón para resolver un problema simple así como problemas de la vida real, y para continuar aprendiendo, dirígete al cuaderno [Perceptron](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb).

Aquí hay un [artículo interesante sobre perceptrones](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590) también.

## [Tarea](lab/README.md)

En esta lección, hemos implementado un perceptrón para la tarea de clasificación binaria, y lo hemos utilizado para clasificar entre dos dígitos manuscritos. En este laboratorio, se te pide resolver el problema de clasificación de dígitos por completo, es decir, determinar qué dígito es más probable que corresponda a una imagen dada.

* [Instrucciones](lab/README.md)
* [Cuaderno](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.