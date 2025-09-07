<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9de7847385eeeda67cfdcce1640ab72",
  "translation_date": "2025-08-24T20:29:44+00:00",
  "source_file": "lessons/5-NLP/17-GenerativeNetworks/README.md",
  "language_code": "zh"
}
-->
# 生成网络

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/117)

循环神经网络（RNN）及其门控单元变体（如长短期记忆单元 LSTM 和门控循环单元 GRU）提供了一种语言建模的机制，因为它们可以学习单词的顺序并预测序列中下一个单词。这使得我们可以使用 RNN 执行**生成任务**，例如普通文本生成、机器翻译，甚至图像描述。

> ✅ 想一想你在使用文本补全等生成任务时受益的场景。研究一下你喜欢的应用程序，看看它们是否利用了 RNN。

在上一单元中讨论的 RNN 架构中，每个 RNN 单元会生成下一个隐藏状态作为输出。然而，我们也可以为每个循环单元添加另一个输出，这样就可以输出一个**序列**（长度与原始序列相等）。此外，我们可以使用不在每一步接受输入的 RNN 单元，而是仅接受一个初始状态向量，然后生成一系列输出。

这使得可以构建不同的神经网络架构，如下图所示：

![展示常见循环神经网络模式的图片。](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.zh.jpg)

> 图片来源：[Andrej Karpaty](http://karpathy.github.io/) 的博客文章 [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

* **一对一** 是传统的神经网络，具有一个输入和一个输出
* **一对多** 是一种生成架构，接受一个输入值，并生成一系列输出值。例如，如果我们想训练一个**图像描述**网络，该网络会生成图片的文字描述，我们可以将图片作为输入，通过 CNN 获取其隐藏状态，然后通过一个循环链逐字生成描述
* **多对一** 对应于我们在上一单元中描述的 RNN 架构，例如文本分类
* **多对多** 或 **序列到序列** 对应于任务如**机器翻译**，其中第一个 RNN 将输入序列的所有信息收集到隐藏状态中，另一个 RNN 链将该状态展开为输出序列。

在本单元中，我们将专注于帮助我们生成文本的简单生成模型。为了简化，我们将使用字符级标记化。

我们将训练这个 RNN 逐步生成文本。在每一步中，我们将取一个长度为 `nchars` 的字符序列，并让网络为每个输入字符生成下一个输出字符：

![展示 RNN 生成单词 'HELLO' 的示例图片。](../../../../../translated_images/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.zh.png)

在生成文本（推理阶段）时，我们从某个**提示**开始，将其传递给 RNN 单元以生成中间状态，然后从该状态开始生成。我们一次生成一个字符，并将状态和生成的字符传递给另一个 RNN 单元以生成下一个字符，直到生成足够的字符。

<img src="images/rnn-generate-inf.png" width="60%"/>

> 图片由作者提供

## ✍️ 练习：生成网络

通过以下笔记本继续学习：

* [使用 PyTorch 的生成网络](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb)
* [使用 TensorFlow 的生成网络](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)

## 软文本生成与温度

每个 RNN 单元的输出是一个字符的概率分布。如果我们总是选择概率最高的字符作为生成文本的下一个字符，文本往往会在相同的字符序列之间“循环”，如下例所示：

```
today of the second the company and a second the company ...
```

然而，如果我们查看下一个字符的概率分布，可能会发现几个最高概率之间的差异并不大，例如一个字符的概率是 0.2，另一个是 0.19 等。例如，在寻找序列 '*play*' 的下一个字符时，下一个字符可能是空格，也可能是 **e**（如单词 *player*）。

这让我们得出结论：并不总是“公平”地选择概率最高的字符，因为选择第二高的字符仍然可能生成有意义的文本。更明智的做法是从网络输出的概率分布中**采样**字符。我们还可以使用一个参数 **温度** 来调整概率分布的平坦程度。如果我们希望增加随机性，可以使分布更平坦；如果希望更倾向于最高概率的字符，可以使分布更陡峭。

在上面链接的笔记本中探索软文本生成的实现方式。

## 总结

虽然文本生成本身可能很有用，但其主要优势在于能够从某个初始特征向量使用 RNN 生成文本。例如，文本生成可以作为机器翻译的一部分（序列到序列，在这种情况下，*编码器* 的状态向量用于生成或*解码*翻译后的消息），或者生成图像的文字描述（在这种情况下，特征向量来自 CNN 提取器）。

## 🚀 挑战

在 Microsoft Learn 上学习相关课程

* 使用 [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste) 进行文本生成

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/217)

## 复习与自学

以下文章可以扩展你的知识

* 使用马尔可夫链、LSTM 和 GPT-2 的不同文本生成方法：[博客文章](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* [Keras 文档](https://keras.io/examples/generative/lstm_character_level_text_generation/)中的文本生成示例

## [作业](lab/README.md)

我们已经了解了如何逐字符生成文本。在实验中，你将探索逐单词的文本生成。

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文档的原始语言版本为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而引起的任何误解或误读不承担责任。