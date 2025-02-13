# Reconocimiento de Entidades Nombradas

Hasta ahora, nos hemos concentrado principalmente en una tarea de PLN: la clasificación. Sin embargo, también hay otras tareas de PLN que se pueden realizar con redes neuronales. Una de esas tareas es **[Reconocimiento de Entidades Nombradas](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), que se ocupa de reconocer entidades específicas dentro del texto, como lugares, nombres de personas, intervalos de fecha y hora, fórmulas químicas, y más.

## [Cuestionario previo a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## Ejemplo de Uso de NER

Supongamos que deseas desarrollar un chatbot de lenguaje natural, similar a Amazon Alexa o Google Assistant. La forma en que funcionan los chatbots inteligentes es *entendiendo* lo que el usuario quiere mediante la clasificación de texto de la frase de entrada. El resultado de esta clasificación es lo que se llama **intención**, que determina lo que debe hacer un chatbot.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Imagen del autor

Sin embargo, un usuario puede proporcionar algunos parámetros como parte de la frase. Por ejemplo, al preguntar por el clima, puede especificar una ubicación o una fecha. Un bot debe ser capaz de entender esas entidades y completar los espacios de parámetros de acuerdo antes de realizar la acción. Aquí es donde entra en juego NER.

> ✅ Otro ejemplo sería [analizar artículos médicos científicos](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Una de las principales cosas que necesitamos buscar son términos médicos específicos, como enfermedades y sustancias médicas. Si bien un pequeño número de enfermedades probablemente se pueden extraer utilizando la búsqueda de subcadenas, entidades más complejas, como compuestos químicos y nombres de medicamentos, requieren un enfoque más complejo.

## NER como Clasificación de Tokens

Los modelos NER son esencialmente **modelos de clasificación de tokens**, porque para cada uno de los tokens de entrada necesitamos decidir si pertenece a una entidad o no, y si lo hace, a qué clase de entidad pertenece.

Considera el siguiente título de un artículo:

**Regurgitación de la válvula tricúspide** y **toxicidad del carbonato de litio** en un recién nacido.

Las entidades aquí son:

* Regurgitación de la válvula tricúspide es una enfermedad (`DIS`)
* El carbonato de litio es una sustancia química (`CHEM`)
* Toxicidad también es una enfermedad (`DIS`)

Observa que una entidad puede abarcar varios tokens. Y, como en este caso, necesitamos distinguir entre dos entidades consecutivas. Por lo tanto, es común utilizar dos clases para cada entidad: una que especifica el primer token de la entidad (a menudo se utiliza el prefijo `B-`, para **b**eginning), y otra - la continuación de una entidad (`I-`, para **i**nner token). También usamos `O` como una clase para representar todos los **o**tros tokens. Este etiquetado de tokens se llama [etiquetado BIO](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (o IOB). Cuando se etiqueta, nuestro título se verá así:

Token | Etiqueta
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
recién | O
nacido | O
. | O

Dado que necesitamos construir una correspondencia uno a uno entre tokens y clases, podemos entrenar un modelo de red neuronal **muchos a muchos** a partir de esta imagen:

![Imagen que muestra patrones comunes de redes neuronales recurrentes.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.es.jpg)

> *Imagen de [esta publicación en el blog](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) de [Andrej Karpathy](http://karpathy.github.io/). Los modelos de clasificación de tokens NER corresponden a la arquitectura de red más a la derecha en esta imagen.*

## Entrenamiento de Modelos NER

Dado que un modelo NER es esencialmente un modelo de clasificación de tokens, podemos usar RNNs que ya conocemos para esta tarea. En este caso, cada bloque de la red recurrente devolverá el ID del token. El siguiente cuaderno de ejemplo muestra cómo entrenar un LSTM para la clasificación de tokens.

## ✍️ Cuadernos de Ejemplo: NER

Continúa tu aprendizaje en el siguiente cuaderno:

* [NER con TensorFlow](../../../../../lessons/5-NLP/19-NER/NER-TF.ipynb)

## Conclusión

Un modelo NER es un **modelo de clasificación de tokens**, lo que significa que se puede utilizar para realizar clasificación de tokens. Esta es una tarea muy común en PLN, ayudando a reconocer entidades específicas dentro del texto, incluyendo lugares, nombres, fechas, y más.

## 🚀 Desafío

Completa la tarea vinculada a continuación para entrenar un modelo de reconocimiento de entidades nombradas para términos médicos, y luego pruébalo en un conjunto de datos diferente.

## [Cuestionario posterior a la clase](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Revisión y Autoestudio

Lee el blog [La Efectividad Irrazonable de las Redes Neuronales Recurrentes](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) y sigue la sección de Lectura Adicional en ese artículo para profundizar tu conocimiento.

## [Tarea](lab/README.md)

En la tarea de esta lección, tendrás que entrenar un modelo de reconocimiento de entidades médicas. Puedes comenzar entrenando un modelo LSTM como se describe en esta lección y continuar usando el modelo de transformador BERT. Lee [las instrucciones](lab/README.md) para obtener todos los detalles.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional por parte de un humano. No nos hacemos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.