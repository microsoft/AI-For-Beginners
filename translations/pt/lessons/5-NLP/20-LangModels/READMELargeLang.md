# Modelos de Linguagem Grande Pré-Treinados

Em todas as nossas tarefas anteriores, estávamos treinando uma rede neural para realizar uma determinada tarefa usando um conjunto de dados rotulados. Com grandes modelos de transformadores, como o BERT, utilizamos modelagem de linguagem de forma auto-supervisionada para construir um modelo de linguagem, que é então especializado para uma tarefa específica com treinamento adicional focado no domínio. No entanto, foi demonstrado que grandes modelos de linguagem também podem resolver muitas tarefas sem NENHUM treinamento específico de domínio. Uma família de modelos capaz de fazer isso é chamada de **GPT**: Transformer Generativo Pré-Treinado.

## [Quiz pré-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Geração de Texto e Perplexidade

A ideia de uma rede neural ser capaz de realizar tarefas gerais sem treinamento posterior é apresentada no artigo [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). A ideia principal é que muitas outras tarefas podem ser modeladas usando **geração de texto**, porque entender texto essencialmente significa ser capaz de produzi-lo. Como o modelo é treinado em uma enorme quantidade de texto que abrange o conhecimento humano, ele também se torna conhecedor de uma ampla variedade de assuntos.

> Compreender e ser capaz de produzir texto também implica saber algo sobre o mundo ao nosso redor. As pessoas também aprendem muito lendo, e a rede GPT é semelhante nesse aspecto.

As redes de geração de texto funcionam prevendo a probabilidade da próxima palavra $$P(w_N)$$. No entanto, a probabilidade incondicional da próxima palavra é igual à frequência dessa palavra no corpus de texto. O GPT é capaz de nos fornecer a **probabilidade condicional** da próxima palavra, dada as anteriores: $$P(w_N | w_{n-1}, ..., w_0)$$

> Você pode ler mais sobre probabilidades em nosso [Currículo de Ciência de Dados para Iniciantes](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)

A qualidade do modelo de geração de linguagem pode ser definida usando **perplexidade**. É uma métrica intrínseca que nos permite medir a qualidade do modelo sem nenhum conjunto de dados específico da tarefa. Baseia-se na noção de *probabilidade de uma frase* - o modelo atribui alta probabilidade a uma frase que provavelmente é real (ou seja, o modelo não está **perplexo** por ela), e baixa probabilidade a frases que fazem menos sentido (por exemplo, *Pode fazer o quê?*). Quando fornecemos ao nosso modelo frases de um corpus de texto real, esperaríamos que elas tivessem alta probabilidade e baixa **perplexidade**. Matematicamente, é definida como a probabilidade inversa normalizada do conjunto de teste:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Você pode experimentar a geração de texto usando [o editor de texto alimentado por GPT da Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. Neste editor, você começa a escrever seu texto, e pressionar **[TAB]** oferecerá várias opções de conclusão. Se elas forem muito curtas ou se você não estiver satisfeito com elas - pressione [TAB] novamente, e você terá mais opções, incluindo trechos de texto mais longos.

## GPT é uma Família

O GPT não é um único modelo, mas sim uma coleção de modelos desenvolvidos e treinados pela [OpenAI](https://openai.com). 

Sob os modelos GPT, temos:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Modelo de linguagem com até 1,5 bilhões de parâmetros. | Modelo de linguagem com até 175 bilhões de parâmetros | 100T de parâmetros e aceita entradas de imagem e texto, produzindo texto como saída. |

Os modelos GPT-3 e GPT-4 estão disponíveis [como um serviço cognitivo da Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) e como [API da OpenAI](https://openai.com/api/).

## Engenharia de Prompt

Como o GPT foi treinado em grandes volumes de dados para entender linguagem e código, ele fornece saídas em resposta a entradas (prompts). Prompts são as entradas ou consultas do GPT onde se fornecem instruções aos modelos sobre as tarefas que eles devem completar a seguir. Para elicitar um resultado desejado, você precisa do prompt mais eficaz, que envolve selecionar as palavras, formatos, frases ou até símbolos certos. Essa abordagem é chamada de [Engenharia de Prompt](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Esta documentação](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) fornece mais informações sobre engenharia de prompt.

## ✍️ Exemplo de Notebook: [Brincando com OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Continue seu aprendizado nos seguintes notebooks:

* [Gerando texto com OpenAI-GPT e Transformers da Hugging Face](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Conclusão

Novos modelos de linguagem pré-treinados não apenas modelam a estrutura da linguagem, mas também contêm uma vasta quantidade de linguagem natural. Assim, eles podem ser usados efetivamente para resolver algumas tarefas de PNL em configurações de zero-shot ou few-shot.

## [Quiz pós-aula](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**Isenção de responsabilidade**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.