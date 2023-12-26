# 常见的CNN结构

### VGG-16

VGG-16是一个在2014年ImageNet top-5分类中达到92.7%准确率的网络。它具有以下层结构:

![ImageNet 图层](../images/vgg-16-arch1.jpg)

从图片中可以看到，VGG遵循传统的金字塔架构，即一系列的卷积-池化层。![ImageNet金字塔](../images/vgg-16-arch.jpg)

>图片来源：[Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet是由微软研究院在2015年提出的一系列模型。ResNet的主要思想是使用**残差块**：

<img src="../images/resnet-block.png" width="300"/>

> 来自[这篇论文](https://arxiv.org/pdf/1512.03385.pdf)的图片

使用恒等传递的原因是让我们的层预测前一层的输出与残差块的输出之间的差异 - 因此得名*残差*。这些块更容易训练，可以构建包含数百个这些块的网络（最常见的变体是ResNet-52、ResNet-101和ResNet-152）。

您还可以将这个网络看作是能够根据数据集调整自己的复杂性。最初，在开始训练网络时，权重值较小，大部分信号通过传递恒等层。随着训练的进行，权重变大，网络参数的重要性增加，网络会调整自己以适应正确分类训练图像所需的表达能力。

### Google Inception

谷歌的Inception架构将这个想法推向了更深的一步，并将每个网络层构建为几个不同路径的组合：
<img src="../images/inception.png" width="400"/>

> 图片来源：[Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

在这里，我们需要强调1x1卷积的作用，因为一开始它们毫无意义。为什么我们需要用1x1的滤波器来扫描图片呢？然而，你需要记住卷积滤波器也能适用于多个深度通道（最初是RGB颜色，在后续的层中是用于不同滤波器的通道），1x1卷积用于使用不同的可训练权重将这些输入通道混合在一起。它也可以被视为在通道维度上的降采样（池化）。

这里有一篇关于这个主题的[好的博客文章](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578)，以及[原始论文](https://arxiv.org/pdf/1312.4400.pdf)。

### MobileNetMobileNet是一系列适用于移动设备的模型，其尺寸较小。如果资源有限且可以牺牲一点精度，可以使用这些模型。它们的主要思想是所谓的**深度可分离卷积**，它允许通过一组空间卷积和深度通道上的1x1卷积的组合来表示卷积滤波器。这显著减少了参数的数量，使网络的尺寸更小，并且更容易用更少的数据进行训练。

这是一个关于MobileNet的很好的博客文章[链接](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470)。

## 结论

在本单元，你学习了计算机视觉神经网络的主要概念 - 卷积网络。实际生活中用于图像分类、目标检测甚至图像生成网络的架构都基于CNN，只是更多层和一些额外的训练技巧。

## 🚀 挑战在附带的笔记本中，底部有关如何获得更高准确性的注释。进行一些实验，看看是否可以实现更高的准确性。

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/207)

## 复习和自学

虽然CNN通常用于计算机视觉任务，但它们通常用于提取固定大小的模式。例如，如果我们处理声音，我们也可以使用CNN来查找音频信号中的一些特定模式 - 在这种情况下，滤波器将是1维的（这个CNN将被称为1D-CNN）。此外，有时还会使用3D-CNN在多维空间中提取特征，例如在视频上发生的某些事件 - CNN可以捕捉随时间变化的某些特征模式。请阅读关于可以使用CNN完成的其他任务的复习和自学材料。

## [作业](../lab/README.zh.md)在这个实验中，你的任务是对不同的猫和狗品种进行分类。这些图像比MNIST数据集更复杂，维度更高，并且有超过10个类别。