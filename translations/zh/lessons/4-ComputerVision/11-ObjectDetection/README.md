<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d85c8b08f6d1b48fd7f35b99f93c1138",
  "translation_date": "2025-08-24T20:33:19+00:00",
  "source_file": "lessons/4-ComputerVision/11-ObjectDetection/README.md",
  "language_code": "zh"
}
-->
# 目标检测

我们之前讨论的图像分类模型通常会接收一张图片并输出一个类别结果，例如在 MNIST 问题中输出类别“数字”。然而，在许多情况下，我们不仅仅想知道图片中是否有物体——我们还希望能够确定它们的具体位置。这正是**目标检测**的核心所在。

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/111)

![目标检测](../../../../../translated_images/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be1b905373ed9c858102c054b16e4595c76ec3f7bba0feb549.zh.png)

> 图片来源：[YOLO v2 网站](https://pjreddie.com/darknet/yolov2/)

## 一种简单的目标检测方法

假设我们想在一张图片中找到一只猫，一种非常简单的目标检测方法可能是：

1. 将图片分割成多个小块。
2. 对每个小块进行图像分类。
3. 对于分类结果激活值足够高的小块，可以认为其中包含目标物体。

![简单目标检测](../../../../../translated_images/naive-detection.e7f1ba220ccd08c68a2ea8e06a7ed75c3fcc738c2372f9e00b7f4299a8659c01.zh.png)

> *图片来源：[练习笔记本](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection-TF.ipynb)*

然而，这种方法远非理想，因为它只能非常粗略地定位物体的边界框。为了更精确地定位，我们需要进行某种**回归**来预测边界框的坐标——这需要特定的数据集。

## 用回归进行目标检测

[这篇博客文章](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491)对目标检测中的形状识别进行了很好的入门介绍。

## 目标检测数据集

在进行目标检测任务时，你可能会遇到以下数据集：

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 包含 20 个类别
* [COCO](http://cocodataset.org/#home) - 常见物体上下文数据集。包含 80 个类别，边界框和分割掩码

![COCO](../../../../../translated_images/coco-examples.71bc60380fa6cceb7caad48bd09e35b6028caabd363aa04fee89c414e0870e86.zh.jpg)

## 目标检测评估指标

### 交并比（IoU）

对于图像分类来说，评估算法性能相对简单；但对于目标检测，我们需要同时评估类别的正确性以及预测边界框位置的精确性。后者通常使用**交并比**（IoU）来衡量，即评估两个框（或任意两个区域）的重叠程度。

![IoU](../../../../../translated_images/iou_equation.9a4751d40fff4e119ecd0a7bcca4e71ab1dc83e0d4f2a0d66ff0859736f593cf.zh.png)

> *图片来源：[这篇关于 IoU 的优秀博客文章](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

其思想很简单——将两个图形的交集面积除以它们的并集面积。对于两个完全相同的区域，IoU 值为 1；对于完全不相交的区域，IoU 值为 0。其他情况下，IoU 值介于 0 到 1 之间。通常我们只考虑 IoU 超过某个阈值的边界框。

### 平均精度（AP）

假设我们想评估某个类别 $C$ 的识别效果。为此，我们使用**平均精度**（AP）指标，其计算方法如下：

1. 考虑精度-召回曲线，该曲线显示检测阈值（从 0 到 1）变化时的准确性。
2. 根据阈值，我们会检测到图片中的更多或更少的物体，并得到不同的精度和召回值。
3. 曲线如下所示：

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *图片来源：[NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

某类别 $C$ 的平均精度是该曲线下的面积。更具体地说，召回轴通常分为 10 个部分，精度在这些点上取平均值：

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP 和 IoU

我们只考虑 IoU 超过某个阈值的检测。例如，在 PASCAL VOC 数据集中通常假设 $\mbox{IoU Threshold} = 0.5$，而在 COCO 数据集中，AP 是针对不同的 $\mbox{IoU Threshold}$ 值计算的。

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *图片来源：[NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### 平均平均精度（mAP）

目标检测的主要评估指标是**平均平均精度**（mAP）。它是所有类别的平均精度值，有时也包括不同的 $\mbox{IoU Threshold}$。关于**mAP**的详细计算过程可以参考
[这篇博客文章](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)，以及[这里的代码示例](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734)。

## 不同的目标检测方法

目标检测算法主要分为两大类：

* **区域提议网络**（R-CNN、Fast R-CNN、Faster R-CNN）。其核心思想是生成**兴趣区域**（ROI），并对其运行 CNN，寻找最大激活值。这种方法与简单方法类似，但 ROI 的生成方式更为智能。此类方法的主要缺点是速度较慢，因为需要对图像进行多次 CNN 分类。
* **单次检测**（YOLO、SSD、RetinaNet）方法。这些架构设计为在一次网络运行中同时预测类别和 ROI。

### R-CNN：基于区域的 CNN

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) 使用[选择性搜索](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf)生成 ROI 区域的层次结构，然后通过 CNN 特征提取器和 SVM 分类器确定物体类别，并通过线性回归确定*边界框*坐标。[官方论文](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/rcnn1.cae407020dfb1d1fb572656e44f75cd6c512cc220591c116c506652c10e47f26.zh.png)

> *图片来源：van de Sande 等人 ICCV’11*

![RCNN-1](../../../../../translated_images/rcnn2.2d9530bb83516484ec65b250c22dbf37d3d23244f32864ebcb91d98fe7c3112c.zh.png)

> *图片来源：[这篇博客](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - 快速 R-CNN

这种方法与 R-CNN 类似，但区域是在应用卷积层之后定义的。

![FRCNN](../../../../../translated_images/f-rcnn.3cda6d9bb41888754037d2d9763e2298a96de5d9bc2a21db3147357aa5da9b1a.zh.png)

> 图片来源：[官方论文](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf)，[arXiv](https://arxiv.org/pdf/1504.08083.pdf)，2015

### Faster R-CNN

这种方法的核心思想是使用神经网络预测 ROI，即所谓的*区域提议网络*。[论文](https://arxiv.org/pdf/1506.01497.pdf)，2016

![FasterRCNN](../../../../../translated_images/faster-rcnn.8d46c099b87ef30ab2ea26dbc4bdd85b974a57ba8eb526f65dc4cd0a4711de30.zh.png)

> 图片来源：[官方论文](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN：基于区域的全卷积网络

这种算法比 Faster R-CNN 更快。其核心思想如下：

1. 使用 ResNet-101 提取特征。
2. 特征通过**位置敏感得分图**处理。每个类别 $C$ 的物体被划分为 $k\times k$ 区域，并训练预测物体的各部分。
3. 对于 $k\times k$ 区域的每个部分，所有网络对物体类别进行投票，选择得票最多的类别。

![r-fcn image](../../../../../translated_images/r-fcn.13eb88158b99a3da50fa2787a6be5cb310d47f0e9655cc93a1090dc7aab338d1.zh.png)

> 图片来源：[官方论文](https://arxiv.org/abs/1605.06409)

### YOLO - 你只需看一次

YOLO 是一种实时单次检测算法。其核心思想如下：

 * 将图像划分为 $S\times S$ 区域。
 * 对每个区域，**CNN** 预测 $n$ 个可能的物体、*边界框*坐标和*置信度*=*概率* * IoU。

 ![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.zh.png)

> 图片来源：[官方论文](https://arxiv.org/abs/1506.02640)

### 其他算法

* RetinaNet: [官方论文](https://arxiv.org/abs/1708.02002)
   - [PyTorch 实现（Torchvision）](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Keras 实现](https://github.com/fizyr/keras-retinanet)
   - [Keras 示例中的 RetinaNet 目标检测](https://keras.io/examples/vision/retinanet/)
* SSD（单次检测器）：[官方论文](https://arxiv.org/abs/1512.02325)

## ✍️ 练习：目标检测

通过以下笔记本继续学习：

[ObjectDetection.ipynb](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)

## 总结

在本课中，你快速了解了实现目标检测的各种方法！

## 🚀 挑战

阅读以下关于 YOLO 的文章和笔记本，并尝试自己动手实践：

* [优秀博客文章](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/)介绍 YOLO
 * [官方网站](https://pjreddie.com/darknet/yolo/)
 * YOLO：[Keras 实现](https://github.com/experiencor/keras-yolo2)，[逐步笔记本](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * YOLO v2：[Keras 实现](https://github.com/experiencor/keras-yolo2)，[逐步笔记本](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## 复习与自学

* [目标检测](https://tjmachinelearning.com/lectures/1718/obj/) 作者：Nikhil Sardana
* [目标检测算法的优秀比较](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [深度学习目标检测算法综述](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [目标检测算法基础入门](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Python 实现 Faster R-CNN 进行目标检测](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [作业：目标检测](lab/README.md)

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文档的原始语言版本为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而引起的任何误解或误读不承担责任。