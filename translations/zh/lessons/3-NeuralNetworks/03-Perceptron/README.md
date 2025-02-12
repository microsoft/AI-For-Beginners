# 神经网络导论：感知器

## [课前测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

1957年，康奈尔航空实验室的Frank Rosenblatt首次尝试实现类似现代神经网络的东西。这是一个名为“Mark-1”的硬件实现，旨在识别简单的几何图形，如三角形、正方形和圆形。

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 图片 [来自维基百科](https://en.wikipedia.org/wiki/Perceptron)

输入图像由20x20的光电池阵列表示，因此神经网络有400个输入和一个二进制输出。一个简单的网络包含一个神经元，也称为**阈值逻辑单元**。神经网络的权重像电位器一样，在训练阶段需要手动调整。

> ✅ 电位器是一种允许用户调整电路电阻的设备。

> 《纽约时报》当时对感知器的描述是：*海军期望这将是一个能够行走、说话、看、写、复制自己并意识到自己存在的电子计算机的胚胎。*

## 感知器模型

假设我们的模型中有N个特征，在这种情况下，输入向量将是大小为N的向量。感知器是一个**二分类**模型，即它能够区分两类输入数据。我们假设对于每个输入向量x，感知器的输出要么是+1，要么是-1，这取决于类别。输出将通过以下公式计算：

y(x) = f(w<sup>T</sup>x)

其中f是阶跃激活函数

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## 训练感知器

要训练一个感知器，我们需要找到一个权重向量w，使大多数值正确分类，即使**错误**最小化。这个错误E通过**感知器准则**定义如下：

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

其中：

* 求和是在那些导致错误分类的训练数据点i上进行的
* x<sub>i</sub>是输入数据，而t<sub>i</sub>对于负例和正例分别为-1和+1。

这个准则被视为权重w的一个函数，我们需要对其进行最小化。通常使用一种称为**梯度下降**的方法，在这种方法中，我们从一些初始权重w<sup>(0)</sup>开始，然后在每一步根据以下公式更新权重：

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

这里η是所谓的**学习率**，∇E(w)表示E的**梯度**。在计算梯度后，我们得到

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

在Python中的算法如下所示：

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

在本课中，您了解了感知器，它是一个二分类模型，以及如何通过使用权重向量来训练它。

## 🚀 挑战

如果您想尝试构建自己的感知器，可以尝试 [Microsoft Learn上的这个实验室](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste)，该实验室使用了 [Azure ML设计器](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste)。

## [课后测验](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## 复习与自学

要了解我们如何使用感知器解决玩具问题以及现实生活中的问题，并继续学习，请访问 [感知器](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb) 笔记本。

这里还有一篇关于感知器的有趣 [文章](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590)。

## [作业](lab/README.md)

在本课中，我们实现了一个用于二分类任务的感知器，并使用它来区分两个手写数字。在这个实验室中，您需要完全解决数字分类的问题，即确定哪个数字最有可能对应于给定的图像。

* [说明](lab/README.md)
* [笔记本](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。虽然我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于关键信息，建议进行专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。