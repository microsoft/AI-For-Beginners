<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5abc5f7978919be90cd313f0c20e8228",
  "translation_date": "2025-09-07T14:28:35+00:00",
  "source_file": "lessons/3-NeuralNetworks/README.md",
  "language_code": "zh"
}
-->
# 神经网络简介

![神经网络内容总结涂鸦](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.zh.png)

正如我们在介绍中讨论的那样，实现智能的一种方法是训练一个**计算机模型**或一个**人工大脑**。自20世纪中期以来，研究人员尝试了不同的数学模型，直到近年来这一方向取得了巨大成功。这些模拟大脑的数学模型被称为**神经网络**。

> 有时神经网络被称为*人工神经网络*（Artificial Neural Networks，ANNs），以表明我们讨论的是模型，而不是实际的神经网络。

## 机器学习

神经网络属于一个更大的学科——**机器学习**，其目标是利用数据训练能够解决问题的计算机模型。机器学习是人工智能的重要组成部分，但我们在本课程中不涉及传统的机器学习内容。

> 请访问我们单独的**[机器学习入门](http://github.com/microsoft/ml-for-beginners)**课程，了解更多关于传统机器学习的内容。

在机器学习中，我们假设有一些示例数据集**X**，以及对应的输出值**Y**。示例通常是由**特征**组成的N维向量，而输出被称为**标签**。

我们将讨论两种最常见的机器学习问题：

* **分类**，需要将输入对象分类为两个或多个类别。
* **回归**，需要为每个输入样本预测一个数值。

> 当将输入和输出表示为张量时，输入数据集是一个大小为M×N的矩阵，其中M是样本数量，N是特征数量。输出标签**Y**是一个大小为M的向量。

在本课程中，我们将仅关注神经网络模型。

## 神经元模型

从生物学中我们知道，大脑由神经细胞组成，每个神经细胞有多个“输入”（轴突）和一个输出（树突）。轴突和树突可以传导电信号，轴突与树突之间的连接可以表现出不同程度的导电性（由神经递质控制）。

![神经元模型](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.zh.jpg) | ![神经元模型](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.zh.png)
----|----
真实神经元 *（[图片](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg)来自维基百科）* | 人工神经元 *（作者提供图片）*

因此，神经元的最简单数学模型包含几个输入**X<sub>1</sub>, ..., X<sub>N</sub>**和一个输出**Y**，以及一系列权重**W<sub>1</sub>, ..., W<sub>N</sub>**。输出计算公式为：

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

其中**f**是某种非线性**激活函数**。

> 早期的神经元模型在1943年由Warren McCullock和Walter Pitts在经典论文[A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf)中描述。Donald Hebb在他的书《[行为的组织：一种神经心理学理论](https://books.google.com/books?id=VNetYrB8EBoC)》中提出了训练这些网络的方法。

## 本节内容

在本节中，我们将学习以下内容：
* [感知机](03-Perceptron/README.md)，一种用于二分类的最早神经网络模型
* [多层网络](04-OwnFramework/README.md)，以及配套笔记本[如何构建我们自己的框架](04-OwnFramework/OwnFramework.ipynb)
* [神经网络框架](05-Frameworks/README.md)，包括以下笔记本：[PyTorch](05-Frameworks/IntroPyTorch.ipynb)和[Keras/Tensorflow](05-Frameworks/IntroKerasTF.ipynb)
* [过拟合](../../../../lessons/3-NeuralNetworks/05-Frameworks)

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。