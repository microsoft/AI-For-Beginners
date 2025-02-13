# Segmentación

Anteriormente aprendimos sobre la Detección de Objetos, que nos permite localizar objetos en la imagen prediciendo sus *cajas delimitadoras*. Sin embargo, para algunas tareas no solo necesitamos cajas delimitadoras, sino también una localización de objetos más precisa. Esta tarea se llama **segmentación**.

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

La segmentación se puede ver como **clasificación de píxeles**, donde para **cada** píxel de la imagen debemos predecir su clase (*fondo* siendo una de las clases). Hay dos algoritmos principales de segmentación:

* **Segmentación semántica** solo indica la clase del píxel y no hace distinción entre diferentes objetos de la misma clase.
* **Segmentación por instancias** divide las clases en diferentes instancias.

Por ejemplo, en la segmentación por instancias, estas ovejas son objetos diferentes, pero para la segmentación semántica todas las ovejas se representan con una sola clase.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Imagen de [este blog](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Existen diferentes arquitecturas neuronales para la segmentación, pero todas tienen la misma estructura. De alguna manera, es similar al autoencoder que aprendiste anteriormente, pero en lugar de descomponer la imagen original, nuestro objetivo es descomponer una **máscara**. Así, una red de segmentación tiene las siguientes partes:

* **Encoder** extrae características de la imagen de entrada.
* **Decoder** transforma esas características en la **imagen de máscara**, con el mismo tamaño y número de canales correspondiente al número de clases.

<img src="images/segm.png" width="80%">

> Imagen de [esta publicación](https://arxiv.org/pdf/2001.05566.pdf)

Debemos mencionar especialmente la función de pérdida que se utiliza para la segmentación. Al usar autoencoders clásicos, necesitamos medir la similitud entre dos imágenes, y podemos usar el error cuadrático medio (MSE) para hacerlo. En la segmentación, cada píxel en la imagen de máscara objetivo representa el número de clase (codificado en one-hot a lo largo de la tercera dimensión), por lo que necesitamos usar funciones de pérdida específicas para la clasificación: pérdida de entropía cruzada, promediada sobre todos los píxeles. Si la máscara es binaria, se utiliza **pérdida de entropía cruzada binaria** (BCE).

> ✅ La codificación one-hot es una forma de codificar una etiqueta de clase en un vector de longitud igual al número de clases. Echa un vistazo a [este artículo](https://datagy.io/sklearn-one-hot-encode/) sobre esta técnica.

## Segmentación para Imágenes Médicas

En esta lección, veremos la segmentación en acción entrenando la red para reconocer nevos humanos (también conocidos como lunares) en imágenes médicas. Usaremos la <a href="https://www.fc.up.pt/addi/ph2%20database.html">Base de Datos PH<sup>2</sup></a> de imágenes de dermatoscopia como fuente de imágenes. Este conjunto de datos contiene 200 imágenes de tres clases: nevo típico, nevo atípico y melanoma. Todas las imágenes también contienen una **máscara** correspondiente que delimita el nevo.

> ✅ Esta técnica es particularmente adecuada para este tipo de imágenes médicas, pero ¿qué otras aplicaciones del mundo real podrías imaginar?

<img alt="navi" src="images/navi.png"/>

> Imagen de la Base de Datos PH<sup>2</sup>

Entrenaremos un modelo para segmentar cualquier nevo de su fondo.

## ✍️ Ejercicios: Segmentación Semántica

Abre los cuadernos a continuación para aprender más sobre diferentes arquitecturas de segmentación semántica, practicar con ellas y verlas en acción.

* [Segmentación Semántica Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Segmentación Semántica TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Conclusión

La segmentación es una técnica muy poderosa para la clasificación de imágenes, que va más allá de las cajas delimitadoras hacia la clasificación a nivel de píxel. Es una técnica utilizada en imágenes médicas, entre otras aplicaciones.

## 🚀 Desafío

La segmentación del cuerpo es solo una de las tareas comunes que podemos realizar con imágenes de personas. Otras tareas importantes incluyen la **detección de esqueletos** y la **detección de poses**. Prueba la biblioteca [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) para ver cómo se puede utilizar la detección de poses.

## Revisión y Autoestudio

Este [artículo de Wikipedia](https://wikipedia.org/wiki/Image_segmentation) ofrece una buena visión general de las diversas aplicaciones de esta técnica. Aprende más por tu cuenta sobre los subdominios de la segmentación por instancias y la segmentación panóptica en este campo de estudio.

## [Tarea](lab/README.md)

En este laboratorio, intenta **segmentación del cuerpo humano** utilizando el [Conjunto de Datos de Segmentación del Cuerpo Completo MADS](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) de Kaggle.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.