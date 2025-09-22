<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-24T09:13:33+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "es"
}
-->
# Modelado del Lenguaje

Las incrustaciones semánticas, como Word2Vec y GloVe, son de hecho un primer paso hacia el **modelado del lenguaje**: crear modelos que de alguna manera *entiendan* (o *representen*) la naturaleza del lenguaje.

## [Cuestionario previo a la lección](https://ff-quizzes.netlify.app/en/ai/quiz/29)

La idea principal detrás del modelado del lenguaje es entrenarlos en conjuntos de datos no etiquetados de manera no supervisada. Esto es importante porque tenemos enormes cantidades de texto no etiquetado disponible, mientras que la cantidad de texto etiquetado siempre estará limitada por el esfuerzo que podamos dedicar a etiquetarlo. Muy a menudo, podemos construir modelos de lenguaje que puedan **predecir palabras faltantes** en el texto, ya que es fácil ocultar una palabra aleatoria en el texto y usarla como muestra de entrenamiento.

## Entrenamiento de Incrustaciones

En nuestros ejemplos anteriores, utilizamos incrustaciones semánticas preentrenadas, pero es interesante ver cómo se pueden entrenar esas incrustaciones. Hay varias ideas posibles que se pueden usar:

* Modelado de lenguaje con **N-Gram**, donde predecimos un token observando los N tokens anteriores (N-grama).
* **Continuous Bag-of-Words** (CBoW), donde predecimos el token central $W_0$ en una secuencia de tokens $W_{-N}$, ..., $W_N$.
* **Skip-gram**, donde predecimos un conjunto de tokens vecinos {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} a partir del token central $W_0$.

![imagen del artículo sobre la conversión de palabras a vectores](../../../../../lessons/5-NLP/14-Embeddings/images/example-algorithms-for-converting-words-to-vectors.png)

> Imagen de [este artículo](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Cuadernos de Ejemplo: Entrenamiento del modelo CBoW

Continúa tu aprendizaje en los siguientes cuadernos:

* [Entrenamiento de Word2Vec CBoW con TensorFlow](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [Entrenamiento de Word2Vec CBoW con PyTorch](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Conclusión

En la lección anterior vimos que las incrustaciones de palabras funcionan como magia. ¡Ahora sabemos que entrenar incrustaciones de palabras no es una tarea muy compleja, y deberíamos ser capaces de entrenar nuestras propias incrustaciones de palabras para texto específico de un dominio si es necesario!

## [Cuestionario posterior a la lección](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Revisión y Autoestudio

* [Tutorial oficial de PyTorch sobre Modelado del Lenguaje](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Tutorial oficial de TensorFlow sobre el entrenamiento del modelo Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* Usar el marco **gensim** para entrenar las incrustaciones más comúnmente utilizadas en unas pocas líneas de código se describe [en esta documentación](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Tarea: Entrenar Modelo Skip-Gram](lab/README.md)

En el laboratorio, te desafiamos a modificar el código de esta lección para entrenar un modelo skip-gram en lugar de CBoW. [Lee los detalles](lab/README.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.