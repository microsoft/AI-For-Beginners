# Modelos de Lenguaje de Gran Tamaño Preentrenados

En todas nuestras tareas anteriores, entrenábamos una red neuronal para realizar una tarea específica utilizando un conjunto de datos etiquetados. Con modelos de transformador grandes, como BERT, utilizamos el modelado del lenguaje de manera auto-supervisada para construir un modelo de lenguaje, que luego se especializa para tareas específicas de acuerdo con un entrenamiento adicional en dominios específicos. Sin embargo, se ha demostrado que los grandes modelos de lenguaje también pueden resolver muchas tareas sin NINGÚN entrenamiento específico de dominio. Una familia de modelos capaces de hacer esto se llama **GPT**: Transformador Generativo Preentrenado.

## [Cuestionario previo a la conferencia](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Generación de Texto y Perplejidad

La idea de que una red neuronal pueda realizar tareas generales sin entrenamiento posterior se presenta en el artículo [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). La idea principal es que muchas otras tareas pueden ser modeladas utilizando **generación de texto**, porque entender texto significa, esencialmente, ser capaz de producirlo. Dado que el modelo se entrena con una gran cantidad de texto que abarca el conocimiento humano, también se vuelve conocedor de una amplia variedad de temas.

> Entender y ser capaz de producir texto también implica saber algo sobre el mundo que nos rodea. Las personas también aprenden leyendo en gran medida, y la red GPT es similar en este aspecto.

Las redes de generación de texto funcionan prediciendo la probabilidad de la siguiente palabra $$P(w_N)$$. Sin embargo, la probabilidad incondicional de la siguiente palabra es igual a la frecuencia de esta palabra en el corpus de texto. GPT es capaz de darnos la **probabilidad condicional** de la siguiente palabra, dado las anteriores: $$P(w_N | w_{n-1}, ..., w_0)$$

> Puedes leer más sobre probabilidades en nuestro [Currículo de Ciencia de Datos para Principiantes](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)

La calidad del modelo de generación de lenguaje se puede definir utilizando **perplejidad**. Es una métrica intrínseca que nos permite medir la calidad del modelo sin ningún conjunto de datos específico para la tarea. Se basa en la noción de *probabilidad de una oración*: el modelo asigna alta probabilidad a una oración que es probable que sea real (es decir, el modelo no está **perplejo** por ella), y baja probabilidad a oraciones que tienen menos sentido (por ejemplo, *¿Puede hacer qué?*). Cuando le damos a nuestro modelo oraciones de un corpus de texto real, esperaríamos que tuvieran alta probabilidad y baja **perplejidad**. Matemáticamente, se define como la probabilidad inversa normalizada del conjunto de prueba:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Puedes experimentar con la generación de texto utilizando [el editor de texto impulsado por GPT de Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. En este editor, comienzas a escribir tu texto, y al presionar **[TAB]** se te ofrecerán varias opciones de finalización. Si son demasiado cortas, o no estás satisfecho con ellas, presiona [TAB] nuevamente y tendrás más opciones, incluyendo fragmentos de texto más largos.

## GPT es una Familia

GPT no es un solo modelo, sino una colección de modelos desarrollados y entrenados por [OpenAI](https://openai.com). 

Bajo los modelos GPT, tenemos:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Modelo de lenguaje con hasta 1.5 mil millones de parámetros. | Modelo de lenguaje con hasta 175 mil millones de parámetros | 100T parámetros y acepta tanto entradas de imagen como de texto y produce texto. |

Los modelos GPT-3 y GPT-4 están disponibles [como un servicio cognitivo de Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), y como [API de OpenAI](https://openai.com/api/).

## Ingeniería de Prompts

Debido a que GPT ha sido entrenado con grandes volúmenes de datos para entender el lenguaje y el código, proporciona salidas en respuesta a entradas (prompts). Los prompts son las entradas o consultas de GPT mediante las cuales se dan instrucciones a los modelos sobre las tareas que deben completar a continuación. Para obtener un resultado deseado, necesitas el prompt más efectivo, lo que implica seleccionar las palabras, formatos, frases o incluso símbolos correctos. Este enfoque se llama [Ingeniería de Prompts](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)

[Esta documentación](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) te proporciona más información sobre la ingeniería de prompts.

## ✍️ Cuaderno de Ejemplo: [Jugando con OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Continúa tu aprendizaje en los siguientes cuadernos:

* [Generando texto con OpenAI-GPT y Transformers de Hugging Face](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Conclusión

Los nuevos modelos de lenguaje preentrenados generales no solo modelan la estructura del lenguaje, sino que también contienen una gran cantidad de lenguaje natural. Por lo tanto, pueden ser utilizados de manera efectiva para resolver algunas tareas de PLN en configuraciones de cero disparos o pocos disparos.

## [Cuestionario posterior a la conferencia](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Si bien nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o malas interpretaciones que surjan del uso de esta traducción.