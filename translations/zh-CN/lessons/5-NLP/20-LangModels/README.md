# 预训练大型语言模型

在我们之前的所有任务中，我们都使用带标签的数据集训练神经网络来完成特定任务。而对于像 BERT 这样的大型 Transformer 模型，我们通过自监督的方式进行语言建模来构建语言模型，然后通过进一步的领域特定训练使其专注于特定的下游任务。然而，研究表明，大型语言模型也可以在没有任何领域特定训练的情况下解决许多任务。这类能够实现这一目标的模型家族被称为 **GPT**：生成式预训练 Transformer。

## [课前测验](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## 文本生成与困惑度

神经网络能够在没有下游训练的情况下完成通用任务的理念在论文 [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) 中提出。其核心思想是许多其他任务可以通过 **文本生成** 来建模，因为理解文本本质上意味着能够生成文本。由于模型在包含人类知识的大量文本上进行了训练，它也因此对广泛的主题有了深入的了解。

> 理解并能够生成文本也意味着对周围世界有所了解。人类在很大程度上也是通过阅读来学习的，而 GPT 网络在这方面与人类类似。

文本生成网络通过预测下一个词的概率 $$P(w_N)$$ 来工作。然而，下一个词的无条件概率等于该词在文本语料库中的出现频率。GPT 能够提供下一个词的 **条件概率**，即基于前面的词：$$P(w_N | w_{n-1}, ..., w_0)$$

> 您可以在我们的 [数据科学初学者课程](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) 中了解更多关于概率的内容。

语言生成模型的质量可以通过 **困惑度** 来定义。这是一种内在指标，可以在没有任何任务特定数据集的情况下衡量模型质量。它基于 *句子的概率* 的概念——模型对可能是真实的句子赋予高概率（即模型对其不 **困惑**），而对不太合理的句子（例如 *Can it does what?*）赋予低概率。当我们给模型提供真实文本语料库中的句子时，我们希望它们具有高概率和低 **困惑度**。数学上，困惑度定义为测试集的归一化逆概率：
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**您可以使用 [Hugging Face 的 GPT 驱动文本编辑器](https://transformer.huggingface.co/doc/gpt2-large) 进行文本生成实验**。在这个编辑器中，您开始编写文本，按下 **[TAB]** 键后会提供几个补全选项。如果选项太短或您不满意，可以再次按下 [TAB] 键，您将获得更多选项，包括更长的文本片段。

## GPT 是一个家族

GPT 不是单一模型，而是由 [OpenAI](https://openai.com) 开发和训练的一系列模型。

在 GPT 模型家族中，我们有：

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|语言模型，参数量高达 15 亿。| 语言模型，参数量高达 1750 亿。| 参数量达 100 万亿，支持图像和文本输入，并输出文本。|

GPT-3 和 GPT-4 模型可以通过 [Microsoft Azure 的认知服务](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) 和 [OpenAI API](https://openai.com/api/) 使用。

## 提示工程

由于 GPT 在大量数据上进行了训练以理解语言和代码，它能够根据输入（提示）生成输出。提示是 GPT 的输入或查询，用户通过提示向模型提供任务指令以完成后续任务。为了获得期望的结果，您需要最有效的提示，这涉及选择合适的词语、格式、短语甚至符号。这种方法被称为 [提示工程](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)。

[此文档](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) 提供了有关提示工程的更多信息。

## ✍️ 示例笔记本：[使用 OpenAI-GPT 进行实验](GPT-PyTorch.ipynb)

通过以下笔记本继续学习：

* [使用 OpenAI-GPT 和 Hugging Face Transformers 生成文本](GPT-PyTorch.ipynb)

## 结论

新的通用预训练语言模型不仅能够建模语言结构，还包含大量自然语言知识。因此，它们可以在零样本或少样本设置中有效地解决一些 NLP 任务。

## [课后测验](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

