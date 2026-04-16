# 初学者友好的 AI 示例

欢迎！本目录包含简单、独立的示例，旨在帮助您入门 AI 和机器学习。每个示例都设计为对初学者友好，并附有详细的注释和逐步的解释。

## 📚 示例概览

| 示例 | 描述 | 难度 | 前置知识 |
|------|------|------|----------|
| [Hello AI World](../../../examples/01-hello-ai-world.py) | 您的第一个 AI 程序——简单的模式识别 | ⭐ 初学者 | Python 基础 |
| [Simple Neural Network](../../../examples/02-simple-neural-network.py) | 从零开始构建一个神经网络 | ⭐⭐ 初学者+ | Python，基础数学 |
| [Image Classifier](./03-image-classifier.ipynb) | 使用预训练模型对图像进行分类 | ⭐⭐ 初学者+ | Python，numpy |
| [Text Sentiment](../../../examples/04-text-sentiment.py) | 分析文本情感（正面/负面） | ⭐⭐ 初学者+ | Python |

## 🚀 入门指南

### 前置知识

确保您已安装 Python（推荐 3.8 或更高版本）。安装所需的包：

```bash
# For Python scripts
pip install numpy

# For Jupyter notebooks (image classifier)
pip install jupyter numpy pillow tensorflow
```

或者使用主课程中的 conda 环境：

```bash
conda env create --name ai4beg --file ../environment.yml
conda activate ai4beg
```

### 运行示例

**对于 Python 脚本 (.py 文件)：**
```bash
python 01-hello-ai-world.py
```

**对于 Jupyter 笔记本 (.ipynb 文件)：**
```bash
jupyter notebook 03-image-classifier.ipynb
```

## 📖 学习路径

我们建议按顺序学习以下示例：

1. **从“Hello AI World”开始** - 学习模式识别的基础知识
2. **构建一个简单的神经网络** - 理解神经网络的工作原理
3. **尝试图像分类器** - 使用真实图像体验 AI 的实际应用
4. **分析文本情感** - 探索自然语言处理

## 💡 初学者提示

- **仔细阅读代码注释** - 它们解释了每一行代码的作用
- **大胆尝试！** - 尝试修改参数，观察结果
- **不要担心无法完全理解** - 学习是一个循序渐进的过程
- **提出问题** - 使用 [讨论板](https://github.com/microsoft/AI-For-Beginners/discussions)

## 🔗 下一步

完成这些示例后，可以探索完整课程：
- [AI 简介](../lessons/1-Intro/README.md)
- [神经网络](../lessons/3-NeuralNetworks/README.md)
- [计算机视觉](../lessons/4-ComputerVision/README.md)
- [自然语言处理](../lessons/5-NLP/README.md)

## 🤝 贡献

觉得这些示例有帮助吗？欢迎帮助我们改进：
- 报告问题或提出改进建议
- 添加更多适合初学者的示例
- 改进文档和注释

---

*记住：每个专家都曾是初学者。祝学习愉快！ 🎓*

---

**免责声明**：  
本文档使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文档为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而引起的任何误解或误读，我们概不负责。