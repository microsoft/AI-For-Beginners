<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3a6b0ddf7e6e3f33b2a543baf086dc9",
  "translation_date": "2025-08-25T21:07:25+00:00",
  "source_file": "README.md",
  "language_code": "hu"
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

# Mesterséges Intelligencia Kezdőknek - Tananyag  

|![ Sketchnote by [(@girlie_mac)](https://twitter.com/girlie_mac) ](./lessons/sketchnotes/ai-overview.png)|  
|:---:|  
| Mesterséges Intelligencia Kezdőknek - _Sketchnote készítette: [@girlie_mac](https://twitter.com/girlie_mac)_ |  

Fedezd fel a **Mesterséges Intelligencia** (MI) világát 12 hetes, 24 leckéből álló tananyagunkkal! Gyakorlati leckéket, kvízeket és laborokat tartalmaz. A tananyag kezdőbarát, és olyan eszközöket mutat be, mint a TensorFlow és a PyTorch, valamint az MI etikai kérdéseit is tárgyalja.  

## Amit megtanulsz  

**[A kurzus gondolattérképe](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**  

Ebben a tananyagban megtanulod:  

* A mesterséges intelligencia különböző megközelítéseit, beleértve a "régi jó" szimbolikus megközelítést **Tudásreprezentációval** és érveléssel ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).  
* **Neurális hálózatokat** és **mélytanulást**, amelyek a modern MI alapját képezik. Ezeket a fontos témákat két népszerű keretrendszer - [TensorFlow](http://Tensorflow.org) és [PyTorch](http://pytorch.org) - kódjain keresztül illusztráljuk.  
* **Neurális architektúrákat** képek és szövegek feldolgozására. Bár a legújabb modelleket is érintjük, nem feltétlenül fedjük le a legkorszerűbbeket.  
* Kevésbé népszerű MI megközelítéseket, mint például a **Genetikus Algoritmusok** és a **Többügynökös Rendszerek**.  

Amit nem fogunk lefedni ebben a tananyagban:  

> [Minden további forrást megtalálsz a kurzushoz a Microsoft Learn gyűjteményünkben](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)  

* Az **MI üzleti alkalmazásainak** eseteit. Javasoljuk, hogy vegyél részt a [Bevezetés az MI-be üzleti felhasználók számára](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) tanulási úton a Microsoft Learn-en, vagy az [AI Business School](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum) programon, amelyet az [INSEAD](https://www.insead.edu/) közreműködésével fejlesztettek ki.  
* A **klasszikus gépi tanulást**, amelyet részletesen bemutatunk a [Gépi Tanulás Kezdőknek Tananyagunkban](http://github.com/Microsoft/ML-for-Beginners).  
* Gyakorlati MI alkalmazásokat, amelyeket a **[Cognitive Services](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)** segítségével építettek. Ehhez javasoljuk, hogy kezdj a Microsoft Learn moduljaival, például [látás](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum), [természetes nyelvfeldolgozás](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum), **[Generatív MI az Azure OpenAI Service segítségével](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** és mások.  
* Specifikus ML **felhőkeretrendszereket**, mint például [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum), [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum), vagy [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum). Javasoljuk, hogy használd a [Gépi tanulási megoldások építése és működtetése az Azure Machine Learning segítségével](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) és a [Gépi tanulási megoldások építése és működtetése az Azure Databricks segítségével](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum) tanulási utakat.  
* **Beszélgető MI** és **chatbotok**. Ehhez külön [Beszélgető MI megoldások létrehozása](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum) tanulási út érhető el, valamint [ez a blogbejegyzés](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) is hasznos lehet.  
* A mélytanulás **mély matematikai háttere**. Ehhez ajánljuk Ian Goodfellow, Yoshua Bengio és Aaron Courville [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) című könyvét, amely online is elérhető: [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).  

Egy könnyed bevezetéshez az _MI a felhőben_ témákhoz érdemes lehet elvégezni a [Bevezetés a mesterséges intelligenciába az Azure-on](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum) tanulási utat.  

# Tartalom  

|     |                                                                 Lecke Link                                                                  |                                           PyTorch/Keras/TensorFlow                                          | Labor                                                            |  
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |  
| 0  |                                 [Kurzus beállítása](./lessons/0-course-setup/setup.md)                                 |                      [Fejlesztési környezet beállítása](./lessons/0-course-setup/how-to-run.md)                       |   |  
| I  |               [**Bevezetés az MI-be**](./lessons/1-Intro/README.md)      | | |  
| 01  |       [Bevezetés és az MI története](./lessons/1-Intro/README.md)       |           -                            | -  |  
| II |              **Szimbolikus MI**              |  
| 02  |       [Tudásreprezentáció és szakértői rendszerek](./lessons/2-Symbolic/README.md)       |            [Szakértői rendszerek](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb) /  [Ontológia](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb) /[Fogalmi gráf](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |  
| III |                        [**Bevezetés a neurális hálózatokba**](./lessons/3-NeuralNetworks/README.md) |||  
| 03  |                [Perceptron](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [Labor](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |  
| 04  |                   [Többrétegű perceptron és saját keretrendszer létrehozása](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [Labor](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |  
| 05  |            [Bevezetés a keretrendszerekbe (PyTorch/TensorFlow) és túltanulás](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Labor](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |  
| IV  |            [**Számítógépes látás**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [Fedezd fel a számítógépes látást a Microsoft Azure-on](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |  
| 06  |            [Bevezetés a számítógépes látásba. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [Labor](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |  
| 07  |            [Konvolúciós neurális hálózatok](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [CNN Architektúrák](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [Labor](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |  
| 08  |            [Előre betanított hálózatok és transzfer tanulás](./lessons/4-ComputerVision/08-TransferLearning/README.md) és [Tanítási trükkök](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Lab](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [Autoenkóderek és VAEs](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [Generatív adverszárius hálózatok és művészi stílusátvitel](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [Objektumfelismerés](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [Lab](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [Szemantikus szegmentáció. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](../../(https:/github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb))             |  |
| V  |            [**Természetes nyelvfeldolgozás**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [Fedezd fel a természetes nyelvfeldolgozást a Microsoft Azure-on](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [Szöveg reprezentáció. Bow/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [Szemantikus szóbeágyazások. Word2Vec és GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [Nyelvi modellezés. Saját beágyazások tanítása](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [Lab](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [Rekurzív neurális hálózatok](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [Generatív rekurzív hálózatok](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.md) / [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.md)             | [Lab](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Transzformerek. BERT.](./lessons/5-NLP/18-Transformers/READMEtransformers.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [Név entitás felismerés](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [Lab](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [Nagy nyelvi modellek, prompt programozás és kevés példás feladatok](./lessons/5-NLP/20-LangModels/READMELargeLang.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **Egyéb AI technikák** || |
| 21  |            [Genetikus algoritmusok](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [Mély megerősítéses tanulás](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [Lab](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [Többügynökös rendszerek](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **AI Etika** | | |
| 24  |            [AI Etika és felelős AI](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: Felelős AI alapelvek](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **Extrák** | | |
| 25  |            [Multi-modális hálózatok, CLIP és VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Notebook](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## Minden lecke tartalmazza

* Előzetes olvasmányokat
* Futtatható Jupyter Notebookokat, amelyek gyakran keretrendszer-specifikusak (**PyTorch** vagy **TensorFlow**). A futtatható notebookok rengeteg elméleti anyagot is tartalmaznak, így a téma megértéséhez legalább az egyik verziót (PyTorch vagy TensorFlow) érdemes átnézni.
* **Labok**, amelyek néhány témához elérhetők, és lehetőséget adnak arra, hogy az elsajátított anyagot egy konkrét problémára alkalmazd.
* Egyes szekciók hivatkozásokat tartalmaznak [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) modulokra, amelyek kapcsolódó témákat fednek le.

## Kezdés

- Létrehoztunk egy [beállítási leckét](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/0-course-setup/setup.md), amely segít a fejlesztési környezeted beállításában. - Oktatóknak létrehoztunk egy [tantervi beállítási leckét](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/0-course-setup/for-teachers.md) is!
- Hogyan [futtasd a kódot VSCode-ban vagy CodeSpace-ben](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/0-course-setup/how-to-run.md)

Kövesd ezeket a lépéseket:

Forkold a repót: Kattints a jobb felső sarokban található "Fork" gombra.

Klónozd a repót: `git clone https://github.com/microsoft/AI-For-Beginners.git`

Ne felejtsd el csillagozni (🌟) ezt a repót, hogy később könnyebben megtaláld.

## Találkozz más tanulókkal

Csatlakozz a [hivatalos AI Discord szerverünkhöz](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum), hogy találkozz és kapcsolatba lépj más tanulókkal, akik ezt a kurzust végzik, és támogatást kapj.

Ha termék-visszajelzésed vagy kérdéseid vannak a fejlesztés során, látogasd meg az [Azure AI Foundry fejlesztői fórumot](https://aka.ms/foundry/forum)

## Kvízek
> **Megjegyzés a kvízekről**: Minden kvíz az etc\quiz-app mappában található Quiz-app mappában van. A leckékből vannak hivatkozva, a kvíz alkalmazás helyben futtatható vagy Azure-ra telepíthető; kövesd az utasításokat a `quiz-app` mappában. Ezeket fokozatosan lokalizálják.
## Segítség Kérve

Van javaslatod, vagy találtál helyesírási vagy kódhibát? Nyiss egy hibajegyet, vagy hozz létre egy pull requestet.

## Külön Köszönet

* **✍️ Elsődleges szerző:** [Dmitry Soshnikov](http://soshnikov.com), PhD  
* **🔥 Szerkesztő:** [Jen Looper](https://twitter.com/jenlooper), PhD  
* **🎨 Illusztrátor:** [Tomomi Imura](https://twitter.com/girlie_mac)  
* **✅ Kvízkészítő:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)  
* **🙏 Fő közreműködők:** [Evgenii Pishchik](https://github.com/Pe4enIks)  

## Egyéb Tananyagok

Csapatunk más tananyagokat is készít! Nézd meg ezeket:

- [Generatív MI Kezdőknek](https://aka.ms/genai-beginners)  
- [Generatív MI Kezdőknek .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)  
- [Generatív MI JavaScript-tel](https://github.com/microsoft/generative-ai-with-javascript)  
- [Generatív MI Java-val](https://github.com/microsoft/Generative-AI-for-beginners-java)  
- [MI Kezdőknek](https://aka.ms/ai-beginners)  
- [Adattudomány Kezdőknek](https://aka.ms/datascience-beginners)  
- [Gépi Tanulás Kezdőknek](https://aka.ms/ml-beginners)  
- [Kiberbiztonság Kezdőknek](https://github.com/microsoft/Security-101)  
- [Webfejlesztés Kezdőknek](https://aka.ms/webdev-beginners)  
- [IoT Kezdőknek](https://aka.ms/iot-beginners)  
- [XR Fejlesztés Kezdőknek](https://github.com/microsoft/xr-development-for-beginners)  
- [GitHub Copilot Mesterfokon: Ügynöki Használat](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)  
- [GitHub Copilot Mesterfokon: C#/.NET Fejlesztőknek](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)  
- [Válaszd a Saját Copilot Kalandodat](https://github.com/microsoft/CopilotAdventures)  

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.