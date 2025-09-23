<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-24T21:05:49+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "ja"
}
-->
# 言語モデリング

Word2VecやGloVeのようなセマンティック埋め込みは、実際には**言語モデリング**への第一歩です。これは、言語の性質を何らかの形で*理解*（または*表現*）するモデルを作成することを意味します。

## [講義前のクイズ](https://ff-quizzes.netlify.app/en/ai/quiz/29)

言語モデリングの主なアイデアは、ラベル付けされていないデータセットを教師なしで学習させることです。これは、ラベル付けされていないテキストが膨大に存在する一方で、ラベル付けされたテキストの量はラベル付けに費やせる労力によって常に制限されるため、重要です。多くの場合、テキスト内の**欠損している単語を予測する**言語モデルを構築できます。これは、テキスト内のランダムな単語をマスクして学習サンプルとして使用するのが簡単だからです。

## 埋め込みの学習

前回の例では、事前に学習されたセマンティック埋め込みを使用しましたが、それらの埋め込みがどのように学習されるかを見るのも興味深いです。以下のようなアイデアがいくつかあります：

* **Nグラム**言語モデリング：N個の前のトークンを見て次のトークンを予測する（Nグラム）
* **連続Bag-of-Words**（CBoW）：トークン列$W_{-N}$, ..., $W_N$の中間トークン$W_0$を予測する
* **Skip-gram**：中間トークン$W_0$から、隣接するトークンの集合{$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$}を予測する

![単語をベクトルに変換するアルゴリズムの例](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.ja.png)

> 画像出典：[この論文](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ 例ノートブック: CBoWモデルの学習

以下のノートブックで学習を続けてください：

* [TensorFlowを使ったCBoW Word2Vecの学習](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [PyTorchを使ったCBoW Word2Vecの学習](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## 結論

前回のレッスンでは、単語埋め込みがまるで魔法のように機能することを学びました！今回の内容で、単語埋め込みの学習がそれほど複雑な作業ではないことが分かりました。必要に応じて、特定の分野のテキストに特化した単語埋め込みを自分で学習させることも可能です。

## [講義後のクイズ](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## 復習と自己学習

* [PyTorch公式の言語モデリングチュートリアル](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html)
* [TensorFlow公式のWord2Vecモデル学習チュートリアル](https://www.TensorFlow.org/tutorials/text/word2vec)
* **gensim**フレームワークを使用して、数行のコードで最も一般的な埋め込みを学習する方法は[こちらのドキュメント](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html)に記載されています。

## 🚀 [課題: Skip-Gramモデルを学習する](lab/README.md)

このラボでは、CBoWモデルのコードを変更してSkip-Gramモデルを学習させることに挑戦していただきます。[詳細はこちら](lab/README.md)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。元の言語で記載された文書が公式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。