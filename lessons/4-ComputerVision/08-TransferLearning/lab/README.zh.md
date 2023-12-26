# 使用迁移学习对牛津宠物进行分类

来自[AI入门课程](https://github.com/microsoft/ai-for-beginners)的实验作业。

## 任务

假设您需要为宠物托儿所开发一个应用程序，用于记录所有宠物。这种应用程序的一个重要功能是能够根据照片自动识别品种。在这个任务中，我们将使用迁移学习来对[Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/)宠物数据集中的真实生活宠物图像进行分类。

## 数据集我们将使用原始的[Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/)宠物数据集，其中包含35种不同的狗和猫品种。

要下载数据集，请使用以下代码段：

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```
## 实验笔记

通过打开 [OxfordPets.ipynb](OxfordPets.ipynb) 来开始实验。

## 要点

迁移学习和预训练网络使得我们能够相对容易地解决现实世界的图像分类问题。然而，预训练网络在相似类型的图像上的表现良好，如果我们开始对非常不同的图像（例如医学图像）进行分类，很可能会获得更差的结果。