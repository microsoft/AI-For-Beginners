# Modelos de lenguaje grandes previamente entrenados

En todas nuestras tareas anteriores, estábamos entrenando una red neuronal para realizar una determinada tarea utilizando un conjunto de datos etiquetados. Con modelos transformadores grandes, como BERT, utilizamos el modelado de lenguaje de forma autosupervisada para construir un modelo de lenguaje, que luego se especializa para tareas posteriores específicas con capacitación adicional en un dominio específico. Sin embargo, se ha demostrado que los modelos de lenguaje grandes también pueden resolver muchas tareas sin NINGUNA capacitación específica en el dominio. Una familia de modelos capaces de hacer eso se llama **GPT**: Transformador generativo preentrenado.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Generación de texto y perplejidad

La idea de que una red neuronal pueda realizar tareas generales sin entrenamiento posterior se presenta en [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) papel. La idea principal es que muchas otras tareas se pueden modelar utilizando **generación de texto**, porque comprender el texto significa esencialmente poder producirlo. Debido a que el modelo se entrena con una gran cantidad de texto que abarca el conocimiento humano, también adquiere conocimientos sobre una amplia variedad de temas.

> Comprender y ser capaz de producir texto también implica saber algo sobre el mundo que nos rodea. La gente también aprende leyendo en gran medida, y la red GPT es similar a este respecto.

Las redes de generación de texto funcionan prediciendo la probabilidad de la siguiente palabra $$P(w_N)$$ Sin embargo, la probabilidad incondicional de la siguiente palabra es igual a la frecuencia de esta palabra en el corpus de texto. GPT es capaz de darnos **probabilidad condicional** de la siguiente palabra, dadas las anteriores: $$P(w_N | w_{n-1}, ..., w_0)$$

> Puedes leer más sobre probabilidades en nuestro [Data Science for Beginers Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)

La calidad del modelo generador de lenguaje se puede definir usando **perplejidad**. Es una métrica intrínseca que nos permite medir la calidad del modelo sin ningún conjunto de datos específico de la tarea. Se basa en la noción de *probabilidad de una oración*: el modelo asigna alta probabilidad a una oración que probablemente sea real (es decir, el modelo no está **perplejo** por ella), y baja probabilidad a oraciones que hacen menos sentido (p. ej. *¿Puede hacer qué?*). Cuando damos a nuestro modelo oraciones de un corpus de texto real, esperaríamos que tuvieran una alta probabilidad y una baja **perplejidad**. Matemáticamente, se define como probabilidad inversa normalizada del conjunto de prueba:
$$
\mathrm{Perplejidad}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$

**Puedes experimentar con la generación de texto usando el [editor de texto con tecnología GPT de Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. En este editor, comienza a escribir su texto y al presionar **[TAB]** se le ofrecerán varias opciones para completarlo. Si son demasiado cortos o no está satisfecho con ellos, presione [TAB] nuevamente y tendrá más opciones, incluidos fragmentos de texto más largos.

## GPT es una familia

GPT no es un modelo único, sino más bien una colección de modelos desarrollados y entrenados por [OpenAI](https://openai.com).

Bajo los modelos GPT, tenemos:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Language model with upto 1.5 billion parameters. | Language model with up to 175 billion parameters | 100T parameters and accepts both image and text inputs and outputs text. |


Los modelos GPT-3 y GPT-4 están disponibles [as a cognitive service from Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), and as [OpenAI API](https://openai.com/api/).

## Ingeniería rápida

Debido a que GPT ha sido capacitado con grandes volúmenes de datos para comprender el lenguaje y el código, proporciona resultados en respuesta a las entradas (indicaciones). Las indicaciones son entradas o consultas de GPT mediante las cuales uno proporciona instrucciones a los modelos sobre las tareas que completarán a continuación. Para obtener el resultado deseado, necesita el mensaje más eficaz que implica seleccionar las palabras, formatos, frases o incluso símbolos correctos. Este enfoque es [Ingeniería rápida](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id= académico-77998-bethanycheum)

[This documentation](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) le proporciona más información sobre ingeniería rápida.

## ✍️ Cuaderno de ejemplo: [Playing with OpenAI-GPT](GPT-PyTorch.ipynb)

Continúa tu aprendizaje en los siguientes cuadernos:

* [Generating text with OpenAI-GPT and Hugging Face Transformers](GPT-PyTorch.ipynb)

## Conclusión

Los nuevos modelos de lenguaje generales previamente entrenados no solo modelan la estructura del lenguaje, sino que también contienen una gran cantidad de lenguaje natural. Por lo tanto, se pueden utilizar de manera efectiva para resolver algunas tareas de PNL en entornos de cero tareas o de pocas oportunidades.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)
