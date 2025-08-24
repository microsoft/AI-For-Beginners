<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bedc8e702db17260cfe824d58b6cfd4",
  "translation_date": "2025-08-24T20:34:33+00:00",
  "source_file": "lessons/4-ComputerVision/06-IntroCV/README.md",
  "language_code": "zh"
}
-->
# 计算机视觉简介

[计算机视觉](https://wikipedia.org/wiki/Computer_vision) 是一个旨在让计算机能够对数字图像进行高层次理解的学科。这是一个非常广泛的定义，因为“理解”可以有很多不同的含义，包括在图片中找到一个物体（**目标检测**）、理解发生了什么（**事件检测**）、用文字描述图片，或者以3D形式重建场景。此外，还有一些与人类图像相关的特殊任务：例如年龄和情绪估计、人脸检测与识别，以及3D姿态估计等。

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/106)

计算机视觉最简单的任务之一是 **图像分类**。

计算机视觉通常被认为是人工智能的一个分支。如今，大多数计算机视觉任务都是通过神经网络解决的。在本节中，我们将深入学习一种专门用于计算机视觉的神经网络——[卷积神经网络](../07-ConvNets/README.md)。

然而，在将图像传递给神经网络之前，许多情况下使用一些算法技术来增强图像是有意义的。

以下是一些可用于图像处理的 Python 库：

* **[imageio](https://imageio.readthedocs.io/en/stable/)** 可用于读取/写入不同的图像格式。它还支持 ffmpeg，一个将视频帧转换为图像的有用工具。
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)**（也称为 PIL）功能更强大，还支持一些图像操作，例如变形、调色板调整等。
* **[OpenCV](https://opencv.org/)** 是一个用 C++ 编写的强大的图像处理库，已成为图像处理的事实标准。它有一个方便的 Python 接口。
* **[dlib](http://dlib.net/)** 是一个 C++ 库，包含许多机器学习算法，包括一些计算机视觉算法。它也有一个 Python 接口，可用于诸如人脸和面部关键点检测等复杂任务。

## OpenCV

[OpenCV](https://opencv.org/) 被认为是图像处理的事实标准。它包含许多有用的算法，使用 C++ 实现。你也可以通过 Python 调用 OpenCV。

学习 OpenCV 的一个好地方是 [这个 Learn OpenCV 课程](https://learnopencv.com/getting-started-with-opencv/)。在我们的课程中，我们的目标不是学习 OpenCV，而是向你展示一些使用它的示例以及如何使用。

### 加载图像

在 Python 中，图像可以方便地表示为 NumPy 数组。例如，大小为 320x200 像素的灰度图像可以存储在一个 200x320 的数组中，而相同尺寸的彩色图像则具有 200x320x3 的形状（对应 3 个颜色通道）。要加载图像，可以使用以下代码：

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

传统上，OpenCV 对彩色图像使用 BGR（蓝-绿-红）编码，而其他 Python 工具则使用更传统的 RGB（红-绿-蓝）。为了使图像显示正确，你需要将其转换为 RGB 颜色空间，可以通过交换 NumPy 数组中的维度或调用 OpenCV 函数来实现：

```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

同样的 `cvtColor` 函数也可以用于执行其他颜色空间转换，例如将图像转换为灰度或 HSV（色调-饱和度-亮度）颜色空间。

你还可以使用 OpenCV 按帧加载视频——在练习 [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb) 中有一个示例。

### 图像处理

在将图像传递给神经网络之前，你可能需要应用几个预处理步骤。OpenCV 可以完成许多任务，包括：

* 使用 `im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)` **调整图像大小**。
* 使用 `im = cv2.medianBlur(im,3)` 或 `im = cv2.GaussianBlur(im, (3,3), 0)` **模糊图像**。
* 通过 NumPy 数组操作改变图像的 **亮度和对比度**，具体方法可参考 [这个 Stackoverflow 说明](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv)。
* 使用 [阈值处理](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html)，通过调用 `cv2.threshold` 或 `cv2.adaptiveThreshold` 函数，这通常比调整亮度或对比度更优。
* 对图像应用不同的 [变换](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html)：
    - **[仿射变换](https://docs.opencv.org/4.5.5/d4/d61/tutorial_warp_affine.html)** 如果你需要对图像进行旋转、调整大小和倾斜，并且知道图像中三个点的源位置和目标位置，仿射变换会保持平行线的平行性。
    - **[透视变换](https://medium.com/analytics-vidhya/opencv-perspective-transformation-9edffefb2143)** 如果你知道图像中四个点的源位置和目标位置，这会很有用。例如，如果你用智能手机从某个角度拍摄了一张矩形文档的照片，并希望将文档本身转换为矩形图像。
* 使用 **[光流](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)** 来理解图像中的运动。

## 使用计算机视觉的示例

在我们的 [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb) 中，我们提供了一些使用计算机视觉完成特定任务的示例：

* **预处理盲文书籍的照片**。我们重点展示如何使用阈值处理、特征检测、透视变换和 NumPy 操作来分离单个盲文符号，以便后续通过神经网络进行分类。

![盲文图像](../../../../../translated_images/braille.341962ff76b1bd7044409371d3de09ced5028132aef97344ea4b7468c1208126.zh.jpeg) | ![预处理后的盲文图像](../../../../../translated_images/braille-result.46530fea020b03c76aac532d7d6eeef7f6fb35b55b1001cd21627907dabef3ed.zh.png) | ![盲文符号](../../../../../translated_images/braille-symbols.0159185ab69d533909dc4d7d26a1971b51401c6a80eb3a5584f250ea880af88b.zh.png)
----|-----|-----

> 图片来源 [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **通过帧差检测视频中的运动**。如果摄像机是固定的，那么摄像机画面中的帧应该彼此非常相似。由于帧以数组表示，只需对两个连续帧的数组进行相减，就可以得到像素差异。对于静态帧，差异应该很小，而当图像中有显著运动时，差异会变大。

![视频帧和帧差图像](../../../../../translated_images/frame-difference.706f805491a0883c938e16447bf5eb2f7d69e812c7f743cbe7d7c7645168f81f.zh.png)

> 图片来源 [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **使用光流检测运动**。[光流](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html) 允许我们理解视频帧中单个像素的运动。光流有两种类型：

   - **稠密光流** 计算每个像素的运动矢量场。
   - **稀疏光流** 基于图像中的一些显著特征（例如边缘），并构建它们从帧到帧的轨迹。

![光流图像](../../../../../translated_images/optical.1f4a94464579a83a10784f3c07fe7228514714b96782edf50e70ccd59d2d8c4f.zh.png)

> 图片来源 [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

## ✍️ 示例笔记本: OpenCV [尝试 OpenCV 实践](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

让我们通过探索 [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb) 来进行一些 OpenCV 的实验。

## 结论

有时，像运动检测或指尖检测这样相对复杂的任务可以完全通过计算机视觉来解决。因此，了解计算机视觉的基本技术以及像 OpenCV 这样的库的功能非常有帮助。

## 🚀 挑战

观看 [这个视频](https://docs.microsoft.com/shows/ai-show/ai-show--2021-opencv-ai-competition--grand-prize-winners--cortic-tigers--episode-32?WT.mc_id=academic-77998-cacaste)，了解 Cortic Tigers 项目以及他们如何通过机器人构建一个基于模块的解决方案来普及计算机视觉任务。研究其他类似项目，这些项目帮助新学习者进入该领域。

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/206)

## 复习与自学

阅读更多关于光流的内容 [在这个优秀教程中](https://learnopencv.com/optical-flow-in-opencv/)。

## [作业](lab/README.md)

在这个实验中，你将拍摄一个包含简单手势的视频，你的目标是使用光流提取上下左右的运动。

<img src="images/palm-movement.png" width="30%" alt="手掌运动帧"/>

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文档的原始语言版本为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而引起的任何误解或误读不承担责任。