<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5abc5f7978919be90cd313f0c20e8228",
  "translation_date": "2025-09-07T14:29:47+00:00",
  "source_file": "lessons/3-NeuralNetworks/README.md",
  "language_code": "ko"
}
-->
# 신경망 소개

![신경망 소개 내용 요약 그림](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.ko.png)

소개에서 논의했듯이, 지능을 구현하는 방법 중 하나는 **컴퓨터 모델** 또는 **인공 두뇌**를 훈련시키는 것입니다. 20세기 중반부터 연구자들은 다양한 수학적 모델을 시도했으며, 최근 몇 년 동안 이 방향이 매우 성공적임이 입증되었습니다. 이러한 두뇌의 수학적 모델을 **신경망**이라고 합니다.

> 때때로 신경망은 *인공 신경망* 또는 ANNs라고 불리며, 이는 실제 뉴런 네트워크가 아닌 모델을 의미합니다.

## 머신 러닝

신경망은 **머신 러닝**이라는 더 큰 학문 분야의 일부로, 데이터로 컴퓨터 모델을 훈련시켜 문제를 해결하는 것을 목표로 합니다. 머신 러닝은 인공지능의 큰 부분을 차지하지만, 이 커리큘럼에서는 고전적인 머신 러닝을 다루지 않습니다.

> 고전적인 머신 러닝에 대해 더 배우고 싶다면 별도의 **[Machine Learning for Beginners](http://github.com/microsoft/ml-for-beginners)** 커리큘럼을 방문하세요.

머신 러닝에서는 예제 데이터셋 **X**와 이에 대응하는 출력 값 **Y**가 있다고 가정합니다. 예제는 종종 **특징**으로 구성된 N차원 벡터이며, 출력은 **레이블**이라고 합니다.

우리는 가장 일반적인 두 가지 머신 러닝 문제를 고려할 것입니다:

* **분류**: 입력 객체를 두 개 이상의 클래스 중 하나로 분류해야 하는 경우.
* **회귀**: 각 입력 샘플에 대해 숫자를 예측해야 하는 경우.

> 입력과 출력을 텐서로 표현할 때, 입력 데이터셋은 M×N 크기의 행렬이며, 여기서 M은 샘플 수, N은 특징 수입니다. 출력 레이블 **Y**는 크기가 M인 벡터입니다.

이 커리큘럼에서는 신경망 모델에만 집중할 것입니다.

## 뉴런 모델

생물학적으로 우리의 뇌는 여러 "입력"(축삭)과 하나의 출력(수상돌기)을 가진 신경 세포로 구성되어 있다는 것을 알고 있습니다. 축삭과 수상돌기는 전기 신호를 전달할 수 있으며, 축삭과 수상돌기 사이의 연결은 다양한 전도성을 나타낼 수 있습니다(신경전달물질에 의해 제어됨).

![뉴런 모델](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.ko.jpg) | ![뉴런 모델](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.ko.png)
----|----
실제 뉴런 *([이미지](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) 출처: Wikipedia)* | 인공 뉴런 *(저자 제공 이미지)*

따라서 뉴런의 가장 간단한 수학적 모델은 여러 입력 X<sub>1</sub>, ..., X<sub>N</sub>과 출력 Y, 그리고 일련의 가중치 W<sub>1</sub>, ..., W<sub>N</sub>을 포함합니다. 출력은 다음과 같이 계산됩니다:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

여기서 f는 비선형 **활성화 함수**입니다.

> 초기 뉴런 모델은 Warren McCullock과 Walter Pitts가 1943년에 발표한 고전 논문 [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf)에서 설명되었습니다. Donald Hebb는 그의 책 "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)"에서 이러한 네트워크를 훈련시키는 방법을 제안했습니다.

## 이 섹션에서

이 섹션에서는 다음을 배울 것입니다:
* [퍼셉트론](03-Perceptron/README.md): 두 클래스 분류를 위한 초기 신경망 모델 중 하나
* [다층 네트워크](04-OwnFramework/README.md): [자체 프레임워크를 구축하는 방법](04-OwnFramework/OwnFramework.ipynb)과 함께 제공되는 노트북
* [신경망 프레임워크](05-Frameworks/README.md): 다음 노트북 포함 [PyTorch](05-Frameworks/IntroPyTorch.ipynb) 및 [Keras/Tensorflow](05-Frameworks/IntroKerasTF.ipynb)
* [오버피팅](../../../../lessons/3-NeuralNetworks/05-Frameworks)

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.