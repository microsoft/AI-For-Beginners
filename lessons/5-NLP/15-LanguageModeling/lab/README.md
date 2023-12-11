# 训练Skip-Gram模型

来自[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)的实验任务。

## 任务

在这个实验中，我们要求您使用Skip-Gram技术训练Word2Vec模型。训练一个具有嵌入的神经网络，用于预测$N$-tokens-wide的Skip-Gram窗口中的相邻单词。您可以使用[本课程的代码](../CBoW-TF.ipynb)，并进行一些微小的修改。

## 数据集

您可以随意选择任何一本书。在[古腾堡计划](https://www.gutenberg.org/)上可以找到很多免费的文本，例如，这是[刘易斯·卡罗尔](https://www.gutenberg.org/files/11/11-0.txt)的《爱丽丝梦游仙境》的直接链接。或者，您可以使用莎士比亚的戏剧作品，可以使用以下代码获取：

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## 开始探索吧！

如果你有时间并且想更深入地了解这个主题，可以尝试探索以下几个方面：

* 嵌入大小如何影响结果？
* 不同的文本风格对结果有何影响？
* 拿取几个非常不同类型的单词及其同义词，获取其向量表示，应用PCA算法将维度降低为2，并在二维空间中绘制它们。你能看到任何模式吗？