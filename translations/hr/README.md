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

# Umjetna inteligencija za početnike - Nastavni plan

|![Sketchnote @girlie_mac https://twitter.com/girlie_mac](https://github.com/microsoft/AI-For-Beginners/raw/main/lessons/sketchnotes/ai-overview.png)|
|:---:|
| AI za početnike - _Sketchnote autorice [@girlie_mac](https://twitter.com/girlie_mac)_ |

Istražite svijet **umjetne inteligencije** (AI) kroz naš 12-tjedni, 24-lekcijski nastavni plan! Obuhvaća praktične lekcije, kvizove i laboratorijske vježbe. Nastavni plan je prilagođen početnicima i pokriva alate poput TensorFlow i PyTorch, kao i etiku u AI


### 🌐 Podrška za više jezika

#### Podržano putem GitHub akcije (automatizirano i uvijek ažurno)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](./README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Khmer](../km/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Radije želite klonirati lokalno?**
>
> Ovaj repozitorij uključuje više od 50 prijevoda jezika, što značajno povećava veličinu preuzimanja. Za kloniranje bez prijevoda koristite sparse checkout:
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
> Ovo vam daje sve što vam treba za dovršetak tečaja s puno bržim preuzimanjem.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ako želite dodatnu podršku za jezike prijevoda, podržani jezici su navedeni [ovdje](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Pridružite se zajednici
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

## Što ćete naučiti

**[Mindmap tečaja](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

U ovom nastavnom planu naučit ćete:

* Različite pristupe umjetnoj inteligenciji, uključujući "dobri stari" simbolički pristup s **predstavljanjem znanja** i rezoniranjem ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
* **Neuralne mreže** i **duboko učenje**, koje su u središtu moderne AI. Koncepte iza ovih važnih tema ilustrirat ćemo pomoću koda u dva najpopularnija okvira - [TensorFlow](http://Tensorflow.org) i [PyTorch](http://pytorch.org).
* **Neuralne arhitekture** za rad sa slikama i tekstom. Pokrit ćemo nove modele, iako možda ne sasvim najnovije iz stanja tehnike.
* Manje popularne AI pristupe kao što su **genetski algoritmi** i **sustavi s više agenata**.

Što nećemo pokrivati u ovom nastavnom planu:

> [Pronađite sve dodatne izvore za ovaj tečaj u našoj kolekciji Microsoft Learn](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)

* Poslovne primjene **AI u poslovanju**. Razmislite o pohađanju [Uvod u AI za poslovne korisnike](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) učne staze na Microsoft Learn, ili [AI Business School](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum), razvijene u suradnji s [INSEAD](https://www.insead.edu/).
* **Klasično strojno učenje**, koje je dobro opisano u našem [nastavnom planu Strojno učenje za početnike](http://github.com/Microsoft/ML-for-Beginners).
* Praktične AI primjene izgrađene korištenjem **[Kognitivnih usluga](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)**. Za to preporučujemo da započnete s modulima Microsoft Learn za [vid](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum), [obradu prirodnog jezika](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum), **[generativnu AI s Azure OpenAI uslugom](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** i druge.
* Specifične ML **Cloud okvire**, poput [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum), [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum), ili [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum). Razmotrite korištenje učnih staza [Izgradnja i upravljanje rješenjima strojnog učenja s Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) i [Izgradnja i upravljanje rješenjima strojnog učenja s Azure Databricks](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum).
* **Razgovorna AI** i **chat botovi**. Postoji zasebna [učna staza za kreiranje razgovornih AI rješenja](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum), a možete se također referirati na [ovaj blog post](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) za detaljnije informacije.
* **Duboku matematiku** iza dubokog učenja. Za to preporučujemo [Duboko učenje](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) autorstva Iana Goodfellowa, Yoshua Bengioa i Aarona Courvillea, koja je dostupna i online na [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).

Za nježan uvod u teme _AI u oblaku_, možete razmotriti pohađanje [Početak s umjetnom inteligencijom na Azureu](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum) učne staze.

# Sadržaj

|     |                                                                 Poveznica na lekciju                                                                  |                                           PyTorch/Keras/TensorFlow                                          | Laboratorijska vježba                                                            |
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |
| 0  |                                 [Postavljanje tečaja](./lessons/0-course-setup/setup.md)                                 |                      [Postavite svoje razvojno okruženje](./lessons/0-course-setup/how-to-run.md)                       |   |
| I  |               [**Uvod u AI**](./lessons/1-Intro/README.md)      | | |
| 01  |       [Uvod i povijest AI](./lessons/1-Intro/README.md)       |           -                            | -  |
| II |              **Simbolička AI**              |
| 02  |       [Predstavljanje znanja i ekspertni sustavi](./lessons/2-Symbolic/README.md)       |            [Ekspertni sustavi](./lessons/2-Symbolic/Animals.ipynb) /  [Ontologija](./lessons/2-Symbolic/FamilyOntology.ipynb) /[Graf koncepata](./lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |
| III |                        [**Uvod u neuronske mreže**](./lessons/3-NeuralNetworks/README.md) |||
| 03  |                [Perceptron](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Bilježnica](./lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [Laboratorij](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 04  |                   [Višeslojni perceptron i izrada vlastitog frameworka](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Bilježnica](./lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [Laboratorij](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 05  |            [Uvod u frameworke (PyTorch/TensorFlow) i prenaučavanje](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](./lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](./lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Laboratorij](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV  |            [**Računalni vid**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [Istražite računalni vid na Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |
| 06  |            [Uvod u računalni vid. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Bilježnica](./lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [Laboratorij](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 07  |            [Konvolucijske neuronske mreže](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [Arhitekture CNN-a](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](./lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](./lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [Laboratorij](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 08  |            [Prethodno istrenirane mreže i transferno učenje](./lessons/4-ComputerVision/08-TransferLearning/README.md) and [Trikovi za treniranje](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](./lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Laboratorij](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [Autoenkoderi i VAE](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](./lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [Generativne adversarijalne mreže i prijenos umjetničkog stila](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](./lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [Detekcija objekata](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](./lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [Laboratorij](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [Semantička segmentacija. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)             |  |
| V  |            [**Obrada prirodnog jezika**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [Istražite obradu prirodnog jezika na Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [Predstavljanje teksta. Bow/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [Semantički vektori riječi. Word2Vec i GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [Modeliranje jezika. Treniranje vlastitih vektora](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [Laboratorij](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [Rekurentne neuronske mreže](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [Generativne rekurentne mreže](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)             | [Laboratorij](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Transformeri. BERT.](./lessons/5-NLP/18-Transformers/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [Prepoznavanje imenovanih entiteta](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [Laboratorij](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [Veliki jezični modeli, prompt programiranje i few-shot zadaci](./lessons/5-NLP/20-LangModels/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **Druge AI tehnike** || |
| 21  |            [Genetski algoritmi](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Bilježnica](./lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [Duboko potkrepljujuće učenje](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](./lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](./lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [Laboratorij](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [Sustavi s više agenata](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **AI etika** | | |
| 24  |            [Etika AI i odgovorni AI](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: Principi odgovornog AI](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **Ostalo** | | |
| 25  |            [Multimodalne mreže, CLIP i VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Bilježnica](./lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## Svaka lekcija sadrži
* Materijal za predčitanje
* Izvršni Jupyter bilježnice, koje su često specifične za okvir (**PyTorch** ili **TensorFlow**). Izvršni bilježnica također sadrži mnogo teorijskog materijala, tako da za razumijevanje teme trebate proći kroz barem jednu verziju bilježnice (bilo PyTorch ili TensorFlow).
* **Laboratoriji** dostupni za neke teme, koji vam daju priliku da pokušate primijeniti naučeni materijal na određeni problem.
* Neki odjeljci sadrže poveznice na module [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) koji pokrivaju povezane teme.

## Početak

### 🎯 Novi u AI? Počnite ovdje!

Ako ste potpuno novi u AI i želite brze, praktične primjere, pogledajte naše [**Primjere prilagođene početnicima**](./examples/README.md)! Oni uključuju:

- 🌟 **Hello AI World** - Vaš prvi AI program (prepoznavanje uzoraka)
- 🧠 **Jednostavna neuronska mreža** - Izgradite neuronsku mrežu od nule  
- 🖼️ **Klasifikator slika** - Klasificirajte slike s detaljnim komentarima
- 💬 **Sentiment teksta** - Analizirajte pozitivan/negativan tekst

Ovi primjeri su dizajnirani da vam pomognu razumjeti AI koncepte prije nego što se upustite u puni kurikulum.

### 📚 Postavljanje kompletnog kurikuluma

- Kreirali smo [lekciju za postavljanje](./lessons/0-course-setup/setup.md) da vam pomognemo s postavljanjem razvojnog okruženja.
- Za predavače, također smo kreirali [lekciju za postavljanje kurikuluma](./lessons/0-course-setup/for-teachers.md)!
- Kako [pokrenuti kod u VSCode ili Codespace-u](./lessons/0-course-setup/how-to-run.md)

Slijedite ove korake:

Forkajte repozitorij: Kliknite na gumb "Fork" u gornjem desnom kutu ove stranice.

Klonirajte repozitorij: `git clone https://github.com/microsoft/AI-For-Beginners.git`

Ne zaboravite dodati zvjezdicu (🌟) ovom repozitoriju da biste ga kasnije lakše pronašli.

## Upoznajte druge učenike

Pridružite se našem [službenom AI Discord serveru](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum) da upoznate i umrežite se s drugim učenicima koji pohađaju ovaj tečaj i dobijete podršku.

Ako imate povratne informacije ili pitanja tijekom izrade, posjetite naš [Azure AI Foundry Developer Forum](https://aka.ms/foundry/forum)

## Kvizevi

> **Napomena o kvizovima**: Svi kvizovi se nalaze u mapi Quiz-app u etc\quiz-app, ili [online ovdje](https://ff-quizzes.netlify.app/). Povezani su iz lekcija, kviz aplikaciju je moguće pokretati lokalno ili je rasporediti na Azure; slijedite upute u `quiz-app` mapi. Postupno se lokaliziraju.

## Potrebna pomoć

Imate li prijedloge ili ste pronašli pravopisne ili kodne pogreške? Otvorite issue ili kreirajte pull request.

## Posebne zahvale

* **✍️ Glavni autor:** [Dmitry Soshnikov](http://soshnikov.com), PhD
* **🔥 Urednik:** [Jen Looper](https://twitter.com/jenlooper), PhD
* **🎨 Ilustrator skica:** [Tomomi Imura](https://twitter.com/girlie_mac)
* **✅ Kreator kvizova:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)
* **🙏 Glavni suradnici:** [Evgenii Pishchik](https://github.com/Pe4enIks)

## Ostali kurikulumi

Naš tim stvara i druge kurikulume! Pogledajte:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain for Beginners](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Agenti
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Serija generativnog AI
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

## Dobivanje pomoći

Ako zapnete ili imate bilo kakvih pitanja o izradi AI aplikacija, pridružite se ostalim učenicima i iskusnim programerima u raspravama o MCP. To je zajednica koja podržava, gdje su pitanja dobrodošla, a znanje se slobodno dijeli.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ako imate povratne informacije o proizvodu ili greške tijekom izrade, posjetite:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:
Ovaj dokument preveden je korištenjem AI usluge prijevoda [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba se smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili kriva tumačenja proizašla iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->