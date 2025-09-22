<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b544f20b796402507fb05a0df893323",
  "translation_date": "2025-08-24T09:22:30+00:00",
  "source_file": "lessons/3-NeuralNetworks/05-Frameworks/README.md",
  "language_code": "es"
}
-->
# Frameworks de Redes Neuronales

Como ya hemos aprendido, para entrenar redes neuronales de manera eficiente necesitamos hacer dos cosas:

* Operar con tensores, por ejemplo, multiplicar, sumar y calcular funciones como sigmoid o softmax.
* Calcular gradientes de todas las expresiones, para realizar la optimización por descenso de gradiente.

## [Cuestionario previo a la clase](https://ff-quizzes.netlify.app/en/ai/quiz/9)

Aunque la biblioteca `numpy` puede realizar la primera parte, necesitamos algún mecanismo para calcular gradientes. En [nuestro framework](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) que desarrollamos en la sección anterior, tuvimos que programar manualmente todas las funciones derivadas dentro del método `backward`, que realiza la retropropagación. Idealmente, un framework debería permitirnos calcular los gradientes de *cualquier expresión* que podamos definir.

Otra cosa importante es poder realizar cálculos en GPU, o en otras unidades de cómputo especializadas, como [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). El entrenamiento de redes neuronales profundas requiere *muchos* cálculos, y poder paralelizar esos cálculos en GPUs es muy importante.

> ✅ El término 'paralelizar' significa distribuir los cálculos entre múltiples dispositivos.

Actualmente, los dos frameworks de redes neuronales más populares son: [TensorFlow](http://TensorFlow.org) y [PyTorch](https://pytorch.org/). Ambos proporcionan una API de bajo nivel para operar con tensores tanto en CPU como en GPU. Además de la API de bajo nivel, también existe una API de alto nivel, llamada [Keras](https://keras.io/) y [PyTorch Lightning](https://pytorchlightning.ai/) respectivamente.

API de bajo nivel | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
-------------------|-------------------------------------|--------------------------------
API de alto nivel  | [Keras](https://keras.io/)         | [PyTorch Lightning](https://pytorchlightning.ai/)

Las **APIs de bajo nivel** en ambos frameworks permiten construir los llamados **gráficos computacionales**. Este gráfico define cómo calcular el resultado (usualmente la función de pérdida) con los parámetros de entrada dados, y puede ser enviado para cálculo en GPU, si está disponible. Hay funciones para diferenciar este gráfico computacional y calcular gradientes, que luego pueden ser utilizados para optimizar los parámetros del modelo.

Las **APIs de alto nivel** consideran las redes neuronales como una **secuencia de capas**, y facilitan mucho la construcción de la mayoría de las redes neuronales. Entrenar el modelo generalmente requiere preparar los datos y luego llamar a una función `fit` para realizar el trabajo.

La API de alto nivel permite construir redes neuronales típicas muy rápidamente sin preocuparse por muchos detalles. Al mismo tiempo, la API de bajo nivel ofrece mucho más control sobre el proceso de entrenamiento, y por eso se utiliza mucho en investigación, cuando se trabaja con nuevas arquitecturas de redes neuronales.

También es importante entender que se pueden usar ambas APIs juntas. Por ejemplo, puedes desarrollar tu propia arquitectura de capa de red utilizando la API de bajo nivel, y luego usarla dentro de una red más grande construida y entrenada con la API de alto nivel. O puedes definir una red utilizando la API de alto nivel como una secuencia de capas, y luego usar tu propio bucle de entrenamiento de bajo nivel para realizar la optimización. Ambas APIs utilizan los mismos conceptos básicos subyacentes y están diseñadas para trabajar bien juntas.

## Aprendizaje

En este curso, ofrecemos la mayoría del contenido tanto para PyTorch como para TensorFlow. Puedes elegir tu framework preferido y solo revisar los notebooks correspondientes. Si no estás seguro de qué framework elegir, lee algunas discusiones en internet sobre **PyTorch vs. TensorFlow**. También puedes echar un vistazo a ambos frameworks para obtener una mejor comprensión.

Cuando sea posible, utilizaremos APIs de alto nivel por simplicidad. Sin embargo, creemos que es importante entender cómo funcionan las redes neuronales desde cero, por lo que al principio comenzamos trabajando con la API de bajo nivel y tensores. Sin embargo, si quieres avanzar rápidamente y no deseas dedicar mucho tiempo a aprender estos detalles, puedes omitirlos e ir directamente a los notebooks de la API de alto nivel.

## ✍️ Ejercicios: Frameworks

Continúa tu aprendizaje en los siguientes notebooks:

API de bajo nivel | [Notebook TensorFlow+Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [PyTorch](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)
-------------------|-------------------------------------|--------------------------------
API de alto nivel  | [Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb)          | *PyTorch Lightning*

Después de dominar los frameworks, repasemos el concepto de sobreajuste.

# Sobreajuste

El sobreajuste es un concepto extremadamente importante en el aprendizaje automático, ¡y es muy importante entenderlo correctamente!

Considera el siguiente problema de aproximar 5 puntos (representados por `x` en los gráficos a continuación):

![linear](../../../../../lessons/3-NeuralNetworks/images/overfit1.jpg) | ![overfit](../../../../../lessons/3-NeuralNetworks/images/overfit2.jpg)
-------------------------|--------------------------
**Modelo lineal, 2 parámetros** | **Modelo no lineal, 7 parámetros**
Error de entrenamiento = 5.3 | Error de entrenamiento = 0
Error de validación = 5.1 | Error de validación = 20

* A la izquierda, vemos una buena aproximación con una línea recta. Debido a que el número de parámetros es adecuado, el modelo entiende correctamente la distribución de los puntos.
* A la derecha, el modelo es demasiado poderoso. Debido a que solo tenemos 5 puntos y el modelo tiene 7 parámetros, puede ajustarse de tal manera que pase por todos los puntos, haciendo que el error de entrenamiento sea 0. Sin embargo, esto impide que el modelo entienda el patrón correcto detrás de los datos, por lo que el error de validación es muy alto.

Es muy importante encontrar un equilibrio correcto entre la riqueza del modelo (número de parámetros) y la cantidad de muestras de entrenamiento.

## Por qué ocurre el sobreajuste

  * No hay suficientes datos de entrenamiento.
  * El modelo es demasiado poderoso.
  * Hay demasiado ruido en los datos de entrada.

## Cómo detectar el sobreajuste

Como puedes ver en el gráfico anterior, el sobreajuste puede detectarse por un error de entrenamiento muy bajo y un error de validación alto. Normalmente, durante el entrenamiento veremos que tanto el error de entrenamiento como el de validación comienzan a disminuir, y luego en algún momento el error de validación podría dejar de disminuir y comenzar a aumentar. Esto será una señal de sobreajuste y un indicador de que probablemente deberíamos detener el entrenamiento en ese punto (o al menos hacer una captura del modelo).

![overfitting](../../../../../lessons/3-NeuralNetworks/images/Overfitting.png)

## Cómo prevenir el sobreajuste

Si detectas que ocurre sobreajuste, puedes hacer lo siguiente:

 * Aumentar la cantidad de datos de entrenamiento.
 * Disminuir la complejidad del modelo.
 * Usar alguna [técnica de regularización](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), como [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), que consideraremos más adelante.

## Sobreajuste y el equilibrio entre sesgo y varianza

El sobreajuste es en realidad un caso de un problema más general en estadística llamado [Equilibrio entre sesgo y varianza](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Si consideramos las posibles fuentes de error en nuestro modelo, podemos ver dos tipos de errores:

* **Errores de sesgo** son causados por nuestro algoritmo al no poder capturar correctamente la relación entre los datos de entrenamiento. Esto puede resultar del hecho de que nuestro modelo no es lo suficientemente poderoso (**subajuste**).
* **Errores de varianza**, que son causados por el modelo al aproximar el ruido en los datos de entrada en lugar de la relación significativa (**sobreajuste**).

Durante el entrenamiento, el error de sesgo disminuye (a medida que nuestro modelo aprende a aproximar los datos) y el error de varianza aumenta. Es importante detener el entrenamiento, ya sea manualmente (cuando detectamos sobreajuste) o automáticamente (introduciendo regularización), para prevenir el sobreajuste.

## Conclusión

En esta lección, aprendiste sobre las diferencias entre las diversas APIs de los dos frameworks de IA más populares, TensorFlow y PyTorch. Además, aprendiste sobre un tema muy importante: el sobreajuste.

## 🚀 Desafío

En los notebooks acompañantes, encontrarás 'tareas' al final; trabaja en los notebooks y completa las tareas.

## [Cuestionario posterior a la clase](https://ff-quizzes.netlify.app/en/ai/quiz/10)

## Revisión y autoestudio

Investiga sobre los siguientes temas:

- TensorFlow
- PyTorch
- Sobreajuste

Pregúntate lo siguiente:

- ¿Cuál es la diferencia entre TensorFlow y PyTorch?
- ¿Cuál es la diferencia entre sobreajuste y subajuste?

## [Asignación](lab/README.md)

En este laboratorio, se te pide resolver dos problemas de clasificación utilizando redes completamente conectadas de una y varias capas con PyTorch o TensorFlow.

* [Instrucciones](lab/README.md)
* [Notebook](../../../../../lessons/3-NeuralNetworks/05-Frameworks/lab/LabFrameworks.ipynb)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.