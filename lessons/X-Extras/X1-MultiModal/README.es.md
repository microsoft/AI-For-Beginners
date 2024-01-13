# Redes multimodales

Tras el éxito de los modelos de transformadores para resolver tareas de PNL, se han aplicado arquitecturas iguales o similares a tareas de visión por computadora. Existe un interés creciente en construir modelos que *combinen* capacidades de visión y lenguaje natural. Uno de esos intentos lo realizó OpenAI y se llama CLIP y DALL.E.

## Preentrenamiento de imagen contrastiva (CLIP)

La idea principal de CLIP es poder comparar mensajes de texto con una imagen y determinar qué tan bien corresponde la imagen al mensaje.

![CLIP Architecture](images/clip-arch.png)

> *Imagen de [this blog post](https://openai.com/blog/clip/)*

El modelo se entrena con imágenes obtenidas de Internet y sus leyendas. Para cada lote, tomamos N pares de (imagen, texto) y los convertimos en algunas representaciones vectoriales I<sub>1</sub>,..., I<sub>N</sub> / T<sub> 1</sub>, ..., T<sub>N</sub>. Luego, esas representaciones se combinan. La función de pérdida se define para maximizar la similitud del coseno entre vectores correspondientes a un par (por ejemplo, I<sub>i</sub> y T<sub>i</sub>) y minimizar la similitud del coseno entre todos los demás pares. Ésa es la razón por la que este enfoque se llama **contrastivo**.

El modelo/biblioteca CLIP está disponible en [OpenAI GitHub](https://github.com/openai/CLIP). El enfoque se describe en [this blog post](https://openai.com/blog/clip/),y con más detalle en [this paper](https://arxiv.org/pdf/2103.00020.pdf).

Una vez que este modelo esté previamente entrenado, podemos darle un lote de imágenes y un lote de mensajes de texto, y devolverá el tensor con probabilidades. CLIP se puede utilizar para varias tareas:

**Clasificación de imágenes**

Supongamos que necesitamos clasificar imágenes entre, digamos, gatos, perros y humanos. En este caso, podemos darle al modelo una imagen y una serie de mensajes de texto: "*una imagen de un gato*", "*una imagen de un perro*", "*una imagen de un humano*". En el vector resultante de 3 probabilidades solo necesitamos seleccionar el índice con mayor valor.

![CLIP for Image Classification](images/clip-class.png)

> *Imagen de [this blog post](https://openai.com/blog/clip/)*

**Búsqueda de imágenes basada en texto**

También podemos hacer lo contrario. Si tenemos una colección de imágenes, podemos pasar esta colección al modelo y un mensaje de texto; esto nos dará la imagen que sea más similar a un mensaje determinado.

## ✍️ Ejemplo: [Using CLIP for Image Classification and Image Search](Clip.ipynb)

Abre el [Clip.ipynb](Clip.ipynb) cuaderno para ver CLIP en acción.

## Generación de imágenes con VQGAN+ CLIP

CLIP también se puede utilizar para **generar imágenes** a partir de un mensaje de texto. Para hacer esto, necesitamos un **modelo generador** que pueda generar imágenes basadas en alguna entrada vectorial. Uno de esos modelos se llama [VQGAN](https://compvis.github.io/taming-transformers/) (Vector-Quantized GAN).

Las principales ideas de VQGAN que lo diferencian del ordinario [GAN](../../4-ComputerVision/10-GANs/README.md) son los siguientes:
* Utilizar una arquitectura transformadora autorregresiva para generar una secuencia de partes visuales ricas en contexto que componen la imagen. Esas partes visuales, a su vez, las aprende [CNN](../../4-ComputerVision/07-ConvNets/README.md)
* Utilice un discriminador de subimagen que detecte si partes de la imagen son "reales" o "falsas" (a diferencia del enfoque de "todo o nada" en GAN tradicional).

Obtenga más información sobre VQGAN en el [Taming Transformers](https://compvis.github.io/taming-transformers/) sitio web.

Una de las diferencias importantes entre VQGAN y GAN tradicional es que este último puede producir una imagen decente a partir de cualquier vector de entrada, mientras que es probable que VQGAN produzca una imagen que no sea coherente. Por lo tanto, necesitamos guiar más el proceso de creación de imágenes, y eso se puede hacer usando CLIP.

![VQGAN+CLIP Architecture](images/vqgan.png)

Para generar una imagen correspondiente a un mensaje de texto, comenzamos con algún vector de codificación aleatorio que se pasa a través de VQGAN para producir una imagen. Luego se utiliza CLIP para producir una función de pérdida que muestra qué tan bien corresponde la imagen al mensaje de texto. El objetivo entonces es minimizar esta pérdida, utilizando la propagación hacia atrás para ajustar los parámetros del vector de entrada.

Una gran biblioteca que implementa VQGAN+CLIP es [Pixray](http://github.com/pixray/pixray) 

![Picture produced by Pixray](images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.png) |  ![Picture produced by pixray](images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.png) | ![Picture produced by Pixray](images/a_closeup_oil_portrait_of_old_male_teacher_of_math.png)
----|----|----
Imagen generada a partir del mensaje *un primer retrato en acuarela de un joven profesor de literatura con un libro* | Imagen generada a partir del mensaje *un primer retrato al óleo de una joven profesora de informática con una computadora* | Imagen generada a partir del mensaje *un primer retrato al óleo de un anciano profesor de matemáticas frente a la pizarra*

> Imágenes de la colección **Artificial Teachers** de [Dmitry Soshnikov](http://soshnikov.com)

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)

DALL-E is a version of GPT-3 trained to generate images from prompts. It has been trained with 12-billion parameters.

Unlike CLIP, DALL-E receives both text and image as a single stream of tokens for both images and text. Therefore, from multiple prompts, you can generate images based on the text.
### [DALL-E 2](https://openai.com/dall-e-2)
La principal diferencia entre DALL.E 1 y 2 es que genera imágenes y arte más realistas.

Ejemplos de generaciones de imágenes con DALL-E:
![Picture produced by Pixray](images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.png) |  ![Picture produced by pixray](images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.png) | ![Picture produced by Pixray](images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.png)
----|----|----
Imagen generada a partir del mensaje *un primer retrato en acuarela de un joven profesor de literatura con un libro* | Imagen generada a partir del mensaje *un primer retrato al óleo de una joven profesora de informática con una computadora* | Imagen generada a partir del mensaje *un primer retrato al óleo de un anciano profesor de matemáticas frente a la pizarra*

## Referencias

* Papel VQGAN: [Taming Transformers for High-Resolution Image Synthesis](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* Papel CLIP: [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/pdf/2103.00020.pdf)


