# 注意力机制与变换器

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/118)

自然语言处理领域中最重要的问题之一是**机器翻译**，这是一个支撑像谷歌翻译等工具的基本任务。在这一部分，我们将专注于机器翻译，或者更一般地说，任何*序列到序列*的任务（这也被称为**句子转导**）。

使用循环神经网络（RNN）时，序列到序列的实现是通过两个递归网络来完成的，其中一个网络，**编码器**，将输入序列压缩成一个隐藏状态，而另一个网络，**解码器**，将这个隐藏状态展开为翻译结果。这种方法存在几个问题：

* 编码器网络的最终状态很难记住句子的开头，从而导致长句子的模型质量较差。
* 序列中的所有单词对结果的影响相同。然而，在现实中，输入序列中的特定单词对顺序输出的影响往往比其他单词更大。

**注意力机制**提供了一种对每个输入向量在RNN每个输出预测中的上下文影响进行加权的方法。它的实现方式是创建输入RNN和输出RNN之间的中间状态的快捷方式。通过这种方式，在生成输出符号 y<sub>t</sub> 时，我们将考虑所有输入隐藏状态 h<sub>i</sub>，并使用不同的权重系数 α<sub>t,i</sub>。

![展示带有加性注意力层的编码器/解码器模型的图像](../../../../../translated_images/encoder-decoder-attention.7a726296894fb567aa2898c94b17b3289087f6705c11907df8301df9e5eeb3de.zh.png)

> 该编码器-解码器模型与加性注意力机制见于 [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf)，引用自 [这篇博客文章](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)

注意力矩阵 {α<sub>i,j</sub>} 表示某些输入单词在生成输出序列中给定单词的程度。以下是这样一个矩阵的示例：

![展示由RNNsearch-50找到的示例对齐的图像，取自Bahdanau - arviz.org](../../../../../translated_images/bahdanau-fig3.09ba2d37f202a6af11de6c82d2d197830ba5f4528d9ea430eb65fd3a75065973.zh.png)

> 图自 [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf) (图3)

注意力机制在当今或近乎当前的自然语言处理技术中起着重要作用。然而，添加注意力机制会大大增加模型参数的数量，这导致了RNN的扩展问题。扩展RNN的一个关键限制是模型的递归性质使得批处理和并行化训练变得具有挑战性。在RNN中，序列的每个元素需要按顺序处理，这意味着它不能轻易并行化。

![带有注意力的编码器解码器](../../../../../lessons/5-NLP/18-Transformers/images/EncDecAttention.gif)

> 图自 [Google的博客](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)

注意力机制的采用结合这一限制导致了我们今天所知和使用的最先进的变换器模型的创建，例如BERT和Open-GPT3。

## 变换器模型

变换器背后的主要思想之一是避免RNN的顺序特性，并创建一个在训练过程中可并行化的模型。这是通过实现两个思想来实现的：

* 位置编码
* 使用自注意力机制来捕捉模式，而不是使用RNN（或CNN）（这就是介绍变换器的论文被称为 *[注意力就是你所需要的一切](https://arxiv.org/abs/1706.03762)* 的原因）

### 位置编码/嵌入

位置编码的思想如下：
1. 使用RNN时，标记的相对位置由步骤数表示，因此不需要显式表示。
2. 然而，一旦我们切换到注意力机制，我们需要知道序列中标记的相对位置。
3. 为了获取位置编码，我们用序列中的标记位置序列（即数字序列0,1,...）增强我们的标记序列。
4. 然后，我们将标记位置与标记嵌入向量混合。为了将位置（整数）转换为向量，我们可以使用不同的方法：

* 可训练的嵌入，类似于标记嵌入。这是我们在这里考虑的方法。我们在标记及其位置之上应用嵌入层，得到相同维度的嵌入向量，然后将它们相加。
* 固定位置编码函数，如原始论文中所提议的。

<img src="images/pos-embedding.png" width="50%"/>

> 作者提供的图像

通过位置嵌入得到的结果同时嵌入了原始标记及其在序列中的位置。

### 多头自注意力

接下来，我们需要捕捉序列中的一些模式。为此，变换器使用**自注意力**机制，这本质上是对同一序列应用的注意力。应用自注意力使我们能够考虑句子中的**上下文**，并查看哪些单词是相互关联的。例如，它使我们能够看到哪些单词是由指代词（如 *它*）引用的，并且还考虑上下文：

![](../../../../../translated_images/CoreferenceResolution.861924d6d384a7d68d8d0039d06a71a151f18a796b8b1330239d3590bd4947eb.zh.png)

> 图自 [Google博客](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)

在变换器中，我们使用**多头注意力**来赋予网络捕捉多种不同类型依赖关系的能力，例如长短期单词关系、共指关系等。

[TensorFlow Notebook](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb) 包含有关变换器层实现的更多细节。

### 编码器-解码器注意力

在变换器中，注意力用于两个地方：

* 使用自注意力捕捉输入文本中的模式
* 执行序列翻译——这是编码器与解码器之间的注意力层。

编码器-解码器注意力与本节开始时描述的RNN中使用的注意力机制非常相似。这个动画图解释了编码器-解码器注意力的作用。

![展示变换器模型中如何执行评估的动画GIF。](../../../../../lessons/5-NLP/18-Transformers/images/transformer-animated-explanation.gif)

由于每个输入位置独立映射到每个输出位置，变换器比RNN更好地进行并行化，这使得能够构建更大且更具表现力的语言模型。每个注意力头可以用来学习单词之间的不同关系，从而改善下游自然语言处理任务。

## BERT

**BERT**（来自变换器的双向编码器表示）是一个非常大的多层变换器网络，其中 *BERT-base* 有12层，*BERT-large* 有24层。该模型首先在一个大型文本数据集（维基百科 + 书籍）上进行预训练，采用无监督训练（预测句子中被屏蔽的单词）。在预训练期间，模型吸收了显著的语言理解能力，这可以通过微调与其他数据集结合使用。这个过程被称为**迁移学习**。

![图片来自 http://jalammar.github.io/illustrated-bert/](../../../../../translated_images/jalammarBERT-language-modeling-masked-lm.34f113ea5fec4362e39ee4381aab7cad06b5465a0b5f053a0f2aa05fbe14e746.zh.png)

> 图片 [来源](http://jalammar.github.io/illustrated-bert/)

## ✍️ 练习：变换器

在以下笔记本中继续学习：

* [PyTorch中的变换器](../../../../../lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb)
* [TensorFlow中的变换器](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb)

## 结论

在本课中，您了解了变换器和注意力机制，这些都是自然语言处理工具箱中的重要工具。变换器架构有许多变体，包括BERT、DistilBERT、BigBird、OpenGPT3等，可以进行微调。[HuggingFace包](https://github.com/huggingface/) 提供了一个用于训练这些架构的库，支持PyTorch和TensorFlow。

## 🚀 挑战

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/218)

## 复习与自学

* [博客文章](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/)，解释经典的 [注意力就是你所需要的一切](https://arxiv.org/abs/1706.03762) 论文。
* [一系列博客文章](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452) 详细解释变换器架构。

## [作业](assignment.md)

**免责声明**：
本文件使用基于机器的人工智能翻译服务进行翻译。虽然我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应视为权威来源。对于关键信息，建议进行专业人工翻译。我们对因使用此翻译而产生的任何误解或误释不承担责任。