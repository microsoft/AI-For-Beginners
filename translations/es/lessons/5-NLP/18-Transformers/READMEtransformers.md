# Mecanismos de Atención y Transformadores

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/118)

Uno de los problemas más importantes en el dominio del PLN es la **traducción automática**, una tarea esencial que subyace a herramientas como Google Translate. En esta sección, nos enfocaremos en la traducción automática, o, de manera más general, en cualquier tarea de *secuencia a secuencia* (que también se llama **transducción de oraciones**).

Con las RNN, la secuencia a secuencia se implementa mediante dos redes recurrentes, donde una red, el **codificador**, colapsa una secuencia de entrada en un estado oculto, mientras que otra red, el **decodificador**, despliega este estado oculto en un resultado traducido. Hay un par de problemas con este enfoque:

* El estado final de la red del codificador tiene dificultades para recordar el comienzo de una oración, lo que provoca una mala calidad del modelo para oraciones largas.
* Todas las palabras en una secuencia tienen el mismo impacto en el resultado. Sin embargo, en la realidad, ciertas palabras en la secuencia de entrada a menudo tienen más impacto en las salidas secuenciales que otras.

**Los Mecanismos de Atención** proporcionan un medio para ponderar el impacto contextual de cada vector de entrada en cada predicción de salida de la RNN. La forma en que se implementa es creando atajos entre los estados intermedios de la RNN de entrada y la RNN de salida. De esta manera, al generar el símbolo de salida y<sub>t</sub>, tomaremos en cuenta todos los estados ocultos de entrada h<sub>i</sub>, con diferentes coeficientes de peso α<sub>t,i</sub>.

![Imagen que muestra un modelo de codificador/decodificador con una capa de atención aditiva](../../../../../translated_images/encoder-decoder-attention.7a726296894fb567aa2898c94b17b3289087f6705c11907df8301df9e5eeb3de.es.png)

> El modelo codificador-decodificador con mecanismo de atención aditiva en [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf), citado de [esta publicación de blog](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)

La matriz de atención {α<sub>i,j</sub>} representaría el grado en que ciertas palabras de entrada juegan un papel en la generación de una palabra dada en la secuencia de salida. A continuación se muestra un ejemplo de tal matriz:

![Imagen que muestra una alineación de muestra encontrada por RNNsearch-50, tomada de Bahdanau - arviz.org](../../../../../translated_images/bahdanau-fig3.09ba2d37f202a6af11de6c82d2d197830ba5f4528d9ea430eb65fd3a75065973.es.png)

> Figura de [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf) (Fig.3)

Los mecanismos de atención son responsables de gran parte del estado actual o casi actual de la técnica en PLN. Sin embargo, añadir atención aumenta considerablemente el número de parámetros del modelo, lo que llevó a problemas de escalabilidad con las RNN. Una restricción clave de la escalabilidad de las RNN es que la naturaleza recurrente de los modelos hace que sea un desafío agrupar y paralelizar el entrenamiento. En una RNN, cada elemento de una secuencia necesita ser procesado en orden secuencial, lo que significa que no se puede paralelizar fácilmente.

![Codificador Decodificador con Atención](../../../../../lessons/5-NLP/18-Transformers/images/EncDecAttention.gif)

> Figura de [Google's Blog](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)

La adopción de mecanismos de atención combinados con esta restricción llevó a la creación de los ahora modelos transformadores de última generación que conocemos y utilizamos hoy, como BERT y Open-GPT3.

## Modelos Transformadores

Una de las ideas principales detrás de los transformadores es evitar la naturaleza secuencial de las RNN y crear un modelo que sea paralelizable durante el entrenamiento. Esto se logra implementando dos ideas:

* codificación posicional
* uso de un mecanismo de autoatención para capturar patrones en lugar de RNNs (o CNNs) (por eso el artículo que introduce los transformadores se llama *[Attention is all you need](https://arxiv.org/abs/1706.03762)*)

### Codificación/Embebido Posicional

La idea de la codificación posicional es la siguiente. 
1. Al usar RNNs, la posición relativa de los tokens está representada por el número de pasos, y por lo tanto no necesita ser representada explícitamente. 
2. Sin embargo, una vez que cambiamos a atención, necesitamos conocer las posiciones relativas de los tokens dentro de una secuencia. 
3. Para obtener la codificación posicional, aumentamos nuestra secuencia de tokens con una secuencia de posiciones de tokens en la secuencia (es decir, una secuencia de números 0,1, ...).
4. Luego mezclamos la posición del token con un vector de embebido del token. Para transformar la posición (entero) en un vector, podemos usar diferentes enfoques:

* Embebido entrenable, similar al embebido de tokens. Este es el enfoque que consideramos aquí. Aplicamos capas de embebido sobre ambos, los tokens y sus posiciones, resultando en vectores de embebido de las mismas dimensiones, que luego sumamos.
* Función de codificación de posición fija, como se propuso en el artículo original.

<img src="images/pos-embedding.png" width="50%"/>

> Imagen del autor

El resultado que obtenemos con el embebido posicional integra tanto el token original como su posición dentro de una secuencia.

### Autoatención Multi-Cabeza

A continuación, necesitamos capturar algunos patrones dentro de nuestra secuencia. Para hacer esto, los transformadores utilizan un mecanismo de **autoatención**, que es esencialmente atención aplicada a la misma secuencia como entrada y salida. Aplicar autoatención nos permite tener en cuenta el **contexto** dentro de la oración y ver qué palabras están interrelacionadas. Por ejemplo, nos permite ver qué palabras son referidas por co-referencias, como *ello*, y también tener en cuenta el contexto:

![](../../../../../translated_images/CoreferenceResolution.861924d6d384a7d68d8d0039d06a71a151f18a796b8b1330239d3590bd4947eb.es.png)

> Imagen del [Blog de Google](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)

En los transformadores, utilizamos **Atención Multi-Cabeza** para darle al modelo la capacidad de capturar varios tipos diferentes de dependencias, por ejemplo, relaciones de palabras a largo plazo frente a corto plazo, co-referencia frente a algo más, etc.

[Notebook de TensorFlow](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb) contiene más detalles sobre la implementación de las capas transformadoras.

### Atención Codificador-Decodificador

En los transformadores, la atención se utiliza en dos lugares:

* Para capturar patrones dentro del texto de entrada utilizando autoatención
* Para realizar traducción de secuencias - es la capa de atención entre el codificador y el decodificador.

La atención codificador-decodificador es muy similar al mecanismo de atención utilizado en las RNN, como se describió al principio de esta sección. Este diagrama animado explica el papel de la atención codificador-decodificador.

![GIF animado que muestra cómo se realizan las evaluaciones en modelos transformadores.](../../../../../lessons/5-NLP/18-Transformers/images/transformer-animated-explanation.gif)

Dado que cada posición de entrada se mapea independientemente a cada posición de salida, los transformadores pueden paralelizarse mejor que las RNN, lo que permite modelos de lenguaje mucho más grandes y expresivos. Cada cabeza de atención puede ser utilizada para aprender diferentes relaciones entre palabras que mejoran las tareas de Procesamiento de Lenguaje Natural posteriores.

## BERT

**BERT** (Representaciones de Codificador Bidireccional de Transformadores) es una red transformadora de múltiples capas muy grande con 12 capas para *BERT-base*, y 24 para *BERT-large*. El modelo se preentrena primero en un gran corpus de datos textuales (WikiPedia + libros) utilizando entrenamiento no supervisado (prediciendo palabras enmascaradas en una oración). Durante el preentrenamiento, el modelo absorbe niveles significativos de comprensión del lenguaje que luego pueden ser aprovechados con otros conjuntos de datos utilizando ajuste fino. Este proceso se llama **aprendizaje por transferencia**.

![imagen de http://jalammar.github.io/illustrated-bert/](../../../../../translated_images/jalammarBERT-language-modeling-masked-lm.34f113ea5fec4362e39ee4381aab7cad06b5465a0b5f053a0f2aa05fbe14e746.es.png)

> Imagen [fuente](http://jalammar.github.io/illustrated-bert/)

## ✍️ Ejercicios: Transformadores

Continúa tu aprendizaje en los siguientes cuadernos:

* [Transformadores en PyTorch](../../../../../lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb)
* [Transformadores en TensorFlow](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb)

## Conclusión

En esta lección aprendiste sobre Transformadores y Mecanismos de Atención, herramientas esenciales en la caja de herramientas del PLN. Hay muchas variaciones de arquitecturas de Transformadores, incluyendo BERT, DistilBERT, BigBird, OpenGPT3 y más que pueden ser ajustadas. El [paquete HuggingFace](https://github.com/huggingface/) proporciona un repositorio para entrenar muchas de estas arquitecturas tanto con PyTorch como con TensorFlow.

## 🚀 Desafío

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/218)

## Revisión y Autoestudio

* [Publicación de blog](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/), que explica el clásico artículo [Attention is all you need](https://arxiv.org/abs/1706.03762) sobre transformadores.
* [Una serie de publicaciones de blog](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452) sobre transformadores, que explican la arquitectura en detalle.

## [Asignación](assignment.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.