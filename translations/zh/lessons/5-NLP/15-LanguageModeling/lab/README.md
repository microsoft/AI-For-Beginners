# 训练 Skip-Gram 模型

来自 [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) 的实验作业。

## 任务

在本实验中，我们挑战您使用 Skip-Gram 技术训练 Word2Vec 模型。训练一个网络，通过嵌入来预测 $N$-tokens 宽的 Skip-Gram 窗口中的邻近词。您可以使用 [本课的代码](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)，并稍作修改。

## 数据集

您可以使用任何书籍。您可以在 [Project Gutenberg](https://www.gutenberg.org/) 找到很多免费的文本，例如，这里有一条直接链接到路易斯·卡罗尔的 [《爱丽丝梦游仙境》](https://www.gutenberg.org/files/11/11-0.txt)。或者，您可以使用莎士比亚的戏剧，您可以使用以下代码获取：

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## 探索！

如果您有时间并想深入了解该主题，可以尝试探索几个方面：

* 嵌入大小如何影响结果？
* 不同文本风格如何影响结果？
* 选取几种非常不同类型的词及其同义词，获取它们的向量表示，应用 PCA 将维度降低到 2，并在二维空间中绘制它们。您能看到任何模式吗？

**免责声明**：
本文件使用基于机器的人工智能翻译服务进行翻译。虽然我们努力追求准确性，但请注意，自动翻译可能包含错误或不准确之处。原始文件的母语版本应被视为权威来源。对于关键信息，建议进行专业人工翻译。我们对因使用本翻译而导致的任何误解或误释不承担责任。