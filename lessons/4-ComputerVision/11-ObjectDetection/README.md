# 目标检测

到目前为止，我们处理的图像分类模型接收一张图像并生成一个分类结果，比如 MNIST 问题中的类别“数字”。然而，在许多情况下，我们不仅想知道一张图片中是否存在对象，还想能够确定它们的精确位置。这正是**目标检测**的关键所在。

## [预先讲义问答](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/111)

![Object Detection](images/Screen_Shot_2016-11-17_at_11.14.54_AM.png)

> 图片来自[YOLO v2 网站](https://pjreddie.com/darknet/yolov2/)

## 一种简单的物体检测方法

假设我们想要在一张图片上找到一只猫，一种非常简单的物体检测方法如下：

1. 将图片分割成多个小块瓦片。
2. 对每个瓦片运行图像分类算法。
3. 那些结果激活度足够高的瓦片可以被认为包含了我们要找的物体。

![Naive Object Detection](images/naive-detection.png)
> *图片来自[Exercise Notebook](ObjectDetection-TF.ipynb)*

然而，这种方法远非理想，因为它只能让算法粗略地定位到对象的边界框。为了更精确地定位，我们需要运行一些回归算法来预测边界框的坐标 - 而为此，我们需要特定的数据集。

## 目标检测的回归算法

[这篇博文](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491)以平缓的方式介绍了检测形状。

## 目标检测的数据集

您可能在此任务中遇到以下数据集：

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 包含20个类别
* [COCO](http://cocodataset.org/#home) - 上下文中的常见物体。包含80个类别、边界框和分割掩码

![COCO](images/coco-examples.jpg)

## 目标检测指标

### 交并比（Intersection over Union）

对于图像分类，衡量算法性能很容易，但对于对象检测，我们需要同时衡量类别的正确性和推断的边界框位置的精确性。对于后者，我们使用所谓的**交并比**(Intersection over Union, IoU)来衡量两个框（或两个任意区域）的重叠程度。

![IoU](images/iou_equation.png)

> *从[这篇关于IoU的博客文章](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)中的第2张图片*

这个想法很简单 - 我们将两个图形之间的交集面积除以它们的并集面积。对于两个完全相同的区域，IoU为1，而对于完全不重叠的区域，IoU为0。否则，它将在0到1之间变化。我们通常只考虑IoU大于某个特定值的边界框。

### 平均精度(Average Precision)

假设我们想要度量一个给定对象类别 C 的识别程度。为了衡量这个指标，我们使用 Average Precision（平均精度）指标，计算方法如下：

1. 考虑准确率-召回率曲线，显示了在不同的检测阈值（从 0 到 1）下的准确度。
2. 根据阈值，我们在图像中可以得到更多或更少的对象检测结果，并得到不同的准确率和召回率。
3. 曲线形状如下图所示：

![ObjDetectionPrecisionRecall](https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png)

> *图片来源于 [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

给定类别$C$的平均精确度是该曲线下的面积。更准确地说，召回轴通常被分为10个部分，并且精确度在所有这些点上求平均：

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP和IoU

我们只考虑IoU高于某个特定值的检测结果。例如，在PASCAL VOC数据集中通常假定$\mbox{IoU阈值}=0.5$，而在COCO中，将使用不同的$\mbox{IoU阈值}$来计算AP。<p align="center">
  <img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>
</p>

> *图片来源：[NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### 平均精度均值 - mAP

目标检测的主要指标被称为**平均精度均值**，或者**mAP**。它是对所有目标类别的平均精度的值，同时有时也会采用$\mbox{IoU Threshold}$。更详细的计算**mAP**的过程在[这篇博文](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)中有描述，也可以在[这里使用代码示例进行查看](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734)。

## 不同的物体检测方法

物体检测算法可以分为两类：

* **区域建议网络** (R-CNN, Fast R-CNN, Faster R-CNN)。其主要思想是生成**感兴趣区域**（ROI），并在其上运行卷积神经网络，寻找最大的激活。这与朴素方法有些相似，唯一的区别是ROI的生成方式更加巧妙。这类方法的一个主要缺点是速度较慢，因为需要将卷积神经网络分类器多次运行在图像上。
* **单次遍历**（YOLO, SSD, RetinaNet）方法。在这些架构中，我们设计网络一次性预测出类别和ROI。

### R-CNN: 基于区域的卷积神经网络

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf)使用[选择性搜索](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf)来生成ROI区域的层次结构，然后将其通过卷积神经网络特征提取器和SVM分类器传递，以确定物体类别，并使用线性回归确定**边界框**坐标。
[官方论文](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](images/rcnn1.png)

> *Image from van de Sande et al. ICCV’11*

![RCNN-1](images/rcnn2.png)

> *图像来源: [这篇博文](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)

### F-RCNN - Fast R-CNN

F-RCNN（Fast R-CNN）是一种基于R-CNN（Region-based Convolutional Neural Networks）的目标检测算法。


![FRCNN](images/f-rcnn.png)

> 图片来源：[论文](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf)，[arXiv](https://arxiv.org/pdf/1504.08083.pdf)，2015

### Faster R-CNN

这种方法的主要思想是使用神经网络来预测ROI（感兴趣区域）-称为*区域建议网络*。[论文](https://arxiv.org/pdf/1506.01497.pdf)，2016![FasterRCNN](images/faster-rcnn.png)

> 图片来源：[官方论文](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: 基于区域的全卷积网络

这个算法比Faster R-CNN还要快。主要思想如下：

1. 我们使用ResNet-101提取特征
1. 特征由**位置敏感的得分图**处理。每个类别的对象被分成$k\times k$个区域，我们的训练目标是预测对象的各个部分。
1. 对于$k\times k$个区域的每个部分，所有网络都对对象类别进行投票，并选择投票最多的对象类别。

![r-fcn image](images/r-fcn.png)

> 图片来自[官方论文](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO是一种实时的一次过程算法。其主要思想如下：* 图像被分成 $S\times S$ 的区域
* 对于每个区域，**卷积神经网络** 预测出 $n$ 个可能的对象，*边界框* 坐标和 *置信度*=*概率* * IoU。

 ![YOLO](images/yolo.png)

> 图片来源：[官方论文](https://arxiv.org/abs/1506.02640)

### 其它算法

* RetinaNet: [官方论文](https://arxiv.org/abs/1708.02002)
   - [Torchvision中的PyTorch实现](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Keras实现](https://github.com/fizyr/keras-retinanet)
   - [Keras示例中的RetinaNet目标检测](https://keras.io/examples/vision/retinanet/)
* SSD (Single Shot Detector): [官方论文](https://arxiv.org/abs/1512.02325)

## ✍️ 练习：目标检测

在以下笔记本中继续学习：[ObjectDetection.ipynb](ObjectDetection.ipynb)

## 结论

在本课程中，您进行了一个快速浏览，了解了目标检测可以实现的各种方式！

## 🚀 挑战

阅读这些关于YOLO的文章和笔记本，并尝试自己动手实践。
 * [推荐优秀博客](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/)，描述了YOLO
 * [官方网站](https://pjreddie.com/darknet/yolo/)
 * Yolo: [Keras 实现](https://github.com/experiencor/keras-yolo2)，[手把手笔记](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [Keras 实现](https://github.com/experiencor/keras-yolo2)，[手把手笔记](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## 复习和自学

* [目标检测](https://tjmachinelearning.com/lectures/1718/obj/) by Nikhil Sardana* [目标检测算法的良好比较](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [深度学习目标检测算法评述](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [基本目标检测算法的逐步介绍](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [以Python实现快速R-CNN的目标检测](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [作业：目标检测](lab/README.md)