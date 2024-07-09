# 卷积神经网络

我们之前已经看到神经网络在处理图像方面非常出色，即使是一层感知器也能够以合理的准确度识别MNIST数据集中的手写数字。然而，MNIST数据集非常特殊，所有数字都居中显示在图像中，这使得任务变得更简单。

## [预备知识测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/107)

在现实生活中，我们希望能够识别图像中的对象，而不管它们在图像中的确切位置。计算机视觉与通常的分类不同，因为当我们试图在图像中找到某个特定的对象时，我们会扫描图像寻找特定的**模式**及其组合。例如，当寻找猫时，我们首先可能会找水平线，它们可以组成猫的触须，然后触须的某种组合可以告诉我们这实际上是一张猫的图片。某种模式的相对位置和存在性很重要，而不是它们在图像上的确切位置。

为了提取模式，我们将使用**卷积滤波器**的概念。如你所知，图像由一个二维矩阵或者带有颜色深度的三维张量表示。应用滤波器意味着我们取一个相对较小的**滤波核（filter kernel）**矩阵，对原始图像中的每个像素计算与相邻点的加权平均值。我们可以将此视为一个小窗口在整个图像上滑动，并根据滤波核矩阵中的权重对所有像素进行平均。![垂直边缘滤镜](../images/filter-vert.png) | ![水平边缘滤镜](../images/filter-horiz.png)
----|----

> 图片由Dmitry Soshnikov提供

例如，如果我们将3x3的垂直边缘和水平边缘滤波器应用于MNIST数字，我们可以在原始图像中的垂直和水平边缘处获得高亮的部分（例如高值）。因此，这两个滤波器可以用于“寻找”边缘。类似地，我们可以设计不同的滤波器来寻找其他低级模式：

<img src="../images/lmfilters.jpg" width="500" align="center"/>> [Leung-Malik 滤波器组的图像](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

然而，尽管我们可以手动设计滤波器来提取一些模式，但我们也可以设计网络以自动学习这些模式。这是CNN的主要思想之一。

## CNN的主要思想

CNN的工作方式基于以下重要思想：

* 卷积滤波器可以提取模式
* 我们可以设计网络以自动训练滤波器* 我们可以使用相同的方法来寻找高层特征中的模式，而不仅仅是在原始图像中寻找。因此，CNN的特征提取是在特征的层次结构上进行的，从低级像素组合开始，一直到较高级别的图像部分的组合。

![分层特征提取](../images/FeatureExtractionCNN.png)

> 图片来自[Hislop-Lynch的一篇论文](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d)，基于[他们的研究](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ 练习：卷积神经网络

让我们继续探索卷积神经网络的工作原理，并通过相应的笔记本了解如何实现可训练的滤波器：
* [Convolutional Neural Networks - PyTorch](../ConvNetsPyTorch.ipynb)
* [Convolutional Neural Networks - TensorFlow](../ConvNetsTF.ipynb)

## 金字塔架构

大多数用于图像处理的CNN都采用所谓的金字塔架构。第一层卷积层通常应用于原始图像，它有相对较少的滤波器（8-16），这些滤波器对应不同的像素组合，例如水平/垂直线条。在下一级中，我们减小网络的空间维度，并增加滤波器的数量，这对应更多可能的简单特征组合。随着每一层的推进，我们向最终的分类器移动时，图像的空间维度减少，滤波器的数量增加。

以VGG-16为例，这是一个在2014年在ImageNet的top-5分类中实现92.7%准确率的网络的架构：

![ImageNet Layers](../images/vgg-16-arch1.jpg)![ImageNet金字塔](../images/vgg-16-arch.jpg)

> 图片来源：[Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## 最知名的CNN架构

[继续学习最知名的CNN架构](CNN_Architectures.zh.md)