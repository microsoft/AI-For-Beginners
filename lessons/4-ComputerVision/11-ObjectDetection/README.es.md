# Detección de objetos

Los modelos de clasificación de imágenes que hemos tratado hasta ahora tomaron una imagen y produjeron un resultado categórico, como la clase "número" en un problema MNIST. Sin embargo, en muchos casos no queremos simplemente saber que una imagen representa objetos, sino que queremos poder determinar su ubicación exacta. Este es exactamente el punto de **detección de objetos**.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/111)

![Object Detection](images/Screen_Shot_2016-11-17_at_11.14.54_AM.png)

> Imagen de [YOLO v2 web site](https://pjreddie.com/darknet/yolov2/)

## A Naive Approach to Object Detection

Assuming we wanted to find a cat on a picture, a very naive approach to object detection would be the following:

1. Break the picture down to a number of tiles
2. Run image classification on each tile.
3. Those tiles that result in sufficiently high activation can be considered to contain the object in question.

![Naive Object Detection](images/naive-detection.png)

> *Imagen de [Exercise Notebook](ObjectDetection-TF.ipynb)*

Sin embargo, este enfoque está lejos de ser ideal, porque solo permite que el algoritmo ubique el cuadro delimitador del objeto de manera muy imprecisa. Para una ubicación más precisa, necesitamos ejecutar algún tipo de **regresión** para predecir las coordenadas de los cuadros delimitadores y, para ello, necesitamos conjuntos de datos específicos.

## Regresión para la detección de objetos

[This blog post](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491) tiene una excelente y suave introducción a la detección de formas.

## Conjuntos de datos para la detección de objetos

Es posible que se encuentre con los siguientes conjuntos de datos para esta tarea:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 20 clases
* [COCO](http://cocodataset.org/#home) - Objetos comunes en contexto. 80 clases, cuadros delimitadores y máscara de segmentación.

![COCO](images/coco-examples.jpg)

## Métricas de detección de objetos

### Intersección sobre Unión

Mientras que para la clasificación de imágenes es fácil medir qué tan bien funciona el algoritmo, para la detección de objetos necesitamos medir tanto la exactitud de la clase como la precisión de la ubicación del cuadro delimitador inferida. Para este último, utilizamos la llamada **Intersección sobre Unión** (IoU), que mide qué tan bien se superponen dos cuadros (o dos áreas arbitrarias).

![IoU](images/iou_equation.png)

> *Figura 2 de [this excellent blog post on IoU](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

La idea es simple: dividimos el área de intersección entre dos figuras por el área de su unión. Para dos áreas idénticas, IoU sería 1, mientras que para áreas completamente desunidas será 0. De lo contrario, variará de 0 a 1. Por lo general, solo consideramos aquellos cuadros delimitadores para los cuales IoU supera un cierto valor.

### Precisión promedio

Supongamos que queremos medir qué tan bien se reconoce una determinada clase de objetos $C$. Para medirlo, utilizamos métricas de **Precisión promedio**, que se calcula de la siguiente manera:

1. Considere la curva de recuperación de precisión que muestra la precisión en función de un valor de umbral de detección (de 0 a 1).
2. Dependiendo del umbral obtendremos más o menos objetos detectados en la imagen, y diferentes valores de precisión y recuperación.
3. La curva se verá así:

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *Image from [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

La precisión promedio para una clase dada $C$ es el área bajo esta curva. Más precisamente, el eje de recuperación generalmente se divide en 10 partes y la precisión se promedia en todos esos puntos:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP y pagaré

Consideraremos solo aquellas detecciones para las cuales IoU esté por encima de un cierto valor. Por ejemplo, en el conjunto de datos PASCAL VOC normalmente se supone $\mbox{IoU Threshold} = 0,5$, mientras que en COCO AP se mide para diferentes valores de $\mbox{IoU Threshold}$.

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *Imagen de [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### Precisión media media - mapa

La métrica principal para la detección de objetos se llama **Precisión promedio media** o **mAP**. Es el valor de la precisión promedio, el promedio de todas las clases de objetos y, a veces, también por encima de $\mbox{IoU Threshold}$. Con más detalle, se describe el proceso de cálculo de **mAP**.
[in this blog post](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)), y tambien [here with code samples](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734).

## Diferentes enfoques de detección de objetos

Hay dos clases amplias de algoritmos de detección de objetos:

* **Redes de propuesta regional** (R-CNN, Fast R-CNN, Faster R-CNN). La idea principal es generar **regiones de interés** (ROI) y ejecutar CNN sobre ellas, buscando la máxima activación. Es un poco similar al enfoque ingenuo, con la excepción de que los ROI se generan de una manera más inteligente. Uno de los mayores inconvenientes de estos métodos es que son lentos, porque necesitamos muchas pasadas del clasificador CNN sobre la imagen.
* **Métodos de una sola pasada** (YOLO, SSD, RetinaNet). En esas arquitecturas diseñamos la red para predecir tanto las clases como el ROI en una sola pasada.

### R-CNN: CNN basada en regiones

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) usos [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) to generate hierarchical structure of ROI regions, which are then passed through CNN feature extractors and SVM-classifiers to determine the object class, and linear regression to determine *bounding box* coordinates. [Official Paper](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](images/rcnn1.png)

> *Imagen de van de Sande et al. ICCV’11*

![RCNN-1](images/rcnn2.png)

> *Imagen de [this blog](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)

### F-RCNN - R-CNN rápido

Este enfoque es similar a R-CNN, pero las regiones se definen después de que se hayan aplicado las capas de convolución.

![FRCNN](images/f-rcnn.png)

> Imagen de [the Official Paper](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### R-CNN más rápido

La idea principal de este enfoque es utilizar una red neuronal para predecir el ROI, la llamada *Red de propuesta de región*. [Artículo](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](images/faster-rcnn.png)

> Imagen de [the official paper](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: red totalmente convolucional basada en regiones

Este algoritmo es incluso más rápido que Faster R-CNN. La idea principal es la siguiente:

1. Extraemos funciones usando ResNet-101
1. Las características se procesan mediante **Mapa de puntuación sensible a la posición**. Cada objeto de las clases $C$ se divide por $k\times k$ regiones, y estamos entrenando para predecir partes de objetos.
1. Para cada parte de $k\times k$ regiones, todas las redes votan por clases de objetos y se selecciona la clase de objeto con voto máximo.

![r-fcn image](images/r-fcn.png)

> Imagen de [official paper](https://arxiv.org/abs/1605.06409)

### YOLO - Sólo miras una vez

YOLO es un algoritmo de un solo paso en tiempo real. La idea principal es la siguiente:

  * La imagen está dividida en regiones $S\times S$
  * Para cada región, **CNN** predice $n$ posibles objetos, *coordenadas del *cuadro delimitador* y *confianza*=*probabilidad* * IoU.

![YOLO](images/yolo.png)

> Imagen de [official paper](https://arxiv.org/abs/1506.02640)

### Otros algoritmos

* RetinaNet: [official paper](https://arxiv.org/abs/1708.02002)
   - [PyTorch Implementation in Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Keras Implementation](https://github.com/fizyr/keras-retinanet)
   - [Object Detection with RetinaNet](https://keras.io/examples/vision/retinanet/) en Keras Samples
* SSD (Single Shot Detector): [official paper](https://arxiv.org/abs/1512.02325)

  ## ✍️ Ejercicios: Detección de objetos

Continúa tu aprendizaje en el siguiente cuaderno:

[ObjectDetection.ipynb](ObjectDetection.ipynb)

## Conclusión

En esta lección, realizó un recorrido relámpago por las diversas formas en que se puede lograr la detección de objetos.

## 🚀 Desafío

Lea estos artículos y cuadernos sobre YOLO y pruébelos usted mismo.

* [Good blog post](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) describiendo YOLO
 * [Official site](https://pjreddie.com/darknet/yolo/)
 * Yolo: [Keras implementation](https://github.com/experiencor/keras-yolo2), [step-by-step notebook](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [Keras implementation](https://github.com/experiencor/keras-yolo2), [step-by-step notebook](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## Revisión y autoestudio

* [Object Detection](https://tjmachinelearning.com/lectures/1718/obj/) by Nikhil Sardana
* [A good comparison of object detection algorithms](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Review of Deep Learning Algorithms for Object Detection](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [A Step-by-Step Introduction to the Basic Object Detection Algorithms](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implementation of Faster R-CNN in Python for Object Detection](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Assignment: Object Detection](lab/README.md)









