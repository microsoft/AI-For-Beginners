# 预训练的大型语言模型

在我们之前的所有任务中，我们都是使用带标签的数据集训练神经网络来执行特定的任务。对于如BERT这样的大型transformer模型，我们使用自监督的语言建模来构建一个语言模型，然后通过进一步的领域特定训练来专门针对特定的下游任务进行专门化的训练。然而，已经证明大型语言模型也可以在没有任何领域特定训练的情况下解决许多任务。这类模型的一个例子就是**GPT**：生成式预训练变换器。

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## 文本生成和困惑度

关于神经网络能够在没有下游训练的情况下执行通用任务的想法在《语言模型是无监督多任务学习者》论文中提出。其主要观点是许多其他任务可以使用**文本生成**进行建模，因为理解文本本质上意味着能够产生文本。由于该模型是在涵盖人类知识的大量文本上进行训练的，所以它也能够具备广泛的主题知识。> 理解和能够产生文本也需要对我们周围的世界有所了解。人们也通过阅读来学习，GPT网络在这方面也是类似的。

文本生成网络通过预测下一个词的概率$$P(w_N)$$来工作。然而，下一个词的无条件概率等于文本语料库中该词的频率。而GPT能够给出给定前面词的情况下的下一个词的**条件概率**：$$P(w_N | w_{n-1}, ..., w_0)$$

> 您可以在我们的[数据科学初学者课程](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)中了解更多关于概率的内容。

语言生成模型的质量可以用**困惑度**来定义。这是一种内在的度量指标，允许我们在没有特定任务数据集的情况下衡量模型的质量。它基于*句子的概率*的概念 - 模型对可能是真实的句子分配较高的概率（即模型对其不感到困惑），对于不太合理的句子分配较低的概率（例如*Can it does what?*）。当我们给模型提供来自真实文本语料库的句子时，我们期望它们具有较高的概率和较低的**困惑度**。在数学上，它被定义为测试集的标准化的逆概率的平方根：
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$
**你可以使用[Hugging Face的GPT强力 文本编辑器](https://transformer.huggingface.co/doc/gpt2-large)进行文本生成的实验**。

在这个编辑器中，你开始写你的文本，并按下**[TAB]**键会给你几个完成选项。如果它们太短，或者你对它们不满意 - 再次按下[TAB]键，你将得到更多的选项，包括更长的文本片段。

## GPT 是一个家族

GPT不是一个单一的模型，而是由[OpenAI](https://openai.com)开发和训练的一系列模型的集合。

在GPT模型下，我们有：

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|含有高达15亿个参数的语言模型。|含有高达1750亿个参数的语言模型。|含有100万亿个参数，并且接受图像和文本输入，并输出文本。|

GPT-3和GPT-4模型可在[Microsoft Azure的认知服务](https://azure.microsoft.com/zh-cn/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste)和[OpenAI API](https://openai.com/api/)中使用。

## 提示工程

由于GPT已经在大量的数据上进行了训练以理解语言和代码，因此当对输入（提示）提供输出时，它们会根据提示返回结果。提示是GPT的输入或查询，通过提示向模型提供完成下一个任务的指令。为了获得所期望的结果，您需要选择最有效的提示，这涉及选择正确的单词、格式、短语甚至符号。这种方法被称为[提示工程](https://learn.microsoft.com/zh-cn/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)。[此文档](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum)提供了更多关于prompt工程的信息。

## ✍️ 示例笔记本：[与OpenAI-GPT玩耍](../GPT-PyTorch.ipynb)

继续学习以下笔记本：

* [使用OpenAI-GPT和Hugging Face Transformers生成文本](../GPT-PyTorch.ipynb)

## 结论

新的通用预训练语言模型不仅可以对语言结构进行建模，还包含大量的自然语言。因此，它们可以在零样本或少样本设置下有效地用于解决一些自然语言处理任务。

## [讲座后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)