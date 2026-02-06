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

# Umělá inteligence pro začátečníky – učební plán

|![Sketchnote by @girlie_mac https://twitter.com/girlie_mac](../../translated_images/cs/ai-overview.0857791951d19500.webp)|
|:---:|
| Umělá inteligence pro začátečníky - _Sketchnote od [@girlie_mac](https://twitter.com/girlie_mac)_ |

Prozkoumejte svět **umělé inteligence** (AI) s naším 12týdenním kurzem o 24 lekcích! Obsahuje praktické lekce, kvízy a laboratoře. Učební plán je přátelský pro začátečníky a zabývá se nástroji jako TensorFlow a PyTorch i etikou v AI.

### 🌐 Podpora více jazyků

#### Podporováno přes GitHub Action (automatizované & vždy aktuální)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](./README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Raději klonovat lokálně?**

> Tento repozitář obsahuje více než 50 jazykových překladů, což výrazně zvyšuje velikost stahování. Pro klonování bez překladů použijte sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git
> cd AI-For-Beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> To vám poskytne vše potřebné ke zvládnutí kurzu a stahování bude mnohem rychlejší.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Pokud chcete, aby byly podporovány další jazykové překlady, jejich seznam naleznete [zde](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Připojte se ke komunitě
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

## Co se naučíte

**[Myšlenková mapa kurzu](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

V tomto učebním plánu se naučíte:

* Různé přístupy k umělé inteligenci, včetně „dobrého starého“ symbolického přístupu s **reprezentací znalostí** a úsudkem ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
* **Neuronové sítě** a **hluboké učení**, které jsou jádrem moderní AI. Koncepty těchto důležitých témat ukážeme pomocí kódu ve dvou nejpopulárnějších frameworcích - [TensorFlow](http://Tensorflow.org) a [PyTorch](http://pytorch.org).
* **Neuronové architektury** pro práci s obrazem a textem. Pokryjeme nedávné modely, i když nemusíme být úplně na špičce současného vývoje.
* Méně populární přístupy k AI, jako jsou **genetické algoritmy** a **multiagentní systémy**.

Co tento učební plán nepokrývá:

> [Najděte všechny další zdroje pro tento kurz v naší kolekci Microsoft Learn](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)

* Případy využití **AI v podnikání**. Doporučujeme absolvovat učební cestu [Úvod do AI pro podnikové uživatele](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) na Microsoft Learn nebo [AI Business School](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum), vyvinutou ve spolupráci s [INSEAD](https://www.insead.edu/).
* **Klasické strojové učení**, které je dobře popsáno v našem [Učebním plánu strojového učení pro začátečníky](http://github.com/Microsoft/ML-for-Beginners).
* Praktické AI aplikace postavené pomocí **[Kognitivních služeb](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)**. Začít doporučujeme moduly na Microsoft Learn zaměřené na [vidění](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum), [zpracování přirozeného jazyka](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum), **[generativní AI s Azure OpenAI Service](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** a další.
* Specifické ML **cloudové frameworky**, jako je [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum), [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum) nebo [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum). Doporučujeme využít učební cesty [Build and operate machine learning solutions with Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) a [Build and Operate Machine Learning Solutions with Azure Databricks](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum).
* **Konverzační AI** a **chatboty**. Existuje samostatná učební cesta [Vytvořte konverzační AI řešení](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum), také si můžete přečíst [tento blogový příspěvek](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) pro podrobnější informace.
* **Hloubková matematika** za hlubokým učením. Doporučujeme knihu [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) od Iana Goodfellowa, Yoshuu Bengia a Aarona Courvilla, která je dostupná také online na [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).

Pro jemný úvod do témat _AI v cloudu_ můžete zvážit absolvování učební cesty [Začínáme s umělou inteligencí na Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum).

# Obsah

|     |                                                                 Odkaz na lekci                                                                  |                                           PyTorch/Keras/TensorFlow                                          | Laboratoř                                                            |
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |
| 0  |                                 [Nastavení kurzu](./lessons/0-course-setup/setup.md)                                 |                      [Nastavte si vývojové prostředí](./lessons/0-course-setup/how-to-run.md)                       |   |
| I  |               [**Úvod do AI**](./lessons/1-Intro/README.md)      | | |
| 01  |       [Úvod a historie AI](./lessons/1-Intro/README.md)       |           -                            | -  |
| II |              **Symbolická AI**              |
| 02  |       [Reprezentace znalostí a expertní systémy](./lessons/2-Symbolic/README.md)       |            [Expertní systémy](./lessons/2-Symbolic/Animals.ipynb) /  [Ontologie](./lessons/2-Symbolic/FamilyOntology.ipynb) /[Konceptuální graf](./lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |
| III |                        [**Úvod do neuronových sítí**](./lessons/3-NeuralNetworks/README.md) |||
| 03  |                [Perceptron](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Notebook](./lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [Laboratoř](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 04  |                   [Vícevrstvý perceptron a vytvoření vlastního frameworku](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Notebook](./lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [Laboratoř](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 05  |            [Úvod do frameworků (PyTorch/TensorFlow) a overfitting](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](./lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](./lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Laboratoř](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV  |            [**Počítačové vidění**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [Prozkoumat Počítačové vidění na Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |
| 06  |            [Úvod do počítačového vidění. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Notebook](./lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [Laboratoř](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 07  |            [Konvoluční neuronové sítě](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [Architektury CNN](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](./lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](./lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [Laboratoř](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 08  |            [Předtrénované sítě a transfer learning](./lessons/4-ComputerVision/08-TransferLearning/README.md) a [Triky při tréninku](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](./lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Laboratoř](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [Autoenkodéry a VAE](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](./lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [Generativní adversariální sítě a umělecký styl transfer](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](./lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [Detekce objektů](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](./lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [Laboratoř](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [Sémantická segmentace. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)             |  |
| V  |            [**Zpracování přirozeného jazyka**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [Prozkoumat zpracování přirozeného jazyka na Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [Reprezentace textu. Bow/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [Sémantické word embeddings. Word2Vec a GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [Modelování jazyka. Trénování vlastních embeddings](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [Laboratoř](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [Rekurentní neuronové sítě](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [Generativní rekurentní sítě](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)             | [Laboratoř](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Transformery. BERT.](./lessons/5-NLP/18-Transformers/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [Rozpoznávání pojmenovaných entit](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [Laboratoř](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [Velké jazykové modely, programování promptů a few-shot úlohy](./lessons/5-NLP/20-LangModels/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **Další AI techniky** || |
| 21  |            [Genetické algoritmy](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Notebook](./lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [Hluboké posilované učení](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](./lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](./lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [Laboratoř](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [Multiagentní systémy](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **Etika AI** | | |
| 24  |            [Etika AI a zodpovědná AI](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: Principy zodpovědné AI](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **Další materiály** | | |
| 25  |            [Multimodální sítě, CLIP a VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Notebook](./lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## Každá lekce obsahuje

* Materiály k předčtení
* Spustitelné Jupyter notebooky, které jsou často specifické pro framework (**PyTorch** nebo **TensorFlow**). Spustitelný notebook také obsahuje hodně teoretického materiálu, takže pro pochopení tématu je třeba projít alespoň jednu verzi notebooku (buď PyTorch nebo TensorFlow).
* **Laboratoře** dostupné pro některá témata, které vám dají příležitost vyzkoušet aplikaci naučeného materiálu na konkrétní problém.
* Některé sekce obsahují odkazy na moduly [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum), které pokrývají související témata.

## Začínáme

### 🎯 Jste noví v AI? Začněte zde!

Pokud jste v AI úplní začátečníci a chcete rychlé, praktické příklady, podívejte se na naše [**příklady pro začátečníky**](./examples/README.md)! Ty zahrnují:

- 🌟 **Hello AI World** - váš první AI program (rozpoznávání vzorů)  
- 🧠 **Jednoduchá neuronová síť** - postavte neuronovou síť od základů
- 🖼️ **Klasifikátor obrázků** - Klasifikujte obrázky s podrobnými komentáři
- 💬 **Sentiment textu** - Analyzujte pozitivní/negativní text

Tyto příklady jsou navrženy tak, aby vám pomohly pochopit koncepty AI předtím, než se ponoříte do celého kurikula.

### 📚 Nastavení celého kurikula

- Vytvořili jsme [lekci pro nastavení](./lessons/0-course-setup/setup.md), která vám pomůže s nastavením vašeho vývojového prostředí. - Pro pedagogy jsme také vytvořili [lekci pro nastavení kurikula](./lessons/0-course-setup/for-teachers.md)!
- Jak [spustit kód ve VSCode nebo Codespace](./lessons/0-course-setup/how-to-run.md)

Postupujte podle těchto kroků:

Forkujte repozitář: Klikněte na tlačítko "Fork" v pravém horním rohu této stránky.

Klonujte repozitář: `git clone https://github.com/microsoft/AI-For-Beginners.git`

Nezapomeňte tohoto repozitáře dát hvězdičku (🌟), abyste jej později snadněji našli.

## Poznejte další studenty

Připojte se k našemu [oficiálnímu AI Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum), kde se můžete setkat a navázat kontakty s dalšími studenty navštěvujícími tento kurz a získat podporu.

Pokud máte zpětnou vazbu k produktu nebo otázky během vývoje, navštivte náš [Azure AI Foundry Developer Forum](https://aka.ms/foundry/forum).

## Kvízy 

> **Poznámka ke kvízům**: Všechny kvízy jsou obsaženy ve složce Quiz-app v etc\quiz-app, nebo [online zde](https://ff-quizzes.netlify.app/). Jsou propojeny v lekcích a aplikace kvízů může být spuštěna lokálně nebo nasazena na Azure; postupujte podle instrukcí ve složce `quiz-app`. Postupně se lokalizují.

## Hledáme pomoc

Máte návrhy nebo jste našli překlepy či chyby v kódu? Založte issue nebo vytvořte pull request.

## Zvláštní poděkování

* **✍️ Hlavní autor:** [Dmitry Soshnikov](http://soshnikov.com), PhD
* **🔥 Editor:** [Jen Looper](https://twitter.com/jenlooper), PhD
* **🎨 Ilustrátor sketchnotů:** [Tomomi Imura](https://twitter.com/girlie_mac)
* **✅ Tvůrce kvízů:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)
* **🙏 Hlavní přispěvatelé:** [Evgenii Pishchik](https://github.com/Pe4enIks)

## Další kurikula

Náš tým vytváří i další kurikula! Podívejte se:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j pro začátečníky](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js pro začátečníky](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain pro začátečníky](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agenti
[![AZD pro začátečníky](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI pro začátečníky](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP pro začátečníky](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI agenti pro začátečníky](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Série Generativní AI
[![Generativní AI pro začátečníky](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generativní AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Jádro učení
[![ML pro začátečníky](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science pro začátečníky](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI pro začátečníky](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Kyberbezpečnost pro začátečníky](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Webový vývoj pro začátečníky](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT pro začátečníky](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![Vývoj XR pro začátečníky](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Série Copilot
[![Copilot pro AI párové programování](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot pro C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Dobrodružství](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Kde získat pomoc

Pokud se zaseknete nebo máte nějaké otázky o tvorbě AI aplikací, připojte se k dalším studentům a zkušeným vývojářům v diskusích o MCP. Je to podpůrná komunita, kde jsou otázky vítány a znalosti jsou sdíleny svobodně.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Pokud máte zpětnou vazbu k produktu nebo při vývoji narazíte na chyby, navštivte:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo mylné interpretace vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->