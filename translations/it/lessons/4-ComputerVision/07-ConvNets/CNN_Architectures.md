# Conocidas Arquitecturas de CNN

### VGG-16

VGG-16 es una red que logró un 92.7% de precisión en la clasificación top-5 de ImageNet en 2014. Tiene la siguiente estructura de capas:

![Capas de ImageNet](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.it.jpg)

Como puedes ver, VGG sigue una arquitectura de pirámide tradicional, que es una secuencia de capas de convolución y agrupamiento.

![Pirámide de ImageNet](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.it.jpg)

> Imagen de [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet es una familia de modelos propuesta por Microsoft Research en 2015. La idea principal de ResNet es utilizar **bloques residuales**:

<img src="images/resnet-block.png" width="300"/>

> Imagen de [este artículo](https://arxiv.org/pdf/1512.03385.pdf)

La razón para usar un paso de identidad es hacer que nuestra capa prediga **la diferencia** entre el resultado de una capa anterior y la salida del bloque residual, de ahí el nombre *residual*. Estos bloques son mucho más fáciles de entrenar, y se pueden construir redes con varios cientos de esos bloques (las variantes más comunes son ResNet-52, ResNet-101 y ResNet-152).

También puedes pensar en esta red como capaz de ajustar su complejidad al conjunto de datos. Inicialmente, cuando comienzas a entrenar la red, los valores de los pesos son pequeños, y la mayor parte de la señal pasa a través de capas de identidad. A medida que avanza el entrenamiento y los pesos se hacen más grandes, la importancia de los parámetros de la red crece, y la red se ajusta para acomodar el poder expresivo necesario para clasificar correctamente las imágenes de entrenamiento.

### Google Inception

La arquitectura Google Inception lleva esta idea un paso más allá y construye cada capa de la red como una combinación de varios caminos diferentes:

<img src="images/inception.png" width="400"/>

> Imagen de [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Aquí, necesitamos enfatizar el papel de las convoluciones 1x1, porque al principio no tienen sentido. ¿Por qué necesitaríamos pasar por la imagen con un filtro 1x1? Sin embargo, debes recordar que los filtros de convolución también trabajan con varios canales de profundidad (originalmente - colores RGB, en capas posteriores - canales para diferentes filtros), y la convolución 1x1 se utiliza para mezclar esos canales de entrada utilizando diferentes pesos entrenables. También se puede ver como un muestreo (pooling) a lo largo de la dimensión de los canales.

Aquí hay [una buena publicación de blog](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) sobre el tema, y [el artículo original](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

MobileNet es una familia de modelos con tamaño reducido, adecuados para dispositivos móviles. Úsalos si tienes pocos recursos y puedes sacrificar un poco de precisión. La idea principal detrás de ellos es la llamada **convolución separable por profundidad**, que permite representar filtros de convolución mediante una composición de convoluciones espaciales y convoluciones 1x1 sobre los canales de profundidad. Esto reduce significativamente el número de parámetros, haciendo que la red sea más pequeña en tamaño y también más fácil de entrenar con menos datos.

Aquí hay [una buena publicación de blog sobre MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Conclusión

En esta unidad, has aprendido el concepto principal detrás de las redes neuronales de visión por computadora: las redes convolucionales. Las arquitecturas de la vida real que impulsan la clasificación de imágenes, la detección de objetos e incluso las redes de generación de imágenes se basan en CNNs, solo que con más capas y algunos trucos adicionales de entrenamiento.

## 🚀 Desafío

En los cuadernos adjuntos, hay notas al final sobre cómo obtener una mayor precisión. Realiza algunos experimentos para ver si puedes lograr una mayor precisión.

## [Cuestionario post-clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/207)

## Revisión y Autoestudio

Aunque las CNN se utilizan más a menudo para tareas de Visión por Computadora, son generalmente buenas para extraer patrones de tamaño fijo. Por ejemplo, si estamos tratando con sonidos, también podríamos querer usar CNNs para buscar patrones específicos en la señal de audio, en cuyo caso los filtros serían unidimensionales (y esta CNN se llamaría 1D-CNN). Además, a veces se utiliza 3D-CNN para extraer características en un espacio multidimensional, como ciertos eventos que ocurren en un video; CNN puede capturar ciertos patrones de características que cambian con el tiempo. Realiza algunas revisiones y autoestudio sobre otras tareas que se pueden realizar con CNNs.

## [Asignación](lab/README.md)

En este laboratorio, se te asigna la tarea de clasificar diferentes razas de gatos y perros. Estas imágenes son más complejas que el conjunto de datos MNIST y de dimensiones más altas, y hay más de 10 clases.

**Disclaimer**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No somos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.