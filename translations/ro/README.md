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

# Inteligență Artificială pentru Începători - Un Curriculum

|![Sketchnote by @girlie_mac https://twitter.com/girlie_mac](../../translated_images/ro/ai-overview.0857791951d19500.webp)|
|:---:|
| AI Pentru Începători - _Sketchnote de la [@girlie_mac](https://twitter.com/girlie_mac)_ |

Explorează lumea **Inteligenței Artificiale** (IA) cu curriculumul nostru de 12 săptămâni, 24 de lecții! Include lecții practice, chestionare și laboratoare. Curriculumul este prietenos pentru începători și acoperă unelte precum TensorFlow și PyTorch, precum și etica în IA


### 🌐 Suport Multilingv

#### Acceptat prin GitHub Action (Automat și Întotdeauna Actualizat)

<!-- CO-OP TRANSLATOR LANGUAGES TABLE START -->
[Arabic](../ar/README.md) | [Bengali](../bn/README.md) | [Bulgarian](../bg/README.md) | [Burmese (Myanmar)](../my/README.md) | [Chinese (Simplified)](../zh-CN/README.md) | [Chinese (Traditional, Hong Kong)](../zh-HK/README.md) | [Chinese (Traditional, Macau)](../zh-MO/README.md) | [Chinese (Traditional, Taiwan)](../zh-TW/README.md) | [Croatian](../hr/README.md) | [Czech](../cs/README.md) | [Danish](../da/README.md) | [Dutch](../nl/README.md) | [Estonian](../et/README.md) | [Finnish](../fi/README.md) | [French](../fr/README.md) | [German](../de/README.md) | [Greek](../el/README.md) | [Hebrew](../he/README.md) | [Hindi](../hi/README.md) | [Hungarian](../hu/README.md) | [Indonesian](../id/README.md) | [Italian](../it/README.md) | [Japanese](../ja/README.md) | [Kannada](../kn/README.md) | [Korean](../ko/README.md) | [Lithuanian](../lt/README.md) | [Malay](../ms/README.md) | [Malayalam](../ml/README.md) | [Marathi](../mr/README.md) | [Nepali](../ne/README.md) | [Nigerian Pidgin](../pcm/README.md) | [Norwegian](../no/README.md) | [Persian (Farsi)](../fa/README.md) | [Polish](../pl/README.md) | [Portuguese (Brazil)](../pt-BR/README.md) | [Portuguese (Portugal)](../pt-PT/README.md) | [Punjabi (Gurmukhi)](../pa/README.md) | [Romanian](./README.md) | [Russian](../ru/README.md) | [Serbian (Cyrillic)](../sr/README.md) | [Slovak](../sk/README.md) | [Slovenian](../sl/README.md) | [Spanish](../es/README.md) | [Swahili](../sw/README.md) | [Swedish](../sv/README.md) | [Tagalog (Filipino)](../tl/README.md) | [Tamil](../ta/README.md) | [Telugu](../te/README.md) | [Thai](../th/README.md) | [Turkish](../tr/README.md) | [Ukrainian](../uk/README.md) | [Urdu](../ur/README.md) | [Vietnamese](../vi/README.md)

> **Preferi să clonezi local?**

> Acest depozit include peste 50 de traduceri care cresc semnificativ dimensiunea descărcării. Pentru a clona fără traduceri, folosește sparse checkout:
> ```bash
> git clone --filter=blob:none --sparse https://github.com/microsoft/AI-For-Beginners.git
> cd AI-For-Beginners
> git sparse-checkout set --no-cone '/*' '!translations' '!translated_images'
> ```
> Aceasta îți oferă tot ce ai nevoie pentru a finaliza cursul cu o descărcare mult mai rapidă.
<!-- CO-OP TRANSLATOR LANGUAGES TABLE END -->

**Dacă dorești să fie adăugate alte limbi pentru traduceri, acestea sunt listate [aici](https://github.com/Azure/co-op-translator/blob/main/getting_started/supported-languages.md)**

## Alătură-te Comunității
[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

## Ce vei învăța

**[Harta mentală a cursului](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

În acest curriculum vei învăța:

* Diferite abordări ale Inteligenței Artificiale, inclusiv abordarea simbolică „veche”, cu **Reprezentare a Cunoștințelor** și raționament ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
* **Rețele Neuronale** și **Învățare Profundă**, care sunt în centrul IA moderne. Vom ilustra conceptele din spatele acestor subiecte importante folosind cod în două dintre cele mai populare cadre - [TensorFlow](http://Tensorflow.org) și [PyTorch](http://pytorch.org).
* **Arhitecturi Neuronale** pentru lucrul cu imagini și text. Vom aborda modele recente, dar poate fi oarecum lipsit de cele mai noi tehnologii.
* Abordări mai puțin populare ale IA, cum ar fi **Algoritmi Genetici** și **Sisteme Multi-Agent**.

Ce nu vom acoperi în acest curriculum:

> [Găsește toate resursele suplimentare pentru acest curs în colecția noastră Microsoft Learn](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)

* Studii de caz de utilizare a **IA în Afaceri**. Ia în considerare urmarea traseului de învățare [Introducere în IA pentru utilizatorii de afaceri](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-bethanycheum) pe Microsoft Learn, sau [Școala de Afaceri AI](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-bethanycheum), dezvoltată în colaborare cu [INSEAD](https://www.insead.edu/).
* **Învățare Automată Clasică**, care este bine descrisă în curriculumul nostru [Machine Learning pentru Începători](http://github.com/Microsoft/ML-for-Beginners).
* Aplicații practice AI construite folosind **[Servicii Cognitive](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-bethanycheum)**. Pentru acestea, recomandăm să începi cu modulele Microsoft Learn pentru [viziune](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-bethanycheum), [procesarea limbajului natural](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-bethanycheum), **[Generative AI cu Azure OpenAI Service](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** și altele.
* Anumite **Cadre Cloud pentru ML**, precum [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-bethanycheum), [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum), sau [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-bethanycheum). Ia în considerare folosirea traseelor de învățare [Construiește și operează soluții de învățare automată cu Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-bethanycheum) și [Construiește și operează soluții de învățare automată cu Azure Databricks](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-bethanycheum).
* **Inteligență Artificială Conversațională** și **Chat Bots**. Există un traseu separat de învățare [Crearea soluțiilor AI conversaționale](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-bethanycheum), și poți consulta [acest articol de blog](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) pentru mai multe detalii.
* **Matematică Avansată** din spatele învățării profunde. În acest scop recomandăm [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) de Ian Goodfellow, Yoshua Bengio și Aaron Courville, disponibil și online la [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).

Pentru o introducere ușoară în subiectele _IA în Cloud_, poți considera urmarea traseului de învățare [Începe cu Inteligența Artificială pe Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-bethanycheum).

# Conținut

|     |                                                                 Legătura Lecției                                                                  |                                           PyTorch/Keras/TensorFlow                                          | Laborator                                                            |
| :-: | :------------------------------------------------------------------------------------------------------------------------------------------: | :---------------------------------------------------------------------------------------------: | ------------------------------------------------------------------------------ |
| 0  |                                 [Configurare Curs](./lessons/0-course-setup/setup.md)                                 |                      [Setează Mediul de Dezvoltare](./lessons/0-course-setup/how-to-run.md)                       |   |
| I  |               [**Introducere în IA**](./lessons/1-Intro/README.md)      | | |
| 01  |       [Introducere și Istoria IA](./lessons/1-Intro/README.md)       |           -                            | -  |
| II |              **IA Simbolică**              |
| 02  |       [Reprezentarea Cunoașterii și Sisteme Expert](./lessons/2-Symbolic/README.md)       |            [Sisteme Expert](./lessons/2-Symbolic/Animals.ipynb) /  [Ontologie](./lessons/2-Symbolic/FamilyOntology.ipynb) /[Grafic de Concepte](./lessons/2-Symbolic/MSConceptGraph.ipynb)                             |  |
| III |                        [**Introducere în Rețelele Neuronale**](./lessons/3-NeuralNetworks/README.md) |||
| 03  |                [Perceptron](./lessons/3-NeuralNetworks/03-Perceptron/README.md)                 |                       [Notebook](./lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb)                      | [Laborator](./lessons/3-NeuralNetworks/03-Perceptron/lab/README.md) |
| 04  |                   [Perceptron cu mai multe straturi și Crearea propriului nostru Cadru](./lessons/3-NeuralNetworks/04-OwnFramework/README.md)                   |        [Notebook](./lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb)        | [Laborator](./lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md) |
| 05  |            [Introducere în Cadre (PyTorch/TensorFlow) și Supraînvățare](./lessons/3-NeuralNetworks/05-Frameworks/README.md)             |           [PyTorch](./lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb) / [Keras](./lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Laborator](./lessons/3-NeuralNetworks/05-Frameworks/lab/README.md) |
| IV  |            [**Viziune pe Calculator**](./lessons/4-ComputerVision/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste) / [TensorFlow](https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste)| [Explorează Viziunea pe Calculator pe Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) |
| 06  |            [Introducere în Viziunea pe Calculator. OpenCV](./lessons/4-ComputerVision/06-IntroCV/README.md)             |           [Notebook](./lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)         | [Laborator](./lessons/4-ComputerVision/06-IntroCV/lab/README.md) |
| 07  |            [Rețele Neuronale Convoluționale](./lessons/4-ComputerVision/07-ConvNets/README.md) &  [Arhitecturi CNN](./lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md)             |           [PyTorch](./lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb) /[TensorFlow](./lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)             | [Laborator](./lessons/4-ComputerVision/07-ConvNets/lab/README.md) |
| 08  |            [Rețele Pre-antrenate și Învățare Transferată](./lessons/4-ComputerVision/08-TransferLearning/README.md) și [Trucuri de Antrenament](./lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md)             |           [PyTorch](./lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb) / [TensorFlow](./lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb)             | [Laborator](./lessons/4-ComputerVision/08-TransferLearning/lab/README.md) |
| 09  |            [Autoencodere și VAE-uri](./lessons/4-ComputerVision/09-Autoencoders/README.md)             |           [PyTorch](./lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)             |  |
| 10  |            [Rețele Generative Adversariale & Transfer Stil Artistic](./lessons/4-ComputerVision/10-GANs/README.md)             |           [PyTorch](./lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/10-GANs/GANTF.ipynb)             |  |
| 11  |            [Detecție de Obiecte](./lessons/4-ComputerVision/11-ObjectDetection/README.md)             |         [TensorFlow](./lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb)             | [Laborator](./lessons/4-ComputerVision/11-ObjectDetection/lab/README.md) |
| 12  |            [Segmentare Semantică. U-Net](./lessons/4-ComputerVision/12-Segmentation/README.md)             |           [PyTorch](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb) / [TensorFlow](./lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)             |  |
| V  |            [**Procesarea Limbajului Natural**](./lessons/5-NLP/README.md)             | [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste) /[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste) | [Explorează Procesarea Limbajului Natural pe Microsoft Azure](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum)|
| 13  |            [Reprezentarea Textului. Bow/TF-IDF](./lessons/5-NLP/13-TextRep/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)             | |
| 14  |            [Încapsulări semantice ale cuvintelor. Word2Vec și GloVe](./lessons/5-NLP/14-Embeddings/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)             |  |
| 15  |            [Modelare a Limbajului. Antrenarea propriilor încapsulări](./lessons/5-NLP/15-LanguageModeling/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)             | [Laborator](./lessons/5-NLP/15-LanguageModeling/lab/README.md) |
| 16  |            [Rețele Neuronale Recurente](./lessons/5-NLP/16-RNN/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb)             |  |
| 17  |            [Rețele Recurente Generative](./lessons/5-NLP/17-GenerativeNetworks/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb) / [TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)             | [Laborator](./lessons/5-NLP/17-GenerativeNetworks/lab/README.md) |
| 18  |            [Transformere. BERT.](./lessons/5-NLP/18-Transformers/README.md)             |           [PyTorch](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb) /[TensorFlow](https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb)             |  |
| 19  |            [Recunoașterea Entităților Nume](./lessons/5-NLP/19-NER/README.md)             |           [TensorFlow](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/19-NER/NER-TF.ipynb)             | [Laborator](./lessons/5-NLP/19-NER/lab/README.md) |
| 20  |            [Modele Mari de Limbaj, Programare Prompt și Sarcini Few-Shot](./lessons/5-NLP/20-LangModels/README.md)             |           [PyTorch](https://microsoft.github.io/AI-For-Beginners/lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb) | |
| VI |            **Alte Tehnici AI** || |
| 21  |            [Algoritmi Genetici](./lessons/6-Other/21-GeneticAlgorithms/README.md)             |           [Notebook](./lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb) | |
| 22  |            [Învățare Profundă prin Consolidare](./lessons/6-Other/22-DeepRL/README.md)             |           [PyTorch](./lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb) /[TensorFlow](./lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb)             | [Laborator](./lessons/6-Other/22-DeepRL/lab/README.md) |
| 23  |            [Sisteme Multi-Agent](./lessons/6-Other/23-MultiagentSystems/README.md)             |  | |
| VII |            **Etica AI** | | |
| 24  |            [Etica AI și AI Responsabil](./lessons/7-Ethics/README.md)             |           [Microsoft Learn: Principiile AI Responsabil](https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste) | |
| IX  |            **Suplimente** | | |
| 25  |            [Rețele Multi-Modal, CLIP și VQGAN](./lessons/X-Extras/X1-MultiModal/README.md)             |           [Notebook](./lessons/X-Extras/X1-MultiModal/Clip.ipynb)    | |

## Fiecare lecție conține

* Material de pre-lectură
* Jupyter Notebooks executabile, adesea specifice cadrului (**PyTorch** sau **TensorFlow**). Notebook-ul executabil conține și mult material teoretic, astfel încât pentru a înțelege subiectul trebuie să parcurgi măcar o versiune a notebook-ului (PyTorch sau TensorFlow).
* **Laboratoare** disponibile pentru unele subiecte, care îți oferă oportunitatea să aplici materialul învățat pe o problemă specifică.
* Unele secțiuni conțin linkuri către module [**MS Learn**](https://learn.microsoft.com/en-us/collections/7w28iy2xrqzdj0?WT.mc_id=academic-77998-bethanycheum) care acoperă subiecte conexe.

## Începutul

### 🎯 Ești nou în AI? Începe aici!

Dacă ești complet nou în AI și vrei exemple rapide, practice, aruncă o privire la [**Exemple pentru Începători**](./examples/README.md)! Acestea includ:

- 🌟 **Hello AI World** - Primul tău program AI (recunoașterea tiparelor)
- 🧠 **Rețea Neuronală Simplă** - Construiește o rețea neuronală de la zero  
- 🖼️ **Clasificator de Imagini** - Clasifică imagini cu comentarii detaliate  
- 💬 **Sentiment Text** - Analizează text pozitiv/negativ

Aceste exemple sunt concepute pentru a vă ajuta să înțelegeți conceptele AI înainte de a începe curricula completă.

### 📚 Configurarea Curriculumului Complet

- Am creat o [lecție de configurare](./lessons/0-course-setup/setup.md) pentru a vă ajuta să vă configurați mediul de dezvoltare. - Pentru educatorii, am creat și o [lecție de configurare a curriculumului](./lessons/0-course-setup/for-teachers.md)!
- Cum să [rulați codul în VSCode sau Codespace](./lessons/0-course-setup/how-to-run.md)

Urmați acești pași:

Furcați Repository-ul: Faceți clic pe butonul "Fork" din colțul din dreapta sus al acestei pagini.

Clonați Repository-ul: `git clone https://github.com/microsoft/AI-For-Beginners.git`

Nu uitați să acordați stea (🌟) acestui repo pentru a-l găsi mai ușor mai târziu.

## Întâlniți alți cursanți

Alăturați-vă [serverului oficial Discord AI](https://aka.ms/genai-discord?WT.mc_id=academic-105485-bethanycheum) pentru a cunoaște și a face networking cu alți cursanți care urmează acest curs și pentru a primi suport.

Dacă aveți feedback despre produs sau întrebări în timpul dezvoltării, vizitați [Forum-ul Dezvoltatorilor Azure AI Foundry](https://aka.ms/foundry/forum)

## Chestionare  

> **O notă despre chestionare**: Toate chestionarele se află în folderul Quiz-app din etc\quiz-app, sau [Online aici](https://ff-quizzes.netlify.app/) Sunt legate din lecții, aplicația de quiz poate fi rulată local sau implementată pe Azure; urmați instrucțiunile din folderul `quiz-app`. Se lucrează treptat la localizarea acestora.

## Ajutor Cerut

Aveți sugestii sau ați găsit greșeli de ortografie sau de cod? Deschideți un issue sau creați o pull request.

## Mulțumiri Speciale

* **✍️ Autor Principal:** [Dmitry Soshnikov](http://soshnikov.com), PhD  
* **🔥 Editor:** [Jen Looper](https://twitter.com/jenlooper), PhD  
* **🎨 Ilustrator Sketchnote:** [Tomomi Imura](https://twitter.com/girlie_mac)  
* **✅ Creator Quiz:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)  
* **🙏 Contribuabili Importanți:** [Evgenii Pishchik](https://github.com/Pe4enIks)

## Alte Curriculumuri

Echipa noastră produce și alte curriculumuri! Consultați:

<!-- CO-OP TRANSLATOR OTHER COURSES START -->
### LangChain  
[![LangChain4j for Beginners](https://img.shields.io/badge/LangChain4j%20for%20Beginners-22C55E?style=for-the-badge&&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchain4j-for-beginners)  
[![LangChain.js for Beginners](https://img.shields.io/badge/LangChain.js%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=0553D6)](https://aka.ms/langchainjs-for-beginners?WT.mc_id=m365-94501-dwahlin)

---

### Azure / Edge / MCP / Agenți  
[![AZD for Beginners](https://img.shields.io/badge/AZD%20for%20Beginners-0078D4?style=for-the-badge&labelColor=E5E7EB&color=0078D4)](https://github.com/microsoft/AZD-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Edge AI for Beginners](https://img.shields.io/badge/Edge%20AI%20for%20Beginners-00B8E4?style=for-the-badge&labelColor=E5E7EB&color=00B8E4)](https://github.com/microsoft/edgeai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![MCP for Beginners](https://img.shields.io/badge/MCP%20for%20Beginners-009688?style=for-the-badge&labelColor=E5E7EB&color=009688)](https://github.com/microsoft/mcp-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI Agents for Beginners](https://img.shields.io/badge/AI%20Agents%20for%20Beginners-00C49A?style=for-the-badge&labelColor=E5E7EB&color=00C49A)](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Seria AI Generativă  
[![Generative AI for Beginners](https://img.shields.io/badge/Generative%20AI%20for%20Beginners-8B5CF6?style=for-the-badge&labelColor=E5E7EB&color=8B5CF6)](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (.NET)](https://img.shields.io/badge/Generative%20AI%20(.NET)-9333EA?style=for-the-badge&labelColor=E5E7EB&color=9333EA)](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (Java)](https://img.shields.io/badge/Generative%20AI%20(Java)-C084FC?style=for-the-badge&labelColor=E5E7EB&color=C084FC)](https://github.com/microsoft/generative-ai-for-beginners-java?WT.mc_id=academic-105485-koreyst)  
[![Generative AI (JavaScript)](https://img.shields.io/badge/Generative%20AI%20(JavaScript)-E879F9?style=for-the-badge&labelColor=E5E7EB&color=E879F9)](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)

---

### Învățare de Bază  
[![ML for Beginners](https://img.shields.io/badge/ML%20for%20Beginners-22C55E?style=for-the-badge&labelColor=E5E7EB&color=22C55E)](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)  
[![Data Science for Beginners](https://img.shields.io/badge/Data%20Science%20for%20Beginners-84CC16?style=for-the-badge&labelColor=E5E7EB&color=84CC16)](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)  
[![AI for Beginners](https://img.shields.io/badge/AI%20for%20Beginners-A3E635?style=for-the-badge&labelColor=E5E7EB&color=A3E635)](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)  
[![Cybersecurity for Beginners](https://img.shields.io/badge/Cybersecurity%20for%20Beginners-F97316?style=for-the-badge&labelColor=E5E7EB&color=F97316)](https://github.com/microsoft/Security-101?WT.mc_id=academic-96948-sayoung)  
[![Web Dev for Beginners](https://img.shields.io/badge/Web%20Dev%20for%20Beginners-EC4899?style=for-the-badge&labelColor=E5E7EB&color=EC4899)](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)  
[![IoT for Beginners](https://img.shields.io/badge/IoT%20for%20Beginners-14B8A6?style=for-the-badge&labelColor=E5E7EB&color=14B8A6)](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)  
[![XR Development for Beginners](https://img.shields.io/badge/XR%20Development%20for%20Beginners-38BDF8?style=for-the-badge&labelColor=E5E7EB&color=38BDF8)](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)

---

### Seria Copilot  
[![Copilot for AI Paired Programming](https://img.shields.io/badge/Copilot%20for%20AI%20Paired%20Programming-FACC15?style=for-the-badge&labelColor=E5E7EB&color=FACC15)](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)  
[![Copilot for C#/.NET](https://img.shields.io/badge/Copilot%20for%20C%23/.NET-FBBF24?style=for-the-badge&labelColor=E5E7EB&color=FBBF24)](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)  
[![Copilot Adventure](https://img.shields.io/badge/Copilot%20Adventure-FDE68A?style=for-the-badge&labelColor=E5E7EB&color=FDE68A)](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)  
<!-- CO-OP TRANSLATOR OTHER COURSES END -->

## Obținerea Ajutorului

Dacă rămâneți blocat sau aveți întrebări despre construirea aplicațiilor AI. Alăturați-vă altor cursanți și dezvoltatori experimentați în discuții despre MCP. Este o comunitate suportivă unde întrebările sunt binevenite și cunoștințele se împărtășesc liber.

[![Microsoft Foundry Discord](https://dcbadge.limes.pink/api/server/nTYy5BXMWG)](https://discord.gg/nTYy5BXMWG)

Dacă aveți feedback despre produs sau erori în timp ce dezvoltați, vizitați:

[![Microsoft Foundry Developer Forum](https://img.shields.io/badge/GitHub-Microsoft_Foundry_Developer_Forum-blue?style=for-the-badge&logo=github&color=000000&logoColor=fff)](https://aka.ms/foundry/forum)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să țineți cont că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un translator uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->