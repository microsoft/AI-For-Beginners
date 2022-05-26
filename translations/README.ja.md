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

# 初心者のための人工知能 カリキュラム

|![ Sketchnote by [(@girlie_mac)](https://twitter.com/girlie_mac) ](../lessons/sketchnotes/ai-overview.png)|
|:---:|
| AI For Beginners - _Sketchnote by [@girlie_mac](https://twitter.com/girlie_mac)_ |

マイクロソフトのAzure Cloud Advocateは、12週間、24レッスンの人工知能に関するカリキュラムを提供します。

このカリキュラムでは、以下のことを学びます。

* **知識表現**と推論（GOFAI）による「古き良き」記号的アプローチを含む、人工知能へのさまざまなアプローチ。
* 現代のAIの中核をなす**ニューラルネットワーク**と**ディープラーニング**。これらの重要なトピックの背後にある概念を、最も人気のある2つのフレームワークであるTensorFlowとPyTorchのコードを使用して説明します。
* 画像やテキストを扱うための**ニューラル・アーキテクチャ**。最近のモデルを取り上げますが、最先端技術については少し不足する可能性があります。
* **遺伝的アルゴリズム**や**マルチエージェントシステム**など、あまり一般的ではないAIアプローチ。

本カリキュラムで扱わない内容

* **AIをビジネスで活用するためのビジネスケース**。Microsoft Learnの学習パス[ビジネスユーザーのためのAI入門](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-57639-dmitryso)や、[INSEAD](https://www.insead.edu/)と共同で開発した[AIビジネススクール](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-57639-dmitryso)の受講をご検討ください。
* **古典的な機械学習**については、[初心者のための機械学習カリキュラム](http://github.com/Microsoft/ML-for-Beginners)で十分に説明されています。
* **[Cognitive Services](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-57639-dmitryso)** を利用して構築された実践的なAIアプリケーション。これには、Microsoft Learnの[ビジョン](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-57639-dmitryso)、[自然言語処理](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-57639-dmitryso)などのモジュールから始めることをお勧めします。
* [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-57639-dmitryso) や [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-57639-dmitryso) などの特定のML **Cloud Frameworks** を利用する [Azure Machine Learning による機械学習ソリューションの構築と運用](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-57639-dmitryso)、[Azure Databricksによる機械学習ソリューションの構築と運用](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-57639-dmitryso) の学習パスの利用を検討します。
* **会話型AI**と**Chat Bots**。別途、[Create conversational AI solutions](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-57639-dmitryso) という学習パスがあり、詳しくは[こちらのブログ](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) も参照してください。
* **ディープラーニングの背後にある深層数学**。これについては、Ian Goodfellow、Yoshua Bengio、Aaron Courvilleによる[Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618)をお勧めします。また、[https://www.deeplearningbook.org/](https://www.deeplearningbook.org/) で公開されています。

クラウドにおける*AI*のトピックを優しく紹介するために、[Get started with artificial intelligence on Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-57639-dmitryso) Learning Pathの受講を検討してもよいでしょう。

---
# コンテンツ

<table>
<tr><th>No</th><th>Lesson</th><th>Intro</th><th>PyTorch</th><th>Keras/TensorFlow</th><th>Lab</th></tr>

<tr><td>I</td><td colspan="4"><b>AI入門</b></td><td></td></tr>
<tr><td>1</td><td>Introduction and History of AI</td><td><a href="lessons/1-Intro/translations/README.ja.md">Text</a></td><td></td><td></td><td></td></tr>

<tr><td>II</td><td colspan="4"><b>シンボリックAI</b></td><td></td></tr>
<tr><td>2 </td><td>Knowledge Representation and Expert Systems</td><td><a href="lessons/2-Symbolic/README.md">Text</a></td><td colspan="2"><a href="lessons/2-Symbolic/Animals.ipynb">Expert System</a>, <a href="lessons/2-Symbolic/FamilyOntology.ipynb">Ontology</a>, <a href="lessons/2-Symbolic/MSConceptGraph.ipynb">Concept Graph</a></td><td></td></tr>
<tr><td>III</td><td colspan="4"><b><a href="lessons/3-NeuralNetworks/README.md">ニューラルネットワーク入門</a></b></td><td></td></tr>
<tr><td>3</td><td>Perceptron</td>
   <td><a href="lessons/3-NeuralNetworks/03-Perceptron/README.md">Text</a>
   <td colspan="2"><a href="lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb">Notebook</a></td><td><a href="lessons/3-NeuralNetworks/03-Perceptron/lab/README.md">Lab</a></td></tr>
<tr><td>4 </td><td>Multi-Layered Perceptron and Creating our own Framework</td><td><a href="lessons/3-NeuralNetworks/04-OwnFramework/README.md">Text</a></td><td colspan="2"><a href="lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb">Notebook</a><td><a href="lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md">Lab</a></td></tr> 
<tr><td>5</td>
   <td>Intro to Frameworks (PyTorch/TensorFlow)<br/>Overfitting</td>
   <td><a href="lessons/3-NeuralNetworks/05-Frameworks/README.md">Text</a><br/><a href="lessons/3-NeuralNetworks/05-Frameworks/Overfitting.md">Text</a></td>
   <td><a href="lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb">PyTorch</td>
   <td><a href="lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.md">Keras/TensorFlow</td>
   <td><a href="lessons/3-NeuralNetworks/05-Frameworks/lab/README.md">Lab</a></td></tr>
<tr><td>IV</td><td><b><a href="lessons/4-ComputerVision/README.md">コンピュータビジョン</a></b></td>
  <td colspan="3"><a href="https://docs.microsoft.com/learn/paths/explore-computer-vision-microsoft-azure/?WT.mc_id=academic-57639-dmitryso"><i>AI Fundamentals: Explore Computer Vision</i></a></td>
  <td></td></tr>
<tr><td></td><td colspan="2"><i>Microsoft Learn Module on Computer Vision</i></td>
  <td><a href="https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-57639-dmitryso"><i>PyTorch</i></a></td>
  <td><a href="https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-57639-dmitryso"><i>TensorFlow</i></a></td>
  <td></td></tr>
<tr><td>6</td><td>Intro to Computer Vision. OpenCV</td><td><a href="lessons/4-ComputerVision/06-IntroCV/README.md">Text</a><td colspan="2"><a href="lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb">Notebook</a></td><td><a href="lessons/4-ComputerVision/06-IntroCV/lab/README.md">Lab</a></td></tr>
<tr><td>7</td><td>Convolutional Neural Networks<br/>CNN Architectures</td><td><a href="lessons/4-ComputerVision/07-ConvNets/README.md">Text</a><br/><a href="lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md">Text</a></td><td><a href="lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb">TensorFlow</a></td><td><a href="lessons/4-ComputerVision/07-ConvNets/lab/README.md">Lab</a></td></tr>
<tr><td>8</td><td>Pre-trained Networks and Transfer Learning<br/>Training Tricks</td><td><a href="lessons/4-ComputerVision/08-TransferLearning/README.md">Text</a><br/><a href="lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md">Text</a></td><td><a href="lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb">TensorFlow</a><br/><a href="lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb">Dropout sample</a></td><td><a href="lessons/4-ComputerVision/08-TransferLearning/lab/README.md">Lab</a></td></tr>
<tr><td>9</td><td>Autoencoders and VAEs</td><td><a href="lessons/4-ComputerVision/09-Autoencoders/README.md">Text</a></td><td><a href="lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPytorch.ipynb">PyTorch</td><td><a href="lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb">TensorFlow</a></td><td></td></tr>
<tr><td>10</td><td>Generative Adversarial Networks<br/>Artistic Style Transfer</td><td><a href="lessons/4-ComputerVision/10-GANs/README.md">Text</a></td><td><a href="lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb">PyTorch</td><td><a href="lessons/4-ComputerVision/10-GANs/GANTF.ipynb">TensorFlow GAN</a><br/><a href="lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb">Style Transfer</a></td><td></td></tr>
<tr><td>11</td><td>Object Detection</td><td><a href="lessons/4-ComputerVision/11-ObjectDetection/README.md">Text</a></td><td>PyTorch</td><td><a href="lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection-TF.ipynb">TensorFlow</td><td><a href="lessons/4-ComputerVision/11-ObjectDetection/lab/README.md">Lab</a></td></tr>
<tr><td>12</td><td>Semantic Segmentation. U-Net</td><td><a href="lessons/4-ComputerVision/12-Segmentation/README.md">Text</a></td><td><a href="lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb">PyTorch</td><td><a href="lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb">TensorFlow</td><td></td></tr>
<tr><td>V</td><td><b><a href="lessons/5-NLP/README.md">自然言語処理</a></b></td>
   <td colspan="3"><a href="https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-57639-dmitryso"><i>AI Fundamentals: Explore Natural Language Processing</i></a></td>
   <td></td></tr>
<tr><td></td><td colspan="2"><i>Microsoft Learn Module on Natural Language</i></td>
   <td><a href="https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-57639-dmitryso"><i>PyTorch</i></a></td>
   <td><a href="https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-57639-dmitryso"><i>TensorFlow</i></a></td>
   <td></td></tr>
<tr><td>13</td><td>Text Representation. Bow/TF-IDF</td><td><a href="lessons/5-NLP/13-TextRep/README.md">Text</a></td><td><a href="lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb">TensorFlow</td><td></td></tr>
<tr><td>14</td><td>Semantic word embeddings. Word2Vec and GloVe</td><td><a href="lessons/5-NLP/14-Embeddings/README.md">Text</td><td><a href="lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb">TensorFlow</a></td><td></td></tr>
<tr><td>15</td><td>Language Modeling. Training your own embeddings</td><td><a href="lessons/5-NLP/15-LanguageModeling/README.md">Text</a></td><td></td><td><a href="lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb">TensorFlow</a></td><td><a href="lessons/5-NLP/15-LanguageModeling/lab/README.md">Lab</a></td></tr>
<tr><td>16</td><td>Recurrent Neural Networks</td><td><a href="lessons/5-NLP/16-RNN/README.md">Text</a></td><td><a href="lessons/5-NLP/16-RNN/RNNPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/5-NLP/16-RNN/RNNTF.ipynb">TensorFlow</a></td><td></td></tr>
<tr><td>17</td><td>Generative Recurrent Networks</td><td><a href="lessons/5-NLP/17-GenerativeNetworks/README.md">Text</a></td><td><a href="lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.md">PyTorch</a></td><td><a href="lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.md">TensorFlow</a></td><td><a href="lessons/5-NLP/17-GenerativeNetworks/lab/README.md">Lab</a></td></tr>
<tr><td>18</td><td>Transformers. BERT.</td><td><a href="lessons/5-NLP/18-Transformers/README.md">Text</a></td><td><a href="lessons/5-NLP/18-Transformers/TransformersPyTorch.md">PyTorch</a></td><td><a href="lessons/5-NLP/18-Transformers/TransformersTF.md">TensorFlow</a></td><td></td></tr>
<tr><td>19</td><td>Named Entity Recognition</td><td><a href="lessons/5-NLP/19-NER/README.md">Text</a></td><td></td><td><a href="lessons/5-NLP/19-NER/NER-TF.ipynb">TensorFlow</a></td><td><a href="lessons/5-NLP/19-NER/lab/README.md">Lab</a></td></tr>
<tr><td>20</td><td>Large Language Models, Prompt Programming and Few-Shot Tasks</td><td><a href="lessons/5-NLP/20-LangModels/README.md">Text</a></td><td><a href="lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb">PyTorch</td><td></td><td></td></tr>
<tr><td>VI</td><td colspan="4"><b>その他のAI技術</b></td><td></td></tr>
<tr><td>21</td><td>Genetic Algorithms</td><td><a href="lessons/6-Other/21-GeneticAlgorithms/README.md">Text</a><td colspan="2"><a href="lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb">Notebook</a></td><td></td></tr>
<tr><td>22</td><td>Deep Reinforcement Learning</td><td><a href="lessons/6-Other/22-DeepRL/README.md">Text</a></td><td></td><td><a href="lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb">TensorFlow</td><td><a href="lessons/6-Other/22-DeepRL/lab/README.md">Lab</a></td></tr>
<tr><td>23</td><td>Multi-Agent Systems</td><td><a href="lessons/6-Other/23-MultiagentSystems/README.md">Text</a></td><td></td><td></td><td></td></tr>
<tr><td>VII</td><td colspan="4"><b>AI倫理</b></td><td></td></tr>
<tr><td>24</td><td>AI Ethics and Responsible AI</td><td><a href="lessons/7-Ethics/README.md">Text</a></td><td colspan="2"><a href="https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-57639-dmitryso"><i>MS Learn: Responsible AI Principles</i></a></td><td></td></tr>
<tr><td></td><td colspan="4"><b>Extras</b></td><td></td></tr>
<tr><td>X1</td><td>Multi-Modal Networks, CLIP and VQGAN</td><td><a href="lessons/X-Extras/X1-MultiModal/README.md">Text</a></td><td colspan="2"><a href="lessons/X-Extras/X1-MultiModal/Clip.ipynb">Notebook</a></td><td></td></tr>
</table>

**[Mindmap of the Course](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

各レッスンには、事前に読むべき資料（上の**Text**としてリンクされています）と、実行可能なJupyter Notebooksが含まれており、これらは多くの場合、フレームワーク（**PyTorch**または**TensorFlow**）に固有のものです。実行可能なノートブックには理論的な内容も多く含まれているので、トピックを理解するためには、少なくとも1つのバージョンのノートブック（PyTorchまたはTensorFlowのどちらか）を通読する必要があります。また、いくつかのトピックには**Lab**が用意されており、学習した内容を特定の問題に適用してみる機会があります。

いくつかのセクションでは、関連するトピックをカバーする **MS Learn** モジュールへのリンクも含まれています。Microsoft Learnは、GPUを利用した便利な学習環境を提供しますが、内容的にはもう少し深いカリキュラムを期待できます。

# Getting Started

**学生の皆さん**、カリキュラムの利用方法はいくつかあります。まず、テキストを読んで GitHub にあるコードに直接目を通すことができます。
もし、いずれかのノートブックでコードを実行したい場合は - 私たちの[手順](./etc/how-to-run.md)を読んで、その方法についての詳しいアドバイスをこの[ブログ記事](https://soshnikov.com/education/how-to-execute-notebooks-from-github/)で見つけてください。

> **Note**: [本カリキュラムのコードの実行方法の説明](./etc/how-to-run.md)

ただし、自習用として受講したい場合は、レポ全体を自分のGitHubアカウントにフォークして、一人で、またはグループで演習をこなすことをお勧めします。

- Start with a pre-lecture quiz
- Read the intro text for the lecture 
- If the lecture has additional notebooks, go through them, reading and executing the code. If both TensorFlow and PyTorch notebooks are provided, you can focus on one of them - chose your favorite framework
- Notebooks often contain some of the challenges that require you to tweak the code a little bit to experiment
- Take the post-lecture quiz
- If there is a lab attached to the module - complete the assignment
- Visit the [Discussion board](https://github.com/microsoft/AI-For-Beginners/discussions) to "learn out loud".
- Chat with other learners [on Gitter](https://gitter.im/Microsoft/ai-for-beginners) or [in Telegram channel](http://t.me/ai_for_beginners).

> For further study, we recommend following these [Microsoft Learn](https://docs.microsoft.com/en-us/users/dmitrysoshnikov-9132/collections/31zgizg2p418yo/?WT.mc_id=academic-57639-dmitryso) modules and learning paths.

**Teachers**, we have [included some suggestions](/etc/for-teachers.md) on how to use this curriculum.

---

## Credits

**✍️ Primary Author:** [Dmitry Soshnikov](http://soshnikov.com), PhD <br/>
**🔥 Editor:** [Jen Looper](https://twitter.com/jenlooper), PhD <br/>
**🎨 Sketchnote illustrator:** [Tomomi Imura](https://twitter.com/girlie_mac) <br/>
**✅ Quiz Creator:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)  <br/>
**🙏 Core Contributors:** [Evgenii Pishchik](https://github.com/Pe4enIks) 

## Meet the Team

[![Promo video](/lessons/sketchnotes/ai-for-beginners.png)](https://youtu.be/m2KrAk0cC1c "Promo video")

> 🎥 Click the image above for a video about the project and the folks who created it!

---

## Pedagogy

We have chosen two pedagogical tenets while building this curriculum: ensuring that it is hands-on **project-based** and that it includes **frequent quizzes**.

By ensuring that the content aligns with projects, the process is made more engaging for students and retention of concepts will be augmented. In addition, a low-stakes quiz before a class sets the intention of the student towards learning a topic, while a second quiz after class ensures further retention. This curriculum was designed to be flexible and fun and can be taken in whole or in part. The projects start small and become increasingly complex by the end of the 12 week cycle.

> Find our [Code of Conduct](etc/CODE_OF_CONDUCT.md), [Contributing](etc/CONTRIBUTING.md), and [Translation](etc/TRANSLATIONS.md) guidelines. Find our [Support Documentation here](etc/SUPPORT.md) and [security information here](etc/SECURITY.md). We welcome your constructive feedback!

> **A note about quizzes**: All quizzes are contained [in this app](https://black-ground-0cc93280f.1.azurestaticapps.net/), for 50 total quizzes of three questions each. They are linked from within the lessons but the quiz app can be run locally; follow the instruction in the `etc/quiz-app` folder.

## Offline access

You can run this documentation offline by using [Docsify](https://docsify.js.org/#/). Fork this repo, [install Docsify](https://docsify.js.org/#/quickstart) on your local machine, and then in the `etc/docsify` folder of this repo, type `docsify serve`. The website will be served on port 3000 on your localhost: `localhost:3000`. A pdf of the curriculum is available [at this link](/etc/pdf/readme.pdf).

## Help Wanted!

Would you like to contribute a translation? Please read our [translation guidelines](etc/TRANSLATIONS.md).

## Other Curricula

Our team produces other curricula! Check out:

- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [Machine Learning for Beginners](http://aka.ms/ML-for-Beginners)
- [Data Science for Beginners](http://aka.ms/Data-Science-for-Beginners)
