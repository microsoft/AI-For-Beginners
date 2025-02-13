# 使用迁移学习对牛津宠物进行分类

来自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的实验作业。

## 任务

想象一下，您需要开发一个宠物托儿所的应用程序来 catalog 所有宠物。这样一个应用程序的一个重要功能将是自动从照片中识别宠物的品种。在这个作业中，我们将使用迁移学习来对来自 [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) 宠物数据集的真实宠物图像进行分类。

## 数据集

我们将使用原始的 [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) 宠物数据集，该数据集包含 35 种不同品种的狗和猫。

要下载数据集，请使用以下代码片段：

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## 启动笔记本

通过打开 [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb) 开始实验。

## 收获

迁移学习和预训练网络使我们能够相对轻松地解决现实世界的图像分类问题。然而，预训练网络在相似类型的图像上效果良好，如果我们开始对非常不同的图像（例如医学图像）进行分类，结果可能会大大降低。

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应视为权威来源。对于关键信息，建议进行专业人工翻译。我们对因使用此翻译而产生的任何误解或误读不承担责任。