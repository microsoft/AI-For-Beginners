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

# 人工智能入門——課程大綱

|![素描筆記作者[(@girlie_mac)](https://twitter.com/girlie_mac) ](./lessons/sketchnotes/ai-overview.png)|
|:---:|
| 人工智能入門 - _素描筆記作者[@girlie_mac](https://twitter.com/girlie_mac)_ |

微軟Azure Cloud很榮幸為您提供一門**人工智能**課程，本課為期12週，共24課時。

您將在本課程學到：

* 不同的人工智能方法，包括傳統的符號推理方法，它擁有**知識再現**和推理能力。([符號人工智能](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
* **神經網絡**與**深度學習**是現代人工智能的核心。我們會利用兩個最流行的框架[TensorFlow](http://Tensorflow.org)和[PyTorch](http://pytorch.org)來解釋背後的重要概念。
* 用於處理圖像和文本的**神經結構**。雖然未必會跟上最新的發展，但我們的介紹會涵蓋近期的模型。
* 其他較不流行的人工智能方法，例如**遺傳算法**和**多智能體系統**.

本課程將不涉及：

* **商業使用AI**的案例。如對該題目有興趣，可考慮參加Microsoft Learn的[人工智能商業應用入門](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-cacaste)或者[AI商學院](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-cacaste)，該課程與INSEAD合作開發[INSEAD](https://www.insead.edu/)。
* **經典機器學習**。本題目在[機器學習入門課程](http://github.com/Microsoft/ML-for-Beginners)中有所涵蓋。
* 利用**[認知服務](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-cacaste)**構建的人工智能應用程序。該題目可通過Microsoft Learn的[視覺處理](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-cacaste)和[自然語言處理](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-cacaste)等課程學習。
* 特定的機器學習**雲框架**，例如[Azure機器學習](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste)或[Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-cacaste)。建議學習[使用Azure Machine Learning構建和運營機器學習解決方案](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-cacaste)和[使用Azure Databricks構建和運營機器學習解決方案](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-cacaste)課程。
* 對於**對話式人工智能**和**聊天機器人**的題目，請參考[創建對話式人工智能](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-cacaste)課程，請參考這篇[文章](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/)獲取更多信息。
* 深度學習背後的**深度數學**。我們推薦閱讀Ian Goodfellow，Yoshua Bengio和Aaron Courville合著的[深度學習](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618)一書，本書可在[https://www.deeplearningbook.org/](https://www.deeplearningbook.org/)在線閱讀。

對於*AI雲計算*的簡介，您可以參加[Azure上的人工智能之旅](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-cacaste)課程。

---
# 課程內容

<table>
<tr><th>編號</th><th>課程</th><th>摘要</th><th>PyTorch</th><th>Keras/TensorFlow</th><th>練習</th></tr>

<tr><td>I</td><td colspan="4"><b>AI簡介</b></td><td></td></tr>
<tr><td>1</td><td>AI的簡介與歷史</td><td><a href="lessons/1-Intro/README.md">Text</a></td><td></td><td></td><td></td></tr>

<tr><td>II</td><td colspan="4"><b>符號人工智能</b></td><td></td></tr>
<tr><td>2 </td><td>知識再現與專家系統</td><td><a href="lessons/2-Symbolic/README.md">Text</a></td><td colspan="2"><a href="lessons/2-Symbolic/Animals.ipynb">專家系統</a>, <a href="lessons/2-Symbolic/FamilyOntology.ipynb">本體論</a>, <a href="lessons/2-Symbolic/MSConceptGraph.ipynb">概念圖</a></td><td></td></tr>
<tr><td>III</td><td colspan="4"><b><a href="lessons/3-NeuralNetworks/README.md">神經網絡簡介</a></b></td><td></td></tr>
<tr><td>3</td><td>感知器</td>
   <td><a href="lessons/3-NeuralNetworks/03-Perceptron/README.md">Text</a>
   <td colspan="2"><a href="lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb">Notebook</a></td><td><a href="lessons/3-NeuralNetworks/03-Perceptron/lab/README.md">Lab</a></td></tr>
<tr><td>4 </td><td>多層感知器與框架構建</td><td><a href="lessons/3-NeuralNetworks/04-OwnFramework/README.md">Text</a></td><td colspan="2"><a href="lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb">Notebook</a><td><a href="lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md">Lab</a></td></tr> 
<tr><td>5</td>
   <td>框架簡介(PyTorch/TensorFlow)<br/>過度擬合</td>
   <td><a href="lessons/3-NeuralNetworks/05-Frameworks/README.md">Text</a><br/><a href="lessons/3-NeuralNetworks/05-Frameworks/Overfitting.md">Text</a></td>
   <td><a href="lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb">PyTorch</a></td>
   <td><a href="lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb">Keras</a>/<a href="lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb">TensorFlow</a></td>
   <td><a href="lessons/3-NeuralNetworks/05-Frameworks/lab/README.md">Lab</a></td></tr>
<tr><td>IV</td><td><b><a href="lessons/4-ComputerVision/README.md">電腦視覺</a></b></td>
  <td colspan="3"><a href="https://docs.microsoft.com/learn/paths/explore-computer-vision-microsoft-azure/?WT.mc_id=academic-77998-cacaste"><i>AI基礎知識：探索電腦視覺</i></a></td>
  <td></td></tr>
<tr><td></td><td colspan="2"><i>Microsoft電腦視覺學習模塊</i></td>
  <td><a href="https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste"><i>PyTorch</i></a></td>
  <td><a href="https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste"><i>TensorFlow</i></a></td>
  <td></td></tr>
<tr><td>6</td><td>電腦視覺入門OpenCV</td><td><a href="lessons/4-ComputerVision/06-IntroCV/README.md">Text</a><td colspan="2"><a href="lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb">Notebook</a></td><td><a href="lessons/4-ComputerVision/06-IntroCV/lab/README.md">Lab</a></td></tr>
<tr><td>7</td><td>卷積神經網絡<br/>CNN架構</td><td><a href="lessons/4-ComputerVision/07-ConvNets/README.md">Text</a><br/><a href="lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md">Text</a></td><td><a href="lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb">TensorFlow</a></td><td><a href="lessons/4-ComputerVision/07-ConvNets/lab/README.md">Lab</a></td></tr>
<tr><td>8</td><td>預訓練網絡和遷移學習<br/>訓練技巧</td><td><a href="lessons/4-ComputerVision/08-TransferLearning/README.md">Text</a><br/><a href="lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md">Text</a></td><td><a href="lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb">TensorFlow</a><br/><a href="lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb">隨機失活樣本</a><br/><a href="lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb">對抗性貓貓</a></td><td><a href="lessons/4-ComputerVision/08-TransferLearning/lab/README.md">Lab</a></td></tr>
<tr><td>9</td><td>自動編碼器和變分自動編碼器（VAE）</td><td><a href="lessons/4-ComputerVision/09-Autoencoders/README.md">Text</a></td><td><a href="lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb">TensorFlow</a></td><td></td></tr>
<tr><td>10</td><td>生成式對抗網絡<br/>藝術風格遷移</td><td><a href="lessons/4-ComputerVision/10-GANs/README.md">Text</a></td><td><a href="lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb">PyTorch</td><td><a href="lessons/4-ComputerVision/10-GANs/GANTF.ipynb">TensorFlow GAN</a><br/><a href="lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb">風格遷移</a></td><td></td></tr>
<tr><td>11</td><td>目標檢測</td><td><a href="lessons/4-ComputerVision/11-ObjectDetection/README.md">Text</a></td><td>PyTorch</td><td><a href="lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb">TensorFlow</td><td><a href="lessons/4-ComputerVision/11-ObjectDetection/lab/README.md">Lab</a></td></tr>
<tr><td>12</td><td>語義分割U-Net</td><td><a href="lessons/4-ComputerVision/12-Segmentation/README.md">Text</a></td><td><a href="lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb">PyTorch</td><td><a href="lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb">TensorFlow</td><td></td></tr>
<tr><td>V</td><td><b><a href="lessons/5-NLP/README.md">自然語言處理</a></b></td>
   <td colspan="3"><a href="https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-cacaste"><i>AI基礎知識：探索自然語言處理</i></a></td>
   <td></td></tr>
<tr><td></td><td colspan="2"><i>Microsoft Learn Module自然語言處理</i></td>
   <td><a href="https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste"><i>PyTorch</i></a></td>
   <td><a href="https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste"><i>TensorFlow</i></a></td>
   <td></td></tr>
<tr><td>13</td><td>文本表示——詞袋模型/TF-IDF</td><td><a href="lessons/5-NLP/13-TextRep/README.md">Text</a></td><td><a href="lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb">TensorFlow</td><td></td></tr>
<tr><td>14</td><td>語義詞嵌入——Word2Vec和GloVe</td><td><a href="lessons/5-NLP/14-Embeddings/README.md">Text</td><td><a href="lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb">TensorFlow</a></td><td></td></tr>
<tr><td>15</td><td>語言建模——訓練你的詞嵌入模型</td><td><a href="lessons/5-NLP/15-LanguageModeling/README.md">Text</a></td><td><a href="lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb">PyTorch</a></td><td><a href="lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb">TensorFlow</a></td><td><a href="lessons/5-NLP/15-LanguageModeling/lab/README.md">Lab</a></td></tr>
<tr><td>16</td><td>遞歸神經網絡</td><td><a href="lessons/5-NLP/16-RNN/README.md">Text</a></td><td><a href="lessons/5-NLP/16-RNN/RNNPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/5-NLP/16-RNN/RNNTF.ipynb">TensorFlow</a></td><td></td></tr>
<tr><td>17</td><td>生成式遞歸網絡</td><td><a href="lessons/5-NLP/17-GenerativeNetworks/README.md">Text</a></td><td><a href="lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.md">PyTorch</a></td><td><a href="lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.md">TensorFlow</a></td><td><a href="lessons/5-NLP/17-GenerativeNetworks/lab/README.md">Lab</a></td></tr>
<tr><td>18</td><td>Transformers與BERT</td><td><a href="lessons/5-NLP/18-Transformers/README.md">Text</a></td><td><a href="lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/5-NLP/18-Transformers/TransformersTF.ipynb">TensorFlow</a></td><td></td></tr>
<tr><td>19</td><td>命名體識別</td><td><a href="lessons/5-NLP/19-NER/README.md">Text</a></td><td></td><td><a href="lessons/5-NLP/19-NER/NER-TF.ipynb">TensorFlow</a></td><td><a href="lessons/5-NLP/19-NER/lab/README.md">Lab</a></td></tr>
<tr><td>20</td><td>大型語言模型、提示編程和少樣本任務</td><td><a href="lessons/5-NLP/20-LangModels/README.md">Text</a></td><td><a href="lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb">PyTorch</td><td></td><td></td></tr>
<tr><td>VI</td><td colspan="4"><b>其他AI技術</b></td><td></td></tr>
<tr><td>21</td><td>遺傳算法</td><td><a href="lessons/6-Other/21-GeneticAlgorithms/README.md">Text</a><td colspan="2"><a href="lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb">Notebook</a></td><td></td></tr>
<tr><td>22</td><td>深度強化學習</td><td><a href="lessons/6-Other/22-DeepRL/README.md">Text</a></td><td><a href="lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb">PyTorch</a></td><td><a href="lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb">TensorFlow</a></td><td><a href="lessons/6-Other/22-DeepRL/lab/README.md">Lab</a></td></tr>
<tr><td>23</td><td>多智能體系統</td><td><a href="lessons/6-Other/23-MultiagentSystems/README.md">Text</a></td><td></td><td></td><td></td></tr>
<tr><td>VII</td><td colspan="4"><b>AI倫理</b></td><td></td></tr>
<tr><td>24</td><td>AI倫理和負責任的人工智能</td><td><a href="lessons/7-Ethics/README.md">Text</a></td><td colspan="2"><a href="https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste"><i>MS Learn：負責任的人工智能原則</i></a></td><td></td></tr>
<tr><td></td><td colspan="4"><b>Extras</b></td><td></td></tr>
<tr><td>X1</td><td>多智能體系統CLIP與VQGAN</td><td><a href="lessons/X-Extras/X1-MultiModal/README.md">Text</a></td><td colspan="2"><a href="lessons/X-Extras/X1-MultiModal/Clip.ipynb">Notebook</a></td><td></td></tr>
</table>

**[課程思維導圖](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

每堂課程都包含一些預讀材料（如以上**文字**上的鏈接），有些課程包含可在Jupyter Notebooks上執行的程序，通常是通過**PyTorch**或 **TensorFlow**的框架執行。Notebook中也含有大量理論材料，為了讓你充分理解學習內容，請至少學習一個notebook中的代碼。有些主題還有**Labs**實驗室，你可以將學到的知識運用到實際問題上。

一些章節還包括了**MS Learn**的相關學習鏈接。Microsoft Learn為大家提供了擁有GPU運算的環境，為本課程的深入學習提供便利條件。

# 你是學生嗎？

請通過以下鏈接獲取資源：

- [學生中心頁面](https://docs.microsoft.com/learn/student-hub?WT.mc_id=academic-77998-cacaste)本頁提供初學者資源、學生資料和如何免費獲得證書的方法。本頁面每個月都會有更新，請不時檢查本頁。
- [微軟學生大使](https://studentambassadors.microsoft.com?WT.mc_id=academic-77998-cacaste)加入由全球學生大使組成的全球社區，這可能是你加入微軟的起點。

# 開始學習

**學生注意事項**：本課程有幾種學習方法，你可以在GitHub上閱讀教學內容和代碼。如果你想運行代碼，請參考[說明](./etc/how-to-run.md)並在此[文章](https://soshnikov.com/education/how-to-execute-notebooks-from-github/)中找到更多運行程序的建議。

> **注意**: [關於如何運行本課程中代碼的說明](./etc/how-to-run.md)

如果你想自學本課程，我們建議你把整個repo複製到自己的GitHub賬戶自學或者與你的團隊一起學習，完成練習。

- 由課前測驗開始
- 閱讀課程簡介 
- 如果講座有額外的notebook，請仔細閱讀代碼並試著執行。如果notebook同時含有TensorFlow和PyTorch框架，你可以選擇一個來執行
- Notebooks通常含有一些小挑戰，你需要稍微調整代碼來試驗
- 參加課後測驗
- 如果課程後面帶有Lab實驗室，請完成實驗室作業
- 請訪問[討論區](https://github.com/microsoft/AI-For-Beginners/discussions)參加討論
- 你可以在[Gitter](https://gitter.im/Microsoft/ai-for-beginners)上或[Telegram頻道](http://t.me/ai_for_beginners)上與其他學生交流

> 如果你想進一步學習，我們推薦[Microsoft Learn](https://docs.microsoft.com/en-us/users/dmitrysoshnikov-9132/collections/31zgizg2p418yo/?WT.mc_id=academic-77998-cacaste)裡面的課程。

**老師注意事項**：我們在此提供了一些教學[建議](/etc/for-teachers.md)。

---

## 貢獻者

**✍️ 主要作者：** [Dmitry Soshnikov](http://soshnikov.com), PhD <br/>
**🔥 編輯：** [Jen Looper](https://twitter.com/jenlooper), PhD <br/>
**🎨 手繪插圖：** [Tomomi Imura](https://twitter.com/girlie_mac) <br/>
**✅ 小測驗作者：** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)  <br/>
**🙏 核心貢獻者：** [Evgenii Pishchik](https://github.com/Pe4enIks) 

## 團隊介紹

[![宣傳短片](/lessons/sketchnotes/ai-for-beginners.png)](https://youtu.be/m2KrAk0cC1c "宣傳短片")

> 🎥 點擊圖片觀看本課程開發者的短片！

---

## 教學法

我們在設計本課程時，課程包含實用性很強的**案例實踐**以及**頻繁的小測驗**。

為保證課程對學生的吸引力，並忠實保留概念的含義，我們力求課程與實踐相輔相成。另外，課前輕鬆小測驗預告了本次學習的主題與範疇，第二個小測驗則繼續吸引學生。本課程的設計盡量做到靈活有趣，可以完整學習也可學習部分內容。不同案例隨著12個星期的學習由淺入深。

> 這裡是[行為準則](etc/CODE_OF_CONDUCT.md)，[貢獻指南](etc/CONTRIBUTING.md)和[翻譯指南](etc/TRANSLATIONS.md)。以及[說明文件](etc/SUPPORT.md)和[安全信息](etc/SECURITY.md)。我們歡迎您的建設性反饋！

> **小測驗說明**: 所有測驗包含在這個[應用程序](https://red-field-0a6ddfd03.1.azurestaticapps.net/)中，共50個小測驗，每個小測驗有三個問題。課程內有小測驗的鏈接，您亦可在本地運行測驗，具體操作請按照`etc/quiz-app`文件夾中說明操作。

## 離線學習

您可以使用[Docsify](https://docsify.js.org/#/)來離線運行本文檔。請首先將本repo分叉（fork），之後在本地電腦[安裝Docsify](https://docsify.js.org/#/quickstart)，最後在repo的`etc/docsify`文件夾輸入`docsify serve`。本文檔將在本地主機的3000端口提供服務`localhost:3000`。此外本課程的PDF版本可在[此鏈接](/etc/pdf/readme.pdf)獲取。

## 我們需要你的幫助！

你想貢獻這一課程的翻譯並分享給更多的人嗎？請參考[翻譯指南](etc/TRANSLATIONS.md)。

## 其他課程

我們的團隊還製作了其他課程！請往：

- [網絡開發入門](https://aka.ms/webdev-beginners)
- [物聯網入門](https://aka.ms/iot-beginners)
- [機器學習入門](https://aka.ms/ml-beginners)
- [數據科學入門](https://aka.ms/datascience-beginners)
