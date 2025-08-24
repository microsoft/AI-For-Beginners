<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3a6b0ddf7e6e3f33b2a543baf086dc9",
  "translation_date": "2025-08-24T21:40:38+00:00",
  "source_file": "README.md",
  "language_code": "hk"
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

# 初學者人工智能課程 - 課程大綱  

|![ 由 [(@girlie_mac)](https://twitter.com/girlie_mac) 繪製的手繪筆記 ](./lessons/sketchnotes/ai-overview.png)|  
|:---:|  
| 初學者人工智能 - _手繪筆記由 [@girlie_mac](https://twitter.com/girlie_mac) 繪製_ |  

透過我們為期 12 週、共 24 節課的課程，探索**人工智能**（AI）的世界！課程包括實用的教學、測驗和實驗室練習。這是一個適合初學者的課程，涵蓋了 TensorFlow 和 PyTorch 等工具，以及 AI 的倫理問題。  

## 你將學到什麼  

**[課程思維導圖](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**  

在這個課程中，你將學到：  

* 不同的人工智能方法，包括傳統的符號方法，使用**知識表示**和推理（[GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)）。  
* **神經網絡**和**深度學習**，這是現代 AI 的核心。我們將使用兩個最受歡迎的框架 [TensorFlow](http://Tensorflow.org) 和 [PyTorch](http://pytorch.org) 的代碼來說明這些重要主題背後的概念。  
* 用於處理圖像和文本的**神經架構**。我們將涵蓋一些近期的模型，但可能不包括最前沿的技術。  
* 不太流行的 AI 方法，例如**遺傳算法**和**多代理系統**。  

我們不會在這個課程中涵蓋：  

> [在 Microsoft Learn 集合中找到本課程的所有額外資源](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)  

* **AI 在商業中的應用案例**。建議參加 [Introduction to AI for business users](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) 的學習路徑，或 [AI Business School](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum)，這是與 [INSEAD](https://www.insead.edu/) 合作開發的。  
* **經典機器學習**，這在我們的 [Machine Learning for Beginners Curriculum](http://github.com/Microsoft/ML-for-Beginners) 中有詳細描述。  
* 使用 **[Cognitive Services](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)** 構建的實際 AI 應用。建議從 Microsoft Learn 的模組開始，例如 [vision](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum)、[natural language processing](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum)、**[Generative AI with Azure OpenAI Service](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** 等。  
* 特定的 ML **雲框架**，例如 [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum)、[Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum) 或 [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum)。建議參考 [Build and operate machine learning solutions with Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) 和 [Build and Operate Machine Learning Solutions with Azure Databricks](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum) 的學習路徑。  
* **對話式 AI** 和 **聊天機器人**。有一個單獨的 [Create conversational AI solutions](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum) 學習路徑，你也可以參考 [這篇博客文章](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) 獲取更多細節。  
* **深度學習的數學基礎**。建議參考 Ian Goodfellow、Yoshua Bengio 和 Aaron Courville 的 [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618)，該書也可以在線獲取：[https://www.deeplearningbook.org/](https://www.deeplearningbook.org/)。  

如果想要輕鬆入門 _雲端 AI_ 主題，可以考慮參加 [Get started with artificial intelligence on Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum) 的學習路徑。  

# 課程內容  

|     |                                                                 課程連結                                                                  |                                           PyTorch/Keras/TensorFlow                                          | 實驗室                                                            |  
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |  
| 0  |                                 [課程設置](./lessons/0-course-setup/setup.md)                                 |                      [設置開發環境](./lessons/0-course-setup/how-to-run.md)                       |   |  
| I  |               [**AI 簡介**](./lessons/1-Intro/README.md)      | | |  
| 01  |       [AI 的簡介與歷史](./lessons/1-Intro/README.md)       |           -                            | -  |  
| II |              **符號 AI**              |  
| 02  |       [知識表示與專家系統](./lessons/2-Symbolic/README.md)       |            [專家系統](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) /  [本體論](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) /[概念圖](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |  
| III |                        [**神經網絡簡介**](./lessons/3-NeuralNetworks/README.md) |||  
| 03  |                [感知器](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [實驗室](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |  
| 04  |                   [多層感知器與創建我們自己的框架](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [實驗室](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |  
| 05  |            [框架簡介 (PyTorch/TensorFlow) 與過擬合](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [實驗室](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |  
| IV  |            [**計算機視覺**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [探索 Microsoft Azure 上的計算機視覺](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |  
| 06  |            [計算機視覺簡介. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [實驗室](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |  
| 07  |            [卷積神經網絡](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [CNN 架構](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [實驗室](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |  
| 08  |            [預訓練網絡與遷移學習](./lessons/4-ComputerVision/08-TransferLearning/README.md) 和 [訓練技巧](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [實驗室](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [自編碼器與變分自編碼器 (VAEs)](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [生成對抗網絡 (GANs) 與藝術風格遷移](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [物件檢測](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [實驗室](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [語義分割. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](../../(https:/github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb))             |  |
| V  |            [**自然語言處理**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [在 Microsoft Azure 上探索自然語言處理](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [文本表示. Bow/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [語義詞嵌入. Word2Vec 和 GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [語言建模. 訓練自己的嵌入](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [實驗室](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [循環神經網絡 (RNN)](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [生成型循環網絡](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.md) / [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.md)             | [實驗室](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [變壓器. BERT.](./lessons/5-NLP/18-Transformers/READMEtransformers.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [命名實體識別 (NER)](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [實驗室](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [大型語言模型、提示編程與少樣本任務](./lessons/5-NLP/20-LangModels/READMELargeLang.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **其他 AI 技術** || |
| 21  |            [遺傳算法](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [深度強化學習](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [實驗室](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [多代理系統](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **AI 倫理** | | |
| 24  |            [AI 倫理與負責任的 AI](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: 負責任的 AI 原則](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **附加內容** | | |
| 25  |            [多模態網絡、CLIP 和 VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## 每節課包含

* 預讀材料  
* 可執行的 Jupyter Notebook，通常針對特定框架（**PyTorch** 或 **TensorFlow**）。可執行的 Notebook 也包含大量理論材料，因此要理解主題，您需要至少閱讀一個版本的 Notebook（PyTorch 或 TensorFlow）。  
* **實驗室**（部分主題提供），讓您有機會將所學材料應用於特定問題。  
* 部分章節包含指向 [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) 模組的鏈接，涵蓋相關主題。

## 開始學習

- 我們已經創建了一個 [設置課程](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/0-course-setup/setup.md)，幫助您設置開發環境。  
- 對於教育工作者，我們還創建了一個 [課程設置指南](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/0-course-setup/for-teachers.md)！  
- 如何 [在 VSCode 或 Codepace 中運行代碼](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/0-course-setup/how-to-run.md)

按照以下步驟操作：

Fork 此倉庫：點擊此頁面右上角的 "Fork" 按鈕。

克隆此倉庫：`git clone https://github.com/microsoft/AI-For-Beginners.git`

別忘了給這個倉庫加星標 (🌟)，以便日後更容易找到。

## 與其他學習者交流

加入我們的 [官方 AI Discord 伺服器](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum)，與其他學習者交流並獲得支持。

如果您在構建過程中有產品反饋或問題，請訪問我們的 [Azure AI Foundry 開發者論壇](https://aka.ms/foundry/forum)

## 測驗
> **關於測驗的注意事項**：所有測驗都存放在 Quiz-app 資料夾內，路徑為 etc\quiz-app。這些測驗已經從課程中連結起來，測驗應用程式可以在本地執行，或者部署到 Azure；請按照 `quiz-app` 資料夾中的指引操作。測驗內容正在逐步進行本地化。
## 尋求協助

有任何建議或發現拼寫或程式碼錯誤？請提出問題或建立拉取請求。

## 特別感謝

* **✍️ 主要作者：** [Dmitry Soshnikov](http://soshnikov.com)，博士
* **🔥 編輯：** [Jen Looper](https://twitter.com/jenlooper)，博士
* **🎨 手繪筆記插畫師：** [Tomomi Imura](https://twitter.com/girlie_mac)
* **✅ 測驗創作者：** [Lateefah Bello](https://github.com/CinnamonXI)，[MLSA](https://studentambassadors.microsoft.com/)
* **🙏 核心貢獻者：** [Evgenii Pishchik](https://github.com/Pe4enIks)

## 其他課程

我們的團隊還製作了其他課程！查看以下內容：

- [初學者的生成式 AI](https://aka.ms/genai-beginners)
- [初學者的生成式 AI .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [使用 JavaScript 的生成式 AI](https://github.com/microsoft/generative-ai-with-javascript)
- [使用 Java 的生成式 AI](https://github.com/microsoft/Generative-AI-for-beginners-java)
- [初學者的 AI](https://aka.ms/ai-beginners)
- [初學者的數據科學](https://aka.ms/datascience-beginners)
- [初學者的機器學習](https://aka.ms/ml-beginners)
- [初學者的網絡安全](https://github.com/microsoft/Security-101) 
- [初學者的網頁開發](https://aka.ms/webdev-beginners)
- [初學者的物聯網](https://aka.ms/iot-beginners)
- [初學者的 XR 開發](https://github.com/microsoft/xr-development-for-beginners)
- [精通 GitHub Copilot 用於代理性使用](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
- [精通 GitHub Copilot 用於 C#/.NET 開發者](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)
- [選擇你的 Copilot 冒險](https://github.com/microsoft/CopilotAdventures)

**免責聲明**：  
本文件使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。