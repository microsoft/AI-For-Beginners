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

# Umetna inteligenca za začetnike - Načrt učenja

|![Sketchnote by @girlie_mac https://twitter.com/girlie_mac](https://github.com/microsoft/AI-For-Beginners/raw/main/lessons/sketchnotes/ai-overview.png)|
|:---:|
| AI Za začetnike - _Sketchnote avtorice [@girlie_mac](https://twitter.com/girlie_mac)_ |

Raziščite svet **umetne inteligence** (UI) s našim 12-tedenskim, 24-lekcijskim načrtom učenja! Vključuje praktične lekcije, kvize in laboratorijske vaje. Načrt je prijazen do začetnikov in pokriva orodja, kot sta TensorFlow in PyTorch, pa tudi etiko v UI.

### 🌐 Podpora več jezikov

#### Podprto preko GitHub Action (avtomatizirano in vedno posodobljeno)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](./README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Raje želite lokalno klonirati?**
>
> Ta repozitorij vključuje več kot 50 prevodov jezikov, kar znatno poveča velikost prenosa. Za kloniranje brez prevodov uporabite sparse checkout:
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
> Tako dobite vse, kar potrebujete za dokončanje tečaja, z veliko hitrejšim prenosom.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Če želite, da so podprti dodatni prevodi jezikov, so ti navedeni [tukaj](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Pridružite se skupnosti
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

## Kaj se boste naučili

**[Mindmap tečaja](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

V tem načrtu učenja se boste naučili:

* Različnih pristopov k umetni inteligenci, vključno s "starim dobrim" simbolnim pristopom s **predstavljanjem znanja** in sklepanjem ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
* **Nevronskih mrež** in **globokega učenja**, ki sta jedro sodobne UI. Koncepte za tema pomembnima področjema bomo ilustrirali z uporabo kode v dveh najbolj priljubljenih ogrodjih - [TensorFlow](http://Tensorflow.org) in [PyTorch](http://pytorch.org).
* **Nevronskih arhitektur** za delo s slikami in besedilom. Pokrili bomo najnovejše modele, a morda bomo nekoliko manj v stiku z najsodobnejšim stanjem.
* Manj priljubljene pristope k UI, kot so **genetski algoritmi** in **sistemi več agentov**.

Kaj v tem načrtu ne bomo pokrivali:

> [Vse dodatne vire za ta tečaj najdete v naši zbirki Microsoft Learn](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)

* Poslovnih primerov uporabe **UI v poslu**. Razmislite o sprejetju [Uvod v UI za poslovne uporabnike](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) učne poti na Microsoft Learn ali [AI poslovne šole](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum), razvite v sodelovanju z [INSEAD](https://www.insead.edu/).
* **Klasičnega strojnega učenja**, ki je dobro opisano v našem [Načrtu učenja o strojnega učenja za začetnike](http://github.com/Microsoft/ML-for-Beginners).
* Praktičnih aplikacij UI, zgrajenih z uporabo **[Kognitivnih storitev](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)**. Za to priporočamo začetek z moduli Microsoft Learn za [vid](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum), [obdelave naravnega jezika](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum), **[Generativno UI z Azure OpenAI Service](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** in druge.
* Specifičnih **oblaku prijaznih ogrodij za ML**, kot so [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum), [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum) ali [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum). Razmislite o uporabi učnih poti [Izdelava in upravljanje rešitev strojnega učenja z Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) in [Izdelava in upravljanje rešitev strojnega učenja z Azure Databricks](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum).
* **Pogovorne UI** in **klepetalne bote**. Obstaja posebna [Učna pot za ustvarjanje pogovornih rešitev UI](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum), lahko pa si ogledate tudi [ta prispevek na blogu](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) za več podrobnosti.
* **Globoka matematika** za globoko učenje. Za to priporočamo [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) avtorjev Ian Goodfellow, Yoshua Bengio in Aaron Courville, ki je na voljo tudi na spletu na [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).

Za nežen uvod v teme _UI v oblaku_ lahko razmislite o sprejetju [Začetek z umetno inteligenco na Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum) učne poti.

# Vsebina

|     |                                                                 Povezava do lekcije                                                                  |                                           PyTorch/Keras/TensorFlow                                          | Laboratorij                                                            |
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |
| 0  |                                 [Nastavitev tečaja](./lessons/0-course-setup/setup.md)                                 |                      [Nastavite svoje razvojno okolje](./lessons/0-course-setup/how-to-run.md)                       |   |
| I  |               [**Uvod v UI**](./lessons/1-Intro/README.md)      | | |
| 01  |       [Uvod in zgodovina UI](./lessons/1-Intro/README.md)       |           -                            | -  |
| II |              **Simbolna UI**              |
| 02  |       [Predstavitev znanja in ekspertni sistemi](./lessons/2-Symbolic/README.md)       |            [Ekspertni sistemi](./lessons/2-Symbolic/Animals.ipynb) /  [Ontologija](./lessons/2-Symbolic/FamilyOntology.ipynb) /[Konceptni graf](./lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |
| III |                        [**Uvod v nevronske mreže**](./lessons/3-NeuralNetworks/README.md) |||
| 03  |                [Perceptron](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Zvezek](./lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [Laboratorij](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 04  |                   [Večplastni perceptron in ustvarjanje lastnega ogrodja](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Zvezek](./lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [Laboratorij](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 05  |            [Uvod v ogrodja (PyTorch/TensorFlow) in prenaučevanje](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](./lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](./lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Laboratorij](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV  |            [**Računalniški vid**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [Raziščite računalniški vid na Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |
| 06  |            [Uvod v računalniški vid. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Zvezek](./lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [Laboratorij](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 07  |            [Konvolucijske nevronske mreže](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [Arhitekture CNN](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](./lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](./lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [Laboratorij](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 08  |            [Predhodno naučene mreže in prenosno učenje](./lessons/4-ComputerVision/08-TransferLearning/README.md) in [Triki pri treningu](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](./lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Laboratorij](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [Avtoenkoderji in VAE](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](./lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [Generativne nasprotujoče se mreže & prenos umetniškega sloga](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](./lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [Zaznavanje objektov](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](./lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [Laboratorij](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [Semantična segmentacija. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)             |  |
| V  |            [**Obdelava naravnega jezika**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [Raziščite obdelavo naravnega jezika na Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [Predstavitev besedila. Bow/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [Semantične vektorske predstavitve besed. Word2Vec in GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [Jezikovno modeliranje. Učenje lastnih vektorskih predstavitev](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [Laboratorij](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [Rekurentne nevronske mreže](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [Generativne rekurentne mreže](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)             | [Laboratorij](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Transformatorji. BERT.](./lessons/5-NLP/18-Transformers/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [Prepoznavanje imenovanih entitet](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [Laboratorij](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [Veliki jezikovni modeli, programiranje pozivov in naloge z malo primeri](./lessons/5-NLP/20-LangModels/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **Druge AI tehnike** || |
| 21  |            [Genetski algoritmi](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Zvezek](./lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [Globoko okrepitveno učenje](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](./lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](./lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [Laboratorij](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [Sistemi z več agenti](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **Etika umetne inteligence** | | |
| 24  |            [Etika umetne inteligence in odgovorna AI](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: Principi odgovorne AI](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **Dodatki** | | |
| 25  |            [Večmodalne mreže, CLIP in VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Zvezek](./lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## Vsaka lekcija vsebuje
* Material za predhodno branje
* Izvedljivi Jupyter zvezki, ki so pogosto specifični za okvir (**PyTorch** ali **TensorFlow**). Izvedljivi zvezek vsebuje tudi veliko teoretičnega gradiva, zato morate za razumevanje teme preiti skozi vsaj eno različico zvezka (bodisi PyTorch ali TensorFlow).
* **Laboratoriji** na voljo za nekatere teme, ki vam omogočajo, da poskusite uporabiti naučeno gradivo na določen problem.
* Nekateri oddelki vsebujejo povezave do modulov [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum), ki pokrivajo sorodne teme.

## Začetek

### 🎯 Nov v AI? Začni tukaj!

Če ste popoln začetnik v AI in želite hitre, praktične primere, si oglejte naše [**Primeri za začetnike**](./examples/README.md)! Ti vključujejo:

- 🌟 **Pozdravljen svet AI** - Vaš prvi AI program (prepoznavanje vzorcev)
- 🧠 **Preprosta nevronska mreža** - Zgradite nevronsko mrežo iz nič  
- 🖼️ **Razvrščevalec slik** - Razvrščajte slike z podrobnimi komentarji
- 💬 **Čustvena analiza besedila** - Analizirajte pozitivno/negativno besedilo

Ti primeri so zasnovani tako, da vam pomagajo razumeti koncepte AI, preden se lotite celotnega učnega načrta.

### 📚 Celotna nastavitev učnega načrta

- Ustvarili smo [lekcijo o nastavitvi](./lessons/0-course-setup/setup.md), ki vam pomaga pri nastavitvi razvojnega okolja. - Za učitelje smo prav tako ustvarili [lekcijo o nastavitvi učnih načrtov](./lessons/0-course-setup/for-teachers.md)!
- Kako [pognati kodo v VSCode ali Codespace](./lessons/0-course-setup/how-to-run.md)

Sledite tem korakom:

Razvejite skladišče: Kliknite na gumb "Fork" zgoraj desno na tej strani.

Klonirajte skladišče: `git clone https://github.com/microsoft/AI-For-Beginners.git`

Ne pozabite zvezdico (🌟) dodati temu repozitoriju, da ga boste lažje našli pozneje.

## Spoznajte druge udeležence

Pridružite se našemu [uradnemu AI Discord strežniku](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum), da spoznate in se povežete z drugimi, ki obiskujejo tečaj, ter pridobite podporo.

Če imate povratne informacije o izdelku ali vprašanja med gradnjo, obiščite naš [Azure AI Foundry Developer Forum](https://aka.ms/foundry/forum)

## Kvizi

> **Opomba o kvizih**: Vsi kvizi so shranjeni v mapi Quiz-app v etc\quiz-app ali [spletno tukaj](https://ff-quizzes.netlify.app/). Povezani so iz lekcij. Kviz aplikacijo lahko zaženete lokalno ali pa jo namestite v Azure – sledite navodilom v mapi `quiz-app`. Postopoma so lokalizirani.

## Iščemo pomoč

Imate predloge ali ste našli pravopisne ali kode napake? Odprite težavo ali ustvarite pull zahtevo.

## Posebne zahvale

* **✍️ Glavni avtor:** [Dmitry Soshnikov](http://soshnikov.com), PhD
* **🔥 Urednik:** [Jen Looper](https://twitter.com/jenlooper), PhD
* **🎨 Ilustratorka skic:** [Tomomi Imura](https://twitter.com/girlie_mac)
* **✅ Ustvarjalec kvizov:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)
* **🙏 Glavni sodelavci:** [Evgenii Pishchik](https://github.com/Pe4enIks)

## Drugi učni načrti

Naša ekipa ustvarja še druge učne načrte! Oglejte si:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j za začetnike](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js za začetnike](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain za začetnike](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agenti
[![AZD za začetnike](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI za začetnike](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP za začetnike](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Agenti AI za začetnike](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serija Generativne AI
[![Generativna AI za začetnike](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativna AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativna AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativna AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Osnovno učenje
[![Strojno učenje za začetnike](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Podatkovna znanost za začetnike](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI za začetnike](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kibernetska varnost za začetnike](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Razvoj spletnih strani za začetnike](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT za začetnike](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Razvoj XR za začetnike](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Serija Copilot
[![Copilot za AI združeno programiranje](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot za C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Pomoc

Če zataknete ali imate kakršna koli vprašanja glede izgradnje AI aplikacij, se pridružite ostalim učencem in izkušenim razvijalcem v razpravah o MCP. To je podporna skupnost, kjer so vprašanja dobrodošla in se znanje prosto deli.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Če imate povratne informacije o izdelku ali napake med gradnjo, obiščite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za točnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v maternem jeziku velja za avtoritativni vir. Za kritične informacije je priporočljiv strokovni prevod, ki ga opravi človek. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->