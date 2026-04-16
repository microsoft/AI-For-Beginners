# 使用迁移学习对牛津宠物进行分类

来自 [AI 初学者课程](https://github.com/microsoft/ai-for-beginners) 的实验任务。

## 任务

想象一下，你需要为一家宠物托管中心开发一个应用程序，用来记录所有的宠物。这样的应用程序一个很棒的功能就是能够通过照片自动识别宠物的品种。在本次任务中，我们将使用迁移学习对 [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) 宠物数据集中的真实宠物图片进行分类。

## 数据集

我们将使用原始的 [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) 宠物数据集，该数据集包含 35 种不同品种的猫和狗。

要下载数据集，请使用以下代码片段：

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## 启动 Notebook

通过打开 [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb) 开始实验。

## 收获

迁移学习和预训练网络使我们能够相对轻松地解决现实世界中的图像分类问题。然而，预训练网络在处理相似类型的图像时效果较好，如果我们开始分类非常不同的图像（例如医学图像），结果可能会大打折扣。

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而引起的任何误解或误读，我们概不负责。