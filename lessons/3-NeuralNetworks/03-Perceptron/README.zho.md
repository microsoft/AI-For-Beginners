# 神经网络简介： 感知器

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

1957 年，康奈尔航空实验室的弗兰克-罗森布拉特（Frank Rosenblatt）首次尝试实现与现代神经网络类似的功能。这是一种名为 "Mark-1 "的硬件实现，旨在识别三角形、正方形和圆形等原始几何图形。

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Images [from Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

输入图像由 20x20 光电池阵列表示，因此神经网络有 400 个输入和一个二进制输出。一个简单的网络包含一个神经元，也称为**阈值逻辑单元**。神经网络的权重就像电位器，在训练阶段需要手动调整。

> ✅ 电位器是一种允许用户调节电路电阻的装置。

> 《纽约时报》当时对感知器进行了报道： *[海军]希望这种电子计算机的雏形能够行走、说话、看东西、写字、自我复制并意识到自己的存在。

##感知器模型

假设我们的模型有 N 个特征，那么输入向量就是一个大小为 N 的向量。感知器是一个**二元分类**模型，即它可以区分输入数据的两个类别。我们假定，对于每个输入向量 x，感知器的输出都是+1或-1，具体取决于类别。输出的计算公式为

y(x) = f(w<sup>T</sup>x)

其中，f 是阶跃激活函数

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## 训练感知器

要训练感知器，我们需要找到一个权重向量 w，它能正确地对大部分数值进行分类，即产生最小的**误差**。这个误差由**感知器准则**定义，其方式如下：

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

也就是:

* 对导致错误分类的训练数据点 i 求和
* x<sub>i</sub> s 为输入数据，t<sub>i</sub> 根据负相关或者正相关相应的的"-1 "或 "+1"。

这个标准被视为权重 w 的函数，我们需要将其最小化。通常情况下，我们会使用一种名为**梯度下降**的方法，即从一些初始权重开始计算 w<sup>(0)</sup>, 然后每一步都根据公式更新权重：

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

 &eta; 即所谓的**学习率**, 并且 &nabla;E(w) 表示 E 的**梯度**。 计算梯度后，我们得出

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Python 中的算法如下所示：

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

## 结论

在这一课中，你了解了二元分类模型感知器，以及如何使用权重向量来训练感知器。

## 🚀 挑战

如果你想建立自己的感知器，请尝试 [this lab on Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) which uses the [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## Review & Self Study

To see how we can use perceptron to solve a toy problem as well as real-life problems, and to continue learning - go to [Perceptron](Perceptron.ipynb) notebook.

Here's an interesting [article about perceptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590
) as well.

## [Assignment](lab/README.md)

In this lesson, we have implemented a perceptron for binary classification task, and we have used it to classify between two handwritten digits. In this lab, you are asked to solve the problem of digit classification entirely, i.e. determine which digit is most likely to correspond to a given image.

* [Instructions](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)
