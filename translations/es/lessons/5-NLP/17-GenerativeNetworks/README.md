# Redes generativas

## [Cuestionario previo a la clase](https://ff-quizzes.netlify.app/en/ai/quiz/33)

Las Redes Neuronales Recurrentes (RNNs) y sus variantes con celdas de compuerta, como las Long Short Term Memory Cells (LSTMs) y las Gated Recurrent Units (GRUs), proporcionan un mecanismo para el modelado del lenguaje, ya que pueden aprender el orden de las palabras y ofrecer predicciones para la siguiente palabra en una secuencia. Esto nos permite usar RNNs para tareas **generativas**, como la generación de texto ordinario, la traducción automática e incluso la generación de descripciones de imágenes.

> ✅ Piensa en todas las veces que te has beneficiado de tareas generativas, como la autocompletación de texto mientras escribes. Investiga tus aplicaciones favoritas para ver si utilizan RNNs.

En la arquitectura de RNN que discutimos en la unidad anterior, cada unidad RNN producía el siguiente estado oculto como salida. Sin embargo, también podemos agregar otra salida a cada unidad recurrente, lo que nos permitiría generar una **secuencia** (que tiene la misma longitud que la secuencia original). Además, podemos usar unidades RNN que no aceptan una entrada en cada paso, sino que toman un vector de estado inicial y luego producen una secuencia de salidas.

Esto permite diferentes arquitecturas neuronales, como se muestra en la imagen a continuación:

![Imagen que muestra patrones comunes de redes neuronales recurrentes.](../../../../../translated_images/es/unreasonable-effectiveness-of-rnn.541ead816778f42d.webp)

> Imagen del blog [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) por [Andrej Karpaty](http://karpathy.github.io/)

* **Uno a uno** es una red neuronal tradicional con una entrada y una salida.
* **Uno a muchos** es una arquitectura generativa que acepta un valor de entrada y genera una secuencia de valores de salida. Por ejemplo, si queremos entrenar una red de **descripción de imágenes** que produzca una descripción textual de una imagen, podemos tomar una imagen como entrada, pasarla por una CNN para obtener su estado oculto y luego usar una cadena recurrente para generar la descripción palabra por palabra.
* **Muchos a uno** corresponde a las arquitecturas RNN que describimos en la unidad anterior, como la clasificación de texto.
* **Muchos a muchos**, o **secuencia a secuencia**, corresponde a tareas como la **traducción automática**, donde primero una RNN recopila toda la información de la secuencia de entrada en el estado oculto, y otra cadena RNN despliega este estado en la secuencia de salida.

En esta unidad, nos enfocaremos en modelos generativos simples que nos ayuden a generar texto. Para simplificar, utilizaremos tokenización a nivel de caracteres.

Entrenaremos esta RNN para generar texto paso a paso. En cada paso, tomaremos una secuencia de caracteres de longitud `nchars` y pediremos a la red que genere el siguiente carácter de salida para cada carácter de entrada:

![Imagen que muestra un ejemplo de generación de la palabra 'HELLO' con una RNN.](../../../../../translated_images/es/rnn-generate.56c54afb52f9781d.webp)

Cuando generamos texto (durante la inferencia), comenzamos con un **prompt**, que se pasa por las celdas RNN para generar su estado intermedio, y luego comienza la generación desde este estado. Generamos un carácter a la vez y pasamos el estado y el carácter generado a otra celda RNN para generar el siguiente, hasta que generemos suficientes caracteres.

<img src="../../../../../translated_images/es/rnn-generate-inf.5168dc65e0370eea.webp" width="60%"/>

> Imagen del autor

## ✍️ Ejercicios: Redes generativas

Continúa tu aprendizaje en los siguientes notebooks:

* [Redes generativas con PyTorch](GenerativePyTorch.ipynb)
* [Redes generativas con TensorFlow](GenerativeTF.ipynb)

## Generación de texto suave y temperatura

La salida de cada celda RNN es una distribución de probabilidad de caracteres. Si siempre tomamos el carácter con la mayor probabilidad como el siguiente carácter en el texto generado, el texto puede volverse "cíclico", repitiendo las mismas secuencias de caracteres una y otra vez, como en este ejemplo:

```
today of the second the company and a second the company ...
```

Sin embargo, si observamos la distribución de probabilidad para el siguiente carácter, podría ser que la diferencia entre las probabilidades más altas no sea muy grande, por ejemplo, un carácter puede tener una probabilidad de 0.2 y otro de 0.19, etc. Por ejemplo, al buscar el siguiente carácter en la secuencia '*play*', el siguiente carácter podría ser igualmente un espacio o **e** (como en la palabra *player*).

Esto nos lleva a la conclusión de que no siempre es "justo" seleccionar el carácter con mayor probabilidad, ya que elegir el segundo más alto aún podría llevarnos a un texto significativo. Es más sabio **muestrear** caracteres de la distribución de probabilidad dada por la salida de la red. También podemos usar un parámetro, **temperatura**, que suaviza la distribución de probabilidad si queremos agregar más aleatoriedad, o la hace más pronunciada si queremos ceñirnos más a los caracteres de mayor probabilidad.

Explora cómo se implementa esta generación de texto suave en los notebooks vinculados anteriormente.

## Conclusión

Aunque la generación de texto puede ser útil por sí misma, los mayores beneficios provienen de la capacidad de generar texto utilizando RNNs a partir de algún vector de características inicial. Por ejemplo, la generación de texto se utiliza como parte de la traducción automática (secuencia a secuencia, en este caso el vector de estado del *encoder* se utiliza para generar o *decodificar* el mensaje traducido), o para generar descripciones textuales de una imagen (en cuyo caso el vector de características provendría de un extractor CNN).

## 🚀 Desafío

Toma algunas lecciones en Microsoft Learn sobre este tema:

* Generación de texto con [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Cuestionario posterior a la clase](https://ff-quizzes.netlify.app/en/ai/quiz/34)

## Revisión y autoestudio

Aquí tienes algunos artículos para ampliar tu conocimiento:

* Diferentes enfoques para la generación de texto con Markov Chain, LSTM y GPT-2: [blog post](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Ejemplo de generación de texto en la [documentación de Keras](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Asignación](lab/README.md)

Hemos visto cómo generar texto carácter por carácter. En el laboratorio, explorarás la generación de texto a nivel de palabras.

---

