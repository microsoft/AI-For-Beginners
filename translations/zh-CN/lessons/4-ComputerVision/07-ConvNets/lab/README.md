# 宠物面部分类

来自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的实验任务。

## 任务

假设你需要开发一个宠物托管应用程序，用于记录所有宠物信息。该应用程序的一个重要功能是通过照片自动识别宠物的品种。这可以通过神经网络成功实现。

你需要训练一个卷积神经网络，使用 **Pet Faces** 数据集对不同品种的猫和狗进行分类。

## 数据集

我们将使用 [Oxford-IIIT Pet Dataset](https://www.robots.ox.ac.uk/~vgg/data/pets/)，该数据集包含37种不同品种的猫和狗的图像。

![我们将处理的数据集](../../../../../../translated_images/zh-CN/data.50b2a9d5484bdbf0.webp)

要下载数据集，请使用以下代码片段：

```python
!wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

**注意：** Oxford-IIIT Pet Dataset 的图像是按文件名组织的（例如，`Abyssinian_1.jpg`，`Bengal_2.jpg`）。笔记本中包含代码，将这些图像组织到按品种分类的子目录中，以便于分类。

## 启动笔记本

通过打开 [PetFaces.ipynb](PetFaces.ipynb) 开始实验。

## 收获

你已经从零开始解决了一个相对复杂的图像分类问题！尽管类别很多，你仍然能够获得合理的准确率！同时，测量 top-k 准确率也是有意义的，因为有些类别即使对人类来说也不容易区分。

---

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于关键信息，建议使用专业人工翻译。我们不对因使用此翻译而产生的任何误解或误读承担责任。