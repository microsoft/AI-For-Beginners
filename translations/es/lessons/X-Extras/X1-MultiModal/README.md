# Redes Multi-Modales

Tras el éxito de los modelos transformadores para resolver tareas de procesamiento de lenguaje natural (NLP), se han aplicado arquitecturas similares a tareas de visión por computadora. Existe un creciente interés en construir modelos que *combinen* capacidades de visión y lenguaje natural. Uno de estos intentos fue realizado por OpenAI, y se llama CLIP y DALL.E.

## Preentrenamiento Contrastivo de Imágenes (CLIP)

La idea principal de CLIP es poder comparar indicaciones de texto con una imagen y determinar qué tan bien la imagen corresponde a la indicación.

![Arquitectura CLIP](../../../../../lessons/X-Extras/X1-MultiModal/images/clip-arch.png)

> *Imagen tomada de [este artículo](https://openai.com/blog/clip/)*

El modelo se entrena con imágenes obtenidas de Internet y sus subtítulos. Para cada lote, tomamos N pares de (imagen, texto) y los convertimos en representaciones vectoriales I, ..., I / T, ..., T. Estas representaciones se emparejan entre sí. La función de pérdida se define para maximizar la similitud coseno entre los vectores correspondientes a un par (por ejemplo, I y T) y minimizar la similitud coseno entre todos los demás pares. Por esta razón, este enfoque se llama **contrastivo**.

El modelo/biblioteca CLIP está disponible en [GitHub de OpenAI](https://github.com/openai/CLIP). El enfoque se describe en [este artículo](https://openai.com/blog/clip/) y con más detalle en [este documento](https://arxiv.org/pdf/2103.00020.pdf).

Una vez que este modelo está preentrenado, podemos darle un lote de imágenes y un lote de indicaciones de texto, y lo que devolverá será un tensor con probabilidades. CLIP puede usarse para varias tareas:

**Clasificación de Imágenes**

Supongamos que necesitamos clasificar imágenes entre, por ejemplo, gatos, perros y humanos. En este caso, podemos darle al modelo una imagen y una serie de indicaciones de texto: "*una foto de un gato*", "*una foto de un perro*", "*una foto de un humano*". En el vector resultante de 3 probabilidades, solo necesitamos seleccionar el índice con el valor más alto.

![CLIP para Clasificación de Imágenes](../../../../../lessons/X-Extras/X1-MultiModal/images/clip-class.png)

> *Imagen tomada de [este artículo](https://openai.com/blog/clip/)*

**Búsqueda de Imágenes Basada en Texto**

También podemos hacer lo contrario. Si tenemos una colección de imágenes, podemos pasar esta colección al modelo y una indicación de texto; esto nos dará la imagen que sea más similar a la indicación dada.

## ✍️ Ejemplo: [Usando CLIP para Clasificación de Imágenes y Búsqueda de Imágenes](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

Abre el cuaderno [Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb) para ver CLIP en acción.

## Generación de Imágenes con VQGAN+CLIP

CLIP también puede usarse para **generación de imágenes** a partir de una indicación de texto. Para hacerlo, necesitamos un **modelo generador** que sea capaz de generar imágenes basadas en alguna entrada vectorial. Uno de estos modelos se llama [VQGAN](https://compvis.github.io/taming-transformers/) (GAN Cuantificado por Vectores).

Las ideas principales de VQGAN que lo diferencian de un [GAN](../../4-ComputerVision/10-GANs/README.md) ordinario son las siguientes:
* Usar una arquitectura transformadora autorregresiva para generar una secuencia de partes visuales contextualmente ricas que componen la imagen. Estas partes visuales, a su vez, son aprendidas por [CNN](../../4-ComputerVision/07-ConvNets/README.md).
* Usar un discriminador de sub-imágenes que detecta si las partes de la imagen son "reales" o "falsas" (a diferencia del enfoque "todo o nada" en los GAN tradicionales).

Aprende más sobre VQGAN en el sitio web [Taming Transformers](https://compvis.github.io/taming-transformers/).

Una de las diferencias importantes entre VQGAN y los GAN tradicionales es que estos últimos pueden producir una imagen decente a partir de cualquier vector de entrada, mientras que VQGAN probablemente produzca una imagen incoherente. Por lo tanto, necesitamos guiar aún más el proceso de creación de imágenes, y eso puede hacerse usando CLIP.

![Arquitectura VQGAN+CLIP](../../../../../lessons/X-Extras/X1-MultiModal/images/vqgan.png)

Para generar una imagen que corresponda a una indicación de texto, comenzamos con algún vector de codificación aleatorio que se pasa a través de VQGAN para producir una imagen. Luego, CLIP se utiliza para producir una función de pérdida que muestra qué tan bien la imagen corresponde a la indicación de texto. El objetivo es minimizar esta pérdida, utilizando retropropagación para ajustar los parámetros del vector de entrada.

Una excelente biblioteca que implementa VQGAN+CLIP es [Pixray](http://github.com/pixray/pixray).

![Imagen generada por Pixray](../../../../../lessons/X-Extras/X1-MultiModal/images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.png) |  ![Imagen generada por Pixray](../../../../../lessons/X-Extras/X1-MultiModal/images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.png) | ![Imagen generada por Pixray](../../../../../lessons/X-Extras/X1-MultiModal/images/a_closeup_oil_portrait_of_old_male_teacher_of_math.png)
----|----|----
Imagen generada con la indicación *un retrato en acuarela de cerca de un joven profesor de literatura con un libro* | Imagen generada con la indicación *un retrato al óleo de cerca de una joven profesora de informática con una computadora* | Imagen generada con la indicación *un retrato al óleo de cerca de un viejo profesor de matemáticas frente a un pizarrón*

> Imágenes de la colección **Artificial Teachers** por [Dmitry Soshnikov](http://soshnikov.com)

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-E es una versión de GPT-3 entrenada para generar imágenes a partir de indicaciones. Ha sido entrenada con 12 mil millones de parámetros.

A diferencia de CLIP, DALL-E recibe tanto texto como imagen como un único flujo de tokens para ambos. Por lo tanto, a partir de múltiples indicaciones, puedes generar imágenes basadas en el texto.

### [DALL-E 2](https://openai.com/dall-e-2)
La principal diferencia entre DALL-E 1 y 2 es que este último genera imágenes y arte más realistas.

Ejemplos de generación de imágenes con DALL-E:
![Imagen generada por DALL-E](../../../../../lessons/X-Extras/X1-MultiModal/images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.png) |  ![Imagen generada por DALL-E](../../../../../lessons/X-Extras/X1-MultiModal/images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.png) | ![Imagen generada por DALL-E](../../../../../lessons/X-Extras/X1-MultiModal/images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.png)
----|----|----
Imagen generada con la indicación *un retrato en acuarela de cerca de un joven profesor de literatura con un libro* | Imagen generada con la indicación *un retrato al óleo de cerca de una joven profesora de informática con una computadora* | Imagen generada con la indicación *un retrato al óleo de cerca de un viejo profesor de matemáticas frente a un pizarrón*

## Referencias

* Documento de VQGAN: [Taming Transformers for High-Resolution Image Synthesis](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* Documento de CLIP: [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/pdf/2103.00020.pdf)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.