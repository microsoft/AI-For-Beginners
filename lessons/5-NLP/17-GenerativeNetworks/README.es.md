# Redes generativas

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/117)

Las redes neuronales recurrentes (RNN) y sus variantes de células cerradas, como las células de memoria a corto plazo (LSTM) y las unidades recurrentes cerradas (GRU), proporcionaron un mecanismo para el modelado del lenguaje en el sentido de que pueden aprender el orden de las palabras y proporcionar predicciones para la siguiente palabra en un secuencia. Esto nos permite utilizar RNN para **tareas generativas**, como la generación de texto normal, la traducción automática e incluso los subtítulos de imágenes.

> ✅ Piensa en todas las veces que te has beneficiado de tareas generativas como completar texto mientras escribes. Investigue un poco sobre sus aplicaciones favoritas para ver si aprovecharon los RNN.

En la arquitectura RNN que analizamos en la unidad anterior, cada unidad RNN produjo el siguiente estado oculto como salida. Sin embargo, también podemos agregar otra salida a cada unidad recurrente, lo que nos permitiría generar una **secuencia** (que tiene la misma longitud que la secuencia original). Además, podemos usar unidades RNN que no aceptan una entrada en cada paso, y simplemente toman algún vector de estado inicial y luego producen una secuencia de salidas.

Esto permite diferentes arquitecturas neuronales que se muestran en la siguiente imagen:

![Image showing common recurrent neural network patterns.](images/unreasonable-effectiveness-of-rnn.jpg)

> Imagen de la publicación del blog [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) by [Andrej Karpaty](http://karpathy.github.io/)
>
> * **Uno a uno** es una red neuronal tradicional con una entrada y una salida
* **Uno a muchos** es una arquitectura generativa que acepta un valor de entrada y genera una secuencia de valores de salida. Por ejemplo, si queremos entrenar una red de **subtítulos de imágenes** que produzca una descripción textual de una imagen, podemos usar una imagen como entrada, pasarla a través de una CNN para obtener su estado oculto y luego tener una cadena recurrente. generar subtítulos palabra por palabra
* **Muchos a uno** corresponde a las arquitecturas RNN que describimos en la unidad anterior, como la clasificación de texto.
* **Muchos a muchos**, o **secuencia a secuencia** corresponde a tareas como **traducción automática**, donde primero hacemos que RNN recopile toda la información de la secuencia de entrada al estado oculto. y otra cadena RNN desenrolla este estado en la secuencia de salida.

En esta unidad, nos centraremos en modelos generativos simples que nos ayudan a generar texto. Para simplificar, utilizaremos la tokenización a nivel de personaje.

Entrenaremos a este RNN para generar texto paso a paso. En cada paso, tomaremos una secuencia de caracteres de longitud `nchars` y le pediremos a la red que genere el siguiente carácter de salida para cada carácter de entrada:

![Image showing an example RNN generation of the word 'HELLO'.](images/rnn-generate.png)

Al generar texto (durante la inferencia), comenzamos con algún **mensaje**, que se pasa a través de las celdas RNN para generar su estado intermedio, y luego desde este estado comienza la generación. Generamos un carácter a la vez y pasamos el estado y el carácter generado a otra celda RNN para generar la siguiente, hasta que generemos suficientes caracteres.

<img src="images/rnn-generate-inf.png" width="60%"/>

> Image by the author

## ✍️ Ejercicios: Redes Generativas

Continúa tu aprendizaje en los siguientes cuadernos:

* [Generative Networks with PyTorch](GenerativePyTorch.ipynb)
* [Generative Networks with TensorFlow](GenerativeTF.ipynb)

## Generación de texto suave y temperatura

La salida de cada celda RNN es una distribución de probabilidad de caracteres. Si siempre tomamos el carácter con mayor probabilidad como el siguiente carácter en el texto generado, el texto a menudo puede "ciclarse" entre las mismas secuencias de caracteres una y otra vez, como en este ejemplo:

```
hoy del segundo la empresa y un segundo la empresa…
```

Sin embargo, si observamos la distribución de probabilidad del siguiente carácter, podría ser que la diferencia entre algunas probabilidades más altas no sea enorme, p. un carácter puede tener una probabilidad de 0,2, otro - 0,19, etc. Por ejemplo, cuando se busca el siguiente carácter en la secuencia '*play*', el siguiente carácter puede ser igualmente un espacio o **e** (como en el palabra *jugador*).

Esto nos lleva a la conclusión de que no siempre es "justo" seleccionar el personaje con mayor probabilidad, porque elegir el segundo más alto aún podría llevarnos a un texto significativo. Es más prudente **muestrear** caracteres de la distribución de probabilidad proporcionada por la salida de la red. También podemos usar un parámetro, **temperatura**, que aplanará la distribución de probabilidad, en caso de que queramos agregar más aleatoriedad, o hacerla más pronunciada, si queremos ceñirnos más a los caracteres de mayor probabilidad.

Explore cómo se implementa esta generación de texto suave en los cuadernos vinculados anteriormente.

## Conclusión

Si bien la generación de texto puede ser útil por sí sola, los principales beneficios provienen de la capacidad de generar texto utilizando RNN a partir de algún vector de características inicial. Por ejemplo, la generación de texto se utiliza como parte de la traducción automática (secuencia a secuencia, en este caso el vector de estado del *codificador* se utiliza para generar o *decodificar* el mensaje traducido), o generar una descripción textual de una imagen (en la que caso, el vector de características provendría del extractor de CNN).

## 🚀 Desafío

Tome algunas lecciones en Microsoft Learn sobre este tema

* Generación de texto con [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/217)

## Revisión y autoestudio

Aquí te dejamos algunos artículos para ampliar tus conocimientos.

* Diferentes enfoques para la generación de texto con Markov Chain, LSTM y GPT-2: [blog post](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Text generation sample in [Keras documentation](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Assignment](lab/README.md)

Hemos visto cómo generar texto carácter por carácter. En la práctica de laboratorio, explorará la generación de texto a nivel de palabra.
