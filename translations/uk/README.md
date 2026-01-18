<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "85102ce4bfab31103e99dc8ca2e2f181",
  "translation_date": "2026-01-16T06:42:24+00:00",
  "source_file": "README.md",
  "language_code": "uk"
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

# Штучний інтелект для початківців - навчальна програма

|![Sketchnote by @girlie_mac https://twitter.com/girlie_mac](../../../../translated_images/uk/ai-overview.0857791951d19500.webp)|
|:---:|
| Штучний інтелект для початківців - _Sketchnote від [@girlie_mac](https://twitter.com/girlie_mac)_ |

Досліджуйте світ **штучного інтелекту** (ШІ) за допомогою нашої 12-тижневої програми з 24 уроків! Вона містить практичні уроки, тести та лабораторні роботи. Навчальна програма дружня до початківців і охоплює інструменти, такі як TensorFlow та PyTorch, а також етику в ШІ.

### 🌐 Підтримка багатьох мов

#### Підтримується через GitHub Action (автоматично та завжди оновлено)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh/README.md) | [Chinese (Traditional, Hong Kong)](../hk/README.md) | [Chinese (Traditional, Macau)](../mo/README.md) | [Chinese (Traditional, Taiwan)](../tw/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../br/README.md) | [Portuguese (Portugal)](../pt/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](../ro/README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](./README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Віддаєте перевагу клонувати локально?**

> Цей репозиторій містить понад 50 мовних перекладів, що значно збільшує розмір завантаження. Щоб клонувати без перекладів, використовуйте sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git
> cd AI-For-Beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Це дасть вам усе необхідне для проходження курсу з набагато швидшим завантаженням.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Якщо ви хочете, щоб були підтримані додаткові мови перекладу, вони перелічені [тут](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Приєднуйтесь до спільноти
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

## Чого ви навчитеся

**[Ментальна карта курсу](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

У цій навчальній програмі ви дізнаєтесь:

* Різні підходи до штучного інтелекту, включаючи «старий добрий» символічний підхід із **репрезентацією знань** та логічним виведенням ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
* **Нейронні мережі** та **глибинне навчання**, які лежать в основі сучасного ШІ. Ми продемонструємо концепції цих важливих тем на прикладах коду у двох найпопулярніших фреймворках - [TensorFlow](http://Tensorflow.org) та [PyTorch](http://pytorch.org).
* **Нейронні архітектури** для роботи з зображеннями та текстом. Ми розглянемо останні моделі, хоча можливо трохи поступимося сучасній передовій.
* Менш популярні підходи в ШІ, такі як **генетичні алгоритми** та **багатоагентні системи**.

Чого ми не охоплюватимемо у цій навчальній програмі:

> [Знайдіть усі додаткові ресурси для цього курсу у нашій колекції Microsoft Learn](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)

* Бізнес-кейси використання **ШІ у бізнесі**. Розгляньте можливість проходження навчальної траєкторії [Вступ до ШІ для бізнес-користувачів](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) на Microsoft Learn або [AI Business School](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum), розроблений у співпраці з [INSEAD](https://www.insead.edu/).
* **Класичне машинне навчання**, яке добре описано у нашій навчальній програмі [Машинне навчання для початківців](http://github.com/Microsoft/ML-for-Beginners).
* Практичні застосування ШІ, створені за допомогою **[Когнітивних сервісів](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)**. Для цього рекомендуємо почати з модулів Microsoft Learn для [зору](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum), [обробки природної мови](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum), **[генеративного ШІ за допомогою Azure OpenAI Service](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** та інших.
* Специфічні ML **хмарні фреймворки**, такі як [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum), [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum) або [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum). Розгляньте використання навчальних шляхів [Створення та експлуатація машинного навчання з Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) і [Створення та експлуатація машинного навчання з Azure Databricks](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum).
* **Розмовний ШІ** та **чат-боти**. Існує окремий навчальний шлях [Створення розмовних рішень ШІ](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum), а також ви можете звернутися до [цього блогу](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) для більшої деталізації.
* **Глибока математика** глибинного навчання. Для цього ми рекомендуємо книгу [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) авторів Іена Гудфеллоу, Йошуа Бенджіо та Аарона Курвіль, яка також доступна онлайн за [адресою](https://www.deeplearningbook.org/).

Для плавного вступу до тематики _ШІ у хмарі_ ви можете розглянути навчальний шлях [Початок роботи з штучним інтелектом на Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum).

# Зміст

|     |                                                                 Посилання на урок                                                                  |                                           PyTorch/Keras/TensorFlow                                          | Лабораторна робота                                                            |
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |
| 0  |                                 [Налаштування курсу](./lessons/0-course-setup/setup.md)                                 |                      [Налаштуйте своє середовище розробки](./lessons/0-course-setup/how-to-run.md)                       |   |
| I  |               [**Вступ до ШІ**](./lessons/1-Intro/README.md)      | | |
| 01  |       [Вступ та історія ШІ](./lessons/1-Intro/README.md)       |           -                            | -  |
| II |              **Символічний ШІ**              |
| 02  |       [Репрезентація знань та експертні системи](./lessons/2-Symbolic/README.md)       |            [Експертні системи](./lessons/2-Symbolic/Animals.ipynb) /  [Онтологія](./lessons/2-Symbolic/FamilyOntology.ipynb) /[Граф понять](./lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |
| III |                        [**Вступ до нейронних мереж**](./lessons/3-NeuralNetworks/README.md) |||
| 03  |                [Перцептрон](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Зошит](./lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [Лабораторна](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 04  |                   [Багатошаровий перцептрон та створення власного фреймворку](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Зошит](./lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [Лабораторна](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 05  |            [Вступ до фреймворків (PyTorch/TensorFlow) та перенавчання](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](./lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](./lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Лабораторна](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV  |            [**Комп’ютерний зір**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [Дослідіть Комп’ютерний зір на Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |
| 06  |            [Вступ до комп’ютерного зору. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Зошит](./lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [Лабораторна](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 07  |            [Згорткові нейронні мережі](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [Архітектури CNN](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](./lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](./lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [Лабораторна](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 08  |            [Попередньо навчені мережі та перенавчання](./lessons/4-ComputerVision/08-TransferLearning/README.md) та [Трюки тренування](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](./lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Лабораторна](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [Автокодировщики та VAE](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](./lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [Генеративно-змагальні мережі та стильове перенесення мистецтва](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](./lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [Виявлення об’єктів](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](./lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [Лабораторна](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [Семантична сегментація. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)             |  |
| V  |            [**Обробка природної мови**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [Дослідіть обробку природної мови на Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [Представлення тексту. Bow/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [Семантичні векторні уявлення слів. Word2Vec і GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [Моделювання мови. Навчання власних векторних уявлень](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [Лабораторна](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [Рекурентні нейронні мережі](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [Генеративні рекурентні мережі](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)             | [Лабораторна](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Трансформери. BERT.](./lessons/5-NLP/18-Transformers/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [Розпізнавання іменованих сутностей](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [Лабораторна](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [Великі мовні моделі, програмування підказок і завдання з малою кількістю прикладів](./lessons/5-NLP/20-LangModels/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **Інші методи ШІ** || |
| 21  |            [Генетичні алгоритми](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Зошит](./lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [Глибинне підкріплювальне навчання](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](./lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](./lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [Лабораторна](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [Системи з багатьма агентами](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **Етика ШІ** | | |
| 24  |            [Етика ШІ та відповідальний ШІ](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: Принципи відповідального ШІ](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **Додатково** | | |
| 25  |            [Мультимодальні мережі, CLIP та VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Зошит](./lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## Кожен урок містить

* Попередній матеріал для читання
* Виконувані зошити Jupyter, які часто специфічні для фреймворку (**PyTorch** або **TensorFlow**). Виконуваний зошит також містить багато теоретичного матеріалу, тому для розуміння теми потрібно пройти хоча б один варіант зошита (або PyTorch, або TensorFlow).
* **Лабораторні роботи** для деяких тем, які дають можливість спробувати застосувати вивчений матеріал до конкретної задачі.
* Деякі розділи містять посилання на модулі [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum), що охоплюють суміжні теми.

## Початок роботи

### 🎯 Новачок у ШІ? Почніть тут!

Якщо ви зовсім новачок у ШІ і хочете швидкі практичні приклади, перегляньте наші [**Приклади для початківців**](./examples/README.md)! Вони включають:

- 🌟 **Hello AI World** - Ваша перша програма ШІ (розпізнавання шаблонів)
- 🧠 **Проста нейронна мережа** - Побудова нейронної мережі з нуля  
- 🖼️ **Класифікатор зображень** - Класифікація зображень з докладними коментарями
- 💬 **Аналіз настрою тексту** — аналіз позитивного/негативного тексту

Ці приклади розроблені, щоб допомогти вам зрозуміти концепції ШІ перед тим, як зануритися у повний навчальний курс.

### 📚 Налаштування повного навчального курсу

- Ми створили [урок з налаштування](./lessons/0-course-setup/setup.md), щоб допомогти вам із налаштуванням вашого середовища розробки. - Для викладачів ми також створили [урок з налаштування навчальних програм](./lessons/0-course-setup/for-teachers.md)!
- Як [запустити код у VSCode або Codespace](./lessons/0-course-setup/how-to-run.md)

Дотримуйтесь цих кроків:

Форкніть репозиторій: натисніть кнопку "Fork" у верхньому правому куті цієї сторінки.

Клонуйте репозиторій: `git clone https://github.com/microsoft/AI-For-Beginners.git`

Не забудьте поставити зірочку (🌟) цьому репозиторію, щоб легше було його знайти пізніше.

## Познайомтесь з іншими учнями

Приєднуйтесь до нашого [офіційного AI Discord сервера](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum), щоб зустріти й поспілкуватися з іншими учнями цього курсу та отримати підтримку.

Якщо у вас є відгуки про продукт або питання під час створення, відвідайте наш [Azure AI Foundry Developer Forum](https://aka.ms/foundry/forum)

## Вікторини

> **Примітка про вікторини**: Всі вікторини знаходяться у папці Quiz-app в etc\quiz-app, або [онлайн тут](https://ff-quizzes.netlify.app/). Вони пов’язані з уроками, застосунок вікторин можна запускати локально або розгортати на Azure; дотримуйтеся інструкцій у папці `quiz-app`. Вікторини поступово локалізуються.

## Потрібна допомога

Чи маєте пропозиції або знайшли орфографічні чи кодові помилки? Створіть issue або pull request.

## Особлива подяка

* **✍️ Головний автор:** [Dmitry Soshnikov](http://soshnikov.com), PhD
* **🔥 Редактор:** [Jen Looper](https://twitter.com/jenlooper), PhD
* **🎨 Ілюстратор скетчнотів:** [Tomomi Imura](https://twitter.com/girlie_mac)
* **✅ Творець вікторин:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)
* **🙏 Основні учасники:** [Evgenii Pishchik](https://github.com/Pe4enIks)

## Інші навчальні програми

Наша команда створює інші навчальні програми! Ознайомтесь із ними:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Агенти
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Серія Generative AI
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---
 
### Основне навчання
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---
 
### Серія Copilot
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Отримання допомоги

Якщо ви застрягли або маєте питання щодо створення AI-застосунків, приєднуйтесь до інших учнів і досвідчених розробників у обговореннях про MCP. Це підтримуюча спільнота, де вітаються питання і відбувається вільний обмін знаннями.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Якщо у вас є відгуки про продукт або помилки під час створення – відвідайте:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою автоматичного перекладача [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичний переклад може містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння чи неправильні тлумачення, що виникли внаслідок використання цього перекладу.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->