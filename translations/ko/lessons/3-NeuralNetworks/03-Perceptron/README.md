# 신경망 소개: 퍼셉트론

## [강의 전 퀴즈](https://ff-quizzes.netlify.app/en/ai/quiz/5)

현대 신경망과 유사한 것을 구현하려는 최초의 시도 중 하나는 1957년 Cornell Aeronautical Laboratory의 Frank Rosenblatt에 의해 이루어졌습니다. 이는 "Mark-1"이라는 하드웨어 구현으로, 삼각형, 사각형, 원과 같은 기본적인 기하학적 도형을 인식하도록 설계되었습니다.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/ko/Rosenblatt-wikipedia.294821b285ac796d.webp' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/ko/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9.webp' alt='The Mark 1 Perceptron' />|

> 이미지 출처: [Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

입력 이미지는 20x20 포토셀 배열로 표현되었으며, 신경망은 400개의 입력과 하나의 이진 출력으로 구성되었습니다. 간단한 네트워크는 하나의 뉴런, 즉 **임계값 논리 유닛**으로 구성되었습니다. 신경망 가중치는 훈련 단계에서 수동으로 조정해야 하는 가변저항기처럼 작동했습니다.

> ✅ 가변저항기는 회로의 저항을 사용자가 조정할 수 있도록 하는 장치입니다.

> 당시 뉴욕 타임즈는 퍼셉트론에 대해 이렇게 썼습니다: *[해군이] 걷고, 말하고, 보고, 쓰고, 스스로를 복제하며 자신의 존재를 인식할 수 있을 것으로 기대하는 전자 컴퓨터의 배아.*

## 퍼셉트론 모델

우리 모델에 N개의 특징이 있다고 가정해 봅시다. 이 경우 입력 벡터는 크기가 N인 벡터가 됩니다. 퍼셉트론은 **이진 분류** 모델로, 입력 데이터의 두 클래스를 구분할 수 있습니다. 각 입력 벡터 x에 대해 퍼셉트론의 출력은 클래스에 따라 +1 또는 -1이 됩니다. 출력은 다음 공식을 사용하여 계산됩니다:

y(x) = f(w<sup>T</sup>x)

여기서 f는 계단 활성화 함수입니다.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/ko/activation-func.b4924007c7ce7764.webp"/>

## 퍼셉트론 훈련

퍼셉트론을 훈련시키기 위해서는 대부분의 값을 올바르게 분류하는 가중치 벡터 w를 찾아야 합니다. 즉, **오류**를 최소화해야 합니다. 이 오류 E는 **퍼셉트론 기준**에 따라 다음과 같이 정의됩니다:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

여기서:

* 합은 잘못된 분류를 초래하는 훈련 데이터 포인트 i에 대해 계산됩니다.
* x<sub>i</sub>는 입력 데이터이고, t<sub>i</sub>는 각각 음수와 양수 예제에 대해 -1 또는 +1입니다.

이 기준은 가중치 w의 함수로 간주되며, 이를 최소화해야 합니다. 종종 **경사 하강법**이라는 방법이 사용되며, 초기 가중치 w<sup>(0)</sup>에서 시작하여 각 단계에서 다음 공식을 사용하여 가중치를 업데이트합니다:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

여기서 &eta;는 **학습률**이고, &nabla;E(w)는 E의 **기울기**를 나타냅니다. 기울기를 계산한 후에는 다음과 같은 결과를 얻습니다:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Python에서의 알고리즘은 다음과 같습니다:

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

이번 강의에서는 이진 분류 모델인 퍼셉트론과 가중치 벡터를 사용하여 이를 훈련시키는 방법에 대해 배웠습니다.

## 🚀 도전 과제

직접 퍼셉트론을 만들어 보고 싶다면 [Microsoft Learn의 실습](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste)을 시도해 보세요. 이 실습에서는 [Azure ML 디자이너](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste)를 사용합니다.

## [강의 후 퀴즈](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## 복습 및 자기 학습

퍼셉트론을 사용하여 간단한 문제와 실제 문제를 해결하는 방법을 확인하고 계속 학습하려면 [Perceptron](Perceptron.ipynb) 노트북을 참조하세요.

퍼셉트론에 대한 흥미로운 [기사](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590)도 있습니다.

## [과제](lab/README.md)

이번 강의에서는 이진 분류 작업을 위한 퍼셉트론을 구현하고 이를 사용하여 두 개의 손글씨 숫자를 분류했습니다. 이번 실습에서는 숫자 분류 문제를 완전히 해결해야 합니다. 즉, 주어진 이미지에 가장 적합한 숫자를 결정해야 합니다.

* [지침](lab/README.md)
* [노트북](lab/PerceptronMultiClass.ipynb)

---

