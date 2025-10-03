<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-24T20:34:26+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "zh"
}
-->
# 宠物面部分类

来自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的实验任务。

## 任务

想象一下，你需要开发一个宠物托管应用程序，用来记录所有的宠物信息。这个应用程序的一个重要功能是能够通过照片自动识别宠物的品种。这可以通过神经网络成功实现。

你需要训练一个卷积神经网络，使用 **Pet Faces** 数据集对不同品种的猫和狗进行分类。

## 数据集

我们将使用 **Pet Faces** 数据集，该数据集来源于 [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) 宠物数据集。它包含35种不同品种的猫和狗。

![我们将处理的数据集](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.zh.png)

要下载数据集，请使用以下代码片段：

```python
!wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## 启动笔记本

通过打开 [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb) 开始实验。

## 收获

你已经从零开始解决了一个相对复杂的图像分类问题！尽管有很多类别，你仍然能够获得不错的准确率！同时，测量 top-k 准确率也是有意义的，因为有些类别即使是人类也很难区分清楚，容易混淆。

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。我们对于因使用本翻译而引起的任何误解或误读不承担责任。