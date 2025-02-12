# Redes generativas

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/117)

Las Redes Neuronales Recurrentes (RNNs) y sus variantes con puertas, como las Celdas de Memoria a Largo y Corto Plazo (LSTMs) y las Unidades Recurrentes con Puertas (GRUs), proporcionaron un mecanismo para el modelado del lenguaje en el que pueden aprender el orden de las palabras y ofrecer predicciones para la siguiente palabra en una secuencia. Esto nos permite usar RNNs para **tareas generativas**, como la generación de texto ordinario, la traducción automática e incluso la creación de descripciones para imágenes.

> ✅ Piensa en todas las ocasiones en que te has beneficiado de tareas generativas, como la finalización de texto mientras escribes. Investiga tus aplicaciones favoritas para ver si aprovecharon RNNs.

En la arquitectura de RNN que discutimos en la unidad anterior, cada unidad RNN producía el siguiente estado oculto como salida. Sin embargo, también podemos añadir otra salida a cada unidad recurrente, lo que nos permitiría generar una **secuencia** (que es igual en longitud a la secuencia original). Además, podemos utilizar unidades RNN que no aceptan una entrada en cada paso, y simplemente toman un vector de estado inicial y luego producen una secuencia de salidas.

Esto permite diferentes arquitecturas neuronales que se muestran en la imagen a continuación:

![Imagen que muestra patrones comunes de redes neuronales recurrentes.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.es.jpg)

> Imagen del artículo del blog [La Efectividad Irrazonable de las Redes Neuronales Recurrentes](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) de [Andrej Karpaty](http://karpathy.github.io/)

* **Uno a uno** es una red neuronal tradicional con una entrada y una salida.
* **Uno a muchos** es una arquitectura generativa que acepta un valor de entrada y genera una secuencia de valores de salida. Por ejemplo, si queremos entrenar una red de **creación de descripciones de imágenes** que produzca una descripción textual de una imagen, podemos tomar una imagen como entrada, pasarla a través de una CNN para obtener su estado oculto y luego tener una cadena recurrente que genere la descripción palabra por palabra.
* **Muchos a uno** corresponde a las arquitecturas RNN que describimos en la unidad anterior, como la clasificación de texto.
* **Muchos a muchos**, o **secuencia a secuencia**, corresponde a tareas como **traducción automática**, donde primero una RNN recopila toda la información de la secuencia de entrada en el estado oculto, y otra cadena RNN despliega este estado en la secuencia de salida.

En esta unidad, nos enfocaremos en modelos generativos simples que nos ayuden a generar texto. Para simplificar, utilizaremos la tokenización a nivel de caracteres.

Entrenaremos esta RNN para generar texto paso a paso. En cada paso, tomaremos una secuencia de caracteres de longitud `nchars` y le pediremos a la red que genere el siguiente carácter de salida para cada carácter de entrada:

![Imagen que muestra un ejemplo de generación RNN de la palabra 'HELLO'.](../../../../../translated_images/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.es.png)

Al generar texto (durante la inferencia), comenzamos con un **mensaje inicial**, que se pasa a través de las celdas RNN para generar su estado intermedio, y luego desde este estado comienza la generación. Generamos un carácter a la vez y pasamos el estado y el carácter generado a otra celda RNN para generar el siguiente, hasta que generamos suficientes caracteres.

<img src="images/rnn-generate-inf.png" width="60%"/>

> Imagen del autor

## ✍️ Ejercicios: Redes Generativas

Continúa tu aprendizaje en los siguientes cuadernos:

* [Redes Generativas con PyTorch](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb)
* [Redes Generativas con TensorFlow](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)

## Generación de texto suave y temperatura

La salida de cada celda RNN es una distribución de probabilidad de caracteres. Si siempre tomamos el carácter con la mayor probabilidad como el siguiente carácter en el texto generado, el texto a menudo puede "ciclarse" entre las mismas secuencias de caracteres una y otra vez, como en este ejemplo:

```
today of the second the company and a second the company ...
```

Sin embargo, si observamos la distribución de probabilidad para el siguiente carácter, podría ser que la diferencia entre algunas de las probabilidades más altas no sea enorme; por ejemplo, un carácter puede tener una probabilidad de 0.2, otro - 0.19, etc. Por ejemplo, al buscar el siguiente carácter en la secuencia '*play*', el siguiente carácter puede ser igualmente un espacio o **e** (como en la palabra *player*).

Esto nos lleva a la conclusión de que no siempre es "justo" seleccionar el carácter con una mayor probabilidad, porque elegir el segundo más alto aún podría llevarnos a un texto significativo. Es más sabio **muestrear** caracteres de la distribución de probabilidad dada por la salida de la red. También podemos usar un parámetro, **temperatura**, que aplanará la distribución de probabilidad en caso de que queramos agregar más aleatoriedad, o la hará más pronunciada si queremos ceñirnos más a los caracteres de mayor probabilidad.

Explora cómo se implementa esta generación de texto suave en los cuadernos vinculados arriba.

## Conclusión

Si bien la generación de texto puede ser útil por derecho propio, los principales beneficios provienen de la capacidad de generar texto utilizando RNNs a partir de algún vector de características inicial. Por ejemplo, la generación de texto se utiliza como parte de la traducción automática (secuencia a secuencia, en este caso el vector de estado del *codificador* se utiliza para generar o *decodificar* el mensaje traducido), o para generar descripciones textuales de una imagen (en cuyo caso el vector de características provendría de un extractor CNN).

## 🚀 Desafío

Toma algunas lecciones en Microsoft Learn sobre este tema

* Generación de Texto con [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/217)

## Revisión y Autoestudio

Aquí hay algunos artículos para ampliar tu conocimiento

* Diferentes enfoques para la generación de texto con Cadenas de Markov, LSTM y GPT-2: [artículo del blog](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Ejemplo de generación de texto en [documentación de Keras](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Asignación](lab/README.md)

Hemos visto cómo generar texto carácter por carácter. En el laboratorio, explorarás la generación de texto a nivel de palabras.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.