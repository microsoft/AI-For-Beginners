# 分割

我们之前学习了物体检测，它允许我们通过预测物体的 *边界框* 来定位图像中的物体。然而，对于某些任务，我们不仅需要边界框，还需要更精确的物体定位。这个任务被称为 **分割**。

## [课前小测](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

分割可以被视为 **像素分类**，对于图像的 **每个** 像素，我们必须预测其类别（*背景* 是其中一个类别）。分割算法主要有两种：

* **语义分割** 仅仅告诉我们像素的类别，而不区分同一类别的不同物体。
* **实例分割** 将类别划分为不同的实例。

对于实例分割，这些羊是不同的物体，但对于语义分割，所有的羊都被表示为一个类别。

<img src="images/instance_vs_semantic.jpeg" width="50%">

> 图片来自 [这篇博客文章](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

有不同的神经网络架构用于分割，但它们都有相同的结构。在某种程度上，它类似于你之前学习的自编码器，但我们的目标不是解构原始图像，而是解构一个 **掩膜**。因此，分割网络具有以下部分：

* **编码器** 从输入图像中提取特征
* **解码器** 将这些特征转换为 **掩膜图像**，其大小和通道数与类别数相对应。

<img src="images/segm.png" width="80%">

> 图片来自 [这篇出版物](https://arxiv.org/pdf/2001.05566.pdf)

我们特别需要提到用于分割的损失函数。当使用经典的自编码器时，我们需要测量两幅图像之间的相似性，我们可以使用均方误差 (MSE) 来做到这一点。在分割中，目标掩膜图像中的每个像素表示类别编号（在第三维度上进行独热编码），因此我们需要使用特定于分类的损失函数 - 交叉熵损失，平均所有像素。如果掩膜是二元的 - 使用 **二元交叉熵损失** (BCE)。

> ✅ 独热编码是一种将类别标签编码为长度等于类别数的向量的方法。查看 [这篇文章](https://datagy.io/sklearn-one-hot-encode/) 以了解这种技术。

## 医学影像的分割

在本课中，我们将通过训练网络识别医学图像上的人类痣（也称为胎记）来看到分割的实际应用。我们将使用 <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> 数据库</a> 的皮肤镜图像作为图像来源。该数据集包含三类共200幅图像：典型痣、非典型痣和黑色素瘤。所有图像还包含一个对应的 **掩膜**，勾勒出痣的轮廓。

> ✅ 这种技术特别适用于这种类型的医学影像，但你能想象其他什么现实世界的应用？

<img alt="navi" src="images/navi.png"/>

> 图片来自 PH<sup>2</sup> 数据库

我们将训练一个模型，从背景中分割出任何痣。

## ✍️ 练习：语义分割

打开下面的笔记本，了解更多关于不同语义分割架构的内容，练习与它们的合作，并观察它们的实际应用。

* [语义分割 Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [语义分割 TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [课后小测](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## 结论

分割是一种非常强大的图像分类技术，超越了边界框，达到了像素级分类。它在医学影像等多种应用中被广泛使用。

## 🚀 挑战

身体分割只是我们可以用人像图像进行的常见任务之一。另一个重要任务包括 **骨架检测** 和 **姿态检测**。尝试使用 [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) 库，看看姿态检测如何被使用。

## 复习与自学

这篇 [维基百科文章](https://wikipedia.org/wiki/Image_segmentation) 提供了对该技术各种应用的良好概述。自行深入了解实例分割和全景分割在这一研究领域的子领域。

## [作业](lab/README.md)

在这个实验中，尝试使用 [全身分割 MADS 数据集](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) 来进行 **人体分割**。

**免责声明**：  
本文件是使用机器翻译的人工智能翻译服务进行翻译的。尽管我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应视为权威来源。对于关键信息，建议进行专业人工翻译。我们对因使用此翻译而导致的任何误解或误读不承担责任。