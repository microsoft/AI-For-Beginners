# Redes Generativas Antagónicas

En la sección anterior, aprendimos sobre **modelos generativos**: modelos que pueden generar nuevas imágenes similares a las que están en el conjunto de datos de entrenamiento. VAE fue un buen ejemplo de un modelo generativo.

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

Sin embargo, si intentamos generar algo realmente significativo, como una pintura a una resolución razonable, con VAE, veremos que el entrenamiento no converge bien. Para este caso de uso, debemos aprender sobre otra arquitectura específicamente dirigida a modelos generativos: **Redes Generativas Antagónicas**, o GANs.

La idea principal de una GAN es tener dos redes neuronales que se entrenarán entre sí:

<img src="images/gan_architecture.png" width="70%"/>

> Imagen de [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Un poco de vocabulario:
> * **Generador** es una red que toma un vector aleatorio y produce la imagen como resultado.
> * **Discriminador** es una red que toma una imagen y debe determinar si es una imagen real (del conjunto de datos de entrenamiento) o si fue generada por un generador. Es esencialmente un clasificador de imágenes.

### Discriminador

La arquitectura del discriminador no difiere de una red de clasificación de imágenes ordinaria. En el caso más simple, puede ser un clasificador totalmente conectado, pero lo más probable es que sea una [red convolucional](../07-ConvNets/README.md).

> ✅ Una GAN basada en redes convolucionales se llama [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

Un discriminador CNN consta de las siguientes capas: varias convoluciones+poolings (con tamaño espacial decreciente) y, una o más capas totalmente conectadas para obtener un "vector de características", el clasificador binario final.

> ✅ Un 'pooling' en este contexto es una técnica que reduce el tamaño de la imagen. "Las capas de pooling reducen las dimensiones de los datos combinando las salidas de grupos de neuronas en una capa en una sola neurona en la siguiente capa." - [fuente](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generador

Un generador es un poco más complicado. Se puede considerar como un discriminador invertido. Comenzando desde un vector latente (en lugar de un vector de características), tiene una capa totalmente conectada para convertirlo en el tamaño/forma requerida, seguida de deconvoluciones+escalado. Esto es similar a la parte *decodificadora* de un [autoencoder](../09-Autoencoders/README.md).

> ✅ Dado que la capa de convolución se implementa como un filtro lineal que recorre la imagen, la deconvolución es esencialmente similar a la convolución y se puede implementar utilizando la misma lógica de capa.

<img src="images/gan_arch_detail.png" width="70%"/>

> Imagen de [Dmitry Soshnikov](http://soshnikov.com)

### Entrenando la GAN

Las GANs se llaman **antagónicas** porque hay una competencia constante entre el generador y el discriminador. Durante esta competencia, tanto el generador como el discriminador mejoran, por lo que la red aprende a producir imágenes cada vez mejores.

El entrenamiento ocurre en dos etapas:

* **Entrenamiento del discriminador**. Esta tarea es bastante directa: generamos un lote de imágenes por el generador, etiquetándolas como 0, que representa una imagen falsa, y tomamos un lote de imágenes del conjunto de datos de entrada (con etiqueta 1, imagen real). Obtenemos alguna *pérdida del discriminador* y realizamos retropropagación.
* **Entrenamiento del generador**. Esto es un poco más complicado, porque no conocemos la salida esperada para el generador directamente. Tomamos toda la red GAN que consiste en un generador seguido de un discriminador, le proporcionamos algunos vectores aleatorios y esperamos que el resultado sea 1 (correspondiente a imágenes reales). Luego congelamos los parámetros del discriminador (no queremos que se entrene en este paso) y realizamos la retropropagación.

Durante este proceso, tanto las pérdidas del generador como las del discriminador no disminuyen significativamente. En la situación ideal, deberían oscilar, correspondiendo a ambas redes mejorando su rendimiento.

## ✍️ Ejercicios: GANs

* [Cuaderno de GAN en TensorFlow/Keras](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [Cuaderno de GAN en PyTorch](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### Problemas con el entrenamiento de GAN

Se sabe que las GANs son especialmente difíciles de entrenar. Aquí hay algunos problemas:

* **Colapso de modo**. Con este término nos referimos a que el generador aprende a producir una imagen exitosa que engaña al discriminador, y no una variedad de imágenes diferentes.
* **Sensibilidad a los hiperparámetros**. A menudo se puede observar que una GAN no converge en absoluto, y luego de repente disminuye en la tasa de aprendizaje, lo que lleva a la convergencia.
* Mantener un **equilibrio** entre el generador y el discriminador. En muchos casos, la pérdida del discriminador puede caer a cero relativamente rápido, lo que resulta en que el generador no pueda entrenarse más. Para superar esto, podemos intentar establecer diferentes tasas de aprendizaje para el generador y el discriminador, o saltar el entrenamiento del discriminador si la pérdida ya es demasiado baja.
* Entrenamiento para **alta resolución**. Reflejando el mismo problema que con los autoencoders, este problema se desencadena porque reconstruir demasiadas capas de la red convolucional conduce a artefactos. Este problema se suele resolver con el llamado **crecimiento progresivo**, cuando primero se entrenan unas pocas capas en imágenes de baja resolución, y luego se "desbloquean" o añaden capas. Otra solución sería agregar conexiones adicionales entre capas y entrenar varias resoluciones a la vez: consulte este [artículo sobre Multi-Scale Gradient GANs](https://arxiv.org/abs/1903.06048) para más detalles.

## Transferencia de Estilo

Las GANs son una excelente manera de generar imágenes artísticas. Otra técnica interesante es la llamada **transferencia de estilo**, que toma una **imagen de contenido** y la redibuja en un estilo diferente, aplicando filtros de una **imagen de estilo**.

La forma en que funciona es la siguiente:
* Comenzamos con una imagen de ruido aleatorio (o con una imagen de contenido, pero para facilitar la comprensión es más fácil comenzar desde ruido aleatorio).
* Nuestro objetivo sería crear una imagen que esté cerca tanto de la imagen de contenido como de la imagen de estilo. Esto se determinaría mediante dos funciones de pérdida:
   - **Pérdida de contenido** se calcula en función de las características extraídas por la CNN en algunas capas de la imagen actual y la imagen de contenido.
   - **Pérdida de estilo** se calcula entre la imagen actual y la imagen de estilo de manera ingeniosa utilizando matrices de Gram (más detalles en el [cuaderno de ejemplo](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)).
* Para hacer que la imagen sea más suave y eliminar el ruido, también introducimos **pérdida de variación**, que calcula la distancia promedio entre píxeles vecinos.
* El bucle principal de optimización ajusta la imagen actual utilizando descenso de gradiente (o algún otro algoritmo de optimización) para minimizar la pérdida total, que es una suma ponderada de las tres pérdidas.

## ✍️ Ejemplo: [Transferencia de Estilo](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## Conclusión

En esta lección, aprendiste sobre las GANs y cómo entrenarlas. También aprendiste sobre los desafíos especiales que este tipo de red neuronal puede enfrentar, y algunas estrategias sobre cómo superarlos.

## 🚀 Desafío

Revisa el [cuaderno de Transferencia de Estilo](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) utilizando tus propias imágenes.

## Revisión y Autoestudio

Para referencia, lee más sobre las GANs en estos recursos:

* Marco Pasini, [10 Lecciones que Aprendí Entrenando GANs durante un Año](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), una arquitectura GAN *de facto* a considerar.
* [Creando Arte Generativo usando GANs en Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Asignación

Revisa uno de los dos cuadernos asociados a esta lección y vuelve a entrenar la GAN con tus propias imágenes. ¿Qué puedes crear?

**Disclaimer**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional por parte de un humano. No somos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.