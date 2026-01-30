# ハリウッドヘッズデータセットを使用した頭部検出

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) のラボ課題。

## 課題

監視カメラの映像で人の数を数えることは、店舗の訪問者数やレストランの混雑時間を推定するために重要なタスクです。この課題を解決するには、さまざまな角度から人間の頭部を検出できる必要があります。人間の頭部を検出する物体検出モデルをトレーニングするために、[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/) を使用することができます。

## データセット

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) には、ハリウッド映画の224,740フレームにわたる369,846の人間の頭部がアノテーションされています。このデータセットは [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) フォーマットで提供されており、各画像には以下のようなXML記述ファイルが付属しています：

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

このデータセットには `head` という1つのオブジェクトクラスしかなく、各頭部についてバウンディングボックスの座標が提供されています。XMLはPythonライブラリを使用して解析することができますし、[このライブラリ](https://pypi.org/project/pascal-voc/) を使用してPASCAL VOCフォーマットを直接扱うことも可能です。

## 物体検出のトレーニング

物体検出モデルをトレーニングするには、以下の方法のいずれかを使用できます：

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) とそのPython APIを使用して、クラウド上でプログラム的にモデルをトレーニングする。Custom Visionでは数百枚以上の画像を使用してモデルをトレーニングすることはできないため、データセットを制限する必要があるかもしれません。
* [Kerasのチュートリアル](https://keras.io/examples/vision/retinanet/) の例を使用してRetinaNetモデルをトレーニングする。
* [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) のtorchvisionに組み込まれたモジュールを使用する。

## 学び

物体検出は業界で頻繁に必要とされるタスクです。[Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) のようなサービスを使用して物体検出を行うこともできますが、物体検出がどのように機能するかを理解し、自分でモデルをトレーニングできることが重要です。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された原文が公式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。