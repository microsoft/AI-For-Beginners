<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "07191303b7ea2aff1d47e2b0fe4bb862",
  "translation_date": "2025-08-29T22:50:25+00:00",
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

[![](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.gg/zxKYvhSnVp?WT.mc_id=academic-000002-leestott)  

# Вештачка интелигенција за почетнике - Наставни план

|![Илустрација од @girlie_mac https://twitter.com/girlie_mac](../../translated_images/ai-overview.0857791951d19500d0ef8b803d77110c738dcafc52306e6d68724742cd4af167.sr.png)|
|:---:|
| Вештачка интелигенција за почетнике - _Илустрација од [@girlie_mac](https://twitter.com/girlie_mac)_ |

Истражите свет **вештачке интелигенције** (AI) уз наш наставни план од 12 недеља и 24 лекције! Укључује практичне лекције, квизове и лабораторије. Наставни план је прилагођен почетницима и обухвата алате као што су TensorFlow и PyTorch, као и етику у области вештачке интелигенције.

### 🌐 Подршка за више језика

#### Подржано преко GitHub Action-а (аутоматски и увек ажурирано)

[French](../fr/README.md) | [Spanish](../es/README.md) | [German](../de/README.md) | [Russian](../ru/README.md) | [Arabic](../ar/README.md) | [Persian (Farsi)](../fa/README.md) | [Urdu](../ur/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Japanese](../ja/README.md) | [Korean](../ko/README.md) | [Hindi](../hi/README.md) | [Bengali](../bn/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Portuguese (Brazil)](../br/README.md) | [Italian](../it/README.md) | [Polish](../pl/README.md) | [Turkish](../tr/README.md) | [Greek](../el/README.md) | [Thai](../th/README.md) | [Swedish](../sv/README.md) | [Danish](../da/README.md) | [Norwegian](../no/README.md) | [Finnish](../fi/README.md) | [Dutch](../nl/README.md) | [Hebrew](../he/README.md) | [Vietnamese](../vi/README.md) | [Indonesian](../id/README.md) | [Malay](../ms/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Swahili](../sw/README.md) | [Hungarian](../hu/README.md) | [Czech](../cs/README.md) | [Slovak](../sk/README.md) | [Romanian](../ro/README.md) | [Bulgarian](../bg/README.md) | [Serbian (Cyrillic)](./README.md) | [Croatian](../hr/README.md) | [Slovenian](../sl/README.md) | [Ukrainian](../uk/README.md) | [Burmese (Myanmar)](../my/README.md)

**Ако желите да подржимо додатне језике, листа подржаних језика је доступна [овде](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Придружите се заједници
[![Azure AI Discord](https://dcbadge.limes.pink/api/server/kzRShWzttr)](https://discord.gg/kzRShWzttr)

## Шта ћете научити

**[Мапа курса](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

У овом наставном плану ћете научити:

* Различите приступе вештачкој интелигенцији, укључујући „добри стари“ симболички приступ са **репрезентацијом знања** и резоновањем ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
* **Неуронске мреже** и **дубоко учење**, који су у сржи савремене вештачке интелигенције. Концепте иза ових важних тема илустроваћемо кодом у два најпопуларнија оквира - [TensorFlow](http://Tensorflow.org) и [PyTorch](http://pytorch.org).
* **Неуронске архитектуре** за рад са сликама и текстом. Покрићемо новије моделе, али можда ћемо бити мање детаљни у погледу најсавременијих решења.
* Мање популарне приступе вештачкој интелигенцији, као што су **генетски алгоритми** и **системи са више агената**.

Шта нећемо покрити у овом наставном плану:

> [Пронађите све додатне ресурсе за овај курс у нашој Microsoft Learn колекцији](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)

* Пословне случајеве коришћења **вештачке интелигенције у пословању**. Размотрите курс [Увод у вештачку интелигенцију за пословне кориснике](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) на Microsoft Learn платформи или [AI Business School](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum), развијен у сарадњи са [INSEAD](https://www.insead.edu/).
* **Класично машинско учење**, које је добро описано у нашем [Наставном плану за машинско учење за почетнике](http://github.com/Microsoft/ML-for-Beginners).
* Практичне примене вештачке интелигенције изграђене коришћењем **[Cognitive Services](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)**. За ово препоручујемо да почнете са модулима Microsoft Learn за [визуелизацију](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum), [обраду природног језика](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum), **[Генеративну вештачку интелигенцију са Azure OpenAI Service](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** и друге.
* Специфичне ML **Cloud Frameworks**, као што су [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum), [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum), или [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum). Размотрите коришћење [Изградња и управљање решењима машинског учења са Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) и [Изградња и управљање решењима машинског учења са Azure Databricks](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum).
* **Конверзацијска вештачка интелигенција** и **чет-ботови**. Постоји посебан [Креирање решења за конверзацијску вештачку интелигенцију](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum) курс, а можете се обратити и [овом блогу](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) за више детаља.
* **Дубока математика** иза дубоког учења. За ово бисмо препоручили књигу [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) аутора Ian Goodfellow, Yoshua Bengio и Aaron Courville, која је такође доступна онлајн на [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).

За лаган увод у теме _вештачке интелигенције у облаку_, можете размотрити курс [Почетак рада са вештачком интелигенцијом на Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum).

# Садржај

|     |                                                                 Линк ка лекцији                                                                  |                                           PyTorch/Keras/TensorFlow                                          | Лабораторија                                                            |
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |
| 0  |                                 [Подешавање курса](./lessons/0-course-setup/setup.md)                                 |                      [Подешавање развојног окружења](./lessons/0-course-setup/how-to-run.md)                       |   |
| I  |               [**Увод у вештачку интелигенцију**](./lessons/1-Intro/README.md)      | | |
| 01  |       [Увод и историја вештачке интелигенције](./lessons/1-Intro/README.md)       |           -                            | -  |
| II |              **Симболичка вештачка интелигенција**              |
| 02  |       [Репрезентација знања и експертски системи](./lessons/2-Symbolic/README.md)       |            [Експертски системи](./lessons/2-Symbolic/Animals.ipynb) /  [Онтологија](./lessons/2-Symbolic/FamilyOntology.ipynb) /[Граф концепата](./lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |
| III |                        [**Увод у неуронске мреже**](./lessons/3-NeuralNetworks/README.md) |||
| 03  |                [Перцептрон](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Бележница](./lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [Лабораторија](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 04  |                   [Вишеслојни перцептрон и креирање сопственог оквира](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Бележница](./lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [Лабораторија](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 05  |            [Увод у оквире (PyTorch/TensorFlow) и пренапрегнутост](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](./lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](./lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Лабораторија](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV  |            [**Рачунарски вид**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [Истражите рачунарски вид на Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |
| 06  |            [Увод у рачунарски вид. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Бележница](./lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [Лабораторија](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 07  |            [Конволуционе неуронске мреже](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [Архитектуре CNN](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](./lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](./lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [Лабораторија](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 08  |            [Унапред обучене мреже и трансфер учење](./lessons/4-ComputerVision/08-TransferLearning/README.md) и [Трикови за обуку](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](./lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Лабораторија](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [Аутоенкодери и варијациони аутоенкодери (VAEs)](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](./lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [Генеративне супарничке мреже и пренос уметничког стила](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](./lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [Детекција објеката](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](./lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [Лабораторија](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [Семантичка сегментација. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)             |  |
| V  |            [**Обрада природног језика**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [Истражите обраду природног језика на Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [Репрезентација текста. Bow/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](./lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](./lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [Семантички уграђени вектори речи. Word2Vec и GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](./lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](./lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [Моделирање језика. Обука сопствених уграђених вектора](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](./lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](./lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [Лабораторија](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [Рекурентне неуронске мреже](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](./lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](./lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [Генеративне рекурентне мреже](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](./lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.md) / [TensorFlow](./lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.md)             | [Лабораторија](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Трансформери. BERT.](./lessons/5-NLP/18-Transformers/READMEtransformers.md)             |           [PyTorch](./lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](./lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [Препознавање именованих ентитета](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](./lessons/5-NLP/19-NER/NER-TF.ipynb)             | [Лабораторија](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [Велики језички модели, програмирање упита и задаци са мало примера](./lessons/5-NLP/20-LangModels/READMELargeLang.md)             |           [PyTorch](./lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **Остале технике вештачке интелигенције** || |
| 21  |            [Генетски алгоритми](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Бележница](./lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [Дубоко појачано учење](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](./lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](./lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [Лабораторија](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [Системи са више агената](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **Етика вештачке интелигенције** | | |
| 24  |            [Етика вештачке интелигенције и одговорна вештачка интелигенција](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: Принципи одговорне вештачке интелигенције](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **Додаци** | | |
| 25  |            [Мултимодалне мреже, CLIP и VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Бележница](./lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## Свака лекција садржи

* Материјал за претходно читање
* Извршиве Jupyter бележнице, које су често специфичне за оквир (**PyTorch** или **TensorFlow**). Извршива бележница такође садржи доста теоријског материјала, тако да је за разумевање теме потребно проћи барем једну верзију бележнице (или PyTorch или TensorFlow).
* **Лабораторије** доступне за неке теме, које вам пружају прилику да примените научени материјал на одређени проблем.
* Неки делови садрже линкове ка [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) модулима који покривају повезане теме.

## Почетак

- Направили смо [лекцију за подешавање](./lessons/0-course-setup/setup.md) како бисмо вам помогли у подешавању развојног окружења. - За едукаторе, направили смо и [лекцију за подешавање наставног плана](./lessons/0-course-setup/for-teachers.md)!
- Како [покренути код у VSCode или Codepace-у](./lessons/0-course-setup/how-to-run.md)

Пратите ове кораке:

Форкујте репозиторијум: Кликните на дугме "Fork" у горњем десном углу ове странице.

Клонирајте репозиторијум: `git clone https://github.com/microsoft/AI-For-Beginners.git`

Не заборавите да означите (🌟) овај репозиторијум како бисте га лакше пронашли касније.

## Упознајте друге учеснике

Придружите се нашем [званичном AI Discord серверу](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum) како бисте упознали и умрежили се са другим учесницима који похађају овај курс и добили подршку.

Ако имате повратне информације о производу или питања током изградње, посетите наш [Azure AI Foundry Developer Forum](https://aka.ms/foundry/forum)

## Квизови
> **Напомена о квизовима**: Сви квизови се налазе у фасцикли Quiz-app у etc\quiz-app, или [онлајн овде](https://ff-quizzes.netlify.app/). Повезани су са лекцијама, а апликација за квизове може се покренути локално или поставити на Azure; пратите упутства у фасцикли `quiz-app`. Постепено се локализују.
## Потребна Помоћ

Имате предлоге или сте пронашли правописне или програмске грешке? Отворите питање или направите pull request.

## Посебна Захвалност

* **✍️ Главни аутор:** [Дмитриј Сошњиков](http://soshnikov.com), доктор наука
* **🔥 Уредник:** [Џен Лупер](https://twitter.com/jenlooper), доктор наука
* **🎨 Илустратор скетчнота:** [Томоми Имура](https://twitter.com/girlie_mac)
* **✅ Креатор квиза:** [Латифа Бело](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)
* **🙏 Главни сарадници:** [Јевгениј Пишчик](https://github.com/Pe4enIks)

## Остали Курикулуми

Наш тим креира и друге курикулуме! Погледајте:

- [Генеративна вештачка интелигенција за почетнике](https://aka.ms/genai-beginners)
- [Генеративна вештачка интелигенција за почетнике .NET](https://github.com/microsoft/Generative-AI-for-beginners-dotnet)
- [Генеративна вештачка интелигенција са JavaScript-ом](https://github.com/microsoft/generative-ai-with-javascript)
- [Генеративна вештачка интелигенција са Java-ом](https://github.com/microsoft/Generative-AI-for-beginners-java)
- [Вештачка интелигенција за почетнике](https://aka.ms/ai-beginners)
- [Наука о подацима за почетнике](https://aka.ms/datascience-beginners)
- [Машинско учење за почетнике](https://aka.ms/ml-beginners)
- [Сајбер безбедност за почетнике](https://github.com/microsoft/Security-101) 
- [Веб развој за почетнике](https://aka.ms/webdev-beginners)
- [Интернет ствари (IoT) за почетнике](https://aka.ms/iot-beginners)
- [XR развој за почетнике](https://github.com/microsoft/xr-development-for-beginners)
- [Усавршавање GitHub Copilot-а за агентску употребу](https://github.com/microsoft/Mastering-GitHub-Copilot-for-Paired-Programming)
- [Усавршавање GitHub Copilot-а за C#/.NET програмере](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers)
- [Изаберите своју авантуру са Copilot-ом](https://github.com/microsoft/CopilotAdventures)

---

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуге за превођење помоћу вештачке интелигенције [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде тачан, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не преузимамо одговорност за било каква погрешна тумачења или неспоразуме који могу настати услед коришћења овог превода.