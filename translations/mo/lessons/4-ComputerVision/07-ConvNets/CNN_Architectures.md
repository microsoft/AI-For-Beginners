<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f7b97b375358cb51a1e098df306bf73",
  "translation_date": "2025-08-26T09:30:59+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md",
  "language_code": "mo"
}
-->
# 常見的 CNN 架構

### VGG-16

VGG-16 是一個在 2014 年 ImageNet top-5 分類中達到 92.7% 準確率的網路。它的層結構如下：

![ImageNet 層結構](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.mo.jpg)

如你所見，VGG 採用了傳統的金字塔架構，也就是一系列的卷積-池化層。

![ImageNet 金字塔](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.mo.jpg)

> 圖片來源：[Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet 是由微軟研究院在 2015 年提出的一系列模型。ResNet 的核心概念是使用 **殘差塊**：

<img src="images/resnet-block.png" width="300"/>

> 圖片來源：[這篇論文](https://arxiv.org/pdf/1512.03385.pdf)

使用身份傳遞的原因是讓我們的層預測 **前一層結果與殘差塊輸出之間的差異**，因此得名為 *殘差*。這些塊更容易訓練，並且可以構建包含數百個這樣的塊的網路（最常見的變體有 ResNet-52、ResNet-101 和 ResNet-152）。

你也可以將這個網路理解為能根據數據集調整其複雜度的模型。最初在訓練網路時，權重值較小，大部分信號通過身份傳遞層。隨著訓練進行，權重變大，網路參數的重要性增強，網路會調整以適應所需的表達能力，從而正確分類訓練圖像。

### Google Inception

Google Inception 架構將這個概念更進一步，將每一層構建為多條不同路徑的組合：

<img src="images/inception.png" width="400"/>

> 圖片來源：[Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

在這裡，我們需要強調 1x1 卷積的作用，因為一開始它看起來似乎沒有意義。為什麼我們需要用 1x1 的濾波器掃描圖像？然而，你需要記住，卷積濾波器也會處理多個深度通道（最初是 RGB 顏色，在後續層中是不同濾波器的通道），而 1x1 卷積用於通過不同的可訓練權重混合這些輸入通道。它也可以被視為在通道維度上的降採樣（池化）。

這裡有一篇[關於 1x1 卷積的好文章](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578)，以及[原始論文](https://arxiv.org/pdf/1312.4400.pdf)。

### MobileNet

MobileNet 是一系列縮小尺寸的模型，適合用於移動設備。如果你的資源有限，並且可以接受一些準確率的犧牲，可以考慮使用它們。其核心概念是所謂的 **深度可分離卷積**，它將卷積濾波器表示為空間卷積與深度通道上的 1x1 卷積的組合。這大大減少了參數數量，使網路尺寸更小，也更容易用較少的數據進行訓練。

這裡有一篇[關於 MobileNet 的好文章](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470)。

## 結論

在這一單元中，你學習了計算機視覺神經網路的主要概念——卷積神經網路。現實中的架構（如圖像分類、物體檢測，甚至圖像生成網路）都是基於 CNN 的，只是增加了更多的層數以及一些額外的訓練技巧。

## 🚀 挑戰

在隨附的筆記本中，底部有關於如何獲得更高準確率的筆記。進行一些實驗，看看你是否能達到更高的準確率。

## [課後測驗](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/207)

## 複習與自學

雖然 CNN 最常用於計算機視覺任務，但它們通常也適合用於提取固定大小的模式。例如，如果我們處理的是聲音，我們也可能希望使用 CNN 來尋找音頻信號中的某些特定模式——在這種情況下，濾波器將是一維的（這樣的 CNN 被稱為 1D-CNN）。此外，有時也會使用 3D-CNN 來提取多維空間中的特徵，例如視頻中發生的某些事件——CNN 可以捕捉隨時間變化的某些特徵模式。進行一些複習和自學，了解 CNN 還能完成哪些其他任務。

## [作業](lab/README.md)

在這個實驗中，你的任務是分類不同的貓和狗品種。這些圖像比 MNIST 數據集更複雜，維度更高，並且類別數超過 10。

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解讀概不負責。