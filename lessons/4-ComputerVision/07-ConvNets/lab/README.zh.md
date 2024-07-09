# 宠物脸部分类

来自[初学者人工智能课程](https://github.com/microsoft/ai-for-beginners)的实验任务。

## 任务

想象你需要开发一个宠物托管应用程序来对所有宠物进行分类。这样一个应用程序的一个伟大的功能是能够通过照片自动识别品种。可以使用神经网络来成功完成这个任务。

你需要训练一个卷积神经网络，使用**宠物脸部**数据集对不同品种的猫和狗进行分类。## 数据集

我们将使用从[Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/)宠物数据集中整理出的**宠物脸部**数据集。它包含35种不同的狗和猫品种。

![我们将处理的数据集](images/data.png)

要下载数据集，请使用以下代码片段：

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
``````python
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## 打开Notebook

通过打开[PetFaces.ipynb](PetFaces.ipynb)来开始实验

## 收获你已经从零开始解决了一个相对复杂的图像分类问题！有很多类别，但你仍然能够获得合理的准确率！对于测量前k个准确率也是有意义的，因为有些类别即使对人类来说也不容易区分清楚。