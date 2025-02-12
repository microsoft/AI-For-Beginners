# 自编码器

在训练卷积神经网络（CNN）时，我们面临的一个问题是需要大量的标记数据。在图像分类的情况下，我们需要将图像分成不同的类别，这是一项手动的工作。

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/109)

然而，我们可能希望使用原始（未标记）数据来训练CNN特征提取器，这被称为**自监督学习**。我们将使用训练图像作为网络的输入和输出，而不是标签。**自编码器**的主要思想是，我们将有一个**编码器网络**，将输入图像转换为某种**潜在空间**（通常只是一个较小尺寸的向量），然后是**解码器网络**，其目标是重构原始图像。

> ✅ 一个[自编码器](https://wikipedia.org/wiki/Autoencoder)是“用于学习未标记数据的有效编码的一种人工神经网络”。

由于我们正在训练自编码器以尽可能多地捕获原始图像的信息以实现准确的重构，因此网络试图找到输入图像的最佳**嵌入**以捕获其含义。

![自编码器示意图](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.zh.jpg)

> 图片来源于[Keras博客](https://blog.keras.io/building-autoencoders-in-keras.html)

## 使用自编码器的场景

虽然重构原始图像本身似乎没有什么用处，但在一些场景中，自编码器尤其有用：

* **降低图像维度以进行可视化**或**训练图像嵌入**。通常，自编码器的结果优于主成分分析（PCA），因为它考虑了图像的空间特性和层次特征。
* **去噪**，即从图像中去除噪声。由于噪声携带了很多无用的信息，自编码器无法将其全部适应于相对较小的潜在空间，因此它只捕获图像的重要部分。在训练去噪器时，我们从原始图像开始，并使用人为添加噪声的图像作为自编码器的输入。
* **超分辨率**，提高图像分辨率。我们从高分辨率图像开始，并使用较低分辨率的图像作为自编码器的输入。
* **生成模型**。一旦我们训练了自编码器，解码器部分可以用来从随机潜在向量创建新对象。

## 变分自编码器（VAE）

传统自编码器以某种方式减少输入数据的维度，找出输入图像的重要特征。然而，潜在向量往往没有太大意义。换句话说，以MNIST数据集为例，确定哪些数字对应于不同的潜在向量并不是一项简单的任务，因为相近的潜在向量不一定对应于相同的数字。

另一方面，为了训练*生成*模型，最好对潜在空间有一些理解。这一思想引导我们到**变分自编码器**（VAE）。

VAE是学习预测潜在参数的*统计分布*的自编码器，即所谓的**潜在分布**。例如，我们可能希望潜在向量以某个均值 z<sub>mean</sub> 和标准差 z<sub>sigma</sub> 正常分布（均值和标准差都是某个维度 d 的向量）。VAE中的编码器学习预测这些参数，然后解码器从该分布中提取一个随机向量以重构对象。

总结：

* 从输入向量，我们预测 `z_mean` 和 `z_log_sigma` （而不是直接预测标准差本身，我们预测其对数）
* 我们从分布 N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>)) 中采样一个向量 `sample`
* 解码器尝试使用 `sample` 作为输入向量来解码原始图像

<img src="images/vae.png" width="50%">

> 图片来自[这篇博客文章](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)，作者为Isaak Dykeman

变分自编码器使用一个复杂的损失函数，由两个部分组成：

* **重构损失**是显示重构图像与目标图像接近程度的损失函数（可以是均方误差，或MSE）。它与普通自编码器中的损失函数相同。
* **KL损失**，确保潜在变量分布接近于正态分布。它基于[Kullback-Leibler散度](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained)的概念 - 一种估计两个统计分布相似度的度量。

VAE的一个重要优势是它们相对容易生成新图像，因为我们知道从哪个分布中采样潜在向量。例如，如果我们在MNIST上用二维潜在向量训练VAE，我们可以变更潜在向量的各个分量以获取不同的数字：

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> 图片由[Dmitry Soshnikov](http://soshnikov.com)提供

观察到图像如何相互融合，因为我们开始从潜在参数空间的不同部分获取潜在向量。我们还可以在二维中可视化这个空间：

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> 图片由[Dmitry Soshnikov](http://soshnikov.com)提供

## ✍️ 练习：自编码器

在这些相应的笔记本中了解更多关于自编码器的信息：

* [TensorFlow中的自编码器](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [PyTorch中的自编码器](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## 自编码器的属性

* **数据特定** - 它们仅在训练过的图像类型上表现良好。例如，如果我们在花卉上训练一个超分辨率网络，它在肖像上效果不好。这是因为网络可以通过从训练数据集中学习的特征中提取细节来生成更高分辨率的图像。
* **有损** - 重构图像与原始图像并不相同。损失的性质由训练过程中使用的*损失函数*定义。
* 适用于**未标记数据**

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/209)

## 结论

在本节课中，您了解了可供AI科学家使用的各种类型的自编码器。您学习了如何构建它们，以及如何使用它们来重构图像。您还了解了VAE以及如何使用它生成新图像。

## 🚀 挑战

在本节课中，您了解了使用自编码器处理图像。但它们也可以用于音乐！查看Magenta项目的[MusicVAE](https://magenta.tensorflow.org/music-vae)项目，该项目使用自编码器学习重构音乐。与这个库进行一些[实验](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb)，看看您能创造出什么。

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## 复习与自学

作为参考，阅读这些资源以了解更多关于自编码器的信息：

* [在Keras中构建自编码器](https://blog.keras.io/building-autoencoders-in-keras.html)
* [关于NeuroHive的博客文章](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [变分自编码器解释](https://kvfrans.com/variational-autoencoders-explained/)
* [条件变分自编码器](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## 作业

在[这个使用TensorFlow的笔记本](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)的最后，您会找到一个“任务” - 将其作为您的作业。

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。虽然我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应视为权威来源。对于关键信息，建议进行专业的人类翻译。我们对因使用本翻译而产生的任何误解或误读不承担任何责任。