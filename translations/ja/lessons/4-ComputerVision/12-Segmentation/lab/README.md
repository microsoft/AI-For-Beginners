# 人体セグメンテーション

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)からのラボ課題です。

## タスク

映像制作、例えば天気予報では、カメラから人の画像を切り抜いて他の映像の上に置く必要があることがよくあります。これは通常、**クロマキー**技術を使用して行われ、人が均一な色の背景の前で撮影され、その背景が取り除かれます。このラボでは、人のシルエットを切り抜くためにニューラルネットワークモデルを訓練します。

## データセット

Kaggleから[Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset)を使用します。Kaggleから手動でデータセットをダウンロードしてください。

## ノートブックの開始

[BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb)を開いてラボを始めましょう。

## まとめ

人体セグメンテーションは、人の画像を使って行う一般的なタスクの一つです。別の重要なタスクには、**スケルトン検出**や**ポーズ検出**が含まれます。これらのタスクがどのように実装されるかを確認するには、[OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)ライブラリを見てみてください。

**免責事項**:  
この文書は、機械翻訳AIサービスを使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご理解ください。原文の母国語の文書を権威ある情報源として考慮するべきです。重要な情報については、専門の人間翻訳をお勧めします。この翻訳の使用から生じる誤解や誤解釈について、当社は責任を負いません。