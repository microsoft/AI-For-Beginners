# 命名实体识别（NER）

来自于[AI初学者课程](https://github.com/microsoft/ai-for-beginners)的实验作业。

## 任务

在这个实验中，你需要训练一个用于医学术语的命名实体识别模型。

## 数据集要训练NER模型，我们需要具有正确标记的医学实体的数据集。[BC5CDR数据集](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/)包含来自1500多篇论文的已标记的疾病和化学实体。您可以在他们的网站上注册后下载这个数据集。

BC5CDR数据集的样式如下：

```
6794356|t|新生儿患有三尖瓣反流和碳酸锂中毒。
6794356|a|描述了一名新生儿患有巨大的三尖瓣反流、心房扑动、充血性心力衰竭和高血清锂水平。这是首个最初表现为三尖瓣反流和心房扑动的患者，也是首个在妊娠初期暴露于锂化合物的婴儿中患有心脏疾病的患者（第11例）。这些婴儿中，63%有三尖瓣的受损。碳酸锂在早期妊娠期间服用时可能是导致先天性心脏病发病率增加的因素。它还会在分娩前引起神经抑制、紫绀和心律失常。
6794356	0	29	三尖瓣反流	疾病	D014262
6794356	34	51	碳酸锂	化学物质	D016651
6794356	52	60	中毒	疾病	D064420
```...

```

在这个数据集中，前两行是论文的标题和摘要，然后是个别的实体，包括在标题+摘要块中的开始和结束位置。除了实体类型，你还可以得到该实体在某个医学本体中的本体ID。

你需要编写一些Python代码将其转换为BIO编码。

## 网络

可以尝试使用LSTM网络来进行命名实体识别，就像你在课堂上所看到的例子一样。然而，在自然语言处理任务中，[变压器架构](https://en.wikipedia.org/wiki/Transformer_(machine_learning_model))，尤其是[BERT语言模型](https://en.wikipedia.org/wiki/BERT_(language_model))的结果要好得多。预训练的BERT模型可以理解语言的通用结构，并且可以通过相对较小的数据集和计算成本进行特定任务的微调。由于我们计划在医疗场景中应用NER，因此使用在医学文本上训练的BERT模型是有意义的。Microsoft Research发布了一个名为[PubMedBERT][PubMedBERT]的预训练模型（[出版物][PubMedBERT-Pub]），该模型使用了来自[PubMed](https://pubmed.ncbi.nlm.nih.gov/)数据库的文本进行微调。

对于训练Transformer模型，*事实上*的标准是[Hugging Face Transformers](https://huggingface.co/)库。该库还包含一个社区维护的预训练模型的存储库，其中包括PubMedBERT。要加载和使用此模型，我们只需要几行代码：

```python
model_name = "microsoft/BiomedNLP-PubMedBERT-base-uncased-abstract"
classes = ... # 类别数：2*实体数+1
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name, classes)
``````

这将为我们提供`model`本身，该模型用于标记分类任务，使用`classes`类的数量，以及将输入文本拆分为标记的`tokenizer`对象。您需要将数据集转换为BIO格式，并考虑PubMedBERT的标记化。您可以使用[这段Python代码](https://gist.github.com/shwars/580b55684be3328eb39ecf01b9cbbd88)作为灵感。

## 要点

这个任务非常接近于你可能遇到的实际任务，如果你想对大量的自然语言文本获得更多的见解。在我们的案例中，我们可以将我们训练好的模型应用于[COVID相关论文的数据集](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)，并查看我们能得到的见解。[这篇博客文章](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/)和[这篇论文](https://www.mdpi.com/2504-2289/6/1/4)描述了使用NER对这些论文语料库进行的研究。