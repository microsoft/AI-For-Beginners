<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-24T21:50:21+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "zh"
}
-->
# 预训练大型语言模型

在我们之前的所有任务中，我们都使用标注数据集训练神经网络来完成特定任务。而对于像 BERT 这样的大型 Transformer 模型，我们通过自监督的方式进行语言建模，构建一个语言模型，然后通过进一步的领域特定训练将其专门化用于特定的下游任务。然而，研究表明，大型语言模型甚至可以在没有任何领域特定训练的情况下解决许多任务。这类能够实现这一点的模型家族被称为 **GPT**：生成式预训练 Transformer。

## [课前测验](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## 文本生成与困惑度

神经网络能够在没有下游训练的情况下完成通用任务的想法，最早在论文 [《语言模型是无监督的多任务学习者》](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) 中提出。其核心思想是，许多其他任务可以通过**文本生成**来建模，因为理解文本本质上意味着能够生成文本。由于模型在包含人类知识的大量文本上进行了训练，它也因此对各种主题变得熟悉。

> 理解并生成文本也意味着对周围世界有所了解。人类在很大程度上也是通过阅读学习的，而 GPT 网络在这方面与人类类似。

文本生成网络通过预测下一个单词的概率 $$P(w_N)$$ 来工作。然而，下一个单词的无条件概率等于该单词在文本语料库中的出现频率。GPT 能够为我们提供下一个单词的**条件概率**，即基于前面的单词：$$P(w_N | w_{n-1}, ..., w_0)$$

> 您可以在我们的 [《数据科学入门课程》](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability) 中了解更多关于概率的内容。

语言生成模型的质量可以通过**困惑度**来定义。这是一种内在的度量方法，可以在没有任何任务特定数据集的情况下衡量模型的质量。它基于*句子概率*的概念——模型会为可能是真实的句子分配高概率（即模型对其不**困惑**），而对不太合理的句子（例如 *Can it does what?*）分配低概率。当我们将真实文本语料库中的句子输入模型时，我们期望它们具有高概率和低**困惑度**。数学上，困惑度定义为测试集的归一化逆概率：
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**您可以使用 [Hugging Face 提供的 GPT 驱动文本编辑器](https://transformer.huggingface.co/doc/gpt2-large) 进行文本生成实验**。在这个编辑器中，您可以开始编写文本，按下 **[TAB]** 键会为您提供几个补全选项。如果选项太短或您不满意，可以再次按下 [TAB] 键，您将获得更多选项，包括更长的文本片段。

## GPT 是一个家族

GPT 不是单一模型，而是由 [OpenAI](https://openai.com) 开发和训练的一系列模型。

在 GPT 模型家族中，我们有：

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|语言模型，参数量高达 15 亿。| 语言模型，参数量高达 1750 亿 | 参数量达 100 万亿，支持图像和文本输入，输出为文本。|

GPT-3 和 GPT-4 模型可以通过 [Microsoft Azure 的认知服务](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) 和 [OpenAI API](https://openai.com/api/) 使用。

## 提示工程

由于 GPT 在大量数据上进行了训练，能够理解语言和代码，因此它会根据输入（提示）生成输出。提示是 GPT 的输入或查询，用户通过提示向模型提供任务指令以完成下一步操作。为了获得理想的结果，您需要设计最有效的提示，这涉及选择合适的词语、格式、短语甚至符号。这种方法被称为 [提示工程](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)。

[此文档](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) 提供了有关提示工程的更多信息。

## ✍️ 示例笔记本：[探索 OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

通过以下笔记本继续学习：

* [使用 OpenAI-GPT 和 Hugging Face Transformers 生成文本](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## 总结

新的通用预训练语言模型不仅能够建模语言结构，还包含大量自然语言知识。因此，它们可以在零样本或少样本的情况下有效地解决一些自然语言处理任务。

## [课后测验](https://ff-quizzes.netlify.app/en/ai/quiz/40)

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文档的原始语言版本为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用本翻译而引起的任何误解或误读不承担责任。