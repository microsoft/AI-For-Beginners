# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)からのラボ課題。

## タスク

このラボでは、医療用語のための名前付きエンティティ認識モデルをトレーニングする必要があります。

## データセット

NERモデルをトレーニングするためには、医療エンティティが適切にラベル付けされたデータセットが必要です。[BC5CDRデータセット](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/)には、1500以上の論文からのラベル付きの病気や化学物質のエンティティが含まれています。ウェブサイトに登録した後にデータセットをダウンロードできます。

BC5CDRデータセットは次のようになります：

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

このデータセットでは、最初の2行に論文のタイトルと要約があり、その後に個々のエンティティが続き、タイトル+要約ブロック内の開始位置と終了位置が示されています。エンティティのタイプに加えて、このエンティティが特定の医療オントロジー内で持つオントロジーIDも得られます。

このデータをBIOエンコーディングに変換するために、いくつかのPythonコードを書く必要があります。

## ネットワーク

NERの最初の試みは、レッスン中に見た例のようにLSTMネットワークを使用して行うことができます。しかし、NLPタスクでは、[トランスフォーマーアーキテクチャ](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))、特に[ BERT言語モデル](https://en.wikipedia.org/wiki/BERT_(language_model))がはるかに良い結果を示します。事前にトレーニングされたBERTモデルは、言語の一般的な構造を理解し、比較的小さなデータセットと計算コストで特定のタスクに微調整することができます。

私たちはNERを医療シナリオに適用する予定なので、医療テキストでトレーニングされたBERTモデルを使用するのが理にかなっています。マイクロソフトリサーチは、[PubMedBERT][PubMedBERT]という事前トレーニングされたモデルをリリースしました（[出版物][PubMedBERT-Pub]）、これは[PubMed](https://pubmed.ncbi.nlm.nih.gov/)リポジトリのテキストを使用して微調整されました。

トランスフォーマーモデルをトレーニングするための*de facto*標準は、[Hugging Face Transformers](https://huggingface.co/)ライブラリです。このライブラリには、PubMedBERTを含むコミュニティが管理する事前トレーニングされたモデルのリポジトリも含まれています。このモデルをロードして使用するには、数行のコードが必要です：

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

これにより、入力テキストをトークンに分割できる`model` itself, built for token classification task using `classes` number of classes, as well as `tokenizer`オブジェクトが得られます。データセットをBIO形式に変換する際には、PubMedBERTのトークン化を考慮する必要があります。[このPythonコード](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88)を参考にすることができます。

## まとめ

このタスクは、自然言語テキストの大規模なボリュームに関する洞察を得たい場合に実際に行う可能性が高いタスクに非常に近いです。私たちの場合、トレーニングしたモデルを[COVID関連論文のデータセット](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)に適用し、どのような洞察が得られるかを確認できます。[このブログ記事](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/)や[この論文](https://www.mdpi.com/2504-2289/6/1/4)は、NERを使用してこの論文コーパスで行うことができる研究について説明しています。

**免責事項**:  
この文書は、機械翻訳AIサービスを使用して翻訳されました。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご理解ください。元の文書は、その母国語での権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解釈について、当社は一切の責任を負いません。