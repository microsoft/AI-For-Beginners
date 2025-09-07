<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7e617f0b8de85a43957a853aba09bfeb",
  "translation_date": "2025-08-24T21:47:55+00:00",
  "source_file": "lessons/5-NLP/18-Transformers/README.md",
  "language_code": "zh"
}
-->
# 注意力机制与Transformer

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/118)

在自然语言处理（NLP）领域中，**机器翻译**是一个非常重要的问题，它是支持像Google翻译这样的工具的核心任务。在本节中，我们将重点讨论机器翻译，或者更广泛地说，任何*序列到序列*任务（也称为**句子转换**）。

使用RNN时，序列到序列任务通过两个循环网络实现，其中一个网络是**编码器**，将输入序列压缩为一个隐藏状态，而另一个网络是**解码器**，将隐藏状态展开为翻译结果。然而，这种方法存在一些问题：

* 编码器网络的最终状态很难记住句子的开头部分，因此对于长句子的模型质量较差。
* 序列中的所有单词对结果的影响是相同的。然而，实际上，输入序列中的某些特定单词对输出序列的影响往往比其他单词更大。

**注意力机制**提供了一种方法，可以为每个输入向量对RNN的每个输出预测的上下文影响赋予不同的权重。其实现方式是创建输入RNN的中间状态与输出RNN之间的快捷连接。这样，在生成输出符号y<sub>t</sub>时，我们会考虑所有输入隐藏状态h<sub>i</sub>，并赋予不同的权重系数α<sub>t,i</sub>。

![显示带有加性注意力层的编码器/解码器模型的图片](../../../../../translated_images/encoder-decoder-attention.7a726296894fb567aa2898c94b17b3289087f6705c11907df8301df9e5eeb3de.zh.png)

> [Bahdanau等人，2015](https://arxiv.org/pdf/1409.0473.pdf)中的加性注意力机制编码器-解码器模型，图片来源于[这篇博客](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)

注意力矩阵{α<sub>i,j</sub>}表示某些输入单词在生成输出序列中某个单词时的作用程度。以下是一个这样的矩阵示例：

![显示RNNsearch-50找到的示例对齐的图片，来源于Bahdanau - arviz.org](../../../../../translated_images/bahdanau-fig3.09ba2d37f202a6af11de6c82d2d197830ba5f4528d9ea430eb65fd3a75065973.zh.png)

> 图片来源于[Bahdanau等人，2015](https://arxiv.org/pdf/1409.0473.pdf)（图3）

注意力机制是当前或接近当前NLP领域最先进技术的核心。然而，添加注意力机制会显著增加模型参数的数量，这导致了RNN的扩展问题。RNN扩展的一个关键限制是其循环特性使得训练难以批量化和并行化。在RNN中，序列的每个元素需要按顺序处理，这意味着它无法轻松并行化。

![带注意力的编码器解码器](../../../../../lessons/5-NLP/18-Transformers/images/EncDecAttention.gif)

> 图片来源于[Google的博客](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)

注意力机制的采用结合了这一限制，促成了我们今天所知的最先进的Transformer模型的诞生，例如BERT和Open-GPT3。

## Transformer模型

Transformer的核心思想之一是避免RNN的顺序特性，创建一个在训练期间可并行化的模型。这通过以下两种方法实现：

* 位置编码
* 使用自注意力机制捕获模式，而不是使用RNN（或CNN）（这也是为什么介绍Transformer的论文被称为*[Attention is all you need](https://arxiv.org/abs/1706.03762)*）

### 位置编码/嵌入

位置编码的思想如下：
1. 使用RNN时，标记的相对位置由步数表示，因此不需要显式表示。
2. 然而，一旦我们切换到注意力机制，我们需要知道序列中标记的相对位置。
3. 为了获得位置编码，我们将标记序列与序列中的标记位置序列（即数字序列0,1, ...）结合。
4. 然后我们将标记位置与标记嵌入向量混合。为了将位置（整数）转换为向量，我们可以使用不同的方法：

* 可训练的嵌入，类似于标记嵌入。这是我们在这里考虑的方法。我们在标记和它们的位置上应用嵌入层，得到相同维度的嵌入向量，然后将它们相加。
* 固定位置编码函数，如原始论文中提出的。

<img src="images/pos-embedding.png" width="50%"/>

> 图片由作者提供

通过位置嵌入，我们得到的结果既嵌入了原始标记，也嵌入了它在序列中的位置。

### 多头自注意力

接下来，我们需要在序列中捕获一些模式。为此，Transformer使用了**自注意力**机制，本质上是将注意力应用于相同的输入和输出序列。应用自注意力使我们能够考虑句子中的**上下文**，并查看哪些单词是相互关联的。例如，它可以帮助我们识别代词（如*it*）所指代的单词，并将上下文纳入考虑：

![](../../../../../translated_images/CoreferenceResolution.861924d6d384a7d68d8d0039d06a71a151f18a796b8b1330239d3590bd4947eb.zh.png)

> 图片来源于[Google博客](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)

在Transformer中，我们使用**多头注意力**，以赋予网络捕获多种依赖关系的能力，例如长期与短期的单词关系、共指关系与其他关系等。

[TensorFlow Notebook](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb)中包含了Transformer层实现的更多细节。

### 编码器-解码器注意力

在Transformer中，注意力机制用于两个地方：

* 使用自注意力捕获输入文本中的模式
* 执行序列翻译——即编码器和解码器之间的注意力层。

编码器-解码器注意力与RNN中使用的注意力机制非常相似，如本节开头所述。以下动画图解说明了编码器-解码器注意力的作用。

![显示Transformer模型中评估如何执行的动画GIF](../../../../../lessons/5-NLP/18-Transformers/images/transformer-animated-explanation.gif)

由于每个输入位置可以独立映射到每个输出位置，Transformer比RNN更容易并行化，这使得更大、更具表现力的语言模型成为可能。每个注意力头可以用来学习单词之间的不同关系，从而改进下游的自然语言处理任务。

## BERT

**BERT**（Bidirectional Encoder Representations from Transformers）是一个非常大的多层Transformer网络，*BERT-base*有12层，*BERT-large*有24层。该模型首先在大规模文本数据（维基百科+书籍）上进行无监督预训练（预测句子中的被遮掩单词）。在预训练期间，模型吸收了大量的语言理解能力，这些能力可以通过微调其他数据集加以利用。这一过程被称为**迁移学习**。

![图片来源于http://jalammar.github.io/illustrated-bert/](../../../../../translated_images/jalammarBERT-language-modeling-masked-lm.34f113ea5fec4362e39ee4381aab7cad06b5465a0b5f053a0f2aa05fbe14e746.zh.png)

> 图片[来源](http://jalammar.github.io/illustrated-bert/)

## ✍️ 练习：Transformer

通过以下笔记本继续学习：

* [PyTorch中的Transformer](../../../../../lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb)
* [TensorFlow中的Transformer](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb)

## 总结

在本课中，你学习了Transformer和注意力机制，它们是NLP工具箱中的重要工具。Transformer架构有许多变体，包括BERT、DistilBERT、BigBird、OpenGPT3等，这些模型可以进行微调。[HuggingFace包](https://github.com/huggingface/)提供了一个用于训练这些架构的库，支持PyTorch和TensorFlow。

## 🚀 挑战

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/218)

## 复习与自学

* [博客文章](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/)，解释了经典的[Attention is all you need](https://arxiv.org/abs/1706.03762)论文。
* [一系列博客文章](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452)，详细解释了Transformer的架构。

## [作业](assignment.md)

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文档的原始语言版本为权威来源。对于关键信息，建议使用专业人工翻译。我们对于因使用本翻译而引起的任何误解或误读不承担责任。