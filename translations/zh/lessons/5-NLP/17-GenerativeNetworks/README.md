# 生成网络

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/117)

递归神经网络（RNN）及其门控单元变体，如长短期记忆单元（LSTM）和门控递归单元（GRU），为语言建模提供了一种机制，因为它们能够学习单词顺序并对序列中的下一个单词进行预测。这使得我们能够将RNN用于**生成任务**，例如普通文本生成、机器翻译甚至图像描述。

> ✅ 想想你在输入时受益于文本补全等生成任务的所有时刻。研究一下你最喜欢的应用程序，看看它们是否利用了RNN。

在我们在上一单元中讨论的RNN架构中，每个RNN单元都生成下一个隐藏状态作为输出。然而，我们还可以为每个递归单元添加另一个输出，这将允许我们输出一个**序列**（其长度与原始序列相等）。此外，我们可以使用不在每一步接受输入的RNN单元，仅使用一些初始状态向量，然后生成一系列输出。

这允许出现不同的神经网络架构，如下图所示：

![展示常见递归神经网络模式的图像。](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.zh.jpg)

> 图片来自博客文章 [递归神经网络的非凡有效性](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) 由 [Andrej Karpaty](http://karpathy.github.io/)

* **一对一** 是传统的神经网络，具有一个输入和一个输出
* **一对多** 是一种生成架构，接受一个输入值，并生成一系列输出值。例如，如果我们想训练一个**图像描述**网络来生成图片的文本描述，我们可以将一张图片作为输入，通过CNN获取其隐藏状态，然后让递归链逐字生成描述
* **多对一** 对应于我们在上一单元中描述的RNN架构，例如文本分类
* **多对多**，或**序列到序列**，对应于诸如**机器翻译**的任务，其中第一个RNN从输入序列中收集所有信息到隐藏状态，另一个RNN链将此状态展开为输出序列。

在本单元中，我们将专注于简单的生成模型，帮助我们生成文本。为了简单起见，我们将使用字符级标记化。

我们将逐步训练这个RNN来生成文本。在每一步中，我们将取长度为 `nchars` 的字符序列，并要求网络为每个输入字符生成下一个输出字符：

![展示单词 'HELLO' 的示例 RNN 生成。](../../../../../translated_images/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.zh.png)

在生成文本时（在推理过程中），我们从一些**提示**开始，该提示通过RNN单元生成其中间状态，然后从这个状态开始生成。我们一次生成一个字符，并将状态和生成的字符传递给另一个RNN单元以生成下一个字符，直到生成足够的字符。

<img src="images/rnn-generate-inf.png" width="60%"/>

> 图片由作者提供

## ✍️ 练习：生成网络

在以下笔记本中继续你的学习：

* [使用 PyTorch 的生成网络](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb)
* [使用 TensorFlow 的生成网络](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)

## 软文本生成与温度

每个RNN单元的输出是字符的概率分布。如果我们总是选择概率最高的字符作为生成文本中的下一个字符，文本往往会在相同的字符序列之间“循环”，就像这个例子：

```
today of the second the company and a second the company ...
```

然而，如果我们查看下一个字符的概率分布，可能会发现几个最高概率之间的差异并不大，例如，一个字符的概率为0.2，另一个为0.19等。例如，在查找序列 '*play*' 中的下一个字符时，下一个字符可以是空格或**e**（如单词 *player* 中）。

这使我们得出结论，选择概率更高的字符并不总是“公平”，因为选择第二高的字符仍然可能导致有意义的文本。更明智的做法是从网络输出给出的概率分布中**采样**字符。我们还可以使用一个参数，**温度**，这将平坦化概率分布，以便我们想增加更多随机性，或者使其更陡峭，如果我们想更贴近最高概率的字符。

探索上述笔记本中如何实现这种软文本生成。

## 结论

虽然文本生成本身可能有用，但主要的好处来自于使用RNN从某个初始特征向量生成文本的能力。例如，文本生成作为机器翻译的一部分（在这种情况下，*编码器*的状态向量用于生成或*解码*翻译消息），或者生成图像的文本描述（在这种情况下，特征向量来自CNN提取器）。

## 🚀 挑战

在 Microsoft Learn 上参加一些关于这个主题的课程

* 使用 [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste) 的文本生成

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/217)

## 复习与自学

以下是一些扩展你知识的文章

* 使用马尔可夫链、LSTM 和 GPT-2 的文本生成不同方法：[博客文章](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* [Keras 文档](https://keras.io/examples/generative/lstm_character_level_text_generation/) 中的文本生成示例

## [作业](lab/README.md)

我们已经看到如何逐字符生成文本。在实验室中，你将探索词级文本生成。

**免责声明**：
本文件是使用机器翻译AI服务进行翻译的。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而导致的任何误解或错误解释不承担责任。