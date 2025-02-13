# 주의 메커니즘과 트랜스포머

## [강의 전 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/118)

자연어 처리(NLP) 분야에서 가장 중요한 문제 중 하나는 **기계 번역**으로, Google Translate와 같은 도구의 기초가 되는 필수 작업입니다. 이 섹션에서는 기계 번역, 또는 더 일반적으로는 모든 *시퀀스-투-시퀀스* 작업(이 작업은 **문장 전이**라고도 불림)에 초점을 맞출 것입니다.

RNN을 사용하면 시퀀스-투-시퀀스는 두 개의 순환 네트워크로 구현됩니다. 한 네트워크인 **인코더**는 입력 시퀀스를 숨겨진 상태로 압축하고, 다른 네트워크인 **디코더**는 이 숨겨진 상태를 번역된 결과로 풀어냅니다. 이 접근 방식에는 몇 가지 문제가 있습니다:

* 인코더 네트워크의 최종 상태는 문장의 시작 부분을 기억하는 데 어려움을 겪어 긴 문장에 대해 모델의 품질이 저하됩니다.
* 시퀀스의 모든 단어가 결과에 동일한 영향을 미칩니다. 그러나 실제로는 입력 시퀀스의 특정 단어가 다른 단어보다 순차적 출력에 더 큰 영향을 미치는 경우가 많습니다.

**주의 메커니즘**은 RNN의 각 출력 예측에 대한 각 입력 벡터의 맥락적 영향을 가중치로 조정하는 수단을 제공합니다. 이를 구현하는 방법은 입력 RNN의 중간 상태와 출력 RNN 사이에 단축 경로를 생성하는 것입니다. 이렇게 하면 출력 기호 y<sub>t</sub>를 생성할 때 모든 입력 숨겨진 상태 h<sub>i</sub>를 서로 다른 가중치 계수 α<sub>t,i</sub>와 함께 고려합니다.

![인코더/디코더 모델과 추가적인 주의 레이어를 보여주는 이미지](../../../../../translated_images/encoder-decoder-attention.7a726296894fb567aa2898c94b17b3289087f6705c11907df8301df9e5eeb3de.ko.png)

> [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf)에서 인용된 추가적인 주의 메커니즘을 가진 인코더-디코더 모델, [이 블로그 게시물](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)에서 인용됨

주의 행렬 {α<sub>i,j</sub>}는 특정 입력 단어가 출력 시퀀스의 주어진 단어 생성에 기여하는 정도를 나타냅니다. 아래는 이러한 행렬의 예입니다:

![RNNsearch-50에 의해 발견된 샘플 정렬을 보여주는 이미지, Bahdanau - arviz.org에서 가져옴](../../../../../translated_images/bahdanau-fig3.09ba2d37f202a6af11de6c82d2d197830ba5f4528d9ea430eb65fd3a75065973.ko.png)

> [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf)에서의 그림 (Fig.3)

주의 메커니즘은 현재 또는 거의 현재의 NLP 최첨단 기술의 많은 부분을 담당하고 있습니다. 그러나 주의를 추가하면 모델 매개변수의 수가 크게 증가하여 RNN의 확장성 문제로 이어집니다. RNN의 확장성에 대한 주요 제약은 모델의 순환적 특성으로 인해 배치 및 병렬 학습이 어렵다는 것입니다. RNN에서는 시퀀스의 각 요소를 순차적으로 처리해야 하므로 쉽게 병렬화할 수 없습니다.

![주의를 가진 인코더 디코더](../../../../../lessons/5-NLP/18-Transformers/images/EncDecAttention.gif)

> [Google의 블로그](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)에서의 그림

주의 메커니즘의 채택과 이러한 제약이 결합되어 현재 우리가 알고 사용하고 있는 최첨단 트랜스포머 모델, 예를 들어 BERT에서 Open-GPT3까지의 모델이 만들어졌습니다.

## 트랜스포머 모델

트랜스포머의 주요 아이디어 중 하나는 RNN의 순차적 특성을 피하고 훈련 중 병렬화할 수 있는 모델을 만드는 것입니다. 이는 두 가지 아이디어를 구현함으로써 달성됩니다:

* 위치 인코딩
* RNN(또는 CNN) 대신 패턴을 포착하기 위해 자기 주의 메커니즘 사용 (그래서 트랜스포머를 소개하는 논문이 *[Attention is all you need](https://arxiv.org/abs/1706.03762)*라고 불리는 이유입니다.)

### 위치 인코딩/임베딩

위치 인코딩의 아이디어는 다음과 같습니다.
1. RNN을 사용할 때 토큰의 상대적 위치는 단계 수로 표현되므로 명시적으로 표현할 필요가 없습니다.
2. 그러나 주의로 전환하면 시퀀스 내의 토큰의 상대적 위치를 알아야 합니다.
3. 위치 인코딩을 얻기 위해 시퀀스의 토큰과 함께 시퀀스 내의 토큰 위치 시퀀스를 보강합니다(즉, 숫자 시퀀스 0, 1, ...).
4. 그런 다음 토큰 위치를 토큰 임베딩 벡터와 혼합합니다. 위치(정수)를 벡터로 변환하기 위해 여러 가지 접근 방식을 사용할 수 있습니다:

* 토큰 임베딩과 유사한 학습 가능한 임베딩. 이것이 우리가 여기서 고려하는 접근 방식입니다. 우리는 토큰과 그 위치 모두에 대해 임베딩 레이어를 적용하여 동일한 차원의 임베딩 벡터를 생성하고 이를 더합니다.
* 원래 논문에서 제안된 고정 위치 인코딩 함수.

<img src="images/pos-embedding.png" width="50%"/>

> 저자에 의해 제공된 이미지

우리가 위치 임베딩으로 얻는 결과는 원래의 토큰과 시퀀스 내의 위치를 모두 포함합니다.

### 다중 헤드 자기 주의

다음으로, 우리는 시퀀스 내에서 몇 가지 패턴을 포착해야 합니다. 이를 위해 트랜스포머는 **자기 주의** 메커니즘을 사용하며, 이는 기본적으로 입력과 출력으로 동일한 시퀀스에 적용되는 주의입니다. 자기 주의를 적용하면 문장 내의 **맥락**을 고려하고 어떤 단어가 서로 관련되어 있는지를 확인할 수 있습니다. 예를 들어, 이는 *it*와 같은 대명사가 지칭하는 단어를 확인하고 맥락을 고려할 수 있게 해줍니다:

![](../../../../../translated_images/CoreferenceResolution.861924d6d384a7d68d8d0039d06a71a151f18a796b8b1330239d3590bd4947eb.ko.png)

> [Google 블로그](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)에서의 이미지

트랜스포머에서는 **다중 헤드 주의**를 사용하여 네트워크가 여러 유형의 의존성을 포착할 수 있는 능력을 부여합니다. 예를 들어, 장기 대 단기 단어 관계, 공동 참조 대 다른 것 등입니다.

[TensorFlow 노트북](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb)에는 트랜스포머 레이어 구현에 대한 자세한 내용이 포함되어 있습니다.

### 인코더-디코더 주의

트랜스포머에서는 주의가 두 곳에서 사용됩니다:

* 자기 주의를 사용하여 입력 텍스트 내의 패턴을 포착하기 위해
* 시퀀스 번역을 수행하기 위해 - 이는 인코더와 디코더 사이의 주의 레이어입니다.

인코더-디코더 주의는 이 섹션의 시작 부분에서 설명한 RNN에서 사용되는 주의 메커니즘과 매우 유사합니다. 이 애니메이션 다이어그램은 인코더-디코더 주의의 역할을 설명합니다.

![트랜스포머 모델에서 평가가 수행되는 방법을 보여주는 애니메이션 GIF.](../../../../../lessons/5-NLP/18-Transformers/images/transformer-animated-explanation.gif)

각 입력 위치가 각 출력 위치에 독립적으로 매핑되기 때문에 트랜스포머는 RNN보다 더 나은 병렬화를 가능하게 하여 훨씬 더 크고 표현력이 풍부한 언어 모델을 생성할 수 있습니다. 각 주의 헤드는 단어 간의 다양한 관계를 학습하는 데 사용될 수 있으며, 이는 하위 자연어 처리 작업을 개선합니다.

## BERT

**BERT** (Bidirectional Encoder Representations from Transformers)는 *BERT-base*의 경우 12층, *BERT-large*의 경우 24층으로 구성된 매우 큰 다층 트랜스포머 네트워크입니다. 이 모델은 먼저 대규모 텍스트 데이터(위키피디아 + 책)에서 비지도 학습(문장에서 마스킹된 단어 예측)을 사용하여 사전 훈련됩니다. 사전 훈련 동안 모델은 상당한 수준의 언어 이해를 흡수하며, 이는 이후 다른 데이터 세트와 함께 미세 조정하여 활용될 수 있습니다. 이 과정을 **전이 학습**이라고 합니다.

![http://jalammar.github.io/illustrated-bert/에서 가져온 이미지](../../../../../translated_images/jalammarBERT-language-modeling-masked-lm.34f113ea5fec4362e39ee4381aab7cad06b5465a0b5f053a0f2aa05fbe14e746.ko.png)

> 이미지 [출처](http://jalammar.github.io/illustrated-bert/)

## ✍️ 연습: 트랜스포머

다음 노트북에서 학습을 계속하세요:

* [PyTorch에서의 트랜스포머](../../../../../lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb)
* [TensorFlow에서의 트랜스포머](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb)

## 결론

이번 수업에서는 트랜스포머와 주의 메커니즘에 대해 배웠으며, 이는 NLP 도구 상자에서 필수적인 도구입니다. BERT, DistilBERT, BigBird, OpenGPT3 등 많은 변형의 트랜스포머 아키텍처가 있으며, 이들은 미세 조정이 가능합니다. [HuggingFace 패키지](https://github.com/huggingface/)는 PyTorch와 TensorFlow 모두에서 이러한 아키텍처를 훈련하기 위한 저장소를 제공합니다.

## 🚀 도전

## [강의 후 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/218)

## 복습 및 자습

* [블로그 게시물](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/), 트랜스포머에 대한 고전적인 [Attention is all you need](https://arxiv.org/abs/1706.03762) 논문을 설명합니다.
* 트랜스포머에 대한 [일련의 블로그 게시물](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452), 아키텍처를 자세히 설명합니다.

## [과제](assignment.md)

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서는 해당 언어로 된 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 우리는 책임을 지지 않습니다.