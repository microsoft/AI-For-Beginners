# Modelos de Linguagem de Grande Escala Pré-Treinados

Em todas as nossas tarefas anteriores, treinamos uma rede neural para realizar uma determinada tarefa usando um conjunto de dados rotulado. Com grandes modelos transformadores, como o BERT, utilizamos modelagem de linguagem de forma autossupervisionada para construir um modelo de linguagem, que é então especializado para tarefas específicas com treinamento adicional em domínios específicos. No entanto, foi demonstrado que grandes modelos de linguagem também podem resolver muitas tarefas sem QUALQUER treinamento específico de domínio. Uma família de modelos capaz de fazer isso é chamada de **GPT**: Transformador Generativo Pré-Treinado.

## [Questionário pré-aula](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Geração de Texto e Perplexidade

A ideia de uma rede neural ser capaz de realizar tarefas gerais sem treinamento adicional é apresentada no artigo [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). A ideia principal é que muitas outras tarefas podem ser modeladas usando **geração de texto**, porque compreender texto essencialmente significa ser capaz de produzi-lo. Como o modelo é treinado em uma enorme quantidade de texto que abrange o conhecimento humano, ele também se torna conhecedor de uma ampla variedade de assuntos.

> Compreender e ser capaz de produzir texto também implica saber algo sobre o mundo ao nosso redor. As pessoas também aprendem muito lendo, e a rede GPT é semelhante nesse aspecto.

Redes de geração de texto funcionam prevendo a probabilidade da próxima palavra $$P(w_N)$$. No entanto, a probabilidade incondicional da próxima palavra é igual à frequência dessa palavra no corpus de texto. O GPT é capaz de nos fornecer a **probabilidade condicional** da próxima palavra, dado as palavras anteriores: $$P(w_N | w_{n-1}, ..., w_0)$$

> Você pode ler mais sobre probabilidades em nosso [Currículo de Ciência de Dados para Iniciantes](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

A qualidade de um modelo de geração de linguagem pode ser definida usando a **perplexidade**. É uma métrica intrínseca que nos permite medir a qualidade do modelo sem qualquer conjunto de dados específico para a tarefa. Ela se baseia na noção de *probabilidade de uma sentença* - o modelo atribui alta probabilidade a uma sentença que provavelmente é real (ou seja, o modelo não está **perplexo** com ela) e baixa probabilidade a sentenças que fazem menos sentido (por exemplo, *Pode isso faz o quê?*). Quando fornecemos ao nosso modelo sentenças de um corpus de texto real, esperamos que elas tenham alta probabilidade e baixa **perplexidade**. Matematicamente, é definida como a probabilidade inversa normalizada do conjunto de teste:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Você pode experimentar a geração de texto usando o [editor de texto baseado em GPT da Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. Neste editor, você começa a escrever seu texto e, ao pressionar **[TAB]**, várias opções de conclusão serão oferecidas. Se forem muito curtas ou você não estiver satisfeito com elas, pressione [TAB] novamente, e você terá mais opções, incluindo trechos de texto mais longos.

## GPT é uma Família

O GPT não é um único modelo, mas sim uma coleção de modelos desenvolvidos e treinados pela [OpenAI](https://openai.com).

Dentro da família de modelos GPT, temos:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Modelo de linguagem com até 1,5 bilhões de parâmetros. | Modelo de linguagem com até 175 bilhões de parâmetros. | 100 trilhões de parâmetros, aceita entradas de texto e imagem, e gera saídas em texto. |

Os modelos GPT-3 e GPT-4 estão disponíveis [como um serviço cognitivo da Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) e também como [API da OpenAI](https://openai.com/api/).

## Engenharia de Prompt

Como o GPT foi treinado em grandes volumes de dados para compreender linguagem e código, ele fornece saídas em resposta a entradas (prompts). Prompts são entradas ou consultas para o GPT, onde se fornecem instruções aos modelos sobre as tarefas a serem realizadas. Para obter o resultado desejado, é necessário criar o prompt mais eficaz, o que envolve selecionar as palavras, formatos, frases ou até mesmo símbolos corretos. Essa abordagem é chamada de [Engenharia de Prompt](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Esta documentação](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) fornece mais informações sobre engenharia de prompt.

## ✍️ Notebook de Exemplo: [Experimentando com OpenAI-GPT](GPT-PyTorch.ipynb)

Continue seu aprendizado nos seguintes notebooks:

* [Gerando texto com OpenAI-GPT e Hugging Face Transformers](GPT-PyTorch.ipynb)

## Conclusão

Novos modelos de linguagem geral pré-treinados não apenas modelam a estrutura da linguagem, mas também contêm uma vasta quantidade de linguagem natural. Assim, eles podem ser usados de forma eficaz para resolver algumas tarefas de PLN em configurações de zero-shot ou few-shot.

## [Questionário pós-aula](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

