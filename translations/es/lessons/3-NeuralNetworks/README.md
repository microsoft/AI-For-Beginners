# Introducción a las Redes Neuronales

![Resumen del contenido de Introducción a Redes Neuronales en un garabato](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.es.png)

Como discutimos en la introducción, una de las formas de lograr inteligencia es entrenar un **modelo de computadora** o un **cerebro artificial**. Desde mediados del siglo XX, los investigadores han probado diferentes modelos matemáticos, hasta que en los últimos años esta dirección ha demostrado ser enormemente exitosa. Tales modelos matemáticos del cerebro se llaman **redes neuronales**.

> A veces, las redes neuronales se denominan *Redes Neuronales Artificiales*, ANNs, para indicar que estamos hablando de modelos, no de redes reales de neuronas.

## Aprendizaje Automático

Las Redes Neuronales son parte de una disciplina más amplia llamada **Aprendizaje Automático**, cuyo objetivo es utilizar datos para entrenar modelos de computadora que sean capaces de resolver problemas. El Aprendizaje Automático constituye una gran parte de la Inteligencia Artificial; sin embargo, no cubrimos el aprendizaje automático clásico en este currículo.

> Visita nuestro currículo separado **[Aprendizaje Automático para Principiantes](http://github.com/microsoft/ml-for-beginners)** para aprender más sobre el aprendizaje automático clásico.

En el Aprendizaje Automático, asumimos que tenemos un conjunto de datos de ejemplos **X**, y valores de salida correspondientes **Y**. Los ejemplos son a menudo vectores N-dimensionales que consisten en **características**, y las salidas se llaman **etiquetas**.

Consideraremos los dos problemas más comunes en el aprendizaje automático:

* **Clasificación**, donde necesitamos clasificar un objeto de entrada en dos o más clases.
* **Regresión**, donde necesitamos predecir un número numérico para cada una de las muestras de entrada.

> Al representar entradas y salidas como tensores, el conjunto de datos de entrada es una matriz de tamaño M×N, donde M es el número de muestras y N es el número de características. Las etiquetas de salida Y son el vector de tamaño M.

En este currículo, nos enfocaremos únicamente en modelos de redes neuronales.

## Un Modelo de Neurona

Desde la biología sabemos que nuestro cerebro consiste en células neuronales, cada una de ellas teniendo múltiples "entradas" (axones) y una salida (dendrita). Los axones y dendritas pueden conducir señales eléctricas, y las conexiones entre axones y dendritas pueden exhibir diferentes grados de conductividad (controlados por neuromediadores).

![Modelo de una Neurona](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.es.jpg) | ![Modelo de una Neurona](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.es.png)
----|----
Neurona Real *([Imagen](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) de Wikipedia)* | Neurona Artificial *(Imagen del Autor)*

Así, el modelo matemático más simple de una neurona contiene varias entradas X<sub>1</sub>, ..., X<sub>N</sub> y una salida Y, y una serie de pesos W<sub>1</sub>, ..., W<sub>N</sub>. Una salida se calcula como:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

donde f es alguna **función de activación** no lineal.

> Los primeros modelos de neuronas fueron descritos en el artículo clásico [Un cálculo lógico de las ideas inmanentes en la actividad nerviosa](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) por Warren McCullock y Walter Pitts en 1943. Donald Hebb en su libro "[La Organización del Comportamiento: Una Teoría Neuropsicológica](https://books.google.com/books?id=VNetYrB8EBoC)" propuso la forma en que estas redes pueden ser entrenadas.

## En esta Sección

En esta sección aprenderemos sobre:
* [Perceptrón](03-Perceptron/README.md), uno de los primeros modelos de red neuronal para clasificación de dos clases
* [Redes multicapa](04-OwnFramework/README.md) con un cuaderno emparejado [cómo construir nuestro propio marco](../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)
* [Frameworks de Redes Neuronales](05-Frameworks/README.md), con estos cuadernos: [PyTorch](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) y [Keras/Tensorflow](../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)
* [Sobreajuste](../../../../lessons/3-NeuralNetworks/05-Frameworks)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por lograr la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No somos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.