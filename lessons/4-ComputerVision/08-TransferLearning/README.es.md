# Pre-trained Networks and Transfer Learning

Training CNNs can take a lot of time, and a lot of data is required for that task. However, much of the time is spent learning the best low-level filters that a network can use to extract patterns from images. A natural question arises - can we use a neural network trained on one dataset and adapt it to classify different images without requiring a full training process?

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/108)

Este enfoque se llama **aprendizaje por transferencia** porque transferimos algunos conocimientos de un modelo de red neuronal a otro. En el aprendizaje por transferencia, normalmente comenzamos con un modelo previamente entrenado, que ha sido entrenado en algún conjunto de datos de imágenes grande, como **ImageNet**. Esos modelos ya pueden hacer un buen trabajo extrayendo diferentes características de imágenes genéricas y, en muchos casos, simplemente construir un clasificador sobre esas características extraídas puede producir un buen resultado.

> ✅ Transfer Learning es un término que se encuentra en otros campos académicos, como la Educación. Se refiere al proceso de tomar conocimiento de un dominio y aplicarlo a otro.

## Modelos previamente entrenados como extractores de características

Las redes convolucionales de las que hemos hablado en la sección anterior contenían una serie de capas, cada una de las cuales se supone que extrae algunas características de la imagen, comenzando desde combinaciones de píxeles de bajo nivel (como una línea o trazo horizontal/vertical), hasta a combinaciones de características de nivel superior, correspondientes a cosas como el ojo de una llama. Si entrenamos a CNN con un conjunto de datos suficientemente grande de imágenes genéricas y diversas, la red debería aprender a extraer esas características comunes.

Tanto Keras como PyTorch contienen funciones para cargar fácilmente pesos de redes neuronales previamente entrenados para algunas arquitecturas comunes, la mayoría de las cuales fueron entrenadas en imágenes de ImageNet. Los más utilizados se describen en la página [Arquitecturas CNN](../07-ConvNets/CNN_Architectures.md) de la lección anterior. En particular, es posible que desee considerar el uso de uno de los siguientes:

* **VGG-16/VGG-19** que son modelos relativamente simples que aún ofrecen buena precisión. A menudo, utilizar VGG como primer intento es una buena opción para ver cómo funciona el aprendizaje por transferencia.
* **ResNet** es una familia de modelos propuesta por Microsoft Research en 2015. Tienen más capas y, por lo tanto, requieren más recursos.
* **MobileNet** es una familia de modelos de tamaño reducido, aptos para dispositivos móviles. Úselos si tiene pocos recursos y puede sacrificar un poco de precisión.

Aquí hay ejemplos de características extraídas de una imagen de un gato por la red VGG-16:

![Features extracted by VGG-16](images/features.png)

## Conjunto de datos sobre gatos y perros

En este ejemplo, usaremos un conjunto de datos de [Cats and Dogs](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), which is very close to a real-life image classification scenario.

## ✍️ Exercise: Transfer Learning

Let's see transfer learning in action in corresponding notebooks:

* [Transfer Learning - PyTorch](TransferLearningPyTorch.ipynb)
* [Transfer Learning - TensorFlow](TransferLearningTF.ipynb)

## Visualizando al gato adversario

La red neuronal previamente entrenada contiene diferentes patrones dentro de su *cerebro*, incluidas nociones de **gato ideal** (así como de perro ideal, cebra ideal, etc.). Sería interesante de alguna manera **visualizar esta imagen**. Sin embargo, no es sencillo, porque los patrones están repartidos por todos los pesos de la red y también organizados en una estructura jerárquica.

Un enfoque que podemos tomar es comenzar con una imagen aleatoria y luego intentar usar la técnica de **optimización de descenso de gradiente** para ajustar esa imagen de tal manera que la red comience a pensar que es un gato.

![Image Optimization Loop](images/ideal-cat-loop.png)

Sin embargo, si hacemos esto, recibiremos algo muy similar a un ruido aleatorio. Esto se debe a que *hay muchas maneras de hacer que la red piense que la imagen de entrada es un gato*, incluidas algunas que no tienen sentido visualmente. Si bien esas imágenes contienen muchos patrones típicos de un gato, no hay nada que las limite a ser visualmente distintivas.

Para mejorar el resultado, podemos agregar otro término a la función de pérdida, que se llama **pérdida de variación**. Es una métrica que muestra qué tan similares son los píxeles vecinos de la imagen. Minimizar la pérdida de variación hace que la imagen sea más suave y elimina el ruido, revelando así patrones más atractivos visualmente. A continuación se muestra un ejemplo de imágenes "ideales" que se clasifican como gatos y cebras con alta probabilidad:

![Ideal Cat](images/ideal-cat.png) | ![Ideal Zebra](images/ideal-zebra.png)
-----|-----
 *Ideal Cat* | *Ideal Zebra*

 Se puede utilizar un enfoque similar para realizar los llamados **ataques adversarios** en una red neuronal. Supongamos que queremos engañar a una red neuronal y hacer que un perro parezca un gato. Si tomamos la imagen del perro, que una red reconoce como un perro, podemos modificarla un poco pero usando la optimización de descenso de gradiente, hasta que la red comience a clasificarlo como un gato:

 ![Picture of a Dog](images/original-dog.png) | ![Picture of a dog classified as a cat](images/adversarial-dog.png)
-----|-----
*Imagen original de un perro* | *Foto de un perro clasificado como gato*

Vea el código para reproducir los resultados anteriores en el siguiente cuaderno:

* [Ideal and Adversarial Cat - TensorFlow](AdversarialCat_TF.ipynb)
## Conclusion

Al utilizar el aprendizaje por transferencia, puede crear rápidamente un clasificador para una tarea de clasificación de objetos personalizada y lograr una alta precisión. Puede ver que las tareas más complejas que estamos resolviendo ahora requieren una mayor potencia computacional y no se pueden resolver fácilmente en la CPU. En la siguiente unidad, intentaremos utilizar una implementación más ligera para entrenar el mismo modelo utilizando menores recursos informáticos, lo que da como resultado una precisión ligeramente menor.

## 🚀 Desafío

En los cuadernos adjuntos, hay notas al final sobre cómo funciona mejor la transferencia de conocimientos con datos de entrenamiento algo similares (un nuevo tipo de animal, tal vez). Experimente un poco con tipos de imágenes completamente nuevos para ver qué tan bien o mal funcionan sus modelos de transferencia de conocimiento.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Revisión y autoestudio

Leer de parte a parte [TrainingTricks.md](TrainingTricks.md) para profundizar su conocimiento sobre alguna otra forma de entrenar sus modelos.

## [Assignment](lab/README.md)

En este laboratorio, usaremos la vida real [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) conjunto de datos de mascotas con 35 razas de perros y gatos, y crearemos un clasificador de aprendizaje por transferencia.
