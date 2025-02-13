# Skip-Gramモデルのトレーニング

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)からのラボ課題です。

## 課題

このラボでは、Skip-Gram技術を使用してWord2Vecモデルをトレーニングすることに挑戦します。$N$トークン幅のSkip-Gramウィンドウ内で隣接する単語を予測するための埋め込みを持つネットワークをトレーニングします。このレッスンの[コード](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)を使用し、少し修正しても構いません。

## データセット

任意の本を使用しても構いません。例えば、[Project Gutenberg](https://www.gutenberg.org/)では多くの無料テキストが見つかります。ここでは、ルイス・キャロルによる[Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt)への直接リンクを示します。また、以下のコードを使用してシェイクスピアの戯曲を取得することもできます。

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## 探索しよう！

時間があれば、さらに深く掘り下げてみてください。いくつかのことを探索してみましょう：

* 埋め込みサイズは結果にどのように影響しますか？
* 異なるテキストスタイルは結果にどのように影響しますか？
* 非常に異なるタイプの単語とその同義語をいくつか取り上げ、それらのベクトル表現を取得し、PCAを適用して次元を2に減らし、2D空間にプロットしてみてください。パターンが見えますか？

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることにご留意ください。原文の母国語の文書が権威ある情報源と見なされるべきです。重要な情報については、専門の人間翻訳を推奨します。この翻訳の使用によって生じた誤解や誤解釈については、当社は責任を負いません。