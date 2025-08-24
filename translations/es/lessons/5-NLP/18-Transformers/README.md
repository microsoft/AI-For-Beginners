<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7e617f0b8de85a43957a853aba09bfeb",
  "translation_date": "2025-08-24T10:17:30+00:00",
  "source_file": "lessons/5-NLP/18-Transformers/README.md",
  "language_code": "es"
}
-->
# Mecanismos de Atención y Transformadores

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/118)

Uno de los problemas más importantes en el ámbito de NLP es la **traducción automática**, una tarea esencial que sustenta herramientas como Google Translate. En esta sección, nos centraremos en la traducción automática o, más generalmente, en cualquier tarea de *secuencia a secuencia* (también llamada **transducción de oraciones**).

Con las RNNs, la tarea de secuencia a secuencia se implementa mediante dos redes recurrentes, donde una red, el **codificador**, comprime una secuencia de entrada en un estado oculto, mientras que otra red, el **decodificador**, despliega este estado oculto en un resultado traducido. Hay algunos problemas con este enfoque:

* El estado final de la red codificadora tiene dificultades para recordar el inicio de una oración, lo que provoca una baja calidad del modelo para oraciones largas.
* Todas las palabras en una secuencia tienen el mismo impacto en el resultado. Sin embargo, en la realidad, palabras específicas en la secuencia de entrada suelen tener más impacto en las salidas secuenciales que otras.

Los **mecanismos de atención** proporcionan un medio para ponderar el impacto contextual de cada vector de entrada en cada predicción de salida de la RNN. La forma en que se implementa es creando atajos entre los estados intermedios de la RNN de entrada y la RNN de salida. De esta manera, al generar el símbolo de salida y<sub>t</sub>, tomaremos en cuenta todos los estados ocultos de entrada h<sub>i</sub>, con diferentes coeficientes de peso α<sub>t,i</sub>.

![Imagen que muestra un modelo codificador/decodificador con una capa de atención aditiva](../../../../../lessons/5-NLP/18-Transformers/images/encoder-decoder-attention.png)

> El modelo codificador-decodificador con mecanismo de atención aditiva en [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf), citado de [este blog](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)

La matriz de atención {α<sub>i,j</sub>} representaría el grado en que ciertas palabras de entrada influyen en la generación de una palabra dada en la secuencia de salida. A continuación, se muestra un ejemplo de dicha matriz:

![Imagen que muestra una alineación de muestra encontrada por RNNsearch-50, tomada de Bahdanau - arviz.org](../../../../../lessons/5-NLP/18-Transformers/images/bahdanau-fig3.png)

> Figura de [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf) (Fig.3)

Los mecanismos de atención son responsables de gran parte del estado del arte actual o cercano al actual en NLP. Sin embargo, agregar atención aumenta significativamente el número de parámetros del modelo, lo que llevó a problemas de escalabilidad con las RNNs. Una restricción clave para escalar las RNNs es que la naturaleza recurrente de los modelos dificulta el procesamiento en lotes y la paralelización del entrenamiento. En una RNN, cada elemento de una secuencia necesita ser procesado en orden secuencial, lo que significa que no se puede paralelizar fácilmente.

![Codificador-Decodificador con Atención](../../../../../lessons/5-NLP/18-Transformers/images/EncDecAttention.gif)

> Figura del [Blog de Google](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)

La adopción de mecanismos de atención combinada con esta restricción llevó a la creación de los modelos transformadores, ahora estado del arte, que conocemos y usamos hoy en día, como BERT y Open-GPT3.

## Modelos Transformadores

Una de las ideas principales detrás de los transformadores es evitar la naturaleza secuencial de las RNNs y crear un modelo que sea paralelizable durante el entrenamiento. Esto se logra implementando dos ideas:

* codificación posicional
* uso del mecanismo de auto-atención para capturar patrones en lugar de RNNs (o CNNs) (por eso el artículo que introduce los transformadores se llama *[Attention is all you need](https://arxiv.org/abs/1706.03762)*)

### Codificación/Embebido Posicional

La idea de la codificación posicional es la siguiente:  
1. Al usar RNNs, la posición relativa de los tokens está representada por el número de pasos, y por lo tanto no necesita ser representada explícitamente.  
2. Sin embargo, una vez que cambiamos a atención, necesitamos conocer las posiciones relativas de los tokens dentro de una secuencia.  
3. Para obtener la codificación posicional, ampliamos nuestra secuencia de tokens con una secuencia de posiciones de tokens en la secuencia (es decir, una secuencia de números 0,1, ...).  
4. Luego mezclamos la posición del token con un vector de embebido del token. Para transformar la posición (entero) en un vector, podemos usar diferentes enfoques:

* Embebido entrenable, similar al embebido de tokens. Este es el enfoque que consideramos aquí. Aplicamos capas de embebido tanto a los tokens como a sus posiciones, lo que da como resultado vectores de embebido de las mismas dimensiones, que luego sumamos.
* Función de codificación posicional fija, como se propone en el artículo original.

<img src="images/pos-embedding.png" width="50%"/>

> Imagen del autor

El resultado que obtenemos con el embebido posicional incluye tanto el token original como su posición dentro de una secuencia.

### Auto-Atención Multi-Cabezal

A continuación, necesitamos capturar algunos patrones dentro de nuestra secuencia. Para hacerlo, los transformadores utilizan un mecanismo de **auto-atención**, que es esencialmente atención aplicada a la misma secuencia como entrada y salida. Aplicar auto-atención nos permite tomar en cuenta el **contexto** dentro de la oración y ver qué palabras están interrelacionadas. Por ejemplo, nos permite ver qué palabras son referidas por correferencias, como *it*, y también tomar el contexto en cuenta:

![](../../../../../lessons/5-NLP/18-Transformers/images/CoreferenceResolution.png)

> Imagen del [Blog de Google](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)

En los transformadores, usamos **atención multi-cabezal** para darle a la red la capacidad de capturar varios tipos diferentes de dependencias, por ejemplo, relaciones de palabras a largo plazo frente a corto plazo, correferencia frente a algo más, etc.

[Notebook de TensorFlow](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb) contiene más detalles sobre la implementación de capas de transformadores.

### Atención Codificador-Decodificador

En los transformadores, la atención se utiliza en dos lugares:

* Para capturar patrones dentro del texto de entrada utilizando auto-atención.
* Para realizar la traducción de secuencias: es la capa de atención entre el codificador y el decodificador.

La atención codificador-decodificador es muy similar al mecanismo de atención utilizado en las RNNs, como se describió al inicio de esta sección. Este diagrama animado explica el papel de la atención codificador-decodificador.

![GIF animado que muestra cómo se realizan las evaluaciones en los modelos transformadores.](../../../../../lessons/5-NLP/18-Transformers/images/transformer-animated-explanation.gif)

Dado que cada posición de entrada se mapea independientemente a cada posición de salida, los transformadores pueden paralelizar mejor que las RNNs, lo que permite modelos de lenguaje mucho más grandes y expresivos. Cada cabeza de atención puede usarse para aprender diferentes relaciones entre palabras que mejoran las tareas de procesamiento de lenguaje natural.

## BERT

**BERT** (Representaciones de Codificador Bidireccional de Transformadores) es una red transformadora muy grande con múltiples capas: 12 capas para *BERT-base* y 24 para *BERT-large*. El modelo se preentrena primero en un gran corpus de datos de texto (Wikipedia + libros) utilizando entrenamiento no supervisado (predicción de palabras enmascaradas en una oración). Durante el preentrenamiento, el modelo absorbe niveles significativos de comprensión del lenguaje que luego pueden aprovecharse con otros conjuntos de datos mediante ajuste fino. Este proceso se llama **aprendizaje por transferencia**.

![imagen de http://jalammar.github.io/illustrated-bert/](../../../../../lessons/5-NLP/18-Transformers/images/jalammarBERT-language-modeling-masked-lm.png)

> Imagen [fuente](http://jalammar.github.io/illustrated-bert/)

## ✍️ Ejercicios: Transformadores

Continúa tu aprendizaje en los siguientes notebooks:

* [Transformadores en PyTorch](../../../../../lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb)
* [Transformadores en TensorFlow](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb)

## Conclusión

En esta lección aprendiste sobre Transformadores y Mecanismos de Atención, herramientas esenciales en el conjunto de herramientas de NLP. Existen muchas variaciones de arquitecturas de transformadores, incluyendo BERT, DistilBERT, BigBird, OpenGPT3 y más, que pueden ajustarse. El paquete [HuggingFace](https://github.com/huggingface/) proporciona un repositorio para entrenar muchas de estas arquitecturas con PyTorch y TensorFlow.

## 🚀 Desafío

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/218)

## Revisión y Estudio Autónomo

* [Publicación de blog](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/), que explica el clásico artículo [Attention is all you need](https://arxiv.org/abs/1706.03762) sobre transformadores.
* [Una serie de publicaciones de blog](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452) sobre transformadores, que explican la arquitectura en detalle.

## [Tarea](assignment.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.