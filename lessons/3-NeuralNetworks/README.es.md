# Introducción a las Redes Neuronales

![Summary of Intro Neural Networks content in a doodle]

Como comentamos en la introducción, una de las formas de lograr inteligencia es entrenar un **modelo de computadora** o un **cerebro artificial**. Desde mediados del siglo XX, los investigadores probaron diferentes modelos matemáticos, hasta que en los últimos años esta tendencia resultó tener un gran éxito. Estos modelos matemáticos del cerebro se denominan **redes neuronales**.

> A veces las redes neuronales se denominan *Redes Neuronales Artificiales*, RNA, para indicar que estamos hablando de modelos, no de redes reales de neuronas.

## Aprendizaje automático

Las redes neuronales son parte de una disciplina más amplia llamada **Aprendizaje automático**, cuyo objetivo es utilizar datos para entrenar modelos informáticos que sean capaces de resolver problemas. El aprendizaje automático constituye una gran parte de la inteligencia artificial; sin embargo, no cubrimos el aprendizaje automático clásico en este plan de estudios.
> Visite nuestro plan de estudios separado **[Aprendizaje automático para principiantes](http://github.com/microsoft/ml-for-beginners)** para obtener más información sobre el aprendizaje automático clásico.

En Machine Learning, asumimos que tenemos algún conjunto de datos de ejemplos **X** y los valores de salida correspondientes **Y**. Los ejemplos suelen ser vectores de N dimensiones que constan de **características** y las salidas se denominan **etiquetas**.

Consideraremos los dos problemas de aprendizaje automático más comunes:

* **Clasificación**, donde necesitamos clasificar un objeto de entrada en dos o más clases.
* **Regresión**, donde necesitamos predecir un número numérico para cada una de las muestras de entrada.

> Al representar entradas y salidas como tensores, el conjunto de datos de entrada es una matriz de tamaño M×N, donde M es el número de muestras y N es el número de características. Las etiquetas de salida Y es el vector de tamaño M.

En este plan de estudios, sólo nos centraremos en los modelos de redes neuronales.

## Un modelo de neurona
Por la biología sabemos que nuestro cerebro está formado por células neuronales, cada una de las cuales tiene múltiples "entradas" (axones) y una salida (dendritas). Los axones y las dendritas pueden conducir señales eléctricas, y las conexiones entre axones y dendritas pueden exhibir diferentes grados de conductividad (controladas por neuromediadores).

![Model of a Neuron](images/synapse-wikipedia.jpg) | ![Model of a Neuron](images/artneuron.png)
----|----
*([Image](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) from Wikipedia)* | Artificial Neuron *(Image by Author)*

Así, el modelo matemático más simple de una neurona contiene varias entradas X<sub>1</sub>, ..., X<sub>N</sub> y una salida Y, y una serie de pesos W<sub>1. </sub>, ..., W<sub>N</sub>. Una salida se calcula como:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

donde f es alguna **función de activación** no lineal.

> Los primeros modelos de neuronas se describieron en el artículo clásico [A logical calculus of the ideas immanent in nervous activity](http://www.springerlink.com/content/61446605110620kg/fulltext.pdf) de Warren McCullock y Walter Pitts en 1943. Donald Hebb en su libro "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" propuso la forma en que se pueden entrenar esas redes.

## En esta sección

En esta sección aprenderemos sobre:
* [Perceptron](03-Perceptron/README.md), uno de los primeros modelos de redes neuronales para la clasificación de dos clases
* [Multi-layered networks](04-OwnFramework/README.md) con un cuaderno emparejado [how to build our own framework](04-OwnFramework/OwnFramework.ipynb)
* [Neural Network Frameworks](05-Frameworks/README.md), con estos cuadernos: [PyTorch](05-Frameworks/IntroPyTorch.ipynb) y [Keras/Tensorflow](05-Frameworks/IntroKerasTF.ipynb)
* [Overfitting](05-Frameworks/Overfitting.md)
