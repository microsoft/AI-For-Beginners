# Redes neuronales convolucionales

Hemos visto antes que las redes neuronales son bastante buenas para manejar imágenes, e incluso el perceptrón de una capa es capaz de reconocer dígitos escritos a mano del conjunto de datos MNIST con una precisión razonable. Sin embargo, el conjunto de datos MNIST es muy especial y todos los dígitos están centrados dentro de la imagen, lo que simplifica la tarea.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/107)

En la vida real, queremos poder reconocer objetos en una imagen independientemente de su ubicación exacta en la imagen. La visión por computadora es diferente de la clasificación genérica, porque cuando intentamos encontrar un determinado objeto en la imagen, escaneamos la imagen en busca de algunos **patrones** específicos y sus combinaciones. Por ejemplo, cuando buscamos un gato, primero podemos buscar líneas horizontales, que pueden formar bigotes, y luego una combinación de bigotes puede decirnos que en realidad es una imagen de un gato. Lo importante es la posición relativa y la presencia de ciertos patrones, no su posición exacta en la imagen.

Para extraer patrones, usaremos la noción de **filtros convolucionales**. Como sabes, una imagen está representada por una matriz 2D o un tensor 3D con profundidad de color. Aplicar un filtro significa que tomamos una matriz de **núcleo de filtro** relativamente pequeña y, para cada píxel de la imagen original, calculamos el promedio ponderado con los puntos vecinos. Podemos ver esto como una pequeña ventana que se desliza sobre toda la imagen y promedia todos los píxeles de acuerdo con los pesos en la matriz del núcleo del filtro.

![Vertical Edge Filter](images/filter-vert.png) | ![Horizontal Edge Filter](images/filter-horiz.png)
----|----

> Imagen de Dmitry Soshnikov

Por ejemplo, si aplicamos filtros de borde vertical y borde horizontal de 3x3 a los dígitos MNIST, podemos obtener resaltados (por ejemplo, valores altos) donde hay bordes verticales y horizontales en nuestra imagen original. Por tanto, esos dos filtros se pueden utilizar para "buscar" bordes. De manera similar, podemos diseñar diferentes filtros para buscar otros patrones de bajo nivel:

<img src="images/lmfilters.jpg" width="500" align="center"/>


Imagen de [Leung-Malik Filter Bank](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

Sin embargo, si bien podemos diseñar los filtros para extraer algunos patrones manualmente, también podemos diseñar la red de tal manera que aprenda los patrones automáticamente. Es una de las ideas principales detrás de la CNN.

## Ideas principales detrás de CNN

La forma en que funcionan las CNN se basa en las siguientes ideas importantes:

* Los filtros convolucionales pueden extraer patrones.
* Podemos diseñar la red de tal manera que los filtros se entrenen automáticamente
* Podemos utilizar el mismo enfoque para encontrar patrones en funciones de alto nivel, no solo en la imagen original. Por lo tanto, la extracción de características de CNN funciona en una jerarquía de características, desde combinaciones de píxeles de bajo nivel hasta combinaciones de partes de imagen de nivel superior.

![Hierarchical Feature Extraction](images/FeatureExtractionCNN.png)

Imagen de [a paper by Hislop-Lynch](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), basa en [their research](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Ejercicios: Redes Neuronales Convolucionales

Sigamos explorando cómo funcionan las redes neuronales convolucionales y cómo podemos lograr filtros entrenables, trabajando con los cuadernos correspondientes:

* [Convolutional Neural Networks - PyTorch](ConvNetsPyTorch.ipynb)
* [Convolutional Neural Networks - TensorFlow](ConvNetsTF.ipynb)

## Pyramid Architecture

Most of the CNNs used for image processing follow a so-called pyramid architecture. The first convolutional layer applied to the original images typically has a relatively low number of filters (8-16), which correspond to different pixel combinations, such as horizontal/vertical lines of strokes. At the next level, we reduce the spatial dimension of the network, and increase the number of filters, which corresponds to more possible combinations of simple features. With each layer, as we move towards the final classifier, spatial dimensions of the image decrease, and the number of filters grow.

As an example, let's look at the architecture of VGG-16, a network that achieved 92.7% accuracy in ImageNet's top-5 classification in 2014:

![ImageNet Layers](images/vgg-16-arch1.jpg)

![ImageNet Pyramid](images/vgg-16-arch.jpg)

> Imagen de [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## Arquitecturas CNN más conocidas

[Continue your study about the best-known CNN architectures](CNN_Architectures.md)



