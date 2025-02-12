# 语言建模

语义嵌入，例如 Word2Vec 和 GloVe，实际上是 **语言建模** 的第一步——创建能够在某种程度上 *理解*（或 *表示*）语言本质的模型。

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

语言建模的主要思想是在无标签数据集上以无监督的方式进行训练。这一点很重要，因为我们有大量的无标签文本可用，而有标签文本的数量总是受到我们在标记上花费的努力的限制。通常，我们可以构建能够 **预测文本中缺失的单词** 的语言模型，因为在文本中随机屏蔽一个单词并将其用作训练样本是很简单的。

## 训练嵌入

在之前的示例中，我们使用了预训练的语义嵌入，但观察这些嵌入是如何训练的也很有趣。有几种可能的思路可以使用：

* **N-Gram** 语言建模，当我们通过查看 N 个之前的标记来预测一个标记（N-gram）
* **连续词袋模型**（CBoW），当我们在标记序列 $W_{-N}$, ..., $W_N$ 中预测中间标记 $W_0$ 时。
* **跳字模型**，我们从中间标记 $W_0$ 预测一组邻近的标记 {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$}。

![来自论文的将单词转换为向量的示例算法](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.zh.png)

> 图片来自 [这篇论文](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ 示例笔记本：训练 CBoW 模型

在以下笔记本中继续学习：

* [使用 TensorFlow 训练 CBoW Word2Vec](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [使用 PyTorch 训练 CBoW Word2Vec](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## 结论

在之前的课程中，我们看到单词嵌入的效果就像魔法一样！现在我们知道训练单词嵌入并不是一项非常复杂的任务，如果需要，我们应该能够为特定领域的文本训练自己的单词嵌入。

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## 复习与自学

* [官方 PyTorch 语言建模教程](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html)。
* [官方 TensorFlow 训练 Word2Vec 模型教程](https://www.TensorFlow.org/tutorials/text/word2vec)。
* 使用 **gensim** 框架在几行代码中训练最常用的嵌入的过程在 [这份文档中](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html) 有描述。

## 🚀 [作业：训练跳字模型](lab/README.md)

在实验中，我们挑战你修改本课的代码，以训练跳字模型，而不是 CBoW。 [阅读详情](lab/README.md)

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。虽然我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于关键信息，建议进行专业人工翻译。我们对因使用本翻译而产生的任何误解或误读不承担任何责任。