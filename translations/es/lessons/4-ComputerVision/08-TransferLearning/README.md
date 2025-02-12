# Redes Neuronales Pre-entrenadas y Aprendizaje por Transferencia

Entrenar CNNs puede llevar mucho tiempo, y se requiere una gran cantidad de datos para esa tarea. Sin embargo, gran parte del tiempo se dedica a aprender los mejores filtros de bajo nivel que una red puede utilizar para extraer patrones de las imágenes. Surge una pregunta natural: ¿podemos usar una red neuronal entrenada en un conjunto de datos y adaptarla para clasificar diferentes imágenes sin necesidad de un proceso de entrenamiento completo?

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/108)

Este enfoque se llama **aprendizaje por transferencia**, porque transferimos parte del conocimiento de un modelo de red neuronal a otro. En el aprendizaje por transferencia, normalmente comenzamos con un modelo pre-entrenado, que ha sido entrenado en un gran conjunto de datos de imágenes, como **ImageNet**. Esos modelos ya pueden hacer un buen trabajo extrayendo diferentes características de imágenes genéricas, y en muchos casos, simplemente construir un clasificador sobre esas características extraídas puede dar un buen resultado.

> ✅ El Aprendizaje por Transferencia es un término que se encuentra en otros campos académicos, como la Educación. Se refiere al proceso de tomar conocimiento de un dominio y aplicarlo a otro.

## Modelos Pre-entrenados como Extractores de Características

Las redes convolucionales de las que hemos hablado en la sección anterior contenían una serie de capas, cada una de las cuales se supone que extrae algunas características de la imagen, comenzando desde combinaciones de píxeles de bajo nivel (como líneas horizontales/verticales o trazos), hasta combinaciones de características de nivel superior, que corresponden a cosas como el ojo de una llama. Si entrenamos una CNN en un conjunto de datos suficientemente grande de imágenes genéricas y diversas, la red debería aprender a extraer esas características comunes.

Tanto Keras como PyTorch contienen funciones para cargar fácilmente los pesos de redes neuronales pre-entrenadas para algunas arquitecturas comunes, la mayoría de las cuales fueron entrenadas en imágenes de ImageNet. Las más utilizadas se describen en la página de [Arquitecturas CNN](../07-ConvNets/CNN_Architectures.md) de la lección anterior. En particular, es posible que desees considerar el uso de uno de los siguientes:

* **VGG-16/VGG-19**, que son modelos relativamente simples que aún ofrecen buena precisión. A menudo, usar VGG como primer intento es una buena elección para ver cómo funciona el aprendizaje por transferencia.
* **ResNet** es una familia de modelos propuestos por Microsoft Research en 2015. Tienen más capas y, por lo tanto, requieren más recursos.
* **MobileNet** es una familia de modelos de tamaño reducido, adecuados para dispositivos móviles. Úsalos si tienes recursos limitados y puedes sacrificar un poco de precisión.

Aquí hay ejemplos de características extraídas de una imagen de un gato por la red VGG-16:

![Características extraídas por VGG-16](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.es.png)

## Conjunto de Datos de Gatos vs. Perros

En este ejemplo, utilizaremos un conjunto de datos de [Gatos y Perros](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), que se asemeja mucho a un escenario real de clasificación de imágenes.

## ✍️ Ejercicio: Aprendizaje por Transferencia

Veamos el aprendizaje por transferencia en acción en los siguientes cuadernos:

* [Aprendizaje por Transferencia - PyTorch](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb)
* [Aprendizaje por Transferencia - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb)

## Visualizando el Gato Adversarial

Una red neuronal pre-entrenada contiene diferentes patrones dentro de su *cerebro*, incluyendo nociones de **gato ideal** (así como perro ideal, cebra ideal, etc.). Sería interesante de alguna manera **visualizar esta imagen**. Sin embargo, no es sencillo, porque los patrones están distribuidos por todos los pesos de la red y también organizados en una estructura jerárquica.

Un enfoque que podemos tomar es comenzar con una imagen aleatoria y luego intentar usar la técnica de **optimización por descenso de gradiente** para ajustar esa imagen de tal manera que la red comience a pensar que es un gato.

![Bucle de Optimización de Imagen](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.es.png)

Sin embargo, si hacemos esto, obtendremos algo muy similar a un ruido aleatorio. Esto se debe a que *hay muchas formas de hacer que la red piense que la imagen de entrada es un gato*, incluyendo algunas que no tienen sentido visualmente. Aunque esas imágenes contienen muchos patrones típicos de un gato, no hay nada que las restrinja a ser visualmente distintivas.

Para mejorar el resultado, podemos agregar otro término a la función de pérdida, que se llama **pérdida de variación**. Es una métrica que muestra cuán similares son los píxeles vecinos de la imagen. Minimizar la pérdida de variación hace que la imagen sea más suave y elimina el ruido, revelando así patrones más visualmente atractivos. Aquí hay un ejemplo de tales imágenes "ideales", que son clasificadas como gato y como cebra con alta probabilidad:

![Gato Ideal](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.es.png) | ![Cebra Ideal](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.es.png)
-----|-----
 *Gato Ideal* | *Cebra Ideal*

Un enfoque similar puede utilizarse para realizar lo que se llama **ataques adversariales** en una red neuronal. Supongamos que queremos engañar a una red neuronal y hacer que un perro se vea como un gato. Si tomamos la imagen de un perro, que es reconocida por una red como un perro, podemos ajustarla un poco usando optimización por descenso de gradiente, hasta que la red comience a clasificarla como un gato:

![Imagen de un Perro](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.es.png) | ![Imagen de un perro clasificado como gato](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.es.png)
-----|-----
*Imagen original de un perro* | *Imagen de un perro clasificado como gato*

Consulta el código para reproducir los resultados anteriores en el siguiente cuaderno:

* [Gato Ideal y Adversarial - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb)
## Conclusión

Usando el aprendizaje por transferencia, puedes rápidamente armar un clasificador para una tarea de clasificación de objetos personalizada y lograr alta precisión. Puedes ver que las tareas más complejas que estamos resolviendo ahora requieren mayor poder computacional y no pueden resolverse fácilmente en la CPU. En la próxima unidad, intentaremos usar una implementación más liviana para entrenar el mismo modelo utilizando recursos computacionales más bajos, lo que resulta en una precisión ligeramente inferior.

## 🚀 Desafío

En los cuadernos adjuntos, hay notas al final sobre cómo el transferir conocimiento funciona mejor con datos de entrenamiento algo similares (quizás un nuevo tipo de animal). Realiza algunos experimentos con tipos de imágenes completamente nuevos para ver qué tan bien o mal funcionan tus modelos de transferencia de conocimiento.

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Revisión y Autoestudio

Lee [TrainingTricks.md](TrainingTricks.md) para profundizar tu conocimiento sobre algunas otras formas de entrenar tus modelos.

## [Tarea](lab/README.md)

En este laboratorio, utilizaremos un conjunto de datos de mascotas de la vida real [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) con 35 razas de gatos y perros, y construiremos un clasificador de aprendizaje por transferencia.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o mala interpretación que surja del uso de esta traducción.