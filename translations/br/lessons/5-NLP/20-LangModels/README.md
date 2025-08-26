<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-26T08:44:51+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "br"
}
-->
# Modelos de Linguagem Pré-Treinados

Em todas as nossas tarefas anteriores, treinamos uma rede neural para realizar uma determinada tarefa usando um conjunto de dados rotulado. Com grandes modelos de transformadores, como o BERT, utilizamos modelagem de linguagem de forma auto-supervisionada para construir um modelo de linguagem, que é então especializado para tarefas específicas com treinamento adicional em domínios específicos. No entanto, foi demonstrado que grandes modelos de linguagem também podem resolver muitas tarefas sem QUALQUER treinamento específico de domínio. Uma família de modelos capaz de fazer isso é chamada de **GPT**: Transformador Pré-Treinado Generativo.

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Geração de Texto e Perplexidade

A ideia de uma rede neural ser capaz de realizar tarefas gerais sem treinamento adicional é apresentada no artigo [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). A ideia principal é que muitas outras tarefas podem ser modeladas usando **geração de texto**, porque entender texto essencialmente significa ser capaz de produzi-lo. Como o modelo é treinado em uma enorme quantidade de texto que abrange o conhecimento humano, ele também se torna conhecedor de uma ampla variedade de assuntos.

> Entender e ser capaz de produzir texto também implica saber algo sobre o mundo ao nosso redor. As pessoas também aprendem muito lendo, e a rede GPT é semelhante nesse aspecto.

Redes de geração de texto funcionam prevendo a probabilidade da próxima palavra $$P(w_N)$$. No entanto, a probabilidade incondicional da próxima palavra é igual à frequência dessa palavra no corpus de texto. O GPT é capaz de nos fornecer a **probabilidade condicional** da próxima palavra, dadas as anteriores: $$P(w_N | w_{n-1}, ..., w_0)$$.

> Você pode ler mais sobre probabilidades em nosso [Currículo de Ciência de Dados para Iniciantes](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

A qualidade de um modelo de geração de linguagem pode ser definida usando **perplexidade**. É uma métrica intrínseca que nos permite medir a qualidade do modelo sem qualquer conjunto de dados específico de tarefa. Ela se baseia na noção de *probabilidade de uma sentença* - o modelo atribui alta probabilidade a uma sentença que provavelmente é real (ou seja, o modelo não está **perplexo** com ela) e baixa probabilidade a sentenças que fazem menos sentido (ex.: *Pode ele faz o quê?*). Quando damos ao nosso modelo sentenças de um corpus de texto real, esperamos que elas tenham alta probabilidade e baixa **perplexidade**. Matematicamente, é definida como a probabilidade inversa normalizada do conjunto de teste:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Você pode experimentar a geração de texto usando o [editor de texto com GPT da Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. Neste editor, você começa a escrever seu texto e, ao pressionar **[TAB]**, várias opções de conclusão serão oferecidas. Se forem muito curtas ou você não estiver satisfeito com elas, pressione [TAB] novamente e terá mais opções, incluindo trechos mais longos de texto.

## GPT é uma Família

GPT não é um único modelo, mas sim uma coleção de modelos desenvolvidos e treinados pela [OpenAI](https://openai.com).

Dentro dos modelos GPT, temos:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Modelo de linguagem com até 1,5 bilhões de parâmetros. | Modelo de linguagem com até 175 bilhões de parâmetros. | 100 trilhões de parâmetros e aceita tanto entradas de imagem quanto de texto, gerando saídas em texto. |

Os modelos GPT-3 e GPT-4 estão disponíveis [como um serviço cognitivo da Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) e como [API da OpenAI](https://openai.com/api/).

## Engenharia de Prompt

Como o GPT foi treinado em grandes volumes de dados para entender linguagem e código, ele fornece respostas em resposta a entradas (prompts). Prompts são entradas ou consultas para o GPT, onde se fornecem instruções aos modelos sobre as tarefas que devem ser realizadas. Para obter um resultado desejado, é necessário o prompt mais eficaz, que envolve selecionar as palavras, formatos, frases ou até símbolos certos. Essa abordagem é chamada de [Engenharia de Prompt](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Esta documentação](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) fornece mais informações sobre engenharia de prompt.

## ✍️ Notebook de Exemplo: [Explorando o OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Continue seu aprendizado nos seguintes notebooks:

* [Gerando texto com OpenAI-GPT e Hugging Face Transformers](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Conclusão

Novos modelos de linguagem pré-treinados gerais não apenas modelam a estrutura da linguagem, mas também contêm uma vasta quantidade de linguagem natural. Assim, eles podem ser usados de forma eficaz para resolver algumas tarefas de PLN em configurações de zero-shot ou few-shot.

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.