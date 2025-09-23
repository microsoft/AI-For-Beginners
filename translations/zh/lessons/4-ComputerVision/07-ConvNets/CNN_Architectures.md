<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f7b97b375358cb51a1e098df306bf73",
  "translation_date": "2025-08-24T20:34:10+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md",
  "language_code": "zh"
}
-->
# 常见的 CNN 架构

### VGG-16

VGG-16 是一个在 2014 年 ImageNet top-5 分类中达到 92.7% 准确率的网络。它的层结构如下：

![ImageNet 层](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.zh.jpg)

如图所示，VGG 采用了传统的金字塔架构，即一系列卷积-池化层的组合。

![ImageNet 金字塔](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.zh.jpg)

> 图片来源于 [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet 是微软研究院在 2015 年提出的一系列模型。ResNet 的核心思想是使用 **残差块**：

<img src="images/resnet-block.png" width="300"/>

> 图片来源于 [这篇论文](https://arxiv.org/pdf/1512.03385.pdf)

使用恒等传递的原因是让我们的层预测前一层结果与残差块输出之间的**差值**，因此得名 *残差*。这些块更容易训练，并且可以构建包含数百个这样的块的网络（最常见的变体是 ResNet-52、ResNet-101 和 ResNet-152）。

你也可以将这个网络理解为能够根据数据集调整其复杂度。最初，在开始训练网络时，权重值较小，大部分信号通过恒等传递层。随着训练的进行，权重变大，网络参数的重要性增加，网络会调整以适应所需的表达能力，从而正确分类训练图像。

### Google Inception

Google Inception 架构将这一思想更进一步，将每一层网络构建为多个不同路径的组合：

<img src="images/inception.png" width="400"/>

> 图片来源于 [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

这里需要强调的是 1x1 卷积的作用，因为一开始它看起来没有意义。为什么需要用 1x1 滤波器处理图像？然而，你需要记住，卷积滤波器也会处理多个深度通道（最初是 RGB 颜色，在后续层中是不同滤波器的通道），而 1x1 卷积用于通过不同的可训练权重将这些输入通道混合在一起。它也可以被视为在通道维度上的降采样（池化）。

这里有一篇关于这个主题的[优秀博客文章](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578)，以及[原始论文](https://arxiv.org/pdf/1312.4400.pdf)。

### MobileNet

MobileNet 是一系列适合移动设备的小型模型。如果资源有限，并且可以牺牲一些准确性，可以使用它们。其核心思想是所谓的 **深度可分离卷积**，它通过空间卷积和深度通道上的 1x1 卷积的组合来表示卷积滤波器。这显著减少了参数数量，使网络更小，同时也更容易用较少的数据进行训练。

这里有一篇关于 MobileNet 的[优秀博客文章](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470)。

## 总结

在本单元中，你已经学习了计算机视觉神经网络的主要概念——卷积网络。现实生活中用于图像分类、目标检测甚至图像生成的网络架构，都是基于 CNN 的，只是增加了更多的层和一些额外的训练技巧。

## 🚀 挑战

在配套的笔记本中，底部有关于如何获得更高准确率的提示。尝试进行一些实验，看看是否可以实现更高的准确率。

## [课后测验](https://ff-quizzes.netlify.app/en/ai/quiz/14)

## 复习与自学

虽然 CNN 最常用于计算机视觉任务，但它们通常也适合提取固定大小的模式。例如，如果我们处理的是声音，也可以使用 CNN 来寻找音频信号中的某些特定模式——在这种情况下，滤波器将是一维的（这种 CNN 被称为 1D-CNN）。此外，有时会使用 3D-CNN 来提取多维空间中的特征，例如视频中发生的某些事件——CNN 可以捕捉随时间变化的某些特征模式。请复习并自学 CNN 在其他任务中的应用。

## [作业](lab/README.md)

在本次实验中，你的任务是对不同的猫狗品种进行分类。这些图像比 MNIST 数据集更复杂，维度更高，并且类别超过 10 个。

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而引起的任何误解或误读不承担责任。