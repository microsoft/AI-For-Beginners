# 命名实体识别 (NER)

来自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的实验任务。

## 任务

在本实验中，你需要训练一个用于医学术语的命名实体识别模型。

## 数据集

为了训练 NER 模型，我们需要一个标注良好的包含医学实体的数据集。[BC5CDR 数据集](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) 包含了从 1500 多篇论文中提取的疾病和化学物质实体。你可以在其网站注册后下载该数据集。

BC5CDR 数据集的格式如下：

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

在这个数据集中，第一行和第二行分别是论文标题和摘要，接下来是各个实体的信息，包括它们在标题+摘要块中的起始和结束位置。除了实体类型外，你还可以获得该实体在某些医学本体中的本体 ID。

你需要编写一些 Python 代码，将这些数据转换为 BIO 编码格式。

## 网络

第一次尝试 NER 时，可以使用 LSTM 网络，就像你在课程中看到的示例一样。然而，在 NLP 任务中，[Transformer 架构](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))，特别是 [BERT 语言模型](https://en.wikipedia.org/wiki/BERT_(language_model))，通常能取得更好的效果。预训练的 BERT 模型能够理解语言的基本结构，并且可以通过相对较小的数据集和计算成本针对特定任务进行微调。

由于我们计划将 NER 应用于医学场景，因此使用在医学文本上训练的 BERT 模型是合理的。微软研究院发布了一个名为 [PubMedBERT][PubMedBERT] 的预训练模型（[相关论文][PubMedBERT-Pub]），该模型使用 [PubMed](https://pubmed.ncbi.nlm.nih.gov/) 仓库中的文本进行了微调。

训练 Transformer 模型的事实标准是 [Hugging Face Transformers](https://huggingface.co/) 库。该库还包含一个由社区维护的预训练模型仓库，其中包括 PubMedBERT。加载和使用该模型只需要几行代码：

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

这段代码为我们提供了一个 `model` 对象，用于基于 `classes` 数量的类别进行标注任务，以及一个 `tokenizer` 对象，用于将输入文本分割为 token。你需要将数据集转换为 BIO 格式，同时考虑到 PubMedBERT 的分词方式。你可以参考 [这段 Python 代码](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) 来获取灵感。

## 收获

这个任务非常接近实际工作中可能遇到的任务，尤其是当你希望从大量自然语言文本中获取更多洞见时。在我们的案例中，我们可以将训练好的模型应用于 [COVID 相关论文数据集](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)，看看能从中获取哪些洞见。[这篇博客文章](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) 和 [这篇论文](https://www.mdpi.com/2504-2289/6/1/4) 描述了可以使用 NER 对该论文语料库进行的研究。

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档作为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而引起的任何误解或误读，我们概不负责。