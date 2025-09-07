<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d85c8b08f6d1b48fd7f35b99f93c1138",
  "translation_date": "2025-08-24T21:09:15+00:00",
  "source_file": "lessons/4-ComputerVision/11-ObjectDetection/README.md",
  "language_code": "ja"
}
-->
# オブジェクト検出

これまで扱ってきた画像分類モデルは、画像を入力として受け取り、MNIST問題における「数字」クラスのようなカテゴリカルな結果を出力していました。しかし、多くの場合、画像に物体が写っていることを知るだけでなく、その正確な位置を特定したいと考えます。それがまさに**オブジェクト検出**の目的です。

## [事前クイズ](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/111)

![オブジェクト検出](../../../../../translated_images/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be1b905373ed9c858102c054b16e4595c76ec3f7bba0feb549.ja.png)

> 画像出典: [YOLO v2 ウェブサイト](https://pjreddie.com/darknet/yolov2/)

## オブジェクト検出の単純なアプローチ

例えば、画像内の猫を見つけたいと仮定します。非常に単純なオブジェクト検出のアプローチは以下のようになります：

1. 画像を複数のタイルに分割する
2. 各タイルに対して画像分類を実行する
3. 十分に高い活性化を示したタイルを、対象の物体を含むとみなす

![単純なオブジェクト検出](../../../../../translated_images/naive-detection.e7f1ba220ccd08c68a2ea8e06a7ed75c3fcc738c2372f9e00b7f4299a8659c01.ja.png)

> *画像出典: [演習ノートブック](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection-TF.ipynb)*

しかし、この方法は理想的とは言えません。なぜなら、アルゴリズムが物体の境界ボックスを非常に不正確にしか特定できないからです。より正確な位置を特定するには、境界ボックスの座標を予測するための**回帰**を実行する必要があります。そのためには、特定のデータセットが必要です。

## オブジェクト検出のための回帰

[このブログ記事](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491)では、形状検出についての優しい導入が紹介されています。

## オブジェクト検出のためのデータセット

このタスクに関連する以下のデータセットに出会うかもしれません：

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 20クラス
* [COCO](http://cocodataset.org/#home) - コンテキスト内の一般的な物体。80クラス、境界ボックスとセグメンテーションマスクを含む

![COCO](../../../../../translated_images/coco-examples.71bc60380fa6cceb7caad48bd09e35b6028caabd363aa04fee89c414e0870e86.ja.jpg)

## オブジェクト検出の評価指標

### Intersection over Union (IoU)

画像分類ではアルゴリズムの性能を測定するのは簡単ですが、オブジェクト検出ではクラスの正確性だけでなく、推定された境界ボックスの位置の精度も測定する必要があります。そのために使用されるのが、**Intersection over Union** (IoU) と呼ばれる指標です。これは、2つのボックス（または任意の2つの領域）がどれだけ重なっているかを測定します。

![IoU](../../../../../translated_images/iou_equation.9a4751d40fff4e119ecd0a7bcca4e71ab1dc83e0d4f2a0d66ff0859736f593cf.ja.png)

> *図2 出典: [この優れたIoUに関するブログ記事](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

アイデアはシンプルです。2つの図形の交差部分の面積を、2つの図形の合計面積で割ります。2つの領域が完全に一致している場合、IoUは1になります。一方、完全に分離している場合は0になります。それ以外の場合は0から1の間で変動します。通常、IoUが一定値を超える境界ボックスのみを考慮します。

### 平均精度 (Average Precision)

特定のクラス $C$ の物体がどれだけ正確に認識されているかを測定したいとします。そのために、**平均精度** (Average Precision) 指標を使用します。計算方法は以下の通りです：

1. 検出閾値（0から1まで）に応じた精度-再現率曲線を考慮します。
2. 閾値に応じて、画像内で検出される物体の数や精度・再現率の値が変わります。
3. 曲線は以下のようになります：

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *画像出典: [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

クラス $C$ の平均精度は、この曲線の下の面積です。より正確には、再現率軸を通常10分割し、精度をその各点で平均化します：

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### APとIoU

IoUが一定値を超える検出のみを考慮します。例えば、PASCAL VOCデータセットでは通常 $\mbox{IoU Threshold} = 0.5$ が仮定されます。一方、COCOでは異なる値の $\mbox{IoU Threshold}$ に対してAPが測定されます。

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *画像出典: [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### 平均平均精度 - mAP

オブジェクト検出の主要な評価指標は**平均平均精度** (Mean Average Precision, mAP) と呼ばれます。これは、すべての物体クラスにわたる平均精度の値であり、時には $\mbox{IoU Threshold}$ にもわたって平均化されます。**mAP** の計算プロセスについては、[このブログ記事](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)や[こちらのコードサンプル付きの記事](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734)で詳しく説明されています。

## オブジェクト検出のさまざまなアプローチ

オブジェクト検出アルゴリズムには、大きく分けて2つのクラスがあります：

* **領域提案ネットワーク** (Region Proposal Networks) (R-CNN, Fast R-CNN, Faster R-CNN)。主なアイデアは、**関心領域** (ROI) を生成し、それに対してCNNを実行して最大活性化を探すことです。この方法は単純なアプローチに似ていますが、ROIがより賢く生成される点が異なります。この方法の主な欠点は、画像に対してCNN分類器を何度も実行する必要があるため、遅いことです。
* **ワンパス** (YOLO, SSD, RetinaNet) メソッド。これらのアーキテクチャでは、クラスとROIの両方を1回のパスで予測するようにネットワークを設計します。

### R-CNN: 領域ベースのCNN

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) は、[Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) を使用してROI領域の階層構造を生成します。これらの領域はCNN特徴抽出器とSVM分類器を通じて物体クラスを決定し、線形回帰を使用して*境界ボックス*の座標を決定します。[公式論文](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/rcnn1.cae407020dfb1d1fb572656e44f75cd6c512cc220591c116c506652c10e47f26.ja.png)

> *画像出典: van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/rcnn2.2d9530bb83516484ec65b250c22dbf37d3d23244f32864ebcb91d98fe7c3112c.ja.png)

> *画像出典: [このブログ](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - Fast R-CNN

このアプローチはR-CNNに似ていますが、領域は畳み込み層が適用された後に定義されます。

![FRCNN](../../../../../translated_images/f-rcnn.3cda6d9bb41888754037d2d9763e2298a96de5d9bc2a21db3147357aa5da9b1a.ja.png)

> 画像出典: [公式論文](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

このアプローチの主なアイデアは、ROIを予測するためにニューラルネットワークを使用することです。これを*領域提案ネットワーク* (Region Proposal Network) と呼びます。[論文](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../translated_images/faster-rcnn.8d46c099b87ef30ab2ea26dbc4bdd85b974a57ba8eb526f65dc4cd0a4711de30.ja.png)

> 画像出典: [公式論文](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: 領域ベースの完全畳み込みネットワーク

このアルゴリズムはFaster R-CNNよりもさらに高速です。主なアイデアは以下の通りです：

1. ResNet-101を使用して特徴を抽出する
1. 特徴を**位置感知スコアマップ**で処理する。クラス $C$ の各物体は $k\times k$ の領域に分割され、物体の部分を予測するように学習する
1. $k\times k$ の各領域の部分について、すべてのネットワークが物体クラスに投票し、最大票を得た物体クラスが選択される

![r-fcn image](../../../../../translated_images/r-fcn.13eb88158b99a3da50fa2787a6be5cb310d47f0e9655cc93a1090dc7aab338d1.ja.png)

> 画像出典: [公式論文](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLOはリアルタイムのワンパスアルゴリズムです。主なアイデアは以下の通りです：

 * 画像を $S\times S$ の領域に分割する
 * 各領域について、**CNN** が $n$ 個の可能な物体、*境界ボックス*の座標、*信頼度*=*確率* * IoU を予測する

 ![YOLO](../../../../../translated_images/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.ja.png)

> 画像出典: [公式論文](https://arxiv.org/abs/1506.02640)

### その他のアルゴリズム

* RetinaNet: [公式論文](https://arxiv.org/abs/1708.02002)
   - [PyTorch 実装 (Torchvision)](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Keras 実装](https://github.com/fizyr/keras-retinanet)
   - [RetinaNet を使用したオブジェクト検出](https://keras.io/examples/vision/retinanet/) (Keras Samples)
* SSD (Single Shot Detector): [公式論文](https://arxiv.org/abs/1512.02325)

## ✍️ 演習: オブジェクト検出

以下のノートブックで学習を続けてください：

[ObjectDetection.ipynb](../../../../../lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)

## 結論

このレッスンでは、オブジェクト検出を実現するさまざまな方法について駆け足で学びました！

## 🚀 チャレンジ

以下の記事やノートブックを読み、YOLOを試してみてください：

* [YOLOに関する良いブログ記事](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/)
 * [公式サイト](https://pjreddie.com/darknet/yolo/)
 * YOLO: [Keras 実装](https://github.com/experiencor/keras-yolo2), [ステップバイステップノートブック](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * YOLO v2: [Keras 実装](https://github.com/experiencor/keras-yolo2), [ステップバイステップノートブック](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [事後クイズ](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/211)

## 復習と自己学習

* [オブジェクト検出](https://tjmachinelearning.com/lectures/1718/obj/) by Nikhil Sardana
* [オブジェクト検出アルゴリズムの良い比較](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [オブジェクト検出のためのディープラーニングアルゴリズムのレビュー](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [基本的なオブジェクト検出アルゴリズムへのステップバイステップの導入](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [PythonでのFaster R-CNNの実装によるオブジェクト検出](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [課題: オブジェクト検出](lab/README.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された原文が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。