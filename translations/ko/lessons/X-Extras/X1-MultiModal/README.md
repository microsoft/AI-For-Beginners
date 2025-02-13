# 다중 모달 네트워크

NLP 작업을 해결하기 위한 트랜스포머 모델의 성공 이후, 동일하거나 유사한 아키텍처가 컴퓨터 비전 작업에 적용되었습니다. 비전과 자연어 능력을 *결합*하는 모델을 구축하려는 관심이 높아지고 있습니다. 이러한 시도의 하나는 OpenAI에 의해 이루어졌으며, CLIP와 DALL.E라고 불립니다.

## 대조 이미지 사전 학습 (CLIP)

CLIP의 주요 아이디어는 텍스트 프롬프트와 이미지를 비교하고 이미지가 프롬프트와 얼마나 잘 일치하는지를 판단할 수 있는 것입니다.

![CLIP 아키텍처](../../../../../translated_images/clip-arch.b3dbf20b4e8ed8be1c38e2bc6100fd3cc257c33cda4692b301be91f791b13ea7.ko.png)

> *[이 블로그 게시물](https://openai.com/blog/clip/)의 사진*

모델은 인터넷에서 얻은 이미지와 그 캡션으로 훈련됩니다. 각 배치마다 N 쌍의 (이미지, 텍스트)를 가져와서 일부 벡터 표현 I로 변환합니다. 그런 다음 이 표현들이 서로 매칭됩니다. 손실 함수는 한 쌍(예: I와 T)에 해당하는 벡터 간의 코사인 유사성을 최대화하고, 다른 모든 쌍 간의 코사인 유사성을 최소화하도록 정의됩니다. 이것이 이 접근 방식이 **대조적**이라고 불리는 이유입니다.

CLIP 모델/라이브러리는 [OpenAI GitHub](https://github.com/openai/CLIP)에서 사용할 수 있습니다. 이 접근 방식은 [이 블로그 게시물](https://openai.com/blog/clip/)에 설명되어 있으며, [이 논문](https://arxiv.org/pdf/2103.00020.pdf)에서 더 자세히 설명됩니다.

이 모델이 사전 훈련되면 이미지 배치와 텍스트 프롬프트 배치를 제공하면 확률이 포함된 텐서를 반환합니다. CLIP은 여러 작업에 사용될 수 있습니다:

**이미지 분류**

예를 들어, 고양이, 개, 사람으로 이미지를 분류해야 한다고 가정해 보겠습니다. 이 경우 모델에 이미지를 제공하고 일련의 텍스트 프롬프트: "*고양이 사진*", "*개 사진*", "*사람 사진*"을 제공할 수 있습니다. 결과 벡터의 3개의 확률 중에서 가장 높은 값을 가진 인덱스를 선택하면 됩니다.

![이미지 분류를 위한 CLIP](../../../../../translated_images/clip-class.3af42ef0b2b19369a633df5f20ddf4f5a01d6c8ffa181e9d3a0572c19f919f72.ko.png)

> *[이 블로그 게시물](https://openai.com/blog/clip/)의 사진*

**텍스트 기반 이미지 검색**

반대로 할 수도 있습니다. 이미지 컬렉션이 있는 경우 이 컬렉션을 모델에 전달하고 텍스트 프롬프트를 제공하면 주어진 프롬프트와 가장 유사한 이미지를 얻을 수 있습니다.

## ✍️ 예제: [CLIP을 이용한 이미지 분류 및 이미지 검색](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

[Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb) 노트북을 열어 CLIP이 작동하는 모습을 확인하세요.

## VQGAN+ CLIP을 이용한 이미지 생성

CLIP은 텍스트 프롬프트에서 **이미지 생성**에도 사용할 수 있습니다. 이를 위해서는 일부 벡터 입력을 기반으로 이미지를 생성할 수 있는 **생성기 모델**이 필요합니다. 이러한 모델 중 하나는 [VQGAN](https://compvis.github.io/taming-transformers/) (벡터 양자화 GAN)이라고 합니다.

VQGAN을 일반 [GAN](../../4-ComputerVision/10-GANs/README.md)과 구별하는 주요 아이디어는 다음과 같습니다:
* 이미지 구성에 필요한 맥락이 풍부한 시각적 부분의 시퀀스를 생성하기 위해 자기 회귀 트랜스포머 아키텍처를 사용합니다. 이러한 시각적 부분은 [CNN](../../4-ComputerVision/07-ConvNets/README.md)에 의해 학습됩니다.
* 이미지의 일부가 "진짜"인지 "가짜"인지 감지하는 서브 이미지 판별기를 사용합니다 (전통적인 GAN의 "모두 또는 아무것도" 접근 방식과는 다릅니다).

VQGAN에 대해 더 알아보려면 [Taming Transformers](https://compvis.github.io/taming-transformers/) 웹사이트를 방문하세요.

VQGAN과 전통적인 GAN의 중요한 차이점 중 하나는 후자가 임의의 입력 벡터에서 괜찮은 이미지를 생성할 수 있는 반면, VQGAN은 일관되지 않은 이미지를 생성할 가능성이 높다는 것입니다. 따라서 이미지 생성 프로세스를 추가로 안내해야 하며, 이는 CLIP을 사용하여 수행할 수 있습니다.

![VQGAN+CLIP 아키텍처](../../../../../translated_images/vqgan.5027fe05051dfa3101950cfa930303f66e6478b9bd273e83766731796e462d9b.ko.png)

텍스트 프롬프트에 해당하는 이미지를 생성하기 위해, 우리는 무작위 인코딩 벡터로 시작하여 VQGAN을 통해 이미지를 생성합니다. 그런 다음 CLIP을 사용하여 이미지가 텍스트 프롬프트와 얼마나 잘 일치하는지를 나타내는 손실 함수를 생성합니다. 목표는 이 손실을 최소화하고, 역전파를 사용하여 입력 벡터 매개변수를 조정하는 것입니다.

VQGAN+CLIP을 구현한 훌륭한 라이브러리는 [Pixray](http://github.com/pixray/pixray)입니다.

![Pixray로 생성된 사진](../../../../../translated_images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.2384968e9db8a0d09dc96de938b9f95bde8a7e1c721f48f286a7795bf16d56c7.ko.png) |  ![Pixray로 생성된 사진](../../../../../translated_images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.e0b6495f210a439077e1c32cc8afdf714e634fe24dc78dc5aa45fd2f560b0ed5.ko.png) | ![Pixray로 생성된 사진](../../../../../translated_images/a_closeup_oil_portrait_of_old_male_teacher_of_math.5362e67aa7fc2683b9d36a613b364deb7454760cd39205623fc1e3938fa133c0.ko.png)
----|----|----
*문학 교사의 젊은 남성의 수채화 초상화*라는 프롬프트로 생성된 사진 | *컴퓨터 과학 교사의 젊은 여성의 유화 초상화*라는 프롬프트로 생성된 사진 | *수학 교사의 노인 남성의 유화 초상화*라는 프롬프트로 생성된 사진

> **인공지능 교사** 컬렉션의 사진, [Dmitry Soshnikov](http://soshnikov.com) 제공

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
DALL-E는 프롬프트에서 이미지를 생성하도록 훈련된 GPT-3의 버전입니다. 120억 개의 매개변수로 훈련되었습니다.

CLIP과 달리 DALL-E는 텍스트와 이미지를 이미지와 텍스트 모두에 대한 단일 토큰 스트림으로 수신합니다. 따라서 여러 프롬프트에서 텍스트를 기반으로 이미지를 생성할 수 있습니다.

### [DALL-E 2](https://openai.com/dall-e-2)
DALL-E 1과 2의 주요 차이점은 더 현실적인 이미지와 예술을 생성한다는 것입니다.

DALL-E로 생성된 이미지 예시:
![Pixray로 생성된 사진](../../../../../translated_images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.6c235e8271d9ed10ce985d86aeb241a58518958647973af136912116b9518fce.ko.png) |  ![Pixray로 생성된 사진](../../../../../translated_images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.f21dc4166340b6c8b4d1cb57efd1e22127407f9b28c9ac7afe11344065369e64.ko.png) | ![Pixray로 생성된 사진](../../../../../translated_images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.d331c2dfbdc3f7c46aa65c0809066f5e7ed4b49609cd259852e760df21051e4a.ko.png)
----|----|----
*문학 교사의 젊은 남성의 수채화 초상화*라는 프롬프트로 생성된 사진 | *컴퓨터 과학 교사의 젊은 여성의 유화 초상화*라는 프롬프트로 생성된 사진 | *수학 교사의 노인 남성의 유화 초상화*라는 프롬프트로 생성된 사진

## 참고 문헌

* VQGAN 논문: [고해상도 이미지 합성을 위한 트랜스포머 조련](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* CLIP 논문: [자연어 감독에서 전이 가능한 시각 모델 학습](https://arxiv.org/pdf/2103.00020.pdf)

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 있을 수 있습니다. 원본 문서는 해당 언어로 된 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 우리는 책임을 지지 않습니다.