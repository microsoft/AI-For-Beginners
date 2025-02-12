# Procesamiento de Lenguaje Natural

![Resumen de tareas de PLN en un garabato](../../../../translated_images/ai-nlp.b22dcb8ca4707ceaee8576db1c5f4089c8cac2f454e9e03ea554f07fda4556b8.es.png)

En esta sección, nos centraremos en el uso de Redes Neuronales para abordar tareas relacionadas con el **Procesamiento de Lenguaje Natural (PLN)**. Existen muchos problemas de PLN que queremos que los ordenadores puedan resolver:

* **Clasificación de texto** es un problema típico de clasificación relacionado con secuencias de texto. Ejemplos incluyen clasificar mensajes de correo electrónico como spam o no spam, o categorizar artículos como deportes, negocios, política, etc. Además, al desarrollar chatbots, a menudo necesitamos entender lo que un usuario quería decir; en este caso, estamos tratando con **clasificación de intenciones**. A menudo, en la clasificación de intenciones necesitamos lidiar con muchas categorías.
* **Análisis de sentimientos** es un problema típico de regresión, donde necesitamos atribuir un número (un sentimiento) que corresponde a cuán positivo o negativo es el significado de una oración. Una versión más avanzada del análisis de sentimientos es el **análisis de sentimientos basado en aspectos** (ABSA), donde atribuimos el sentimiento no a toda la oración, sino a diferentes partes de ella (aspectos), por ejemplo, *En este restaurante, me gustó la cocina, pero la atmósfera era horrible*.
* **Reconocimiento de Entidades Nombradas** (NER) se refiere al problema de extraer ciertas entidades del texto. Por ejemplo, podríamos necesitar entender que en la frase *Necesito volar a París mañana* la palabra *mañana* se refiere a una FECHA, y *París* es una UBICACIÓN.  
* **Extracción de palabras clave** es similar a NER, pero necesitamos extraer automáticamente palabras importantes para el significado de la oración, sin entrenamiento previo para tipos de entidades específicos.
* **Agrupamiento de texto** puede ser útil cuando queremos agrupar oraciones similares, por ejemplo, solicitudes similares en conversaciones de soporte técnico.
* **Respuesta a preguntas** se refiere a la capacidad de un modelo para responder a una pregunta específica. El modelo recibe un pasaje de texto y una pregunta como entradas, y necesita proporcionar un lugar en el texto donde se contiene la respuesta a la pregunta (o, a veces, generar el texto de respuesta).
* **Generación de texto** es la capacidad de un modelo para generar nuevo texto. Puede considerarse como una tarea de clasificación que predice la siguiente letra/palabra basada en un *texto de entrada*. Modelos avanzados de generación de texto, como GPT-3, son capaces de resolver otras tareas de PLN, como clasificación, utilizando una técnica llamada [programación de prompts](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0) o [ingeniería de prompts](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29).
* **Resumen de texto** es una técnica cuando queremos que una computadora "lea" un texto largo y lo resuma en unas pocas oraciones.
* **Traducción automática** puede verse como una combinación de comprensión de texto en un idioma y generación de texto en otro.

Inicialmente, la mayoría de las tareas de PLN se resolvían utilizando métodos tradicionales como gramáticas. Por ejemplo, en la traducción automática se utilizaban analizadores para transformar la oración inicial en un árbol de sintaxis, luego se extraían estructuras semánticas de nivel superior para representar el significado de la oración, y con base en este significado y la gramática del idioma objetivo se generaba el resultado. Hoy en día, muchas tareas de PLN se resuelven de manera más efectiva utilizando redes neuronales.

> Muchos métodos clásicos de PLN están implementados en la biblioteca de Python [Natural Language Processing Toolkit (NLTK)](https://www.nltk.org). Hay un excelente [Libro de NLTK](https://www.nltk.org/book/) disponible en línea que cubre cómo se pueden resolver diferentes tareas de PLN utilizando NLTK.

En nuestro curso, nos centraremos principalmente en el uso de Redes Neuronales para PLN, y utilizaremos NLTK cuando sea necesario.

Ya hemos aprendido sobre el uso de redes neuronales para tratar con datos tabulares y con imágenes. La principal diferencia entre esos tipos de datos y el texto es que el texto es una secuencia de longitud variable, mientras que el tamaño de entrada en el caso de las imágenes se conoce de antemano. Mientras que las redes convolucionales pueden extraer patrones de los datos de entrada, los patrones en el texto son más complejos. Por ejemplo, podemos tener negaciones separadas del sujeto que sean arbitrarias para muchas palabras (por ejemplo, *No me gustan las naranjas*, frente a *No me gustan esas grandes naranjas coloridas y sabrosas*), y eso aún debería interpretarse como un solo patrón. Por lo tanto, para manejar el lenguaje necesitamos introducir nuevos tipos de redes neuronales, como *redes recurrentes* y *transformadores*.

## Instalar Bibliotecas

Si estás utilizando una instalación local de Python para ejecutar este curso, es posible que necesites instalar todas las bibliotecas requeridas para PLN utilizando los siguientes comandos:

**Para PyTorch**
```bash
pip install -r requirements-torch.txt
```
**Para TensorFlow**
```bash
pip install -r requirements-tf.txt
```

> Puedes probar PLN con TensorFlow en [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/?WT.mc_id=academic-77998-cacaste)

## Advertencia sobre GPU

En esta sección, en algunos de los ejemplos estaremos entrenando modelos bastante grandes.
* **Usa una computadora habilitada para GPU**: Es recomendable ejecutar tus cuadernos en una computadora habilitada para GPU para reducir los tiempos de espera al trabajar con modelos grandes.
* **Restricciones de memoria de GPU**: Ejecutar en una GPU puede llevar a situaciones donde te quedes sin memoria de GPU, especialmente al entrenar modelos grandes.
* **Consumo de memoria de GPU**: La cantidad de memoria de GPU consumida durante el entrenamiento depende de varios factores, incluido el tamaño del minibatch.
* **Minimiza el tamaño del minibatch**: Si encuentras problemas de memoria de GPU, considera reducir el tamaño del minibatch en tu código como una posible solución.
* **Liberación de memoria de GPU en TensorFlow**: Las versiones más antiguas de TensorFlow pueden no liberar correctamente la memoria de GPU al entrenar múltiples modelos dentro de un mismo kernel de Python. Para gestionar el uso de memoria de GPU de manera efectiva, puedes configurar TensorFlow para que asigne memoria de GPU solo según sea necesario.
* **Inclusión de código**: Para configurar TensorFlow para que aumente la asignación de memoria de GPU solo cuando sea necesario, incluye el siguiente código en tus cuadernos:

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
```

Si estás interesado en aprender sobre PLN desde una perspectiva clásica de ML, visita [este conjunto de lecciones](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP)

## En esta Sección
En esta sección aprenderemos sobre:

* [Representación de texto como tensores](13-TextRep/README.md)
* [Embeddings de palabras](14-Emdeddings/README.md)
* [Modelado del lenguaje](15-LanguageModeling/README.md)
* [Redes Neuronales Recurrentes](16-RNN/README.md)
* [Redes Generativas](17-GenerativeNetworks/README.md)
* [Transformadores](18-Transformers/README.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.