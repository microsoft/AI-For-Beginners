# 知名的 CNN 架构

### VGG-16

VGG-16 是一个在 2014 年的 ImageNet 前五名分类中达到 92.7% 准确率的网络。它具有以下层结构：

![ImageNet Layers](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.zh.jpg)

如你所见，VGG 遵循传统的金字塔架构，这是一个卷积-池化层的序列。

![ImageNet Pyramid](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.zh.jpg)

> 图片来自 [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet 是微软研究院在 2015 年提出的一系列模型。ResNet 的主要思想是使用 **残差块**：

<img src="images/resnet-block.png" width="300"/>

> 图片来自 [这篇论文](https://arxiv.org/pdf/1512.03385.pdf)

使用恒等传递的原因在于让我们的层预测 **前一层的结果与残差块的输出之间的差异**，因此得名 *残差*。这些块更容易训练，并且可以构建包含数百个这样的块的网络（最常见的变体是 ResNet-52、ResNet-101 和 ResNet-152）。

你也可以将这个网络视为能够根据数据集调整其复杂性。最初，当你开始训练网络时，权重值较小，大部分信号通过恒等传递层。当训练进行时，权重变得更大，网络参数的显著性增加，网络会调整以满足正确分类训练图像所需的表达能力。

### Google Inception

Google Inception 架构在这个想法上更进一步，将每个网络层构建为多个不同路径的组合：

<img src="images/inception.png" width="400"/>

> 图片来自 [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

在这里，我们需要强调 1x1 卷积的作用，因为乍一看它们似乎没有意义。为什么我们需要使用 1x1 的滤波器遍历图像？然而，你需要记住，卷积滤波器也与多个深度通道一起工作（最初是 RGB 颜色，在后续层中是不同滤波器的通道），而 1x1 卷积用于使用不同的可训练权重将这些输入通道混合在一起。它也可以被视为在通道维度上的下采样（池化）。

这里有 [一篇关于此主题的好博客文章](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578)，以及 [原始论文](https://arxiv.org/pdf/1312.4400.pdf)。

### MobileNet

MobileNet 是一系列尺寸较小的模型，适合移动设备使用。如果你的资源有限，并且可以牺牲一些准确性，可以使用它们。它们的主要思想是所谓的 **深度可分离卷积**，允许通过空间卷积和对深度通道的 1x1 卷积的组合来表示卷积滤波器。这显著减少了参数的数量，使网络的大小更小，并且在较少数据的情况下更易于训练。

这里有 [一篇关于 MobileNet 的好博客文章](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470)。

## 结论

在本单元中，你学习了计算机视觉神经网络的主要概念——卷积网络。驱动图像分类、物体检测甚至图像生成网络的实际架构都是基于 CNN 的，只是具有更多层和一些额外的训练技巧。

## 🚀 挑战

在随附的笔记本中，底部有关于如何获得更高准确性的说明。做一些实验，看看你能否达到更高的准确性。

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/207)

## 复习与自学

虽然 CNN 最常用于计算机视觉任务，但它们通常适合提取固定大小的模式。例如，如果我们处理声音，我们也可能想使用 CNN 来寻找音频信号中的某些特定模式——在这种情况下，滤波器将是 1 维的（而这个 CNN 将被称为 1D-CNN）。此外，有时使用 3D-CNN 来提取多维空间中的特征，例如视频中发生的某些事件——CNN 可以捕捉随时间变化的特征模式。进行一些关于 CNN 可以完成的其他任务的复习和自学。

## [作业](lab/README.md)

在这个实验中，你的任务是对不同的猫和狗品种进行分类。这些图像比 MNIST 数据集更复杂，维度更高，并且类别超过 10 个。

**免责声明**：
本文件使用机器翻译的人工智能服务进行翻译。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于关键信息，建议进行专业人工翻译。我们对因使用此翻译而导致的任何误解或误释不承担责任。