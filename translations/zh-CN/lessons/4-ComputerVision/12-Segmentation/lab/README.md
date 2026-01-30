# 人体分割

来自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的实验任务。

## 任务

在视频制作中，例如天气预报，我们经常需要从摄像机中剪切出人像，并将其叠加到其他画面上。这通常通过 **抠像技术（chroma key）** 实现，即人在一个统一颜色的背景前拍摄，然后将背景移除。在本实验中，我们将训练一个神经网络模型来剪切出人像轮廓。

## 数据集

我们将使用来自 Kaggle 的 [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset)。请从 Kaggle 手动下载该数据集。

## 起始笔记本

通过打开 [BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb) 开始实验。

## 收获

人体分割只是我们可以对人物图像进行的常见任务之一。其他重要任务包括 **骨架检测** 和 **姿态检测**。可以查看 [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) 库，了解如何实现这些任务。

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文档的原始语言版本为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用本翻译而引起的任何误解或误读不承担责任。