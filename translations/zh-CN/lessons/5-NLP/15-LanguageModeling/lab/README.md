# 训练 Skip-Gram 模型

来自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的实验任务。

## 任务

在本实验中，我们挑战你使用 Skip-Gram 技术训练 Word2Vec 模型。训练一个嵌入网络来预测 $N$ 个词宽的 Skip-Gram 窗口中的邻近词。你可以使用[本课中的代码](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)，并稍作修改。

## 数据集

你可以使用任何书籍。你可以在 [Project Gutenberg](https://www.gutenberg.org/) 找到许多免费文本，例如，这里有一个直接链接到刘易斯·卡罗尔的《爱丽丝梦游仙境》：[Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt)。或者，你可以使用莎士比亚的戏剧，以下代码可以获取：

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## 探索！

如果你有时间并希望深入研究这个主题，可以尝试探索以下内容：

* 嵌入大小如何影响结果？
* 不同的文本风格如何影响结果？
* 选择几组非常不同类型的单词及其同义词，获取它们的向量表示，应用 PCA 将维度降到 2，并在二维空间中绘制它们。你能发现任何模式吗？

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文档的原始语言版本为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用此翻译而引起的任何误解或误读不承担责任。