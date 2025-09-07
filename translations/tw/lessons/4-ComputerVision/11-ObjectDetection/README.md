<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d85c8b08f6d1b48fd7f35b99f93c1138",
  "translation_date": "2025-08-24T21:57:32+00:00",
  "source_file": "lessons/4-ComputerVision/11-ObjectDetection/README.md",
  "language_code": "tw"
}
-->
# 物件偵測

我們之前討論的影像分類模型，主要是將影像輸入並產生一個分類結果，例如在 MNIST 問題中，分類結果是「數字」類別。然而，在許多情況下，我們不僅僅想知道影像中有物件存在，我們還希望能夠確定它們的精確位置。這正是**物件偵測**的目的所在。

## [課前測驗](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/111)

![物件偵測](../../../../../translated_images/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be1b905373ed9c858102c054b16e4595c76ec3f7bba0feb549.tw.png)

> 圖片來源：[YOLO v2 網站](https://pjreddie.com/darknet/yolov2/)

## 一個簡單的物件偵測方法

假設我們想在一張圖片中找到一隻貓，一個非常簡單的物件偵測方法可能如下：

1. 將圖片分割成多個小區塊。
2. 對每個區塊進行影像分類。
3. 將分類結果中激活值足夠高的區塊視為包含目標物件。

![簡單的物件偵測](../../../../../translated_images/naive-detection.e7f1ba220ccd08c68a2ea8e06a7ed75c3fcc738c2372f9e00b7f4299a8659c01.tw.png)

> *圖片來源：[練習筆記本](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection-TF.ipynb)*

然而，這種方法並不理想，因為它只能非常粗略地定位物件的邊界框。要更精確地定位，我們需要進行某種**回歸**來預測邊界框的座標，而這需要特定的數據集。

## 用回歸進行物件偵測

[這篇部落格文章](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491)提供了一個非常好的物件偵測入門介紹。

## 物件偵測的數據集

在進行物件偵測時，你可能會遇到以下數據集：

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 包含 20 個類別
* [COCO](http://cocodataset.org/#home) - 常見物件的上下文。包含 80 個類別、邊界框和分割遮罩

![COCO](../../../../../translated_images/coco-examples.71bc60380fa6cceb7caad48bd09e35b6028caabd363aa04fee89c414e0870e86.tw.jpg)

## 物件偵測的評估指標

### 交集比聯集 (Intersection over Union, IoU)

在影像分類中，衡量算法表現相對容易，但在物件偵測中，我們需要同時衡量類別的正確性以及推測邊界框位置的精確性。對於後者，我們使用所謂的**交集比聯集** (IoU)，它衡量兩個框（或任意兩個區域）的重疊程度。

![IoU](../../../../../translated_images/iou_equation.9a4751d40fff4e119ecd0a7bcca4e71ab1dc83e0d4f2a0d66ff0859736f593cf.tw.png)

> *圖片來源：[這篇優秀的 IoU 部落格文章](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

概念很簡單——將兩個區域的交集面積除以它們的聯集面積。對於完全重疊的區域，IoU 值為 1；對於完全不相交的區域，IoU 值為 0。其他情況下，IoU 值介於 0 到 1 之間。我們通常只考慮 IoU 超過某個值的邊界框。

### 平均精度 (Average Precision, AP)

假設我們想衡量某個類別 $C$ 的物件識別效果。為了衡量它，我們使用**平均精度**指標，其計算方式如下：

1. 考慮精度-召回曲線，顯示隨著偵測閾值（從 0 到 1）變化的準確性。
2. 根據閾值，我們會在影像中偵測到更多或更少的物件，並得到不同的精度和召回值。
3. 曲線看起來如下：

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *圖片來源：[NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

某個類別 $C$ 的平均精度是該曲線下的面積。更精確地說，召回軸通常分為 10 個部分，精度在所有這些點上進行平均：

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP 和 IoU

我們只考慮那些 IoU 超過某個值的偵測。例如，在 PASCAL VOC 數據集中，通常假設 $\mbox{IoU Threshold} = 0.5$，而在 COCO 數據集中，AP 是針對不同的 $\mbox{IoU Threshold}$ 值進行測量的。

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *圖片來源：[NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### 平均平均精度 - mAP

物件偵測的主要評估指標是**平均平均精度** (Mean Average Precision, mAP)。它是所有物件類別的平均精度值，有時也包括不同的 $\mbox{IoU Threshold}$。更詳細的 mAP 計算過程可以參考
[這篇部落格文章](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)，以及[這裡的程式碼範例](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734)。

## 不同的物件偵測方法

物件偵測算法主要分為兩大類：

* **區域提案網絡** (Region Proposal Networks)（如 R-CNN、Fast R-CNN、Faster R-CNN）。主要思想是生成**感興趣區域** (ROI)，並對其進行 CNN 分析以尋找最大激活值。這與簡單方法有些相似，但 ROI 是以更聰明的方式生成的。這類方法的一個主要缺點是速度較慢，因為需要多次對影像進行 CNN 分析。
* **單次通過** (One-pass) 方法（如 YOLO、SSD、RetinaNet）。這些架構設計的網絡能在一次通過中同時預測類別和 ROI。

### R-CNN: 基於區域的 CNN

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) 使用 [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) 生成 ROI 區域的層次結構，然後通過 CNN 特徵提取器和 SVM 分類器來確定物件類別，並通過線性回歸來確定*邊界框*座標。[官方論文](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/rcnn1.cae407020dfb1d1fb572656e44f75cd6c512cc220591c116c506652c10e47f26.tw.png)

> *圖片來源：van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/rcnn2.2d9530bb83516484ec65b250c22dbf37d3d23244f32864ebcb91d98fe7c3112c.tw.png)

> *圖片來源：[這篇部落格](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - 快速 R-CNN

這種方法與 R-CNN 類似，但區域是在卷積層應用後定義的。

![FRCNN](../../../../../translated_images/f-rcnn.3cda6d9bb41888754037d2d9763e2298a96de5d9bc2a21db3147357aa5da9b1a.tw.png)

> 圖片來源：[官方論文](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf)，[arXiv](https://arxiv.org/pdf/1504.08083.pdf)，2015

### Faster R-CNN

這種方法的主要思想是使用神經網絡來預測 ROI，即所謂的*區域提案網絡*。[論文](https://arxiv.org/pdf/1506.01497.pdf)，2016

![FasterRCNN](../../../../../translated_images/faster-rcnn.8d46c099b87ef30ab2ea26dbc4bdd85b974a57ba8eb526f65dc4cd0a4711de30.tw.png)

> 圖片來源：[官方論文](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: 基於區域的全卷積網絡

這種算法比 Faster R-CNN 更快。主要思想如下：

1. 使用 ResNet-101 提取特徵。
2. 特徵通過**位置敏感分數圖**處理。每個類別 $C$ 的物件被分成 $k\times k$ 區域，我們訓練網絡來預測物件的部分。
3. 對於 $k\times k$ 區域中的每個部分，所有網絡對物件類別進行投票，選擇得票最多的物件類別。

![r-fcn 圖片](../../../../../translated_images/r-fcn.13eb88158b99a3da50fa2787a6be5cb310d47f0e9655cc93a1090dc7aab338d1.tw.png)

> 圖片來源：[官方論文](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO 是一種即時的單次通過算法。主要思想如下：

 * 將影像分成 $S\times S$ 區域。
 * 對每個區域，**CNN** 預測 $n$ 個可能的物件、*邊界框*座標以及*置信度*=*概率* * IoU。

 ![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.tw.png)

> 圖片來源：[官方論文](https://arxiv.org/abs/1506.02640)

### 其他算法

* RetinaNet: [官方論文](https://arxiv.org/abs/1708.02002)
   - [PyTorch 實現](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Keras 實現](https://github.com/fizyr/keras-retinanet)
   - [RetinaNet 物件偵測](https://keras.io/examples/vision/retinanet/)（Keras 範例）
* SSD (單次偵測器): [官方論文](https://arxiv.org/abs/1512.02325)

## ✍️ 練習：物件偵測

繼續學習以下筆記本：

[ObjectDetection.ipynb](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)

## 結論

在本課中，你快速瀏覽了各種物件偵測方法！

## 🚀 挑戰

閱讀以下文章和筆記本，並嘗試使用 YOLO：

* [優秀的部落格文章](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) 描述 YOLO
 * [官方網站](https://pjreddie.com/darknet/yolo/)
 * YOLO: [Keras 實現](https://github.com/experiencor/keras-yolo2)，[逐步筆記本](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * YOLO v2: [Keras 實現](https://github.com/experiencor/keras-yolo2)，[逐步筆記本](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [課後測驗](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## 回顧與自學

* [物件偵測](https://tjmachinelearning.com/lectures/1718/obj/) 作者：Nikhil Sardana
* [物件偵測算法的良好比較](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [深度學習物件偵測算法回顧](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [物件偵測算法的逐步介紹](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Python 中 Faster R-CNN 的物件偵測實現](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [作業：物件偵測](lab/README.md)

**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對於因使用此翻譯而引起的任何誤解或誤讀概不負責。