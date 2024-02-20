# 计算机视觉简介

[计算机视觉](https://zh.wikipedia.org/wiki/Computer_vision) 是一门学科，旨在使计算机能够对数字图像进行高级理解。这是一个相当广泛的定义，因为*理解*可以有很多不同的含义，包括在图片中找到一个物体（**物体检测**），理解正在发生的情况（**事件检测**），用文本描述一幅图片，或者重建一个三维场景。还有一些与人类图像相关的特殊任务：年龄和情绪估计，人脸检测和识别，以及3D姿势估计，仅举几例。

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/106)

计算机视觉中最简单的任务之一是**图像分类**。

计算机视觉通常被认为是人工智能的一个分支。如今，大多数计算机视觉任务都是使用神经网络来解决的。在本节中，我们将更深入地学习用于计算机视觉的特殊类型神经网络，即[卷积神经网络](../../07-ConvNets/README.md)。然而，在将图像传递给神经网络之前，在许多情况下，使用一些算法技术来增强图像是有意义的。

有几个可用于图像处理的Python库：

* **[imageio](https://imageio.readthedocs.io/en/stable/)** 可用于读写不同的图像格式。它也支持ffmpeg，这是一个将视频帧转换为图像的有用工具。
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)**（也称为PIL）更强大一些，并且还支持一些图像操作，如变形，调色板调整等。
* **[OpenCV](https://opencv.org/)** 是一个强大的用C++编写的图像处理库，已成为图像处理的事实标准。它有一个方便的Python接口。
* **[dlib](http://dlib.net/)** 是一个实现许多机器学习算法的C++库，包括一些计算机视觉算法。它也有一个Python接口，可以用于挑战性的任务，如人脸和面部标志检测。

## OpenCV[OpenCV](https://opencv.org/) 被认为是图像处理的**事实**标准。它包含了很多有用的算法，使用C++实现。你也可以从Python中调用OpenCV。

一个很好的学习OpenCV的地方是[这个学习OpenCV的课程](https://learnopencv.com/getting-started-with-opencv/)。在我们的课程中，我们的目标不是学习OpenCV，而是向你展示一些可以使用OpenCV的例子以及如何使用。

### 加载图片

在Python中，图像可以方便地用NumPy数组表示。例如，大小为320x200像素的灰度图像将存储在一个200x320的数组中，相同尺寸的彩色图像将具有200x320x3的形状（3个颜色通道）。要加载图像，可以使用以下代码：

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

传统上，OpenCV对于彩色图像使用BGR（蓝绿红）编码，而其他Python工具使用传统的RGB（红绿蓝）编码。为了使图像显示正确，需要将其转换为RGB颜色空间，可以通过交换NumPy数组的维度或调用OpenCV函数来实现：
```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

相同的`cvtColor`函数可以用来进行其他颜色空间的转换，比如将图像转换为灰度图或者HSV（色调-饱和度-亮度）颜色空间。

你也可以使用OpenCV逐帧加载视频 - 在练习[OpenCV Notebook](../OpenCV.ipynb)中有一个示例。

### 图像处理

在将图像输入神经网络之前，你可能想要进行一些预处理步骤。OpenCV可以做很多事情，包括：

* 使用`im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)`来改变图像的大小。
* 使用`im = cv2.medianBlur(im,3)`或者`im = cv2.GaussianBlur(im, (3,3), 0)`来对图像进行模糊处理。
* 可以通过NumPy数组操作来改变图像的亮度和对比度，参考[这个Stackoverflow的帖子](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv)。
* 使用阈值化方法，可以通过调用`cv2.threshold`/`cv2.adaptiveThreshold`函数，这通常比调整亮度或对比度更可取。
* 对图像应用不同的变换，参考[这个OpenCV文档](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html)：
    - 如果您需要将旋转、调整大小和倾斜组合到图像中，并且知道图像中三个点的源位置和目标位置，则**仿射变换**很有用。仿射变换保持平行线平行。
    - 如果您知道图像中四个点的源位置和目标位置，则**透视变换**非常有用。例如，如果您从某个角度通过智能手机相机拍摄一个矩形文件的图片，并且想要制作一个表示文档本身的矩形图像。
* 通过使用**光流算法**来了解图像内部的运动。参考[这个OpenCV文档](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)。

## 使用计算机视觉的示例

在我们的 [OpenCV Notebook](../OpenCV.ipynb) 中，我们提供了一些使用计算机视觉进行特定任务的示例：

* **预处理一张盲文书的照片**。我们关注如何使用阈值处理、特征检测、透视变换和 NumPy 操作，将单个盲文符号分离出来，以便神经网络进一步分类。

![盲文图像](../data/braille.jpeg) | ![预处理的盲文图像](../images/braille-result.png) | ![盲文符号](../images/braille-symbols.png)
----|-----|-----

> 图像来自 [OpenCV.ipynb](../OpenCV.ipynb)* **使用帧差法检测视频中的运动**。如果相机固定不动，那么相机捕捉到的帧应该是非常相似的。由于帧被表示为数组，通过对连续两个帧的数组进行相减操作，我们将得到像素差异，对于静止帧来说这个差异应该很低，而一旦图像中有实质性的运动，差异将会增大。

![视频帧和帧差异的图像](../images/frame-difference.png)

> 图片来源：[OpenCV.ipynb](../OpenCV.ipynb)

* **使用光流法检测运动**。[光流法](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html)允许我们理解视频帧上个体像素是如何移动的。光流法有两种类型：

   - **稠密光流**计算每个像素的移动向量场，用于显示它的移动方向。
   - **稀疏光流**基于提取图像中的一些有特色的特征(例如边缘)，并根据这些特征在帧之间建立它们的轨迹。

![光流图像](../images/optical.png)

> 图片来源：[OpenCV.ipynb](../OpenCV.ipynb)

## ✍️ 示例笔记本：OpenCV [尝试OpenCV的实例操作](../OpenCV.ipynb)

使用OpenCV进行一些实验，可以探索[OpenCV笔记本](../OpenCV.ipynb)。

## 结论

有时候，相对复杂的任务，如运动检测或指尖检测，可以纯粹通过计算机视觉来解决。因此，了解计算机视觉的基本技术以及像OpenCV这样的库能做什么非常有帮助。

## 🚀 挑战

观看[该视频](https://docs.microsoft.com/shows/ai-show/ai-show--2021-opencv-ai-competition--grand-prize-winners--cortic-tigers--episode-32?WT.mc_id=academic-77998-cacaste)，了解Cortic Tigers项目以及他们是如何通过一个基于块的解决方案来普及计算机视觉任务的。还要研究其他类似的项目，帮助新学习者进入这个领域。

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/206)

## 复习与自学

在这个很棒的教程中[阅读更多关于光流](https://learnopencv.com/optical-flow-in-opencv/)。

## [任务](lab/README.md)

在这个实验中，你将使用简单的手势录制一个视频，并使用光流提取上下左右的运动。


<img src="../images/palm-movement.png" width="30%" alt="掌部运动帧"/>