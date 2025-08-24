<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7336583e4630220c835335da640016db",
  "translation_date": "2025-08-24T20:39:04+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/lab/README.md",
  "language_code": "zh"
}
-->
# 使用感知机进行多类别分类

来自 [AI 初学者课程](https://github.com/microsoft/ai-for-beginners) 的实验任务。

## 任务

使用我们在本课中为 MNIST 手写数字的二分类开发的代码，创建一个多类别分类器，能够识别任意数字。计算训练集和测试集上的分类准确率，并打印出混淆矩阵。

## 提示

1. 对于每个数字，创建一个二分类器的数据集，区分“该数字 vs. 其他所有数字”
2. 为二分类训练 10 个不同的感知机（每个数字一个）
3. 定义一个函数，用于分类输入的数字

> **提示**：如果我们将所有 10 个感知机的权重组合成一个矩阵，我们可以通过一次矩阵乘法将所有 10 个感知机应用于输入数字。然后，只需对输出应用 `argmax` 操作即可找到最可能的数字。

## 起始笔记本

通过打开 [PerceptronMultiClass.ipynb](../../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb) 开始实验。

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文档的原始语言版本为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而引起的任何误解或误读不承担责任。