# NER

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) のラボ課題。

## 課題

このラボでは、医療用語の固有表現認識（NER）モデルをトレーニングする必要があります。

## データセット

NERモデルをトレーニングするには、医療エンティティが適切にラベル付けされたデータセットが必要です。[BC5CDRデータセット](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) には、1500以上の論文から抽出された疾患および化学物質のエンティティがラベル付けされています。このデータセットは、ウェブサイトで登録後にダウンロードできます。

BC5CDRデータセットは以下のような形式です：

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

このデータセットでは、最初の2行に論文のタイトルと要約があり、その後に個々のエンティティが続きます。エンティティには、タイトル＋要約ブロック内での開始位置と終了位置が記載されています。さらに、エンティティの種類に加えて、特定の医療オントロジー内でのオントロジーIDも取得できます。

このデータをBIOエンコーディングに変換するためのPythonコードを書く必要があります。

## ネットワーク

NERの最初の試みとしては、レッスン中に見た例のようにLSTMネットワークを使用することができます。しかし、NLPタスクでは、[トランスフォーマーアーキテクチャ](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))、特に[BERT言語モデル](https://en.wikipedia.org/wiki/BERT_(language_model))がはるかに良い結果を示します。事前トレーニングされたBERTモデルは言語の一般的な構造を理解しており、比較的小さなデータセットと計算コストで特定のタスクに微調整することができます。

医療シナリオにNERを適用する予定であるため、医療テキストでトレーニングされたBERTモデルを使用するのが理にかなっています。Microsoft Researchは、[PubMed](https://pubmed.ncbi.nlm.nih.gov/)リポジトリのテキストを使用して微調整された[PubMedBERT][PubMedBERT] ([publication][PubMedBERT-Pub]) という事前トレーニング済みモデルを公開しています。

トランスフォーマーモデルをトレーニングするための事実上の標準は、[Hugging Face Transformers](https://huggingface.co/) ライブラリです。このライブラリには、PubMedBERTを含むコミュニティが管理する事前トレーニング済みモデルのリポジトリも含まれています。このモデルをロードして使用するには、ほんの数行のコードが必要です：

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

これにより、`classes`の数に基づいてトークン分類タスク用に構築された`model`本体と、入力テキストをトークンに分割できる`tokenizer`オブジェクトが得られます。データセットをBIO形式に変換し、PubMedBERTのトークン化を考慮する必要があります。[このPythonコード](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88)を参考にすることができます。

## 学び

この課題は、大量の自然言語テキストから洞察を得たい場合に実際に直面する可能性が高いタスクに非常に近いものです。今回の場合、トレーニングしたモデルを[COVID関連論文のデータセット](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)に適用し、どのような洞察が得られるかを確認することができます。[このブログ記事](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/)や[この論文](https://www.mdpi.com/2504-2289/6/1/4)では、NERを使用してこの論文コーパスで行える研究について説明しています。

**免責事項**:  
この文書は、AI翻訳サービス [Co-op Translator](https://github.com/Azure/co-op-translator) を使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された原文が公式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や誤認について、当方は一切の責任を負いません。