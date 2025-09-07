<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-24T10:20:05+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "pt"
}
-->
# Modelos de Linguagem Pré-Treinados de Grande Escala

Em todas as nossas tarefas anteriores, treinámos uma rede neural para realizar uma determinada tarefa utilizando um conjunto de dados rotulado. Com modelos transformadores grandes, como o BERT, utilizamos modelagem de linguagem de forma auto-supervisionada para construir um modelo de linguagem, que é então especializado para uma tarefa específica com treino adicional específico do domínio. No entanto, foi demonstrado que modelos de linguagem de grande escala também podem resolver muitas tarefas sem QUALQUER treino específico do domínio. Uma família de modelos capaz de fazer isso é chamada de **GPT**: Transformador Generativo Pré-Treinado.

## [Questionário pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Geração de Texto e Perplexidade

A ideia de uma rede neural ser capaz de realizar tarefas gerais sem treino adicional é apresentada no artigo [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). A ideia principal é que muitas outras tarefas podem ser modeladas utilizando **geração de texto**, porque compreender texto essencialmente significa ser capaz de produzi-lo. Como o modelo é treinado com uma enorme quantidade de texto que abrange o conhecimento humano, ele também se torna conhecedor de uma ampla variedade de assuntos.

> Compreender e ser capaz de produzir texto também implica saber algo sobre o mundo ao nosso redor. As pessoas também aprendem, em grande parte, através da leitura, e a rede GPT é semelhante nesse aspeto.

Redes de geração de texto funcionam ao prever a probabilidade da próxima palavra $$P(w_N)$$. No entanto, a probabilidade incondicional da próxima palavra é igual à frequência dessa palavra no corpus de texto. O GPT é capaz de nos fornecer a **probabilidade condicional** da próxima palavra, dadas as anteriores: $$P(w_N | w_{n-1}, ..., w_0)$$.

> Pode ler mais sobre probabilidades no nosso [Currículo de Ciência de Dados para Iniciantes](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

A qualidade de um modelo de geração de linguagem pode ser definida utilizando a **perplexidade**. É uma métrica intrínseca que nos permite medir a qualidade do modelo sem qualquer conjunto de dados específico da tarefa. Baseia-se na noção de *probabilidade de uma frase* - o modelo atribui alta probabilidade a uma frase que provavelmente é real (ou seja, o modelo não está **perplexo** com ela) e baixa probabilidade a frases que fazem menos sentido (ex.: *Pode ele faz o quê?*). Quando damos ao nosso modelo frases de um corpus de texto real, esperamos que tenham alta probabilidade e baixa **perplexidade**. Matematicamente, é definida como a probabilidade inversa normalizada do conjunto de teste:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Pode experimentar a geração de texto utilizando o [editor de texto alimentado por GPT da Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. Neste editor, começa a escrever o seu texto e, ao pressionar **[TAB]**, serão oferecidas várias opções de conclusão. Se forem demasiado curtas ou não estiver satisfeito com elas, pressione [TAB] novamente e terá mais opções, incluindo trechos de texto mais longos.

## GPT é uma Família

O GPT não é um único modelo, mas sim uma coleção de modelos desenvolvidos e treinados pela [OpenAI](https://openai.com).

Dentro dos modelos GPT, temos:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Modelo de linguagem com até 1,5 mil milhões de parâmetros. | Modelo de linguagem com até 175 mil milhões de parâmetros. | 100T parâmetros e aceita tanto entradas de imagem como de texto, e produz texto. |

Os modelos GPT-3 e GPT-4 estão disponíveis [como um serviço cognitivo da Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) e como [API da OpenAI](https://openai.com/api/).

## Engenharia de Prompts

Como o GPT foi treinado com volumes vastos de dados para compreender linguagem e código, ele fornece respostas em resposta a entradas (prompts). Prompts são entradas ou consultas para o GPT, onde se fornecem instruções aos modelos sobre as tarefas que devem ser realizadas. Para obter um resultado desejado, é necessário o prompt mais eficaz, o que envolve selecionar as palavras, formatos, frases ou até símbolos certos. Esta abordagem é chamada de [Engenharia de Prompts](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Esta documentação](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) fornece-lhe mais informações sobre engenharia de prompts.

## ✍️ Notebook de Exemplo: [Explorando o OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Continue a sua aprendizagem nos seguintes notebooks:

* [Gerando texto com OpenAI-GPT e Hugging Face Transformers](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Conclusão

Novos modelos de linguagem pré-treinados gerais não apenas modelam a estrutura da linguagem, mas também contêm uma vasta quantidade de linguagem natural. Assim, podem ser utilizados de forma eficaz para resolver algumas tarefas de PLN em configurações de zero-shot ou few-shot.

## [Questionário pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.