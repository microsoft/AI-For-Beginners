# Representando el texto como tensoras

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Clasificación de texto

A lo largo de la primera parte de esta sección, nos centraremos en la tarea de **clasificación de texto**. Usaremos el [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset) Conjunto de datos, que contiene artículos de noticias como los siguientes:

* Categoría: Ciencia/Tecnología
* Título: Ky. Company gana una subvención para estudiar péptidos (AP)
*Cuerpo: AP - Una empresa fundada por un investigador de química de la Universidad de Louisville ganó una subvención para desarrollar...

Nuestro objetivo será clasificar la noticia en una de las categorías basadas en texto.

## Representando texto

Si queremos resolver tareas de procesamiento del lenguaje natural (PNL) con redes neuronales, necesitamos alguna forma de representar el texto como tensores. Las computadoras ya representan caracteres textuales como números que se asignan a fuentes en la pantalla mediante codificaciones como ASCII o UTF-8.

<img alt="Image showing diagram mapping a character to an ASCII and binary representation" src="images/ascii-character-map.png" width="50%"/>

> [Image source](https://www.seobility.net/en/wiki/ASCII)

Como seres humanos, entendemos lo que **representa** cada letra y cómo todos los caracteres se unen para formar las palabras de una oración. Sin embargo, los ordenadores por sí solos no tienen esa comprensión y las redes neuronales tienen que aprender el significado durante el entrenamiento.

Por tanto, podemos utilizar diferentes enfoques a la hora de representar texto:

* **Representación a nivel de carácter**, cuando representamos texto tratando cada carácter como un número. Dado que tenemos *C* caracteres diferentes en nuestro corpus de texto, la palabra *Hola* estaría representada por el tensor 5x*C*. Cada letra correspondería a una columna tensorial en codificación one-hot.
* **Representación a nivel de palabra**, en la que creamos un **vocabulario** de todas las palabras de nuestro texto y luego las representamos usando codificación one-hot. Este enfoque es algo mejor, porque cada letra por sí sola no tiene mucho significado y, por lo tanto, al utilizar conceptos semánticos de nivel superior (palabras), simplificamos la tarea de la red neuronal. Sin embargo, dado el gran tamaño del diccionario, debemos lidiar con tensores dispersos de alta dimensión.

Independientemente de la representación, primero debemos convertir el texto en una secuencia de **tokens**, siendo un token un carácter, una palabra o, a veces, incluso parte de una palabra. Luego, convertimos el token en un número, normalmente usando **vocabulario**, y este número se puede introducir en una red neuronal mediante codificación one-hot.

## N-Gramos

En el lenguaje natural, el significado preciso de las palabras sólo puede determinarse en contexto. Por ejemplo, los significados de *red neuronal* y *red de pesca* son completamente diferentes. Una de las formas de tener esto en cuenta es construir nuestro modelo sobre pares de palabras y considerar los pares de palabras como fichas de vocabulario separadas. De esta forma, la frase *me gusta ir a pescar* quedará representada por la siguiente secuencia de fichas: *me gusta*, *me gusta*, *ir*, *ir a pescar*. El problema con este enfoque es que el tamaño del diccionario crece significativamente y combinaciones como *ir a pescar* y *ir de compras* se presentan mediante tokens diferentes, que no comparten ninguna similitud semántica a pesar del mismo verbo.

En algunos casos, también podemos considerar el uso de trigramas (combinaciones de tres palabras). Por lo tanto, el enfoque a menudo se denomina **n-gramas**. Además, tiene sentido utilizar n-gramas con representación a nivel de carácter, en cuyo caso los n-gramas corresponderán aproximadamente a diferentes programas de estudio.

## Bolsa de palabras y TF/IDF

Al resolver tareas como la clasificación de texto, debemos poder representar el texto mediante un vector de tamaño fijo, que usaremos como entrada para el clasificador denso final. Una de las formas más sencillas de hacerlo es combinar todas las representaciones de palabras individuales, por ejemplo. agregándolos. Si agregamos codificaciones one-hot de cada palabra, terminaremos con un vector de frecuencias, que muestra cuántas veces aparece cada palabra dentro del texto. Esta representación de texto se llama **bolsa de palabras** (BoW).

<img src="images/bow.png" width="90%"/>

> Image by the author

Un BoW esencialmente representa qué palabras aparecen en el texto y en qué cantidades, lo que de hecho puede ser una buena indicación de de qué trata el texto. Por ejemplo, es probable que un artículo de noticias sobre política contenga palabras como *presidente* y *país*, mientras que una publicación científica tendría algo como *colisionador*, *descubierto*, etc. Por lo tanto, la frecuencia de las palabras puede en muchos casos ser una buena indicador del contenido del texto.

El problema con BoW es que ciertas palabras comunes, como *and*, *is*, etc. aparecen en la mayoría de los textos y tienen frecuencias más altas, enmascarando las palabras que son realmente importantes. Podemos reducir la importancia de esas palabras teniendo en cuenta la frecuencia con la que aparecen en toda la colección de documentos. Esta es la idea principal detrás del enfoque TF/IDF, que se trata con más detalle en los cuadernos adjuntos a esta lección.

Sin embargo, ninguno de esos enfoques puede tener en cuenta plenamente la **semántica** del texto. Necesitamos modelos de redes neuronales más potentes para hacer esto, lo cual discutiremos más adelante en esta sección.

## ✍️ Ejercicios: Representación de Texto

Continúa tu aprendizaje en los siguientes cuadernos:

* [Text Representation with PyTorch](TextRepresentationPyTorch.ipynb)
* [Text Representation with TensorFlow](TextRepresentationTF.ipynb)

## Conclusión

Hasta ahora, hemos estudiado técnicas que pueden agregar peso de frecuencia a diferentes palabras. Sin embargo, no pueden representar significado u orden. Como dijo el famoso lingüista J. R. Firth en 1935: "El significado completo de una palabra es siempre contextual, y ningún estudio del significado aparte del contexto puede tomarse en serio". Más adelante en el curso aprenderemos cómo capturar información contextual del texto utilizando modelos de lenguaje.

## 🚀 Desafío

Pruebe otros ejercicios utilizando una bolsa de palabras y diferentes modelos de datos. Quizás te inspire esto [competition on Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Revisión y autoestudio

Practica tus habilidades con incrustaciones de texto y técnicas de bolsa de palabras en [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Assignment: Notebooks](assignment.md)
