# 注意机制和Transformer

## [预讲座测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/118)

自然语言处理领域中最重要的问题之一是**机器翻译**，这是支撑Google翻译等工具的基本任务。在本节中，我们将专注于机器翻译，或者更一般地说，任何*序列到序列*的任务（也称为**句子转导**）。

使用循环神经网络（RNN），序列到序列是通过两个循环网络实现的，其中一个网络，**编码器**，将输入序列转化为隐藏状态，而另一个网络，**解码器**，将这个隐藏状态展开为翻译结果。这种方法存在几个问题：

* 编码器网络的最终状态很难记住句子的开头，从而导致对于长句子的模型质量较差。
* 序列中的所有单词对结果具有相同的影响。然而，在现实中，输入序列中的特定单词往往比其他单词对顺序输出的结果影响更大。**注意机制**提供了一种方法来评估RNN每个输入向量对于输出预测的上下文影响。其实现方式是在输入RNN和输出RNN之间创建中间状态的捷径。通过这种方式，在生成输出符号y<sub>t</sub>时，我们将考虑所有的输入隐藏状态h<sub>i</sub>，并赋予不同的权重系数&alpha;<sub>t,i</sub>。

![显示带有加性注意层的编码器/解码器模型的图像](../images/encoder-decoder-attention.png)

>来自[Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf)的加法注意机制编码器-解码器模型，引用自[这篇博文](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)

注意矩阵{&alpha;<sub>i,j</sub>}表示某些输入单词在生成输出序列中某个单词时的重要程度。下面是一个示例：

![显示RNNsearch-50找到的示例对齐，摘自Bahdanau - arviz.org](../images/bahdanau-fig3.png)> 来自 [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf) 的图3

注意机制在自然语言处理的当前或最新研究中起着很大的作用。然而，添加注意机制会大大增加模型参数的数量，这导致了在循环神经网络中遇到的扩展问题。扩展循环神经网络的一个关键限制是模型的循环特性使得批处理和并行化训练变得困难。在循环神经网络中，每个序列元素都需要按顺序处理，这意味着无法轻易进行并行化处理。

![带有注意机制的编码器-解码器](../images/EncDecAttention.gif)

> 来自 [Google's Blog](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html) 

通过采用注意机制并结合这个限制，现在的Transformer模型成为了我们今天所知道和使用的最先进模型，如BERT和Open-GPT3。## Transformer模型

Transformer模型的主要思想之一是避免RNN的顺序性，并创建一个在训练过程中可以并行化的模型。这通过实现两个想法来实现:

* 位置编码
* 使用自注意机制来捕捉模式，而不是使用RNN(或CNN) (这就是为什么引入transformer的论文被称为"注意力就是一切" *[Attention is all you need](https://arxiv.org/abs/1706.03762)*

### 位置编码/嵌入位置编码的思想如下：
1. 在使用RNN时，标记的相对位置由步数表示，因此不需要明确地表示。
2. 然而，一旦切换到注意力机制，我们就需要知道序列中标记之间的相对位置。
3. 为了获得位置编码，我们在标记序列上增加了一个标记位置序列（即，一系列数字0,1, …）。
4. 然后，我们将标记位置与标记嵌入向量混合。为了将位置（整数）转换为向量，我们可以使用不同的方法：

* 可训练的嵌入，类似于标记嵌入。这是我们在这里考虑的方法。我们在标记和它们的位置的基础上应用嵌入层，得到相同维度的嵌入向量，然后将它们相加。
* 固定的位置编码函数，如原始论文中所提出的。

![位置编码](../images/pos-embedding.png)> 作者提供的图像

通过位置嵌入我们得到的结果，既嵌入了原始令牌，也嵌入了它在序列中的位置。

### 多头自注意力

接下来，我们需要捕捉序列中的一些模式。为此，transformers 使用了**自注意力**机制，该机制实质上是将注意力应用于相同的输入和输出序列。应用自注意力使我们能够考虑句子中的**上下文**，并看到哪些单词之间存在关联。例如，它使我们能够看到哪些单词由于指代关系而相关，并且还考虑了上下文：

![](../images/CoreferenceResolution.png)

> 图片来源于[Google博客](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)

在transformers中，我们使用**多头注意力（Multi-Head Attention）**以便让网络具备捕捉多个不同类型依赖关系的能力，例如长期依赖与短期依赖、共指与其他依赖等等。

[TensorFlow Notebook](../TransformersTF.ipynb)包含了有关transformer层实现的更多细节。

### 编码器-解码器注意力

在transformers中，注意力机制在两个位置上被使用：* 使用自注意力机制来捕捉输入文本中的模式
* 执行序列翻译 - 它是编码器和解码器之间的注意力层。

编码器-解码器注意力机制与RNN中使用的注意力机制非常相似，如本节开头所述。这个动画图解释了编码器-解码器注意力的作用。

![动画GIF展示了如何在transformer模型中执行评估。](.。/images/transformer-animated-explanation.gif)

由于每个输入位置都独立映射到每个输出位置，因此transformer可以比RNN更好地并行化，这使得可以构建更大更具表达力的语言模型。每个注意力头都可以用于学习不同单词之间的关系，从而改善下游的自然语言处理任务。## BERT

**BERT**（双向编码器转换器）是一个非常大的多层Transformer网络，*BERT-base*有12层，*BERT-large*有24层。该模型首先通过无监督训练（预测句子中的掩码词）在大规模文本数据（维基百科+图书）上进行预训练。在预训练过程中，模型获得了丰富的语言理解能力，然后可以通过微调与其他数据集结合使用。这个过程称为**迁移学习**。

![图片来源于http://jalammar.github.io/illustrated-bert/](../images/jalammarBERT-language-modeling-masked-lm.png)

> 图片来源：[http://jalammar.github.io/illustrated-bert/](http://jalammar.github.io/illustrated-bert/)

## ✍️ 练习：转换器继续学习以下的笔记本：

* [使用PyTorch的Transformers](../TransformersPyTorch.ipynb)
* [使用TensorFlow的Transformers](../TransformersTF.ipynb)

## 结论

在本课程中，你学习了Transformer和Attention Mechanism，这些都是在NLP工具箱中非常重要的工具。Transformer架构有很多变种，包括BERT、DistilBERT、BigBird、OpenGPT3等等，这些都可以进行微调。[HuggingFace package](https://github.com/huggingface/)提供了一个存储库，可以使用PyTorch和TensorFlow训练许多这些架构。

## 🚀 挑战

## [Lecture Quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/218)

## 复习与自学

* [博客文章](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/)，解释了关于变压器的经典论文[Attention is all you need](https://arxiv.org/abs/1706.03762)。
* [一系列博客文章](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452)关于变压器的详细架构解释。

## [任务](assignment.zh.md)