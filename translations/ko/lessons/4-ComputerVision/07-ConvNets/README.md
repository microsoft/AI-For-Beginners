<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a560d5b845962cf33dc102266e409568",
  "translation_date": "2025-09-23T13:17:54+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/README.md",
  "language_code": "ko"
}
-->
# 컨볼루션 신경망

이전에 신경망이 이미지를 처리하는 데 매우 효과적이며, 단일 계층 퍼셉트론조차도 MNIST 데이터셋의 손글씨 숫자를 합리적인 정확도로 인식할 수 있다는 것을 살펴보았습니다. 하지만 MNIST 데이터셋은 매우 특별하며, 모든 숫자가 이미지 중앙에 위치해 있어 작업이 더 간단해집니다.

## [강의 전 퀴즈](https://ff-quizzes.netlify.app/en/ai/quiz/13)

실제 상황에서는 이미지 내에서 객체의 정확한 위치와 상관없이 객체를 인식할 수 있어야 합니다. 컴퓨터 비전은 일반적인 분류와는 다릅니다. 특정 객체를 이미지에서 찾으려 할 때, 우리는 특정 **패턴**과 그 조합을 찾기 위해 이미지를 스캔합니다. 예를 들어, 고양이를 찾으려 할 때, 먼저 수평선을 찾아 수염을 형성할 수 있고, 그런 다음 수염의 특정 조합이 실제로 고양이의 이미지임을 알려줄 수 있습니다. 특정 패턴의 상대적 위치와 존재는 중요하지만, 이미지에서의 정확한 위치는 중요하지 않습니다.

패턴을 추출하기 위해 **컨볼루션 필터**라는 개념을 사용할 것입니다. 이미지는 2D-매트릭스 또는 색상 깊이를 가진 3D-텐서로 표현됩니다. 필터를 적용한다는 것은 비교적 작은 **필터 커널** 매트릭스를 가져와 원본 이미지의 각 픽셀에 대해 이웃한 점들과 가중 평균을 계산하는 것을 의미합니다. 이를 작은 창이 전체 이미지를 슬라이딩하며 필터 커널 매트릭스의 가중치에 따라 모든 픽셀을 평균화하는 것으로 볼 수 있습니다.

![수직 엣지 필터](../../../../../translated_images/filter-vert.b7148390ca0bc356ddc7e55555d2481819c1e86ddde9dce4db5e71a69d6f887f.ko.png) | ![수평 엣지 필터](../../../../../translated_images/filter-horiz.59b80ed4feb946efbe201a7fe3ca95abb3364e266e6fd90820cb893b4d3a6dda.ko.png)
----|----

> 이미지 제공: Dmitry Soshnikov

예를 들어, MNIST 숫자에 3x3 수직 엣지 및 수평 엣지 필터를 적용하면 원본 이미지에서 수직 및 수평 엣지가 있는 부분을 강조 표시(예: 높은 값)할 수 있습니다. 따라서 이 두 필터는 엣지를 "찾는" 데 사용할 수 있습니다. 마찬가지로, 다른 저수준 패턴을 찾기 위해 다양한 필터를 설계할 수 있습니다:

<img src="images/lmfilters.jpg" width="500" align="center"/>

> 이미지 출처: [Leung-Malik 필터 뱅크](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

하지만 패턴을 추출하기 위해 필터를 수동으로 설계할 수도 있지만, 네트워크를 설계하여 패턴을 자동으로 학습하도록 할 수도 있습니다. 이것이 CNN의 주요 아이디어 중 하나입니다.

## CNN의 주요 아이디어

CNN이 작동하는 방식은 다음과 같은 중요한 아이디어를 기반으로 합니다:

* 컨볼루션 필터는 패턴을 추출할 수 있다.
* 필터가 자동으로 학습되도록 네트워크를 설계할 수 있다.
* 원본 이미지뿐만 아니라 고수준 특징에서도 패턴을 찾는 데 동일한 접근 방식을 사용할 수 있다. 따라서 CNN 특징 추출은 저수준 픽셀 조합에서 시작하여 이미지 부분의 고수준 조합까지 특징의 계층 구조에서 작동한다.

![계층적 특징 추출](../../../../../translated_images/FeatureExtractionCNN.d9b456cbdae7cb643fde3032b81b2940e3cf8be842e29afac3f482725ba7f95c.ko.png)

> 이미지 출처: [Hislop-Lynch의 논문](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), [그들의 연구](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)를 기반으로 함

## ✍️ 연습: 컨볼루션 신경망

컨볼루션 신경망이 어떻게 작동하는지, 그리고 학습 가능한 필터를 어떻게 구현할 수 있는지 탐구하기 위해 관련 노트북을 통해 학습을 계속 진행해 봅시다:

* [컨볼루션 신경망 - PyTorch](ConvNetsPyTorch.ipynb)
* [컨볼루션 신경망 - TensorFlow](ConvNetsTF.ipynb)

## 피라미드 아키텍처

이미지 처리를 위해 사용되는 대부분의 CNN은 소위 피라미드 아키텍처를 따릅니다. 원본 이미지에 적용되는 첫 번째 컨볼루션 계층은 일반적으로 상대적으로 적은 수의 필터(8-16)를 가지며, 이는 수평/수직 선이나 획과 같은 다양한 픽셀 조합에 해당합니다. 다음 단계에서는 네트워크의 공간적 차원을 줄이고 필터 수를 늘리며, 이는 간단한 특징의 더 많은 조합에 해당합니다. 각 계층에서 최종 분류기로 이동할수록 이미지의 공간적 차원은 감소하고 필터 수는 증가합니다.

예를 들어, 2014년 ImageNet의 상위 5개 분류에서 92.7%의 정확도를 달성한 VGG-16 네트워크의 아키텍처를 살펴봅시다:

![ImageNet 계층](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.ko.jpg)

![ImageNet 피라미드](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.ko.jpg)

> 이미지 출처: [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## 잘 알려진 CNN 아키텍처

[잘 알려진 CNN 아키텍처에 대해 계속 학습하세요](CNN_Architectures.md)

---

