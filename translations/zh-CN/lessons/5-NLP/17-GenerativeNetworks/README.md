# 生成网络

## [课前测验](https://ff-quizzes.netlify.app/en/ai/quiz/33)

循环神经网络（RNN）及其门控单元变体（如长短时记忆单元 LSTM 和门控循环单元 GRU）提供了一种语言建模机制，它们可以学习单词的顺序并预测序列中的下一个单词。这使得我们可以使用 RNN 执行**生成任务**，例如普通文本生成、机器翻译，甚至图像描述。

> ✅ 想想你在输入时受益于文本补全等生成任务的所有场景。研究一下你喜欢的应用程序，看看它们是否使用了 RNN。

在我们上一单元讨论的 RNN 架构中，每个 RNN 单元会生成下一个隐藏状态作为输出。然而，我们也可以为每个循环单元添加另一个输出，这样就可以输出一个**序列**（与原始序列长度相等）。此外，我们可以使用不在每一步接受输入的 RNN 单元，只接受一些初始状态向量，然后生成一系列输出。

这使得可以构建不同的神经网络架构，如下图所示：

![展示常见循环神经网络模式的图片。](../../../../../translated_images/zh-CN/unreasonable-effectiveness-of-rnn.541ead816778f42d.webp)

> 图片来源于 [Andrej Karpaty](http://karpathy.github.io/) 的博客文章 [循环神经网络的非凡有效性](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)

* **一对一**是传统的神经网络，具有一个输入和一个输出
* **一对多**是一种生成架构，接受一个输入值并生成一系列输出值。例如，如果我们想训练一个**图像描述**网络来生成图片的文本描述，可以将图片作为输入，通过 CNN 获得其隐藏状态，然后通过循环链逐字生成描述
* **多对一**对应于我们在上一单元中描述的 RNN 架构，例如文本分类
* **多对多**或**序列到序列**对应于任务如**机器翻译**，其中第一个 RNN 收集输入序列中的所有信息到隐藏状态，另一个 RNN 链将该状态展开为输出序列。

在本单元中，我们将重点关注帮助生成文本的简单生成模型。为了简化，我们将使用字符级标记化。

我们将训练这个 RNN 逐步生成文本。在每一步中，我们将取长度为 `nchars` 的字符序列，并要求网络为每个输入字符生成下一个输出字符：

![展示 RNN 生成单词 'HELLO' 的示例图片。](../../../../../translated_images/zh-CN/rnn-generate.56c54afb52f9781d.webp)

在生成文本（推理阶段）时，我们从某个**提示**开始，将其传递给 RNN 单元以生成中间状态，然后从该状态开始生成。我们一次生成一个字符，并将状态和生成的字符传递给另一个 RNN 单元以生成下一个字符，直到生成足够的字符。

<img src="../../../../../translated_images/zh-CN/rnn-generate-inf.5168dc65e0370eea.webp" width="60%"/>

> 图片由作者提供

## ✍️ 练习：生成网络

通过以下笔记本继续学习：

* [使用 PyTorch 的生成网络](GenerativePyTorch.ipynb)
* [使用 TensorFlow 的生成网络](GenerativeTF.ipynb)

## 软文本生成与温度

每个 RNN 单元的输出是一个字符的概率分布。如果我们总是选择概率最高的字符作为生成文本的下一个字符，文本可能会出现“循环”现象，重复相同的字符序列，如以下示例：

```
today of the second the company and a second the company ...
```

然而，如果我们查看下一个字符的概率分布，可能会发现几个最高概率之间的差异并不大，例如一个字符的概率为 0.2，另一个为 0.19 等。例如，在寻找序列 '*play*' 的下一个字符时，下一个字符可能是空格，也可能是 **e**（如单词 *player*）。

这让我们得出结论：选择概率最高的字符并不总是“公平”的，因为选择第二高的字符仍可能生成有意义的文本。更明智的做法是从网络输出的概率分布中**采样**字符。我们还可以使用一个参数 **温度**，来平滑概率分布，以增加随机性，或者使分布更陡峭，以更倾向于选择最高概率的字符。

在上述链接的笔记本中探索软文本生成的实现方式。

## 总结

虽然文本生成本身可能很有用，但其主要优势在于能够从某些初始特征向量使用 RNN 生成文本。例如，文本生成可以作为机器翻译的一部分（序列到序列，在这种情况下，来自*编码器*的状态向量用于生成或*解码*翻译后的消息），或者生成图像的文本描述（在这种情况下，特征向量来自 CNN 提取器）。

## 🚀 挑战

在 Microsoft Learn 上学习相关课程：

* 使用 [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste) 进行文本生成

## [课后测验](https://ff-quizzes.netlify.app/en/ai/quiz/34)

## 复习与自学

以下文章可以扩展你的知识：

* 使用马尔可夫链、LSTM 和 GPT-2 进行文本生成的不同方法：[博客文章](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* [Keras 文档](https://keras.io/examples/generative/lstm_character_level_text_generation/)中的文本生成示例

## [作业](lab/README.md)

我们已经了解了如何逐字符生成文本。在实验中，你将探索逐词生成文本。

---

