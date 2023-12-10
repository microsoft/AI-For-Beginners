# 分割

我们之前学习了目标检测，它可以通过预测目标的*边界框*来定位图像中的对象。然而，对于某些任务，我们不仅需要边界框，还需要更精确的对象定位。这个任务称为**分割**。

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

分割可以被看作是**像素分类**，对于图像的**每个**像素，我们必须预测其类别（*背景*是其中一个类别）。有两种主要的分割算法：

* **语义分割**只告诉像素的类别，并且不区分同一类别的不同对象
* **实例分割**将类别划分为不同的实例。对于实例分割，这些羊是不同的对象，但对于语义分割，所有羊都被表示为一个类别。

<img src="images/instance_vs_semantic.jpeg" width="50%">

> 图片来源：[这篇博客文章](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

有不同的用于分割的神经架构，但它们都具有相同的结构。从某种意义上说，它类似于之前学到的自编码器，但我们的目标不是解构原始图像，而是解构一个 **掩码（mask）**。因此，分割网络包括以下几个部分：

* **编码器（Encoder）** 从输入图像中提取特征* **解码器** 将这些特征转换成与类别数量相对应的尺寸和通道数的**掩码图像**。

<img src="images/segm.png" width="80%">

> 图片来自[这篇论文](https://arxiv.org/pdf/2001.05566.pdf)

我们特别需要提到用于分割的损失函数。在使用经典的自编码器时，我们需要衡量两个图像之间的相似性，我们可以使用均方误差（MSE）来进行衡量。在分割中，目标掩码图像中的每个像素表示类别编号（沿第三个维度进行one-hot编码），因此我们需要使用特定于分类的损失函数 - 交叉熵损失，该损失在所有像素上进行平均。如果掩码是二进制的 - 会使用**二进制交叉熵损失**（BCE）。

> ✅ One-hot编码是一种将类别标签编码为长度等于类别数量的向量的方法。可以参考[这篇文章](https://datagy.io/sklearn-one-hot-encode/)了解这种技术。

## 医学图像分割

在本课程中，我们将通过训练神经网络来识别医学图像中的人体痣（也称为痣）来实现分割。我们将使用<a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup>数据库</a>中的皮肤镜图像作为图像来源。该数据集包含三类的200张图像：典型痣、非典型痣和黑素瘤。所有图像还包含一个相应的**掩码**，用于勾画痣的轮廓。

> ✅ 这种技术特别适用于这类医学图像，但你能想象其他哪些真实世界的应用呢？

<img alt="navi" src="images/navi.png"/>

> 来自PH<sup>2</sup>数据库的图像我们将训练一个模型，将任何黑素痣从其背景中分割出来。

## ✍️ 练习：语义分割

打开下面的笔记本了解更多关于不同语义分割架构，练习如何使用它们，并看到它们的实际效果。

* [Pytorch语义分割](SemanticSegmentationPytorch.ipynb)
* [TensorFlow语义分割](SemanticSegmentationTF.ipynb)

## [演讲后的测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## 结论

分割是一种非常强大的图像分类技术，可以实现像素级别的分类，超越了边界框的限制。它是医学成像等应用中常用的技术。

## 🚀 挑战

身体分割只是我们可以对人体图像进行的常见任务之一。其他重要的任务包括**骨骼检测**和**姿态检测**。尝试使用[OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)库，来了解如何使用姿态检测。

## 复习与自学

这篇[wikipedia文章](https://wikipedia.org/wiki/Image_segmentation)提供了关于这个技术各种应用的良好概述。在这个调查领域中，自己了解更多关于实例分割和全景分割的子域。

## [作业](lab/README.md)

在这个实验中，试试使用[Kaggle上的全身分割 MADS 数据集](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset)来进行**人体分割**。