# Procesamiento de Lenguaje Natural

![Resumen de tareas de PLN en un dibujo](../../../../lessons/sketchnotes/ai-nlp.png)

En esta sección, nos enfocaremos en usar Redes Neuronales para manejar tareas relacionadas con el **Procesamiento de Lenguaje Natural (PLN)**. Hay muchos problemas de PLN que queremos que las computadoras puedan resolver:

* **Clasificación de texto** es un problema típico de clasificación relacionado con secuencias de texto. Ejemplos incluyen clasificar mensajes de correo electrónico como spam o no spam, o categorizar artículos como deporte, negocios, política, etc. Además, al desarrollar chatbots, a menudo necesitamos entender lo que un usuario quiso decir; en este caso estamos tratando con **clasificación de intención**. Frecuentemente, en la clasificación de intención necesitamos manejar muchas categorías.
* **Análisis de sentimientos** es un problema típico de regresión, donde necesitamos atribuir un número (un sentimiento) que corresponda a cuán positivo/negativo es el significado de una oración. Una versión más avanzada del análisis de sentimientos es el **análisis de sentimientos basado en aspectos** (ABSA), donde atribuimos el sentimiento no a toda la oración, sino a diferentes partes de ella (aspectos), por ejemplo: *En este restaurante, me gustó la cocina, pero la atmósfera era horrible*.
* **Reconocimiento de entidades nombradas** (NER) se refiere al problema de extraer ciertas entidades del texto. Por ejemplo, podríamos necesitar entender que en la frase *Necesito volar a París mañana*, la palabra *mañana* se refiere a una FECHA, y *París* es una UBICACIÓN.  
* **Extracción de palabras clave** es similar a NER, pero necesitamos extraer palabras importantes para el significado de la oración automáticamente, sin preentrenamiento para tipos específicos de entidades.
* **Agrupación de texto** puede ser útil cuando queremos agrupar oraciones similares, por ejemplo, solicitudes similares en conversaciones de soporte técnico.
* **Respuesta a preguntas** se refiere a la capacidad de un modelo para responder una pregunta específica. El modelo recibe un pasaje de texto y una pregunta como entradas, y necesita proporcionar un lugar en el texto donde se encuentre la respuesta a la pregunta (o, a veces, generar el texto de la respuesta).
* **Generación de texto** es la capacidad de un modelo para generar texto nuevo. Puede considerarse como una tarea de clasificación que predice la siguiente letra/palabra basada en algún *texto inicial*. Modelos avanzados de generación de texto, como GPT-3, son capaces de resolver otras tareas de PLN utilizando una técnica llamada [programación con prompts](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0) o [ingeniería de prompts](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29).
* **Resumen de texto** es una técnica en la que queremos que una computadora "lea" un texto largo y lo resuma en unas pocas oraciones.
* **Traducción automática** puede verse como una combinación de comprensión de texto en un idioma y generación de texto en otro.

Inicialmente, la mayoría de las tareas de PLN se resolvían utilizando métodos tradicionales como gramáticas. Por ejemplo, en la traducción automática se utilizaban analizadores para transformar la oración inicial en un árbol sintáctico, luego se extraían estructuras semánticas de nivel superior para representar el significado de la oración, y con base en este significado y la gramática del idioma de destino se generaba el resultado. Hoy en día, muchas tareas de PLN se resuelven de manera más efectiva utilizando redes neuronales.

> Muchos métodos clásicos de PLN están implementados en la biblioteca de Python [Natural Language Processing Toolkit (NLTK)](https://www.nltk.org). Hay un excelente [Libro de NLTK](https://www.nltk.org/book/) disponible en línea que cubre cómo resolver diferentes tareas de PLN utilizando NLTK.

En nuestro curso, nos enfocaremos principalmente en usar Redes Neuronales para PLN, y utilizaremos NLTK cuando sea necesario.

Ya hemos aprendido sobre el uso de redes neuronales para manejar datos tabulares y con imágenes. La principal diferencia entre esos tipos de datos y el texto es que el texto es una secuencia de longitud variable, mientras que el tamaño de entrada en el caso de las imágenes se conoce de antemano. Aunque las redes convolucionales pueden extraer patrones de los datos de entrada, los patrones en el texto son más complejos. Por ejemplo, podemos tener una negación separada del sujeto por muchas palabras arbitrarias (por ejemplo: *No me gustan las naranjas*, vs. *No me gustan esas naranjas grandes, coloridas y sabrosas*), y eso aún debe interpretarse como un solo patrón. Por lo tanto, para manejar el lenguaje necesitamos introducir nuevos tipos de redes neuronales, como *redes recurrentes* y *transformadores*.

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

En esta sección, en algunos de los ejemplos entrenaremos modelos bastante grandes.
* **Usa una computadora con GPU**: Es recomendable ejecutar tus notebooks en una computadora con GPU para reducir los tiempos de espera al trabajar con modelos grandes.
* **Restricciones de memoria de GPU**: Ejecutar en una GPU puede llevar a situaciones en las que te quedes sin memoria de GPU, especialmente al entrenar modelos grandes.
* **Consumo de memoria de GPU**: La cantidad de memoria de GPU consumida durante el entrenamiento depende de varios factores, incluido el tamaño del minibatch.
* **Minimiza el tamaño del minibatch**: Si encuentras problemas de memoria de GPU, considera reducir el tamaño del minibatch en tu código como una posible solución.
* **Liberación de memoria de GPU en TensorFlow**: Las versiones antiguas de TensorFlow pueden no liberar correctamente la memoria de GPU al entrenar múltiples modelos dentro de un mismo kernel de Python. Para gestionar el uso de memoria de GPU de manera efectiva, puedes configurar TensorFlow para que asigne memoria de GPU solo según sea necesario.
* **Inclusión de código**: Para configurar TensorFlow para que crezca la asignación de memoria de GPU solo cuando sea necesario, incluye el siguiente código en tus notebooks:

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
```

Si estás interesado en aprender sobre PLN desde una perspectiva de ML clásico, visita [esta serie de lecciones](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP)

## En esta sección
En esta sección aprenderemos sobre:

* [Representar texto como tensores](13-TextRep/README.md)
* [Embeddings de palabras](14-Emdeddings/README.md)
* [Modelado de lenguaje](15-LanguageModeling/README.md)
* [Redes Neuronales Recurrentes](16-RNN/README.md)
* [Redes Generativas](17-GenerativeNetworks/README.md)
* [Transformadores](18-Transformers/README.md)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.