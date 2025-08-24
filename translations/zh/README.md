<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3a6b0ddf7e6e3f33b2a543baf086dc9",
  "translation_date": "2025-08-24T20:27:06+00:00",
  "source_file": "README.md",
  "language_code": "zh"
}
-->
[![GitHub license](https://img.shields.io/github/license/microsoft/AI-For-Beginners.svg)](https://github.com/microsoft/AI-For-Beginners/blob/main/LICENSE)  
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/AI-For-Beginners.svg)](https://GitHub.com/microsoft/AI-For-Beginners/graphs/contributors/)  
[![GitHub issues](https://img.shields.io/github/issues/microsoft/AI-For-Beginners.svg)](https://GitHub.com/microsoft/AI-For-Beginners/issues/)  
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/AI-For-Beginners.svg)](https://GitHub.com/microsoft/AI-For-Beginners/pulls/)  
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/AI-For-Beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/AI-For-Beginners/watchers/)  
[![GitHub forks](https://img.shields.io/github/forks/microsoft/AI-For-Beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/AI-For-Beginners/network/)  
[![GitHub stars](https://img.shields.io/github/stars/microsoft/AI-For-Beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/AI-For-Beginners/stargazers/)  
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/microsoft/ai-for-beginners/HEAD)  
[![Gitter](https://badges.gitter.im/Microsoft/ai-for-beginners.svg)](https://gitter.im/Microsoft/ai-for-beginners?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)  

[![](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.gg/zxKYvhSnVp?WT.mc_id=academic-000002-leestott)  

# 人工智能入门 - 课程大纲  

|![ 由 [(@girlie_mac)](https://twitter.com/girlie_mac) 绘制的草图 ](./lessons/sketchnotes/ai-overview.png)|  
|:---:|  
| 人工智能入门 - _草图由 [@girlie_mac](https://twitter.com/girlie_mac) 绘制_ |  

通过我们的 12 周、24 节课程大纲，探索**人工智能**（AI）的世界！课程包括实践课程、测验和实验室，适合初学者，涵盖了 TensorFlow 和 PyTorch 等工具，以及 AI 的伦理问题。  

## 你将学到什么  

**[课程思维导图](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**  

在本课程中，你将学习：  

* 人工智能的不同方法，包括“传统的”基于符号的**知识表示**和推理方法（[GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)）。  
* **神经网络**和**深度学习**，它们是现代 AI 的核心。我们将使用两种最流行的框架 [TensorFlow](http://Tensorflow.org) 和 [PyTorch](http://pytorch.org) 的代码来说明这些重要主题背后的概念。  
* 用于处理图像和文本的**神经网络架构**。我们将涵盖一些最新的模型，但可能不包括最前沿的内容。  
* 不太流行的 AI 方法，例如**遗传算法**和**多智能体系统**。  

本课程不包括以下内容：  

> [在我们的 Microsoft Learn 资源集合中找到本课程的所有附加资源](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)  

* **AI 在商业中的应用案例**。建议学习 Microsoft Learn 上的 [面向商业用户的 AI 入门](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) 学习路径，或与 [INSEAD](https://www.insead.edu/) 合作开发的 [AI 商学院](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum)。  
* **经典机器学习**，这部分内容已在我们的 [机器学习入门课程](http://github.com/Microsoft/ML-for-Beginners) 中详细描述。  
* 使用 **[认知服务](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)** 构建的实际 AI 应用。建议从 Microsoft Learn 的模块开始学习 [计算机视觉](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum)、[自然语言处理](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum)、**[Azure OpenAI 服务的生成式 AI](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** 等内容。  
* 特定的机器学习**云框架**，如 [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum)、[Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum) 或 [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum)。建议学习 [使用 Azure Machine Learning 构建和操作机器学习解决方案](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) 和 [使用 Azure Databricks 构建和操作机器学习解决方案](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum) 学习路径。  
* **对话式 AI** 和 **聊天机器人**。可以参考 [创建对话式 AI 解决方案](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum) 学习路径，或阅读 [这篇博客文章](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) 了解更多细节。  
* **深度学习的数学原理**。建议阅读 Ian Goodfellow、Yoshua Bengio 和 Aaron Courville 的 [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618)，也可以在线访问 [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/)。  

如果想要轻松了解 _云端 AI_ 主题，可以学习 [在 Azure 上开始人工智能之旅](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum) 学习路径。  

# 课程内容  

|     |                                                                 课程链接                                                                  |                                           PyTorch/Keras/TensorFlow                                          | 实验室                                                            |  
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |  
| 0  |                                 [课程设置](./lessons/0-course-setup/setup.md)                                 |                      [设置开发环境](./lessons/0-course-setup/how-to-run.md)                       |   |  
| I  |               [**AI 简介**](./lessons/1-Intro/README.md)      | | |  
| 01  |       [AI 简介与历史](./lessons/1-Intro/README.md)       |           -                            | -  |  
| II |              **符号 AI**              |  
| 02  |       [知识表示与专家系统](./lessons/2-Symbolic/README.md)       |            [专家系统](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) /  [本体论](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) /[概念图](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |  
| III |                        [**神经网络简介**](./lessons/3-NeuralNetworks/README.md) |||  
| 03  |                [感知机](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [实验室](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |  
| 04  |                   [多层感知机与创建我们自己的框架](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [实验室](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |  
| 05  |            [框架简介（PyTorch/TensorFlow）与过拟合](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [实验室](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |  
| IV  |            [**计算机视觉**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [在 Microsoft Azure 上探索计算机视觉](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |  
| 06  |            [计算机视觉简介. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [实验室](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |  
| 07  |            [卷积神经网络](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [CNN 架构](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [实验室](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |  
| 08  |            [预训练网络和迁移学习](./lessons/4-ComputerVision/08-TransferLearning/README.md) 和 [训练技巧](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [实验](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [自动编码器和变分自动编码器 (VAEs)](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [生成对抗网络 (GANs) 和艺术风格迁移](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [目标检测](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [实验](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [语义分割. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](../../(https:/github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb))             |  |
| V  |            [**自然语言处理**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [在 Microsoft Azure 上探索自然语言处理](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [文本表示. Bow/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [语义词嵌入. Word2Vec 和 GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [语言建模. 训练自己的嵌入](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [实验](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [循环神经网络 (RNN)](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [生成循环网络](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.md) / [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.md)             | [实验](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Transformer. BERT.](./lessons/5-NLP/18-Transformers/READMEtransformers.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [命名实体识别 (NER)](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [实验](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [大型语言模型、提示编程和少样本任务](./lessons/5-NLP/20-LangModels/READMELargeLang.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **其他 AI 技术** || |
| 21  |            [遗传算法](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [深度强化学习](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [实验](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [多智能体系统](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **AI伦理** | | |
| 24  |            [AI伦理与负责任的AI](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: 负责任的AI原则](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **额外内容** | | |
| 25  |            [多模态网络、CLIP 和 VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## 每节课包含

* 预读材料
* 可执行的 Jupyter Notebook，通常针对特定框架（**PyTorch** 或 **TensorFlow**）。可执行的 Notebook 还包含大量理论内容，因此要理解主题，您需要至少阅读一个版本的 Notebook（PyTorch 或 TensorFlow）。
* **实验**：部分主题提供实验，您可以尝试将所学内容应用于具体问题。
* 部分章节包含链接到 [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) 模块，涵盖相关主题。

## 入门指南

- 我们创建了一个 [设置课程](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/0-course-setup/setup.md)，帮助您设置开发环境。
- 对于教育工作者，我们还创建了一个 [课程设置指南](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/0-course-setup/for-teachers.md)！
- 如何 [在 VSCode 或 Codepace 中运行代码](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/0-course-setup/how-to-run.md)

按照以下步骤操作：

Fork 仓库：点击页面右上角的 "Fork" 按钮。

克隆仓库：`git clone https://github.com/microsoft/AI-For-Beginners.git`

别忘了给这个仓库加星标 (🌟)，方便以后找到。

## 认识其他学习者

加入我们的 [官方 AI Discord 服务器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum)，与其他学习者交流并获得支持。

如果您在构建过程中有产品反馈或问题，请访问我们的 [Azure AI Foundry 开发者论坛](https://aka.ms/foundry/forum)

## 测验
> **关于测验的说明**：所有测验都存储在 etc\quiz-app 文件夹中的 Quiz-app 文件夹内。它们通过课程内容链接到测验应用程序，该应用程序可以在本地运行或部署到 Azure；请按照 `quiz-app` 文件夹中的说明操作。测验正在逐步进行本地化。
## 寻求帮助

您有建议或发现拼写或代码错误吗？请提交问题或创建拉取请求。

## 特别感谢

* **✍️ 主要作者:** [Dmitry Soshnikov](http://soshnikov.com), 博士
* **🔥 编辑:** [Jen Looper](https://twitter.com/jenlooper), 博士
* **🎨 手绘笔记插画师:** [Tomomi Imura](https://twitter.com/girlie_mac)
* **✅ 测验创建者:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)
* **🙏 核心贡献者:** [Evgenii Pishchik](https://github.com/Pe4enIks)

## 其他课程

我们的团队还制作了其他课程！查看以下内容：

- [初学者生成式 AI](https://aka.ms/genai-beginners)
- [初学者生成式 AI .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [使用 JavaScript 的生成式 AI](https://github.com/microsoft/generative-ai-with-javascript)
- [使用 Java 的生成式 AI](https://github.com/microsoft/Generative-AI-for-beginners-java)
- [初学者 AI](https://aka.ms/ai-beginners)
- [初学者数据科学](https://aka.ms/datascience-beginners)
- [初学者机器学习](https://aka.ms/ml-beginners)
- [初学者网络安全](https://github.com/microsoft/Security-101) 
- [初学者 Web 开发](https://aka.ms/webdev-beginners)
- [初学者物联网](https://aka.ms/iot-beginners)
- [初学者 XR 开发](https://github.com/microsoft/xr-development-for-beginners)
- [掌握 GitHub Copilot 的智能使用](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
- [为 C#/.NET 开发者掌握 GitHub Copilot](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)
- [选择你的 Copilot 冒险](https://github.com/microsoft/CopilotAdventures)

**免责声明**：  
本文档使用AI翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文档的原始语言版本为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用本翻译而引起的任何误解或误读不承担责任。