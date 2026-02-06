# 物件偵測

我們之前處理的影像分類模型，通常是輸入一張圖片並產生一個分類結果，例如在 MNIST 問題中得到「數字」這個類別。然而，在許多情況下，我們不僅僅想知道圖片中有物件存在，我們還希望能夠確定它們的精確位置。這正是**物件偵測**的目的。

## [課前測驗](https://ff-quizzes.netlify.app/en/ai/quiz/21)

![物件偵測](../../../../../translated_images/zh-TW/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be.webp)

> 圖片來源：[YOLO v2 網站](https://pjreddie.com/darknet/yolov2/)

## 一個簡單的物件偵測方法

假設我們想在一張圖片中找到一隻貓，一個非常簡單的物件偵測方法可能如下：

1. 將圖片分割成多個小區塊。
2. 對每個區塊進行影像分類。
3. 對於分類結果有足夠高信心的區塊，可以認為包含目標物件。

![簡單物件偵測](../../../../../translated_images/zh-TW/naive-detection.e7f1ba220ccd08c6.webp)

> *圖片來源：[練習筆記本](ObjectDetection-TF.ipynb)*

然而，這種方法並不理想，因為它只能非常粗略地定位物件的邊界框。為了更精確地定位，我們需要進行某種**回歸**來預測邊界框的座標，而這需要特定的數據集。

## 用回歸進行物件偵測

[這篇部落格文章](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491)提供了一個非常好的入門指南，介紹如何偵測形狀。

## 物件偵測的數據集

在進行物件偵測時，你可能會遇到以下數據集：

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 包含 20 個類別
* [COCO](http://cocodataset.org/#home) - 常見物件的上下文。包含 80 個類別、邊界框和分割遮罩

![COCO](../../../../../translated_images/zh-TW/coco-examples.71bc60380fa6cceb.webp)

## 物件偵測的評估指標

### 交集比聯集 (Intersection over Union, IoU)

在影像分類中，衡量算法表現相對簡單；但在物件偵測中，我們需要同時衡量類別的正確性以及推測邊界框位置的精確性。對於後者，我們使用所謂的**交集比聯集** (IoU)，它衡量兩個框（或任意兩個區域）的重疊程度。

![IoU](../../../../../translated_images/zh-TW/iou_equation.9a4751d40fff4e11.webp)

> *圖片來源：[這篇優秀的 IoU 部落格文章](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

概念很簡單——將兩個圖形的交集面積除以它們的聯集面積。對於完全相同的區域，IoU 值為 1；而對於完全不相交的區域，IoU 值為 0。其他情況下，IoU 值介於 0 到 1 之間。我們通常只考慮 IoU 超過某個值的邊界框。

### 平均精度 (Average Precision, AP)

假設我們想衡量某個類別 $C$ 的物件被識別的效果。為了衡量這一點，我們使用**平均精度**指標，其計算方式如下：

1. 考慮精度-召回曲線，顯示檢測閾值（從 0 到 1）對準確性的影響。
2. 根據閾值，我們會在圖片中檢測到更多或更少的物件，並得到不同的精度和召回值。
3. 曲線看起來如下：

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *圖片來源：[NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

給定類別 $C$ 的平均精度是該曲線下的面積。更精確地說，召回軸通常分為 10 部分，精度在所有這些點上取平均值：

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP 和 IoU

我們只考慮那些 IoU 超過某個值的檢測。例如，在 PASCAL VOC 數據集中，通常假設 $\mbox{IoU Threshold} = 0.5$，而在 COCO 中，AP 是針對不同的 $\mbox{IoU Threshold}$ 值進行測量的。

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *圖片來源：[NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### 平均平均精度 - mAP

物件偵測的主要指標稱為**平均平均精度** (Mean Average Precision, mAP)。它是所有物件類別的平均精度，有時也包括不同的 $\mbox{IoU Threshold}$。更詳細的 mAP 計算過程可以參考
[這篇部落格文章](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)，以及[這裡的程式碼範例](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734)。

## 不同的物件偵測方法

物件偵測算法主要分為兩大類：

* **區域提案網路** (Region Proposal Networks)（如 R-CNN、Fast R-CNN、Faster R-CNN）。主要思想是生成**感興趣區域** (ROI)，並對其進行 CNN 分析以尋找最大激活值。這與簡單方法有些相似，但 ROI 是以更聰明的方式生成的。這類方法的主要缺點是速度較慢，因為需要多次 CNN 分類器的運行。
* **一次通過** (One-pass) 方法（如 YOLO、SSD、RetinaNet）。這些架構設計成一次性預測類別和 ROI。

### R-CNN: 基於區域的 CNN

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) 使用[選擇性搜索](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf)生成 ROI 區域的層次結構，然後通過 CNN 特徵提取器和 SVM 分類器來確定物件類別，並通過線性回歸確定*邊界框*座標。[官方論文](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/zh-TW/rcnn1.cae407020dfb1d1f.webp)

> *圖片來源：van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/zh-TW/rcnn2.2d9530bb83516484.webp)

> *圖片來源：[這篇部落格](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - 快速 R-CNN

這種方法與 R-CNN 類似，但區域是在卷積層應用後定義的。

![FRCNN](../../../../../translated_images/zh-TW/f-rcnn.3cda6d9bb4188875.webp)

> 圖片來源：[官方論文](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf)，[arXiv](https://arxiv.org/pdf/1504.08083.pdf)，2015

### Faster R-CNN

這種方法的主要思想是使用神經網路來預測 ROI，即所謂的*區域提案網路* (Region Proposal Network)。[論文](https://arxiv.org/pdf/1506.01497.pdf)，2016

![FasterRCNN](../../../../../translated_images/zh-TW/faster-rcnn.8d46c099b87ef30a.webp)

> 圖片來源：[官方論文](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: 基於區域的全卷積網路

這種算法比 Faster R-CNN 更快。主要思想如下：

1. 使用 ResNet-101 提取特徵。
2. 特徵通過**位置敏感分數圖** (Position-Sensitive Score Map) 處理。每個類別 $C$ 的物件被分成 $k\times k$ 區域，我們訓練模型來預測物件的部分。
3. 對於 $k\times k$ 區域中的每個部分，所有網路對物件類別進行投票，選擇投票最多的物件類別。

![r-fcn 圖片](../../../../../translated_images/zh-TW/r-fcn.13eb88158b99a3da.webp)

> 圖片來源：[官方論文](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO 是一種即時的一次通過算法。主要思想如下：

 * 將圖片分成 $S\times S$ 區域。
 * 對每個區域，**CNN** 預測 $n$ 個可能的物件、*邊界框*座標以及*信心值*=*概率* * IoU。

 ![YOLO](../../../../../translated_images/zh-TW/yolo.a2648ec82ee8bb4e.webp)

> 圖片來源：[官方論文](https://arxiv.org/abs/1506.02640)

### 其他算法

* RetinaNet: [官方論文](https://arxiv.org/abs/1708.02002)
   - [PyTorch 實現](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Keras 實現](https://github.com/fizyr/keras-retinanet)
   - [RetinaNet 物件偵測](https://keras.io/examples/vision/retinanet/) 在 Keras 範例中
* SSD (單次檢測器): [官方論文](https://arxiv.org/abs/1512.02325)

## ✍️ 練習：物件偵測

繼續學習以下筆記本：

[ObjectDetection.ipynb](ObjectDetection.ipynb)

## 結論

在這節課中，你快速瀏覽了各種物件偵測方法！

## 🚀 挑戰

閱讀以下文章和筆記本，並嘗試使用 YOLO：

* [優秀的部落格文章](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) 描述 YOLO
 * [官方網站](https://pjreddie.com/darknet/yolo/)
 * YOLO: [Keras 實現](https://github.com/experiencor/keras-yolo2)，[逐步筆記本](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * YOLO v2: [Keras 實現](https://github.com/experiencor/keras-yolo2)，[逐步筆記本](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [課後測驗](https://ff-quizzes.netlify.app/en/ai/quiz/22)

## 回顧與自學

* [物件偵測](https://tjmachinelearning.com/lectures/1718/obj/) 作者：Nikhil Sardana
* [物件偵測算法的良好比較](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [深度學習物件偵測算法回顧](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [物件偵測算法的逐步介紹](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Python 中 Faster R-CNN 的物件偵測實現](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [作業：物件偵測](lab/README.md)

---

