# Redes generativas de confrontación

En la sección anterior, aprendimos sobre los **modelos generativos**: modelos que pueden generar nuevas imágenes similares a las del conjunto de datos de entrenamiento. VAE fue un buen ejemplo de modelo generativo.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

Sin embargo, si intentamos generar algo realmente significativo, como una pintura con una resolución razonable, con VAE, veremos que el entrenamiento no converge bien. Para este caso de uso, deberíamos conocer otra arquitectura dirigida específicamente a modelos generativos: **Redes generativas adversas** o GAN.

La idea principal de una GAN es tener dos redes neuronales que se entrenarán entre sí:

<img src="images/gan_architecture.png" width="70%"/>

> Imagen de [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Un poco de vocabulario:
> * **Generador** es una red que toma algún vector aleatorio y produce la imagen como resultado
> * **Discriminator** es una red que toma una imagen y debe indicar si es una imagen real (del conjunto de datos de entrenamiento) o si fue generada por un generador. Es esencialmente un clasificador de imágenes.

### Discriminador

La arquitectura del discriminador no difiere de la de una red de clasificación de imágenes ordinaria. En el caso más simple, puede ser un clasificador completamente conectado, pero lo más probable es que sea una [red convolucional] (../07-ConvNets/README.md).

> ✅ Una GAN basada en redes convolucionales se llama [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

Un discriminador CNN consta de las siguientes capas: varias convoluciones + agrupaciones (con tamaño espacial decreciente) y una o más capas completamente conectadas para obtener el "vector de características", clasificador binario final.

> ✅ Un 'pooling' en este contexto es una técnica que reduce el tamaño de la imagen. "La agrupación de capas reduce las dimensiones de los datos al combinar las salidas de los grupos de neuronas en una capa en una sola neurona en la siguiente capa". - [fuente](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generador

Un generador es un poco más complicado. Puedes considerarlo como un discriminador inverso. A partir de un vector latente (en lugar de un vector de características), tiene una capa completamente conectada para convertirla al tamaño/forma requerido, seguida de deconvoluciones + ampliación de escala. Esto es similar a la parte *decodificador* de [autoencoder](../09-Autoencoders/README.md).

> ✅ Debido a que la capa de convolución se implementa como un filtro lineal que atraviesa la imagen, la deconvolución es esencialmente similar a la convolución y se puede implementar usando la misma lógica de capa.

<img src="images/gan_arch_detail.png" width="70%"/>

> Imagen de [Dmitry Soshnikov](http://soshnikov.com)

### Entrenando la GAN

Las GAN se denominan **adversarias** porque existe una competencia constante entre el generador y el discriminador. Durante esta competencia, tanto el generador como el discriminador mejoran, por lo que la red aprende a producir cada vez mejores imágenes.

La formación se desarrolla en dos etapas:

* **Entrenando al discriminador**. Esta tarea es bastante sencilla: generamos un lote de imágenes mediante el generador, las etiquetamos con 0, que significa imagen falsa, y tomamos un lote de imágenes del conjunto de datos de entrada (con etiqueta 1, imagen real). Obtenemos algo de *pérdida de discriminador* y realizamos backprop.
* **Entrenamiento del generador**. Esto es un poco más complicado, porque no conocemos directamente la salida esperada del generador. Tomamos toda la red GAN que consta de un generador seguido de un discriminador, la alimentamos con algunos vectores aleatorios y esperamos que el resultado sea 1 (correspondiente a imágenes reales). Luego congelamos los parámetros del discriminador (no queremos que se entrene en este paso) y realizamos la backprop.

Durante este proceso, las pérdidas tanto del generador como del discriminador no disminuyen significativamente. En la situación ideal deberían oscilar, correspondiendo a que ambas redes mejoren su rendimiento.

## ✍️ Ejercicios: GAN 

* [GAN Notebook in TensorFlow/Keras](GANTF.ipynb)
* [GAN Notebook in PyTorch](GANPyTorch.ipynb)

### Problemas con el entrenamiento GAN

Se sabe que las GAN son especialmente difíciles de entrenar. Aquí hay algunos problemas:

* **Modo Colapso**. Con este término queremos decir que el generador aprende a producir una imagen exitosa que engaña al generador, y no una variedad de imágenes diferentes.
* **Sensibilidad a los hiperparámetros**. A menudo se puede ver que una GAN no converge en absoluto y luego, repentinamente, la tasa de aprendizaje disminuye, lo que conduce a la convergencia.
* Mantener un **equilibrio** entre el generador y el discriminador. En muchos casos, la pérdida del discriminador puede caer a cero con relativa rapidez, lo que provoca que el generador no pueda seguir entrenándose. Para superar esto, podemos intentar establecer diferentes tasas de aprendizaje para el generador y el discriminador, u omitir el entrenamiento del discriminador si la pérdida ya es demasiado baja.
* Entrenamiento para **alta resolución**. Reflejando el mismo problema que con los codificadores automáticos, este problema se desencadena porque la reconstrucción de demasiadas capas de red convolucional genera artefactos. Este problema generalmente se resuelve con el llamado **crecimiento progresivo**, cuando primero se entrenan algunas capas en imágenes de baja resolución y luego se "desbloquean" o agregan capas. Otra solución sería agregar conexiones adicionales entre capas y entrenar varias resoluciones a la vez; consulte este [artículo sobre GAN de gradiente multiescala] (https://arxiv.org/abs/1903.06048) para obtener más detalles.

## Transferencia de estilo

Las GAN son una excelente manera de generar imágenes artísticas. Otra técnica interesante es la llamada **transferencia de estilo**, que toma una **imagen de contenido** y la vuelve a dibujar en un estilo diferente, aplicando filtros de **imagen de estilo**.

La forma en que funciona es la siguiente:
* Comenzamos con una imagen de ruido aleatorio (o con una imagen de contenido, pero para facilitar la comprensión es más fácil comenzar con ruido aleatorio)
* Nuestro objetivo sería crear una imagen de este tipo, que se acerque tanto a la imagen de contenido como a la imagen de estilo. Esto estaría determinado por dos funciones de pérdida:
    - La **pérdida de contenido** se calcula en función de las características extraídas por CNN en algunas capas de la imagen actual y la imagen del contenido.
    - La **pérdida de estilo** se calcula entre la imagen actual y la imagen de estilo de una manera inteligente utilizando matrices de Gram (más detalles en el [example notebook](StyleTransfer.ipynb))
* Para suavizar la imagen y eliminar el ruido, también introducimos la **Pérdida de variación**, que calcula la distancia promedio entre píxeles vecinos.
* El bucle de optimización principal ajusta la imagen actual mediante el descenso de gradiente (o algún otro algoritmo de optimización) para minimizar la pérdida total, que es una suma ponderada de las tres pérdidas.

## ✍️ Ejemplo: [Style Transfer](StyleTransfer.ipynb)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## Conclusión

En esta lección, aprendiste sobre GANS y cómo entrenarlos. También aprendió sobre los desafíos especiales que puede enfrentar este tipo de red neuronal y algunas estrategias sobre cómo superarlos.

## 🚀 Desafío

Corre por el [Style Transfer notebook](StyleTransfer.ipynb) usando tus propias imágenes. 

## Revisión y autoestudio

Como referencia, lea más sobre las GAN en estos recursos:

* Marco Pasini, [10 Lessons I Learned Training GANs for one Year](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), a *de facto* GAN arquitectura a considerar
* [Creating Generative Art using GANs on Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Asignación

Vuelva a visitar uno de los dos cuadernos asociados a esta lección y vuelva a entrenar la GAN con sus propias imágenes. ¿Qué puedes crear?
