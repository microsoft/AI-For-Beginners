# Marcos de Redes Neuronales

Como ya hemos aprendido, para poder entrenar redes neuronales de manera eficiente necesitamos hacer dos cosas:

* Operar con tensores, es decir, multiplicar, sumar y calcular algunas funciones como sigmoid o softmax.
* Calcular gradientes de todas las expresiones, con el fin de realizar la optimización por descenso de gradiente.

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/105)

Mientras que la biblioteca `numpy` puede realizar la primera parte, necesitamos algún mecanismo para calcular gradientes. En [nuestro marco](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) que hemos desarrollado en la sección anterior, tuvimos que programar manualmente todas las funciones derivadas dentro del método `backward`, que realiza la retropropagación. Idealmente, un marco debería brindarnos la oportunidad de calcular gradientes de *cualquier expresión* que podamos definir.

Otra cosa importante es poder realizar cálculos en GPU, o en cualquier otra unidad de computación especializada, como [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). El entrenamiento de redes neuronales profundas requiere *muchos* cálculos, y poder paralelizar esos cálculos en GPUs es muy importante.

> ✅ El término 'paralelizar' significa distribuir los cálculos entre múltiples dispositivos.

Actualmente, los dos marcos neuronales más populares son: [TensorFlow](http://TensorFlow.org) y [PyTorch](https://pytorch.org/). Ambos proporcionan una API de bajo nivel para operar con tensores tanto en CPU como en GPU. Encima de la API de bajo nivel, también hay una API de alto nivel, llamada [Keras](https://keras.io/) y [PyTorch Lightning](https://pytorchlightning.ai/) respectivamente.

API de Bajo Nivel | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
------------------|-------------------------------------|--------------------------------
API de Alto Nivel  | [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**Las APIs de bajo nivel** en ambos marcos permiten construir lo que se llama **gráficas computacionales**. Esta gráfica define cómo calcular la salida (normalmente la función de pérdida) con los parámetros de entrada dados, y puede ser enviada para cálculo en GPU, si está disponible. Existen funciones para diferenciar esta gráfica computacional y calcular gradientes, que luego pueden ser utilizados para optimizar los parámetros del modelo.

**Las APIs de alto nivel** consideran las redes neuronales como una **secuencia de capas**, y facilitan la construcción de la mayoría de las redes neuronales. Entrenar el modelo generalmente requiere preparar los datos y luego llamar a una función `fit` para realizar el trabajo.

La API de alto nivel permite construir redes neuronales típicas muy rápidamente sin preocuparse por muchos detalles. Al mismo tiempo, la API de bajo nivel ofrece mucho más control sobre el proceso de entrenamiento, y por lo tanto se utiliza mucho en investigación, cuando se trabaja con nuevas arquitecturas de redes neuronales.

También es importante entender que puedes usar ambas APIs juntas, es decir, puedes desarrollar tu propia arquitectura de capa de red utilizando la API de bajo nivel, y luego usarla dentro de la red más grande construida y entrenada con la API de alto nivel. O puedes definir una red usando la API de alto nivel como una secuencia de capas, y luego usar tu propio bucle de entrenamiento de bajo nivel para realizar la optimización. Ambas APIs utilizan los mismos conceptos básicos subyacentes y están diseñadas para funcionar bien juntas.

## Aprendizaje

En este curso, ofrecemos la mayor parte del contenido tanto para PyTorch como para TensorFlow. Puedes elegir tu marco preferido y solo pasar por los cuadernos correspondientes. Si no estás seguro de qué marco elegir, lee algunas discusiones en internet sobre **PyTorch vs. TensorFlow**. También puedes echar un vistazo a ambos marcos para obtener una mejor comprensión.

Donde sea posible, utilizaremos APIs de alto nivel por simplicidad. Sin embargo, creemos que es importante entender cómo funcionan las redes neuronales desde cero, por lo que al principio comenzamos trabajando con la API de bajo nivel y tensores. Sin embargo, si deseas avanzar rápidamente y no quieres pasar mucho tiempo aprendiendo estos detalles, puedes saltarte eso e ir directamente a los cuadernos de la API de alto nivel.

## ✍️ Ejercicios: Marcos

Continúa tu aprendizaje en los siguientes cuadernos:

API de Bajo Nivel | [Cuaderno TensorFlow+Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [PyTorch](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)
------------------|-------------------------------------|--------------------------------
API de Alto Nivel  | [Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) | *PyTorch Lightning*

Después de dominar los marcos, recapitularemos la noción de sobreajuste.

# Sobreajuste

El sobreajuste es un concepto extremadamente importante en el aprendizaje automático, ¡y es muy importante entenderlo correctamente!

Considera el siguiente problema de aproximar 5 puntos (representados por `x` en los gráficos a continuación):

![linear](../../../../../translated_images/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.es.jpg) | ![overfit](../../../../../translated_images/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.es.jpg)
-------------------------|--------------------------
**Modelo lineal, 2 parámetros** | **Modelo no lineal, 7 parámetros**
Error de entrenamiento = 5.3 | Error de entrenamiento = 0
Error de validación = 5.1 | Error de validación = 20

* A la izquierda, vemos una buena aproximación de línea recta. Debido a que el número de parámetros es adecuado, el modelo capta la idea detrás de la distribución de puntos correctamente.
* A la derecha, el modelo es demasiado potente. Dado que solo tenemos 5 puntos y el modelo tiene 7 parámetros, puede ajustarse de tal manera que pase por todos los puntos, haciendo que el error de entrenamiento sea 0. Sin embargo, esto impide que el modelo entienda el patrón correcto detrás de los datos, por lo que el error de validación es muy alto.

Es muy importante encontrar un equilibrio correcto entre la riqueza del modelo (número de parámetros) y la cantidad de muestras de entrenamiento.

## Por qué ocurre el sobreajuste

  * No hay suficientes datos de entrenamiento.
  * Modelo demasiado potente.
  * Demasiado ruido en los datos de entrada.

## Cómo detectar el sobreajuste

Como puedes ver en el gráfico anterior, el sobreajuste se puede detectar por un error de entrenamiento muy bajo y un error de validación alto. Normalmente, durante el entrenamiento, veremos que tanto el error de entrenamiento como el de validación comienzan a disminuir, y luego en algún momento el error de validación puede dejar de disminuir y comenzar a aumentar. Esto será una señal de sobreajuste y un indicador de que probablemente deberíamos detener el entrenamiento en este punto (o al menos hacer una instantánea del modelo).

![overfitting](../../../../../translated_images/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.es.png)

## Cómo prevenir el sobreajuste

Si puedes ver que ocurre el sobreajuste, puedes hacer una de las siguientes acciones:

 * Aumentar la cantidad de datos de entrenamiento.
 * Disminuir la complejidad del modelo.
 * Utilizar alguna [técnica de regularización](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), como [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), que consideraremos más adelante.

## Sobreajuste y el Compromiso Bias-Varianza

El sobreajuste es en realidad un caso de un problema más genérico en estadística llamado [Compromiso Bias-Varianza](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Si consideramos las posibles fuentes de error en nuestro modelo, podemos ver dos tipos de errores:

* **Errores de sesgo** son causados por el hecho de que nuestro algoritmo no puede capturar correctamente la relación entre los datos de entrenamiento. Puede resultar del hecho de que nuestro modelo no es lo suficientemente potente (**subajuste**).
* **Errores de varianza**, que son causados por el modelo que aproxima el ruido en los datos de entrada en lugar de una relación significativa (**sobreajuste**).

Durante el entrenamiento, el error de sesgo disminuye (a medida que nuestro modelo aprende a aproximar los datos), y el error de varianza aumenta. Es importante detener el entrenamiento - ya sea manualmente (cuando detectamos sobreajuste) o automáticamente (introduciendo regularización) - para prevenir el sobreajuste.

## Conclusión

En esta lección, aprendiste sobre las diferencias entre las diversas APIs para los dos marcos de IA más populares, TensorFlow y PyTorch. Además, aprendiste sobre un tema muy importante, el sobreajuste.

## 🚀 Desafío

En los cuadernos acompañantes, encontrarás 'tareas' al final; trabaja a través de los cuadernos y completa las tareas.

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/205)

## Revisión y Autoestudio

Realiza una investigación sobre los siguientes temas:

- TensorFlow
- PyTorch
- Sobreajuste

Pregúntate las siguientes cuestiones:

- ¿Cuál es la diferencia entre TensorFlow y PyTorch?
- ¿Cuál es la diferencia entre sobreajuste y subajuste?

## [Asignación](lab/README.md)

En este laboratorio, se te pide resolver dos problemas de clasificación utilizando redes completamente conectadas de una y múltiples capas usando PyTorch o TensorFlow.

* [Instrucciones](lab/README.md)
* [Cuaderno](../../../../../lessons/3-NeuralNetworks/05-Frameworks/lab/LabFrameworks.ipynb)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.