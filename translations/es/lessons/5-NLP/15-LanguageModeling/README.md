# Modelado de Lenguaje

Las incrustaciones semánticas, como Word2Vec y GloVe, son en realidad un primer paso hacia el **modelado de lenguaje**: crear modelos que de alguna manera *entiendan* (o *representen*) la naturaleza del lenguaje.

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

La idea principal detrás del modelado de lenguaje es entrenarlos en conjuntos de datos no etiquetados de manera no supervisada. Esto es importante porque tenemos enormes cantidades de texto no etiquetado disponible, mientras que la cantidad de texto etiquetado siempre estará limitada por el esfuerzo que podamos dedicar a etiquetar. Más a menudo, podemos construir modelos de lenguaje que puedan **predecir palabras faltantes** en el texto, porque es fácil enmascarar una palabra aleatoria en el texto y usarla como una muestra de entrenamiento.

## Entrenamiento de Incrustaciones

En nuestros ejemplos anteriores, utilizamos incrustaciones semánticas preentrenadas, pero es interesante ver cómo se pueden entrenar esas incrustaciones. Hay varias ideas posibles que se pueden utilizar:

* Modelado de lenguaje **N-Gram**, cuando predecimos un token observando N tokens anteriores (N-gram)
* **Bolsa de Palabras Continua** (CBoW), cuando predecimos el token del medio $W_0$ en una secuencia de tokens $W_{-N}$, ..., $W_N$.
* **Skip-gram**, donde predecimos un conjunto de tokens vecinos {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} a partir del token del medio $W_0$.

![imagen del artículo sobre la conversión de palabras a vectores](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.es.png)

> Imagen de [este artículo](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Notebooks de Ejemplo: Entrenamiento del modelo CBoW

Continúa tu aprendizaje en los siguientes notebooks:

* [Entrenamiento de CBoW Word2Vec con TensorFlow](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [Entrenamiento de CBoW Word2Vec con PyTorch](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Conclusión

En la lección anterior hemos visto que las incrustaciones de palabras funcionan como magia. Ahora sabemos que entrenar incrustaciones de palabras no es una tarea muy compleja, y deberíamos ser capaces de entrenar nuestras propias incrustaciones de palabras para texto específico de dominio si es necesario.

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Revisión y Autoestudio

* [Tutorial oficial de PyTorch sobre Modelado de Lenguaje](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Tutorial oficial de TensorFlow sobre el entrenamiento del modelo Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* Usar el marco **gensim** para entrenar las incrustaciones más comúnmente utilizadas en unas pocas líneas de código se describe [en esta documentación](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Tarea: Entrenar el Modelo Skip-Gram](lab/README.md)

En el laboratorio, te retamos a modificar el código de esta lección para entrenar un modelo skip-gram en lugar de CBoW. [Lee los detalles](lab/README.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.