# 计算机视觉入门

[计算机视觉](https://wikipedia.org/wiki/Computer_vision) 是一门学科，其目标是让计算机获得对数字图像的高级理解。这是一个相当宽泛的定义，因为 "理解 "可以有许多不同的含义，包括在图片上找到一个对象（**对象检测**）、理解正在发生的事情（**事件检测**）、用文字描述图片或重建三维场景。此外，还有一些与人类图像相关的特殊任务：年龄和情感估计、人脸检测和识别以及三维姿态估计等等。

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/106)

计算机视觉最简单的任务之一就是**图像分类**。

计算机视觉通常被认为是人工智能的一个分支。如今，大多数计算机视觉任务都是通过神经网络来解决的。在本节中，我们将进一步了解用于计算机视觉的特殊神经网络--[卷积神经网络](../../07-ConvNets/README.md)。

不过，在将图像传递给神经网络之前，很多情况下都需要使用一些算法技术来增强图像。

有几个 Python 库可以用于图像处理：

* **[imageio](https://imageio.readthedocs.io/en/stable/)** 可用于读取/写入不同的图像格式。它还支持 ffmpeg，这是一种将视频帧转换为图像的实用工具。
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)** (也称为 PIL）功能更强大一些，还支持一些图像处理功能，如变形、调色板调整等。
* **[OpenCV](https://opencv.org/)** 是一个用 C++ 编写的功能强大的图像处理库，已成为图像处理的*事实*标准。它有一个方便的 Python 接口。
* **[dlib](http://dlib.net/)** 是一个 C++ 库，可以实现许多机器学习算法，包括一些计算机视觉算法。它还有一个 Python 接口，可用于人脸和面部地标检测等具有挑战性的任务。

## 开放式计算机辅助设计（OpenCV)

[OpenCV](https://opencv.org/) 被认为是图像处理的*事实*标准。它包含大量有用的算法，用 C++ 实现。你也可以从 Python 中调用 OpenCV。

学习 OpenCV 的好地方是 [学习 OpenCV 课程](https://learnopencv.com/getting-started-with-opencv/). 在我们的课程中，我们的目标不是学习 OpenCV，而是向你展示一些可以使用 OpenCV 的例子，以及如何使用。

### 加载图片

Python 中的图像可以方便地用 NumPy 数组表示。例如，大小为 320x200 像素的灰度图像将存储在一个 200x320 的数组中，同样大小的彩色图像的形状为 200x320x3（表示 3 个颜色通道）。要加载图像，可以使用以下代码：

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

传统上，OpenCV 对彩色图像使用 BGR（蓝-绿-红）编码，而其他 Python 工具则使用更传统的 RGB（红-绿-蓝）编码。为了使图像看起来正确，您需要通过交换 NumPy 数组中的维数或调用 OpenCV 函数，将图像转换为 RGB 色彩空间：

```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

同样的 `cvtColor` 函数可用于执行其他色彩空间转换，如将图像转换为灰度或 HSV（色相-饱和度-值）色彩空间。

您还可以使用 OpenCV 逐帧加载视频 - [OpenCV Notebook](OpenCV.ipynb) 习题中给出了一个示例。

### 图像处理

在将图像输入神经网络之前，您可能需要应用几个预处理步骤。OpenCV 可以做很多事情，包括

* **调整大小** 使用 `im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)`
* **模糊化** 使用 `im = cv2.medianBlur(im,3)` or `im = cv2.GaussianBlur(im, (3,3), 0)`
* 改变图像的**亮度和对比度**可通过 NumPy 数组操作完成，如以下所述 [在此 Stackoverflow 说明中](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv).
* 使用 [阈值](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html) 调用 `cv2.threshold`/`cv2.adaptiveThreshold`函数，这通常比调整亮度或对比度更好。
* 对这个图片应用不同的 [transformations](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html) :
    - **[Affine transformations](https://docs.opencv.org/4.5.5/d4/d61/tutorial_warp_affine.html)** 如果需要对图像进行旋转、大小调整和倾斜，并且知道图像中三个点的源点和目标点位置，那么 Affine 变换就会非常有用。仿射变换使平行线保持平行。
    - **[Perspective transformations](https://medium.com/analytics-vidhya/opencv-perspective-transformation-9edffefb2143)** 当你知道图像中 4 个点的源位置和目标位置时，该功能就会派上用场。例如，如果您通过智能手机摄像头从某个角度拍摄了一张矩形文件的照片，并希望制作出该文件本身的矩形图像，您可以使用以下方法来制作矩形图像。
* 使用 **[optical flow](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)**.

## 使用计算机视觉的例子

在我们的 [OpenCV Notebook](.../OpenCV.ipynb)中，我们列举了一些计算机视觉可用于执行特定任务的例子：

* 对盲文书籍的照片进行预处理**。我们的重点是如何使用阈值处理、特征检测、透视变换和 NumPy 操作来分离单个盲文符号，以便神经网络进行进一步分类。

![盲文图像](../data/braille.jpeg) | ![盲文图像预处理](../images/braille-result.png) | ![盲文符号](../images/braille-symbols.png)
----|-----|-----

> 图片来自于 [OpenCV.ipynb](../OpenCV.ipynb)

* 利用帧差检测视频中的运动**。如果摄像机是固定的，那么摄像机馈送的帧应该非常相似。由于帧是以数组表示的，因此只需减去随后两个帧的数组，就能得到像素差，静态帧的像素差应该较小，而一旦图像中出现大量运动，像素差就会变大。

![视频帧图像和帧差](../images/frame-difference.png)

> Image from [OpenCV.ipynb](OpenCV.ipynb)

** 利用光学流检测运动**。通过[光学流](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html)，我们可以了解视频帧上的单个像素是如何移动的。光流有两种类型：

   - 密集光流**计算矢量场，显示每个像素的移动位置。
   - 稀疏光学流***基于图像中的一些显著特征（如边缘），并建立其从一帧到另一帧的轨迹。

![光流图像](../images/optical.png)

> 图片来自于 [OpenCV.ipynb](../OpenCV.ipynb)

## ✍️ 笔记本范例： OpenCV [体验 OpenCV 操作](../OpenCV.ipynb)

让我们通过探索 [OpenCV Notebook](../OpenCV.ipynb)用 OpenCV 做一些实验吧

## 结论

有时，一些相对复杂的任务，如运动检测或指尖检测，完全可以通过计算机视觉来解决。因此，了解计算机视觉的基本技术以及 OpenCV 等库的功能非常有帮助。

## 🚀 挑战

观看 [这个视频](https://docs.microsoft.com/shows/ai-show/ai-show--2021-opencv-ai-competition--grand-prize-winners--cortic-tigers--episode-32?WT.mc_id=academic-77998-cacaste) 从人工智能展上了解 Cortic Tigers 项目，以及他们如何通过机器人构建一个基于块的解决方案来实现计算机视觉任务的民主化。对类似的其他项目进行一些研究，以帮助新学员进入这一领域。

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/206)

## 回顾 & 自学

了解有关光流的更多信息 [在这个伟大的教程中](https://learnopencv.com/optical-flow-in-opencv/).

## [任务](../lab/README.md)

在本实验室中，您将拍摄一段带有简单手势的视频，目标是使用光学流提取上/下/左/右的动作。

<img src="../images/palm-movement.png" width="30%" alt="Palm Movement Frame"/>
