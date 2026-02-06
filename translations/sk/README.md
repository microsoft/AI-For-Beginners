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

# Umelá inteligencia pre začiatočníkov - učebný plán

|![Sketchnote by @girlie_mac https://twitter.com/girlie_mac](../../translated_images/sk/ai-overview.0857791951d19500.webp)|
|:---:|
| AI pre začiatočníkov - _Sketchnote od [@girlie_mac](https://twitter.com/girlie_mac)_ |

Preskúmajte svet **umelej inteligencie** (UI) s naším 12-týždňovým, 24-lekčným učebným plánom! Zahŕňa praktické lekcie, kvízy a laboratória. Učebný plán je priateľský pre začiatočníkov a pokrýva nástroje ako TensorFlow a PyTorch, ako aj etiku v UI.

### 🌐 Podpora viacerých jazykov

#### Podporované cez GitHub Action (Automatizované & vždy aktuálne)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](./README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Preferujete klonovať lokálne?**

> Tento repozitár obsahuje viac ako 50 jazykových prekladov, čo výrazne zvyšuje veľkosť stiahnutia. Ak chcete klonovať bez prekladov, použite sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git
> cd AI-For-Beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> To vám poskytne všetko potrebné na dokončenie kurzu s oveľa rýchlejším sťahovaním.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ak chcete podporu ďalších jazykov prekladov, sú uvedené [tu](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Pripojte sa ku komunite
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

## Čo sa naučíte

**[Myšlienková mapa kurzu](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

V tomto učebnom pláne sa naučíte:

* Rôzne prístupy k umelej inteligencii, vrátane "starého dobrého" symbolického prístupu s **reprezentáciou znalostí** a uvažovaním ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
* **Neuronové siete** a **hlboké učenie**, ktoré sú jadrom modernej UI. Koncepty za týmito dôležitými témami si vysvetlíme pomocou kódu v dvoch najpopulárnejších frameworkoch - [TensorFlow](http://Tensorflow.org) a [PyTorch](http://pytorch.org).
* **Neuronové architektúry** na prácu s obrázkami a textom. Pokryjeme nedávne modely, hoci možno nie úplne najmodernejšie.
* Menej populárne prístupy k UI, ako sú **genetické algoritmy** a **multi-agentné systémy**.

Čo nebudeme pokrývať v tomto učebnom pláne:

> [Nájdite všetky ďalšie zdroje pre tento kurz v našej Microsoft Learn kolekcii](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)

* Biznisové prípady používania **UI v podnikaní**. Zvážte absolvovanie vzdelávacej cesty [Úvod do AI pre obchodných používateľov](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) na Microsoft Learn, alebo [AI Business School](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum), vyvinutú v spolupráci s [INSEAD](https://www.insead.edu/).
* **Klasické strojové učenie**, ktoré je dobre popísané v našom [učebnom pláne Strojové učenie pre začiatočníkov](http://github.com/Microsoft/ML-for-Beginners).
* Praktické aplikácie UI postavené pomocou **[Kognitívnych služieb](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)**. Na to odporúčame začať modulmi Microsoft Learn pre [pozeranie](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum), [spracovanie prirodzeného jazyka](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum), **[Generatívnu AI s Azure OpenAI Service](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** a ďalšie.
* Špecifické ML **cloudové frameworky**, ako napríklad [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum), [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum) alebo [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum). Zvážte použitie vzdelávacích ciest [Vytvárajte a spravujte riešenia strojového učenia pomocou Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) a [Vytvárajte a spravujte riešenia strojového učenia s Azure Databricks](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum).
* **Konverzačnú AI** a **Chat Boty**. Existuje samostatná vzdelávacia cesta [Vytváranie konverzačných AI riešení](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum), a môžete tiež pozrieť [tento blogový príspevok](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) pre viac detailov.
* **Hlbokú matematiku** za hlbokým učením. Na to odporúčame knihu [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) od Iana Goodfellowa, Yoshua Bengia a Aarona Courvilla, ktorá je tiež dostupná online na [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).

Pre jemný úvod do tém _AI v cloude_ môžete zvážiť absolvovanie vzdelávacej cesty [Začať s umelou inteligenciou na Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum).

# Obsah

|     |                                                                 Odkaz na lekciu                                                                  |                                           PyTorch/Keras/TensorFlow                                          | Laboratórium                                                            |
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |
| 0  |                                 [Nastavenie kurzu](./lessons/0-course-setup/setup.md)                                 |                      [Nastavte si vývojové prostredie](./lessons/0-course-setup/how-to-run.md)                       |   |
| I  |               [**Úvod do UI**](./lessons/1-Intro/README.md)      | | |
| 01  |       [Úvod a história UI](./lessons/1-Intro/README.md)       |           -                            | -  |
| II |              **Symbolická UI**              |
| 02  |       [Reprezentácia znalostí a expertové systémy](./lessons/2-Symbolic/README.md)       |            [Expertové systémy](./lessons/2-Symbolic/Animals.ipynb) /  [Ontológia](./lessons/2-Symbolic/FamilyOntology.ipynb) /[Konceptuálny graf](./lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |
| III |                        [**Úvod do neuronových sietí**](./lessons/3-NeuralNetworks/README.md) |||
| 03  |                [Perceptrón](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Notebook](./lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [Laboratórium](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 04  |                   [Viacvrstvový perceptrón a vytvorenie vlastného frameworku](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Notebook](./lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [Laboratórium](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 05  |            [Úvod do frameworkov (PyTorch/TensorFlow) a overfitting](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](./lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](./lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Laboratórium](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV  |            [**Počítačové videnie**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [Preskúmajte počítačové videnie na Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |
| 06  |            [Úvod do počítačového videnia. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Notebook](./lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [Laboratórium](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 07  |            [Konvolučné neurónové siete](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [Architektúry CNN](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](./lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](./lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [Laboratórium](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 08  |            [Predtrénované siete a transfer learning](./lessons/4-ComputerVision/08-TransferLearning/README.md) a [Triky pri trénovaní](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](./lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Laboratórium](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [Autoenkódery a VAE](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](./lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [Generatívne adversariálne siete a umelecký štýl prenosu](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](./lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [Detekcia objektov](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](./lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [Laboratórium](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [Sémantická segmentácia. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)             |  |
| V  |            [**Spracovanie prirodzeného jazyka**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [Preskúmajte spracovanie prirodzeného jazyka na Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [Reprezentácia textu. Bow/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [Sémantické vektorové reprezentácie slov. Word2Vec a GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [Jazykové modelovanie. Tréning vlastných embeddingov](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [Laboratórium](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [Rekurentné neurónové siete](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [Generatívne rekurentné siete](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)             | [Laboratórium](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Transformery. BERT.](./lessons/5-NLP/18-Transformers/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [Rozpoznávanie pomenovaných entít](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [Laboratórium](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [Veľké jazykové modely, programovanie promptov a úlohy s málo príkladmi](./lessons/5-NLP/20-LangModels/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **Iné AI techniky** || |
| 21  |            [Genetické algoritmy](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Notebook](./lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [Hlboké posilňovacie učenie](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](./lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](./lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [Laboratórium](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [Viacagentové systémy](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **Etika AI** | | |
| 24  |            [Etika AI a zodpovedná AI](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: Zásady zodpovednej AI](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **Doplnky** | | |
| 25  |            [Multimodálne siete, CLIP a VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Notebook](./lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## Každá lekcia obsahuje

* Materiál na predčítanie
* Spustiteľné Jupyter notebooky, ktoré sú často špecifické pre framework (**PyTorch** alebo **TensorFlow**). Spustiteľný notebook zároveň obsahuje veľa teoretického materiálu, takže na pochopenie témy musíte prejsť aspoň jednou verziou notebooku (či už PyTorch alebo TensorFlow).
* **Laboratóriá** dostupné pri niektorých témach, ktoré vám dávajú príležitosť vyskúšať si aplikovať naučený materiál na konkrétny problém.
* Niektoré sekcie obsahujú odkazy na moduly [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum), ktoré pokrývajú súvisiace témy.

## Začínáme

### 🎯 Nový v AI? Začni tu!

Ak ste úplne nový v AI a chcete rýchle, praktické príklady, pozrite si naše [**Príklady pre začiatočníkov**](./examples/README.md)! Tieto zahŕňajú:

- 🌟 **Hello AI World** - váš prvý AI program (rozpoznávanie vzorov)
- 🧠 **Jednoduchá neurónová sieť** - Vytvorte neurónovú sieť od nuly  

- 🖼️ **Klasifikátor obrázkov** - Triedi obrázky s podrobnými komentármi
- 💬 **Sentiment textu** - Analyzuje pozitívny/negatívny text

Tieto príklady sú určené na to, aby vám pomohli pochopiť koncepty AI pred tým, než sa pustíte do celého kurikula.

### 📚 Nastavenie celého kurikula

- Vytvorili sme [lekciu o nastavení](./lessons/0-course-setup/setup.md), ktorá vám pomôže nastaviť vývojové prostredie. - Pre pedagógov sme pripravili aj [lekciu o nastavení kurikula](./lessons/0-course-setup/for-teachers.md)!
- Ako [spustiť kód vo VSCode alebo v Codespace](./lessons/0-course-setup/how-to-run.md)

Postupujte podľa týchto krokov:

Forknite Repository: Kliknite na tlačidlo "Fork" v pravom hornom rohu tejto stránky.

Skopírujte Repository: `git clone https://github.com/microsoft/AI-For-Beginners.git`

Nezabudnite zaradiť tento repozitár medzi svoje obľúbené (🌟), aby ste ho neskôr ľahšie našli.

## Spoznajte iných študentov

Pripojte sa k nášmu [oficiálnemu Discord serveru AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum), kde môžete nadviazať kontakty s inými študentmi, ktorí tento kurz absolvujú, a získať podporu.

Ak máte spätnú väzbu na produkt alebo otázky počas tvorby, navštívte náš [Azure AI Foundry Developer Forum](https://aka.ms/foundry/forum)

## Kvízy

> **Poznámka kvízov**: Všetky kvízy sú umiestnené v priečinku Quiz-app v etc\quiz-app, alebo [online tu](https://ff-quizzes.netlify.app/). Sú prepojené v rámci lekcií, aplikácia kvízov sa dá spustiť lokálne alebo nasadiť na Azure; riadi sa podľa inštrukcií v priečinku `quiz-app`. Postupne sa lokalizujú.

## Potrebná pomoc

Máte návrhy alebo ste našli pravopisné či kódové chyby? Vytvorte issue alebo pull request.

## Špeciálne poďakovanie

* **✍️ Hlavný autor:** [Dmitry Soshnikov](http://soshnikov.com), PhD
* **🔥 Editor:** [Jen Looper](https://twitter.com/jenlooper), PhD
* **🎨 Ilustrátor sketchnote:** [Tomomi Imura](https://twitter.com/girlie_mac)
* **✅ Tvorca kvízov:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)
* **🙏 Hlavní prispievatelia:** [Evgenii Pishchik](https://github.com/Pe4enIks)

## Iné kurikulá

Náš tím tiež vytvára ďalšie kurikulá! Pozrite si:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j pre začiatočníkov](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js pre začiatočníkov](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain pre začiatočníkov](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agentúry
[![AZD pre začiatočníkov](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pre začiatočníkov](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pre začiatočníkov](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agentúry pre začiatočníkov](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generatívne AI Série
[![Generatívne AI pre začiatočníkov](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generatívne AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generatívne AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generatívne AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Základné učenie
[![ML pre začiatočníkov](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Dátová veda pre začiatočníkov](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI pre začiatočníkov](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kyberbezpečnosť pre začiatočníkov](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webový vývoj pre začiatočníkov](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT pre začiatočníkov](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR vývoj pre začiatočníkov](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot séria
[![Copilot pre AI párované programovanie](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot pre C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot dobrodružstvo](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Získanie pomoci

Ak sa zaseknete alebo máte otázky ohľadom tvorby AI aplikácií, pripojte sa k ďalším študentom a skúseným vývojárom v diskusiách o MCP. Je to podporujúca komunita, kde sú otázky vítané a znalosti sa slobodne zdieľajú.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ak máte spätnú väzbu na produkt alebo chyby počas vývoja, navštívte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->