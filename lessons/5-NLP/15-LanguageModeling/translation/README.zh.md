# 语言建模

语义嵌入，例如Word2Vec和GloVe，实际上是语言建模的第一步-创建一些以某种方式“理解”（或“代表”）语言属性的模型。

##[预讲座测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

语言建模的主要思想是以无监督的方式在未标记的数据集上进行训练。这很重要，因为我们有大量未标记的文本可用，而标记文本的数量总是受我们在标记上可以花费的精力的限制。通常，我们可以构建能够在文本中预测缺失单词的语言模型，因为很容易屏蔽文本中的一个随机单词并将其用作训练样本。

##训练嵌入在之前的例子中，我们使用了预训练的语义嵌入，但有趣的是看到这些嵌入是如何训练的。有几个可能的想法可以使用：

* **N-Gram**语言模型，通过查看N个前面的标记（N-gram）来预测标记。
* **Continuous Bag-of-Words**（CBoW），在一个标记序列$W_{-N}$，..., $W_N$中预测中间的标记$W_0$。
* **Skip-gram**，通过中间标记$W_0$来预测一组相邻的标记{$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$}。

![将单词转换为向量的论文图像](../../14-Embeddings/images/example-algorithms-for-converting-words-to-vectors.png)

> 图片来源于[这篇论文](https://arxiv.org/pdf/1301.3781.pdf)## ✍️ 示例笔记本：训练CBoW模型

请继续在以下笔记本中学习：

* [使用TensorFlow训练CBoW Word2Vec](../CBoW-TF.ipynb)
* [使用PyTorch训练CBoW Word2Vec](../CBoW-PyTorch.ipynb)


## 结论在前面的课程中，我们已经了解到词嵌入的神奇之处！现在我们知道训练词嵌入并不是一个非常复杂的任务，如果需要的话，我们应该能够针对特定领域的文本训练自己的词嵌入。

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## 复习与自学

* [官方PyTorch语言建模教程](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html)。
* [官方TensorFlow训练Word2Vec模型教程](https://www.TensorFlow.org/tutorials/text/word2vec)。
* 使用**gensim**框架在几行代码中训练常用的嵌入方法可以在[此文档](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html)中找到。## 🚀 任务: 训练Skip-Gram模型

在这个实验中，我们要求您修改本课程的代码，训练Skip-Gram模型，而不是CBoW模型。[点击阅读详细信息](../lab/README.zh.md)