# 神经网络简介

![Summary of Intro Neural Networks content in a doodle](../sketchnotes/ai-neuralnetworks.png)

正如我们在导言中所讨论的，实现智能的方法之一是训练**计算机模型**或**人工大脑**。自 20 世纪中叶以来，研究人员尝试了不同的数学模型，直到近年来，这一方向被证明是非常成功的。这种大脑数学模型被称为**神经网络。

> 有时，神经网络被称为**人工神经网络*，ANNs，以表明我们谈论的是模型，而不是真正的神经元网络。

## 机器学习

神经网络是机器学习（**Machine Learning）这门更大学科的一部分，其目标是利用数据来训练能够解决问题的计算机模型。机器学习是人工智能的重要组成部分，但本课程并不涉及经典的机器学习。

> 请访问我们单独的 **[机器学习入门](http://github.com/microsoft/ml-for-beginners)** 课程，了解有关经典机器学习的更多信息。

在机器学习中，我们假设有一些示例数据集**X**和相应的输出值**Y**。示例通常是由**特征**组成的 N 维向量，输出称为**标签**。

我们将考虑两个最常见的机器学习问题：

* 分类**，我们需要将输入对象分为两个或多个类别。
**回归**，我们需要对每个输入样本预测一个数字。

> 以张量表示输入和输出时，输入数据集是一个大小为 M&times;N 的矩阵，其中 M 是样本数，N 是特征数。输出标签 Y 是大小为 M 的向量。

在本课程中，我们将只关注神经网络模型。

## 神经元模型

从生物学角度，我们知道大脑由神经细胞组成，每个神经细胞都有多个 "输入"（轴突）和一个输出（树突）。轴突和树突可以传导电信号，轴突和树突之间的连接可以表现出不同程度的传导性（由神经介质控制）。

![Model of a Neuron](images/synapse-wikipedia.jpg) | ![Model of a Neuron](images/artneuron.png)
----|----
Real Neuron *([Image](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) from Wikipedia)* | Artificial Neuron *(Image by Author)*

Thus, the simplest mathematical model of a neuron contains several inputs X<sub>1</sub>, ..., X<sub>N</sub> and an output Y, and a series of weights W<sub>1</sub>, ..., W<sub>N</sub>. An output is calculated as:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

where f is some non-linear **activation function**.

> Early models of neuron were described in the classical paper [A logical calculus of the ideas immanent in nervous activity](http://www.springerlink.com/content/61446605110620kg/fulltext.pdf) by Warren McCullock and Walter Pitts in 1943. Donald Hebb in his book "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)" proposed the way those networks can be trained.

## In this Section

In this section we will learn about:
* [Perceptron](03-Perceptron/README.md), one of the earliest neural network models for two-class classification
* [Multi-layered networks](04-OwnFramework/README.md) with a paired notebook [how to build our own framework](04-OwnFramework/OwnFramework.ipynb)
* [Neural Network Frameworks](05-Frameworks/README.md), with these notebooks: [PyTorch](05-Frameworks/IntroPyTorch.ipynb) and [Keras/Tensorflow](05-Frameworks/IntroKerasTF.ipynb)
* [Overfitting](05-Frameworks/Overfitting.md)
