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

# 초보자를 위한 인공지능

|![ Sketchnote by [(@girlie_mac)](https://twitter.com/girlie_mac) ](/lessons/sketchnotes/ai-overview.png)|
|:---:|
| AI For Beginners - _Sketchnote by [@girlie_mac](https://twitter.com/girlie_mac)_ |

마이크로 소프트와 함께 12주, 24개의 강의를 통해 **인공지능**의 세계를 탐험하세요! 기호주의(Symbolic) AI, 인공신경망, 컴퓨터비전, 자연어처리 등을 탐구하세요. 실습형 강의와 퀴즈, 자유로운 실험을 통해 학습하세요. 본 과정은 텐서플로우, 파이토치, AI윤리를 기반으로 초보자에게 적합하게 고안되었습니다. 인공지능으로의 여행을 시작하세요!
심볼
이 과정에서 배울 것은 아래와 같습니다: 

* **지식 표현**과 추론처럼 "좋지만 오래된" 기호주의적 접근 등의 다양한 인공지능을 해석하는 관점.  
* 근대 AI의 핵심인 **인공신경망**과 **심층신경망**. 가장 유명한 프레임워크인 [텐서플로우(Tensorflow)](http://Tensorflow.org)와 [파이토치(Pytorch)](http://pytorch.org)를 사용하여 두 주제에 대한 개념을 코드로 이해할 것입니다.  
* 사진과 글자에 사용되는 **신경망 구조**. 오래되지 않은 모델을 배울것이지만 완전 최신이라고 하기엔 부족할 수도 있습니다. 
* **유전 알고리즘**과 **다중 에이전트 시스템**같은 덜 유명한 AI기법. 

아래와 같은 주제는 본 과정에서 다루지 않습니다:

* 기업에서의 **AI 활용사례**. MS Learn의 [기업 사용자를 위한 AI 소개](https://docs.microsoft.com/learn/paths/introduction-ai-for-business-users/?WT.mc_id=academic-77998-cacaste)나, 세계 최고의 경영대학 중 하나인 [INSEAD](https://www.insead.edu/)와 협력하여 만든 [Microsoft AI를 통한 비즈니스 혁신](https://www.microsoft.com/ai/ai-business-school/?WT.mc_id=academic-77998-cacaste) 학습경로를 참고하세요. 
* **기계학습**, 이를 위한 학습과정은 [초보자를 위한 기계학습](http://github.com/Microsoft/ML-for-Beginners)에 따로 준비되어있습니다.
* **애저 AI 서비스**를 사용한 AI 구축. [컴퓨터 비전](https://docs.microsoft.com/learn/paths/create-computer-vision-solutions-azure-cognitive-services/?WT.mc_id=academic-77998-cacaste), [자연어 처리](https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-cacaste), **[애저 오픈AI를 사용한 생성형 AI](https://learn.microsoft.com/en-us/training/paths/develop-ai-solutions-azure-openai/?WT.mc_id=academic-77998-bethanycheum)** 등과 같은 학습경로를 참고하세요. 
* [애저 기계학습](https://azure.microsoft.com/services/machine-learning/?WT.mc_id=academic-77998-cacaste), [Microsoft Fabric](https://learn.microsoft.com/en-us/training/paths/get-started-fabric/?WT.mc_id=academic-77998-bethanycheum), or [애저 Databricks](https://docs.microsoft.com/learn/paths/data-engineer-azure-databricks?WT.mc_id=academic-77998-cacaste)과 같은 특정 **클라우드 프레임워크**. [애저 기계 학습 작업 영역 살펴보기](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/?WT.mc_id=academic-77998-cacaste)와 [Azure Databricks를 사용한 기계 학습](https://docs.microsoft.com/learn/paths/build-operate-machine-learning-solutions-azure-databricks/?WT.mc_id=academic-77998-cacaste) 학습경로를 참고하세요.
* **대화형 AI**와 **챗봇**. MS Learn의 [대화형 AI 만들기](https://docs.microsoft.com/learn/paths/create-conversational-ai-solutions/?WT.mc_id=academic-77998-cacaste) 학습경로를 참고하세요. 자세히 알고 싶다면 [이 블로그 글](https://soshnikov.com/azure/hello-bot-conversational-ai-on-microsoft-platform/)을 참고하세요.
* **AI 수학**. [심층학습](https://product.kyobobook.co.kr/detail/S000001916915) 책을 추천합니다. 

*클라우드에서의 AI*에 간단히 알고 싶다면 [Microsoft 애저 AI 기본 사항: AI 개요](https://docs.microsoft.com/learn/paths/get-started-with-artificial-intelligence-on-azure/?WT.mc_id=academic-77998-cacaste) 학습경로를 참고하세요.

## 안내사항 - 생성형 AI에 대한 학습과정이 새로 출시되었습니다!

생성형 AI에 대한 12개의 강의를 통해 배울 것은 아래와 같습니다:

- 프롬프트 엔지니어링 (생성형 AI에게 좋은 질문을 만드는 것을 의미합니다.)
- 텍스트 및 이미지 생성 앱
- 검색 앱

이 과정 역시 강의와, 과제, 퀴즈 등으로 구성되어 있습니다. 

> https://aka.ms/genai-beginners

---
# 강의 목록

<table>
<tr><th width = 75>순번</th><th>강의명</th><th width = 75>개요</th><th>PyTorch</th><th>Keras/TensorFlow</th><th>Lab</th></tr>

<tr><td>I</td><td colspan="4"><b>AI 소개</b></td><td></td></tr>
<tr><td>1</td><td>AI의 역사</td><td><a href="lessons/1-Intro/README.md">읽기</a></td><td></td><td></td><td></td></tr>

<tr><td>II</td><td colspan="4"><b>Symbolic AI</b></td><td></td></tr>
<tr><td>2 </td><td>지식표현과 전문가시스템</td><td><a href="lessons/2-Symbolic/README.md">읽기</a></td><td colspan="2"><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/Animals.ipynb">전문가시스템</a>, <a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/FamilyOntology.ipynb">온톨로지</a>, <a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/2-Symbolic/MSConceptGraph.ipynb">개념 그래프</a></td><td></td></tr>
<tr><td>III</td><td colspan="4"><b><a href="lessons/3-NeuralNetworks/README.md">신경망 소개</a></b></td><td></td></tr>
<tr><td>3</td><td>퍼셉트론</td>
   <td><a href="lessons/3-NeuralNetworks/03-Perceptron/README.md">읽기</a>
   <td colspan="2"><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb">Notebook</a></td><td><a href="lessons/3-NeuralNetworks/03-Perceptron/lab/README.md">Lab</a></td></tr>
<tr><td>4 </td><td>다층 퍼셉트론 <br> 나만의 프레임워크 만들기</td><td><a href="lessons/3-NeuralNetworks/04-OwnFramework/README.md">Text</a></td><td colspan="2"><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb">Notebook</a><td><a href="lessons/3-NeuralNetworks/04-OwnFramework/lab/README.md">Lab</a></td></tr> 
<tr><td>5</td>
   <td>프레임워크(PyTorch/TensorFlow) 개요 <br> 과적합</td>
   <td><a href="lessons/3-NeuralNetworks/05-Frameworks/README.md">읽기</a></td>
   <td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb">PyTorch</a></td>
   <td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb">Keras</a>/<a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb">TensorFlow</a></td>
   <td><a href="lessons/3-NeuralNetworks/05-Frameworks/lab/README.md">Lab</a></td></tr>
<tr><td>IV</td><td><b><a href="lessons/4-ComputerVision/README.md">컴퓨터 비전</a></b></td>
  <td colspan="3"><a href="https://docs.microsoft.com/learn/paths/explore-computer-vision-microsoft-azure/?WT.mc_id=academic-77998-cacaste"><i>Microsoft 애저 AI 기본 사항: 컴퓨터 비전</i></a></td>
  <td></td></tr>
<tr><td></td><td colspan="2"><i>컴퓨터 비전에 대한 Microsoft Learn 모듈</i></td>
  <td><a href="https://docs.microsoft.com/learn/modules/intro-computer-vision-pytorch/?WT.mc_id=academic-77998-cacaste"><i>PyTorch</i></a></td>
  <td><a href="https://docs.microsoft.com/learn/modules/intro-computer-vision-TensorFlow/?WT.mc_id=academic-77998-cacaste"><i>TensorFlow</i></a></td>
  <td></td></tr>
<tr><td>6</td><td>컴퓨터 비전 개요, OpenCV</td><td><a href="lessons/4-ComputerVision/06-IntroCV/README.md">읽기</a><td colspan="2"><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb">Notebook</a></td><td><a href="lessons/4-ComputerVision/06-IntroCV/lab/README.md">Lab</a></td></tr>
<tr><td>7</td><td>CNN, 합성곱 신경망</td><td><a href="lessons/4-ComputerVision/07-ConvNets/README.md">읽기</a><br/><a href="lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md">읽기</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb">PyTorch</a></td><td><a href="lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb">TensorFlow</a></td><td><a href="lessons/4-ComputerVision/07-ConvNets/lab/README.md">Lab</a></td></tr>
<tr><td>8</td><td>사전 학습 모델과 전이학습<br/>학습 기법들</td><td><a href="lessons/4-ComputerVision/08-TransferLearning/README.md">읽기</a><br/><a href="lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md">읽기</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb">PyTorch</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb">TensorFlow</a><br/><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb">드롭아웃 예제</a><br/><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb">Adversarial Cat</a></td><td><a href="lessons/4-ComputerVision/08-TransferLearning/lab/README.md">Lab</a></td></tr>
<tr><td>9</td><td>오토인코더와 VAE</td><td><a href="lessons/4-ComputerVision/09-Autoencoders/README.md">읽기</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb">PyTorch</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb">TensorFlow</a></td><td></td></tr>
<tr><td>10</td><td>생성적 적대 신경망<br/>미술 스타일 학습</td><td><a href="lessons/4-ComputerVision/10-GANs/README.md">읽기</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb">PyTorch</td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/10-GANs/GANTF.ipynb">TensorFlow GAN</a><br/><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb">Style Transfer</a></td><td></td></tr>
<tr><td>11</td><td>객체 인식</td><td><a href="lessons/4-ComputerVision/11-ObjectDetection/README.md">읽기</a></td><td>PyTorch</td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/11-ObjectDetection/ObjectDetection.ipynb">TensorFlow</td><td><a href="lessons/4-ComputerVision/11-ObjectDetection/lab/README.md">Lab</a></td></tr>
<tr><td>12</td><td>의미적 분할, U-Net</td><td><a href="lessons/4-ComputerVision/12-Segmentation/README.md">읽기</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb">PyTorch</td><td><a href="lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb">TensorFlow</td><td></td></tr>
<tr><td>V</td><td><b><a href="lessons/5-NLP/README.md">자연어 처리</a></b></td>
   <td colspan="3"><a href="https://docs.microsoft.com/learn/paths/explore-natural-language-processing/?WT.mc_id=academic-77998-cacaste"><i>Microsoft 애저 AI 기본 사항: 자연어 처리</i></a></td>
   <td></td></tr>
<tr><td></td><td colspan="2"><i>자연어 처리에 대한 Microsoft Learn 모듈</i></td>
   <td><a href="https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste"><i>PyTorch</i></a></td>
   <td><a href="https://docs.microsoft.com/learn/modules/intro-natural-language-processing-TensorFlow/?WT.mc_id=academic-77998-cacaste"><i>TensorFlow</i></a></td>
   <td></td></tr>
<tr><td>13</td><td>글자 표현, Bow/TF-IDF</td><td><a href="lessons/5-NLP/13-TextRep/README.md">읽기</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb">PyTorch</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb">TensorFlow</td><td></td></tr>
<tr><td>14</td><td>의미적 단어 임베딩, Word2Vec과 GloVe</td><td><a href="lessons/5-NLP/14-Embeddings/README.md">읽기</td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb">PyTorch</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb">TensorFlow</a></td><td></td></tr>
<tr><td>15</td><td>언어 모델링, 나만의 임베딩 만들기</td><td><a href="lessons/5-NLP/15-LanguageModeling/README.md">읽기</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb">PyTorch</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb">TensorFlow</a></td><td><a href="lessons/5-NLP/15-LanguageModeling/lab/README.md">Lab</a></td></tr>
<tr><td>16</td><td>순환 신경망</td><td><a href="lessons/5-NLP/16-RNN/README.md">읽기</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNPyTorch.ipynb">PyTorch</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/16-RNN/RNNTF.ipynb">TensorFlow</a></td><td></td></tr>
<tr><td>17</td><td>생성적 순환 신경망</td><td><a href="lessons/5-NLP/17-GenerativeNetworks/README.md">읽기</a></td><td><a href="lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.md">PyTorch</a></td><td><a href="lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.md">TensorFlow</a></td><td><a href="lessons/5-NLP/17-GenerativeNetworks/lab/README.md">Lab</a></td></tr>
<tr><td>18</td><td>트랜스포머, BERT</td><td><a href="lessons/5-NLP/18-Transformers/README.md">읽기</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb">PyTorch</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/5-NLP/18-Transformers/TransformersTF.ipynb">TensorFlow</a></td><td></td></tr>
<tr><td>19</td><td>개체명 인식</td><td><a href="lessons/5-NLP/19-NER/README.md">읽기</a></td><td></td><td><a href="lessons/5-NLP/19-NER/NER-TF.ipynb">TensorFlow</a></td><td><a href="lessons/5-NLP/19-NER/lab/README.md">Lab</a></td></tr>
<tr><td>20</td><td>LLM, 대규모 언어 모델 <br> 프롬프트 프로그래밍과 Few-Shot 학습</td><td><a href="lessons/5-NLP/20-LangModels/README.md">읽기</a></td><td><a href="lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb">PyTorch</td><td></td><td></td></tr>
<tr><td>VI</td><td colspan="4"><b>다른 AI 기법</b></td><td></td></tr>
<tr><td>21</td><td>유전 알고리즘</td><td><a href="lessons/6-Other/21-GeneticAlgorithms/README.md">읽기</a><td colspan="2"><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6-Other/21-GeneticAlgorithms/Genetic.ipynb">Notebook</a></td><td></td></tr>
<tr><td>22</td><td>심층 강화학습</td><td><a href="lessons/6-Other/22-DeepRL/README.md">읽기</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6-Other/22-DeepRL/CartPole-RL-PyTorch.ipynb">PyTorch</a></td><td><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/6-Other/22-DeepRL/CartPole-RL-TF.ipynb">TensorFlow</a></td><td><a href="lessons/6-Other/22-DeepRL/lab/README.md">Lab</a></td></tr>
<tr><td>23</td><td>다중 에이전트 시스템</td><td><a href="lessons/6-Other/23-MultiagentSystems/README.md">읽기</a></td><td></td><td></td><td></td></tr>
<tr><td>VII</td><td colspan="4"><b>AI 윤리</b></td><td></td></tr>
<tr><td>24</td><td>AI 윤리와 책임있는 AI</td><td><a href="lessons/7-Ethics/README.md">읽기</a></td><td colspan="2"><a href="https://docs.microsoft.com/learn/paths/responsible-ai-business-principles/?WT.mc_id=academic-77998-cacaste"><i>MS Learn: Responsible AI Principles(링크 없음)</i></a></td><td></td></tr>
<tr><td></td><td colspan="4"><b>기타</b></td><td></td></tr>
<tr><td>X1</td><td>멀티모달 신경망, CLIP과 VQGAN</td><td><a href="lessons/X-Extras/X1-MultiModal/README.md">읽기</a></td><td colspan="2"><a href="https://github.com/microsoft/AI-For-Beginners/blob/main/lessons/X-Extras/X1-MultiModal/Clip.ipynb">Notebook</a></td><td></td></tr>
</table>

**[마인드맵](http://soshnikov.com/courses/ai-for-beginners/mindmap.html)**

각 강의는 링크 되어있는 **읽기**와, **Pytorch**나 **Tensorflow** 등의 프레임워크로 코드를 실행할 수 있는 주피터 노트북(**Notebook**)으로 구성됩니다. 주피터 노트북에는 이론적인 설명도 많으니 두 프레임워크 중 하나는 꼭 확인해 주세요. **Labs**가 있는 강의도 있습니다. 이는 배운 것을 실습해 볼 수 있도록 가이드와 함께 문제가 준비되어 있습니다. 

몇몇 주제는 **MS Learn**과 링크되어 있습니다. 그 주제를 좀 더 공부하고 싶으시다면 참고하시길 바랍니다.

# 학생인가요?

아래의 사이트도 확인해보세요:

- [Microsoft 학생 허브](https://docs.microsoft.com/learn/student-hub?WT.mc_id=academic-77998-cacaste)
학생을 위한 다양한 학습자료, 개발도구 재공하고 있습니다.
- [Microsoft 커뮤니티리더](https://studentambassadors.microsoft.com?WT.mc_id=academic-77998-cacaste)
글로벌 학생 커뮤니티에 참여하세요. 

# 시작하기

**학생**이십니까? 이 과정을 사용하는 몇가지 방법을 소개하겠습니다. 우선 단순히 읽기 자료를 읽고 코드를 확인해 볼 수 있습니다. 주피터 노트북 코드 실행이 궁금하다면 [여기를 참고하세요](./etc/how-to-run.md), 더 자세한 설명은 [이 영문 블로그](https://soshnikov.com/education/how-to-execute-notebooks-from-github/)에도 있습니다.

> **안내사항**: [제공되는 코드를 실행하는 방법](./etc/how-to-run.md)

하지만, 깃허브를 통해 전체 레포지토리를 포크하고 혼자 혹은 그룹으로 과제들을 완료하는 것을 추천합니다.

- 사전 퀴즈를 먼저 풀어보세요.
- 강의 개요 읽기자료를 읽으세요.
- 주피터 노트북 자료가 있으면 코드를 읽어보고 실행해보세요. 프레임워크는 텐서플로우/파이토치 아무거나 하나만 집중하여 학습하세요.
- 노트북 자료에는 가끔 약간의 수정이 필요한 과제가 있을 수 있습니다. 
- 강의 수강 후 퀴즈를 풀어보세요. 
- lab이 있는 경우 그 과제를 완료하세요.
- [토의장](https://github.com/microsoft/AI-For-Beginners/discussions)에 방문하여 "다 같이 공부하세요".

> 더 자세한 공부를 위한다면, 이 [Microsoft Learn](https://docs.microsoft.com/en-us/users/dmitrysoshnikov-9132/collections/31zgizg2p418yo/?WT.mc_id=academic-77998-cacaste) 모듈과 학습경로를 따라 학습하는 것을 추천합니다. 

**교육자**를 위한 [몇 가지의 활용법](/etc/for-teachers.md)을 적어두었습니다.

---

## Credits

**✍️ Primary Author:** [Dmitry Soshnikov](http://soshnikov.com), PhD <br/>
**🔥 Editor:** [Jen Looper](https://twitter.com/jenlooper), PhD <br/>
**🎨 Sketchnote illustrator:** [Tomomi Imura](https://twitter.com/girlie_mac) <br/>
**✅ Quiz Creator:** [Lateefah Bello](https://github.com/CinnamonXI), [MLSA](https://studentambassadors.microsoft.com/)  <br/>
**🙏 Core Contributors:** [Evgenii Pishchik](https://github.com/Pe4enIks) 

## 제작자를 만나보세요

[![Promo video](/lessons/sketchnotes/ai-for-beginners.png)](https://youtu.be/m2KrAk0cC1c "Promo video")

> 🎥 제작자와 프로젝트에 대한 비디오를 보시려면 위의 그림을 클릭하세요!

---

## 학습철학

**프로젝트 기반 실습**과 **잦은 퀴즈**, 두가지 목적을 가지고 이 과정을 기획하였습니다. 

프로젝트 기반의 콘텐츠는 학생들의 흥미를 돋우고 내용을 기억하는 것에 도움이 됩니다. 그리고 사전 퀴즈는 이번에 어떤 것을 배우게 되는지 인지시키기 위해, 강의 후 퀴즈는 학습 내용의 보존을 위해 마련하였습니다. 재미있고 유연하게 기획되었기 때문에 전체를 학습하는 것이 아니라 원하는 부분만을 학습해도 괜찮도록 만들었습니다. 처음에는 간단하겠지만 강의가 계속 될수록 점점 복잡해집니다. 

> [행동규칙](etc/CODE_OF_CONDUCT.md), [기여](etc/CONTRIBUTING.md) 그리고 [번역](etc/TRANSLATIONS.md) 가이드라인을 확인해보세요. Find our [지원](etc/SUPPORT.md)과 [보안](etc/SECURITY.md) 문서를 확인해보세요. 여러분의 피드백을 환영합니다!

> **퀴즈에 대한 안내사항**: 모든 퀴즈는 [여기](https://red-field-0a6ddfd03.1.azurestaticapps.net/)를 통해 풀 수 있습니다. 총 50개의 퀴즈에 각 3개의 문제가 있습니다. 웹앱이지만, 모든 내용은 프로젝트에 있으니 로컬로도 실행할 수 있습니다; `etc/quiz-app`을 확인해보세요. 

## Offline access

> 내용이 부정확하여 번역을 하지 않았습니다.

You can run this documentation offline by using [Docsify](https://docsify.js.org/#/). Fork this repo, [install Docsify](https://docsify.js.org/#/quickstart) on your local machine, and then in the `etc/docsify` folder of this repo, type `docsify serve`. The website will be served on port 3000 on your localhost: `localhost:3000`. A pdf of the curriculum is available [at this link](/etc/pdf/readme.pdf).

## 번역

번역을 원하시면 [번역 가이드라인](etc/TRANSLATIONS.md)을 확인하세요. 

## 다른 학습과정

- [초보자를 위한 인공지능](https://aka.ms/ai-beginners)
- [초보자를 위한 데이터 사이언스](https://aka.ms/datascience-beginners)
- [초보자를 위한 생성형 AI](https://aka.ms/genai-beginners)
- [초보자를 위한 웹 개발](https://aka.ms/webdev-beginners)
- [초보자를 위한 IoT](https://aka.ms/iot-beginners)
- [초보자를 위한 기계학습](https://aka.ms/ml-beginners)
- [초보자를 위한 XR 개발](https://aka.ms/xr-dev-for-beginners)
- [AI와 함께하는 개발: 깃허브 Copilot](https://aka.ms/GitHubCopilotAI)
