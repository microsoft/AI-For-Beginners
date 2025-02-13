# 自然语言处理

![NLP任务总结手绘图](../../../../translated_images/ai-nlp.b22dcb8ca4707ceaee8576db1c5f4089c8cac2f454e9e03ea554f07fda4556b8.zh.png)

在本节中，我们将重点讨论使用神经网络处理与**自然语言处理（NLP）**相关的任务。我们希望计算机能够解决许多NLP问题：

* **文本分类**是一个典型的分类问题，涉及文本序列。例如，将电子邮件消息分类为垃圾邮件与非垃圾邮件，或者将文章归类为体育、商业、政治等。此外，在开发聊天机器人时，我们常常需要理解用户想表达的内容——在这种情况下，我们处理的是**意图分类**。在意图分类中，我们通常需要处理多个类别。
* **情感分析**是一个典型的回归问题，我们需要给句子的含义分配一个数字（情感），以表示其正面或负面的程度。情感分析的更高级版本是**基于方面的情感分析**（ABSA），我们将情感归因于句子的不同部分（方面），例如：*在这家餐厅，我喜欢菜肴，但气氛糟糕*。
* **命名实体识别**（NER）是指从文本中提取特定实体的问题。例如，我们可能需要理解在短语*我明天需要飞往巴黎*中，单词*明天*指的是日期，而*巴黎*是一个地点。  
* **关键词提取**类似于NER，但我们需要自动提取对句子含义重要的单词，而不需要针对特定实体类型进行预训练。
* **文本聚类**在我们想要将相似句子分组时非常有用，例如在技术支持对话中的相似请求。
* **问答系统**指的是模型回答特定问题的能力。模型接收一段文本和一个问题作为输入，并需要提供文本中包含问题答案的位置（或者，有时生成答案文本）。
* **文本生成**是模型生成新文本的能力。它可以被视为一个分类任务，根据某些*文本提示*预测下一个字母/单词。高级文本生成模型，如GPT-3，能够使用一种称为[提示编程](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0)或[提示工程](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29)的技术解决其他NLP任务，如分类。
* **文本摘要**是一种技术，当我们希望计算机“阅读”长文本并用几句话进行总结时使用。
* **机器翻译**可以被视为在一种语言中理解文本和在另一种语言中生成文本的结合。

最初，大多数NLP任务是使用传统方法如语法解决的。例如，在机器翻译中，解析器被用来将初始句子转换为语法树，然后提取更高级的语义结构来表示句子的含义，并根据这个含义和目标语言的语法生成结果。如今，许多NLP任务通过神经网络更有效地解决。

> 许多经典的NLP方法已在[自然语言处理工具包（NLTK）](https://www.nltk.org)的Python库中实现。在线上有一本很棒的[NLTK书](https://www.nltk.org/book/)，涵盖了如何使用NLTK解决不同的NLP任务。

在我们的课程中，我们将主要专注于使用神经网络进行NLP，并在需要时使用NLTK。

我们已经学习了如何使用神经网络处理表格数据和图像。这些数据类型与文本之间的主要区别在于，文本是可变长度的序列，而图像的输入大小是预先已知的。虽然卷积网络可以从输入数据中提取模式，但文本中的模式更为复杂。例如，否定与主语的分离在许多词中是任意的（例如：*我不喜欢橙子*，与*我不喜欢那些大而色彩斑斓的美味橙子*），而这仍应被解释为一种模式。因此，为了处理语言，我们需要引入新的神经网络类型，如*递归网络*和*变换器*。

## 安装库

如果您使用本地Python安装来运行本课程，您可能需要使用以下命令安装NLP所需的所有库：

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

在本节中，在一些示例中我们将训练相当大的模型。
* **使用支持GPU的计算机**：建议在支持GPU的计算机上运行您的笔记本，以减少处理大型模型时的等待时间。
* **GPU内存限制**：在GPU上运行可能会导致内存不足的情况，特别是在训练大型模型时。
* **GPU内存消耗**：训练期间消耗的GPU内存量取决于多个因素，包括小批量大小。
* **最小化小批量大小**：如果遇到GPU内存问题，请考虑在代码中减少小批量大小作为潜在解决方案。
* **TensorFlow GPU内存释放**：旧版本的TensorFlow在一个Python内核中训练多个模型时可能无法正确释放GPU内存。为了有效管理GPU内存使用，您可以配置TensorFlow仅在需要时分配GPU内存。
* **代码包含**：要将TensorFlow设置为仅在需要时增长GPU内存分配，请在您的笔记本中包含以下代码：

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
```

如果您有兴趣从经典机器学习的角度学习NLP，请访问[这套课程](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP)。

## 本节内容
在本节中，我们将学习：

* [将文本表示为张量](13-TextRep/README.md)
* [词嵌入](14-Emdeddings/README.md)
* [语言建模](15-LanguageModeling/README.md)
* [递归神经网络](16-RNN/README.md)
* [生成网络](17-GenerativeNetworks/README.md)
* [变换器](18-Transformers/README.md)

**免责声明**：
本文件是使用基于机器的人工智能翻译服务进行翻译的。尽管我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应视为权威来源。对于关键信息，建议进行专业人工翻译。我们对因使用此翻译而导致的任何误解或误释不承担责任。