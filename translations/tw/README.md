<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85102ce4bfab31103e99dc8ca2e2f181",
  "translation_date": "2026-01-15T12:02:02+00:00",
  "source_file": "README.md",
  "language_code": "tw"
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

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

# 人工智慧初學者課程綱要

|![Sketchnote by @girlie_mac https://twitter.com/girlie_mac](../../../../translated_images/tw/ai-overview.0857791951d19500.webp)|
|:---:|
| AI For Beginners - _筆記圖解由 [@girlie_mac](https://twitter.com/girlie_mac) 製作_ |

探索 **人工智慧**（AI）的世界，透過我們的 12 週、24 課程規劃！內容包含實作課程、測驗與實驗室。此課程適合初學者，涵蓋 TensorFlow 和 PyTorch 等工具，以及人工智慧倫理。

### 🌐 多語言支援

#### 透過 GitHub Action 支援（自動且永遠保持最新）

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](./README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **偏好在本地端 Clone？**

> 本儲存庫包含 50 多種語言的翻譯，因此下載大小會顯著增加。若要不包含翻譯內容地下載，請使用稀疏檢出功能：
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git
> cd AI-For-Beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> 這樣您可以快速下載完成課程所需的所有內容。
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**如果您希望支援其他翻譯語言，請參考 [此處](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md) 列出的語言。**

## 加入社群
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

## 你將學到什麼

**[課程心智圖](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

在本課程中，你將學習：

* 不同的人工智慧方法，包括使用 **知識表達** 和推理的「經典舊派」符號主義方法 ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence))。
* 作為現代 AI 核心的 **神經網路** 與 **深度學習**。我們將使用兩個最受歡迎框架 —— [TensorFlow](http://Tensorflow.org) 和 [PyTorch](http://pytorch.org) 的程式碼範例，來說明這些重要主題背後的概念。
* 運用於圖像與文本處理的 **神經架構**。將涵蓋近期模型，但可能未包含最新的尖端技術。
* 較不普及的 AI 方法，例如 **基因演算法** 與 **多代理系統**。

本課程不涵蓋：

> [在我們的 Microsoft Learn 系列中，找到本課程的所有額外資源](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)

* **AI 在商業**中的案例。建議參考 Microsoft Learn 的 [商業用戶 AI 入門](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) 課程路徑，或與 [INSEAD](https://www.insead.edu/) 合作開發的 [AI 商業學院](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum)。
* **經典機器學習**，詳細說明請參考我們的 [初學者機器學習課程](http://github.com/Microsoft/ML-for-Beginners)。
* 使用 **[認知服務](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)** 架設的實務 AI 應用。建議從 Microsoft Learn 的 [視覺](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum)、[自然語言處理](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum)、**[Generative AI with Azure OpenAI Service](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** 等模組開始。
* 具體的 ML **雲端框架**，如 [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum)、[Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum) 或 [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum)。可參考[使用 Azure Machine Learning 建構與營運機器學習解決方案](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum)及[使用 Azure Databricks 建構與營運機器學習解決方案](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum)課程路徑。
* **對話式 AI** 與 **聊天機器人**，另有 [建立對話式 AI 解決方案](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum) 專門課程，且可參考[此部落格文章](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/)詳細了解。
* 深入的 **深度學習數學理論**。推薦閱讀 Ian Goodfellow、Yoshua Bengio 與 Aaron Courville 所著的 [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618)，線上版也可在 [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/) 瀏覽。

欲輕鬆入門 _雲端 AI_ 可考慮學習 [Azure 人工智慧入門](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum) 路徑。

# 內容

|     |                                                                 課程連結                                                                 |                                           PyTorch/Keras/TensorFlow                                          | 實驗室                                                            |
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |
| 0  |                                 [課程設置](./lessons/0-course-setup/setup.md)                                 |                      [開發環境設定說明](./lessons/0-course-setup/how-to-run.md)                       |   |
| I  |               [**人工智慧導論**](./lessons/1-Intro/README.md)      | | |
| 01  |       [人工智慧簡介與歷史](./lessons/1-Intro/README.md)       |           -                            | -  |
| II |              **符號主義 AI**              |
| 02  |       [知識表示與專家系統](./lessons/2-Symbolic/README.md)       |            [專家系統](./lessons/2-Symbolic/Animals.ipynb) /  [本體論](./lessons/2-Symbolic/FamilyOntology.ipynb) /[概念圖](./lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |
| III |                        [**神經網路導論**](./lessons/3-NeuralNetworks/README.md) |||
| 03  |                [感知器](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [筆記本](./lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [實驗室](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 04  |                   [多層感知器與創建我們自己的框架](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [筆記本](./lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [實驗室](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 05  |            [框架介紹 (PyTorch/TensorFlow) 與過擬合](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](./lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](./lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [實驗室](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV  |            [**電腦視覺**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [在 Microsoft Azure 探索電腦視覺](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |
| 06  |            [電腦視覺入門. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [筆記本](./lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [實驗室](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 07  |            [卷積神經網路](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [CNN 架構](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](./lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](./lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [實驗室](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 08  |            [預訓練網絡和遷移學習](./lessons/4-ComputerVision/08-TransferLearning/README.md) 及 [訓練技巧](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](./lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [實驗室](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [自編碼器與變分自編碼器 (VAE)](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](./lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [生成對抗網絡 & 藝術風格轉換](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](./lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [物體偵測](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](./lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [實驗室](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [語義分割. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)             |  |
| V  |            [**自然語言處理**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [在 Microsoft Azure 探索自然語言處理](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [文本表示法. 词袋模型/Bow 及 TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [語義詞嵌入. Word2Vec 與 GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [語言建模. 訓練您自己的嵌入](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [實驗室](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [循環神經網路](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [生成循環網絡](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)             | [實驗室](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Transformer. BERT.](./lessons/5-NLP/18-Transformers/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [命名實體識別](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [實驗室](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [大型語言模型、提示程式設計與少量示例任務](./lessons/5-NLP/20-LangModels/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **其他 AI 技術** || |
| 21  |            [遺傳演算法](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [筆記本](./lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [深度強化學習](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](./lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](./lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [實驗室](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [多智能體系統](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **AI 倫理** | | |
| 24  |            [AI 倫理與負責任的人工智慧](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: 負責任的 AI 原則](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **額外資源** | | |
| 25  |            [多模態網絡、CLIP 與 VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [筆記本](./lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## 每堂課包含

* 預習資料
* 可執行的 Jupyter 筆記本，通常針對特定框架（**PyTorch** 或 **TensorFlow**）。該筆記本也包含大量理論內容，因此要理解主題，您至少需要完成其中一種版本的筆記本（PyTorch 或 TensorFlow）。
* 有些主題提供**實驗室**，讓您有機會嘗試將所學應用於特定問題。
* 部分章節含有鏈接至涵蓋相關主題的 [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) 模組。

## 開始前

### 🎯 AI 新手？ 從這裡開始！

如果您是 AI 完全新手，想要快速、實作範例，請查看我們的 [**初學者友善範例**](./examples/README.md)！這些範例包括：

- 🌟 **哈囉 AI 世界** - 您的第一個 AI 程式（模式識別）
- 🧠 **簡易神經網路** - 從零建造一個神經網路
- 🖼️ **圖像分類器** - 帶詳細註解的圖像分類器
- 💬 **文字情感分析** - 分析正面/負面文字

這些範例旨在幫助您在深入完整課程之前理解 AI 概念。

### 📚 完整課程設定

- 我們已建立一個[設定課程](./lessons/0-course-setup/setup.md)來協助您設定開發環境。 - 對教育工作者，我們也建立了[課程設定教學](./lessons/0-course-setup/for-teachers.md)！
- 如何在 VSCode 或 Codespace 中[執行程式碼](./lessons/0-course-setup/how-to-run.md)

請依照以下步驟操作：

分支此倉儲：點擊此頁右上角的「Fork」按鈕。

複製倉儲：`git clone https://github.com/microsoft/AI-For-Beginners.git`

別忘了給這個 repo 點星 (🌟)，以便日後更容易找到。

## 認識其他學習者

加入我們的[官方 AI Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum)，與其他修讀本課程的學習者交流並獲得支援。

如果在開發過程中有產品反饋或問題，請造訪我們的[Azure AI Foundry 開發者論壇](https://aka.ms/foundry/forum)

## 小測驗

> **關於小測驗的提醒**：所有小測驗都在 etc\quiz-app 的 Quiz-app 資料夾中，或於[線上查看](https://ff-quizzes.netlify.app/)。它們從課程內容中鏈接，測驗應用程式可以在本地執行或部署到 Azure；請依照 `quiz-app` 資料夾中的說明操作。這些內容正在逐步本地化中。

## 需要協助

您有建議或發現拼字或程式碼錯誤嗎？請提出議題或建立拉取請求。

## 特別感謝

* **✍️ 主要作者：** [Dmitry Soshnikov](http://soshnikov.com), PhD
* **🔥 編輯：** [Jen Looper](https://twitter.com/jenlooper), PhD
* **🎨 筆記插畫師：** [Tomomi Imura](https://twitter.com/girlie_mac)
* **✅ 小測驗創作者：** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)
* **🙏 核心貢獻者：** [Evgenii Pishchik](https://github.com/Pe4enIks)

## 其他課程

我們團隊還有其他課程！請查看：

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

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
 
### 核心學習
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

## 尋求協助

如果你遇到困難或者對開發 AI 應用有任何疑問，加入學習者與資深開發者的 MCP 討論群組吧。這是個支持性社群，歡迎提問並無私分享知識。

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

如果在開發過程中有產品反饋或錯誤，請造訪：

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：  
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於翻譯的準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議使用專業人工翻譯。對於因使用本翻譯而產生的任何誤解或錯誤詮釋，我們不承擔任何責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->