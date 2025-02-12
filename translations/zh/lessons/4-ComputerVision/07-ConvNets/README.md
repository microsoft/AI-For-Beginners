# 卷积神经网络

我们之前已经看到，神经网络在处理图像方面表现相当不错，甚至单层感知器也能够以合理的准确率识别 MNIST 数据集中的手写数字。然而，MNIST 数据集非常特殊，所有数字都居中于图像中，这使得任务变得简单。

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/107)

在现实生活中，我们希望能够识别图像中的物体，而不论它们在图像中的确切位置。计算机视觉不同于一般的分类，因为当我们试图在图像中找到某个特定物体时，我们是在扫描图像，寻找一些特定的 **模式** 及其组合。例如，当寻找一只猫时，我们首先可能会寻找可以形成胡须的水平线，然后某种胡须的组合可以告诉我们，这实际上是一只猫的图像。相对位置和某些模式的存在是重要的，而不是它们在图像上的确切位置。

为了提取模式，我们将使用 **卷积滤波器** 的概念。正如你所知，图像由 2D 矩阵或带有颜色深度的 3D 张量表示。应用滤波器意味着我们取相对较小的 **滤波器内核** 矩阵，并对原始图像中的每个像素计算与邻近点的加权平均。我们可以将其视为一个小窗口在整个图像上滑动，并根据滤波器内核矩阵中的权重对所有像素进行平均。

![垂直边缘滤波器](../../../../../translated_images/filter-vert.b7148390ca0bc356ddc7e55555d2481819c1e86ddde9dce4db5e71a69d6f887f.zh.png) | ![水平边缘滤波器](../../../../../translated_images/filter-horiz.59b80ed4feb946efbe201a7fe3ca95abb3364e266e6fd90820cb893b4d3a6dda.zh.png)
----|----

> 图片由 Dmitry Soshnikov 提供

例如，如果我们对 MNIST 数字应用 3x3 的垂直边缘和水平边缘滤波器，我们可以在原始图像中获得高亮（例如，高值）的位置，这些位置对应于垂直和水平边缘。因此，这两个滤波器可以用来“寻找”边缘。类似地，我们可以设计不同的滤波器来寻找其他低级模式：
你已接受训练的数据截止到 2023 年 10 月。

> [Leung-Malik 滤波器组](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

然而，虽然我们可以手动设计滤波器来提取一些模式，我们也可以设计网络，使其能够自动学习模式。这是卷积神经网络（CNN）背后的主要思想之一。

## CNN 背后的主要思想

CNN 的工作原理基于以下重要思想：

* 卷积滤波器可以提取模式
* 我们可以以某种方式设计网络，使得滤波器能够自动训练
* 我们可以使用相同的方法在高级特征中找到模式，而不仅仅是在原始图像中。因此，CNN 特征提取在特征层次上工作，从低级像素组合开始，一直到更高级的图像部分组合。

![分层特征提取](../../../../../translated_images/FeatureExtractionCNN.d9b456cbdae7cb643fde3032b81b2940e3cf8be842e29afac3f482725ba7f95c.zh.png)

> 图片来自 [Hislop-Lynch 的论文](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d)，基于 [他们的研究](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ 练习：卷积神经网络

让我们继续探索卷积神经网络的工作原理，以及如何实现可训练的滤波器，通过以下笔记本进行实践：

* [卷积神经网络 - PyTorch](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb)
* [卷积神经网络 - TensorFlow](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)

## 金字塔架构

大多数用于图像处理的 CNN 遵循一种所谓的金字塔架构。应用于原始图像的第一个卷积层通常具有相对较少的滤波器（8-16），这些滤波器对应于不同的像素组合，例如水平/垂直线条的笔画。在下一个层级中，我们减少网络的空间维度，并增加滤波器的数量，这对应于更多简单特征的可能组合。随着每一层的推进，朝向最终分类器，图像的空间维度减小，而滤波器的数量增加。

作为例子，让我们看看 VGG-16 的架构，这个网络在 2014 年的 ImageNet 前 5 名分类中达到了 92.7% 的准确率：

![ImageNet 层](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.zh.jpg)

![ImageNet 金字塔](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.zh.jpg)

> 图片来自 [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## 最知名的 CNN 架构

[继续学习最知名的 CNN 架构](CNN_Architectures.md)

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。虽然我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于重要信息，建议进行专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。