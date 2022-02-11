[![GitHub license](https://img.shields.io/github/license/microsoft/AI-For-Beginners.svg)](https://github.com/microsoft/AI-For-Beginners/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/AI-For-Beginners.svg)](https://GitHub.com/microsoft/AI-For-Beginners/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/AI-For-Beginners.svg)](https://GitHub.com/microsoft/AI-For-Beginners/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/AI-For-Beginners.svg)](https://GitHub.com/microsoft/AI-For-Beginners/pulls/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/AI-For-Beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/AI-For-Beginners/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/AI-For-Beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/AI-For-Beginners/network/)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/AI-For-Beginners.svg?style=social&label=Star)](https://GitHub.com/microsoft/AI-For-Beginners/stargazers/)

# Artificial Intelligence for Beginners - A Curriculum

Azure Cloud Advocates at Microsoft are pleased to offer a 12-week, 24-lesson curriculum all about **Artificial Intelligence**. In this curriculum, you will learn:

* Different approaches to Artificial Intelligence, including "good old" symbolic approach with **Knowledge Representation** and reasoning.
* **Neural Networks** and **Deep Learning**, which are at the core of modern AI. We will try to illustrate all ideas using code in two most popular frameworks - Tensorflow(http://tensorflow.org) and PyTorch(http://pytorch.org).
* **Neural Architectures** for working with Images and Text. We will try to cover very recent models, but may lack a little bit on state-of-the-art.
* Less popular AI approaches, such as **Genetic Algorithms**

What we will not cover in this curricula:
* **Classic Machine Learning**, which is well described in our [Machine Learning for Beginners Curriculum](http://github.com/Microsoft/ML-for-Beginners)
* Practical AI applications build using **[Cognitive Services](https://azure.microsoft.com/services/cognitive-services/?WT.mcid=academic-33554-dmitryso)**. You may want to go to separate courses on Microsoft Learn for [vision](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mcid=academic-33554-dmitryso), [natural language processing](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mcid=academic-33554-dmitryso) and others.
* Specific ML **Cloud Frameworks**, such as [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mcid=academic-33554-dmitryso). There is great learning path [Build and operate machine learning solutions with Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mcid=academic-33554-dmitryso) for this.
* **Conversational AI** and **Chat Bots**. There is a separate [Create conversational AI solutions](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mcid=academic-33554-dmitryso) learning path, and you can also refer to [this blog post](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/)

For a gentle introduction to *AI in the Cloud* topic you may consider taking [Get started with artificial intelligence on Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mcid=academic-33554-dmitryso) Learning Path.

---
# Content

<table>
<tr><th>No</th><th>Lesson</th><th>Intro</th><th>PyTorch</th><th>Keras/Tensorflow</th><th>Lab</th></tr>

<tr><td>I</td><td colspan="4"><b>Introduction to AI</b></td><td>PAT</td></tr>
<tr><td>1</td><td>Introduction and History of AI</td><td><a href="1-Intro/README.md">Text</a></td><td></td><td></td><td></td></tr>

<tr><td>II</td><td colspan="4"><b>Symbolic AI</b></td><td>PAT</td></tr>
<tr><td>2 </td><td>Knowledge Representation and Expert Systems</td><td>Text</td><td></td><td></td><td></td></tr>
<tr><td>III</td><td colspan="4"><b><a href="3-NeuralNetworks/README.md">Introduction to Neural Networks</a></b></td><td>PAT</td></tr>
<tr><td>3</td><td>Perceptron</td>
   <td><a href="3-NeuralNetworks/03-Perceptron/README.md">Text</a>
   <td colspan="2"><a href="3-NeuralNetworks/03-Perceptron/Perceptron.ipynb">Notebook</a></td><td></td></tr>
<tr><td>4 </td><td>Multi-Layered Perceptron and Creating our own Framework</td><td><a href="3-NeuralNetworks/04-OwnFramework/README.md">Text</a></td><td colspan="2"><a href="3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb">Notebook</a><td></td></tr> 
<tr><td>5</td>
   <td>Intro to Frameworks (PyTorch/Tensorflow)<br/>Overfitting</td>
   <td><a href="3-NeuralNetworks/05-Frameworks/README.md">Text</a><br/><a href="3-NeuralNetworks/05-Frameworks/Overfitting.md">Text</a></td>
   <td><a href="3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb">PyTorch</td>
   <td><a href="3-NeuralNetworks/05-Frameworks/IntroKerasTF.md">Keras/Tensorflow</td><td></td></tr>
<tr><td>IV</td><td colspan="2"><b><a href="4-ComputerVision/README.md">Computer Vision</a></b></td>
  <td><a href="https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-33554-dmitryso">MS Learn</a></td>
  <td><a href="https://docs.microsoft.com/learn/modules/intro-computer-vision-tensorflow/?WT.mc_id=academic-33554-dmitryso">MS Learn</a></td>
  <td>PAT</td></tr>
<tr><td>6</td><td>Intro to Computer Vision. OpenCV</td><td>Text<td colspan="2">Notebook</td><td></td></tr>
<tr><td>7</td><td>Convolutional Neural Networks<br/>CNN Architectures<br/>Training Tricks</td><td><a href="4-ComputerVision/07-ConvNets/README.md">Text</a><br/><a href="4-ComputerVision/07-ConvNets/CNN_Architectures.md">Text</a></td><td><a href="4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb">PyTorch</a></td><td><a href="4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb">Tensorflow</a></td><td></td></tr>
<tr><td>8</td><td>Pre-trained Networks and Transfer Learning</td><td><a href="4-ComputerVision/08-TransferLearning/README.md">Text</a><br/><a href="4-ComputerVision/08-TransferLearning/TrainingTricks.md">Text</a></td><td><a href="4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb">PyTorch</a></td><td><a href="4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb">Tensorflow</a><br/><a href="4-ComputerVision/08-TransferLearning/Dropout.ipynb">Dropout sample</a></td><td></td></tr>
<tr><td>9</td><td>Autoencoders and VAEs</td><td><a href="4-ComputerVision/09-Autoencoders/README.md">Text</a></td><td>PyTorch</td><td><a href="4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb">Tensorflow</a></td><td></td></tr>
<tr><td>10</td><td>Generative Adversarial Networks</td><td><a href="4-ComputerVision/10-GANs/README.md">Text</a></td><td>PyTorch</td><td><a href="4-ComputerVision/10-GANs/GANs.ipynb">Tensorflow</a></td><td></td></tr>
<tr><td>11</td><td>Object Detection</td><td>Text</td><td>PyTorch</td><td>Tensorflow</td><td></td></tr>
<tr><td>12</td><td>Instance Segmentation. U-Net</td><td>Text</td><td>PyTorch</td><td>Tensorflow</td><td></td></tr>
<tr><td>V</td><td colspan="2"><b><a href="5-NLP/README.md">Natural Language Processing</a></b></td>
   <td><a href="https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-33554-dmitryso">MS Learn</a></td>
   <td><a href="https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/?WT.mc_id=academic-33554-dmitryso">MS Learn</a></td>
   <td>PAT</td></tr>
<tr><td>13</td><td>Text Representation. Bow/TF-IDF</td><td><a href="5-NLP/13-TextRep/README.md">Text</a></td><td><a href="5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb">PyTorch</a></td><td><a href="5-NLP/13-TextRep/TextRepresentationTF.ipynb">Tensorflow</td><td></td></tr>
<tr><td>14</td><td>Semantic word embeddings. Word2Vec and GloVe</td><td><a href="5-NLP/14-Embeddings/README.md">Text</td><td><a href="5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb">PyTorch</a></td><td><a href="5-NLP/14-Embeddings/EmbeddingsTF.ipynb">Tensorflow</a></td><td></td></tr>
<tr><td>15</td><td>Language Modeling. Training your own embeddings</td><td><a href="5-NLP/15-LanguageModeling">Text</a></td><td>PyTorch</td><td>Tensorflow</td><td></td></tr>
<tr><td>16</td><td>Recurrent Neural Networks</td><td><a href="5-NLP/16-RNN/README.md">Text</a></td><td><a href="5-NLP/16-RNN/RNNPyTorch.ipynb">PyTorch</a></td><td><a href="5-NLP/16-RNN/RNNTF.ipynb">Tensorflow</a></td><td></td></tr>
<tr><td>17</td><td>Generative Recurrent Networks</td><td><a href="5-NLP/17-GenerativeNetworks/README.md">Text</a></td><td><a href="5-NLP/17-GenerativeNetworks/GenerativePyTorch.md">PyTorch</a></td><td><a href="5-NLP/17-GenerativeNetworks/GenerativeTF.md">Tensorflow</a></td><td></td></tr>
<tr><td>18</td><td>Transformers. BERT.</td><td><a href="5-NLP/18-Transformers/README.md">Text</a></td><td><a href="5-NLP/18-Transformers/TransformersPyTorch.md">PyTorch</a></td><td><a href="5-NLP/18-Transformers/TransformersTF.md">Tensorflow</a></td><td></td></tr>
<tr><td>19</td><td>Named Entity Recognition</td><td>Text</td><td>PyTorch</td><td>Tensorflow</td><td></td></tr>
<tr><td>20</td><td>Text Generation using GPT</td><td>Text</td><td>PyTorch</td><td>Tensorflow</td><td></td></tr>
<tr><td>VI</td><td colspan="4"><b>Other AI Techniques</b></td><td>PAT</td></tr>
<tr><td>21</td><td>Genetic Algorithms</td><td>Text<td colspan="2">Notebook</td><td></td></tr>
<tr><td>22</td><td>Deep Reinforcement Learning</td><td>Text</td><td>PyTorch</td><td>Tensorflow</td><td></td></tr>
<tr><td>23</td><td>Multi-Agent Systems</td><td>Text</td><td></td><td></td><td></td></tr>
<tr><td>VII</td><td colspan="4"><b>AI Ethics</b></td><td>PAT</td></tr>
<tr><td>24</td><td>AI Ethics and Responsible AI</td><td>Text</td><td></td><td></td><td></td></tr>
</table>

Each lesson contains some pre-reading material (linked as **Text** above), and some executable Jupyter Notebooks, which are often specific to the framework (**PyTorch** or **Tensorflow**). The executable notebook also contains a lot of theoretical material, so to understand the topic you need to go through at least one version of the notebooks (either PyTorch or Tensorflow). There are also **Labs** available for some topics, which give you an opportunity to try applying the material you have learnt to some specific problem. 

Some sections also contain links to **MS Learn** modules that cover related topics. Microsoft Learn provides convenient GPU-enabled learning environment, although in terms of content you can expect this curriculum to go a bit deeper.

Course sections also include the links to **PAT**s - Progress Assessment Tool, a list of items that you are likely to get to know after completing the module. You can review it and assess your progress on the course yourself. 

![Mindmap of the Course](Mindmap.svg)
# Getting Started

**Students**, there are a couple of ways to use the curriculum. First of all, you can just read the text and look through the code directly on GitHub. If you want to run the code in any of the notebooks - you can find the advice on how to do it [in this blog post](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

However, if you are serious about the course, we suggest to fork the entire repo to your own GitHub account and complete the exercises on your own or with a group:

- Start with a pre-lecture quiz.
- Read the intro text for the lecture 
- If the lecture has additional notebooks, go through them, reading and executing the code. If both Tensorflow and PyTorch notebooks are provided, you can focus on one of them - chose your favourite framework.
- Notebooks often contain some of the challenges that require you to tweak the code a little bit to experiment. Do not by lazy and do it!
- Take the post-lecture quiz.
- If there is a lab attached to the module - complete the assignment.
- Visit the [Discussion board](https://github.com/microsoft/AI-For-Beginners/discussions) to and "learn out loud" by filling out the appropriate PAT rubric. A 'PAT' is a Progress Assessment Tool that is a rubric you fill out to further your learning. You can also react to other PATs so we can learn together.

> For further study, we recommend following these [Microsoft Learn](https://docs.microsoft.com/en-us/users/jenlooper-2911/collections/k7o7tg1gp306q4?WT.mc_id=academic-15963-cxa) modules and learning paths.

**Teachers**, we have [included some suggestions](for-teachers.md) on how to use this curriculum.

---

## Credits

**✍️ Hearty thanks to our authors** TBD

**🎨 Thanks as well to our illustrators** TBD

**🙏 Special thanks 🙏 to our Microsoft Student Ambassador authors, reviewers and content contributors**, notably TBD


## Meet the Team

[![Promo video](ml-for-beginners.png)](https://youtu.be/Tj1XWrDSYJU "Promo video")

> 🎥 Click the image above for a video about the project and the folks who created it!

---

## Pedagogy

We have chosen two pedagogical tenets while building this curriculum: ensuring that it is hands-on **project-based** and that it includes **frequent quizzes**.

By ensuring that the content aligns with projects, the process is made more engaging for students and retention of concepts will be augmented. In addition, a low-stakes quiz before a class sets the intention of the student towards learning a topic, while a second quiz after class ensures further retention. This curriculum was designed to be flexible and fun and can be taken in whole or in part. The projects start small and become increasingly complex by the end of the 12 week cycle.

> Find our [Code of Conduct](CODE_OF_CONDUCT.md), [Contributing](CONTRIBUTING.md), and [Translation](TRANSLATIONS.md) guidelines. We welcome your constructive feedback!

> **A note about quizzes**: All quizzes are contained [in this app](https://jolly-sea-0a877260f.azurestaticapps.net), for 50 total quizzes of three questions each. They are linked from within the lessons but the quiz app can be run locally; follow the instruction in the `quiz-app` folder.

## Offline access

You can run this documentation offline by using [Docsify](https://docsify.js.org/#/). Fork this repo, [install Docsify](https://docsify.js.org/#/quickstart) on your local machine, and then in the root folder of this repo, type `docsify serve`. The website will be served on port 3000 on your localhost: `localhost:3000`.

## Help Wanted!

Would you like to contribute a translation? Please read our [translation guidelines](TRANSLATIONS.md).

## Other Curricula

Our team produces other curricula! Check out:

- [Web Dev for Beginners](https://aka.ms/webdev-beginners)
- [IoT for Beginners](https://aka.ms/iot-beginners)
- [Machine Learning for Beginners](http://github.com/microsoft/ML-for-Beginners)
- [Data Science for Beginners](http://github.com/microsoft/Data-Science-for-Beginners)
