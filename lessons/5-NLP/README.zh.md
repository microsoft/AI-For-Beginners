# 自然语言处理

![NLP任务摘要](../sketchnotes/ai-nlp.png)

在本节中，我们将着重讨论使用神经网络处理与自然语言处理(NLP)相关的任务。有许多我们希望计算机能够解决的NLP问题：

* **文本分类** 是涉及文本序列的典型分类问题。例如，将电子邮件消息分类为垃圾邮件和非垃圾邮件，或将文章归类为体育、商业、政治等等。此外，在开发聊天机器人时，我们经常需要理解用户的意图 - 在这种情况下，我们处理的是**意图分类**。通常，在意图分类中，我们需要处理许多类别。
* **情感分析** 是一个典型的回归问题，我们需要为一个句子的意义归属一个数字（情感），表示其是积极的还是消极的。情感分析的一个更高级版本是**基于方面的情感分析**（ABSA），在其中我们将情感归属于句子的不同部分（方面），例如*在这家餐厅里，我喜欢菜肴，但气氛很糟糕*。
* **命名实体识别**（NER）是指从文本中提取特定实体的问题。例如，我们可能需要理解在短语*明天我需要飞往巴黎*中，*明天*表示日期，*巴黎*是一个位置。
* **关键词提取**类似于NER，但我们需要自动提取对句子意义重要的单词，而无需为特定实体类型进行预训练。* **文本聚类**在我们想要将相似的句子分组在一起时非常有用，例如，在技术支持对话中相似的请求。
* **问答系统**是指模型回答特定问题的能力。模型接收文本段落和问题作为输入，并需要提供包含问题答案的文本位置（或者有时生成答案文本）。
* **文本生成**是模型生成新文本的能力。它可以被视为根据一些“文本提示”预测下一个字/词的分类任务。先进的文本生成模型，如GPT-3，可以使用一种称为[提示编程](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0)或[提示工程](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29)的技术解决其他NLP任务，如分类。
* **文本摘要**是一种技术，当我们希望计算机能够“阅读”长篇文本并用几句话总结它时使用。
* **机器翻译**可以看作是在一种语言中的文本理解和另一种语言中的文本生成的组合。

最初，大多数NLP任务是使用传统方法来解决的，比如语法。例如，在机器翻译中，解析器被用来将初始句子转换成语法树，然后提取更高层次的语义结构来表示句子的含义，再根据这个含义和目标语言的语法生成结果。现在，许多NLP任务使用神经网络来解决更有效。

> 许多经典的NLP方法在Python库[自然语言处理工具包（NLTK）](https://www.nltk.org)中实现。有一本名为[NLTK Book](https://www.nltk.org/book/)的在线书籍，介绍了如何使用NLTK解决不同的NLP任务。在我们的课程中，我们主要关注使用神经网络进行自然语言处理，并在需要的情况下使用NLTK。

我们已经学习了如何使用神经网络处理表格数据和图像。这些类型的数据与文本的区别在于，文本是一个可变长度的序列，而图像的输入大小是预先确定的。虽然卷积网络可以从输入数据中提取模式，但文本中的模式更复杂。例如，我们可以将否定从主题中分隔开来对诸多单词(例如，*我不喜欢橙子*与 *我不喜欢那些大而色彩丰富的美味橙子*)，而它们仍然应该被解释为一个模式。因此，为了处理语言，我们需要引入新的神经网络类型，如*循环网络*和*变压器*。

## 安装库

如果您正在使用本地Python安装运行此课程，则可能需要使用以下命令安装NLP的所有必需库:

**对于PyTorch**
```bash

```
pip install -r requirements-torch.txt
```

**对于TensorFlow**
```bash
pip install -r requirements-tf.txt
```

> 您可以在[Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/?WT.mc_id=academic-77998-cacaste)上尝试使用TensorFlow进行NLP。

## GPU警告

在本节中，我们将训练一些相当大的模型。建议在启用GPU的计算机上运行笔记本，以尽量减少等待时间。

在使用GPU运行时，可能会遇到GPU内存不足的情况。在训练过程中，消耗的GPU内存量取决于许多因素，包括小批量的大小。如果遇到内存问题，您可以尝试在代码中将小批量的大小最小化。

而且，某些较旧版本的TensorFlow如果在一个Python内核中训练多个模型时，可能无法正确释放GPU内存。为了谨慎使用GPU内存，您可以将TensorFlow选项设置为仅在需要时增加GPU内存分配。您需要在笔记本中包含以下代码:

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
```
```python
tf.config.experimental.set_memory_growth(physical_devices[0], True)
```

如果您对从经典机器学习的角度学习自然语言处理感兴趣，请访问[这套教程](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP)

## 在本节中
在本节中，我们将学习以下内容：

* [将文本表示为张量](13-TextRep/README.md)
* [词嵌入](14-Emdeddings/README.md)* [语言模型](15-LanguageModeling/README.md)
* [循环神经网络](16-RNN/README.md)
* [生成网络](17-GenerativeNetworks/README.md)
* [Transformer](18-Transformers/README.md)