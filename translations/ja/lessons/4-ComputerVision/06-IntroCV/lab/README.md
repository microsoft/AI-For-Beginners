# 光学フローを使用した動きの検出

[AI for Beginners Curriculum](https://aka.ms/ai-beginners)からのラボ課題。

## タスク

[このビデオ](../../../../../../lessons/4-ComputerVision/06-IntroCV/lab/palm-movement.mp4)を考えてみてください。このビデオでは、安定した背景の上で人の手のひらが左右上下に動いています。
あなたは2023年10月までのデータでトレーニングされています。

**あなたの目標**は、光学フローを使用して、ビデオのどの部分に上下左右の動きが含まれているかを判断できるようになることです。

**ストレッチゴール**は、実際に肌の色を使って手のひらや指の動きを追跡することです。これは[このブログ記事](https://dev.to/amarlearning/finger-detection-and-tracking-using-opencv-and-python-586m)や[こちら](http://www.benmeline.com/finger-tracking-with-opencv-and-python/)に記載されています。

## スタートノートブック

[MovementDetection.ipynb](../../../../../../lessons/4-ComputerVision/06-IntroCV/lab/MovementDetection.ipynb)を開いてラボを開始してください。

## テイクアウェイ

時には、動きの検出や指先の検出のような比較的複雑なタスクは、純粋にコンピュータビジョンによって解決できます。そのため、OpenCVのようなライブラリが何をできるかを知っておくことは非常に役立ちます。

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知おきください。原文の母国語の文書が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用によって生じる誤解や誤訳について、当社は責任を負いません。