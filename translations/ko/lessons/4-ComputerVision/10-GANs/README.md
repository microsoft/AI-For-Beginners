<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-24T21:28:44+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "ko"
}
-->
# 생성적 적대 신경망 (Generative Adversarial Networks)

이전 섹션에서는 **생성 모델**에 대해 배웠습니다. 생성 모델은 학습 데이터셋에 있는 이미지와 유사한 새로운 이미지를 생성할 수 있는 모델입니다. VAE는 생성 모델의 좋은 예시였습니다.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/19)

하지만 VAE를 사용하여 합리적인 해상도의 그림과 같이 정말 의미 있는 것을 생성하려고 하면 학습이 잘 수렴하지 않는다는 것을 알게 됩니다. 이러한 경우에는 생성 모델에 특화된 또 다른 아키텍처인 **생성적 적대 신경망(GAN)**에 대해 배워야 합니다.

GAN의 주요 아이디어는 두 개의 신경망을 서로 경쟁하며 학습시키는 것입니다:

<img src="images/gan_architecture.png" width="70%"/>

> 이미지 출처: [Dmitry Soshnikov](http://soshnikov.com)

> ✅ 간단한 용어 정리:
> * **Generator**: 랜덤 벡터를 입력으로 받아 이미지를 생성하는 네트워크
> * **Discriminator**: 이미지를 입력으로 받아 그것이 학습 데이터셋에서 온 실제 이미지인지, 아니면 Generator가 생성한 이미지인지 판별하는 네트워크. 본질적으로 이미지 분류기입니다.

### Discriminator

Discriminator의 아키텍처는 일반적인 이미지 분류 네트워크와 다르지 않습니다. 가장 간단한 경우에는 완전 연결된 분류기일 수 있지만, 대부분 [컨볼루션 네트워크](../07-ConvNets/README.md)가 사용됩니다.

> ✅ 컨볼루션 네트워크를 기반으로 한 GAN은 [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)이라고 합니다.

CNN 기반 Discriminator는 다음과 같은 레이어로 구성됩니다: 여러 개의 컨볼루션+풀링 레이어(공간 크기 감소)와 "특징 벡터"를 얻기 위한 하나 이상의 완전 연결 레이어, 최종적으로 이진 분류기.

> ✅ 여기서 '풀링'은 이미지 크기를 줄이는 기법입니다. "풀링 레이어는 한 레이어의 뉴런 클러스터 출력값을 다음 레이어의 단일 뉴런으로 결합하여 데이터의 차원을 줄입니다." - [출처](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generator

Generator는 약간 더 복잡합니다. 이를 Discriminator의 반대로 생각할 수 있습니다. 잠재 벡터(특징 벡터 대신)에서 시작하여 필요한 크기/형태로 변환하는 완전 연결 레이어를 거친 후, 디컨볼루션+업스케일링을 수행합니다. 이는 [오토인코더](../09-Autoencoders/README.md)의 *디코더* 부분과 유사합니다.

> ✅ 컨볼루션 레이어가 이미지를 따라 선형 필터로 구현되기 때문에 디컨볼루션은 본질적으로 컨볼루션과 유사하며 동일한 레이어 로직을 사용하여 구현할 수 있습니다.

<img src="images/gan_arch_detail.png" width="70%"/>

> 이미지 출처: [Dmitry Soshnikov](http://soshnikov.com)

### GAN 학습

GAN은 **적대적**이라고 불리는데, 이는 Generator와 Discriminator 간의 지속적인 경쟁이 있기 때문입니다. 이 경쟁 과정에서 Generator와 Discriminator 모두 개선되며, 네트워크는 점점 더 나은 이미지를 생성하는 방법을 학습합니다.

학습은 두 단계로 이루어집니다:

* **Discriminator 학습**: 이 작업은 비교적 간단합니다. Generator가 생성한 이미지 배치를 가져와 이를 0(가짜 이미지)로 레이블링하고, 입력 데이터셋에서 가져온 이미지 배치를 1(실제 이미지)로 레이블링합니다. 그런 다음 *Discriminator 손실*을 계산하고 역전파를 수행합니다.
* **Generator 학습**: 이 작업은 약간 더 까다롭습니다. Generator의 예상 출력값을 직접적으로 알 수 없기 때문입니다. Generator와 Discriminator로 구성된 전체 GAN 네트워크를 사용하여 랜덤 벡터를 입력으로 제공하고 결과가 1(실제 이미지에 해당)이라고 기대합니다. 이 단계에서는 Discriminator의 파라미터를 고정시켜 학습되지 않도록 하고 역전파를 수행합니다.

이 과정에서 Generator와 Discriminator의 손실은 크게 감소하지 않습니다. 이상적인 상황에서는 두 손실이 진동하며 두 네트워크가 성능을 개선하는 것을 나타냅니다.

## ✍️ 연습: GANs

* [TensorFlow/Keras를 사용한 GAN 노트북](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [PyTorch를 사용한 GAN 노트북](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### GAN 학습의 문제점

GAN은 학습이 특히 어려운 것으로 알려져 있습니다. 몇 가지 문제점은 다음과 같습니다:

* **모드 붕괴**: Generator가 Discriminator를 속이는 하나의 성공적인 이미지만 생성하고 다양한 이미지를 생성하지 않는 현상입니다.
* **하이퍼파라미터에 대한 민감성**: GAN이 전혀 수렴하지 않다가 학습률을 갑자기 낮추면 수렴하는 경우가 종종 있습니다.
* Generator와 Discriminator 간의 **균형 유지**: 많은 경우 Discriminator 손실이 상대적으로 빠르게 0으로 떨어지며, 이는 Generator가 더 이상 학습할 수 없게 만듭니다. 이를 극복하기 위해 Generator와 Discriminator에 서로 다른 학습률을 설정하거나 Discriminator 손실이 이미 너무 낮은 경우 Discriminator 학습을 건너뛸 수 있습니다.
* **고해상도 학습**: 오토인코더와 동일한 문제를 반영하며, 너무 많은 컨볼루션 네트워크 레이어를 재구성하면 아티팩트가 발생합니다. 이 문제는 일반적으로 **점진적 성장**을 통해 해결됩니다. 처음에는 저해상도 이미지에서 몇 개의 레이어를 학습한 후 레이어를 "잠금 해제"하거나 추가합니다. 또 다른 해결책은 레이어 간에 추가 연결을 추가하고 여러 해상도를 동시에 학습하는 것입니다. 자세한 내용은 [Multi-Scale Gradient GANs 논문](https://arxiv.org/abs/1903.06048)을 참조하세요.

## 스타일 전이 (Style Transfer)

GAN은 예술적인 이미지를 생성하는 훌륭한 방법입니다. 또 다른 흥미로운 기법은 **스타일 전이**로, 하나의 **콘텐츠 이미지**를 가져와 **스타일 이미지**의 필터를 적용하여 다른 스타일로 다시 그리는 것입니다.

작동 방식은 다음과 같습니다:
* 랜덤 노이즈 이미지(또는 콘텐츠 이미지로 시작할 수 있지만 이해를 위해 랜덤 노이즈로 시작하는 것이 더 쉽습니다)를 시작점으로 사용합니다.
* 목표는 콘텐츠 이미지와 스타일 이미지 모두에 가까운 이미지를 생성하는 것입니다. 이는 두 가지 손실 함수로 결정됩니다:
   - **콘텐츠 손실**: 현재 이미지와 콘텐츠 이미지에서 CNN이 특정 레이어에서 추출한 특징을 기반으로 계산됩니다.
   - **스타일 손실**: 현재 이미지와 스타일 이미지 간의 손실을 Gram 행렬을 사용하여 계산합니다(자세한 내용은 [예제 노트북](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)을 참조하세요).
* 이미지를 더 부드럽게 만들고 노이즈를 제거하기 위해 **변동 손실**을 도입합니다. 이는 인접 픽셀 간 평균 거리를 계산합니다.
* 주요 최적화 루프는 총 손실(세 손실의 가중 합)을 최소화하기 위해 현재 이미지를 조정합니다. 이를 위해 경사 하강법(또는 다른 최적화 알고리즘)을 사용합니다.

## ✍️ 예제: [스타일 전이](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/20)

## 결론

이 강의에서는 GAN과 이를 학습시키는 방법에 대해 배웠습니다. 또한 이 유형의 신경망이 직면할 수 있는 특별한 문제와 이를 극복하기 위한 몇 가지 전략에 대해 배웠습니다.

## 🚀 도전 과제

[스타일 전이 노트북](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)을 실행하여 자신의 이미지를 사용해 보세요.

## 복습 및 자기 학습

GAN에 대해 더 알고 싶다면 다음 자료를 참고하세요:

* Marco Pasini, [1년 동안 GAN을 학습시키며 배운 10가지 교훈](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), 고려할 만한 *사실상 표준* GAN 아키텍처
* [Azure ML에서 GAN을 사용하여 생성적 예술 만들기](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## 과제

이 강의와 관련된 두 개의 노트북 중 하나를 다시 방문하여 자신의 이미지를 사용해 GAN을 재학습시켜 보세요. 무엇을 만들 수 있나요?

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.