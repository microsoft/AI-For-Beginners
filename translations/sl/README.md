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

# Umetna inteligenca za začetnike - učni načrt

|![Sketchnote by @girlie_mac https://twitter.com/girlie_mac](../../translated_images/sl/ai-overview.0857791951d19500.webp)|
|:---:|
| AI za začetnike - _Skiznot avtorice [@girlie_mac](https://twitter.com/girlie_mac)_ |

Raziščite svet **umetne inteligence** (UI) z našim 12-tedenskim učnim načrtom s 24 lekcijami! Vključuje praktične lekcije, kvize in delavnice. Učni načrt je prijazen začetnikom in pokriva orodja, kot sta TensorFlow in PyTorch, ter tudi etiko v UI.


### 🌐 Podpora za več jezikov

#### Podprto preko GitHub Action (avtomatizirano in vedno posodobljeno)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](./README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Raje klonirate lokalno?**

> Ta repozitorij vključuje več kot 50 prevodov, kar znatno poveča velikost prenosa. Za klon brez prevodov uporabite sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git
> cd AI-For-Beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Tako dobite vse, kar potrebujete za dokončanje tečaja z veliko hitrejšim prenosom.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Če želite podpreti dodatne jezike prevodov, so podprti jeziki navedeni [tukaj](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Pridružite se skupnosti
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

## Kaj se boste naučili

**[Miselnica tečaja](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

V tem učnem načrtu se boste naučili:

* Različnih pristopov k umetni inteligenci, vključno z "dobrim starim" simbolnim pristopom s **predstavljanjem znanja** in sklepanjem ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
* **Nevronskih mrež** in **globokega učenja**, ki so jedro sodobne UI. Pojasnili bomo koncepte za tema pomembnima področjema z uporabo kode v dveh najbolj priljubljenih okvirjih - [TensorFlow](http://Tensorflow.org) in [PyTorch](http://pytorch.org).
* **Nevronskih arhitektur** za delo s slikami in besedilom. Pokrili bomo najnovejše modele, čeprav morda ne povsem najnovejše dosežke.
* Manj priljubljene pristope k UI, kot so **genetski algoritmi** in **večagentni sistemi**.

Kaj ne bomo zajemali v tem učnem načrtu:

> [Poiščite vse dodatne vire za ta tečaj v naši zbirki Microsoft Learn](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)

* Poslovnih primerov uporabe **UI v poslovanju**. Razmislite o opravilu učne poti [Uvod v UI za poslovne uporabnike](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) na Microsoft Learn ali [AI poslovno šolo](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum), razvito v sodelovanju z [INSEAD](https://www.insead.edu/).
* **Klasičnega strojnega učenja**, ki je dobro opisan v našem [Učnem načrtu strojnega učenja za začetnike](http://github.com/Microsoft/ML-for-Beginners).
* Praktičnih UI aplikacij, zgrajenih z uporabo **[Kognitivnih storitev](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)**. Za to priporočamo, da začnete z moduli Microsoft Learn za [vid](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum), [obdelavo naravnega jezika](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum), **[generativno UI z Azure OpenAI Service](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** in druge.
* Specifične ML **oblake ogrodja**, kot so [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum), [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum), ali [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum). Uporabite učni poti [Build and operate machine learning solutions with Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) in [Build and Operate Machine Learning Solutions with Azure Databricks](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum).
* **Pogovorno UI** in **pogovorne bote**. Obstaja ločena učna pot [Ustvarite pogovorne UI rešitve](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum), prav tako pa si lahko ogledate [to objavo na blogu](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) za več podrobnosti.
* **Globoko matematiko** za globoko učenje. Za to priporočamo [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) avtorjev Ian Goodfellow, Yoshua Bengio in Aaron Courville, ki je na voljo tudi na spletu na [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).

Za prijazen uvod v teme _UI v oblaku_ razmislite o opravljanju učne poti [Začni z umetno inteligenco na Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum).

# Vsebina

|     |                                                                 Povezava do lekcije                                                                  |                                           PyTorch/Keras/TensorFlow                                          | Laboratorij                                                            |
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |
| 0  |                                 [Nastavitev tečaja](./lessons/0-course-setup/setup.md)                                 |                      [Nastavite svoje razvojno okolje](./lessons/0-course-setup/how-to-run.md)                       |   |
| I  |               [**Uvod v UI**](./lessons/1-Intro/README.md)      | | |
| 01  |       [Uvod in zgodovina UI](./lessons/1-Intro/README.md)       |           -                            | -  |
| II |              **Simbolna UI**              |
| 02  |       [Predstavljanje znanja in ekspertni sistemi](./lessons/2-Symbolic/README.md)       |            [Ekspertni sistemi](./lessons/2-Symbolic/Animals.ipynb) /  [Ontologija](./lessons/2-Symbolic/FamilyOntology.ipynb) /[Graf konceptov](./lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |
| III |                        [**Uvod v nevronske mreže**](./lessons/3-NeuralNetworks/README.md) |||
| 03  |                [Perceptron](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Zvezek](./lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [Laboratorij](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 04  |                   [Večplastni perceptron in ustvarjanje lastnega ogrodja](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Zvezek](./lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [Laboratorij](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 05  |            [Uvod v ogrodja (PyTorch/TensorFlow) in prenaučenje](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](./lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](./lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Laboratorij](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV  |            [**Računalniški vid**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [Raziskuj računalniški vid na Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |
| 06  |            [Uvod v računalniški vid. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Zvezek](./lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [Laboratorij](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 07  |            [Konvolucijske nevronske mreže](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [CNN arhitekture](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](./lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](./lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [Laboratorij](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 08  |            [Predhodno usposobljene mreže in prenosno učenje](./lessons/4-ComputerVision/08-TransferLearning/README.md) in [Triki pri usposabljanju](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](./lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Laboratorij](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [Avtoenkoderji in VAE-ji](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](./lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [Generativne nasprotujoče mreže in prenos umetniškega stila](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](./lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [Zaznavanje predmetov](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](./lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [Laboratorij](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [Semantična segmentacija. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)             |  |
| V  |            [**Obdelava naravnega jezika**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [Raziskuj obdelavo naravnega jezika na Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [Predstavitev besedila. Bow/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [Semantični vgrajeni zapisi besed. Word2Vec in GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [Modeliranje jezika. Usposabljanje lastnih vgrajenih zapisov](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [Laboratorij](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [Rekurentne nevronske mreže](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [Generativne rekurentne mreže](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)             | [Laboratorij](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Transformatorji. BERT.](./lessons/5-NLP/18-Transformers/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [Prepoznavanje poimenovanih entitet](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [Laboratorij](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [Veliki jezikovni modeli, programiranje navodil in naloge z malo primeri](./lessons/5-NLP/20-LangModels/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **Druge tehnike umetne inteligence** || |
| 21  |            [Genetski algoritmi](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Zvezek](./lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [Globoko učenje z okrepljenjem](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](./lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](./lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [Laboratorij](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [Sistemi z več agenti](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **Etika umetne inteligence** | | |
| 24  |            [Etika umetne inteligence in odgovorna umetna inteligenca](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: Načela odgovorne umetne inteligence](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **Dodatki** | | |
| 25  |            [Večmodalne mreže, CLIP in VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Zvezek](./lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## Vsaka lekcija vsebuje

* Material za predhodno branje
* Izvršljive Jupyter zvezke, ki so pogosto specifični za ogrodje (**PyTorch** ali **TensorFlow**). Izvršljivi zvezek vsebuje tudi veliko teoretičnega gradiva, zato je za razumevanje teme potrebno prebrati vsaj eno različico zvezka (bodisi PyTorch ali TensorFlow).
* **Laboratorije** na voljo za nekatere teme, ki vam omogočajo, da preizkusite uporabo naučenega gradiva na določenem problemu.
* Nekateri razdelki vsebujejo povezave do modulov [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum), ki pokrivajo sorodne teme.

## Začni

### 🎯 Nov v AI? Začni tukaj!

Če ste popolnoma novi v AI in želite hitre, praktične primere, si oglejte naše [**Primere za začetnike**](./examples/README.md)! Ti vključujejo:

- 🌟 **Pozdravljen AI svet** - vaš prvi program AI (prepoznavanje vzorcev)
- 🧠 **Preprosta nevronska mreža** - zgradite nevronsko mrežo iz nič  

- 🖼️ **Razvrščevalnik slik** - Razvrsti slike z obširnimi komentarji  
- 💬 **Sentiment besedila** - Analiza pozitivnega/negativnega besedila  

Ti primeri so oblikovani tako, da vam pomagajo razumeti pojme umetne inteligence, preden se lotite celotnega učnega načrta.

### 📚 Nastavitev celotnega učnega načrta

- Ustvarili smo [nastavitveno lekcijo](./lessons/0-course-setup/setup.md), ki vam pomaga pri nastavitvi razvojnega okolja. - Za izobraževalce smo pripravili tudi [lekcijo o nastavitvi učnih načrtov](./lessons/0-course-setup/for-teachers.md)!
- Kako [pognati kodo v VSCode ali Codespace](./lessons/0-course-setup/how-to-run.md)  

Sledite tem korakom:

Odvežite repozitorij: Kliknite na gumb "Fork" v zgornjem desnem kotu te strani.  

Klonirajte repozitorij: `git clone https://github.com/microsoft/AI-For-Beginners.git`  

Ne pozabite tej repozitorij dati zvezdico (🌟), da ga boste lažje našli kasneje.

## Spoznajte druge udeležence

Pridružite se našemu [uradnemu AI Discord strežniku](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum), da spoznate in se povežete z drugimi udeleženci tečaja ter dobite podporo.

Če imate povratne informacije o izdelku ali vprašanja med razvojem, obiščite naš [Azure AI Foundry Developer Forum](https://aka.ms/foundry/forum)

## Kvizi

> **Opomba o kvizih**: Vsi kvizi so nameščeni v mapi Quiz-app v etc\quiz-app ali [spletno tukaj](https://ff-quizzes.netlify.app/). Povezani so znotraj lekcij, kviz aplikacijo je mogoče pognati lokalno ali namestiti v Azure; sledite navodilom v mapi `quiz-app`. Postopoma se lokalizirajo.

## Iščemo pomoč

Imate predloge ali ste našli pravopisne ali kodne napake? Odprite issue ali ustvarite pull request.

## Posebne zahvale

* **✍️ Glavni avtor:** [Dmitry Soshnikov](http://soshnikov.com), PhD  
* **🔥 Urednik:** [Jen Looper](https://twitter.com/jenlooper), PhD  
* **🎨 Ilustrator sketchnotov:** [Tomomi Imura](https://twitter.com/girlie_mac)  
* **✅ Ustvarjalec kvizov:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)  
* **🙏 Glavni sodelavci:** [Evgenii Pishchik](https://github.com/Pe4enIks)  

## Drugi učni načrti

Naša ekipa ustvarja tudi druge učne načrte! Oglejte si:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agenti
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Serija generativne AI
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### Osnovno učenje
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Serija Copilot
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Dobite pomoč

Če se zataknete ali imate kakršnakoli vprašanja glede ustvarjanja AI aplikacij. Pridružite se ostalim udeležencem in izkušenim razvijalcem v razpravah o MCP. Gre za podporno skupnost, kjer so vprašanja dobrodošla in se znanje prosto deli.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Če imate povratne informacije o izdelku ali napake med razvojem, obiščite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da avtomatski prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj velja za zanesljiv vir. Za ključne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->