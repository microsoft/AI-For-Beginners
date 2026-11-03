# Procesamiento de Lenguaje Natural

![Resumen de tareas de PLN en un garabato](../../../../translated_images/es/ai-nlp.b22dcb8ca4707cea.webp)

En esta sección, nos centraremos en el uso de Redes Neuronales para manejar tareas relacionadas con el **Procesamiento de Lenguaje Natural (PLN)**. Hay muchos problemas de PLN que queremos que las computadoras puedan resolver:

* **Clasificación de texto** es un problema típico de clasificación relacionado con secuencias de texto. Algunos ejemplos incluyen clasificar mensajes de correo electrónico como spam vs. no spam, o categorizar artículos como deportes, negocios, política, etc. Además, cuando desarrollamos bots de chat, a menudo necesitamos entender lo que un usuario quería decir; en este caso estamos tratando con la **clasificación de intención**. Frecuentemente, en la clasificación de intención tenemos que manejar muchas categorías.
* **Análisis de sentimiento** es un problema típico de regresión, donde necesitamos atribuir un número (un sentimiento) correspondiente a qué tan positivo/negativo es el significado de una oración. Una versión más avanzada del análisis de sentimiento es el **análisis de sentimiento basado en aspectos** (ABSA), donde atribuimos sentimiento no a toda la oración, sino a diferentes partes de ella (aspectos), por ejemplo, *En este restaurante, me gustó la cocina, pero el ambiente fue terrible*.
* **Reconocimiento de Entidades Nombradas** (REN) se refiere al problema de extraer ciertas entidades del texto. Por ejemplo, podríamos necesitar entender que en la frase *Necesito volar a París mañana* la palabra *mañana* se refiere a FECHA, y *París* es una UBICACIÓN.  
* **Extracción de palabras clave** es similar al REN, pero necesitamos extraer automáticamente palabras importantes para el significado de la oración, sin preentrenamiento para tipos específicos de entidad.
* **Agrupamiento de texto** puede ser útil cuando queremos agrupar oraciones similares, por ejemplo, solicitudes similares en conversaciones de soporte técnico.
* **Respuesta a preguntas** se refiere a la capacidad de un modelo para responder a una pregunta específica. El modelo recibe un pasaje de texto y una pregunta como entradas, y necesita proporcionar el lugar en el texto donde está contenida la respuesta a la pregunta (o, a veces, generar el texto de la respuesta).
* **Generación de texto** es la habilidad de un modelo para generar texto nuevo. Se puede considerar como una tarea de clasificación que predice la siguiente letra/palabra basada en un *prompt de texto*. Modelos avanzados de generación de texto, como GPT-3, son capaces de resolver otras tareas de PLN como clasificación usando una técnica llamada [programación de prompts](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0) o [ingeniería de prompts](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29)
* **Resumen de texto** es una técnica cuando queremos que una computadora "lea" un texto largo y lo resuma en unas pocas oraciones.
* **Traducción automática** puede verse como una combinación de la comprensión de texto en un idioma, y la generación de texto en otro idioma.

Inicialmente, la mayoría de las tareas de PLN se resolvían usando métodos tradicionales como gramáticas. Por ejemplo, en la traducción automática se usaban analizadores sintácticos para transformar la oración inicial en un árbol sintáctico, luego se extraían estructuras semánticas de nivel superior para representar el significado de la oración, y basado en este significado y la gramática del idioma objetivo se generaba el resultado. Hoy en día, muchas tareas de PLN se resuelven más eficazmente usando redes neuronales.

> Muchos métodos clásicos de PLN están implementados en la biblioteca Python [Natural Language Processing Toolkit (NLTK)](https://www.nltk.org). Hay un gran [Libro de NLTK](https://www.nltk.org/book/) disponible en línea que cubre cómo se pueden resolver diferentes tareas de PLN usando NLTK.

En nuestro curso, nos enfocaremos principalmente en el uso de Redes Neuronales para PLN, y usaremos NLTK cuando sea necesario.

Ya hemos aprendido sobre el uso de redes neuronales para tratar con datos tabulares y con imágenes. La diferencia principal entre esos tipos de datos y el texto es que el texto es una secuencia de longitud variable, mientras que el tamaño de entrada en el caso de imágenes se conoce de antemano. Aunque las redes convolucionales pueden extraer patrones de los datos de entrada, los patrones en el texto son más complejos. Por ejemplo, podemos tener negación separada del sujeto por un número arbitrario de palabras (por ejemplo, *No me gustan las naranjas*, vs. *No me gustan esas naranjas grandes, coloridas y sabrosas*), y eso aún debe interpretarse como un solo patrón. Por lo tanto, para manejar el lenguaje necesitamos introducir nuevos tipos de redes neuronales, como *redes recurrentes* y *transformers*.

## Instalar Librerías

Si está utilizando una instalación local de Python para ejecutar este curso, puede que necesite instalar todas las librerías requeridas para PLN usando los siguientes comandos:

**Para PyTorch**
```bash
pip install -r requirements-pytorch.txt
```
**Para TensorFlow**
```bash
pip install -r requirements-tf.txt
```

> Puedes probar PLN con TensorFlow en [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/?WT.mc_id=academic-77998-cacaste)

## Advertencia sobre GPU

En esta sección, en algunos de los ejemplos entrenaremos modelos bastante grandes.
* **Usa una computadora con GPU Habilitada**: Es recomendable ejecutar tus notebooks en una computadora con GPU para reducir los tiempos de espera al trabajar con modelos grandes.
* **Limitaciones de memoria GPU**: Ejecutar en una GPU puede llevar a situaciones donde te quedes sin memoria GPU, especialmente al entrenar modelos grandes.
* **Consumo de memoria GPU**: La cantidad de memoria GPU consumida durante el entrenamiento depende de varios factores, incluyendo el tamaño del minibatch.
* **Minimiza el tamaño del minibatch**: Si encuentras problemas de memoria GPU, considera reducir el tamaño del minibatch en tu código como una posible solución.
* **Liberación de memoria GPU en TensorFlow**: Las versiones antiguas de TensorFlow pueden no liberar la memoria GPU correctamente cuando se entrenan múltiples modelos dentro de un solo kernel de Python. Para manejar efectivamente el uso de memoria GPU, puedes configurar TensorFlow para que asigne memoria GPU sólo según sea necesario.
* **Inclusión de código**: Para configurar TensorFlow para que aumente la asignación de memoria GPU sólo cuando sea necesario, incluye el siguiente código en tus notebooks:

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
```

Si te interesa aprender sobre PLN desde una perspectiva clásica de ML, visita [esta serie de lecciones](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP)

## En esta sección
En esta sección aprenderemos sobre:

* [Representar texto como tensores](13-TextRep/README.md)
* [Word Embeddings](14-Embeddings/README.md)
* [Modelado de Lenguaje](15-LanguageModeling/README.md)
* [Redes Neuronales Recurrentes](16-RNN/README.md)
* [Redes Generativas](17-GenerativeNetworks/README.md)
* [Transformers](18-Transformers/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->