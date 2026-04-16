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

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

# 人工智能初学者课程

|![Sketchnote by @girlie_mac https://twitter.com/girlie_mac](https://github.com/microsoft/AI-For-Beginners/raw/main/lessons/sketchnotes/ai-overview.png)|
|:---:|
| AI For Beginners - _作者 [@girlie_mac](https://twitter.com/girlie_mac) 的手绘笔记_ |

通过我们的12周、24课时课程探索**人工智能**（AI）的世界！课程包含实用课程、测验和实验。课程适合初学者，涵盖了TensorFlow和PyTorch等工具，以及人工智能伦理。

### 🌐 多语言支持

#### 通过GitHub Action支持（自动且始终保持最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](./README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **倾向于本地克隆？**
>
> 本仓库包含50多种语言的翻译，因此下载体积较大。若想无翻译克隆，请使用稀疏检出：
>
> **Bash / macOS / Linux:**
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git
> cd AI-For-Beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
>
> **CMD (Windows):**
> ```cmd
> git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git
> cd AI-For-Beginners
> git sparse-checkout set --no-cone "/*" "!translations" "!translated_images"
> ```
>
> 这样可以获得完成课程所需的全部内容，下载速度更快。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**如果您希望支持额外的翻译语言，支持的语言列表请见[这里](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## 加入社区
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

## 您将学到什么

**[课程思维导图](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

在本课程中，您将学习：

* 不同的人工智能方法，包括基于**知识表示**和推理的“传统”符号方法（[GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)）。
* 现代人工智能核心的**神经网络**和**深度学习**。我们将通过两个最受欢迎框架的代码示例（[TensorFlow](http://Tensorflow.org) 和 [PyTorch](http://pytorch.org)）来解释这些重要主题背后的概念。
* 处理图像和文本的**神经架构**。将涵盖近期模型，但对最前沿技术可能稍显不足。
* 不太常见的AI方法，如**遗传算法**和**多智能体系统**。

本课程不涵盖：

> [查找本课程的所有额外资源，请访问我们的 Microsoft Learn 收藏](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)

* 在**业务中应用AI**的商业案例。可以考虑学习Microsoft Learn上的 [面向业务用户的AI介绍](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) 学习路径，或微软与 [INSEAD](https://www.insead.edu/) 合作开发的 [AI商业学院](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum)。
* **经典机器学习**，我们在 [Machine Learning for Beginners Curriculum](http://github.com/Microsoft/ML-for-Beginners) 中有详细描述。
* 使用 **[认知服务](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)** 构建的实际AI应用。推荐先学习 Microsoft Learn 中的 [视觉](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum)、[自然语言处理](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum)、**[Azure OpenAI 服务的生成式AI](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** 等模块。
* 特定的机器学习 **云框架**，如 [Azure 机器学习](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum)，[Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum) 或 [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum)。可以参考 [使用 Azure 机器学习构建和运营机器学习解决方案](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) 和 [使用 Azure Databricks 构建和运营机器学习解决方案](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum) 学习路径。
* **对话式AI** 和 **聊天机器人**。另有单独的 [创建对话式AI解决方案](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum) 学习路径，也可以参考 [这篇博客](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) 获得更多细节。
* 深度学习背后的**深层数学**。推荐参考 Ian Goodfellow、Yoshua Bengio 和 Aaron Courville 的《[Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618)》，该书也可在线阅读：[https://www.deeplearningbook.org/](https://www.deeplearningbook.org/)。

如果想轻松入门 _云端AI_ 主题，可以考虑学习 [在 Azure 上开始使用人工智能](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum) 学习路径。

# 内容

|     |                                                                 Lesson Link                                                                  |                                           PyTorch/Keras/TensorFlow                                          | Lab                                                            |
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |
| 0  |                                 [课程环境设置](./lessons/0-course-setup/setup.md)                                 |                      [设置您的开发环境](./lessons/0-course-setup/how-to-run.md)                       |   |
| I  |               [**人工智能简介**](./lessons/1-Intro/README.md)      | | |
| 01  |       [人工智能介绍与历史](./lessons/1-Intro/README.md)       |           -                            | -  |
| II |              **符号人工智能**              |
| 02  |       [知识表示与专家系统](./lessons/2-Symbolic/README.md)       |            [专家系统](./lessons/2-Symbolic/Animals.ipynb) /  [本体论](./lessons/2-Symbolic/FamilyOntology.ipynb) /[概念图](./lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |
| III |                        [**神经网络简介**](./lessons/3-NeuralNetworks/README.md) |||
| 03  |                [感知器](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [笔记本](./lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [实验](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 04  |                   [多层感知器及自建框架](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [笔记本](./lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [实验](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 05  |            [框架简介（PyTorch/TensorFlow）和过拟合](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](./lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](./lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [实验](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV  |            [**计算机视觉**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [探索 Microsoft Azure 上的计算机视觉](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |
| 06  |            [计算机视觉简介。OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [笔记本](./lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [实验](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 07  |            [卷积神经网络](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [CNN 架构](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](./lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](./lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [实验](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 08  |            [预训练网络与迁移学习](./lessons/4-ComputerVision/08-TransferLearning/README.md) 和 [训练技巧](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](./lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [实验](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [自动编码器与变分自动编码器](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](./lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [生成对抗网络与艺术风格迁移](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](./lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [目标检测](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](./lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [实验](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [语义分割。U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)             |  |
| V  |            [**自然语言处理**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [探索 Microsoft Azure 上的自然语言处理](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [文本表示。词袋模型/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [语义词向量。Word2Vec 和 GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [语言建模。训练你自己的词向量](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [实验](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [循环神经网络](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [生成循环网络](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)             | [实验](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Transformer。BERT。](./lessons/5-NLP/18-Transformers/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [命名实体识别](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [实验](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [大型语言模型，提示编程与少样本任务](./lessons/5-NLP/20-LangModels/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **其他 AI 技术** || |
| 21  |            [遗传算法](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [笔记本](./lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [深度强化学习](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](./lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](./lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [实验](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [多智能体系统](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **AI 伦理** | | |
| 24  |            [AI 伦理与负责任 AI](./lessons/7-Ethics/README.md)             |           [Microsoft Learn：负责任 AI 原则](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **附加内容** | | |
| 25  |            [多模态网络，CLIP 与 VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [笔记本](./lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## 每节课包含
* 预读材料
* 可执行的 Jupyter 笔记本，通常针对特定框架（**PyTorch** 或 **TensorFlow**）。可执行笔记本还包含大量理论材料，因此要理解主题，您需要至少阅读一个版本的笔记本（PyTorch 或 TensorFlow）。
* 一些主题提供 **实验室**，让您有机会将所学内容应用到具体问题中。
* 部分章节包含指向涵盖相关主题的 [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) 模块的链接。

## 入门指南

### 🎯 AI 新手？从这里开始！

如果您是 AI 完全新手且想要快速的动手示例，请查看我们的 [**初学者友好示例**](./examples/README.md)！其中包括：

- 🌟 **Hello AI World** - 您的第一个 AI 程序（模式识别）
- 🧠 **简单神经网络** - 从零构建神经网络  
- 🖼️ **图像分类器** - 带有详细注释的图像分类
- 💬 **文本情感分析** - 分析文本的积极/消极情感

这些示例旨在帮助您理解 AI 概念，然后再深入完整课程。

### 📚 完整课程设置

- 我们创建了一个 [环境设置课程](./lessons/0-course-setup/setup.md)，帮助您搭建开发环境。
- 面向教育者，我们也创建了一个 [课程设置指导](./lessons/0-course-setup/for-teachers.md)！
- 了解如何在 VSCode 或 Codespace 中 [运行代码](./lessons/0-course-setup/how-to-run.md)

请按以下步骤操作：

Fork 仓库：点击本页面右上角的“Fork”按钮。

克隆仓库：`git clone https://github.com/microsoft/AI-For-Beginners.git`

别忘了给该仓库点星 (🌟)，方便以后查找。

## 认识其他学习者

加入我们的[官方 AI Discord 服务器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum)，与正在学习本课程的其他学习者交流与建立联系，获得帮助支持。

如果在构建中有产品反馈或问题，请访问我们的 [Azure AI Foundry 开发者论坛](https://aka.ms/foundry/forum)

## 测验

> **关于测验的说明**：所有测验文件均在 etc\quiz-app 的 Quiz-app 文件夹中，或可[在线访问](https://ff-quizzes.netlify.app/)。它们链接于课程中，测验应用可在本地运行或部署到 Azure；请按照 `quiz-app` 文件夹中的说明操作。测验正在逐步本地化。

## 需要帮助

您有建议或发现拼写或代码错误？请提出问题或创建拉取请求。

## 特别感谢

* **✍️ 主要作者：** [Dmitry Soshnikov](http://soshnikov.com)，博士
* **🔥 编辑：** [Jen Looper](https://twitter.com/jenlooper)，博士
* **🎨 速写插画师：** [Tomomi Imura](https://twitter.com/girlie_mac)
* **✅ 测验创建者：** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)
* **🙏 核心贡献者：** [Evgenii Pishchik](https://github.com/Pe4enIks)

## 其他课程

我们的团队还制作了其他课程！敬请查看：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### 生成式 AI 系列
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### 核心学习
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot 系列
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## 获取帮助

如果您在构建 AI 应用时遇到困难或有任何疑问，欢迎加入学习者和资深开发者一起讨论 MCP 的社区。这里是一个支持性强的社区，鼓励提问并自由分享知识。

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如有产品反馈或构建中遇到错误，请访问：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：  
本文件采用人工智能翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能存在错误或不准确之处。原始文件的母语版本应视为权威来源。对于关键信息，建议使用专业人工翻译。因使用本翻译而产生的任何误解或误译，我们不承担任何责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->