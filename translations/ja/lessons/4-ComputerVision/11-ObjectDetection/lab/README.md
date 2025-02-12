# ハリウッドヘッズデータセットを用いた頭部検出

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)からのラボ課題です。

## 課題

監視カメラの映像ストリーム上の人の数をカウントすることは、店舗の訪問者数やレストランの混雑時間を推定するために重要なタスクです。この課題を解決するためには、異なる角度から人の頭を検出できる必要があります。人の頭を検出するためのオブジェクト検出モデルをトレーニングするには、[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/)を使用できます。

## データセット

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip)には、ハリウッド映画の224,740フレームに注釈が付けられた369,846個の人の頭が含まれています。このデータセットは[https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC)フォーマットで提供されており、各画像には次のようなXML記述ファイルがあります。

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

このデータセットには、オブジェクトのクラスは`head`のみで、各頭部に対してバウンディングボックスの座標が得られます。Pythonライブラリを使用してXMLを解析するか、[このライブラリ](https://pypi.org/project/pascal-voc/)を使用してPASCAL VOCフォーマットを直接扱うことができます。

## オブジェクト検出のトレーニング

以下のいずれかの方法を使用してオブジェクト検出モデルをトレーニングできます。

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)とそのPython APIを使用して、クラウド上でプログラム的にモデルをトレーニングします。カスタムビジョンは数百枚の画像以上を使用してモデルをトレーニングすることができないため、データセットを制限する必要があるかもしれません。
* [Kerasチュートリアル](https://keras.io/examples/vision/retinanet/)の例を使用してRetinaNetモデルをトレーニングします。
* [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)の組み込みモジュールを使用します。

## まとめ

オブジェクト検出は、産業界で頻繁に要求されるタスクです。オブジェクト検出を実行するために使用できるサービス（例えば[Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)）はありますが、オブジェクト検出がどのように機能するかを理解し、自分のモデルをトレーニングできることが重要です。

**免責事項**:  
この文書は、機械翻訳サービスを使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご理解ください。元の文書は、その原文が権威ある情報源と見なされるべきです。重要な情報については、専門の人間翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解釈については、当社は責任を負いません。