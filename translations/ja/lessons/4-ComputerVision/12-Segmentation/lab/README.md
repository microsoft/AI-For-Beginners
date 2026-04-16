# 人体セグメンテーション

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) のラボ課題。

## 課題

ビデオ制作、例えば天気予報では、カメラで撮影した人の画像を切り抜き、別の映像の上に配置する必要があることがあります。これには通常、**クロマキー**技術が使用されます。人が均一な色の背景の前で撮影され、その背景が取り除かれる方法です。このラボでは、人のシルエットを切り抜くためのニューラルネットワークモデルを訓練します。

## データセット

Kaggleの[Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset)を使用します。データセットはKaggleから手動でダウンロードしてください。

## スタートノートブック

[BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb) を開いてラボを開始してください。

## 学び

人体セグメンテーションは、人の画像を使ってできる一般的なタスクの一つに過ぎません。他にも重要なタスクとして、**骨格検出**や**ポーズ検出**があります。[OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) ライブラリを調べて、それらのタスクがどのように実装されるかを確認してください。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。元の言語で記載された文書が公式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。