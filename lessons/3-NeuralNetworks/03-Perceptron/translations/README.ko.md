# 뉴럴 네트워크 소개: Perceptron

## [강의 전 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/103)

현대의 뉴럴 네트워크와 유사한 것을 구현하려는 최초의 시도 중 하나는 1957년 코넬 항공 연구소의 프랭크 로젠블랫에 의해 수행되었습니다. 삼각형, 사각형, 원과 같은 원시적인 기하학적 도형을 인식하기 위해 설계된 "Mark-1"이라는 하드웨어였습니다.

|      |      |
|--------------|-----------|
|<img src='../images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='../images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> 이미지 출처 [위키피디아](https://en.wikipedia.org/wiki/Perceptron)

입력 이미지는 20x20 광전지 배열로 표현되었습니다. 따라서 뉴럴 네트워크에는 400개의 입력과 하나의 이진 출력이 있습니다. 간단한 네트워크에는 **임계값 논리 장치(threshold logic unit)** 라 불리는 하나의 뉴런이 포함되어 있습니다. 뉴럴 네트워크의 가중치들은 훈련 단계에서 수동으로 조정해야 하는 가변 저항(potentiometer)처럼 작동합니다.

> ✅ 가변 저항은 사용자가 회로의 저항을 조정할 수 있는 장치입니다.

> 당시 뉴욕 타임즈는 Perceptron에 대해 다음과 같이 썼습니다: *해군이 기대하는 전자 컴퓨터의 배아는 걷고, 말하고, 보고, 쓰고, 번식하고, 자신의 존재를 자각할 수 있을 것입니다.*

## Perceptron 모델

모델에 N개의 특징이 있다고 가정하고, 이 경우 입력 벡터는 크기 N의 벡터가 됩니다. Perceptron은 **이진 분류** 모델로, 입력 데이터를 두 가지 클래스로 구분할 수 있습니다. 각 입력 벡터 x에 대해 Perceptron의 출력은 클래스에 따라 +1 또는 -1이 될 것이라고 가정합니다. 출력은 아래의 공식을 사용하여 계산됩니다.

y(x) = f(w<sup>T</sup>x)

여기서 f는 계단 활성화 함수(step activation function)입니다.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../images/activation-func.png"/>

## Perceptron 훈련

Perceptron을 훈련하려면 대부분의 값을 올바르게 분류하는, 즉 가장 작은 **오차**를 발생하는 가중치 벡터 w를 찾아야 합니다. 이 오차는 아래와 같은 방식으로 **퍼셉트론 기준(perceptron criterion)** 에 의해 정의됩니다:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

여기서:

* 잘못된 분류가 발생한 훈련 데이터 i지점에서 합계를 구합니다.
* x<sub>i</sub>는 입력 데이터이고, t<sub>i</sub>는 음수인지 양수인지에 따라 -1 또는 +1이 됩니다.

이 기준은 가중치 w에 대한 함수로 생각할 수 있고, 이를 최소화해야 합니다. 간혹, **경사 하강(gradient descent)** 이라는 방법이 사용되는데, 초기 가중치 w(0)로 시작한 다음 각 단계에서 공식에 따라 가중치를 업데이트하는 방식입니다:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

여기서 &eta;는 **학습률(learning rate)** 를 의미하고, &nabla;E(w)는 E의 **기울기(gradient)** 를 나타냅니다. 기울기를 계산한 후에는 아래와 같이 마무리됩니다.

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Python의 알고리즘은 다음과 같습니다.:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # 가중치 초기화 (거의 무작위로)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # perceptron 출력 계산
        if z < 0: # negative로 분류된 positive
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # positive로 분류된 negative
            weights = weights - eta*weights.shape

    return weights
```

## 결론

이번 강의에서는 이진 분류 모델인 Perceptron과 가중치 벡터를 사용해서 Perceptron을 훈련하는 방법에 대해서 배웠습니다.

## 🚀 도전 과제

자신만의 Perceptron을 구축해보고 싶다면, [Azure ML designer](https://docs.microsoft.com/ko-kr/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste)를 사용하는 [Microsoft Learn](https://docs.microsoft.com/ko-kr/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste)에서 이 실습을 해보시기 바랍니다.

## [강의 후 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/203)

## 복습 및 자가 학습

Perceptron을 사용하여 간단한 문제뿐만 아니라 실제 문제를 해결하고, 학습을 계속할 진행하려면 [Perceptron Notebook](../Perceptron.ipynb)으로 이동하시 바랍니다.

여기 Perceptron에 대한 [흥미로운 기사](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590)도 있습니다.

## [과제](../lab/README.md)

이번 강의에서, 이진 분류 작업을 위한 퍼셉트론을 구현하고 이를 이용해 두 개의 손으로 쓴 숫자를 분류해 보았습니다. 실습에서는 숫자 분류 문제를 완전히 해결해야 합니다. 즉, 주어진 이미지에 가장 일치할 가능성이 높은 숫자를 결정해야 합니다.

* [설명](../lab/README.md)
* [Notebook](../lab/PerceptronMultiClass.ipynb)
