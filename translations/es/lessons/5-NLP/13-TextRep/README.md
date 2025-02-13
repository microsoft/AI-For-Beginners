# Representación de Texto como Tensores

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Clasificación de Texto

A lo largo de la primera parte de esta sección, nos centraremos en la tarea de **clasificación de texto**. Utilizaremos el conjunto de datos [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset), que contiene artículos de noticias como los siguientes:

* Categoría: Sci/Tech
* Título: La empresa de Ky. gana una subvención para estudiar péptidos (AP)
* Cuerpo: AP - Una empresa fundada por un investigador en química en la Universidad de Louisville ganó una subvención para desarrollar...

Nuestro objetivo será clasificar el artículo de noticias en una de las categorías basadas en el texto.

## Representación del texto

Si queremos resolver tareas de Procesamiento de Lenguaje Natural (NLP) con redes neuronales, necesitamos alguna forma de representar el texto como tensores. Las computadoras ya representan caracteres textuales como números que se asignan a fuentes en tu pantalla utilizando codificaciones como ASCII o UTF-8.

<img alt="Imagen que muestra un diagrama que mapea un carácter a una representación ASCII y binaria" src="images/ascii-character-map.png" width="50%"/>

> [Fuente de la imagen](https://www.seobility.net/en/wiki/ASCII)

Como humanos, entendemos lo que cada letra **representa**, y cómo todos los caracteres se combinan para formar las palabras de una oración. Sin embargo, las computadoras por sí solas no tienen tal comprensión, y la red neuronal tiene que aprender el significado durante el entrenamiento.

Por lo tanto, podemos usar diferentes enfoques al representar el texto:

* **Representación a nivel de carácter**, cuando representamos el texto tratando cada carácter como un número. Dado que tenemos *C* caracteres diferentes en nuestro corpus de texto, la palabra *Hola* se representaría mediante un tensor de 5x*C*. Cada letra correspondería a una columna del tensor en codificación one-hot.
* **Representación a nivel de palabra**, en la que creamos un **vocabulario** de todas las palabras en nuestro texto, y luego representamos las palabras utilizando codificación one-hot. Este enfoque es algo mejor, porque cada letra por sí sola no tiene mucho significado, y así, al usar conceptos semánticos de mayor nivel - palabras - simplificamos la tarea para la red neuronal. Sin embargo, dado el gran tamaño del diccionario, necesitamos lidiar con tensores dispersos de alta dimensión.

Independientemente de la representación, primero necesitamos convertir el texto en una secuencia de **tokens**, donde un token puede ser un carácter, una palabra, o a veces incluso parte de una palabra. Luego, convertimos el token en un número, típicamente usando un **vocabulario**, y este número puede ser alimentado a una red neuronal utilizando codificación one-hot.

## N-Grams

En el lenguaje natural, el significado preciso de las palabras solo puede determinarse en contexto. Por ejemplo, los significados de *red neuronal* y *red de pesca* son completamente diferentes. Una de las formas de tener esto en cuenta es construir nuestro modelo sobre pares de palabras, considerando los pares de palabras como tokens de vocabulario separados. De esta manera, la oración *Me gusta ir a pescar* se representará mediante la siguiente secuencia de tokens: *Me gusta*, *gusta ir*, *ir a*, *a pescar*. El problema con este enfoque es que el tamaño del diccionario crece significativamente, y combinaciones como *ir a pescar* y *ir de compras* se presentan con diferentes tokens, que no comparten ninguna similitud semántica a pesar de tener el mismo verbo.  

En algunos casos, también podemos considerar el uso de tri-gramas -- combinaciones de tres palabras --. Así, el enfoque se denomina a menudo **n-grams**. Además, tiene sentido usar n-grams con representación a nivel de carácter, en cuyo caso los n-grams corresponderán aproximadamente a diferentes sílabas.

## Bolsa de Palabras y TF/IDF

Al resolver tareas como la clasificación de texto, necesitamos poder representar el texto mediante un vector de tamaño fijo, que utilizaremos como entrada para el clasificador denso final. Una de las formas más simples de hacerlo es combinar todas las representaciones de palabras individuales, por ejemplo, sumándolas. Si sumamos las codificaciones one-hot de cada palabra, terminaremos con un vector de frecuencias, que muestra cuántas veces aparece cada palabra dentro del texto. Tal representación del texto se llama **bolsa de palabras** (BoW).

<img src="images/bow.png" width="90%"/>

> Imagen del autor

Un BoW representa esencialmente qué palabras aparecen en el texto y en qué cantidades, lo que puede ser una buena indicación de lo que trata el texto. Por ejemplo, un artículo de noticias sobre política es probable que contenga palabras como *presidente* y *país*, mientras que una publicación científica tendría algo como *colisionador*, *descubierto*, etc. Así, las frecuencias de palabras pueden ser en muchos casos un buen indicador del contenido del texto.

El problema con BoW es que ciertas palabras comunes, como *y*, *es*, etc., aparecen en la mayoría de los textos, y tienen las frecuencias más altas, ocultando las palabras que son realmente importantes. Podemos reducir la importancia de esas palabras teniendo en cuenta la frecuencia con la que ocurren en toda la colección de documentos. Esta es la idea principal detrás del enfoque TF/IDF, que se cubre con más detalle en los cuadernos adjuntos a esta lección.

Sin embargo, ninguno de estos enfoques puede tener en cuenta completamente la **semántica** del texto. Necesitamos modelos de redes neuronales más poderosos para hacer esto, que discutiremos más adelante en esta sección.

## ✍️ Ejercicios: Representación de Texto

Continúa tu aprendizaje en los siguientes cuadernos:

* [Representación de Texto con PyTorch](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb)
* [Representación de Texto con TensorFlow](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)

## Conclusión

Hasta ahora, hemos estudiado técnicas que pueden agregar peso de frecuencia a diferentes palabras. Sin embargo, no son capaces de representar el significado o el orden. Como dijo el famoso lingüista J. R. Firth en 1935, "El significado completo de una palabra siempre es contextual, y ningún estudio de significado separado del contexto puede tomarse en serio." Aprenderemos más adelante en el curso cómo capturar la información contextual del texto utilizando modelado de lenguaje.

## 🚀 Desafío

Intenta algunos otros ejercicios utilizando bolsa de palabras y diferentes modelos de datos. Podrías inspirarte en esta [competencia en Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words)

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Revisión y Autoestudio

Practica tus habilidades con técnicas de embeddings de texto y bolsa de palabras en [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Asignación: Cuadernos](assignment.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional por parte de un humano. No nos hacemos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.