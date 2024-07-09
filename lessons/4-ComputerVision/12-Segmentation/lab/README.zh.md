# 人体分割

来自[AI初学者课程](https://github.com/microsoft/ai-for-beginners)的实验分配。

## 任务

在视频制作中，例如天气预报中，我们经常需要从相机中剪出一个人的图像并将其放在其他片段的顶部。这通常是使用**色度键**技术完成的，当人物站在统一颜色的背景前面进行拍摄时，这个背景会被移除。在这个实验中，我们将训练一个神经网络模型来剪出人的轮廓。

## 数据集我们将使用来自Kaggle的[分割全身MADS数据集](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset)。从Kaggle手动下载数据集。

## 开始笔记本

通过打开[BodySegmentation.ipynb](BodySegmentation.ipynb)来开始实验室。

## 结论

身体分割只是我们可以用人的图像进行的常见任务之一。另一个重要任务包括**骨骼检测**和**姿势检测**。可以查看[OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)库，了解如何实现这些任务。