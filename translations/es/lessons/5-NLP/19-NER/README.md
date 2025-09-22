<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd10f434e444bce61b7f97eeb1ff6a55",
  "translation_date": "2025-08-24T09:14:01+00:00",
  "source_file": "lessons/5-NLP/19-NER/README.md",
  "language_code": "es"
}
-->
# Reconocimiento de Entidades Nombradas

Hasta ahora, nos hemos concentrado principalmente en una tarea de PLN: la clasificación. Sin embargo, existen otras tareas de PLN que se pueden realizar con redes neuronales. Una de esas tareas es **[Reconocimiento de Entidades Nombradas](https://wikipedia.org/wiki/Named-entity_recognition)** (NER, por sus siglas en inglés), que se ocupa de reconocer entidades específicas dentro de un texto, como lugares, nombres de personas, intervalos de fechas y horas, fórmulas químicas, entre otros.

## [Cuestionario previo a la lección](https://ff-quizzes.netlify.app/en/ai/quiz/37)

## Ejemplo de Uso de NER

Supongamos que deseas desarrollar un chatbot de lenguaje natural, similar a Amazon Alexa o Google Assistant. La forma en que funcionan los chatbots inteligentes es *entendiendo* lo que el usuario quiere mediante la clasificación de texto en la frase de entrada. El resultado de esta clasificación es el llamado **intento**, que determina lo que el chatbot debe hacer.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Imagen del autor

Sin embargo, un usuario puede proporcionar algunos parámetros como parte de la frase. Por ejemplo, al preguntar por el clima, puede especificar una ubicación o una fecha. Un bot debe ser capaz de entender esas entidades y completar los espacios de los parámetros en consecuencia antes de realizar la acción. Aquí es exactamente donde entra en juego NER.

> ✅ Otro ejemplo sería [analizar artículos científicos médicos](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Una de las principales cosas que necesitamos buscar son términos médicos específicos, como enfermedades y sustancias médicas. Mientras que un pequeño número de enfermedades probablemente se pueda extraer mediante búsqueda de subcadenas, entidades más complejas, como compuestos químicos y nombres de medicamentos, requieren un enfoque más sofisticado.

## NER como Clasificación de Tokens

Los modelos de NER son esencialmente **modelos de clasificación de tokens**, porque para cada uno de los tokens de entrada necesitamos decidir si pertenece a una entidad o no, y si lo hace, a qué clase de entidad pertenece.

Consideremos el siguiente título de un artículo:

**Regurgitación de la válvula tricúspide** y **carbonato de litio** **toxicidad** en un recién nacido.

Las entidades aquí son:

* Regurgitación de la válvula tricúspide es una enfermedad (`DIS`)
* Carbonato de litio es una sustancia química (`CHEM`)
* Toxicidad también es una enfermedad (`DIS`)

Observa que una entidad puede abarcar varios tokens. Y, como en este caso, necesitamos distinguir entre dos entidades consecutivas. Por lo tanto, es común usar dos clases para cada entidad: una que especifica el primer token de la entidad (a menudo se usa el prefijo `B-`, para **b**eginning o inicio), y otra para la continuación de una entidad (`I-`, para **i**nner token o token interno). También usamos `O` como clase para representar todos los **o**tros tokens. Este etiquetado de tokens se llama [etiquetado BIO](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (o IOB). Cuando se etiqueta, nuestro título se verá así:

Token | Etiqueta
------|---------
Tricuspid | B-DIS
valve | I-DIS
regurgitation | I-DIS
and | O
lithium | B-CHEM
carbonate | I-CHEM
toxicity | B-DIS
in | O
a | O
newborn | O
infant | O
. | O

Dado que necesitamos construir una correspondencia uno a uno entre tokens y clases, podemos entrenar un modelo neuronal **muchos a muchos** como el que se muestra en esta imagen:

![Imagen que muestra patrones comunes de redes neuronales recurrentes.](../../../../../lessons/5-NLP/17-GenerativeNetworks/images/unreasonable-effectiveness-of-rnn.jpg)

> *Imagen de [este artículo](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) de [Andrej Karpathy](http://karpathy.github.io/). Los modelos de clasificación de tokens NER corresponden a la arquitectura de red más a la derecha en esta imagen.*

## Entrenamiento de Modelos NER

Dado que un modelo NER es esencialmente un modelo de clasificación de tokens, podemos usar RNNs, con las que ya estamos familiarizados, para esta tarea. En este caso, cada bloque de la red recurrente devolverá el ID del token. El siguiente cuaderno de ejemplo muestra cómo entrenar un LSTM para la clasificación de tokens.

## ✍️ Cuadernos de Ejemplo: NER

Continúa tu aprendizaje en el siguiente cuaderno:

* [NER con TensorFlow](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Conclusión

Un modelo NER es un **modelo de clasificación de tokens**, lo que significa que se puede usar para realizar clasificación de tokens. Esta es una tarea muy común en PLN, que ayuda a reconocer entidades específicas dentro de un texto, incluyendo lugares, nombres, fechas y más.

## 🚀 Desafío

Completa la tarea vinculada a continuación para entrenar un modelo de reconocimiento de entidades nombradas para términos médicos, y luego pruébalo en un conjunto de datos diferente.

## [Cuestionario posterior a la lección](https://ff-quizzes.netlify.app/en/ai/quiz/38)

## Revisión y Autoestudio

Lee el artículo [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) y sigue la sección de Lecturas Adicionales en ese artículo para profundizar tu conocimiento.

## [Tarea](lab/README.md)

En la tarea de esta lección, tendrás que entrenar un modelo de reconocimiento de entidades médicas. Puedes comenzar entrenando un modelo LSTM como se describe en esta lección, y luego avanzar al uso del modelo transformador BERT. Lee [las instrucciones](lab/README.md) para obtener todos los detalles.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.