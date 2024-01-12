# Modelado de lenguaje

Las incrustaciones semánticas, como Word2Vec y GloVe, son de hecho un primer paso hacia el **modelado del lenguaje**: crear modelos que de alguna manera *comprenden* (o *representan*) la naturaleza del lenguaje.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

La idea principal detrás del modelado de lenguajes es entrenarlos en conjuntos de datos sin etiquetar y sin supervisión. Esto es importante porque tenemos grandes cantidades de texto sin etiquetar disponibles, mientras que la cantidad de texto etiquetado siempre estará limitada por la cantidad de esfuerzo que podamos dedicar al etiquetado. En la mayoría de los casos, podemos crear modelos de lenguaje que pueden **predecir las palabras que faltan** en el texto, porque es fácil enmascarar una palabra aleatoria en el texto y usarla como muestra de entrenamiento.

## Integraciones de entrenamiento

En nuestros ejemplos anteriores, utilizamos incorporaciones semánticas previamente entrenadas, pero es interesante ver cómo se pueden entrenar esas incorporaciones. Hay varias ideas posibles que se pueden utilizar:

* Modelado de lenguaje **N-Gram**, cuando predecimos un token observando N tokens anteriores (N-gram)
* **Bolsa de palabras continua** (CBoW), cuando predecimos el token medio $W_0$ en una secuencia de tokens $W_{-N}$, ..., $W_N$.
* **Skip-gram**, donde predecimos un conjunto de tokens vecinos {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} del token del medio $W_0$.

![image from paper on converting words to vectors](../14-Embeddings/images/example-algorithms-for-converting-words-to-vectors.png)

> Imagen de [this paper](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Cuadernos de ejemplo: Entrenamiento del modelo CBoW

Continúa tu aprendizaje en los siguientes cuadernos:

* [Training CBoW Word2Vec with TensorFlow](CBoW-TF.ipynb)
* [Training CBoW Word2Vec with PyTorch](CBoW-PyTorch.ipynb)

## Conclusión

¡En la lección anterior vimos que las incrustaciones de palabras funcionan como magia! Ahora sabemos que entrenar incrustaciones de palabras no es una tarea muy compleja y, si es necesario, deberíamos poder entrenar nuestras propias incrustaciones de palabras para texto de dominio específico.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Revisión y autoestudio

* [Official PyTorch tutorial on Language Modeling](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Official TensorFlow tutorial on training Word2Vec model](https://www.TensorFlow.org/tutorials/text/word2vec).
* Se describe el uso del marco **gensim** para entrenar las incrustaciones más utilizadas en unas pocas líneas de código [in this documentation](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Assignment: Train Skip-Gram Model](lab/README.md)

In the lab, we challenge you to modify the code from this lesson to train skip-gram model instead of CBoW.[Read the details](lab/README.md)

