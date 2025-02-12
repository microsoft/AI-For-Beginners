# 宠物面孔分类

来自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的实验作业。

## 任务

想象一下，您需要开发一个宠物托儿所的应用程序来 catalog 所有宠物。这样一个应用程序的一个重要功能是能够从照片中自动识别品种。这可以通过神经网络成功实现。

您需要训练一个卷积神经网络来使用 **Pet Faces** 数据集对不同品种的猫和狗进行分类。

## 数据集

我们将使用 **Pet Faces** 数据集，该数据集源自 [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) 的宠物数据集。它包含 35 种不同品种的狗和猫。

![我们将处理的数据集](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.zh.png)

要下载数据集，请使用以下代码片段：

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## 启动笔记本

通过打开 [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb) 开始实验。

## 收获

您已经从零开始解决了一个相对复杂的图像分类问题！类的数量相当多，但您仍然能够获得合理的准确性！测量 top-k 准确性也是有意义的，因为一些类即使对人类来说也不容易区分。

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。尽管我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应视为权威来源。对于关键信息，建议进行专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。