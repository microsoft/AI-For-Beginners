# 物件偵測

我們之前處理的影像分類模型，會將影像輸入並產生一個分類結果，例如在 MNIST 問題中，分類為「數字」的類別。然而，在許多情況下，我們不僅僅想知道圖片中有物件，我們還希望能夠確定它們的精確位置。這正是**物件偵測**的目的。

## [課前測驗](https://ff-quizzes.netlify.app/en/ai/quiz/21)

![物件偵測](../../../../../translated_images/zh-MO/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be.webp)

> 圖片來源：[YOLO v2 網站](https://pjreddie.com/darknet/yolov2/)

## 一個簡單的物件偵測方法

假設我們想在一張圖片中找到一隻貓，一個非常簡單的物件偵測方法如下：

1. 將圖片分割成多個小區塊。
2. 對每個區塊進行影像分類。
3. 將分類結果中激活值足夠高的區塊視為包含目標物件的區域。

![簡單的物件偵測](../../../../../translated_images/zh-MO/naive-detection.e7f1ba220ccd08c6.webp)

> *圖片來源：[練習筆記本](ObjectDetection-TF.ipynb)*

然而，這種方法並不理想，因為它只能非常粗略地定位物件的邊界框。為了更精確地定位，我們需要進行某種**迴歸**來預測邊界框的座標，而這需要特定的數據集。

## 用迴歸進行物件偵測

[這篇部落格文章](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491)對於偵測形狀提供了一個很好的入門介紹。

## 物件偵測的數據集

在這個任務中，你可能會遇到以下數據集：

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 包含 20 個類別
* [COCO](http://cocodataset.org/#home) - 常見物件的上下文。包含 80 個類別、邊界框和分割遮罩

![COCO](../../../../../translated_images/zh-MO/coco-examples.71bc60380fa6cceb.webp)

## 物件偵測的評估指標

### 交集比聯集 (IoU)

對於影像分類來說，衡量演算法的表現相對簡單；但對於物件偵測，我們需要同時衡量類別的正確性以及推測邊界框位置的精確性。後者使用所謂的**交集比聯集**（IoU）來衡量，這是一種用來評估兩個框（或任意兩個區域）重疊程度的方法。

![IoU](../../../../../translated_images/zh-MO/iou_equation.9a4751d40fff4e11.webp)

> *圖片來源：[這篇優秀的 IoU 部落格文章](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

概念很簡單——將兩個區域的交集面積除以它們的聯集面積。對於完全相同的區域，IoU 值為 1；對於完全不相交的區域，IoU 值為 0。其他情況下，IoU 值介於 0 到 1 之間。我們通常只考慮 IoU 超過某個值的邊界框。

### 平均精度 (AP)

假設我們想衡量某個類別 $C$ 的物件被識別的效果。為此，我們使用**平均精度**（AP）指標，其計算方式如下：

1. 考慮一條精度-召回曲線，該曲線顯示了檢測閾值（從 0 到 1）對應的準確性。
2. 根據閾值，我們會在圖片中檢測到更多或更少的物件，並得到不同的精度和召回值。
3. 曲線看起來如下：

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *圖片來源：[NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

對於給定類別 $C$ 的平均精度是這條曲線下的面積。更精確地說，召回軸通常被分為 10 個部分，並在這些點上平均精度值：

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP 和 IoU

我們只考慮那些 IoU 超過某個值的檢測。例如，在 PASCAL VOC 數據集中，通常假設 $\mbox{IoU Threshold} = 0.5$，而在 COCO 中，AP 是針對不同的 $\mbox{IoU Threshold}$ 值進行測量的。

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *圖片來源：[NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### 平均平均精度 - mAP

物件偵測的主要評估指標稱為**平均平均精度**（mAP）。它是所有物件類別的平均精度值，有時也包括不同 $\mbox{IoU Threshold}$ 的平均值。更詳細的 mAP 計算過程可以參考
[這篇部落格文章](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3))，以及[這裡的程式碼範例](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734)。

## 不同的物件偵測方法

物件偵測演算法大致分為兩類：

* **區域提議網路**（R-CNN、Fast R-CNN、Faster R-CNN）。主要思想是生成**感興趣區域**（ROI），並對其運行 CNN，尋找最大激活值。這與簡單方法有些相似，但 ROI 是以更聰明的方式生成的。這類方法的主要缺點是速度較慢，因為需要對圖片進行多次 CNN 分類。
* **單次通過**（YOLO、SSD、RetinaNet）方法。在這些架構中，網路設計為一次性預測類別和 ROI。

### R-CNN: 基於區域的 CNN

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) 使用 [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) 生成層次結構的 ROI 區域，然後通過 CNN 特徵提取器和 SVM 分類器來確定物件類別，並通過線性迴歸確定*邊界框*座標。[官方論文](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/zh-MO/rcnn1.cae407020dfb1d1f.webp)

> *圖片來源：van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/zh-MO/rcnn2.2d9530bb83516484.webp)

> *圖片來源：[這篇部落格](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - 快速 R-CNN

這種方法與 R-CNN 類似，但區域是在卷積層應用之後定義的。

![FRCNN](../../../../../translated_images/zh-MO/f-rcnn.3cda6d9bb4188875.webp)

> 圖片來源：[官方論文](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf)，[arXiv](https://arxiv.org/pdf/1504.08083.pdf)，2015

### Faster R-CNN

這種方法的主要思想是使用神經網路來預測 ROI，即所謂的*區域提議網路*。[論文](https://arxiv.org/pdf/1506.01497.pdf)，2016

![FasterRCNN](../../../../../translated_images/zh-MO/faster-rcnn.8d46c099b87ef30a.webp)

> 圖片來源：[官方論文](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: 基於區域的全卷積網路

這種演算法比 Faster R-CNN 更快。主要思想如下：

1. 使用 ResNet-101 提取特徵。
2. 特徵經過**位置敏感分數圖**處理。每個來自 $C$ 類別的物件被劃分為 $k\times k$ 區域，並訓練網路預測物件的部分。
3. 對於 $k\times k$ 區域中的每個部分，所有網路對物件類別進行投票，選擇得票最多的物件類別。

![r-fcn 圖片](../../../../../translated_images/zh-MO/r-fcn.13eb88158b99a3da.webp)

> 圖片來源：[官方論文](https://arxiv.org/abs/1605.06409)

### YOLO - 你只需看一次

YOLO 是一種實時的單次通過演算法。主要思想如下：

 * 將圖片劃分為 $S\times S$ 區域。
 * 對於每個區域，**CNN** 預測 $n$ 個可能的物件、*邊界框*座標以及*置信度*=*概率* * IoU。

 ![YOLO](../../../../../translated_images/zh-MO/yolo.a2648ec82ee8bb4e.webp)

> 圖片來源：[官方論文](https://arxiv.org/abs/1506.02640)

### 其他演算法

* RetinaNet: [官方論文](https://arxiv.org/abs/1708.02002)
   - [PyTorch 實現](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Keras 實現](https://github.com/fizyr/keras-retinanet)
   - [Keras 範例中的 RetinaNet](https://keras.io/examples/vision/retinanet/)
* SSD (單次檢測器): [官方論文](https://arxiv.org/abs/1512.02325)

## ✍️ 練習：物件偵測

繼續學習以下筆記本：

[ObjectDetection.ipynb](ObjectDetection.ipynb)

## 結論

在本課中，你快速瀏覽了各種物件偵測的方法！

## 🚀 挑戰

閱讀以下關於 YOLO 的文章和筆記本，並嘗試實作：

* [優秀的部落格文章](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) 描述 YOLO
 * [官方網站](https://pjreddie.com/darknet/yolo/)
 * Yolo: [Keras 實現](https://github.com/experiencor/keras-yolo2)，[逐步筆記本](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [Keras 實現](https://github.com/experiencor/keras-yolo2)，[逐步筆記本](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [課後測驗](https://ff-quizzes.netlify.app/en/ai/quiz/22)

## 回顧與自學

* [物件偵測](https://tjmachinelearning.com/lectures/1718/obj/) by Nikhil Sardana
* [物件偵測演算法的良好比較](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [深度學習物件偵測演算法回顧](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [物件偵測基本演算法的逐步介紹](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [用 Python 實現 Faster R-CNN 進行物件偵測](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [作業：物件偵測](lab/README.md)

---

