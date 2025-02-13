# Modelo de Skip-Gram para Entrenamiento

Tarea del [Currículo de IA para Principiantes](https://github.com/microsoft/ai-for-beginners).

## Tarea

En este laboratorio, te desafiamos a entrenar un modelo Word2Vec utilizando la técnica Skip-Gram. Entrena una red con incrustaciones para predecir palabras vecinas en una ventana Skip-Gram de $N$-tokens de ancho. Puedes usar el [código de esta lección](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) y modificarlo ligeramente.

## El Conjunto de Datos

Puedes utilizar cualquier libro. Puedes encontrar muchos textos gratuitos en [Project Gutenberg](https://www.gutenberg.org/), por ejemplo, aquí tienes un enlace directo a [Las aventuras de Alicia en el país de las maravillas](https://www.gutenberg.org/files/11/11-0.txt) de Lewis Carroll. O, puedes usar las obras de Shakespeare, que puedes obtener utilizando el siguiente código:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## ¡Explora!

Si tienes tiempo y quieres profundizar en el tema, intenta explorar varias cosas:

* ¿Cómo afecta el tamaño de la incrustación a los resultados?
* ¿Cómo afectan los diferentes estilos de texto al resultado?
* Toma varios tipos de palabras muy diferentes y sus sinónimos, obtén sus representaciones vectoriales, aplica PCA para reducir las dimensiones a 2 y trázalas en un espacio 2D. ¿Ves algún patrón?

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o mala interpretación que surja del uso de esta traducción.