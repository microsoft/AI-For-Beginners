# NER

来自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的实验作业。

## 任务

在这个实验中，您需要训练一个用于医学术语的命名实体识别模型。

## 数据集

为了训练 NER 模型，我们需要一个标注良好的包含医学实体的数据集。[BC5CDR 数据集](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/) 包含来自 1500 多篇论文的标注疾病和化学实体。您可以在他们的网站注册后下载数据集。

BC5CDR 数据集的格式如下：

```
6794356|t|Tricuspid valve regurgitation and lithium carbonate toxicity in a newborn infant.
6794356|a|A newborn with massive tricuspid regurgitation, atrial flutter, congestive heart failure, and a high serum lithium level is described. This is the first patient to initially manifest tricuspid regurgitation and atrial flutter, and the 11th described patient with cardiac disease among infants exposed to lithium compounds in the first trimester of pregnancy. Sixty-three percent of these infants had tricuspid valve involvement. Lithium carbonate may be a factor in the increasing incidence of congenital heart disease when taken during early pregnancy. It also causes neurologic depression, cyanosis, and cardiac arrhythmia when consumed prior to delivery.
6794356	0	29	Tricuspid valve regurgitation	Disease	D014262
6794356	34	51	lithium carbonate	Chemical	D016651
6794356	52	60	toxicity	Disease	D064420
...
```

在这个数据集中，前两行是论文的标题和摘要，接下来是单个实体，包含在标题+摘要块中的起始和结束位置。除了实体类型，您还将获得该实体在某个医学本体中的本体 ID。

您需要编写一些 Python 代码将其转换为 BIO 编码。

## 网络

第一次尝试 NER 可以使用 LSTM 网络，就像您在课程中看到的例子一样。然而，在 NLP 任务中，[变压器架构](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))，特别是 [BERT 语言模型](https://en.wikipedia.org/wiki/BERT_(language_model)) 表现得更好。预训练的 BERT 模型理解语言的一般结构，并且可以通过相对较小的数据集和计算成本进行微调以适应特定任务。

由于我们计划将 NER 应用到医学场景中，使用在医学文本上训练的 BERT 模型是合理的。微软研究院发布了一个名为 [PubMedBERT][PubMedBERT] 的预训练模型 ([publication][PubMedBERT-Pub])，该模型是使用来自 [PubMed](https://pubmed.ncbi.nlm.nih.gov/) 仓库的文本进行微调的。

训练变压器模型的*事实*标准是 [Hugging Face Transformers](https://huggingface.co/) 库。它还包含一个由社区维护的预训练模型库，包括 PubMedBERT。要加载和使用这个模型，我们只需几行代码：

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # number of classes: 2*entities+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
```

这将给我们提供 `model` itself, built for token classification task using `classes` number of classes, as well as `tokenizer` 对象，可以将输入文本拆分为标记。您需要将数据集转换为 BIO 格式，同时考虑 PubMedBERT 的分词。您可以使用 [这段 Python 代码](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88) 作为灵感。

## 收获

这个任务非常接近您如果想深入了解大量自然语言文本时可能会遇到的实际任务。在我们的案例中，我们可以将训练好的模型应用于 [与 COVID 相关的论文数据集](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)，看看我们能够获得哪些洞察。 [这篇博客文章](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/) 和 [这篇论文](https://www.mdpi.com/2504-2289/6/1/4) 描述了可以在这个论文语料库上使用 NER 进行的研究。

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。虽然我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于关键信息，建议进行专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。