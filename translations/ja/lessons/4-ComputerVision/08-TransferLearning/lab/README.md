# 転移学習を用いたOxford Petsの分類

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)のラボ課題。

## 課題

ペットの保育園向けに、すべてのペットをカタログ化するアプリケーションを開発する必要があると想像してください。このアプリケーションの素晴らしい機能の1つは、写真から自動的に品種を判別することです。この課題では、転移学習を使用して、[Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/)ペットデータセットから実際のペット画像を分類します。

## データセット

使用するのは、35種類の犬と猫の品種を含むオリジナルの[Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/)ペットデータセットです。

データセットをダウンロードするには、以下のコードスニペットを使用してください：

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## ノートブックの開始

ラボを始めるには、[OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)を開いてください。

## 学びのポイント

転移学習と事前学習済みネットワークを使用することで、現実世界の画像分類問題を比較的簡単に解決できます。ただし、事前学習済みネットワークは、似た種類の画像に対してはうまく機能しますが、非常に異なる種類の画像（例：医療画像）を分類し始めると、結果が大幅に悪化する可能性があります。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当社は責任を負いません。