# Marcos de redes neuronales

Como ya hemos aprendido, para poder entrenar redes neuronales de manera eficiente necesitamos hacer dos cosas:

* Para operar con tensores, por ej. para multiplicar, sumar y calcular algunas funciones como sigmoide o softmax
* Para calcular los gradientes de todas las expresiones, para realizar la optimización del descenso de gradientes.

  ## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/105)

Si bien la biblioteca `numpy` puede hacer la primera parte, necesitamos algún mecanismo para calcular los gradientes. En [our framework](../04-OwnFramework/OwnFramework.ipynb) que hemos desarrollado en la sección anterior, tuvimos que programar manualmente todas las funciones derivadas dentro del método "hacia atrás", que realiza retropropagación. Idealmente, un marco debería darnos la oportunidad de calcular gradientes de *cualquier expresión* que podamos definir.

Otra cosa importante es poder realizar cálculos en GPU o cualquier otra unidad de cálculo especializada, como [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit).El entrenamiento de redes neuronales profundas requiere *muchos* cálculos, y poder paralelizar esos cálculos en las GPU es muy importante.

> ✅ El término 'paralelizar' significa distribuir los cálculos en múltiples dispositivos.

Actualmente, los dos marcos neuronales más populares son: [TensorFlow](http://TensorFlow.org) y [PyTorch](https://pytorch.org/). Ambos proporcionan una API de bajo nivel para operar con tensores tanto en CPU como en GPU. Además de la API de bajo nivel, también existe una API de nivel superior, llamada [Keras](https://keras.io/) y [PyTorch Lightning](https://pytorchlightning.ai/) correspondientemente.

API de bajo nivel | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
--------------|-------------------------------------|--------------------------------
API de alto nivel| [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

Las **API de bajo nivel** en ambos marcos le permiten crear los llamados **gráficos computacionales**. Este gráfico define cómo calcular la salida (normalmente la función de pérdida) con parámetros de entrada determinados y se puede enviar para su cálculo en la GPU, si está disponible. Hay funciones para diferenciar este gráfico computacional y calcular gradientes, que luego se pueden usar para optimizar los parámetros del modelo.

Las **API de alto nivel** consideran las redes neuronales como una **secuencia de capas** y facilitan mucho la construcción de la mayoría de las redes neuronales. Entrenar el modelo generalmente requiere preparar los datos y luego llamar a una función "adecuada" para hacer el trabajo.

La API de alto nivel le permite construir redes neuronales típicas muy rápidamente sin preocuparse por muchos detalles. Al mismo tiempo, las API de bajo nivel ofrecen mucho más control sobre el proceso de entrenamiento y, por lo tanto, se utilizan mucho en la investigación cuando se trata de nuevas arquitecturas de redes neuronales.

También es importante comprender que puede utilizar ambas API juntas, por ejemplo. puede desarrollar su propia arquitectura de capa de red utilizando API de bajo nivel y luego usarla dentro de la red más grande construida y entrenada con API de alto nivel. O puede definir una red utilizando la API de alto nivel como una secuencia de capas y luego usar su propio bucle de entrenamiento de bajo nivel para realizar la optimización. Ambas API utilizan los mismos conceptos básicos subyacentes y están diseñadas para funcionar bien juntas.

## Aprendiendo

En este curso, ofrecemos la mayor parte del contenido tanto para PyTorch como para TensorFlow. Puedes elegir tu marco preferido y solo revisar los cuadernos correspondientes. Si no está seguro de qué marco elegir, lea algunas discusiones en Internet sobre **PyTorch vs. TensorFlow**. También puede echar un vistazo a ambos marcos para comprender mejor.

Siempre que sea posible, utilizaremos API de alto nivel para simplificar. Sin embargo, creemos que es importante comprender cómo funcionan las redes neuronales desde cero, por lo que al principio comenzamos trabajando con API y tensores de bajo nivel. Sin embargo, si desea comenzar rápidamente y no quiere perder mucho tiempo aprendiendo estos detalles, puede omitirlos e ir directamente a los cuadernos de API de alto nivel.

## ✍️ Ejercicios: Marcos

Continúa tu aprendizaje en los siguientes cuadernos:

API de bajo nivel | [TensorFlow+Keras Notebook](IntroKerasTF.ipynb) | [PyTorch](IntroPyTorch.ipynb)
--------------|-------------------------------------|--------------------------------
API de alto nivel| [Keras](IntroKeras.ipynb) | *PyTorch Lightning*

Después de dominar los marcos, recapitulemos la noción de sobreajuste.

# Sobreajuste

El sobreajuste es un concepto extremadamente importante en el aprendizaje automático y es muy importante hacerlo bien.

Considere el siguiente problema de aproximar 5 puntos (representado por "x" en los gráficos siguientes):

![linear](../images/overfit1.jpg) | ![overfit](../images/overfit2.jpg)
-------------------------|--------------------------
**Modelo lineal, 2 parámetros** | **Modelo no lineal, 7 parámetros**
Error de entrenamiento = 5,3 | Error de entrenamiento = 0
Error de validación = 5.1 | Error de validación = 20

* A la izquierda vemos una buena aproximación en línea recta. Debido a que el número de parámetros es adecuado, el modelo capta correctamente la idea detrás de la distribución de puntos.
* A la derecha, el modelo es demasiado poderoso. Debido a que solo tenemos 5 puntos y el modelo tiene 7 parámetros, se puede ajustar de tal manera que pase por todos los puntos, lo que hace que el error de entrenamiento sea 0. Sin embargo, esto impide que el modelo comprenda el patrón correcto detrás de los datos, por lo que el error de validación es muy alto.

Es muy importante lograr un equilibrio correcto entre la riqueza del modelo (número de parámetros) y el número de muestras de entrenamiento.

## ¿Por qué ocurre el sobreajuste?

   * No hay suficientes datos de entrenamiento
   * Modelo demasiado potente
   * Demasiado ruido en los datos de entrada

## Cómo detectar el sobreajuste

Como puede ver en el gráfico anterior, el sobreajuste se puede detectar mediante un error de entrenamiento muy bajo y un error de validación alto. Normalmente, durante el entrenamiento, veremos que tanto los errores de entrenamiento como los de validación comienzan a disminuir y luego, en algún momento, el error de validación puede dejar de disminuir y comenzar a aumentar. Esto será una señal de sobreajuste y el indicador de que probablemente deberíamos dejar de entrenar en este punto (o al menos tomar una instantánea del modelo).

![overfitting](../images/Overfitting.png)

## Cómo prevenir el sobreajuste

Si puede ver que se produce un sobreajuste, puede realizar una de las siguientes acciones:

  * Aumentar la cantidad de datos de entrenamiento.
  * Disminuir la complejidad del modelo.
  * Usa algo [regularization technique](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), como [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), lo que consideraremos más adelante.

## Compensación entre sobreajuste y sesgo-varianza

El sobreajuste es en realidad un caso de un problema más genérico en estadística llamado [Bias-Variance Tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Si consideramos las posibles fuentes de error en nuestro modelo, podemos ver dos tipos de errores:

* **Los errores de sesgo** se deben a que nuestro algoritmo no puede capturar correctamente la relación entre los datos de entrenamiento. Puede deberse al hecho de que nuestro modelo no es lo suficientemente potente (**underfitting**).
* **Errores de varianza**, que se deben a que el modelo aproxima el ruido en los datos de entrada en lugar de una relación significativa (**sobreajuste**).

Durante el entrenamiento, el error de sesgo disminuye (a medida que nuestro modelo aprende a aproximar los datos) y el error de varianza aumenta. Es importante detener el entrenamiento, ya sea manualmente (cuando detectamos un sobreajuste) o automáticamente (al introducir la regularización), para evitar el sobreajuste.

## Conclusión

En esta lección, aprendió sobre las diferencias entre las distintas API para los dos marcos de IA más populares, TensorFlow y PyTorch. Además, aprendiste sobre un tema muy importante, el sobreajuste.

## 🚀 Desafío

En los cuadernos adjuntos encontrará "tareas" en la parte inferior; Trabajar en los cuadernos y completar las tareas.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/205)

## Revisión y autoestudio

Investiga un poco sobre los siguientes temas:

- TensorFlow
-PyTorch
- Sobreajuste

Pregúntate a ti mismo las siguientes preguntas:

- ¿Cuál es la diferencia entre TensorFlow y PyTorch?
- ¿Cuál es la diferencia entre sobreajuste y desajuste?

  ## [Assignment](lab/README.md)

En esta práctica de laboratorio, se le pedirá que resuelva dos problemas de clasificación utilizando redes completamente conectadas de una o varias capas utilizando PyTorch o TensorFlow.

* [Instructions](lab/README.md)
* [Notebook](lab/LabFrameworks.ipynb)
