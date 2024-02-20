# 神经网络简介

![Intro神经网络内容总结的素描图](../../sketchnotes/ai-neuralnetworks.png)

正如我们在介绍中讨论的那样，实现智能的方法之一是训练一个计算机模型或人工智能大脑。从20世纪中期开始，研究人员尝试了不同的数学模型，直到近年来这个方向被证明非常成功。这样的数学模型称为神经网络。

> 有时神经网络被称为"人工神经网络"（Artificial Neural Networks，ANNs），以此表示我们讨论的是模型，而不是真实的神经网络。

## 机器学习

神经网络是 **机器学习** 的一部分，它的目标是使用数据训练计算机模型以解决问题。机器学习构成了人工智能的很大一部分，但是我们在这个课程中不涵盖传统的机器学习。

> 访问我们的独立的 **[机器学习入门](http://github.com/microsoft/ml-for-beginners)** 课程，了解更多关于传统机器学习的知识。

在机器学习中，我们假设我们有一些示例数据集 **X** 和相应的输出值 **Y**。示例通常是由 **特征** 组成的 N 维向量，输出被称为 **标签**。

我们将考虑到最常见的两个机器学习问题：

* **分类**，我们需要将输入对象分类到两个或更多类别中。
* **回归**，我们需要为每个输入样本预测一个数值。> 当把输入和输出表示为张量时，输入数据集是一个大小为M×N的矩阵，其中M是样本数量，N是特征数量。输出标签Y是大小为M的向量。

在本课程中，我们只关注神经网络模型。

## 神经元模型

从生物学角度，我们知道我们的大脑由神经细胞组成，每个神经细胞都有多个输入（轴突）和一个输出（树突）。轴突和树突能够传导电信号，而轴突和树突之间的连接可以表现出不同程度的传导性（由神经介质控制）。

![神经元模型](../images/synapse-wikipedia.jpg) | ![神经元模型](../images/artneuron.png)----|----
真实神经元 *([图片](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) 来自维基百科)* | 人工神经元 *(作者提供的图片)*

因此，神经元的最简单的数学模型包含多个输入 X<sub>1</sub>, ..., X<sub>N</sub> 和一个输出 Y，以及一系列权重 W<sub>1</sub>, ..., W<sub>N</sub>。输出被计算为：

<img src="../images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

其中 f 是某种非线性的**激活函数**。

> 神经元的早期模型在1943年由Warren McCullock和Walter Pitts在经典论文中描述[A logical calculus of the ideas immanent in nervous activity](http://www.springerlink.com/content/61446605110620kg/fulltext.pdf)，Donald Hebb在他的书"[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)"中提出了如何训练这些网络的方法。## 在本节中

在本节中，我们将学习以下内容：
* [感知机](../03-Perceptron/translation/README.zh.md)，是用于二分类问题的最早的神经网络模型之一
* [多层网络](../04-OwnFramework/translation/README.zh.md)，还有一个配套的笔记本[如何构建我们自己的框架](../04-OwnFramework/OwnFramework.ipynb)
* [神经网络框架](../05-Frameworks/translations/README.zh.md)，包括这些笔记本：[PyTorch](../05-Frameworks/IntroPyTorch.ipynb)和[Keras/Tensorflow](../05-Frameworks/IntroKerasTF.ipynb)
* [过拟合](../05-Frameworks/Overfitting.md)