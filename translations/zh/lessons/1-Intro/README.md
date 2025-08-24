<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-24T20:31:38+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "zh"
}
-->
> 图片由 [Dmitry Soshnikov](http://soshnikov.com) 提供

随着时间的推移，计算资源变得更加廉价，同时可用的数据量也大幅增加，因此神经网络方法在许多领域（如计算机视觉或语音理解）中开始展现出与人类竞争的卓越表现。在过去的十年里，“人工智能”这个术语大多被用作“神经网络”的同义词，因为我们听到的大多数人工智能成功案例都基于神经网络。

我们可以通过创建国际象棋程序的演变来观察这些方法的变化：

* 早期的国际象棋程序基于搜索算法——程序会显式地尝试估算对手在接下来几步中的可能走法，并根据几步内可以达到的最佳局面选择最优走法。这种方法促成了所谓的 [alpha-beta 剪枝](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) 搜索算法的发展。
* 搜索策略在游戏后期效果较好，因为此时搜索空间由于可能走法较少而受到限制。然而，在游戏开局阶段，搜索空间非常庞大，因此可以通过从人类棋局中学习来改进算法。后来的实验采用了所谓的 [基于案例的推理](https://en.wikipedia.org/wiki/Case-based_reasoning)，程序会在知识库中寻找与当前棋局非常相似的案例。
* 能够战胜人类玩家的现代程序基于神经网络和 [强化学习](https://en.wikipedia.org/wiki/Reinforcement_learning)，这些程序通过长时间与自己对弈并从自己的错误中学习来掌握棋艺——这与人类学习下棋的方式非常相似。然而，计算机程序可以在更短的时间内进行更多的对局，因此学习速度远快于人类。

✅ 研究一下其他由人工智能参与的游戏。

同样，我们也可以看到“对话程序”（可能通过图灵测试）的开发方法是如何变化的：

* 早期的此类程序，例如 [Eliza](https://en.wikipedia.org/wiki/ELIZA)，基于非常简单的语法规则，并将输入句子重新表述为问题。
* 现代助手，如 Cortana、Siri 或 Google Assistant，都是混合系统，它们使用神经网络将语音转换为文本并识别用户意图，然后利用某些推理或显式算法来执行所需的操作。
* 在未来，我们可能会看到完全基于神经网络的模型能够独立处理对话。最近的 GPT 和 [Turing-NLG](https://turing.microsoft.com/) 系列神经网络在这一领域展现了巨大的成功。

> 图片由 Dmitry Soshnikov 提供，[照片](https://unsplash.com/photos/r8LmVbUKgns) 来自 [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto)，Unsplash

## 最近的人工智能研究

近年来，神经网络研究的快速增长始于 2010 年左右，当时大型公共数据集开始变得可用。一组名为 [ImageNet](https://en.wikipedia.org/wiki/ImageNet) 的庞大图像集合（包含约 1400 万张标注图像）催生了 [ImageNet 大规模视觉识别挑战赛](https://image-net.org/challenges/LSVRC/)。

![ILSVRC 准确率](../../../../lessons/1-Intro/images/ilsvrc.gif)

> 图片由 [Dmitry Soshnikov](http://soshnikov.com) 提供

2012 年，[卷积神经网络](../4-ComputerVision/07-ConvNets/README.md) 首次被用于图像分类，这使得分类错误率显著下降（从接近 30% 降至 16.4%）。2015 年，微软研究院的 ResNet 架构[达到了人类水平的准确率](https://doi.org/10.1109/ICCV.2015.123)。

从那时起，神经网络在许多任务中表现出了非常成功的效果：

---

年份 | 达到人类水平的任务
-----|-----------------
2015 | [图像分类](https://doi.org/10.1109/ICCV.2015.123)
2016 | [对话语音识别](https://arxiv.org/abs/1610.05256)
2018 | [自动机器翻译](https://arxiv.org/abs/1803.05567)（中译英）
2020 | [图像描述生成](https://arxiv.org/abs/2009.13682)

在过去几年中，我们见证了大型语言模型（如 BERT 和 GPT-3）的巨大成功。这主要是因为有大量的通用文本数据可用，这使得我们能够训练模型来捕捉文本的结构和意义，先在通用文本集合上进行预训练，然后将这些模型专门化用于更具体的任务。我们将在本课程后续部分中学习更多关于[自然语言处理](../5-NLP/README.md)的内容。

## 🚀 挑战

在互联网上进行探索，找出你认为人工智能最有效的应用领域。是地图应用程序、语音转文字服务，还是视频游戏？研究该系统是如何构建的。

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## 复习与自学

通过阅读[这节课](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML)来回顾人工智能和机器学习的历史。从该课程顶部的手绘笔记或本节课中选取一个元素，深入研究其文化背景，以了解其演变过程。

**作业**：[游戏创作活动](assignment.md)

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文档的原始语言版本为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用本翻译而引起的任何误解或误读不承担责任。