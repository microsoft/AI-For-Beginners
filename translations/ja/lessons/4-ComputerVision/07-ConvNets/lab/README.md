<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-24T21:10:44+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "ja"
}
-->
# ペットの顔の分類

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) のラボ課題。

## 課題

ペットの保育施設向けに、すべてのペットをカタログ化するアプリケーションを開発する必要があると想像してください。このようなアプリケーションの素晴らしい機能の1つは、写真から自動的に品種を特定することです。これはニューラルネットワークを使用することで成功裏に実現できます。

**Pet Faces** データセットを使用して、猫と犬のさまざまな品種を分類する畳み込みニューラルネットワークをトレーニングする必要があります。

## データセット

使用するのは、[Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) ペットデータセットから派生した **Pet Faces** データセットです。このデータセットには、35種類の犬と猫の品種が含まれています。

![扱うデータセット](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.ja.png)

データセットをダウンロードするには、以下のコードスニペットを使用してください：

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## ノートブックの開始

ラボを始めるには、[PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb) を開いてください。

## 学びのポイント

画像分類という比較的複雑な問題をゼロから解決しましたね！クラスの数がかなり多かったにもかかわらず、合理的な精度を達成できました。また、top-k 精度を測定することも理にかなっています。なぜなら、人間でも明確に区別がつかないクラスを混同するのは簡単だからです。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された文書を正式な情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。