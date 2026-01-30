# 神经网络入门：感知机

## [课前测验](https://ff-quizzes.netlify.app/en/ai/quiz/5)

1957年，康奈尔航空实验室的Frank Rosenblatt首次尝试实现类似现代神经网络的模型。这是一种名为“Mark-1”的硬件实现，设计用于识别简单的几何图形，例如三角形、正方形和圆形。

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/zh-CN/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/zh-CN/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='The Mark 1 Perceptron' />|

> 图片来源：[维基百科](https://en.wikipedia.org/wiki/Perceptron)

输入图像由20x20的光电池阵列表示，因此神经网络有400个输入和一个二进制输出。一个简单的网络包含一个神经元，也称为**阈值逻辑单元**。神经网络的权重类似于电位器，在训练阶段需要手动调整。

> ✅ 电位器是一种允许用户调整电路电阻的设备。

> 《纽约时报》当时对感知机的报道是：*一种电子计算机的胚胎，[海军]期望它能够行走、说话、看见、写作、自我复制并意识到自己的存在。*

## 感知机模型

假设我们的模型有N个特征，那么输入向量将是一个大小为N的向量。感知机是一种**二分类**模型，即它可以区分两类输入数据。我们假设对于每个输入向量x，感知机的输出将是+1或-1，具体取决于类别。输出通过以下公式计算：

y(x) = f(w<sup>T</sup>x)

其中f是一个阶跃激活函数

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/zh-CN/activation-func.b4924007c7ce7764.webp"/>

## 训练感知机

为了训练感知机，我们需要找到一个权重向量w，使得大多数值能够被正确分类，即使**误差**最小化。这个误差E通过**感知机准则**定义如下：

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

其中：

* 求和是在那些导致错误分类的训练数据点i上进行的
* x<sub>i</sub>是输入数据，t<sub>i</sub>对于负样本是-1，对于正样本是+1。

这个准则被视为权重w的函数，我们需要对其进行最小化。通常使用一种称为**梯度下降**的方法，我们从一些初始权重w<sup>(0)</sup>开始，然后在每一步根据以下公式更新权重：

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

这里&eta;是所谓的**学习率**，&nabla;E(w)表示E的**梯度**。计算梯度后，我们得到：

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Python中的算法如下：

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## 总结

在本课中，你学习了感知机，这是一种二分类模型，并了解了如何通过使用权重向量来训练它。

## 🚀 挑战

如果你想尝试构建自己的感知机，可以试试[Microsoft Learn上的这个实验](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste)，它使用了[Azure ML设计器](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste)。

## [课后测验](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## 复习与自学

要了解如何使用感知机解决一个简单问题以及实际问题，并继续学习，请查看[感知机](Perceptron.ipynb)笔记本。

这里还有一篇有趣的[关于感知机的文章](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590)。

## [作业](lab/README.md)

在本课中，我们实现了一个用于二分类任务的感知机，并使用它来区分两个手写数字。在本实验中，你需要完全解决数字分类问题，即确定给定图像最可能对应的数字。

* [说明](lab/README.md)
* [笔记本](lab/PerceptronMultiClass.ipynb)

---

