# Embeddings

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/114)

Cuando entrenamos clasificadores basados en BoW o TF/IDF, trabajamos con vectores de bolsa de palabras de alta dimensión con una longitud de `vocab_size`, y estábamos convirtiendo explícitamente vectores de representación posicional de baja dimensión en una representación dispersa de one-hot. Sin embargo, esta representación one-hot no es eficiente en términos de memoria. Además, cada palabra se trata de manera independiente, es decir, los vectores codificados one-hot no expresan ninguna similitud semántica entre las palabras.

La idea de **embedding** es representar palabras mediante vectores densos de menor dimensión, que de alguna manera reflejan el significado semántico de una palabra. Más adelante discutiremos cómo construir embeddings significativos, pero por ahora pensemos en los embeddings como una forma de reducir la dimensionalidad de un vector de palabras.

Así que, la capa de embedding tomaría una palabra como entrada y produciría un vector de salida de tamaño especificado `embedding_size`. En cierto sentido, es muy similar a una capa `Linear`, pero en lugar de tomar un vector codificado one-hot, podrá tomar un número de palabra como entrada, lo que nos permite evitar la creación de grandes vectores codificados one-hot.

Al usar una capa de embedding como primera capa en nuestra red de clasificador, podemos cambiar de un modelo de bolsa de palabras a un modelo de **embedding bag**, donde primero convertimos cada palabra en nuestro texto en su correspondiente embedding y luego calculamos alguna función agregada sobre todos esos embeddings, como `sum`, `average` o `max`.

![Imagen que muestra un clasificador de embedding para cinco palabras en secuencia.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.it.png)

> Imagen del autor

## ✍️ Ejercicios: Embeddings

Continúa tu aprendizaje en los siguientes cuadernos:
* [Embeddings con PyTorch](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb)
* [Embeddings TensorFlow](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)

## Embeddings Semánticos: Word2Vec

Mientras que la capa de embedding aprendió a mapear palabras a representaciones vectoriales, esta representación no necesariamente tenía mucho significado semántico. Sería ideal aprender una representación vectorial de tal manera que palabras similares o sinónimos correspondan a vectores que están cerca unos de otros en términos de alguna distancia vectorial (por ejemplo, distancia euclidiana).

Para lograrlo, necesitamos preentrenar nuestro modelo de embedding en una gran colección de texto de una manera específica. Una forma de entrenar embeddings semánticos se llama [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Se basa en dos arquitecturas principales que se utilizan para producir una representación distribuida de palabras:

 - **Bolsa de palabras continua** (CBoW) — en esta arquitectura, entrenamos el modelo para predecir una palabra a partir del contexto circundante. Dado el ngrama $(W_{-2},W_{-1},W_0,W_1,W_2)$, el objetivo del modelo es predecir $W_0$ a partir de $(W_{-2},W_{-1},W_1,W_2)$.
 - **Skip-gram continuo** es lo opuesto a CBoW. El modelo utiliza una ventana de palabras de contexto circundante para predecir la palabra actual.

CBoW es más rápido, mientras que skip-gram es más lento, pero hace un mejor trabajo representando palabras poco frecuentes.

![Imagen que muestra ambos algoritmos CBoW y Skip-Gram para convertir palabras en vectores.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.it.png)

> Imagen de [este artículo](https://arxiv.org/pdf/1301.3781.pdf)

Los embeddings preentrenados de Word2Vec (así como otros modelos similares, como GloVe) también se pueden usar en lugar de la capa de embedding en redes neuronales. Sin embargo, necesitamos lidiar con los vocabularios, porque el vocabulario utilizado para preentrenar Word2Vec/GloVe probablemente difiera del vocabulario en nuestro corpus de texto. Echa un vistazo a los cuadernos anteriores para ver cómo se puede resolver este problema.

## Embeddings Contextuales

Una limitación clave de las representaciones de embedding preentrenadas tradicionales como Word2Vec es el problema de la desambiguación del sentido de la palabra. Aunque los embeddings preentrenados pueden capturar parte del significado de las palabras en contexto, cada posible significado de una palabra se codifica en el mismo embedding. Esto puede causar problemas en modelos posteriores, ya que muchas palabras, como la palabra 'play', tienen diferentes significados dependiendo del contexto en el que se utilizan.

Por ejemplo, la palabra 'play' en estas dos oraciones diferentes tiene un significado bastante distinto:

- Fui a una **obra** en el teatro.
- John quiere **jugar** con sus amigos.

Los embeddings preentrenados anteriores representan ambos significados de la palabra 'play' en el mismo embedding. Para superar esta limitación, necesitamos construir embeddings basados en un **modelo de lenguaje**, que se entrena en un gran corpus de texto y *sabe* cómo se pueden combinar las palabras en diferentes contextos. Discutir los embeddings contextuales está fuera del alcance de este tutorial, pero volveremos a ellos al hablar sobre modelos de lenguaje más adelante en el curso.

## Conclusión

En esta lección, descubriste cómo construir y usar capas de embedding en TensorFlow y Pytorch para reflejar mejor los significados semánticos de las palabras.

## 🚀 Desafío

Word2Vec se ha utilizado para algunas aplicaciones interesantes, incluyendo la generación de letras de canciones y poesía. Echa un vistazo a [este artículo](https://www.politetype.com/blog/word2vec-color-poems) que explica cómo el autor utilizó Word2Vec para generar poesía. También mira [este video de Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) para descubrir una explicación diferente de esta técnica. Luego intenta aplicar estas técnicas a tu propio corpus de texto, quizás obtenido de Kaggle.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/214)

## Revisión y Autoestudio

Lee este artículo sobre Word2Vec: [Estimación Eficiente de Representaciones de Palabras en Espacio Vectorial](https://arxiv.org/pdf/1301.3781.pdf)

## [Asignación: Cuadernos](assignment.md)

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.