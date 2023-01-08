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

# Inteligência Artificial para Iniciantes - Um Currículo

|![ Sketchnote by [(@girlie_mac)](https://twitter.com/girlie_mac) ](../lessons/sketchnotes/ai-overview.png)|
|:---:|
| IA para iniciantes - _Sketchnote por [@girlie_mac](https://twitter.com/girlie_mac)_ |

Os Defensores da Cloud do Azure da Microsoft têm o prazer de oferecer um currículo de 12 semanas e 24 aulas sobre **Inteligência Artificial**.

Neste currículo, você aprenderá:

* Diferentes abordagens da Inteligência Artificial, incluindo a "boa e velha" abordagem simbólica com **Representação de Conhecimento** e raciocínio ([GOFAI](https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence)).
* **Redes Neurais** e **Aprendizado Profundo**, que estão no centro da IA moderna. Ilustraremos os conceitos por trás desses tópicos importantes usando código em duas das estruturas mais populares - [TensorFlow](http://Tensorflow.org) e [PyTorch](http://pytorch.org).
* **Arquiteturas Neurais** para trabalhar com imagens e texto. Abordaremos modelos recentes, mas pode faltar um pouco no estado da arte.
* Abordagens de IA menos populares, como **Algoritmos Genéticos** e **Sistemas Multiagentes**.

O que não abordaremos neste currículo:

* Casos de negócios de uso de **IA nos Negócios**. Considere fazer [Introdução à IA para usuários corporativos](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-cacaste) caminho de aprendizado no Microsoft Learn ou [IA Escola de Negócios](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-cacaste), desenvolvido em cooperação com [INSEAD](https://www.insead.edu/).
* **Aprendizado de Máquina Clássico**, que está bem descrito em nosso [Currículo de Aprendizado de Máquina para Iniciantes](http://github.com/Microsoft/ML-for-Beginners)
* Aplicações práticas de IA construídas usando **[Serviços Cognitivos](https://azure.microsoft.com/services/cognitive-services/?WT.mc_id=academic-77998-cacaste)**. Para isso, recomendamos que você comece com os módulos Microsoft Learn para [vision](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-cacaste), [processamento de linguagem natural](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-cacaste) e outros.
* ML **Cloud Frameworks** específico, como [Azure Machine Learning](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste) ou [Azure Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-cacaste). Considere usar [Crie e opere soluções de aprendizado de máquina com o Azure Machine Learning](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-cacaste) e [Crie e opere soluções de aprendizado de máquina com Azure Databricks](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-cacaste) caminhos de aprendizagem.
* **IA de conversação** e **Chat Bots**. Existe um próprio [Crie soluções de IA conversacional](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-cacaste) caminho de aprendizagem, e você também pode consultar [esta postagem do blog](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/) para mais detalhes.
* **Deep Mathematics** por trás da aprendizagem profunda. Para isso, recomendamos [Deep Learning](https://www.amazon.com/Deep-Learning-Adaptive-Computation-Machine/dp/0262035618) por Ian Goodfellow, Yoshua Bengio e Aaron Courville, que também está disponível online em [https://www.deeplearningbook.org/](https://www.deeplearningbook.org/).

Para uma introdução suave aos tópicos de *AI in the Cloud*, considere fazer o [Introdução à inteligência artificial no Azure](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-cacaste) Caminho de Aprendizagem.

---
# Conteúdo

<table>
<tr><th>No</th><th>Lesson</th><th>Intro</th><th>PyTorch</th><th>Keras/TensorFlow</th><th>Lab</th></tr>

<tr><td>I</td><td colspan="4"><b>Introdução à IA</b></td><td></td></tr>
<tr><td>1</td><td>Introdução e história da IA</td><td><a href="lessons/1-Intro/README.md">Texto</a></td><td></td><td></td><td></td></tr>

<tr><td>II</td><td colspan="4"><b>IA Simbólica</b></td><td></td></tr>
<tr><td>2 </td><td>Representação do Conhecimento e Sistemas Especialistas</td><td><a href="lessons/2-Symbolic/README.md">Texto</a></td><td colspan="2"><a href="lessons/2-Symbolic/Animals.ipynb">Sistema Inteligente</a>, <a href="lessons/2-Symbolic/FamilyOntology.ipynb">Ontologia</a>, <a href="lessons/2-Symbolic/MSConceptGraph.ipynb">Gráfico Conceitual</a></td><td></td></tr>
<tr><td>III</td><td colspan="4"><b><a href="lessons/3-NeuralNetworks/README.md">Introdução às Redes Neurais</a></b></td><td></td></tr>
<tr><td>3</td><td>Perceptron</td>
   <td><a href="lessons/3-NeuralNetworks/03-Perceptron/README.md">Text</a>
   <td colspan="2"><a href="lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb">Notebook</a></td><td><a href="lessons/3-NeuralNetworks/03-Perceptron/lab/README.md">Lab</a></td></tr>
<tr><td>4 </td><td>Perceptron multicamadas e criando nosso próprio Framework</td><td><a href="lessons/3-NeuralNetworks/04-OwnFramework/README.md">Texto</a></td><td colspan="2"><a href="lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb">Notebook</a><td><a href="lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md">Lab</a></td></tr> 
<tr><td>5</td>
   <td>Introdução aos Frameworks (PyTorch/TensorFlow)<br/>Sobreajuste</td>
   <td><a href="lessons/3-NeuralNetworks/05-Frameworks/README.md">Texo</a><br/><a href="lessons/3-NeuralNetworks/05-Frameworks/Overfitting.md">Texto</a></td>
   <td><a href="lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb">PyTorch</a></td>
   <td><a href="lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb">Keras</a>/<a href="lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb">TensorFlow</a></td>
   <td><a href="lessons/3-NeuralNetworks/05-Frameworks/lab/README.md">Lab</a></td></tr>
<tr><td>IV</td><td><b><a href="lessons/4-ComputerVision/README.md">Visão Computacional</a></b></td>
  <td colspan="3"><a href="https://docs.microsoft.com/learn/paths/explore-computer-vision-microsoft-azure/?WT.mc_id=academic-77998-cacaste"><i>Fundamentos da IA: explore a Visão Computacional</i></a></td>
  <td></td></tr>
<tr><td></td><td colspan="2"><i>Módulo Microsoft Learn sobre Visão Computacional</i></td>
  <td><a href="https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste"><i>PyTorch</i></a></td>
  <td><a href="https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste"><i>TensorFlow</i></a></td>
  <td></td></tr>
<tr><td>6</td><td>Introdução à Visão Computacional. OpenCV</td><td><a href="lessons/4-ComputerVision/06-IntroCV/README.md">Texto</a><td colspan="2"><a href="lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb">Notebook</a></td><td><a href="lessons/4-ComputerVision/06-IntroCV/lab/README.md">Lab</a></td></tr>
<tr><td>7</td><td>Redes Neurais Convolucionais<br/>Arquiteturas CNN</td><td><a href="lessons/4-ComputerVision/07-ConvNets/README.md">Texto</a><br/><a href="lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md">Texto</a></td><td><a href="lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb">TensorFlow</a></td><td><a href="lessons/4-ComputerVision/07-ConvNets/lab/README.md">Lab</a></td></tr>
<tr><td>8</td><td>Redes pré-treinadas e Aprendizado de Transferência<br/>Truques de Treinamento</td><td><a href="lessons/4-ComputerVision/08-TransferLearning/README.md">Texto</a><br/><a href="lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md">Texto</a></td><td><a href="lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb">TensorFlow</a><br/><a href="lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb">Amostra de abandono</a><br/><a href="lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb">Gato Adversário</a></td><td><a href="lessons/4-ComputerVision/08-TransferLearning/lab/README.md">Lab</a></td></tr>
<tr><td>9</td><td>Autoencoders e VAEs</td><td><a href="lessons/4-ComputerVision/09-Autoencoders/README.md">Texto</a></td><td><a href="lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb">TensorFlow</a></td><td></td></tr>
<tr><td>10</td><td>Redes Adversárias Gerativas<br/>Transferência de Estilo Artístico</td><td><a href="lessons/4-ComputerVision/10-GANs/README.md">Texto</a></td><td><a href="lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb">PyTorch</td><td><a href="lessons/4-ComputerVision/10-GANs/GANTF.ipynb">TensorFlow GAN</a><br/><a href="lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb">Transferência de Estilo</a></td><td></td></tr>
<tr><td>11</td><td>Detecção de Objetos</td><td><a href="lessons/4-ComputerVision/11-ObjectDetection/README.md">Texto</a></td><td>PyTorch</td><td><a href="lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb">TensorFlow</td><td><a href="lessons/4-ComputerVision/11-ObjectDetection/lab/README.md">Lab</a></td></tr>
<tr><td>12</td><td>Segmentação Semântica. U-Net</td><td><a href="lessons/4-ComputerVision/12-Segmentation/README.md">Texto</a></td><td><a href="lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb">PyTorch</td><td><a href="lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb">TensorFlow</td><td></td></tr>
<tr><td>V</td><td><b><a href="lessons/5-NLP/README.md">Processamento de Linguagem Natural</a></b></td>
   <td colspan="3"><a href="https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-cacaste"><i>Fundamentos da IA: explore o processamento de linguagem natural</i></a></td>
   <td></td></tr>
<tr><td></td><td colspan="2"><i>Módulo Microsoft Learn em Linguagem Natural</i></td>
   <td><a href="https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste"><i>PyTorch</i></a></td>
   <td><a href="https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste"><i>TensorFlow</i></a></td>
   <td></td></tr>
<tr><td>13</td><td>Representação de Texto. Arco/TF-IDF</td><td><a href="lessons/5-NLP/13-TextRep/README.md">Text</a></td><td><a href="lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb">TensorFlow</td><td></td></tr>
<tr><td>14</td><td>Incorporações semânticas de palavras. Word2Vec e GloVe</td><td><a href="lessons/5-NLP/14-Embeddings/README.md">Texto</td><td><a href="lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb">TensorFlow</a></td><td></td></tr>
<tr><td>15</td><td>Modelagem de Linguagem. Treinando suas próprias incorporações</td><td><a href="lessons/5-NLP/15-LanguageModeling/README.md">Texto</a></td><td><a href="lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb">PyTorch</a></td><td><a href="lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb">TensorFlow</a></td><td><a href="lessons/5-NLP/15-LanguageModeling/lab/README.md">Lab</a></td></tr>
<tr><td>16</td><td>Redes Neurais Recorrentes</td><td><a href="lessons/5-NLP/16-RNN/README.md">Texto</a></td><td><a href="lessons/5-NLP/16-RNN/RNNPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/5-NLP/16-RNN/RNNTF.ipynb">TensorFlow</a></td><td></td></tr>
<tr><td>17</td><td>Redes Gerativas Recorrentes</td><td><a href="lessons/5-NLP/17-GenerativeNetworks/README.md">Texto</a></td><td><a href="lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.md">PyTorch</a></td><td><a href="lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.md">TensorFlow</a></td><td><a href="lessons/5-NLP/17-GenerativeNetworks/lab/README.md">Lab</a></td></tr>
<tr><td>18</td><td>Transformadores. BERT.</td><td><a href="lessons/5-NLP/18-Transformers/README.md">Texto</a></td><td><a href="lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/5-NLP/18-Transformers/TransformersTF.ipynb">TensorFlow</a></td><td></td></tr>
<tr><td>19</td><td>Reconhecimento de Entidade Nomeada</td><td><a href="lessons/5-NLP/19-NER/README.md">Texto</a></td><td></td><td><a href="lessons/5-NLP/19-NER/NER-TF.ipynb">TensorFlow</a></td><td><a href="lessons/5-NLP/19-NER/lab/README.md">Lab</a></td></tr>
<tr><td>20</td><td>Modelos de Linguagem Grande, Programação Prompt e Tarefas de Poucos Tiros</td><td><a href="lessons/5-NLP/20-LangModels/README.md">Texto</a></td><td><a href="lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb">PyTorch</td><td></td><td></td></tr>
<tr><td>VI</td><td colspan="4"><b>Outras Técnicas de IA</b></td><td></td></tr>
<tr><td>21</td><td>Algorítmos Genéticos</td><td><a href="lessons/6-Other/21-GeneticAlgorithms/README.md">Texto</a><td colspan="2"><a href="lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb">Notebook</a></td><td></td></tr>
<tr><td>22</td><td>Aprendizado por Reforço Profundo</td><td><a href="lessons/6-Other/22-DeepRL/README.md">Texto</a></td><td><a href="lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb">PyTorch</a></td><td><a href="lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb">TensorFlow</a></td><td><a href="lessons/6-Other/22-DeepRL/lab/README.md">Lab</a></td></tr>
<tr><td>23</td><td>Sistemas Multiagentes</td><td><a href="lessons/6-Other/23-MultiagentSystems/README.md">Texto</a></td><td></td><td></td><td></td></tr>
<tr><td>VII</td><td colspan="4"><b>Ética da IA</b></td><td></td></tr>
<tr><td>24</td><td>Ética de IA e IA Responsável</td><td><a href="lessons/7-Ethics/README.md">Texto</a></td><td colspan="2"><a href="https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste"><i>MS Learn: princípios de IA Responsável</i></a></td><td></td></tr>
<tr><td></td><td colspan="4"><b>Extras</b></td><td></td></tr>
<tr><td>X1</td><td>Redes Multimodais, CLIP e VQGAN</td><td><a href="lessons/X-Extras/X1-MultiModal/README.md">Texto</a></td><td colspan="2"><a href="lessons/X-Extras/X1-MultiModal/Clip.ipynb">Notebook</a></td><td></td></tr>
</table>

**[Mapa Mental do Curso](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

Cada lição contém algum material de pré-leitura (link como **Texto** acima) e alguns Jupyter Notebooks executáveis, que geralmente são específicos para a estrutura (**PyTorch** ou **TensorFlow**). O notebook executável também contém muito material teórico, portanto, para entender o tópico, você precisa passar por pelo menos uma versão dos notebooks (PyTorch ou TensorFlow). Há também **Labs** disponíveis para alguns tópicos, que oferecem a oportunidade de tentar aplicar o material aprendido a um problema específico.

Algumas seções também contêm links para módulos do **MS Learn** que abrangem tópicos relacionados. O Microsoft Learn fornece um ambiente de aprendizado conveniente habilitado para GPU, embora em termos de conteúdo você possa esperar que este currículo seja um pouco mais profundo.

# Você é estudante?

Comece com os seguintes recursos:

- [Página do Hub do Aluno](https://docs.microsoft.com/learn/student-hub?WT.mc_id=academic-77998-cacaste) Nesta página, você encontrará recursos para iniciantes, pacotes de estudante e até formas de obter um voucher de certificado gratuito. Esta é uma página que você deseja marcar e verificar de tempos em tempos, pois trocamos o conteúdo pelo menos uma vez por mês.
- [Embaixadores do Microsoft Student Learn](https://studentambassadors.microsoft.com?WT.mc_id=academic-77998-cacaste) Junte-se a uma comunidade global de estudantes embaixadores, este pode ser o seu caminho para a Microsoft.

# Começando

**Estudantes**, existem algumas maneiras de usar o currículo. Em primeiro lugar, você pode apenas ler o texto e examinar o código diretamente no GitHub. Se você deseja executar o código em qualquer um dos notebooks - [leia nossas instruções](./etc/how-to-run.md), e encontre mais conselhos sobre como fazer isso [neste post do blog](https://soshnikov.com/education/how-to-execute-notebooks-from-github/).

> **Observação**: [Instruções sobre como executar o código neste currículo](./etc/how-to-run.md)

No entanto, se você quiser fazer o curso como um projeto de autoestudo, sugerimos que você faça um fork de todo o repo para sua própria conta do GitHub e conclua os exercícios sozinho ou com um grupo:

- Comece com um questionário pré-aula
- Leia o texto de introdução da palestra
- Se a palestra tiver notebooks adicionais, percorra-os, lendo e executando o código. Se os notebooks TensorFlow e PyTorch forem fornecidos, você pode se concentrar em um deles - escolha sua estrutura favorita
- Os notebooks geralmente contêm alguns dos desafios que exigem que você ajuste um pouco o código para experimentar
- Faça o teste pós-palestra
- Se houver um laboratório anexado ao módulo - conclua a tarefa
- Visite o [Fórum de Discussão](https://github.com/microsoft/AI-For-Beginners/discussions) para "aprender em voz alta".
- Bate-papo com outros alunos [no Gitter](https://gitter.im/Microsoft/ai-for-beginners) ou [no canal do Telegram](http://t.me/ai_for_beginners).

> Para um estudo mais aprofundado, recomendamos seguir estes [Microsoft Learn](https://docs.microsoft.com/en-us/users/dmitrysoshnikov-9132/collections/31zgizg2p418yo/?WT.mc_id=academic-77998-cacaste) módulos e caminhos de aprendizagem.

**Professores**, nós [incluímos algumas sugestões](/etc/for-teachers.md) sobre como usar este currículo.

---

## Créditos

**✍️ Autor Primário:** [Dmitry Soshnikov](http://soshnikov.com), PhD <br/>
**🔥 Editor:** [Jen Looper](https://twitter.com/jenlooper), PhD <br/>
**🎨 Ilustrador Sketchnote:** [Tomomi Imura](https://twitter.com/girlie_mac) <br/>
**✅ Criador de Quiz:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)  <br/>
**🙏 Principais Colaboradores:** [Evgenii Pishchik](https://github.com/Pe4enIks) 

## Conheça o Time

[![Promo video](/lessons/sketchnotes/ai-for-beginners.png)](https://youtu.be/m2KrAk0cC1c "Promo video")

> 🎥 Clique na imagem acima para ver um vídeo sobre o projeto e as pessoas que o criaram!

---

## Pedagogia

Escolhemos dois princípios pedagógicos ao construir este currículo: garantir que seja prático **baseado em projeto** e que inclua **testes frequentes**.

Ao garantir que o conteúdo esteja alinhado com os projetos, o processo se torna mais envolvente para os alunos e a retenção de conceitos aumenta. Além disso, um questionário de baixo risco antes de uma aula define a intenção do aluno em relação ao aprendizado de um tópico, enquanto um segundo questionário após a aula garante maior retenção. Este currículo foi projetado para ser flexível e divertido e pode ser feito no todo ou em parte. Os projetos começam pequenos e se tornam cada vez mais complexos ao final do ciclo de 12 semanas.

> Encontre nosso [Código de Conduta](/etc/CODE_OF_CONDUCT.md), [Contribuindo](/etc/CONTRIBUTING.md), e [Tradução](/etc/TRANSLATIONS.md) diretrizes. Encontre nossa [Documentação de suporte aqui](/etc/SUPPORT.md) e [informações de segurança aqui](/etc/SECURITY.md). Congratulamo-nos com o seu feedback construtivo!

>**Uma observação sobre questionários**: Todos os questionários estão contidos [neste aplicativo](https://red-field-0a6ddfd03.1.azurestaticapps.net/), para 50 questionários totais de três perguntas cada. Eles estão vinculados nas lições, mas o aplicativo de teste pode ser executado localmente; siga as instruções na pasta `etc/quiz-app`.

## Acesso off-line

Você pode executar esta documentação off-line usando [Docsify](https://docsify.js.org/#/). Fork este repositório, [instale Docsify](https://docsify.js.org/#/quickstart) na usa  máquina local, e, em seguida, na pasta `etc/docsify` deste repositório, digite `docsify serve`. O site será executado na porta 3000 em seu localhost: `localhost:3000`. Um pdf do currículo está disponível [neste link](/etc/pdf/readme.pdf).

## Procura-se ajuda!

Gostaria de contribuir com uma tradução? Leia nossas [diretrizes de tradução](/etc/TRANSLATIONS.md).

## Outros currículos

Nossa equipe produz outros currículos! Veja:

- [Desenvolvimento Web para Iniciantes](https://aka.ms/webdev-beginners)
- [IoT para Iniciantes](https://aka.ms/iot-beginners)
- [Machine Learning para Iniciantes](https://aka.ms/ml-beginners)
- [Data Science para Iniciantes](https://aka.ms/datascience-beginners)
