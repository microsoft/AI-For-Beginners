# 人体分割

来自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的实验任务。

## 任务

在视频制作中，例如天气预报，我们常常需要从摄像机中剪切出人像，并将其放置在其他画面上。这通常通过 **色度键** 技术完成，当一个人在均匀颜色背景前拍摄时，该背景会被去除。在这个实验中，我们将训练一个神经网络模型来剪切出人类轮廓。

## 数据集

我们将使用来自 Kaggle 的 [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset)。请从 Kaggle 手动下载数据集。

## 启动笔记本

通过打开 [BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb) 来开始实验。

## 收获

人体分割只是我们可以对人像图像执行的常见任务之一。另一个重要的任务包括 **骨架检测** 和 **姿态检测**。查看 [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) 库，了解这些任务如何实现。

**免责声明**：  
本文件是使用机器翻译的人工智能翻译服务进行翻译的。尽管我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原文件的母语版本应被视为权威来源。对于重要信息，建议进行专业人工翻译。我们对因使用此翻译而导致的任何误解或误释不承担责任。