# Segmentación

Anteriormente aprendimos sobre la Detección de Objetos, que nos permite localizar objetos en la imagen prediciendo sus *cuadros delimitadores*. Sin embargo, para algunas tareas no sólo necesitamos cuadros delimitadores, sino también una localización de objetos más precisa. Esta tarea se llama **segmentación**.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

La segmentación puede verse como una **clasificación de píxeles**, mientras que para **cada** píxel de imagen debemos predecir su clase (*el fondo* es una de las clases). Hay dos algoritmos de segmentación principales:

* **Segmentación semántica** solo indica la clase de píxel y no hace distinción entre diferentes objetos de la misma clase.
* **La segmentación de instancias** divide las clases en diferentes instancias.

Por ejemplo, en la segmentación, estas ovejas son objetos diferentes, pero para la segmentación semántica todas las ovejas están representadas por una clase.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Imagen de [this blog post](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Existen diferentes arquitecturas neuronales para la segmentación, pero todas tienen la misma estructura. En cierto modo, es similar al codificador automático que conoció anteriormente, pero en lugar de deconstruir la imagen original, nuestro objetivo es deconstruir una **máscara**. Así, una red de segmentación tiene las siguientes partes:

* **Codificador** extrae características de la imagen de entrada
* **Decoder** transforma esas características en la **imagen de máscara**, con el mismo tamaño y número de canales correspondientes al número de clases.

<img src="images/segm.png" width="80%">

> Imagen de [this publication](https://arxiv.org/pdf/2001.05566.pdf)

Debemos mencionar especialmente la función de pérdida que se utiliza para la segmentación. Cuando utilizamos codificadores automáticos clásicos, necesitamos medir la similitud entre dos imágenes y podemos usar el error cuadrático medio (MSE) para hacerlo. En la segmentación, cada píxel en la imagen de la máscara de destino representa el número de clase (codificado en caliente a lo largo de la tercera dimensión), por lo que necesitamos usar funciones de pérdida específicas para la clasificación: pérdida de entropía cruzada, promediada sobre todos los píxeles. Si la máscara es binaria, se utiliza **pérdida de entropía cruzada binaria** (BCE).

> ✅ La codificación one-hot es una forma de codificar una etiqueta de clase en un vector de longitud igual al número de clases. Echa un vistazo a [this article](https://datagy.io/sklearn-one-hot-encode/) en esta técnica.
>
> ## Segmentación para imágenes médicas

En esta lección, veremos la segmentación en acción entrenando a la red para que reconozca nevos humanos (también conocidos como lunares) en imágenes médicas. Usaremos la <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> Base de datos</a> de imágenes de dermatoscopia como imagen. fuente. Este conjunto de datos contiene 200 imágenes de tres clases: nevo típico, nevo atípico y melanoma. Todas las imágenes también contienen una **máscara** correspondiente que delinea el nevo.

> ✅ Esta técnica es particularmente apropiada para este tipo de imágenes médicas, pero ¿qué otras aplicaciones en el mundo real podrías imaginar?
>
> <img alt="navi" src="images/navi.png"/>

> Imagen de the PH<sup>2</sup> Database

Entrenaremos un modelo para segmentar cualquier nevo desde su fondo.

## ✍️ Ejercicios: Segmentación Semántica

Abra los cuadernos siguientes para obtener más información sobre las diferentes arquitecturas de segmentación semántica, practicar cómo trabajar con ellas y verlas en acción.

* [Semantic Segmentation Pytorch](SemanticSegmentationPytorch.ipynb)
* [Semantic Segmentation TensorFlow](SemanticSegmentationTF.ipynb)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Conclusión

La segmentación es una técnica muy poderosa para la clasificación de imágenes, que va más allá de los cuadros delimitadores a la clasificación a nivel de píxeles. Es una técnica utilizada en imágenes médicas, entre otras aplicaciones.

## 🚀 Desafío

La segmentación corporal es solo una de las tareas comunes que podemos realizar con imágenes de personas. Otras tareas importantes incluyen **detección de esqueleto** y **detección de pose**. Pruebe la biblioteca [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) para ver cómo se puede utilizar la detección de pose.

## Revisión y autoestudio

Es [wikipedia article](https://wikipedia.org/wiki/Image_segmentation) ofrece una buena visión general de las diversas aplicaciones de esta técnica. Obtenga más información por su cuenta sobre los subdominios de segmentación de instancias y segmentación panóptica en este campo de investigación.
## [Assignment](lab/README.md)

En este laboratorio, intente **human body segmentation** usando [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) de Kaggle.


