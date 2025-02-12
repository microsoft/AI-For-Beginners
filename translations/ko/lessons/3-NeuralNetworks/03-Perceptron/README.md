# 신경망 소개: 퍼셉트론

## [강의 전 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

현대 신경망과 유사한 것을 구현하려는 첫 번째 시도 중 하나는 1957년 코넬 항공 연구소의 프랭크 로젠블라트에 의해 이루어졌습니다. 이는 삼각형, 사각형 및 원과 같은 원시 기하학적 도형을 인식하도록 설계된 "Mark-1"이라는 하드웨어 구현이었습니다.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='프랭크 로젠블라트'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='Mark 1 퍼셉트론' />|

> 이미지 [출처: 위키백과](https://en.wikipedia.org/wiki/Perceptron)

입력 이미지는 20x20 포토셀 배열로 표현되었으며, 따라서 신경망은 400개의 입력과 하나의 이진 출력을 가졌습니다. 간단한 네트워크는 하나의 뉴런, 즉 **임계값 논리 장치**로 구성되었습니다. 신경망의 가중치는 훈련 단계에서 수동 조정이 필요한 전위차계처럼 작용했습니다.

> ✅ 전위차계는 사용자가 회로의 저항을 조정할 수 있게 해주는 장치입니다.

> 뉴욕 타임즈는 그 당시 퍼셉트론에 대해 다음과 같이 썼습니다: *[해군]이 기대하는 전자 컴퓨터의 배아로, 스스로 걷고, 말하고, 보고, 쓰고, 재생산하며, 자신의 존재를 인식할 수 있을 것으로 보인다.*

## 퍼셉트론 모델

모델에 N개의 특성이 있다고 가정할 경우, 입력 벡터는 크기 N의 벡터가 됩니다. 퍼셉트론은 **이진 분류** 모델로, 즉 두 클래스의 입력 데이터를 구분할 수 있습니다. 각 입력 벡터 x에 대해 퍼셉트론의 출력은 클래스에 따라 +1 또는 -1이 될 것이라고 가정합니다. 출력은 다음 공식을 사용하여 계산됩니다:

y(x) = f(w<sup>T</sup>x)

여기서 f는 단계 활성화 함수입니다.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## 퍼셉트론 훈련

퍼셉트론을 훈련시키기 위해서는 대부분의 값을 올바르게 분류하는 가중치 벡터 w를 찾아야 합니다. 즉, 가장 작은 **오류**를 결과로 만들어야 합니다. 이 오류 E는 다음과 같은 방식으로 **퍼셉트론 기준**에 의해 정의됩니다:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

여기서:

* 잘못된 분류를 초래하는 훈련 데이터 포인트 i에 대해 합산합니다.
* x<sub>i</sub>는 입력 데이터이고, t<sub>i</sub>는 각각 음성과 양성 예제에 대해 -1 또는 +1입니다.

이 기준은 가중치 w의 함수로 간주되며, 이를 최소화해야 합니다. 종종 **경량 하강법**이라는 방법이 사용되며, 여기서 우리는 일부 초기 가중치 w<sup>(0)</sup>로 시작하고, 각 단계에서 다음 공식을 따라 가중치를 업데이트합니다:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

여기서 η는 이른바 **학습률**이며, ∇E(w)는 E의 **기울기**를 나타냅니다. 기울기를 계산한 후에는 다음과 같은 결과를 얻습니다:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Python에서 알고리즘은 다음과 같습니다:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## 결론

이번 수업에서는 이진 분류 모델인 퍼셉트론에 대해 배우고, 가중치 벡터를 사용하여 이를 훈련시키는 방법을 배웠습니다.

## 🚀 도전 과제

자신만의 퍼셉트론을 만들어 보고 싶다면, [Microsoft Learn의 이 실습](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste)을 시도해 보세요. 이 실습은 [Azure ML 디자이너](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste)를 사용합니다.

## [강의 후 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## 복습 및 자기 학습

퍼셉트론을 사용하여 장난감 문제와 실제 문제를 해결하는 방법을 보려면, [퍼셉트론](../../../../../lessons/3-NeuralNetworks/03-Perceptron/Perceptron.ipynb) 노트북으로 가서 계속 학습하세요.

퍼셉트론에 대한 흥미로운 [기사](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590)도 있습니다.

## [과제](lab/README.md)

이번 수업에서는 이진 분류 작업을 위한 퍼셉트론을 구현하고, 이를 사용하여 두 개의 손글씨 숫자를 분류했습니다. 이 실습에서는 주어진 이미지에 가장 적합한 숫자가 무엇인지 완전히 해결하는 문제를 해결해야 합니다.

* [지침](lab/README.md)
* [노트북](../../../../../lessons/3-NeuralNetworks/03-Perceptron/lab/PerceptronMultiClass.ipynb)

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 된 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 우리는 책임을 지지 않습니다.