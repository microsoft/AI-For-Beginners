# 神經網路入門：感知器

## [課前測驗](https://ff-quizzes.netlify.app/en/ai/quiz/5)

1957年，康奈爾航空實驗室的 Frank Rosenblatt 嘗試實現了一種類似現代神經網路的模型。這是一個名為 "Mark-1" 的硬體實現，設計用來識別基本幾何圖形，例如三角形、正方形和圓形。

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/zh-TW/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/zh-TW/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='The Mark 1 Perceptron' />|

> 圖片來源：[維基百科](https://en.wikipedia.org/wiki/Perceptron)

輸入圖像由 20x20 的光電陣列表示，因此神經網路有 400 個輸入和一個二元輸出。一個簡單的網路包含一個神經元，也被稱為 **閾值邏輯單元**。神經網路的權重類似於電位器，需要在訓練階段手動調整。

> ✅ 電位器是一種允許使用者調整電路阻抗的裝置。

> 《紐約時報》當時對感知器的描述是：*一種電子計算機的胚胎，[海軍]期望它能夠行走、說話、看見、書寫、自我複製並意識到自己的存在。*

## 感知器模型

假設我們的模型有 N 個特徵，此時輸入向量將是一個大小為 N 的向量。感知器是一種 **二元分類** 模型，也就是說它可以區分兩類輸入數據。我們假設對於每個輸入向量 x，感知器的輸出將是 +1 或 -1，取決於所屬的類別。輸出通過以下公式計算：

y(x) = f(w<sup>T</sup>x)

其中 f 是一個階梯激活函數

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/zh-TW/activation-func.b4924007c7ce7764.webp"/>

## 訓練感知器

要訓練感知器，我們需要找到一個權重向量 w，使得大部分數據能夠被正確分類，也就是使 **誤差** 最小化。這個誤差 E 根據 **感知器準則** 定義如下：

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

其中：

* 求和僅針對那些分類錯誤的訓練數據點 i
* x<sub>i</sub> 是輸入數據，t<sub>i</sub> 對應於負例和正例分別為 -1 或 +1。

這個準則被視為權重 w 的函數，我們需要對其進行最小化。通常使用一種稱為 **梯度下降** 的方法，我們從某個初始權重 w<sup>(0)</sup> 開始，然後在每一步根據以下公式更新權重：

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

其中 &eta; 是所謂的 **學習率**，&nabla;E(w) 表示 E 的 **梯度**。計算梯度後，我們得到：

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Python 中的算法如下：

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

## 結論

在本課中，你學習了感知器這種二元分類模型，以及如何通過使用權重向量來訓練它。

## 🚀 挑戰

如果你想嘗試自己構建一個感知器，可以試試 [Microsoft Learn 的這個實驗](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste)，它使用了 [Azure ML 設計器](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste)。

## [課後測驗](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## 回顧與自學

要了解如何使用感知器解決玩具問題以及實際問題，並繼續學習，請參考 [Perceptron](Perceptron.ipynb) 筆記本。

這裡還有一篇有趣的[感知器相關文章](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590)。

## [作業](lab/README.md)

在本課中，我們實現了一個用於二元分類任務的感知器，並使用它來區分兩個手寫數字。在這次實驗中，你需要完全解決數字分類問題，也就是確定給定圖像最可能對應的數字。

* [指導說明](lab/README.md)
* [筆記本](lab/PerceptronMultiClass.ipynb)

---

