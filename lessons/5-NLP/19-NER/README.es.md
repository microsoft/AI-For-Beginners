# Reconocimiento de entidad nombrada

Hasta ahora nos hemos concentrado principalmente en una tarea de PNL: la clasificación. Sin embargo, también existen otras tareas de PNL que se pueden realizar con redes neuronales. Una de esas tareas es **[Reconocimiento de entidad con nombre](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), que se ocupa del reconocimiento de entidades específicas dentro del texto, como lugares, nombres de personas, fechas. -intervalos de tiempo, fórmulas químicas, etc.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## Ejemplo de uso de NER

Suponga que desea desarrollar un bot de chat en lenguaje natural, similar a Amazon Alexa o Google Assistant. La forma en que funcionan los chatbots inteligentes es *comprender* lo que el usuario quiere clasificando el texto en la oración de entrada. El resultado de esta clasificación es la llamada **intención**, que determina lo que debe hacer un chat bot.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Imagen del autor

Sin embargo, un usuario puede proporcionar algunos parámetros como parte de la frase. Por ejemplo, cuando pregunta por el tiempo, puede especificar un lugar o una fecha. Un robot debería poder comprender esas entidades y completar los espacios de parámetros en consecuencia antes de realizar la acción. Aquí es exactamente donde entra en juego NER.

> ✅ Otro ejemplo sería [análisis de artículos médicos científicos] (https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Una de las principales cosas que debemos buscar son términos médicos específicos, como enfermedades y sustancias médicas. Si bien es probable que se pueda extraer una pequeña cantidad de enfermedades mediante la búsqueda de subcadenas, entidades más complejas, como compuestos químicos y nombres de medicamentos, necesitan un enfoque más complejo.
>
> ## NER como clasificación de tokens

Los modelos NER son esencialmente **modelos de clasificación de tokens**, porque para cada uno de los tokens de entrada debemos decidir si pertenece a una entidad o no, y si es así, a qué clase de entidad.

Considere el siguiente título del artículo:

**Insuficiencia de la válvula tricúspide** y **carbonato de litio** **toxicidad** en un recién nacido.

Las entidades aquí son:

* La insuficiencia de la válvula tricúspide es una enfermedad (`DIS`)
* El carbonato de litio es una sustancia química (`CHEM`)
* La toxicidad también es una enfermedad (`DIS`)

Observe que una entidad puede abarcar varios tokens. Y, como en este caso, debemos distinguir entre dos entidades consecutivas. Por lo tanto, es común usar dos clases para cada entidad: una que especifica el primer token de la entidad (a menudo se usa el prefijo `B-`, para **b**comienzo) y otra, la continuación de una entidad ( `I-`, para **i**nner token). También usamos `O` como clase para representar todos los **otros** tokens. Este etiquetado de tokens se denomina [etiquetado BIO](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (o IOB). Cuando esté etiquetado, nuestro título se verá así:

Ficha | Etiqueta
------|-----
Tricúspide | B-DIS
válvula | I-DIS
regurgitación | I-DIS
y | O
litio | B-CHEM
carbonato | I-CHEM
toxicidad | B-DIS
en | O
un | O
recién nacido | O
infantil | O
. | O

Dado que necesitamos construir una correspondencia uno a uno entre tokens y clases, podemos entrenar un modelo de red neuronal **muchos a muchos** más a la derecha a partir de esta imagen:

![Image showing common recurrent neural network patterns.](../17-GenerativeNetworks/images/unreasonable-effectiveness-of-rnn.jpg)

> *Imagen de [this blog post](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) by [Andrej Karpathy](http://karpathy.github.io/). NER token classification models correspond to the right-most network architecture on this picture.*

## Entrenamiento de modelos NER

Dado que un modelo NER es esencialmente un modelo de clasificación de tokens, podemos usar RNN con los que ya estamos familiarizados para esta tarea. En este caso, cada bloque de red recurrente devolverá el ID del token. El siguiente cuaderno de ejemplo muestra cómo entrenar LSTM para la clasificación de tokens.

## ✍️ Cuadernos de ejemplo: NER

Continúa tu aprendizaje en el siguiente cuaderno:

* [NER with TensorFlow](NER-TF.ipynb)

## Conclusión

Un modelo NER es un **modelo de clasificación de tokens**, lo que significa que se puede utilizar para realizar una clasificación de tokens. Esta es una tarea muy común en PNL y ayuda a reconocer entidades específicas dentro del texto, incluidos lugares, nombres, fechas y más.

## 🚀 Desafío

Complete la tarea vinculada a continuación para entrenar un modelo de reconocimiento de entidades con nombre para términos médicos y luego pruébelo en un conjunto de datos diferente.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Revisión y autoestudio

Leer el blog [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) y siga la sección de lecturas adicionales de ese artículo para profundizar sus conocimientos.

## [Assignment](lab/README.md)

En la tarea de esta lección, deberá entrenar un modelo de reconocimiento de entidades médicas. Puede comenzar entrenando un modelo LSTM como se describe en esta lección y continuar usando el modelo de transformador BERT. Lea [las instrucciones](lab/README.md) para obtener todos los detalles.
