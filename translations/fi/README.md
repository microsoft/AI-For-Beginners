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

# Tekoäly aloittelijoille – Oppimäärä

|![Sketchnote by @girlie_mac https://twitter.com/girlie_mac](../../translated_images/fi/ai-overview.0857791951d19500.webp)|
|:---:|
| AI Aloittelijoille – _Sketchnote by [@girlie_mac](https://twitter.com/girlie_mac)_ |

Tutustu **tekoälyn** (AI) maailmaan 12 viikon ja 24 oppitunnin oppimäärällämme! Se sisältää käytännönläheisiä oppitunteja, testejä ja laboratorioita. Oppimäärä on aloittelijaystävällinen ja kattaa työkaluja kuten TensorFlow ja PyTorch, sekä tekoälyn etiikan.


### 🌐 Monikielinen tuki

#### Tuettu GitHub Actionin avulla (automaattinen ja aina ajan tasalla)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](./README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Haluatko mieluummin kloonata paikallisesti?**

> Tämä arkisto sisältää yli 50 kielikäännöstä, mikä kasvattaa latauskokoa merkittävästi. Kloonaa ilman käännöksiä käyttämällä sparse checkout -ominaisuutta:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git
> cd AI-For-Beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Saat kaiken tarvitsemasi kurssin suorittamiseen huomattavasti nopeammalla latauksella.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Jos haluat tuettavan lisäkielien käännöksiä, ne on listattu [tässä](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Liity yhteisöön
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

## Mitä opit

**[Kurssin miellekartta](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

Tässä oppimäärässä opit:

* Eri lähestymistapoja tekoälyyn, mukaan lukien "hyvä vanha" symbolinen lähestymistapa, johon kuuluu **Tiedon esittäminen** ja päättely ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
* **Neuroverkot** ja **Syväoppiminen**, jotka ovat modernin tekoälyn ytimessä. Selitämme näiden tärkeiden aiheiden perusteet koodin avulla kahdessa suosituimmassa kehikossa - [TensorFlow](http://Tensorflow.org) ja [PyTorch](http://pytorch.org).
* **Neuroarkkitehtuurit** kuvien ja tekstin käsittelyyn. Käytämme tuoreita malleja, mutta emme ehkä kata viimeisintä alan huippua.
* Vähemmän tunnettuja tekoälymenetelmiä, kuten **Geneettiset algoritmit** ja **Moniagenttijärjestelmät**.

Mitä emme käsittele tässä oppimäärässä:

> [Löydä kaikki lisäresurssit tälle kurssille Microsoft Learn -kokoelmastamme](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)

* Liiketapauksia **tekoälyn hyödyntämisestä liiketoiminnassa**. Suosittelemme ottamaan [Johdanto tekoälyyn liikkeenharjoittajille](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) -oppipolun Microsoft Learnissä tai [AI Business School](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum), joka on kehitetty yhteistyössä [INSEADin](https://www.insead.edu/) kanssa.
* **Perinteistä koneoppimista**, jota käsitellään hyvin meidän [Machine Learning for Beginners -oppimäärässämme](http://github.com/Microsoft/ML-for-Beginners).
* Käytännön tekoälysovelluksia, jotka on rakennettu **[Cognitive Services](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)** -palveluiden avulla. Aloita Microsoft Learniksen moduuleista, kuten [näkymä](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum), [luonnollisen kielen käsittely](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum), **[Generative AI Azuren OpenAI-palvelulla](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** ja muut.
* Tietyt ML:n **pilvikehykset**, kuten [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum), [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum) tai [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum). Suosittelemme oppipolkuja [Build and operate machine learning solutions with Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) ja [Build and Operate Machine Learning Solutions with Azure Databricks](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum).
* **Keskustelevaa tekoälyä** ja **Chat-botteja**. Tähän on olemassa erillinen [Create conversational AI solutions](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum) -oppipolku, ja voit lisäksi lukea [tästä blogikirjoituksesta](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) lisätietoja.
* **Syvää matematiikkaa** syväoppimisen taustalla. Tähän suosittelemme [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) -kirjaa, jonka ovat kirjoittaneet Ian Goodfellow, Yoshua Bengio ja Aaron Courville. Se on myös saatavilla verkossa osoitteessa [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).

Hellävaraisesta johdannosta _tekoälyyn pilvessä_ aiheisiin voit ottaa [Get started with artificial intelligence on Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum) -oppipolun.

# Sisältö

|     |                                                                 Lesson Link                                                                  |                                           PyTorch/Keras/TensorFlow                                          | Lab                                                            |
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |
| 0  |                                 [Kurssin asennus](./lessons/0-course-setup/setup.md)                                 |                      [Kehitysympäristön asennus](./lessons/0-course-setup/how-to-run.md)                       |   |
| I  |               [**Johdanto tekoälyyn**](./lessons/1-Intro/README.md)      | | |
| 01  |       [Johdanto ja tekoälyn historia](./lessons/1-Intro/README.md)       |           -                            | -  |
| II |              **Symbolinen tekoäly**              |
| 02  |       [Tiedon esittäminen ja asiantuntijajärjestelmät](./lessons/2-Symbolic/README.md)       |            [Asiantuntijajärjestelmät](./lessons/2-Symbolic/Animals.ipynb) /  [Ontologia](./lessons/2-Symbolic/FamilyOntology.ipynb) /[Käsitteiden verkko](./lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |
| III |                        [**Johdanto neuroverkkoihin**](./lessons/3-NeuralNetworks/README.md) |||
| 03  |                [Perceptroni](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Muistikirja](./lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [Labra](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 04  |                   [Monikerroksinen perceptroni ja oman kehyksen luominen](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Muistikirja](./lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [Labra](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 05  |            [Johdanto kehyksiin (PyTorch/TensorFlow) ja ylisovittaminen](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](./lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](./lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Labra](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV  |            [**Koneoppiminen näkökentässä**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [Tutustu koneoppimiseen Microsoft Azurella](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |
| 06  |            [Johdanto koneoppimiseen. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Muistikirja](./lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [Labra](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 07  |            [Konvoluutiohermoverkot](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [CNN-arkkitehtuurit](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](./lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](./lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [Labra](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 08  |            [Esikoulutetut verkot ja siirto-oppiminen](./lessons/4-ComputerVision/08-TransferLearning/README.md) ja [Koulutusvinkit](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](./lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Labra](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [Autokooderit ja VAE:t](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](./lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [Generatiiviset vastustukselliset verkot ja taiteellinen tyylinsiirto](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](./lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [Kohteen tunnistus](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](./lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [Labra](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [Semanttinen segmentointi. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)             |  |
| V  |            [**Luonnollisen kielen käsittely**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [Tutustu luonnollisen kielen käsittelyyn Microsoft Azurella](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [Tekstin esitys. Bow/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [Semanttiset sanamuisteet. Word2Vec ja GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [Kielimallinnus. Omien upotusten opettaminen](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [Labra](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [Toistuvat neuroverkot](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [Generatiiviset toistuvat verkot](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)             | [Labra](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Transformerit. BERT.](./lessons/5-NLP/18-Transformers/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [Nimettyjen entiteettien tunnistus](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [Labra](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [Suuret kielimallit, tehtäväkehotteiden ohjelmointi ja vähän esimerkkitehtäviä](./lessons/5-NLP/20-LangModels/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **Muut tekoälytekniikat** || |
| 21  |            [Geneettiset algoritmit](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Muistikirja](./lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [Syvä vahvistusoppiminen](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](./lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](./lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [Labra](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [Moniagenttijärjestelmät](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **Tekoälyn etiikka** | | |
| 24  |            [Tekoälyn etiikka ja vastuullinen tekoäly](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: Vastuullisen tekoälyn periaatteet](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **Ekstrat** | | |
| 25  |            [Monimodaaliset verkot, CLIP ja VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Muistikirja](./lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## Jokainen oppitunti sisältää

* Ennakkolukemateriaalia
* Suoritettavia Jupyter-muistikirjoja, jotka ovat usein kehyspesifisiä (**PyTorch** tai **TensorFlow**). Suoritettava muistikirja sisältää myös runsaasti teoreettista materiaalia, joten aiheen ymmärtämiseksi sinun tulee käydä läpi vähintään yksi versio muistikirjasta (joko PyTorch- tai TensorFlow-versio).
* Joillekin aiheille on saatavilla **labroja**, jotka antavat sinulle mahdollisuuden kokeilla oppimaasi käytännössä tietyn ongelman parissa.
* Joissakin osioissa on linkkejä [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) -moduuleihin, jotka käsittelevät aiheeseen liittyviä teemoja.

## Aloittaminen

### 🎯 Uusi tekoälyssä? Aloita tästä!

Jos olet täysin uusi tekoälyssä ja haluat nopeita, käytännönläheisiä esimerkkejä, tutustu [**Aloittelijaystävällisiin esimerkkeihin**](./examples/README.md)! Näihin sisältyy:

- 🌟 **Hei tekoäly maailma** - Ensimmäinen tekoälyohjelmasi (kuviomallien tunnistus)
- 🧠 **Yksinkertainen neuroverkko** - Rakenna neuroverkko alusta alkaen  

- 🖼️ **Kuvien luokittelija** - Luokittele kuvia yksityiskohtaisten kommenttien kanssa  
- 💬 **Tekstin sentimentti** - Analysoi positiivinen/negatiivinen teksti  

Nämä esimerkit on suunniteltu auttamaan sinua ymmärtämään tekoälyn käsitteitä ennen kuin sukellat koko opetussuunnitelmaan.

### 📚 Koko opetussuunnitelman asennus

- Olemme luoneet [asennusosion](./lessons/0-course-setup/setup.md) auttamaan kehitysympäristön määrittämisessä. - Opettajille olemme myös luoneet [opetussuunnitelman asennusosion](./lessons/0-course-setup/for-teachers.md)!  
- Kuinka [Suorittaa koodi VSCode- tai Codespace-ympäristössä](./lessons/0-course-setup/how-to-run.md)  

Seuraa näitä ohjeita:

Forkkaa arkisto: Klikkaa sivun oikeassa yläkulmassa olevaa "Fork"-painiketta.

Kloonaa arkisto: `git clone https://github.com/microsoft/AI-For-Beginners.git`

Älä unohda tähdätä (🌟) tätä repoa löytääksesi sen helpommin myöhemmin.

## Tapaa muut oppijat

Liity [viralliseen AI Discord -palvelimeemme](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum) tavataaksesi ja verkostoituaksesi muiden tämän kurssin opiskelijoiden kanssa ja saadaksesi tukea.

Jos sinulla on tuotepalautetta tai kysymyksiä rakentamisen aikana, käy [Azure AI Foundry -kehittäjäfoorumilla](https://aka.ms/foundry/forum)

## Kyselyt

> **Huomio kyselyistä**: Kaikki kyselyt löytyvät Quiz-app-kansiosta polussa etc\quiz-app, tai [verkossa täällä](https://ff-quizzes.netlify.app/). Ne on linkitetty oppituntien sisältä. Kyselysovellus voidaan suorittaa paikallisesti tai ottaa käyttöön Azureen; noudata ohjeita `quiz-app`-kansiossa. Ne lokalisoidaan vähitellen.

## Apua tarvitaan

Onko sinulla ehdotuksia tai oletko löytänyt kirjoitus- tai koodivirheitä? Luo issue tai pull request.

## Erityiskiitokset

* **✍️ Pääkirjoittaja:** [Dmitry Soshnikov](http://soshnikov.com), FT  
* **🔥 Toimittaja:** [Jen Looper](https://twitter.com/jenlooper), FT  
* **🎨 Sketchnote-kuvittaja:** [Tomomi Imura](https://twitter.com/girlie_mac)  
* **✅ Kyselyjen tekijä:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)  
* **🙏 Keskeiset osallistujat:** [Evgenii Pishchik](https://github.com/Pe4enIks)  

## Muut opetussuunnitelmat

Tiimimme tuottaa myös muita opetussuunnitelmia! Tutustu:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain  
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)  
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)  
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)  
---

### Azure / Edge / MCP / Agentit  
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)  

---
 
### Generatiivisen tekoälyn sarja  
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)  

---
 
### Perusopetus  
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)  

---
 
### Copilot-sarja  
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Apua saatavilla

Jos jumitut tai sinulla on kysyttävää tekoälysovellusten rakentamisesta, liity muiden oppijoiden ja kokeneiden kehittäjien keskusteluihin MCP:stä. Se on kannustava yhteisö, jossa kysymyksiä saa esittää ja tietoa jaetaan vapaasti.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Jos sinulla on tuotepalautetta tai virheitä rakentamisen aikana, käy:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, automaattisissa käännöksissä voi esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää virallisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä mahdollisesti aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->