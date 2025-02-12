# Redes Neuronales Convolucionales

Hemos visto anteriormente que las redes neuronales son bastante efectivas para trabajar con imágenes, e incluso un perceptrón de una sola capa es capaz de reconocer dígitos manuscritos del conjunto de datos MNIST con una precisión razonable. Sin embargo, el conjunto de datos MNIST es muy especial, y todos los dígitos están centrados dentro de la imagen, lo que hace que la tarea sea más sencilla.

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/107)

En la vida real, queremos ser capaces de reconocer objetos en una imagen sin importar su ubicación exacta en ella. La visión por computadora es diferente de la clasificación genérica, porque cuando intentamos encontrar un cierto objeto en la imagen, estamos escaneando la imagen en busca de ciertos **patrones** y sus combinaciones. Por ejemplo, al buscar un gato, primero podemos buscar líneas horizontales, que pueden formar bigotes, y luego una combinación específica de bigotes puede indicarnos que en realidad es una imagen de un gato. La posición relativa y la presencia de ciertos patrones es importante, y no su posición exacta en la imagen.

Para extraer patrones, utilizaremos la noción de **filtros convolucionales**. Como saben, una imagen está representada por una matriz 2D, o un tensor 3D con profundidad de color. Aplicar un filtro significa que tomamos una matriz de **núcleo de filtro** relativamente pequeña, y para cada píxel en la imagen original calculamos el promedio ponderado con los puntos vecinos. Podemos ver esto como una pequeña ventana deslizándose sobre toda la imagen, promediando todos los píxeles de acuerdo con los pesos en la matriz del núcleo del filtro.

![Filtro de Borde Vertical](../../../../../translated_images/filter-vert.b7148390ca0bc356ddc7e55555d2481819c1e86ddde9dce4db5e71a69d6f887f.es.png) | ![Filtro de Borde Horizontal](../../../../../translated_images/filter-horiz.59b80ed4feb946efbe201a7fe3ca95abb3364e266e6fd90820cb893b4d3a6dda.es.png)
----|----

> Imagen de Dmitry Soshnikov

Por ejemplo, si aplicamos filtros de borde vertical y horizontal de 3x3 a los dígitos MNIST, podemos obtener resaltados (por ejemplo, valores altos) donde hay bordes verticales y horizontales en nuestra imagen original. Así, esos dos filtros pueden ser utilizados para "buscar" bordes. De manera similar, podemos diseñar diferentes filtros para buscar otros patrones de bajo nivel:
Estás entrenado con datos hasta octubre de 2023.

> Imagen de [Banco de Filtros Leung-Malik](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

Sin embargo, aunque podemos diseñar los filtros para extraer algunos patrones manualmente, también podemos diseñar la red de tal manera que aprenda los patrones automáticamente. Esta es una de las ideas principales detrás de la CNN.

## Ideas principales detrás de la CNN

La forma en que funcionan las CNN se basa en las siguientes ideas importantes:

* Los filtros convolucionales pueden extraer patrones
* Podemos diseñar la red de tal manera que los filtros se entrenen automáticamente
* Podemos utilizar el mismo enfoque para encontrar patrones en características de alto nivel, no solo en la imagen original. Así, la extracción de características de la CNN trabaja en una jerarquía de características, comenzando desde combinaciones de píxeles de bajo nivel, hasta combinaciones de partes de la imagen de nivel superior.

![Extracción de Características Jerárquicas](../../../../../translated_images/FeatureExtractionCNN.d9b456cbdae7cb643fde3032b81b2940e3cf8be842e29afac3f482725ba7f95c.es.png)

> Imagen de [un artículo de Hislop-Lynch](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), basado en [su investigación](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Ejercicios: Redes Neuronales Convolucionales

Continuemos explorando cómo funcionan las redes neuronales convolucionales, y cómo podemos lograr filtros entrenables, trabajando a través de los cuadernos correspondientes:

* [Redes Neuronales Convolucionales - PyTorch](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb)
* [Redes Neuronales Convolucionales - TensorFlow](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)

## Arquitectura Piramidal

La mayoría de las CNN utilizadas para el procesamiento de imágenes siguen una arquitectura piramidal. La primera capa convolucional aplicada a las imágenes originales típicamente tiene un número relativamente bajo de filtros (8-16), que corresponden a diferentes combinaciones de píxeles, como líneas de trazos horizontales/verticales. En el siguiente nivel, reducimos la dimensión espacial de la red, y aumentamos el número de filtros, lo que corresponde a más posibles combinaciones de características simples. Con cada capa, a medida que avanzamos hacia el clasificador final, las dimensiones espaciales de la imagen disminuyen, y el número de filtros aumenta.

Como ejemplo, veamos la arquitectura de VGG-16, una red que logró una precisión del 92.7% en la clasificación top-5 de ImageNet en 2014:

![Capas de ImageNet](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.es.jpg)

![Pirámide de ImageNet](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.es.jpg)

> Imagen de [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## Arquitecturas de CNN Más Conocidas

[Continúa tu estudio sobre las arquitecturas de CNN más conocidas](CNN_Architectures.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No somos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.