<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85102ce4bfab31103e99dc8ca2e2f181",
  "translation_date": "2026-01-16T05:34:49+00:00",
  "source_file": "README.md",
  "language_code": "sr"
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

# Вештачка интелигенција за почетнике - Наставни план

|![Sketchnote by @girlie_mac https://twitter.com/girlie_mac](../../../../translated_images/sr/ai-overview.0857791951d19500.webp)|
|:---:|
| AI For Beginners - _Скетчнот од [@girlie_mac](https://twitter.com/girlie_mac)_ |

Истражите свет **Вештачке интелигенције** (AI) са нашим 12-недељним, 24-лекцијским наставним планом! Обухвата практичне лекције, квизове и лабораторијске задатке. Наставни план је прилагођен почетницима и покрива алате као што су TensorFlow и PyTorch, као и етику у AI

### 🌐 Подршка за више језика

#### Подржано преко GitHub Action (аутоматизовано и увек ажурирано)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](./README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Више волите да клонирате локално?**

> Овај репозиторијум укључује преко 50 превода што значајно повећава величину преузимања. Да бисте клонирали без превода, користите sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git
> cd AI-For-Beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Ово вам даје све што вам је потребно за завршавање курса са много бржим преузимањем.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ако желите да додатни језици буду подржани, они су наведени [овде](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Придружите се заједници
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

## Шта ћете научити

**[Ментална мапа курса](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

У овом наставном плану ћете научити:

* Различите приступе Вештачкој интелигенцији, укључујући "добар стари" симболички приступ са **Представљањем знања** и резоновањем ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
* **Нервне мреже** и **Дубоко учење**, које су у срцу модерне AI. Илустроваћемо концепте иза ових важних тема користећи код у два од најпопуларнијих фрејмворка - [TensorFlow](http://Tensorflow.org) и [PyTorch](http://pytorch.org).
* **Нервне архитектуре** за рад са сликама и текстом. Покрићемо новије моделе али можда ћемо мало заостати за најмодернијим стањем.
* Мање популарне AI приступе, као што су **Генетски алгоритми** и **Мулти-агентски системи**.

Шта нећемо покрити у овом наставном плану:

> [Пронађите све додатне ресурсе за овај курс у нашој Microsoft Learn колекцији](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)

* Пословне случајеве коришћења **AI у пословању**. Размотрите узимање [Увода у AI за пословне кориснике](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) на Microsoft Learn, или [AI Пословне школе](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum), развијене у сарадњи са [INSEAD](https://www.insead.edu/).
* **Класично машинско учење**, које је добро описано у нашем [Плану учења Машинско учење за почетнике](http://github.com/Microsoft/ML-for-Beginners).
* Практичне AI апликације изграђене коришћењем **[Когнитивних услуга](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)**. За ово препоручујемо да почнете са Microsoft Learn модулима за [видио](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum), [природну обраду језика](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum), **[Генеративни AI са Azure OpenAI сервисом](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** и друге.
* Специфичне ML **Cloud фрејмворке**, као што су [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum), [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum), или [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum). Размотрите коришћење [Изградње и управљања машинским учењем са Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) и [Изградње и управљања машинским учењем са Azure Databricks](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum) планова учења.
* **Разговорни AI** и **Чет ботове**. Постоји посебан [Креирај разговорна AI решења](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum) план учења, а можете погледати и [овaj блог пост](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) за више детаља.
* **Дубока математика** иза дубоког учења. За ово препоручујемо [Дубоко учење](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) аутора Иана Гудфелоу, Јошуа Бенгио и Аарона Коурвила, која је доступна и онлајн на [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).

За благи увод у теме _AI у облаку_ можете размотрити [Почните са вештачком интелигенцијом на Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum) план учења.

# Садржај

|     |                                                                 Лекција                                                  |                                           PyTorch/Keras/TensorFlow                                          | Лабораторијски задатак                                    |
| :-: | :--------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | -------------------------------------------------------- |
| 0  |                                 [Подешавање курса](./lessons/0-course-setup/setup.md)                                |                      [Подеси свој развојни амбијент](./lessons/0-course-setup/how-to-run.md)                       |                                                          |
| I  |               [**Увод у AI**](./lessons/1-Intro/README.md)                                                         |                                                                                                       |                                                          |
| 01  |       [Увод и историја AI](./lessons/1-Intro/README.md)                                                            |           -                                                                                           | -                                                        |
| II |              **Симболичка AI**                                                                                       |
| 02  |       [Представљање знања и експертски системи](./lessons/2-Symbolic/README.md)                                       |            [Експертски системи](./lessons/2-Symbolic/Animals.ipynb) /  [Онтологија](./lessons/2-Symbolic/FamilyOntology.ipynb) /[Граф концепата](./lessons/2-Symbolic/MSConceptGraph.ipynb)                             |                                                          |
| III |                        [**Увод у нервне мреже**](./lessons/3-NeuralNetworks/README.md)                                  |                                                                                                       |                                                          |
| 03  |                [Перцептрон](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Бележница](./lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [Лаб](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 04  |                   [Вишеслојни перцептрон и креирање нашег оквира](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Бележница](./lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [Лаб](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 05  |            [Увод у оквире (PyTorch/TensorFlow) и пренаглашавање](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](./lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](./lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Лаб](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV  |            [**Компјутерски вид**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [Истражи Компјутерски вид на Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |
| 06  |            [Увод у компјутерски вид. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Бележница](./lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [Лаб](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 07  |            [Конволуционе неуронске мреже](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [CNN архитектуре](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](./lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](./lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [Лаб](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 08  |            [Претрениране мреже и преносно учење](./lessons/4-ComputerVision/08-TransferLearning/README.md) и [Тренинг трикови](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](./lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Лаб](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [Аутоенкодери и VAE-ови](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](./lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [Генеративне принципе мреже и пренос уметничког стила](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](./lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [Детекција објеката](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](./lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [Лаб](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [Семантичка сегментација. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)             |  |
| V  |            [**Обрада природног језика**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [Истражи Обраду природног језика на Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [Представљање текста. Bow/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [Семантички уградљиви вектори речи. Word2Vec и GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [Моделирање језика. Тренирање сопствених уградњи](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [Лаб](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [Рекурентне неуронске мреже](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [Генеративне рекурентне мреже](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)             | [Лаб](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Трансформери. BERT.](./lessons/5-NLP/18-Transformers/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [Препознавање именованих ентитета](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [Лаб](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [Велики језички модели, програмирање упита и Few-Shot задаци](./lessons/5-NLP/20-LangModels/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **Остале AI технике** || |
| 21  |            [Генетски алгоритми](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Бележница](./lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [Дубоко учење појачања](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](./lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](./lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [Лаб](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [Вишеразински системи](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **AI етика** | | |
| 24  |            [Етика AI и одговорни AI](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: Начела одговорног AI-а](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **Додатно** | | |
| 25  |            [Вишемодалне мреже, CLIP и VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Бележница](./lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## Ће урок садржи

* Материјал за претходно читање
* Извршне Jupyter бележнице, које су често специфичне за оквир (**PyTorch** или **TensorFlow**). Извршна бележница такође садржи много теоријског материјала, па да бисте разумели тему потребно је да прођете кроз бар једну верзију бележнице (било PyTorch или TensorFlow).
* **Лабораторије** доступне за неке теме, које вам омогућавају да пробате применити научени материјал на конкретан проблем.
* Неке секције садрже линкове ка [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) модулима који покривају сродне теме.

## Почетак

### 🎯 Нов у AI? Почни овде!

Ако си потпуно нов у AI и желиш брзе, практичне примере, погледај наше [**Пријатељске примере за почетнике**](./examples/README.md)! Ово укључује:

- 🌟 **Здраво AI света** - Твој први AI програм (препознавање образаца)
- 🧠 **Једноставна неуронска мрежа** - Направи неуронску мрежу од нуле  
- 🖼️ **Класификатор слика** - Класификуј слике са детаљним коментарима
- 💬 **Сентимент текста** - Анализа позитивног/негативног текста

Ови примери су осмишљени да вам помогну да разумете концепте вештачке интелигенције пре него што зароните у цео курикулум.

### 📚 Подешавање пуног курикулума

- Направили смо [лекцију за подешавање](./lessons/0-course-setup/setup.md) да вам помогнемо са подешавањем развојног окружења. - За наставнике, направили смо и [лекцију за подешавање курикулума](./lessons/0-course-setup/for-teachers.md)!
- Како да [покренете код у VSCode или Codespace](./lessons/0-course-setup/how-to-run.md)

Пратите ове кораке:

Направите форк репозиторијума: Кликните на дугме „Fork“ у горњем десном углу ове странице.

Клонирајте репозиторијум: `git clone https://github.com/microsoft/AI-For-Beginners.git`

Не заборавите да ставите звездицу (🌟) овом репозиторијуму да бисте га касније лакше пронашли.

## Упознајте друге учеснике

Придружите се нашем [званичном AI Discord серверу](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum) да упознате и умрежите се са другим учесницима овог курса и добијете подршку.

Ако имате повратне информације о производу или питања током израде посетите наш [Azure AI Foundry Developer Forum](https://aka.ms/foundry/forum)

## Квизови

> **Напомена о квизовима**: Сви квизови су садржани у фасцикли Quiz-app у etc\quiz-app, или [онлајн овде](https://ff-quizzes.netlify.app/) Они су повезани изнутра у лекцијама, квиз апликација може да се покрене локално или да се инсталира на Azure; пратите упутства у фасцикли `quiz-app`. Полако се лоцализују.

## Тражи се помоћ

Имате ли предлоге или сте пронашли правописне или код грешке? Отворите issue или направите pull request.

## Посебне захвалности

* **✍️ Главни аутор:** [Дмитриј Сошников](http://soshnikov.com), доктор наука
* **🔥 Уредник:** [Џен Лупер](https://twitter.com/jenlooper), доктор наука
* **🎨 Илустратор скичнота:** [Томоми Имура](https://twitter.com/girlie_mac)
* **✅ Креатор квизова:** [Латифа Белло](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)
* **🙏 Основни сарадници:** [Евгениј Пишчик](https://github.com/Pe4enIks)

## Остали курикулуми

Наш тим производи и друге курикулуме! Погледајте:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agents
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Generative AI Series
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Core Learning
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Copilot Series
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Како добити помоћ

Ако сте заглављени или имате било каквих питања о изради AI апликација. Придружите се осталим ученицима и искусним програмерима у дискусијама о MCP. То је подржавајућа заједница у којој су питања добродошла и знање се слободно дели.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ако имате повратне информације о производу или грешке током израде посетите:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Одрицање одговорности**:  
Овај документ је преведен помоћу AI услуге за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било какве неспоразуме или погрешна тумачења која произилазе из коришћења овог превода.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->