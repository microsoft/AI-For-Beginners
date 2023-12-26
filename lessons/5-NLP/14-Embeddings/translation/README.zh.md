# 嵌入

## [预课测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/114)

当基于BoW或TF/IDF训练分类器时，我们操作的是具有长度`vocab_size`的高维词袋向量，并且从低维位置表示向量显式地转换为稀疏的one-hot表示。然而，这种one-hot表示不是内存高效的。此外，每个单词都被独立地对待，即one-hot编码的向量不表示单词之间的任何语义相似性。

**嵌入**的想法是用低维稠密向量来表示单词，这些向量在某种程度上反映了单词的语义含义。我们稍后将讨论如何构建有意义的单词嵌入，但现在让我们将嵌入视为降低单词向量维度的一种方式。

因此，嵌入层将以单词作为输入，并产生指定`embedding_size`的输出向量。在某种意义上，它非常类似于`Linear`层，但它不需要一个one-hot编码的向量作为输入，而是可以接受一个单词编号作为输入，从而避免创建大的one-hot编码向量。通过在分类器网络中使用嵌入层作为第一层，我们可以从词袋模型切换到**嵌入包**模型，其中我们首先将文本中的每个单词转换为相应的嵌入向量，然后计算所有这些嵌入向量的聚合函数，例如`sum`、`average`或`max`。

![展示了一个用于五个序列单词的嵌入分类器的图像。](../images/embedding-classifier-example.png)

> 图片由作者创建

## ✍️ 练习：嵌入模型

在以下笔记本中继续学习：
* [PyTorch中的嵌入](../EmbeddingsPyTorch.ipynb)* [Embeddings TensorFlow](../EmbeddingsTF.ipynb)

## 语义嵌入：Word2Vec

虽然嵌入层学习到了将单词映射到向量表示的方法，但是这种表示方式并没有太多的语义意义。我们希望学习到一种向量表示，使得相似的单词或者同义词在向量空间中相互靠近（比如欧几里得距离）。

为了实现这个目标，我们需要在大量的文本集合上以一种特定的方式预训练我们的嵌入模型。训练语义嵌入的一种方法叫做[Word2Vec](https://en.wikipedia.org/wiki/Word2vec)。它基于两种主要的架构来生成单词的分布式表示：

- **连续词袋模型**（CBoW）- 在这个架构中，我们训练模型从周围的上下文中预测一个单词。给定ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$，模型的目标是从$(W_{-2},W_{-1},W_1,W_2)$预测$W_0$。
- **连续Skip-Gram模型**与CBoW相反。该模型使用上下文窗口中的单词来预测当前的单词。CBoW更快，而skip-gram更慢，但在表示不常见的单词方面做得更好。

![显示CBoW和skip-gram算法将单词转换为向量的图像](../images/example-algorithms-for-converting-words-to-vectors.png)

> 图片来自[这篇论文](https://arxiv.org/pdf/1301.3781.pdf)

Word2Vec预训练的嵌入（以及其他类似的模型，例如GloVe）也可以用于神经网络中的嵌入层的替代。但是，我们需要处理词汇表，因为用于预训练Word2Vec / GloVe的词汇表可能与我们文本语料库中的词汇表不同。请查看上面的Notebooks，了解如何解决这个问题。

## 上下文嵌入

传统的预训练嵌入表示（如Word2Vec）存在一个关键限制，即词义消歧的问题。虽然预训练嵌入可以捕捉到一些单词在上下文中的含义，但是每个单词的所有可能含义都被编码成相同的嵌入。这可能会在下游模型中引起问题，因为许多单词（如“play”）在不同的上下文中有不同的含义。

例如，在这两个不同的句子中，“play”这个词有着相当不同的意义：

- 我去剧院看了一场**剧**。
- 约翰想和他的朋友**玩**。

以上的预训练嵌入表示将“play”这个词的这两个意义都表示为相同的嵌入。为了克服这个限制，我们需要基于**语言模型**构建嵌入，该模型在大型文本语料库上进行训练，并且*了解*在不同的上下文中如何组合单词。讨论上下文嵌入超出了本教程的范围，但我们将在本课程后面讲到语言模型时再回头讨论这个话题。## 结论

在本课程中，你了解了如何在TensorFlow和Pytorch中构建和使用嵌入层，以更好地反映单词的语义含义。

## 🚀 挑战

Word2Vec已经被用于一些有趣的应用，包括生成歌词和诗歌。阅读[这篇文章](https://www.politetype.com/blog/word2vec-color-poems)，该文章详细介绍了作者如何使用Word2Vec来生成诗歌。还可以观看[Dan Shiffmann的这个视频](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain)，了解另一种解释这个技术的方法。然后尝试将这些技术应用到你自己的文本语料库中，可能是从Kaggle获取的。

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/214)

## 回顾和自学

阅读这篇关于Word2Vec的论文：[Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [作业：笔记本](assignment.zh.md)