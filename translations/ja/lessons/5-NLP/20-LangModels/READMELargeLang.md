# 事前学習済み大規模言語モデル

これまでのすべてのタスクでは、ラベル付きデータセットを使用して特定のタスクを実行するためにニューラルネットワークを訓練していました。BERTのような大規模トランスフォーマーモデルでは、自己教師あり方式で言語モデルを構築し、その後、特定のドメインに特化したトレーニングを行って特定の下流タスクに特化させます。しかし、大規模言語モデルは、ANYドメイン特化型のトレーニングなしで多くのタスクを解決できることが示されています。そのようなモデルのファミリーは**GPT**（Generative Pre-Trained Transformer）と呼ばれています。

## [講義前のクイズ](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## テキスト生成とパープレキシティ

ニューラルネットワークが下流のトレーニングなしで一般的なタスクを実行できるというアイデアは、[Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)という論文で示されています。主なアイデアは、他の多くのタスクが**テキスト生成**を使用してモデル化できるということです。なぜなら、テキストを理解することは本質的にそれを生成できることを意味するからです。モデルは人間の知識を包含する膨大なテキストで訓練されているため、さまざまな主題に関する知識も得ることができます。

> テキストを理解し生成できることは、私たちの周りの世界について何かを知っていることも含意しています。人々も大きな程度で読むことによって学び、GPTネットワークはこの点で類似しています。

テキスト生成ネットワークは、次の単語の確率 $$P(w_N)$$ を予測することによって機能します。しかし、次の単語の無条件確率は、この単語がテキストコーパス内に存在する頻度に等しいです。GPTは、前の単語を考慮した上で次の単語の**条件付き確率**を提供することができます: $$P(w_N | w_{n-1}, ..., w_0)$$

> 確率についてもっと知りたい場合は、私たちの[Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)を読んでみてください。

言語生成モデルの質は**パープレキシティ**を使用して定義できます。これは、タスク特化型データセットなしでモデルの質を測定するための内在的な指標です。これは*文の確率*の概念に基づいており、モデルは実際に存在する可能性の高い文に高い確率を割り当て（つまり、モデルはそれに**困惑**しない）、あまり意味を成さない文には低い確率を割り当てます（例: *Can it does what?*）。実際のテキストコーパスからモデルに文を与えたとき、高い確率と低い**パープレキシティ**を持つことを期待します。数学的には、テストセットの正規化された逆確率として定義されます:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**[Hugging FaceのGPT駆動テキストエディタ](https://transformer.huggingface.co/doc/gpt2-large)を使用してテキスト生成を試してみてください**。このエディタでは、テキストの入力を開始し、**[TAB]**を押すといくつかの補完オプションが表示されます。オプションが短すぎる場合や満足できない場合は、再度[TAB]を押すと、より長いテキストを含む追加のオプションが得られます。

## GPTはファミリーです

GPTは単一のモデルではなく、[OpenAI](https://openai.com)によって開発され、訓練されたモデルのコレクションです。

GPTモデルには以下があります:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| 最大15億パラメータを持つ言語モデル。 | 最大1750億パラメータを持つ言語モデル。 | 100Tパラメータを持ち、画像とテキストの両方の入力を受け付け、テキストを出力します。 |

GPT-3およびGPT-4モデルは、[Microsoft Azureの認知サービス](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste)として、また[OpenAI API](https://openai.com/api/)として利用可能です。

## プロンプトエンジニアリング

GPTは膨大なデータ量で言語とコードを理解するように訓練されているため、入力（プロンプト）に対して出力を提供します。プロンプトは、モデルに対して次に完了するタスクに関する指示を提供するGPTの入力またはクエリです。望ましい結果を引き出すためには、適切な言葉、形式、フレーズ、さらには記号を選択することが含まれる最も効果的なプロンプトが必要です。このアプローチは[プロンプトエンジニアリング](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)と呼ばれています。

[このドキュメント](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum)では、プロンプトエンジニアリングに関する詳細情報を提供しています。

## ✍️ 例ノートブック: [OpenAI-GPTで遊ぶ](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

次のノートブックで学習を続けてください:

* [OpenAI-GPTとHugging Face Transformersを使用したテキスト生成](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## 結論

新しい一般的な事前学習済み言語モデルは、言語構造をモデル化するだけでなく、大量の自然言語も含んでいます。したがって、これらはゼロショットまたは少数ショットの設定でいくつかのNLPタスクを効果的に解決するために使用できます。

## [講義後のクイズ](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されました。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることにご注意ください。原文はその言語での権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解釈について、当社は一切の責任を負いません。