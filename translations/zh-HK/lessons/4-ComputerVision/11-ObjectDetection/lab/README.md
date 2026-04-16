# 使用 Hollywood Heads Dataset 進行頭部檢測

來自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的實驗課題。

## 任務

在監控攝像機的視頻流中計算人數是一項重要的任務，這可以幫助我們估算商店的訪客數量、餐廳的繁忙時段等。為了解決這個問題，我們需要能夠從不同角度檢測人類的頭部。為了訓練物件檢測模型來檢測人類頭部，我們可以使用 [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/)。

## 數據集

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) 包含 369,846 個人類頭部的標註，這些標註來自 224,740 張好萊塢電影的影格。數據集以 [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) 格式提供，每張圖片都有一個 XML 描述文件，其格式如下：

```xml
<annotation>
	<folder>HollywoodHeads</folder>
	<filename>mov_021_149390.jpeg</filename>
	<source>
		<database>HollywoodHeads 2015 Database</database>
		<annotation>HollywoodHeads 2015</annotation>
		<image>WILLOW</image>
	</source>
	<size>
		<width>608</width>
		<height>320</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>head</name>
		<bndbox>
			<xmin>201</xmin>
			<ymin>1</ymin>
			<xmax>480</xmax>
			<ymax>263</ymax>
		</bndbox>
		<difficult>0</difficult>
	</object>
	<object>
		<name>head</name>
		<bndbox>
			<xmin>3</xmin>
			<ymin>4</ymin>
			<xmax>241</xmax>
			<ymax>285</ymax>
		</bndbox>
		<difficult>0</difficult>
	</object>
</annotation>
```

在這個數據集中，只有一類物件 `head`，每個頭部都提供了邊界框的座標。你可以使用 Python 的庫來解析 XML，或者使用 [這個庫](https://pypi.org/project/pascal-voc/) 直接處理 PASCAL VOC 格式。

## 訓練物件檢測模型

你可以使用以下方法之一來訓練物件檢測模型：

* 使用 [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) 及其 Python API，在雲端以程式化方式訓練模型。Custom Vision 無法使用超過幾百張圖片來訓練模型，因此你可能需要限制數據集的大小。
* 使用 [Keras 教程](https://keras.io/examples/vision/retinanet/) 中的範例來訓練 RetunaNet 模型。
* 使用 [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) 中的內建模組進行訓練。

## 重點

物件檢測是業界經常需要的一項任務。雖然有一些服務可以用來執行物件檢測（例如 [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)），但了解物件檢測的工作原理並能夠訓練自己的模型是非常重要的。

**免責聲明**：  
本文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始語言的文件應被視為具權威性的來源。對於重要資訊，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。