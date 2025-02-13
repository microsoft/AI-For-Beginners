# 预训练的大型语言模型

在我们之前的所有任务中，我们都在训练一个神经网络，以使用标记数据集执行某项特定任务。对于像 BERT 这样的庞大变换模型，我们使用自我监督的语言建模来构建语言模型，然后通过进一步的领域特定训练将其专门化为特定的下游任务。然而，已经证明大型语言模型也可以在没有任何领域特定训练的情况下解决许多任务。能够做到这一点的一类模型被称为 **GPT**：生成预训练变换器。

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## 文本生成与困惑度

神经网络能够在没有下游训练的情况下执行一般任务的想法在论文 [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) 中提出。主要思想是许多其他任务可以通过 **文本生成** 进行建模，因为理解文本本质上意味着能够生成文本。由于模型是在大量包含人类知识的文本上训练的，它也变得对各种主题具有知识。

> 理解和能够生成文本也意味着对我们周围的世界有一定的了解。人们在很大程度上也是通过阅读来学习的，GPT 网络在这方面是相似的。

文本生成网络通过预测下一个单词的概率 $$P(w_N)$$ 来工作。然而，下一个单词的无条件概率等于该单词在文本语料库中的频率。GPT 能够给我们提供下一个单词的 **条件概率**，给定前面的单词：$$P(w_N | w_{n-1}, ..., w_0)$$

> 您可以在我们的 [初学者数据科学课程](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) 中阅读更多关于概率的内容。

语言生成模型的质量可以通过 **困惑度** 来定义。它是一种内在指标，允许我们在没有任何特定任务数据集的情况下衡量模型质量。它基于 *句子的概率* 的概念——模型对可能真实的句子分配高概率（即模型对其不感到 **困惑**），而对意义较少的句子分配低概率（例如 *它能做什么？*）。当我们给模型提供来自真实文本语料库的句子时，我们期望它们具有高概率和低 **困惑度**。从数学上讲，它被定义为测试集的归一化逆概率：
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**您可以使用 [Hugging Face 提供的 GPT 驱动文本编辑器进行文本生成实验](https://transformer.huggingface.co/doc/gpt2-large)**。在此编辑器中，您开始撰写文本，按 **[TAB]** 将为您提供多个完成选项。如果它们太短，或者您对它们不满意——再次按 [TAB]，您将获得更多选项，包括更长的文本片段。

## GPT 是一个家族

GPT 不是单一模型，而是由 [OpenAI](https://openai.com) 开发和训练的一系列模型。

在 GPT 模型下，我们有：

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| 具有最多 15 亿个参数的语言模型。 | 具有最多 1750 亿个参数的语言模型 | 100T 参数，接受图像和文本输入，并输出文本。 |

GPT-3 和 GPT-4 模型可作为 [Microsoft Azure 的认知服务](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste)，以及 [OpenAI API](https://openai.com/api/) 使用。

## 提示工程

由于 GPT 已在大量数据上进行训练以理解语言和代码，因此它们会根据输入（提示）提供输出。提示是 GPT 的输入或查询，通过这些输入，用户向模型提供有关下一步完成的任务的指令。为了引出期望的结果，您需要最有效的提示，这涉及选择正确的单词、格式、短语甚至符号。这种方法被称为 [提示工程](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)

[该文档](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) 为您提供有关提示工程的更多信息。

## ✍️ 示例笔记本：[与 OpenAI-GPT 玩耍](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

在以下笔记本中继续您的学习：

* [使用 OpenAI-GPT 和 Hugging Face Transformers 生成文本](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## 结论

新的通用预训练语言模型不仅建模语言结构，还包含大量自然语言。因此，它们可以有效地用于在零样本或少样本设置中解决一些 NLP 任务。

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。尽管我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于关键信息，建议进行专业的人类翻译。我们对因使用此翻译而导致的任何误解或误释不承担责任。