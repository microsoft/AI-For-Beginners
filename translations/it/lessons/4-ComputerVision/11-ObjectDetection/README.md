YOLO es un algoritmo en tiempo real de una sola pasada. La idea principal es la siguiente:

* La imagen se divide en regiones de $S\times S$.
* Para cada región, **CNN** predice $n$ objetos posibles, las coordenadas del *bounding box* y la *confianza* = *probabilidad* * IoU.

![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.it.png)

### SSD - Single Shot MultiBox Detector

SSD es otro método de detección de objetos en una sola pasada. La idea es similar a YOLO, pero en lugar de dividir la imagen en regiones, se utiliza una serie de capas de detección que producen predicciones de *bounding boxes* y clases en diferentes escalas.

![SSD](../../../../../translated_images/ssd.8f409ceb7ad470415f8995994dd89282b57541bff09ecde650902217c84f4c0d.it.png)

> *Imagen de [Este artículo](https://arxiv.org/pdf/1512.02325.pdf)*

### RetinaNet

RetinaNet es un enfoque que combina la velocidad de los métodos de una sola pasada con la precisión de los métodos de propuesta de región. Utiliza una función de pérdida llamada *Focal Loss* para abordar el problema del desbalanceo de clases en la detección de objetos.

![RetinaNet](../../../../../translated_images/retinanet.cfd3ebd2e5c63692a1c543b868134b66e4b0789230c22679b07eebd0e69d7cbc.it.png)

> *Imagen de [Este artículo](https://arxiv.org/pdf/1708.02002.pdf)*

## Conclusión

La detección de objetos es un campo emocionante en la visión por computadora que ha visto un progreso significativo en los últimos años. Desde métodos simples y naïve hasta enfoques avanzados como YOLO, SSD y RetinaNet, hay una variedad de técnicas disponibles para abordar diferentes desafíos en la detección de objetos. A medida que la tecnología avanza, podemos esperar ver aún más innovaciones en este campo.
> Image from [official paper](https://arxiv.org/abs/1506.02640)

### Other Algorithms

* RetinaNet: [official paper](https://arxiv.org/abs/1708.02002)
   - [PyTorch Implementation in Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Keras Implementation](https://github.com/fizyr/keras-retinanet)
   - [Object Detection with RetinaNet](https://keras.io/examples/vision/retinanet/) in Keras Samples
* SSD (Single Shot Detector): [official paper](https://arxiv.org/abs/1512.02325)

## ✍️ Exercises: Object Detection

Continue your learning with the following notebook:

[ObjectDetection.ipynb](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)

## Conclusion

In this lesson, you explored the different methods available for object detection!

## 🚀 Challenge

Go through these articles and notebooks on YOLO and try them out for yourself:

* [Good blog post](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) discussing YOLO
 * [Official site](https://pjreddie.com/darknet/yolo/)
 * Yolo: [Keras implementation](https://github.com/experiencor/keras-yolo2), [step-by-step notebook](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [Keras implementation](https://github.com/experiencor/keras-yolo2), [step-by-step notebook](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## Review & Self Study

* [Object Detection](https://tjmachinelearning.com/lectures/1718/obj/) by Nikhil Sardana
* [A good comparison of object detection algorithms](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Review of Deep Learning Algorithms for Object Detection](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [A Step-by-Step Introduction to the Basic Object Detection Algorithms](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implementation of Faster R-CNN in Python for Object Detection](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Assignment: Object Detection](lab/README.md)

**Disclaimer**: 
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.