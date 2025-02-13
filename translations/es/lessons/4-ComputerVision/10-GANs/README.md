# Redes Generativas Antagónicas

En la sección anterior, aprendimos sobre **modelos generativos**: modelos que pueden generar nuevas imágenes similares a las del conjunto de datos de entrenamiento. VAE fue un buen ejemplo de un modelo generativo.

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

Sin embargo, si intentamos generar algo realmente significativo, como una pintura en una resolución razonable, con VAE, veremos que el entrenamiento no converge bien. Para este caso de uso, debemos aprender sobre otra arquitectura específicamente diseñada para modelos generativos: **Redes Generativas Antagónicas**, o GANs.

La idea principal de una GAN es tener dos redes neuronales que se entrenan entre sí:

<img src="images/gan_architecture.png" width="70%"/>

> Imagen de [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Un poco de vocabulario:
> * **Generador** es una red que toma un vector aleatorio y produce la imagen como resultado.
> * **Discriminador** es una red que toma una imagen y debe decir si es una imagen real (del conjunto de datos de entrenamiento) o fue generada por un generador. Es esencialmente un clasificador de imágenes.

### Discriminador

La arquitectura del discriminador no difiere de una red de clasificación de imágenes ordinaria. En el caso más simple, puede ser un clasificador totalmente conectado, pero lo más probable es que sea una [red convolucional](../07-ConvNets/README.md).

> ✅ Una GAN basada en redes convolucionales se llama [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

Un discriminador CNN consta de las siguientes capas: varias convoluciones + agrupamientos (con tamaño espacial decreciente) y, una o más capas totalmente conectadas para obtener el "vector de características", el clasificador binario final.

> ✅ Un 'agrupamiento' en este contexto es una técnica que reduce el tamaño de la imagen. "Las capas de agrupamiento reducen las dimensiones de los datos combinando las salidas de grupos de neuronas en una capa en una sola neurona en la siguiente capa." - [fuente](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generador

Un generador es un poco más complicado. Se puede considerar como un discriminador invertido. Comenzando desde un vector latente (en lugar de un vector de características), tiene una capa totalmente conectada para convertirlo en el tamaño/forma requeridos, seguida de deconvoluciones + aumento de escala. Esto es similar a la parte de *decodificador* de un [autoencoder](../09-Autoencoders/README.md).

> ✅ Dado que la capa de convolución se implementa como un filtro lineal que recorre la imagen, la deconvolución es esencialmente similar a la convolución y puede implementarse utilizando la misma lógica de capa.

<img src="images/gan_arch_detail.png" width="70%"/>

> Imagen de [Dmitry Soshnikov](http://soshnikov.com)

### Entrenando la GAN

Las GAN se llaman **antagónicas** porque hay una competencia constante entre el generador y el discriminador. Durante esta competencia, tanto el generador como el discriminador mejoran, por lo que la red aprende a producir imágenes cada vez mejores.

El entrenamiento ocurre en dos etapas:

* **Entrenando al discriminador**. Esta tarea es bastante directa: generamos un lote de imágenes con el generador, etiquetándolas como 0, que representa una imagen falsa, y tomamos un lote de imágenes del conjunto de datos de entrada (con etiqueta 1, imagen real). Obtenemos una *pérdida del discriminador* y realizamos retropropagación.
* **Entrenando al generador**. Esto es un poco más complicado, porque no conocemos la salida esperada para el generador directamente. Tomamos toda la red GAN compuesta por un generador seguido de un discriminador, le proporcionamos algunos vectores aleatorios y esperamos que el resultado sea 1 (correspondiente a imágenes reales). Luego congelamos los parámetros del discriminador (no queremos que se entrene en este paso) y realizamos la retropropagación.

Durante este proceso, las pérdidas tanto del generador como del discriminador no disminuyen significativamente. En la situación ideal, deberían oscilar, lo que corresponde a que ambas redes mejoran su rendimiento.

## ✍️ Ejercicios: GANs

* [Cuaderno GAN en TensorFlow/Keras](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [Cuaderno GAN en PyTorch](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### Problemas con el entrenamiento de GAN

Se sabe que las GAN son especialmente difíciles de entrenar. Aquí hay algunos problemas:

* **Colapso de modo**. Por este término nos referimos a que el generador aprende a producir una imagen exitosa que engaña al discriminador, y no una variedad de imágenes diferentes.
* **Sensibilidad a los hiperparámetros**. A menudo se puede ver que una GAN no converge en absoluto, y luego, de repente, disminuye en la tasa de aprendizaje, lo que lleva a la convergencia.
* Mantener un **equilibrio** entre el generador y el discriminador. En muchos casos, la pérdida del discriminador puede caer a cero relativamente rápido, lo que resulta en que el generador no puede entrenar más. Para superar esto, podemos intentar establecer diferentes tasas de aprendizaje para el generador y el discriminador, o saltar el entrenamiento del discriminador si la pérdida ya es demasiado baja.
* Entrenamiento para **alta resolución**. Reflejando el mismo problema que con los autoencoders, este problema se activa porque reconstruir demasiadas capas de una red convolucional conduce a artefactos. Este problema se resuelve típicamente con el llamado **crecimiento progresivo**, cuando primero se entrenan algunas capas en imágenes de baja resolución y luego se "desbloquean" o añaden capas. Otra solución sería agregar conexiones adicionales entre capas y entrenar varias resoluciones a la vez; consulte este [artículo sobre GANs de Gradiente Multi-escala](https://arxiv.org/abs/1903.06048) para más detalles.

## Transferencia de Estilo

Las GAN son una excelente manera de generar imágenes artísticas. Otra técnica interesante es la llamada **transferencia de estilo**, que toma una **imagen de contenido** y la vuelve a dibujar en un estilo diferente, aplicando filtros de la **imagen de estilo**.

La forma en que funciona es la siguiente:
* Comenzamos con una imagen de ruido aleatorio (o con una imagen de contenido, pero para fines de comprensión es más fácil comenzar desde ruido aleatorio).
* Nuestro objetivo sería crear una imagen que esté cerca tanto de la imagen de contenido como de la imagen de estilo. Esto se determinaría mediante dos funciones de pérdida:
   - **Pérdida de contenido** se calcula en función de las características extraídas por la CNN en algunas capas de la imagen actual y la imagen de contenido.
   - **Pérdida de estilo** se calcula entre la imagen actual y la imagen de estilo de una manera inteligente utilizando matrices de Gram (más detalles en el [cuaderno de ejemplo](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)).
* Para hacer la imagen más suave y eliminar el ruido, también introducimos **pérdida de variación**, que calcula la distancia promedio entre píxeles vecinos.
* El bucle de optimización principal ajusta la imagen actual utilizando descenso de gradiente (o algún otro algoritmo de optimización) para minimizar la pérdida total, que es una suma ponderada de las tres pérdidas.

## ✍️ Ejemplo: [Transferencia de Estilo](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## Conclusión

En esta lección, aprendiste sobre las GAN y cómo entrenarlas. También aprendiste sobre los desafíos especiales que este tipo de red neuronal puede enfrentar y algunas estrategias sobre cómo superarlos.

## 🚀 Desafío

Ejecuta el [cuaderno de Transferencia de Estilo](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) utilizando tus propias imágenes.

## Revisión y Autoestudio

Para referencia, lee más sobre las GAN en estos recursos:

* Marco Pasini, [10 Lecciones que Aprendí Entrenando GANs durante un Año](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), una arquitectura GAN *de facto* a considerar
* [Creando Arte Generativo usando GANs en Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Tarea

Revisita uno de los dos cuadernos asociados a esta lección y vuelve a entrenar la GAN con tus propias imágenes. ¿Qué puedes crear?

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.