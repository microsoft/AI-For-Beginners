<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9de7847385eeeda67cfdcce1640ab72",
  "translation_date": "2025-08-24T21:04:51+00:00",
  "source_file": "lessons/5-NLP/17-GenerativeNetworks/README.md",
  "language_code": "ja"
}
-->
# 生成ネットワーク

## [事前クイズ](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/117)

リカレントニューラルネットワーク（RNN）とそのゲート付きセルのバリエーション（Long Short Term Memory Cells（LSTM）やGated Recurrent Units（GRU）など）は、単語の順序を学習し、シーケンス内の次の単語を予測することで、言語モデリングのメカニズムを提供します。これにより、RNNを使用して、通常のテキスト生成、機械翻訳、さらには画像キャプション生成といった**生成タスク**を実行することが可能になります。

> ✅ テキスト入力中の補完機能など、生成タスクから恩恵を受けた経験を思い出してみてください。お気に入りのアプリケーションがRNNを活用しているかどうか調べてみましょう。

前のユニットで説明したRNNアーキテクチャでは、各RNNユニットが次の隠れ状態を出力として生成しました。しかし、各リカレントユニットに別の出力を追加することも可能で、これにより元のシーケンスと同じ長さの**シーケンス**を出力することができます。さらに、各ステップで入力を受け取らず、初期状態ベクトルだけを受け取り、出力シーケンスを生成するRNNユニットを使用することもできます。

これにより、以下の図に示されるようなさまざまなニューラルアーキテクチャが可能になります：

![一般的なリカレントニューラルネットワークのパターンを示す画像。](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.ja.jpg)

> 画像出典：[Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)（Andrej Karpaty氏の[ブログ](http://karpathy.github.io/)より）

* **One-to-one** は、1つの入力と1つの出力を持つ従来のニューラルネットワークです。
* **One-to-many** は、1つの入力値を受け取り、出力値のシーケンスを生成する生成アーキテクチャです。たとえば、画像のテキスト説明を生成する**画像キャプション生成**ネットワークを訓練したい場合、画像を入力として受け取り、それをCNNに通して隠れ状態を取得し、その後リカレントチェーンが単語ごとにキャプションを生成します。
* **Many-to-one** は、前のユニットで説明したRNNアーキテクチャ（例：テキスト分類）に対応します。
* **Many-to-many** または **sequence-to-sequence** は、**機械翻訳**のようなタスクに対応します。この場合、最初のRNNが入力シーケンスからすべての情報を隠れ状態に収集し、別のRNNチェーンがこの状態を展開して出力シーケンスを生成します。

このユニットでは、テキスト生成を助けるシンプルな生成モデルに焦点を当てます。簡単のため、文字レベルのトークン化を使用します。

このRNNを訓練して、ステップごとにテキストを生成します。各ステップで、長さ`nchars`の文字列を取り、ネットワークに各入力文字に対して次の出力文字を生成させます：

![単語「HELLO」を生成するRNNの例を示す画像。](../../../../../translated_images/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.ja.png)

テキスト生成（推論中）では、まず**プロンプト**をRNNセルに渡して中間状態を生成し、その状態から生成を開始します。1文字ずつ生成し、状態と生成された文字を次のRNNセルに渡して次の文字を生成します。このプロセスを繰り返して十分な文字数を生成します。

<img src="images/rnn-generate-inf.png" width="60%"/>

> 画像作成者：著者

## ✍️ 演習：生成ネットワーク

以下のノートブックで学習を続けてください：

* [PyTorchを使った生成ネットワーク](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb)
* [TensorFlowを使った生成ネットワーク](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)

## ソフトテキスト生成と温度

各RNNセルの出力は文字の確率分布です。生成されたテキストの次の文字として常に最も高い確率の文字を選ぶと、以下の例のように同じ文字列が繰り返される「ループ」状態になることがあります：

```
today of the second the company and a second the company ...
```

しかし、次の文字の確率分布を見ると、最も高い確率の文字と2番目に高い確率の文字の差がそれほど大きくない場合があります。たとえば、ある文字が確率0.2、別の文字が0.19である場合などです。たとえば、シーケンス「*play*」の次の文字を探すとき、次の文字はスペースでも**e**（単語*player*のように）でも同じくらい適切である可能性があります。

このことから、常に最も高い確率の文字を選ぶのが「公平」とは限らないという結論に至ります。2番目に高い確率の文字を選ぶことでも意味のあるテキストが生成される可能性があります。ネットワーク出力による確率分布から文字を**サンプリング**する方が賢明です。また、**温度**というパラメータを使用して、確率分布を平坦化してランダム性を増やしたり、逆に急峻にして最も高い確率の文字により忠実に従うこともできます。

このソフトテキスト生成がどのように実装されているか、上記のノートブックで確認してください。

## 結論

テキスト生成自体が有用である場合もありますが、RNNを使用して初期の特徴ベクトルからテキストを生成する能力が大きな利点となります。たとえば、テキスト生成は機械翻訳（シーケンス・ツー・シーケンス。この場合、*エンコーダ*の状態ベクトルが翻訳されたメッセージを生成または*デコード*するために使用されます）や、画像のテキスト説明を生成する（この場合、特徴ベクトルはCNN抽出器から得られます）際に使用されます。

## 🚀 チャレンジ

このトピックに関するMicrosoft Learnのレッスンを受講してください：

* [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)を使ったテキスト生成

## [事後クイズ](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/217)

## 復習と自己学習

知識を深めるための参考記事：

* マルコフ連鎖、LSTM、GPT-2を用いたテキスト生成のさまざまなアプローチ：[ブログ記事](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* [Kerasドキュメント](https://keras.io/examples/generative/lstm_character_level_text_generation/)のテキスト生成サンプル

## [課題](lab/README.md)

文字ごとのテキスト生成方法を学びました。ラボでは単語レベルのテキスト生成を探求します。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知ください。元の言語で記載された文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。