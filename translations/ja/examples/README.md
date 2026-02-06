# 初心者向けAI例

ようこそ！このディレクトリには、AIや機械学習を始めるためのシンプルで独立した例が含まれています。各例は初心者向けに設計されており、詳細なコメントやステップバイステップの説明が付いています。

## 📚 例の概要

| 例 | 説明 | 難易度 | 前提条件 |
|----|------|--------|----------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | 初めてのAIプログラム - シンプルなパターン認識 | ⭐ 初心者 | Pythonの基本 |
| [Simple Neural Network](../../../examples/02-simple-neural-network.py) | ニューラルネットワークをゼロから構築 | ⭐⭐ 初心者+ | Python、基礎数学 |
| [Image Classifier](./03-image-classifier.ipynb) | 事前学習済みモデルで画像を分類 | ⭐⭐ 初心者+ | Python、numpy |
| [Text Sentiment](../../../examples/04-text-sentiment.py) | テキストの感情分析（ポジティブ/ネガティブ） | ⭐⭐ 初心者+ | Python |

## 🚀 始め方

### 前提条件

Pythonがインストールされていることを確認してください（推奨バージョンは3.8以上）。必要なパッケージをインストールします：

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

または、メインカリキュラムのconda環境を使用してください：

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### 例の実行方法

**Pythonスクリプト（.pyファイル）の場合：**
```bash
python 01-hello-ai-world.py
```

**Jupyterノートブック（.ipynbファイル）の場合：**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 学習パス

例を順番に進めることをお勧めします：

1. **「Hello AI World」から始める** - パターン認識の基本を学ぶ
2. **シンプルなニューラルネットワークを構築する** - ニューラルネットワークの仕組みを理解する
3. **画像分類器を試す** - 実際の画像でAIを体験する
4. **テキスト感情分析を行う** - 自然言語処理を探求する

## 💡 初心者へのヒント

- **コードコメントをよく読む** - 各行が何をしているか説明されています
- **試してみる！** - 値を変更して結果を確認してみましょう
- **すべてを理解しようとしない** - 学習には時間がかかります
- **質問する** - [Discussion board](https://github.com/microsoft/AI-For-Beginners/discussions)を活用してください

## 🔗 次のステップ

これらの例を完了したら、完全なカリキュラムを探求してください：
- [AIの導入](../lessons/1-Intro/README.md)
- [ニューラルネットワーク](../lessons/3-NeuralNetworks/README.md)
- [コンピュータビジョン](../lessons/4-ComputerVision/README.md)
- [自然言語処理](../lessons/5-NLP/README.md)

## 🤝 コントリビューション

これらの例が役に立ったと感じたら、改善にご協力ください：
- 問題を報告したり改善案を提案する
- 初心者向けの例を追加する
- ドキュメントやコメントを改善する

---

*覚えておいてください：すべての専門家はかつて初心者でした。学習を楽しんでください！ 🎓*

---

**免責事項**:  
この文書は、AI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文（元の言語で記載された文書）を公式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の利用に起因する誤解や誤認について、当方は一切の責任を負いかねます。