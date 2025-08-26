<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-26T09:14:16+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "mo"
}
-->
# 生成對抗網絡

在上一節中，我們學習了**生成模型**：這些模型可以生成與訓練數據集中的圖像相似的新圖像。VAE 是生成模型的一個很好的例子。

## [課前測驗](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

然而，如果我們嘗試生成一些真正有意義的東西，比如一幅具有合理解析度的畫作，使用 VAE 可能會發現訓練效果不佳。針對這種情況，我們需要學習另一種專門用於生成模型的架構——**生成對抗網絡**，簡稱 GAN。

GAN 的主要思想是使用兩個神經網絡，並讓它們相互對抗進行訓練：

<img src="images/gan_architecture.png" width="70%"/>

> 圖片來源：[Dmitry Soshnikov](http://soshnikov.com)

> ✅ 一些術語：
> * **生成器（Generator）** 是一個網絡，它接收一個隨機向量，並生成一幅圖像作為結果。
> * **判別器（Discriminator）** 是一個網絡，它接收一幅圖像，並判斷該圖像是真實圖像（來自訓練數據集）還是由生成器生成的。它本質上是一個圖像分類器。

### 判別器

判別器的架構與普通的圖像分類網絡並無不同。在最簡單的情況下，它可以是一個全連接分類器，但更可能是一個[卷積網絡](../07-ConvNets/README.md)。

> ✅ 基於卷積網絡的 GAN 被稱為 [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

一個 CNN 判別器由以下層組成：幾個卷積+池化層（空間尺寸逐漸減小），以及一個或多個全連接層以獲得“特徵向量”，最後是一個二元分類器。

> ✅ 在這裡，“池化”是一種減小圖像尺寸的技術。“池化層通過將一層中神經元簇的輸出合併為下一層中的單個神經元來減少數據的維度。”——[來源](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### 生成器

生成器稍微複雜一些。你可以將其視為一個反向的判別器。從一個潛在向量（類似於特徵向量）開始，它通過一個全連接層轉換為所需的尺寸/形狀，然後是反卷積+上採樣。這與[自編碼器](../09-Autoencoders/README.md)的*解碼器*部分類似。

> ✅ 由於卷積層是通過線性濾波器遍歷圖像來實現的，反卷積本質上與卷積類似，可以使用相同的層邏輯來實現。

<img src="images/gan_arch_detail.png" width="70%"/>

> 圖片來源：[Dmitry Soshnikov](http://soshnikov.com)

### 訓練 GAN

GAN 被稱為**對抗性**，因為生成器和判別器之間存在持續的競爭。在這種競爭中，生成器和判別器都會不斷改進，從而使網絡學會生成越來越好的圖像。

訓練分為兩個階段：

* **訓練判別器**。這個任務相對簡單：我們生成一批由生成器生成的圖像，標記為 0（代表假圖像），並從輸入數據集中取一批圖像（標記為 1，真實圖像）。我們計算出一些*判別器損失*，然後進行反向傳播。
* **訓練生成器**。這稍微複雜一些，因為我們無法直接知道生成器的期望輸出。我們將整個 GAN 網絡（由生成器和判別器組成）輸入一些隨機向量，並期望結果為 1（對應於真實圖像）。然後我們凍結判別器的參數（此步驟不希望訓練判別器），並進行反向傳播。

在這個過程中，生成器和判別器的損失不會顯著下降。在理想情況下，它們應該呈現振盪，這表明兩個網絡的性能都在提高。

## ✍️ 練習：GANs

* [TensorFlow/Keras 的 GAN Notebook](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [PyTorch 的 GAN Notebook](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### GAN 訓練的問題

GAN 以訓練困難著稱。以下是一些常見問題：

* **模式崩潰（Mode Collapse）**。這是指生成器學會生成一個成功欺騙判別器的圖像，而不是生成多樣化的圖像。
* **對超參數的敏感性**。經常會看到 GAN 完全無法收斂，然後突然因學習率的減小而收斂。
* **生成器與判別器之間的平衡**。在許多情況下，判別器的損失可能會迅速降為零，導致生成器無法進一步訓練。為了解決這個問題，我們可以嘗試為生成器和判別器設置不同的學習率，或者在判別器損失已經很低時跳過其訓練。
* **高解析度訓練**。與自編碼器的問題類似，重建過多層的卷積網絡會導致伪影。這個問題通常通過所謂的**漸進式增長**來解決，首先在低解析度圖像上訓練幾層，然後“解鎖”或添加更多層。另一種解決方案是增加層之間的額外連接，並同時訓練多個解析度——詳情請參考這篇[多尺度梯度 GAN 論文](https://arxiv.org/abs/1903.06048)。

## 風格遷移

GAN 是生成藝術圖像的一種好方法。另一種有趣的技術是所謂的**風格遷移**，它將一幅**內容圖像**重新繪製為另一種風格，應用來自**風格圖像**的濾鏡。

其工作原理如下：
* 我們從一幅隨機噪聲圖像開始（或者從內容圖像開始，但為了便於理解，從隨機噪聲開始更簡單）。
* 我們的目標是創建一幅圖像，使其同時接近內容圖像和風格圖像。這由兩個損失函數決定：
   - **內容損失**基於 CNN 在某些層提取的當前圖像與內容圖像的特徵計算。
   - **風格損失**通過使用 Gram 矩陣以巧妙的方式計算當前圖像與風格圖像之間的差異（更多細節請參考[示例 Notebook](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)）。
* 為了使圖像更平滑並去除噪聲，我們還引入了**變異損失**，它計算相鄰像素之間的平均距離。
* 主優化循環使用梯度下降（或其他優化算法）調整當前圖像，以最小化總損失，這是所有三個損失的加權和。

## ✍️ 示例：[風格遷移](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [課後測驗](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## 總結

在本課中，你學習了 GAN 的基本概念以及如何訓練它們。你還了解了這種類型的神經網絡可能面臨的特殊挑戰，以及一些解決這些挑戰的策略。

## 🚀 挑戰

使用你自己的圖像運行[風格遷移 Notebook](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)。

## 複習與自學

參考以下資源，進一步了解 GAN：

* Marco Pasini，[我在訓練 GAN 一年中學到的 10 個教訓](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN)，一個值得考慮的 GAN 標準架構
* [在 Azure ML 上使用 GAN 創建生成藝術](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## 作業

重溫本課程相關的兩個 Notebook 中的一個，並使用你自己的圖像重新訓練 GAN。你能創造出什麼？

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。