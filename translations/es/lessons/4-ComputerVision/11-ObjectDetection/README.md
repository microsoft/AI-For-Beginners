<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d85c8b08f6d1b48fd7f35b99f93c1138",
  "translation_date": "2025-08-24T09:16:52+00:00",
  "source_file": "lessons/4-ComputerVision/11-ObjectDetection/README.md",
  "language_code": "es"
}
-->
# Detección de Objetos

Los modelos de clasificación de imágenes que hemos visto hasta ahora toman una imagen y producen un resultado categórico, como la clase 'número' en un problema de MNIST. Sin embargo, en muchos casos no solo queremos saber que una imagen contiene objetos, sino que también queremos determinar su ubicación precisa. Esto es exactamente el objetivo de la **detección de objetos**.

## [Cuestionario previo a la lección](https://ff-quizzes.netlify.app/en/ai/quiz/21)

![Detección de Objetos](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/Screen_Shot_2016-11-17_at_11.14.54_AM.png)

> Imagen de [sitio web de YOLO v2](https://pjreddie.com/darknet/yolov2/)

## Un Enfoque Ingenuo para la Detección de Objetos

Supongamos que queremos encontrar un gato en una imagen. Un enfoque muy ingenuo para la detección de objetos sería el siguiente:

1. Dividir la imagen en varias secciones o mosaicos.
2. Ejecutar un modelo de clasificación de imágenes en cada mosaico.
3. Aquellos mosaicos que resulten en una activación suficientemente alta pueden considerarse como que contienen el objeto en cuestión.

![Detección Ingenua](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/naive-detection.png)

> *Imagen del [Cuaderno de Ejercicios](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection-TF.ipynb)*

Sin embargo, este enfoque está lejos de ser ideal, ya que solo permite al algoritmo localizar la caja delimitadora del objeto de manera muy imprecisa. Para una ubicación más precisa, necesitamos ejecutar algún tipo de **regresión** para predecir las coordenadas de las cajas delimitadoras, y para ello necesitamos conjuntos de datos específicos.

## Regresión para la Detección de Objetos

[Esta publicación de blog](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491) ofrece una excelente introducción a la detección de formas.

## Conjuntos de Datos para la Detección de Objetos

Es posible que encuentres los siguientes conjuntos de datos para esta tarea:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 20 clases
* [COCO](http://cocodataset.org/#home) - Objetos Comunes en Contexto. 80 clases, cajas delimitadoras y máscaras de segmentación

![COCO](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/coco-examples.jpg)

## Métricas de Detección de Objetos

### Intersección sobre Unión

Mientras que para la clasificación de imágenes es fácil medir qué tan bien funciona el algoritmo, para la detección de objetos necesitamos medir tanto la corrección de la clase como la precisión de la ubicación inferida de la caja delimitadora. Para esto último, usamos la llamada **Intersección sobre Unión** (IoU), que mide qué tan bien se superponen dos cajas (o dos áreas arbitrarias).

![IoU](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/iou_equation.png)

> *Figura 2 de [esta excelente publicación sobre IoU](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

La idea es simple: dividimos el área de intersección entre dos figuras por el área de su unión. Para dos áreas idénticas, IoU sería 1, mientras que para áreas completamente disjuntas será 0. En otros casos, variará entre 0 y 1. Normalmente solo consideramos aquellas cajas delimitadoras para las que IoU supera un cierto valor.

### Precisión Promedio

Supongamos que queremos medir qué tan bien se reconoce una clase de objetos $C$ dada. Para medirlo, usamos la métrica de **Precisión Promedio**, que se calcula de la siguiente manera:

1. Consideramos la curva de Precisión-Recall, que muestra la precisión dependiendo de un valor umbral de detección (de 0 a 1).
2. Dependiendo del umbral, obtendremos más o menos objetos detectados en la imagen, y diferentes valores de precisión y recall.
3. La curva se verá así:

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *Imagen de [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

La Precisión Promedio para una clase $C$ dada es el área bajo esta curva. Más precisamente, el eje de Recall se divide típicamente en 10 partes, y la Precisión se promedia en todos esos puntos:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP e IoU

Solo consideraremos aquellas detecciones para las que IoU esté por encima de un cierto valor. Por ejemplo, en el conjunto de datos PASCAL VOC típicamente se asume $\mbox{IoU Threshold} = 0.5$, mientras que en COCO AP se mide para diferentes valores de $\mbox{IoU Threshold}$.

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *Imagen de [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### Precisión Promedio Media - mAP

La métrica principal para la Detección de Objetos se llama **Precisión Promedio Media**, o **mAP**. Es el valor de la Precisión Promedio, promediado entre todas las clases de objetos, y a veces también sobre $\mbox{IoU Threshold}$. El proceso de cálculo de **mAP** se describe en detalle
[en esta publicación de blog](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3), y también [aquí con ejemplos de código](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734).

## Diferentes Enfoques para la Detección de Objetos

Existen dos grandes clases de algoritmos de detección de objetos:

* **Redes de Propuesta de Regiones** (R-CNN, Fast R-CNN, Faster R-CNN). La idea principal es generar **Regiones de Interés** (ROI) y ejecutar una CNN sobre ellas, buscando la activación máxima. Es un poco similar al enfoque ingenuo, con la excepción de que las ROI se generan de una manera más inteligente. Una de las principales desventajas de estos métodos es que son lentos, ya que se necesitan muchos pases del clasificador CNN sobre la imagen.
* Métodos de **una sola pasada** (YOLO, SSD, RetinaNet). En estas arquitecturas diseñamos la red para predecir tanto las clases como las ROI en un solo pase.

### R-CNN: CNN Basada en Regiones

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) utiliza [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) para generar una estructura jerárquica de regiones ROI, que luego se pasan por extractores de características CNN y clasificadores SVM para determinar la clase del objeto, y regresión lineal para determinar las coordenadas de la *caja delimitadora*. [Artículo oficial](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/rcnn1.png)

> *Imagen de van de Sande et al. ICCV’11*

![RCNN-1](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/rcnn2.png)

> *Imágenes de [este blog](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - Fast R-CNN

Este enfoque es similar a R-CNN, pero las regiones se definen después de que se han aplicado las capas de convolución.

![FRCNN](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/f-rcnn.png)

> Imagen del [Artículo Oficial](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

La idea principal de este enfoque es usar una red neuronal para predecir las ROI, la llamada *Red de Propuesta de Regiones*. [Artículo](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/faster-rcnn.png)

> Imagen del [artículo oficial](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: Red Completamente Convolucional Basada en Regiones

Este algoritmo es incluso más rápido que Faster R-CNN. La idea principal es la siguiente:

1. Extraemos características usando ResNet-101.
2. Las características se procesan mediante un **Mapa de Puntuación Sensible a la Posición**. Cada objeto de las clases $C$ se divide en regiones de $k\times k$, y entrenamos para predecir partes de los objetos.
3. Para cada parte de las regiones $k\times k$, todas las redes votan por las clases de objetos, y se selecciona la clase de objeto con el máximo voto.

![r-fcn image](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/r-fcn.png)

> Imagen del [artículo oficial](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO es un algoritmo de una sola pasada en tiempo real. La idea principal es la siguiente:

 * La imagen se divide en regiones de $S\times S$.
 * Para cada región, **CNN** predice $n$ posibles objetos, las coordenadas de la *caja delimitadora* y la *confianza* = *probabilidad* * IoU.

 ![YOLO](../../../../../lessons/4-ComputerVision/11-ObjectDetection/images/yolo.png)

> Imagen del [artículo oficial](https://arxiv.org/abs/1506.02640)

### Otros Algoritmos

* RetinaNet: [artículo oficial](https://arxiv.org/abs/1708.02002)
   - [Implementación en PyTorch en Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Implementación en Keras](https://github.com/fizyr/keras-retinanet)
   - [Detección de Objetos con RetinaNet](https://keras.io/examples/vision/retinanet/) en ejemplos de Keras
* SSD (Single Shot Detector): [artículo oficial](https://arxiv.org/abs/1512.02325)

## ✍️ Ejercicios: Detección de Objetos

Continúa tu aprendizaje en el siguiente cuaderno:

[ObjectDetection.ipynb](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)

## Conclusión

En esta lección hiciste un recorrido rápido por las diversas formas en que se puede lograr la detección de objetos.

## 🚀 Desafío

Lee estos artículos y cuadernos sobre YOLO y pruébalos por ti mismo:

* [Buen artículo](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) que describe YOLO
 * [Sitio oficial](https://pjreddie.com/darknet/yolo/)
 * Yolo: [Implementación en Keras](https://github.com/experiencor/keras-yolo2), [cuaderno paso a paso](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [Implementación en Keras](https://github.com/experiencor/keras-yolo2), [cuaderno paso a paso](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Cuestionario posterior a la lección](https://ff-quizzes.netlify.app/en/ai/quiz/22)

## Revisión y Autoestudio

* [Detección de Objetos](https://tjmachinelearning.com/lectures/1718/obj/) por Nikhil Sardana
* [Una buena comparación de algoritmos de detección de objetos](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Revisión de Algoritmos de Aprendizaje Profundo para la Detección de Objetos](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [Introducción paso a paso a los algoritmos básicos de detección de objetos](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implementación de Faster R-CNN en Python para la Detección de Objetos](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Asignación: Detección de Objetos](lab/README.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.