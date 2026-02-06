# スキップグラムモデルのトレーニング

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) のラボ課題。

## 課題

このラボでは、スキップグラム手法を使用してWord2Vecモデルをトレーニングすることに挑戦します。埋め込みを使用して、$N$トークン幅のスキップグラムウィンドウ内の隣接する単語を予測するネットワークをトレーニングしてください。[このレッスンのコード](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)を使用し、少し修正することができます。

## データセット

どんな本でも使用可能です。[Project Gutenberg](https://www.gutenberg.org/) には多くの無料テキストがあります。例えば、ルイス・キャロルの [不思議の国のアリス](https://www.gutenberg.org/files/11/11-0.txt) への直接リンクがあります。または、以下のコードを使用してシェイクスピアの戯曲を取得することもできます。

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## 探求してみよう！

時間があり、さらに深く学びたい場合は、以下のことを試してみてください：

* 埋め込みサイズが結果にどのように影響するか？
* 異なる文体が結果にどのように影響するか？
* 非常に異なる種類の単語とその同義語をいくつか選び、それらのベクトル表現を取得し、PCAを適用して次元を2に削減し、2D空間にプロットしてみてください。何かパターンが見えますか？

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。