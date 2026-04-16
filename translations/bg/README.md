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

# Изкуствен интелект за начинаещи - Учебна програма

|![Sketchnote by @girlie_mac https://twitter.com/girlie_mac](https://github.com/microsoft/AI-For-Beginners/raw/main/lessons/sketchnotes/ai-overview.png)|
|:---:|
| AI For Beginners - _Скетчноут от [@girlie_mac](https://twitter.com/girlie_mac)_ |

Изследвайте света на **Изкуствения интелект** (ИИ) с нашата 12-седмична програма с 24 урока! Включва практически уроци, викторини и лабораторни упражнения. Учебната програма е подходяща за начинаещи и обхваща инструменти като TensorFlow и PyTorch, както и етика в ИИ


### 🌐 Поддръжка на множество езици

#### Поддържа се чрез GitHub Action (Автоматично и винаги актуално)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](./README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Предпочитате да клонирате локално?**
>
> Това хранилище включва над 50 езикови превода, което значително увеличава размера на изтегляне. За да клонирате без преводи, използвайте sparse checkout:
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
> Това ви дава всичко необходимо за завършване на курса с много по-бързо изтегляне.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Ако желаете да имате допълнителни поддържани езици за превод, те са изброени [тук](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Присъединете се към общността
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

## Какво ще научите

**[Ментална карта на курса](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

В тази учебна програма ще научите:

* Различни подходи към изкуствения интелект, включително "добрия стар" символен подход с **Представяне на знанието** и разсъждаване ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
* **Невронни мрежи** и **Дълбоко обучение**, които са в основата на съвременния ИИ. Ще илюстрираме концепциите зад тези важни теми с код в две от най-популярните рамки - [TensorFlow](http://Tensorflow.org) и [PyTorch](http://pytorch.org).
* **Невронни архитектури** за работа с изображения и текст. Ще покрием последни модели, но може да липсва малко от съвременния елит.
* По-малко популярни подходи в ИИ, като **Генетични алгоритми** и **Мултиагентни системи**.

Какво няма да покриваме в тази учебна програма:

> [Намерете всички допълнителни ресурси за този курс в нашата колекция в Microsoft Learn](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)

* Бизнес случаи за използване на **ИИ в бизнеса**. Помислете да вземете учебния път [Въведение в ИИ за бизнес потребители](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) в Microsoft Learn, или [AI Business School](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum), разработен в сътрудничество с [INSEAD](https://www.insead.edu/).
* **Класическо машинно обучение**, което е добре описано в нашата [Учебна програма за машинно обучение за начинаещи](http://github.com/Microsoft/ML-for-Beginners).
* Практически ИИ приложения, изградени с помощта на **[Когнитивни услуги](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)**. За това препоръчваме да започнете с Microsoft Learn модули за [компютърно зрение](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum), [обработка на естествен език](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum), **[Генеративен ИИ с Azure OpenAI Service](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** и други.
* Специфични ML **Облачни рамки**, като [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum), [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum) или [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum). Помислете да използвате учебните пътища [Създаване и опериране на решения за машинно обучение с Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) и [Създаване и опериране на решения за машинно обучение с Azure Databricks](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum).
* **Разговорен ИИ** и **Чат ботове**. Съществува отделен учебен път [Създаване на разговорни AI решения](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum), както и можете да се обърнете към [този блог пост](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) за повече детайли.
* **Дълбока математика** зад дълбокото обучение. За това препоръчваме [Дълбоко обучение](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) от Ian Goodfellow, Yoshua Bengio и Aaron Courville, която също е достъпна онлайн на [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).

За плавно въвеждане в темите за _ИИ в облака_ може да помислите да вземете учебния път [Започнете с изкуствен интелект в Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum).

# Съдържание

|     |                                                                 Урок Линк                                                                  |                                           PyTorch/Keras/TensorFlow                                          | Лабораторно упражнение                                                            |
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |
| 0  |                                 [Настройка на курса](./lessons/0-course-setup/setup.md)                                 |                      [Настройте средата си за разработка](./lessons/0-course-setup/how-to-run.md)                       |   |
| I  |               [**Въведение в ИИ**](./lessons/1-Intro/README.md)      | | |
| 01  |       [Въведение и история на ИИ](./lessons/1-Intro/README.md)       |           -                            | -  |
| II |              **Символен ИИ**              |
| 02  |       [Представяне на знанието и експертни системи](./lessons/2-Symbolic/README.md)       |            [Експертни системи](./lessons/2-Symbolic/Animals.ipynb) /  [Онтология](./lessons/2-Symbolic/FamilyOntology.ipynb) /[Граф на концепциите](./lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |
| III |                        [**Въведение в невронните мрежи**](./lessons/3-NeuralNetworks/README.md) |||
| 03  |                [Персептрон](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Тетрадка](./lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [Лаборатория](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 04  |                   [Многослоен персептрон и създаване на собствена рамка](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Тетрадка](./lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [Лаборатория](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 05  |            [Въведение в рамките (PyTorch/TensorFlow) и прекомерно обучение](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](./lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](./lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Лаборатория](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV  |            [**Компютърно зрение**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [Разгледайте компютърното зрение в Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |
| 06  |            [Въведение в компютърното зрение. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Тетрадка](./lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [Лаборатория](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 07  |            [Конволюционни невронни мрежи](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [Архитектури на CNN](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](./lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](./lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [Лаборатория](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 08  |            [Предварително обучени мрежи и трансферно обучение](./lessons/4-ComputerVision/08-TransferLearning/README.md) и [Трикове при обучението](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](./lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Лаборатория](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [Автоенкодери и VAE](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](./lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [Генеративни състезателни мрежи и пренасяне на художествен стил](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](./lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [Обектно детектиране](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](./lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [Лаборатория](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [Семантично сегментиране. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)             |  |
| V  |            [**Обработка на естествен език**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [Разгледайте обработката на естествен език в Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [Представяне на текст. Bow/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [Семантични векторни представяния на думи. Word2Vec и GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [Езиково моделиране. Обучение на собствени вграденя](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [Лаборатория](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [Рекурентни невронни мрежи](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [Генеративни рекурентни мрежи](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)             | [Лаборатория](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Трансформъри. BERT.](./lessons/5-NLP/18-Transformers/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [Распознаване на именовани обекти](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [Лаборатория](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [Големи езикови модели, програмиране с подсказки и задачи с малко примери](./lessons/5-NLP/20-LangModels/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **Други AI техники** || |
| 21  |            [Генетични алгоритми](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Тетрадка](./lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [Дълбоко подсилващо обучение](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](./lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](./lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [Лаборатория](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [Многoагентски системи](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **Етика в AI** | | |
| 24  |            [Етика в AI и отговорен AI](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: Принципи за отговорен AI](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **Допълнително** | | |
| 25  |            [Мултимодални мрежи, CLIP и VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Тетрадка](./lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## Във всеки урок съдържа
* Материал за предварително четене
* Изпълними Jupyter тетрадки, които често са специфични за дадена рамка (**PyTorch** или **TensorFlow**). Изпълнимата тетрадка съдържа и много теоретичен материал, така че за да разберете темата, трябва да преминете през поне една версия на тетрадката (или PyTorch, или TensorFlow).
* **Лаборатории**, налични за някои теми, които ви дават възможност да опитате да приложите научения материал към конкретен проблем.
* Някои секции съдържат връзки към модули от [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum), които покриват свързани теми.

## Започване

### 🎯 Нов в AI? Започни тук!

Ако сте напълно нови в AI и искате бързи, практични примери, разгледайте нашите [**Примери за начинаещи**](./examples/README.md)! Те включват:

- 🌟 **Hello AI World** - Вашата първа AI програма (разпознаване на шаблони)
- 🧠 **Проста невронна мрежа** - Изграждане на невронна мрежа от нулата  
- 🖼️ **Класификатор на изображения** - Класифицирайте изображения с подробни коментари
- 💬 **Текстов сентимент** - Анализиране на положителен/отрицателен текст

Тези примери са създадени, за да ви помогнат да разберете концепциите на AI преди да се потопите напълно в учебната програма.

### 📚 Пълна настройка на учебната програма

- Създадохме [урок за настройка](./lessons/0-course-setup/setup.md), който да ви помогне с настройката на средата за разработка.
- За преподаватели също сме създали [урок за настройка на учебната програма](./lessons/0-course-setup/for-teachers.md)!
- Как да [стартирате кода във VSCode или Codespace](./lessons/0-course-setup/how-to-run.md)

Следвайте тези стъпки:

Форкнете хранилището: Кликнете на бутона "Fork" в горния десен ъгъл на тази страница.

Клонирайте хранилището: `git clone https://github.com/microsoft/AI-For-Beginners.git`

Не забравяйте да дадете звезда (🌟) на това хранилище, за да го намерите по-лесно по-късно.

## Срещнете други учащи

Присъединете се към нашия [официален Discord сървър за AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum), за да се срещнете и да създадете мрежа с други учащи, които следват курса, и да получите подкрепа.

Ако имате обратна връзка или въпроси по време на работа, посетете нашия [Azure AI Foundry Developer Forum](https://aka.ms/foundry/forum).

## Въпроси

> **Бележка относно въпросите**: Всички въпроси се съдържат в папката Quiz-app в etc\quiz-app, или [онлайн тук](https://ff-quizzes.netlify.app/). Те са свързани от уроците; приложението за въпроси може да се стартира локално или да се разположи в Azure; следвайте инструкциите в папката `quiz-app`. Постепенно се локализират.

## Търсим помощ

Имате ли предложения или сте открили грешки в правописа или кода? Създайте проблем (issue) или pull request.

## Специални благодарности

* **✍️ Основен автор:** [Дмитрий Сошников](http://soshnikov.com), доктор по науки
* **🔥 Редактор:** [Джен Лупър](https://twitter.com/jenlooper), доктор по науки
* **🎨 Илюстратор на скици:** [Томоми Имура](https://twitter.com/girlie_mac)
* **✅ Създател на въпроси:** [Латифа Бело](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)
* **🙏 Основни сътрудници:** [Евгений Пищик](https://github.com/Pe4enIks)

## Други учебни програми

Нашият екип създава и други учебни програми! Вижте:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j за начинаещи](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js за начинаещи](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)
[![LangChain за начинаещи](https://img.shields.io/badge/LangChain%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://github.com/microsoft/langchain-for-beginners?WT.mc_id=m365-94501-dwahlin)
---

### Azure / Edge / MCP / Агенти
[![AZD за начинаещи](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI за начинаещи](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP за начинаещи](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI агенти за начинаещи](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Серия за генеративен AI
[![Генеративен AI за начинаещи](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Генеративен AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Генеративен AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Генеративен AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Основно обучение
[![ML за начинаещи](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science за начинаещи](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI за начинаещи](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Киберсигурност за начинаещи](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Уеб разработка за начинаещи](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT за начинаещи](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Разработка за начинаещи](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Серия Copilot
[![Copilot за AI парно програмиране](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot за C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Приключения с Copilot](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Получаване на помощ

Ако се затрудните или имате въпроси относно създаването на AI приложения, присъединете се към други учащи и опитни разработчици в дискусии за MCP. Това е поддържаща общност, където въпросите са добре дошли и знанието се споделя свободно.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Ако имате обратна връзка или грешки по време на разработване, посетете:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Отказ от отговорност**:
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->