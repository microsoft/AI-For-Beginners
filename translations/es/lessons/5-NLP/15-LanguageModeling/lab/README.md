# Entrenando el Modelo Skip-Gram

Asignación de laboratorio del [Currículo de AI para Principiantes](https://github.com/microsoft/ai-for-beginners).

## Tarea

En este laboratorio, te desafiamos a entrenar un modelo Word2Vec utilizando la técnica Skip-Gram. Entrena una red con embeddings para predecir palabras vecinas en una ventana Skip-Gram de $N$ tokens de ancho. Puedes usar el [código de esta lección](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) y modificarlo ligeramente.

## El Conjunto de Datos

Puedes usar cualquier libro que desees. Hay muchos textos gratuitos disponibles en [Project Gutenberg](https://www.gutenberg.org/), por ejemplo, aquí tienes un enlace directo a [Las aventuras de Alicia en el País de las Maravillas](https://www.gutenberg.org/files/11/11-0.txt) de Lewis Carroll. O bien, puedes usar las obras de Shakespeare, las cuales puedes obtener con el siguiente código:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## ¡Explora!

Si tienes tiempo y quieres profundizar en el tema, intenta explorar varias cosas:

* ¿Cómo afecta el tamaño del embedding a los resultados?
* ¿Cómo afectan los diferentes estilos de texto al resultado?
* Toma varios tipos de palabras muy diferentes y sus sinónimos, obtén sus representaciones vectoriales, aplica PCA para reducir las dimensiones a 2 y represéntalos en un espacio 2D. ¿Ves algún patrón?

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.