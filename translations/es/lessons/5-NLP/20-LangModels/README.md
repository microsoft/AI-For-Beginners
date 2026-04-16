# Modelos de Lenguaje Grandes Preentrenados

En todas nuestras tareas anteriores, entrenábamos una red neuronal para realizar una tarea específica utilizando un conjunto de datos etiquetado. Con modelos transformadores grandes, como BERT, utilizamos el modelado de lenguaje de manera auto-supervisada para construir un modelo de lenguaje, que luego se especializa en tareas específicas con entrenamiento adicional en dominios concretos. Sin embargo, se ha demostrado que los modelos de lenguaje grandes también pueden resolver muchas tareas sin necesidad de entrenamiento específico en un dominio. Una familia de modelos capaz de hacer esto se llama **GPT**: Transformador Generativo Preentrenado.

## [Cuestionario previo a la clase](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Generación de Texto y Perplejidad

La idea de que una red neuronal pueda realizar tareas generales sin entrenamiento adicional se presenta en el artículo [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). La idea principal es que muchas otras tareas pueden modelarse utilizando **generación de texto**, porque entender el texto esencialmente significa ser capaz de producirlo. Debido a que el modelo está entrenado con una enorme cantidad de texto que abarca el conocimiento humano, también se vuelve experto en una amplia variedad de temas.

> Entender y ser capaz de producir texto también implica saber algo sobre el mundo que nos rodea. Las personas también aprenden en gran medida leyendo, y la red GPT es similar en este aspecto.

Las redes de generación de texto funcionan prediciendo la probabilidad de la siguiente palabra $$P(w_N)$$. Sin embargo, la probabilidad incondicional de la siguiente palabra equivale a la frecuencia de esa palabra en el corpus de texto. GPT es capaz de proporcionarnos la **probabilidad condicional** de la siguiente palabra, dadas las anteriores: $$P(w_N | w_{n-1}, ..., w_0)$$

> Puedes leer más sobre probabilidades en nuestro [Currículo de Ciencia de Datos para Principiantes](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

La calidad de un modelo generador de lenguaje puede definirse utilizando la **perplejidad**. Es una métrica intrínseca que nos permite medir la calidad del modelo sin necesidad de un conjunto de datos específico para la tarea. Se basa en la noción de *probabilidad de una oración*: el modelo asigna alta probabilidad a una oración que es probable que sea real (es decir, el modelo no está **perplejo** por ella) y baja probabilidad a oraciones que tienen menos sentido (por ejemplo, *¿Puede hacer qué?*). Cuando le damos al modelo oraciones de un corpus de texto real, esperaríamos que tengan alta probabilidad y baja **perplejidad**. Matemáticamente, se define como la probabilidad inversa normalizada del conjunto de prueba:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Puedes experimentar con la generación de texto utilizando el [editor de texto impulsado por GPT de Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. En este editor, comienzas escribiendo tu texto y al presionar **[TAB]** se te ofrecerán varias opciones de completado. Si son demasiado cortas o no estás satisfecho con ellas, presiona [TAB] nuevamente y tendrás más opciones, incluyendo fragmentos de texto más largos.

## GPT es una Familia

GPT no es un modelo único, sino una colección de modelos desarrollados y entrenados por [OpenAI](https://openai.com).

Dentro de los modelos GPT, tenemos:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Modelo de lenguaje con hasta 1.5 mil millones de parámetros. | Modelo de lenguaje con hasta 175 mil millones de parámetros. | 100T parámetros y acepta tanto entradas de texto como de imágenes, y genera texto como salida. |

Los modelos GPT-3 y GPT-4 están disponibles [como un servicio cognitivo de Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) y como [API de OpenAI](https://openai.com/api/).

## Ingeniería de Prompts

Debido a que GPT ha sido entrenado con grandes volúmenes de datos para entender lenguaje y código, proporciona resultados en respuesta a entradas (prompts). Los prompts son consultas o instrucciones que se le dan al modelo para que realice tareas específicas. Para obtener un resultado deseado, necesitas el prompt más efectivo, lo que implica seleccionar las palabras, formatos, frases o incluso símbolos adecuados. Este enfoque se llama [Ingeniería de Prompts](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Esta documentación](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) te proporciona más información sobre ingeniería de prompts.

## ✍️ Notebook de Ejemplo: [Jugando con OpenAI-GPT](GPT-PyTorch.ipynb)

Continúa tu aprendizaje en los siguientes notebooks:

* [Generación de texto con OpenAI-GPT y Hugging Face Transformers](GPT-PyTorch.ipynb)

## Conclusión

Los nuevos modelos de lenguaje preentrenados generales no solo modelan la estructura del lenguaje, sino que también contienen una gran cantidad de conocimiento en lenguaje natural. Por lo tanto, pueden utilizarse de manera efectiva para resolver algunas tareas de procesamiento de lenguaje natural en configuraciones de zero-shot o few-shot.

## [Cuestionario posterior a la clase](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

