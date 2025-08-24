<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-24T21:51:33+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "ja"
}
-->
# 事前学習済みの大規模言語モデル

これまでのタスクでは、ラベル付きデータセットを使用して特定のタスクを実行するニューラルネットワークを訓練してきました。BERTのような大規模なトランスフォーマーモデルでは、自己教師あり学習を用いて言語モデルを構築し、その後、特定の下流タスクに特化したドメイン固有の訓練を行います。しかし、大規模言語モデルはドメイン固有の訓練を一切行わなくても多くのタスクを解決できることが示されています。このようなモデル群は**GPT**（Generative Pre-Trained Transformer）と呼ばれます。

## [講義前のクイズ](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## テキスト生成とパープレキシティ

下流訓練なしで一般的なタスクを実行できるニューラルネットワークのアイデアは、[Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)という論文で提示されています。この論文の主なアイデアは、多くのタスクが**テキスト生成**を用いてモデル化できるということです。テキストを理解することは、基本的にそれを生成できる能力を意味します。モデルが膨大な量のテキストで訓練されているため、人間の知識を網羅し、幅広い分野についても知識を持つようになります。

> テキストを理解し生成できることは、周囲の世界について何かを知っていることも意味します。人々は読書を通じて多くのことを学びますが、GPTネットワークもこの点で似ています。

テキスト生成ネットワークは次の単語の確率 $$P(w_N)$$ を予測することで動作します。ただし、次の単語の無条件確率はテキストコーパス内でのその単語の頻度に等しくなります。GPTは、前の単語を条件とした次の単語の**条件付き確率**を提供することができます: $$P(w_N | w_{n-1}, ..., w_0)$$

> 確率についての詳細は、[Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)をご覧ください。

言語生成モデルの品質は**パープレキシティ**を使用して定義できます。これは、タスク固有のデータセットを使用せずにモデルの品質を測定するための内在的な指標です。*文の確率*という概念に基づいており、モデルは現実的である可能性が高い文に高い確率を割り当て（つまり、モデルがその文に対して**困惑**していない）、意味が通じにくい文（例: *Can it does what?*）には低い確率を割り当てます。モデルに実際のテキストコーパスからの文を与えると、それらが高い確率を持ち、低い**パープレキシティ**を持つことが期待されます。数学的には、テストセットの正規化された逆確率として定義されます:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**[Hugging FaceのGPT搭載テキストエディタ](https://transformer.huggingface.co/doc/gpt2-large)**を使用してテキスト生成を試すことができます。このエディタでは、テキストを書き始めて**[TAB]**キーを押すと、いくつかの補完オプションが表示されます。オプションが短すぎたり満足できない場合は、再度[TAB]キーを押すと、より長いテキストを含む追加のオプションが表示されます。

## GPTはファミリー

GPTは単一のモデルではなく、[OpenAI](https://openai.com)によって開発・訓練されたモデルのコレクションです。

GPTモデルには以下があります:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|最大15億のパラメータを持つ言語モデル | 最大1750億のパラメータを持つ言語モデル | 100兆のパラメータを持ち、画像とテキストの入力を受け取り、テキストを出力するモデル |

GPT-3およびGPT-4モデルは、[Microsoft Azureの認知サービス](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste)として、または[OpenAI API](https://openai.com/api/)として利用可能です。

## プロンプトエンジニアリング

GPTは膨大なデータで訓練されており、言語やコードを理解する能力を持っています。そのため、入力（プロンプト）に応じて出力を提供します。プロンプトとは、モデルに次に完了するタスクについて指示を与えるGPTへの入力やクエリのことです。望ましい結果を得るためには、最も効果的なプロンプトが必要であり、それには適切な単語、形式、フレーズ、さらには記号を選択することが含まれます。このアプローチは[プロンプトエンジニアリング](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)と呼ばれます。

[このドキュメント](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum)では、プロンプトエンジニアリングに関する詳細情報を提供しています。

## ✍️ サンプルノートブック: [OpenAI-GPTで遊ぶ](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

以下のノートブックで学習を続けてください:

* [OpenAI-GPTとHugging Face Transformersを使用したテキスト生成](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## 結論

新しい一般的な事前学習済み言語モデルは、言語構造をモデル化するだけでなく、膨大な自然言語を含んでいます。そのため、ゼロショットまたは少数ショット設定でいくつかのNLPタスクを効果的に解決することができます。

## [講義後のクイズ](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。元の言語で記載された文書が公式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。