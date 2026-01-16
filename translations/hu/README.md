<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85102ce4bfab31103e99dc8ca2e2f181",
  "translation_date": "2026-01-16T04:44:06+00:00",
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

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

# Mesterséges intelligencia kezdőknek – Tanterv

|![Sketchnote by @girlie_mac https://twitter.com/girlie_mac](../../../../translated_images/hu/ai-overview.0857791951d19500.webp)|
|:---:|
| AI For Beginners - _Vázlat [@girlie_mac](https://twitter.com/girlie_mac) tollából_ |

Fedezd fel a **Mesterséges intelligencia** (AI) világát 12 hét alatt, 24 leckén keresztül! Gyakorlati leckékkel, kvízekkel és laborokkal. A tanterv kezdőknek készült, és olyan eszközöket fed le, mint a TensorFlow és a PyTorch, valamint az AI etikai kérdéseit is.

### 🌐 Többnyelvű támogatás

#### GitHub Action segítségével (automatikus és mindig naprakész)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](./README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Szeretnéd helyileg klónozni?**

> Ez a tároló 50+ nyelvi fordítást tartalmaz, ami jelentősen megnöveli a letöltés méretét. Ha fordítások nélkül szeretnéd klónozni, használd a sparse checkout-ot:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git
> cd AI-For-Beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Így mindent megkapsz a tanfolyam elvégzéséhez sokkal gyorsabb letöltéssel.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ha további fordítási nyelvek támogatását szeretnéd, ezek listája itt található: [itt](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Csatlakozz a közösséghez
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

## Mit fogsz tanulni

**[A tanfolyam áttekintő térképe](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

Ebben a tantervben megtanulod:

* A mesterséges intelligencia különböző megközelítéseit, beleértve a „régi” szimbolikus megközelítést a **tudásreprezentációval** és az érveléssel ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
* A **neurális hálózatokat** és a **mélytanulást**, amelyek a modern AI magját képezik. Ezeknek a fontos témáknak a koncepcióit két népszerű keretrendszer – a [TensorFlow](http://Tensorflow.org) és a [PyTorch](http://pytorch.org) – segítségével fogjuk bemutatni kódpéldákkal.
* **Neurális architektúrákat** képek és szövegek feldolgozására. Áttekintjük a legújabb modelleket, bár lehet, hogy kissé elmaradunk a legmodernebbektől.
* Kevésbé népszerű AI megközelítéseket, mint például a **genetikus algoritmusok** és a **többügynökös rendszerek**.

A tanterv nem foglalkozik:

> [Találd meg az összes további forrást a tanfolyamhoz a Microsoft Learn gyűjteményünkben](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)

* Az **AI üzleti alkalmazásával** kapcsolatos üzleti esetekkel. Érdemes megfontolni a [Bevezető az AI használatához üzleti felhasználóknak](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) tanulási útvonalat a Microsoft Learn-en, vagy az [AI Business School](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum) programot, amelyet az [INSEAD](https://www.insead.edu/) partneri együttműködésében fejlesztettek ki.
* A **klasszikus gépi tanulást**, amelyről jól szól a [Gépi tanulás kezdőknek tanterve](http://github.com/Microsoft/ML-for-Beginners).
* Gyakorlati AI alkalmazásokat, amelyek a **[Kognitív Szolgáltatásokat](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)** használják. Ehhez ajánljuk, hogy kezdd a Microsoft Learn moduljaival a [képfeldolgozás](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum), a [természetes nyelv feldolgozás](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum), illetve a **[Generatív AI az Azure OpenAI szolgáltatásával](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** témákban.
* Specifikus ML **felhőkeretrendszereket**, mint például az [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum), a [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum) vagy az [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum). Érdemes használni a [Gépi tanulási megoldások építése és üzemeltetése Azure Machine Learning-gel](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) és a [Gépi tanulási megoldások építése és üzemeltetése Azure Databricks-szel](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum) tanulási útvonalakat.
* A **beszélgető AI-t** és a **csevegőbotokat**. Ehhez külön van egy [Beszélgető AI megoldások létrehozása](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum) tanulási útvonal, illetve további részleteket találsz [ebben a blogbejegyzésben](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/).
* A mélytanulás mögötti **mély matematikát**. Ehhez ajánljuk Ian Goodfellow, Yoshua Bengio és Aaron Courville [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) című könyvét, amely online is elérhető a [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/) oldalon.

A _felhőben zajló AI_ témák finom bevezetőjeként érdemes lehet megfontolni a [Mesterséges intelligencia megismerése Azure-on](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum) tanulási útvonalat.

# Tartalom

|     |                                                                 Lecke link                                                                 |                                           PyTorch/Keras/TensorFlow                                          | Labor                                                           |
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |
| 0  |                                 [Tanfolyam beállítása](./lessons/0-course-setup/setup.md)                                 |                      [Fejlesztői környezet beállítása](./lessons/0-course-setup/how-to-run.md)                       |   |
| I  |               [**Bevezetés az AI-be**](./lessons/1-Intro/README.md)      | | |
| 01  |       [Bevezetés és az AI története](./lessons/1-Intro/README.md)       |           -                            | -  |
| II |              **Szimbólikus AI**              |
| 02  |       [Tudásreprezentáció és szakértői rendszerek](./lessons/2-Symbolic/README.md)       |            [Szakértői rendszerek](./lessons/2-Symbolic/Animals.ipynb) /  [Ontológia](./lessons/2-Symbolic/FamilyOntology.ipynb) /[Fogalmi gráf](./lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |
| III |                        [**Bevezetés a neurális hálózatokba**](./lessons/3-NeuralNetworks/README.md) |||
| 03  |                [Perceptron](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Jegyzetfüzet](./lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [Labor](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 04  |                   [Többrétegű Perceptron és Saját Keretrendszer Létrehozása](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Jegyzetfüzet](./lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [Labor](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 05  |            [Bevezetés a Keretrendszerekbe (PyTorch/TensorFlow) és Túltanulás](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](./lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](./lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Labor](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV  |            [**Számítógépes Látás**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [Számítógépes látás felfedezése Microsoft Azure-on](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |
| 06  |            [Bevezetés a Számítógépes Látásba. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Jegyzetfüzet](./lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [Labor](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 07  |            [Konvolúciós Neurális Hálók](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [CNN Architektúrák](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](./lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](./lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [Labor](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 08  |            [Előre Betanított Hálók és Átviteli Tanulás](./lessons/4-ComputerVision/08-TransferLearning/README.md) és [Tanítási Trükkök](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](./lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Labor](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [Autoenkódolók és VAE-k](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](./lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [Generatív Ellenséges Hálók & Művészi Stílusátvitel](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](./lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [Objektum Felismerés](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](./lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [Labor](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [Szemantikus Szegmentálás. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)             |  |
| V  |            [**Természetes Nyelvfeldolgozás**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [Természetes Nyelvfeldolgozás felfedezése Microsoft Azure-on](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [Szöveg reprezentáció. Bag of Words/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [Szemantikus szóbeágyazások. Word2Vec és GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [Nyelvi modellezés. Saját beágyazások tanítása](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [Labor](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [Rekurzív Neurális Hálók](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [Generatív Rekurzív Hálók](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)             | [Labor](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Transformer-ek. BERT.](./lessons/5-NLP/18-Transformers/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [Névkitöltő Entitás Felismerés](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [Labor](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [Nagy Nyelvi Modellek, Prompt Programozás és Néhány Példány Feladat](./lessons/5-NLP/20-LangModels/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **Egyéb AI Technikák** || |
| 21  |            [Genetikus Algoritmusok](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Jegyzetfüzet](./lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [Mély Megerősítéses Tanulás](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](./lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](./lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [Labor](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [Többügynökös Rendszerek](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **AI Etika** | | |
| 24  |            [AI Etika és Felelős MI](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: Felelős MI Elvek](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **Extrák** | | |
| 25  |            [Multimodális Hálózatok, CLIP és VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Jegyzetfüzet](./lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## Minden lecke tartalmaz

* Előolvasási anyagot
* Végrehajtható Jupyter Jegyzetfüzeteket, amelyek gyakran keretrendszer-specifikusak (**PyTorch** vagy **TensorFlow**). A végrehajtható jegyzetfüzet sok elméleti anyagot is tartalmaz, ezért a téma megértéséhez legalább az egyik változatot végig kell menni (akár PyTorch, akár TensorFlow).
* Bizonyos témákhoz elérhetőek **Laborok**, amelyek lehetőséget adnak, hogy a tanult anyagot konkrét problémára alkalmazd.
* Néhány szekció tartalmaz linkeket [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) modulokhoz, amelyek kapcsolódó témákat fednek le.

## Kezdés

### 🎯 Új vagy az MI területén? Kezdd itt!

Ha teljesen új vagy az MI területén, és gyors, gyakorlatias példákat keresel, nézd meg a [**Kezdőbarát Példáinkat**](./examples/README.md)! Ezek tartalmazzák:

- 🌟 **Hello AI Világ** - Az első AI programod (minta felismerés)
- 🧠 **Egyszerű Neurális Háló** - Építs neurális hálót a semmiből  
- 🖼️ **Képosztályozó** - Képeket osztályoz részletes megjegyzésekkel
- 💬 **Szöveg érzelmi tónusa** - Pozitív/negatív szöveg elemzése

Ezek a példák segítenek megérteni az MI fogalmait, mielőtt belekezdenél a teljes tananyagba.

### 📚 Teljes tananyag beállítása

- Létrehoztunk egy [beállítási leckét](./lessons/0-course-setup/setup.md), hogy segítsünk a fejlesztőkörnyezeted beállításában. - Oktatók számára létrehoztunk egy [tananyag beállítási leckét](./lessons/0-course-setup/for-teachers.md) is!
- Hogyan futtathatod a kódot VSCode-ban vagy Codespace-ben [itt](./lessons/0-course-setup/how-to-run.md)

Kövesd ezeket a lépéseket:

Forkold a tárolót: Kattints a "Fork" gombra ennek az oldalnak a jobb felső sarkában.

Klónozd a tárolót: `git clone https://github.com/microsoft/AI-For-Beginners.git`

Ne felejtsd el megcsillagozni (🌟) ezt a repót, hogy később könnyebben megtaláld.

## Ismerkedj meg más tanulókkal

Csatlakozz hivatalos AI Discord szerverünkhöz ([ide](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum)), hogy találkozz és kapcsolatokat építs más, a tanfolyamot végző tanulókkal, valamint támogató közösséget kapj.

Ha termékvisszajelzésed vagy kérdésed van fejlesztés közben, látogass el az [Azure AI Foundry Fejlesztői Fórumra](https://aka.ms/foundry/forum)

## Kvízek

> **Megjegyzés a kvízekhez**: Minden kvíz a Quiz-app mappában található az etc\quiz-app alatt, vagy [online itt](https://ff-quizzes.netlify.app/). A leckékből linkeltek, a kvíz alkalmazás lokálisan futtatható vagy Azure-ba telepíthető; kövesd az utasításokat a `quiz-app` mappában. Fokozatosan lokalizáljuk őket.

## Segítséget kérünk

Van javaslatod vagy találtál helyesírási vagy kód hibákat? Nyiss egy issue-t vagy hozz létre egy pull requestet.

## Külön köszönet

* **✍️ Fő szerző:** [Dmitry Soshnikov](http://soshnikov.com), PhD
* **🔥 Szerkesztő:** [Jen Looper](https://twitter.com/jenlooper), PhD
* **🎨 Sketchnote illusztrátor:** [Tomomi Imura](https://twitter.com/girlie_mac)
* **✅ Kvíz készítő:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)
* **🙏 Fő közreműködők:** [Evgenii Pishchik](https://github.com/Pe4enIks)

## Egyéb tananyagok

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
[![AI ügynökök kezdőknek](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Generatív AI sorozat
[![Generatív AI kezdőknek](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatív AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### Alap tanulás
[![Gépi tanulás kezdőknek](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Adattudomány kezdőknek](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![MI kezdőknek](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kiberbiztonság kezdőknek](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web fejlesztés kezdőknek](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT kezdőknek](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR fejlesztés kezdőknek](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Copilot sorozat
[![Copilot AI páros programozáshoz](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot C#/.NET-hez](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot kalandok](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Segítség kérése

Ha elakadsz vagy kérdésed van az MI alkalmazások fejlesztésével kapcsolatban, csatlakozz a többi tanulóhoz és tapasztalt fejlesztőhöz a MCP-vel kapcsolatos beszélgetésekhez. Ez egy támogató közösség, ahol a kérdések szívesen látottak és a tudás szabadon megosztott.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ha termék-visszajelzésed vagy hibákat találsz fejlesztés közben, látogass el:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár igyekszünk pontos fordítást nyújtani, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai emberi fordítást javasolunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->