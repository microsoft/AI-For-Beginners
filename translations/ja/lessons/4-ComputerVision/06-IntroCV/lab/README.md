# 光の流れを使った動きの検出

[AI for Beginners Curriculum](https://aka.ms/ai-beginners)の課題。

## 課題

[この動画](../../../../../../lessons/4-ComputerVision/06-IntroCV/lab/palm-movement.mp4)では、安定した背景の上で人の手のひらが左/右/上/下に動いています。

**目標**は、光の流れを使って、動画のどの部分が上/下/左/右の動きを含んでいるかを判定することです。

**追加目標**として、[このブログ記事](https://dev.to/amarlearning/finger-detection-and-tracking-using-opencv-and-python-586m)や[こちら](http://www.benmeline.com/finger-tracking-with-opencv-and-python/)で説明されているように、肌の色を利用して手のひらや指の動きを実際に追跡することが挙げられます。

## スタートノートブック

[MovementDetection.ipynb](../../../../../../lessons/4-ComputerVision/06-IntroCV/lab/MovementDetection.ipynb)を開いて課題を始めてください。

## 学び

動きの検出や指先の検出といった比較的複雑なタスクが、純粋にコンピュータビジョンだけで解決できる場合があります。そのため、OpenCVのようなライブラリが何をできるのかを知っておくことは非常に役立ちます。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。