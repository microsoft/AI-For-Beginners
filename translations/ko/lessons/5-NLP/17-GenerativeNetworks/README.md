# 생성적 네트워크

## [강의 전 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/117)

순환 신경망(RNN)과 Long Short Term Memory Cells(LSTM), Gated Recurrent Units(GRU)와 같은 게이트가 있는 셀 변형은 언어 모델링을 위한 메커니즘을 제공하여 단어 순서를 학습하고 시퀀스에서 다음 단어에 대한 예측을 제공할 수 있습니다. 이를 통해 RNN을 일반적인 텍스트 생성, 기계 번역, 심지어 이미지 캡셔닝과 같은 **생성 작업**에 사용할 수 있습니다.

> ✅ 텍스트 입력 시 텍스트 완성과 같은 생성 작업의 혜택을 받은 모든 경우를 생각해 보세요. 좋아하는 애플리케이션이 RNN을 활용했는지 조사해 보세요.

이전 단원에서 논의한 RNN 아키텍처에서는 각 RNN 유닛이 다음 숨겨진 상태를 출력으로 생성했습니다. 그러나 각 순환 유닛에 또 다른 출력을 추가할 수 있으며, 이를 통해 **시퀀스**(원래 시퀀스와 길이가 동일)를 출력할 수 있습니다. 또한 각 단계에서 입력을 받지 않는 RNN 유닛을 사용하고, 초기 상태 벡터만 받아서 출력 시퀀스를 생성할 수 있습니다.

이로 인해 아래 그림에 나타난 다양한 신경망 아키텍처가 가능합니다:

![일반적인 순환 신경망 패턴을 보여주는 이미지.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.ko.jpg)

> 이미지 출처: [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) 블로그 게시물, [Andrej Karpaty](http://karpathy.github.io/) 저자

* **일대일**은 하나의 입력과 하나의 출력을 가지는 전통적인 신경망입니다.
* **일대다**는 하나의 입력 값을 받아 출력 값의 시퀀스를 생성하는 생성적 아키텍처입니다. 예를 들어, **이미지 캡셔닝** 네트워크를 훈련하여 사진의 텍스트 설명을 생성하려면 사진을 입력으로 사용하고 CNN을 통해 숨겨진 상태를 얻은 후, 순환 체인이 단어별로 캡션을 생성하도록 할 수 있습니다.
* **다대일**은 이전 단원에서 설명한 RNN 아키텍처에 해당하며, 예를 들어 텍스트 분류가 있습니다.
* **다대다**, 또는 **시퀀스-투-시퀀스**는 **기계 번역**과 같은 작업에 해당하며, 여기서 첫 번째 RNN이 입력 시퀀스의 모든 정보를 숨겨진 상태로 수집하고, 다른 RNN 체인이 이 상태를 출력 시퀀스로 펼칩니다.

이번 단원에서는 텍스트 생성을 도와주는 간단한 생성 모델에 집중할 것입니다. 간단함을 위해 문자 수준의 토큰화를 사용할 것입니다.

이 RNN을 단계별로 텍스트를 생성하도록 훈련시킬 것입니다. 각 단계에서 길이가 `nchars`인 문자 시퀀스를 가져와서 각 입력 문자에 대해 다음 출력 문자를 생성하도록 네트워크에 요청합니다:

![단어 'HELLO'의 RNN 생성 예시를 보여주는 이미지.](../../../../../translated_images/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.ko.png)

텍스트를 생성할 때(추론 중) 우리는 어떤 **프롬프트**로 시작하여 RNN 셀을 통해 이를 전달하여 중간 상태를 생성한 후, 이 상태에서 생성을 시작합니다. 우리는 한 번에 하나의 문자를 생성하고, 상태와 생성된 문자를 다른 RNN 셀에 전달하여 다음 문자를 생성합니다. 이 과정을 충분한 문자를 생성할 때까지 반복합니다.

<img src="images/rnn-generate-inf.png" width="60%"/>

> 저자 제공 이미지

## ✍️ 연습문제: 생성적 네트워크

다음 노트북에서 학습을 계속하세요:

* [PyTorch로 생성적 네트워크](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb)
* [TensorFlow로 생성적 네트워크](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)

## 부드러운 텍스트 생성과 온도

각 RNN 셀의 출력은 문자에 대한 확률 분포입니다. 생성된 텍스트에서 항상 가장 높은 확률을 가진 문자를 다음 문자로 선택하면, 텍스트가 같은 문자 시퀀스 간에 "순환"될 수 있습니다. 예를 들어 다음과 같습니다:

```
today of the second the company and a second the company ...
```

그러나 다음 문자의 확률 분포를 살펴보면, 몇 개의 가장 높은 확률 간의 차이가 크지 않을 수 있습니다. 예를 들어, 한 문자의 확률이 0.2이고, 다른 문자의 확률이 0.19일 수 있습니다. 예를 들어, 시퀀스 '*play*'에서 다음 문자는 공백이거나 **e** (단어 *player*에서처럼)일 수 있습니다.

이로 인해 우리는 항상 높은 확률을 가진 문자를 선택하는 것이 "공정"하지 않을 수 있다는 결론에 도달합니다. 두 번째로 높은 확률의 문자를 선택하는 것도 여전히 의미 있는 텍스트로 이어질 수 있습니다. 따라서 네트워크 출력에 의해 제공된 확률 분포에서 문자를 **샘플링**하는 것이 더 현명합니다. 또한 **온도**라는 매개변수를 사용하여 확률 분포를 평탄하게 하거나, 높은 확률의 문자에 더 집중하고 싶을 때 더 가파르게 만들 수 있습니다.

위에 링크된 노트북에서 이 부드러운 텍스트 생성이 어떻게 구현되는지 살펴보세요.

## 결론

텍스트 생성이 그 자체로 유용할 수 있지만, 주요 이점은 RNN을 사용하여 초기 특성 벡터에서 텍스트를 생성할 수 있는 능력에서 비롯됩니다. 예를 들어, 텍스트 생성은 기계 번역의 일부로 사용됩니다(이 경우 *인코더*에서의 상태 벡터가 번역된 메시지를 생성하거나 *디코드*하는 데 사용됨), 또는 이미지의 텍스트 설명을 생성하는 데 사용됩니다(이 경우 특성 벡터는 CNN 추출기에서 옵니다).

## 🚀 도전 과제

이 주제에 대해 Microsoft Learn에서 몇 가지 수업을 들어보세요.

* [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)로 텍스트 생성

## [강의 후 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/217)

## 복습 및 자기 학습

지식을 확장할 수 있는 몇 가지 기사를 소개합니다.

* Markov Chain, LSTM 및 GPT-2를 사용한 텍스트 생성의 다양한 접근 방식: [블로그 게시물](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* [Keras 문서](https://keras.io/examples/generative/lstm_character_level_text_generation/)에서의 텍스트 생성 샘플

## [과제](lab/README.md)

문자를 하나씩 생성하는 방법을 살펴보았습니다. 이번 실습에서는 단어 수준의 텍스트 생성을 탐구할 것입니다.

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서는 해당 언어로 작성된 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 우리는 책임을 지지 않습니다.