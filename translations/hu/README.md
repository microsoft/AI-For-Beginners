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

# Mesterséges intelligencia kezdőknek – Oktatási anyag

|![Sketchnote by @girlie_mac https://twitter.com/girlie_mac](../../translated_images/hu/ai-overview.0857791951d19500.webp)|
|:---:|
| AI For Beginners – _Sketchnote készítette: [@girlie_mac](https://twitter.com/girlie_mac)_ |

Fedezd fel a **Mesterséges Intelligencia** (MI) világát 12 hetes, 24 leckéből álló tananyagunkkal! Gyakorlati leckéket, kvízeket és laborokat tartalmaz. Az anyag kezdőbarát, és olyan eszközöket fed le, mint a TensorFlow és a PyTorch, valamint az MI etikáját is.

### 🌐 Többnyelvű támogatás

#### GitHub Action-nal támogatott (Automatizált és Mindig naprakész)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](./README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Szeretnéd helyben klónozni?**

> Ez a tároló 50+ nyelvi fordítást tartalmaz, ami jelentősen megnöveli a letöltési méretet. Ha fordítások nélkül szeretnéd klónozni, használj sparse checkout-ot:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git
> cd AI-For-Beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Ez gyorsabb letöltést tesz lehetővé, ugyanakkor minden szükséges anyagot megkapsz a tanfolyam elvégzéséhez.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ha további fordítási nyelveket szeretnél támogatni, azok listája [itt található](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Csatlakozz a közösséghez
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

## Mit fogsz megtanulni

**[A tanfolyam elmetérképe](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

Ebben a tananyagban megtanulod:

* A mesterséges intelligencia különböző megközelítéseit, beleértve a „régi jó” szimbolikus megközelítést a **tudás-reprezentációval** és érveléssel ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
* A **neurális hálózatokat** és a **mélytanulást**, amelyek a modern MI alapját képezik. Ezeknek a fontos témáknak a fogalmait a két legnépszerűbb keretrendszer - a [TensorFlow](http://Tensorflow.org) és a [PyTorch](http://pytorch.org) – példáin keresztül mutatjuk be.
* **Neurális architektúrákat** képek és szövegek kezelésére. Legújabb modelleket is érintünk, bár a legfrissebb állapotot lehet, hogy kevésbé fedjük le.
* Kevésbé népszerű MI megközelítéseket, mint a **genetikus algoritmusok** és a **multi-ügynök rendszerek**.

A mit nem tartalmaz a tananyagban:

> [Minden további forrás megtalálható a Microsoft Learn gyűjteményünkben](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)

* Az **MI üzleti alkalmazásainak** eseteit. Ilyen témákhoz ajánljuk a [Bevezetés az MI-be üzleti felhasználók számára](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) tanulási útvonalat a Microsoft Learn-en, vagy az [AI Business School](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum) programot, amelyet az [INSEAD](https://www.insead.edu/) együttműködésével fejlesztettek ki.
* A **klasszikus gépi tanulást**, amely jól le van írva a [Machine Learning for Beginners Curriculum](http://github.com/Microsoft/ML-for-Beginners) tananyagunkban.
* Gyakorlati MI alkalmazásokat, amelyek a **[Kognitív Szolgáltatások](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)** segítségével készültek. Ehhez ajánljuk a Microsoft Learn moduljait a [látás](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum), a [természetes nyelvfeldolgozás](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum) és a **[Generatív MI az Azure OpenAI szolgáltatással](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** területeken, valamint más témákat.
* Konkrét ML **felhőkeretrendszereket**, például az [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum), a [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum) vagy az [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum). Ilyen témákhoz ajánljuk a [Gépi tanulási megoldások építése és üzemeltetése Azure Machine Learninggel](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) és az [Gépi tanulási megoldások építése és üzemeltetése Azure Databricks-szel](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum) tanulási útvonalakat.
* **Konverzációs MI-t** és **Chat botokat**. Van egy külön [Konverzációs MI megoldások létrehozása](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum) tanulási útvonal, valamint hivatkozhatsz erre a [blogbejegyzésre](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/), ha részletesebb információkra van szükséged.
* A mélytanulás **mély matematikáját**. Ehhez ajánljuk Ian Goodfellow, Yoshua Bengio és Aaron Courville [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) című könyvét, amely elérhető online is: [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).

Az _MI a felhőben_ témakörök gyengéd bevezetéséhez érdemes lehet végigmenni a [Kezdés a mesterséges intelligenciával az Azure-on](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum) tanulási útvonalat.

# Tartalom

|     |                                                                 Lecke link                                                                  |                                           PyTorch/Keras/TensorFlow                                          | Labor                                                            |
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |
| 0  |                                 [Tanfolyam beállítása](./lessons/0-course-setup/setup.md)                                 |                      [Fejlesztői környezet beállítása](./lessons/0-course-setup/how-to-run.md)                       |   |
| I  |               [**Bevezetés az MI-be**](./lessons/1-Intro/README.md)      | | |
| 01  |       [Bevezetés és az MI története](./lessons/1-Intro/README.md)       |           -                            | -  |
| II |              **Szimbolikus MI**              |
| 02  |       [Tudás-reprezentáció és szakértői rendszerek](./lessons/2-Symbolic/README.md)       |            [Szakértői rendszerek](./lessons/2-Symbolic/Animals.ipynb) /  [Ontológia](./lessons/2-Symbolic/FamilyOntology.ipynb) /[Fogalomgráf](./lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |
| III |                        [**Bevezetés a neurális hálózatokhoz**](./lessons/3-NeuralNetworks/README.md) |||
| 03  |                [Perceptron](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Jegyzetfüzet](./lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [Labor](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 04  |                   [Többrétegű perceptron és saját keretrendszer létrehozása](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Jegyzetfüzet](./lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [Labor](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 05  |            [Bevezetés a keretrendszerekbe (PyTorch/TensorFlow) és túltanulás](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](./lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](./lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Labor](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV  |            [**Számítógépes látás**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [Fedezd fel a számítógépes látást a Microsoft Azure-en](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |
| 06  |            [Bevezetés a számítógépes látásba. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Jegyzetfüzet](./lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [Labor](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 07  |            [Konvolúciós neurális hálózatok](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [CNN architektúrák](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](./lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](./lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [Labor](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 08  |            [Előre betanított hálózatok és transfer learning](./lessons/4-ComputerVision/08-TransferLearning/README.md) és [Tréning trükkök](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](./lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Labor](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [Autoenkódolók és VAE-k](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](./lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [Generatív ellenfelek hálózatai & Művészi stílustranszfer](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](./lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [Objektumfelismerés](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](./lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [Labor](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [Szemantikus szegmentálás. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)             |  |
| V  |            [**Természetes nyelvfeldolgozás**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [Fedezd fel a természetes nyelvfeldolgozást a Microsoft Azure-en](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [Szöveges reprezentáció. Bow/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [Szemantikus szóbeágyazások. Word2Vec és GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [Nyelvi modellezés. Saját beágyazások tanítása](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [Labor](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [Rekurzív neurális hálózatok](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [Generatív rekurzív hálózatok](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)             | [Labor](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Transformerek. BERT.](./lessons/5-NLP/18-Transformers/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [Névegyelem felismerés](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [Labor](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [Nagy nyelvi modellek, prompt programozás és néhány feladat kevés példával](./lessons/5-NLP/20-LangModels/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **Egyéb mesterséges intelligencia technikák** || |
| 21  |            [Genetikus algoritmusok](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Jegyzetfüzet](./lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [Mély megerősítéses tanulás](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](./lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](./lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [Labor](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [Többügynökös rendszerek](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **Mesterséges intelligencia etika** | | |
| 24  |            [AI etika és felelős mesterséges intelligencia](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: Felelős AI alapelvek](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **Extra anyagok** | | |
| 25  |            [Többmodális hálózatok, CLIP és VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Jegyzetfüzet](./lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## Minden leckéhez tartozik

* Előolvasási anyag
* Futatható Jupyter jegyzetfüzetek, amelyek gyakran adott keretrendszerhez (**PyTorch** vagy **TensorFlow**) kötöttek. A futtatható jegyzetfüzetben sok elméleti anyag is található, így a téma megértéséhez legalább az egyik verzión (PyTorch vagy TensorFlow) végig kell menni.
* Bizonyos témákhoz **laborok** érhetők el, melyek lehetőséget adnak a tanultak gyakorlati alkalmazására egy adott probléma megoldásában.
* Néhány rész tartalmaz linkeket [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) modulokhoz, amelyek kapcsolódó témákat fednek le.

## Első lépések

### 🎯 Újonc az MI-ben? Kezdj itt!

Ha teljesen új vagy az MI-ben és gyors, gyakorlati példákat keresel, nézd meg a [**Kezdőknek szánt példákat**](./examples/README.md)! Ezek tartalmazzák:

- 🌟 **Hello MI Világ** - Az első MI programod (mintafelismerés)
- 🧠 **Egyszerű neurális hálózat** - Neurális hálózat építése a semmiből  

- 🖼️ **Képosztályozó** - Osztályozza a képeket részletes megjegyzésekkel
- 💬 **Szövegérzelem** - Pozitív/negatív szöveg elemzése

Ezek a példák segítenek megérteni az MI fogalmait, mielőtt belevágnál a teljes tananyagba.

### 📚 Teljes tananyag beállítása

- Készítettünk egy [beállító leckét](./lessons/0-course-setup/setup.md), amely segít a fejlesztői környezet beállításában. - Oktatók számára is létrehoztunk egy [tananyagbeállító leckét](./lessons/0-course-setup/for-teachers.md)!
- Hogyan [futtasd a kódot VSCode-ban vagy Codespace-ben](./lessons/0-course-setup/how-to-run.md)

Kövesd ezeket a lépéseket:

Forkold a Tárolót: Kattints a "Fork" gombra az oldal jobb felső sarkában.

Klónozd a Tárolót: `git clone https://github.com/microsoft/AI-For-Beginners.git`

Ne felejtsd el megjelölni csillaggal (🌟) ezt a tárolót, hogy később könnyebben megtaláld.

## Ismerkedj meg más tanulókkal

Csatlakozz az [hivatalos AI Discord szerverünkhöz](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum), hogy találkozz és kapcsolatot építs más, a tanfolyamot végző tanulókkal, valamint kérj támogatást.

Ha termék visszajelzésed vagy kérdésed van a fejlesztés közben, látogass el az [Azure AI Foundry fejlesztői fórumára](https://aka.ms/foundry/forum)

## Kvízek 

> **Megjegyzés a kvízekhez**: Minden kvíz az etc\quiz-app mappában, a Quiz-app mappában található, illetve [Online itt](https://ff-quizzes.netlify.app/) érhető el. A leckékből hivatkozva használhatók, a kvízalkalmazás futtatható helyileg vagy telepíthető Azure-ra; kövesd az utasításokat a `quiz-app` mappában. Fokozatosan lokalizálásra kerülnek.

## Segítséget Kérünk

Van javaslatod vagy hibát találtál helyesírásban vagy kódban? Nyiss egy problémát vagy hozz létre egy pull requestet.

## Külön Köszönet

* **✍️ Fő szerző:** [Dmitry Soshnikov](http://soshnikov.com), PhD
* **🔥 Szerkesztő:** [Jen Looper](https://twitter.com/jenlooper), PhD
* **🎨 Sketchnote illusztrátor:** [Tomomi Imura](https://twitter.com/girlie_mac)
* **✅ Kvíz készítő:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)
* **🙏 Alapvető közreműködők:** [Evgenii Pishchik](https://github.com/Pe4enIks)

## Egyéb Tananyagok

Csapatunk más tananyagokat is készít! Nézd meg:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j kezdőknek](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js kezdőknek](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Ügynökök
[![AZD kezdőknek](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI kezdőknek](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP kezdőknek](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Ügynökök kezdőknek](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatív MI sorozat
[![Generatív MI kezdőknek](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatív MI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatív MI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatív MI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Alapvető tanulás
[![ML kezdőknek](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Adattudomány kezdőknek](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![MI kezdőknek](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kiberbiztonság kezdőknek](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webfejlesztés kezdőknek](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT kezdőknek](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR fejlesztés kezdőknek](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot sorozat
[![Copilot AI páros programozáshoz](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET fejlesztéshez](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Kaland](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Segítségkérés

Ha elakadsz vagy kérdésed van az MI alkalmazások fejlesztésével kapcsolatban, csatlakozz más tanulókhoz és tapasztalt fejlesztőkhöz az MCP-vel kapcsolatos beszélgetésekben. Ez egy támogató közösség, ahol a kérdések szívesen fogadottak és a tudás szabadon megosztott.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ha termék-visszajelzésed vagy hibákba ütközöl fejlesztés közben, látogass el ide:

[![Microsoft Foundry fejlesztői fórum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hivatalos forrásnak. Fontos információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->