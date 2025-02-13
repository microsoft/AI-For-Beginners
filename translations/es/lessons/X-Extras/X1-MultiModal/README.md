# Redes Neuronales Multi-Modales

Tras el éxito de los modelos de transformadores para resolver tareas de procesamiento de lenguaje natural (NLP), se han aplicado arquitecturas similares a tareas de visión por computadora. Hay un creciente interés en construir modelos que *combinan* capacidades de visión y lenguaje natural. Uno de estos intentos fue realizado por OpenAI, y se llama CLIP y DALL.E.

## Pre-entrenamiento de Imágenes Contrastivas (CLIP)

La idea principal de CLIP es poder comparar indicaciones de texto con una imagen y determinar qué tan bien la imagen corresponde a la indicación.

![Arquitectura CLIP](../../../../../translated_images/clip-arch.b3dbf20b4e8ed8be1c38e2bc6100fd3cc257c33cda4692b301be91f791b13ea7.es.png)

> *Imagen del [este post del blog](https://openai.com/blog/clip/)*

El modelo se entrena con imágenes obtenidas de Internet y sus descripciones. Para cada lote, tomamos N pares de (imagen, texto) y los convertimos en representaciones vectoriales. Esas representaciones se emparejan entre sí. La función de pérdida se define para maximizar la similitud coseno entre los vectores correspondientes a un par (por ejemplo, I y T), y minimizar la similitud coseno entre todos los demás pares. Esa es la razón por la cual este enfoque se llama **contrastivo**.

El modelo/biblioteca CLIP está disponible en [OpenAI GitHub](https://github.com/openai/CLIP). El enfoque se describe en [este post del blog](https://openai.com/blog/clip/), y con más detalle en [este artículo](https://arxiv.org/pdf/2103.00020.pdf).

Una vez que este modelo está pre-entrenado, podemos darle un lote de imágenes y un lote de indicaciones de texto, y devolverá un tensor con probabilidades. CLIP se puede utilizar para varias tareas:

**Clasificación de Imágenes**

Supongamos que necesitamos clasificar imágenes entre, digamos, gatos, perros y humanos. En este caso, podemos darle al modelo una imagen y una serie de indicaciones de texto: "*una imagen de un gato*", "*una imagen de un perro*", "*una imagen de un humano*". En el vector resultante de 3 probabilidades, solo necesitamos seleccionar el índice con el valor más alto.

![CLIP para Clasificación de Imágenes](../../../../../translated_images/clip-class.3af42ef0b2b19369a633df5f20ddf4f5a01d6c8ffa181e9d3a0572c19f919f72.es.png)

> *Imagen del [este post del blog](https://openai.com/blog/clip/)*

**Búsqueda de Imágenes Basada en Texto**

También podemos hacer lo opuesto. Si tenemos una colección de imágenes, podemos pasar esta colección al modelo y una indicación de texto; esto nos dará la imagen que es más similar a la indicación dada.

## ✍️ Ejemplo: [Usando CLIP para Clasificación de Imágenes y Búsqueda de Imágenes](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

Abre el [Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb) notebook para ver CLIP en acción.

## Generación de Imágenes con VQGAN+ CLIP

CLIP también se puede utilizar para **generación de imágenes** a partir de una indicación de texto. Para hacer esto, necesitamos un **modelo generador** que pueda generar imágenes basadas en alguna entrada vectorial. Uno de estos modelos se llama [VQGAN](https://compvis.github.io/taming-transformers/) (Generador Antagónico Cuantificado por Vectores).

Las principales ideas de VQGAN que lo diferencian de un [GAN](../../4-ComputerVision/10-GANs/README.md) ordinario son las siguientes:
* Utilizar una arquitectura de transformador autorregresiva para generar una secuencia de partes visuales ricas en contexto que componen la imagen. Esas partes visuales son a su vez aprendidas por [CNN](../../4-ComputerVision/07-ConvNets/README.md).
* Usar un discriminador de sub-imágenes que detecte si partes de la imagen son "reales" o "falsas" (a diferencia del enfoque "todo o nada" en un GAN tradicional).

Aprende más sobre VQGAN en el sitio web de [Taming Transformers](https://compvis.github.io/taming-transformers/).

Una de las diferencias importantes entre VQGAN y un GAN tradicional es que este último puede producir una imagen decente a partir de cualquier vector de entrada, mientras que VQGAN es probable que produzca una imagen que no sea coherente. Por lo tanto, necesitamos guiar aún más el proceso de creación de la imagen, y eso se puede hacer usando CLIP.

![Arquitectura VQGAN+CLIP](../../../../../translated_images/vqgan.5027fe05051dfa3101950cfa930303f66e6478b9bd273e83766731796e462d9b.es.png)

Para generar una imagen correspondiente a una indicación de texto, comenzamos con algún vector de codificación aleatorio que se pasa a través de VQGAN para producir una imagen. Luego, se utiliza CLIP para producir una función de pérdida que muestra qué tan bien la imagen corresponde a la indicación de texto. El objetivo es minimizar esta pérdida, utilizando retropropagación para ajustar los parámetros del vector de entrada.

Una gran biblioteca que implementa VQGAN+CLIP es [Pixray](http://github.com/pixray/pixray).

![Imagen producida por Pixray](../../../../../translated_images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.2384968e9db8a0d09dc96de938b9f95bde8a7e1c721f48f286a7795bf16d56c7.es.png) |  ![Imagen producida por Pixray](../../../../../translated_images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.e0b6495f210a439077e1c32cc8afdf714e634fe24dc78dc5aa45fd2f560b0ed5.es.png) | ![Imagen producida por Pixray](../../../../../translated_images/a_closeup_oil_portrait_of_old_male_teacher_of_math.5362e67aa7fc2683b9d36a613b364deb7454760cd39205623fc1e3938fa133c0.es.png)
----|----|----
Imagen generada a partir de la indicación *un primer plano de un retrato en acuarela de un joven profesor de literatura con un libro* | Imagen generada a partir de la indicación *un primer plano de un retrato al óleo de una joven profesora de ciencias de la computación con una computadora* | Imagen generada a partir de la indicación *un primer plano de un retrato al óleo de un viejo profesor de matemáticas frente a una pizarra*

> Imágenes de la colección **Maestros Artificiales** por [Dmitry Soshnikov](http://soshnikov.com).

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-E es una versión de GPT-3 entrenada para generar imágenes a partir de indicaciones. Ha sido entrenada con 12 mil millones de parámetros.

A diferencia de CLIP, DALL-E recibe tanto texto como imagen como un único flujo de tokens para imágenes y texto. Por lo tanto, a partir de múltiples indicaciones, puedes generar imágenes basadas en el texto.

### [DALL-E 2](https://openai.com/dall-e-2)
La principal diferencia entre DALL-E 1 y 2 es que genera imágenes y arte más realistas.

Ejemplos de generación de imágenes con DALL-E:
![Imagen producida por Pixray](../../../../../translated_images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.6c235e8271d9ed10ce985d86aeb241a58518958647973af136912116b9518fce.es.png) |  ![Imagen producida por Pixray](../../../../../translated_images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.f21dc4166340b6c8b4d1cb57efd1e22127407f9b28c9ac7afe11344065369e64.es.png) | ![Imagen producida por Pixray](../../../../../translated_images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.d331c2dfbdc3f7c46aa65c0809066f5e7ed4b49609cd259852e760df21051e4a.es.png)
----|----|----
Imagen generada a partir de la indicación *un primer plano de un retrato en acuarela de un joven profesor de literatura con un libro* | Imagen generada a partir de la indicación *un primer plano de un retrato al óleo de una joven profesora de ciencias de la computación con una computadora* | Imagen generada a partir de la indicación *un primer plano de un retrato al óleo de un viejo profesor de matemáticas frente a una pizarra* 

## Referencias

* Artículo de VQGAN: [Taming Transformers for High-Resolution Image Synthesis](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* Artículo de CLIP: [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/pdf/2103.00020.pdf)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No somos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.