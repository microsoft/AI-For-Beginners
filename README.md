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
* **Neural Networks** and **Deep Learning**, which are at the core of modern AI. We will try to illustrate all ideas using code in two most popular frameworks - [Tensorflow](http://tensorflow.org) and [PyTorch](http://pytorch.org).
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

| No | Lesson | Intro | PyTorch | Tensorflow | Lab |
|----|--------|-------|---------|------------|-----|
| <td colspan="4">**Introduction to AI** | [PAT] |
| 1 | Introduction and History of AI | [Text] | | | |
| <td colspan="4">**Symbolic AI**  | [PAT] |
| 2 | Knowledge Representation and Expert Systems | [Text] | | | |
| <td colspan="4">**Introduction to Neural Networks**  | [PAT] |
| 3 | Perceptron | [Text] | <td colspan="2">[Notebook] | 
| 4 | Intro to Frameworks (PyTorch/Tensorflow) | [Text] | [PyTorch]	| [Tensorflow] | |
| 5 | Multi-Layered Perceptron | [Text] | [PyTorch]	| [Tensorflow] | | 
| <td colspan="2">**Computer Vision** | [MS Learn][PTLearnCV] | [MS Learn][TFLearnCV] | [PAT] |
| 6	| Intro to Computer Vision. OpenCV | [Text] | <td colspan="2">[Notebook] | |
| 7	| Convolutional Neural Networks	| [Text] | [PyTorch] | [Tensorflow] | |
| 8	| Pre-trained Networks and Transfer Learning | [Text] | [PyTorch] | [Tensorflow] | |
| 9 | Autoencoders and VAEs | [Text] | [PyTorch] | [Tensorflow] | |
| 10 | Generative Adversarial Networks | [Text] | [PyTorch] | [Tensorflow] | |
| 11 | Object Detection | [Text] | [PyTorch] | [Tensorflow] | |
| 12 | Instance Segmentation. U-Net | [Text] | [PyTorch] | [Tensorflow] | |
| <td colspan="2">**Natural Language Processing** | [MS Learn][PTLearnNLP] | [MS Learn][TFLearnNLP] | [PAT] |
| 13 | Text Representation. Bow/TF-IDF | [Text] | [PyTorch] | [Tensorflow] | |
| 14 | Semantic Word Embeddings | [Text] | [PyTorch] | [Tensorflow] | |
| 15 | Training your own embeddings | [Text] | [PyTorch] | [Tensorflow] | |
| 16 | Recurrent Neural Networks| [Text] | [PyTorch] | [Tensorflow] | |
| 17 | Generative Recurrent Networks | [Text] | [PyTorch] | [Tensorflow] | |
| 18 | Language Modelling. BERT. Transformers. | [Text] | [PyTorch] | [Tensorflow] | |
| 19 | Named Entity Recognition. | [Text] | [PyTorch] | [Tensorflow] | |
| 20 | Text Generation using GPT | [Text] | [PyTorch] | [Tensorflow] | |
| <td colspan="4">**Other AI Techniques**  | [PAT](1-intro/PAT.md) |
| 21 | Genetic Algorithms | [Text] | <td colspan="2">[Notebook] |
| 22 | Deep Reinforcement Learning | [Text] | [PyTorch] | [Tensorflow] | |
| 23 | Multi-Agent Systems | [Text] | | | |
| <td colspan="4">**AI Ethics**  | [PAT] |
| 24 | AI Ethics and Responsible AI	| [Text] | | | |

Each lesson contains some pre-reading material (linked as **Text** above), and some executable Jupyter Notebooks, which are often specific to the framework (**PyTorch** or **Tensorflow**). The executable notebook also contains a lot of theoretical material, so to understand the topic you need to go through at least one version of the notebooks (either PyTorch or Tensorflow). There are also **Labs** available for some topics, which give you an opportunity to try applying the material you have learnt to some specific problem. 

Some sections also contain links to **MS Learn** modules that cover related topics. Microsoft Learn provides convenient GPU-enabled learning environment, although in terms of content you can expect this curriculum to go a bit deeper.

Course sections also include the links to **PAT**s - Progress Assessment Tool, a list of items that you are likely to get to know after completing the module. You can review it and assess your progress on the course yourself. 

---
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

[TFLearnCV]: https://docs.microsoft.com/learn/modules/intro-computer-vision-tensorflow/?WT.mc_id=academic-33554-dmitryso
[TFLearnNLP]: https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/?WT.mc_id=academic-33554-dmitryso
[PTLearnCV]: https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-33554-dmitryso
[PTLearnNLP]: https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-33554-dmitryso