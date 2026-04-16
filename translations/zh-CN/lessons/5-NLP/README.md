# 自然语言处理

![NLP任务总结图](../../../../translated_images/zh-CN/ai-nlp.b22dcb8ca4707cea.webp)

在本节中，我们将重点使用神经网络来处理与**自然语言处理 (NLP)**相关的任务。我们希望计算机能够解决许多NLP问题：

* **文本分类**是一个典型的与文本序列相关的分类问题。例如，将电子邮件分类为垃圾邮件或非垃圾邮件，或者将文章分类为体育、商业、政治等类别。此外，在开发聊天机器人时，我们通常需要理解用户的意图——这就是所谓的**意图分类**。意图分类通常需要处理许多类别。
* **情感分析**是一个典型的回归问题，我们需要为句子的正面/负面意义赋予一个数值（情感）。更高级的情感分析是**基于方面的情感分析** (ABSA)，它不是为整个句子赋予情感，而是为句子的不同部分（方面）赋予情感，例如：*在这家餐厅，我喜欢菜品，但氛围很糟糕*。
* **命名实体识别** (NER) 是从文本中提取特定实体的问题。例如，我们需要理解在短语*我明天要飞往巴黎*中，*明天*指的是日期，*巴黎*是一个地点。
* **关键词提取**与NER类似，但我们需要自动提取对句子意义重要的词，而无需针对特定实体类型进行预训练。
* **文本聚类**在我们希望将相似的句子分组时非常有用，例如在技术支持对话中将相似的请求归类。
* **问答**是指模型回答特定问题的能力。模型接收一个文本段落和一个问题作为输入，并需要提供文本中包含问题答案的位置（有时需要生成答案文本）。
* **文本生成**是模型生成新文本的能力。它可以被视为一个分类任务，根据某些*文本提示*预测下一个字母/单词。高级文本生成模型（如GPT-3）能够通过一种称为[提示编程](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0)或[提示工程](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29)的技术解决其他NLP任务，例如分类。
* **文本摘要**是一种技术，我们希望计算机能够“阅读”长文本并用几句话进行总结。
* **机器翻译**可以被视为一种结合一种语言的文本理解和另一种语言的文本生成的任务。

最初，大多数NLP任务是通过传统方法（如语法）解决的。例如，在机器翻译中，解析器用于将初始句子转换为语法树，然后提取高级语义结构以表示句子的意义，基于这种意义和目标语言的语法生成结果。如今，许多NLP任务通过神经网络更有效地解决。

> 许多经典的NLP方法在[自然语言处理工具包 (NLTK)](https://www.nltk.org) Python库中实现。在线有一本很棒的[NLTK书籍](https://www.nltk.org/book/)，涵盖了如何使用NLTK解决不同的NLP任务。

在我们的课程中，我们将主要关注使用神经网络进行NLP，并在需要时使用NLTK。

我们已经学习了如何使用神经网络处理表格数据和图像。这些数据类型与文本的主要区别在于，文本是一个可变长度的序列，而图像的输入大小是预先确定的。虽然卷积网络可以从输入数据中提取模式，但文本中的模式更复杂。例如，否定可能与主语分隔许多单词（例如：*我不喜欢橙子*，与*我不喜欢那些又大又多彩又美味的橙子*），但仍应被解释为一个模式。因此，为了处理语言，我们需要引入新的神经网络类型，例如*循环网络*和*Transformer*。

## 安装库

如果您使用本地Python安装运行本课程，可能需要使用以下命令安装所有NLP所需的库：

**对于PyTorch**
```bash
pip install -r requirements-torch.txt
```
**对于TensorFlow**
```bash
pip install -r requirements-tf.txt
```

> 您可以在[Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/?WT.mc_id=academic-77998-cacaste)上尝试使用TensorFlow进行NLP。

## GPU警告

在本节中，我们将在一些示例中训练较大的模型。
* **使用支持GPU的计算机**：建议在支持GPU的计算机上运行您的笔记本，以减少训练大型模型时的等待时间。
* **GPU内存限制**：在GPU上运行可能会导致GPU内存不足的情况，尤其是在训练大型模型时。
* **GPU内存消耗**：训练期间消耗的GPU内存量取决于多个因素，包括小批量大小。
* **最小化小批量大小**：如果遇到GPU内存问题，可以考虑减少代码中的小批量大小作为解决方案。
* **TensorFlow GPU内存释放**：旧版本的TensorFlow可能无法正确释放GPU内存，尤其是在一个Python内核中训练多个模型时。为了有效管理GPU内存使用，可以配置TensorFlow仅在需要时分配GPU内存。
* **代码包含**：要设置TensorFlow仅在需要时增长GPU内存分配，请在笔记本中包含以下代码：

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
```

如果您对从经典机器学习角度学习NLP感兴趣，请访问[这套课程](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP)。

## 本节内容
在本节中，我们将学习：

* [将文本表示为张量](13-TextRep/README.md)
* [词嵌入](14-Emdeddings/README.md)
* [语言建模](15-LanguageModeling/README.md)
* [循环神经网络](16-RNN/README.md)
* [生成网络](17-GenerativeNetworks/README.md)
* [Transformer](18-Transformers/README.md)

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文档的原始语言版本为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而引起的任何误解或误读不承担责任。