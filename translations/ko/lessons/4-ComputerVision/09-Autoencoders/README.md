<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-24T21:27:54+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "ko"
}
-->
# 오토인코더

CNN(합성곱 신경망)을 훈련할 때, 문제 중 하나는 많은 양의 라벨링된 데이터가 필요하다는 점입니다. 이미지 분류의 경우, 이미지를 서로 다른 클래스에 나누는 작업이 필요하며, 이는 수작업으로 이루어집니다.

## [강의 전 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/109)

하지만, CNN 특징 추출기를 훈련하기 위해 라벨이 없는 원시 데이터(비라벨링 데이터)를 사용하고 싶을 수도 있습니다. 이를 **자기 지도 학습(self-supervised learning)**이라고 합니다. 라벨 대신, 훈련 이미지를 네트워크의 입력과 출력으로 사용합니다. **오토인코더(autoencoder)**의 주요 아이디어는 입력 이미지를 **잠재 공간(latent space)**으로 변환하는 **인코더 네트워크**와, 원본 이미지를 재구성하는 것을 목표로 하는 **디코더 네트워크**를 사용하는 것입니다.

> ✅ [오토인코더](https://wikipedia.org/wiki/Autoencoder)는 "라벨이 없는 데이터의 효율적인 코딩을 학습하기 위해 사용되는 인공 신경망의 한 유형"입니다.

오토인코더를 훈련할 때, 네트워크는 원본 이미지를 가능한 한 정확하게 재구성하기 위해 입력 이미지의 최적의 **임베딩(embedding)**을 찾으려고 합니다.

![AutoEncoder Diagram](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.ko.jpg)

> 이미지 출처: [Keras 블로그](https://blog.keras.io/building-autoencoders-in-keras.html)

## 오토인코더 사용 시나리오

원본 이미지를 재구성하는 것이 그 자체로는 유용하지 않아 보일 수 있지만, 오토인코더가 특히 유용한 몇 가지 시나리오가 있습니다:

* **이미지 차원 축소를 통한 시각화** 또는 **이미지 임베딩 훈련**. 오토인코더는 이미지의 공간적 특성과 계층적 특징을 고려하기 때문에, 일반적으로 PCA보다 더 나은 결과를 제공합니다.
* **노이즈 제거(denoising)**, 즉 이미지에서 노이즈를 제거하는 작업. 노이즈는 쓸모없는 정보를 많이 포함하고 있기 때문에, 오토인코더는 상대적으로 작은 잠재 공간에 이를 모두 담을 수 없으며, 따라서 이미지의 중요한 부분만 캡처합니다. 노이즈 제거기를 훈련할 때는 원본 이미지를 사용하고, 인위적으로 노이즈를 추가한 이미지를 오토인코더의 입력으로 사용합니다.
* **초해상도(super-resolution)**, 즉 이미지 해상도를 높이는 작업. 고해상도 이미지를 시작점으로 사용하고, 저해상도 이미지를 오토인코더 입력으로 사용합니다.
* **생성 모델(generative models)**. 오토인코더를 훈련한 후, 디코더 부분을 사용하여 무작위 잠재 벡터에서 새로운 객체를 생성할 수 있습니다.

## 변분 오토인코더(VAE)

전통적인 오토인코더는 입력 데이터를 어떤 방식으로든 차원을 축소하여 입력 이미지의 중요한 특징을 파악합니다. 하지만, 잠재 벡터는 종종 직관적으로 이해하기 어렵습니다. 예를 들어, MNIST 데이터셋을 사용한다고 가정했을 때, 서로 다른 잠재 벡터가 어떤 숫자에 해당하는지 파악하는 것은 쉽지 않습니다. 이는 가까운 잠재 벡터가 반드시 동일한 숫자에 해당하지 않기 때문입니다.

반면, *생성* 모델을 훈련하려면 잠재 공간에 대한 이해가 있는 것이 더 좋습니다. 이러한 아이디어는 **변분 오토인코더(Variational Auto-Encoder, VAE)**로 이어집니다.

VAE는 잠재 매개변수의 *통계적 분포*를 예측하도록 학습하는 오토인코더입니다. 이를 **잠재 분포(latent distribution)**라고 합니다. 예를 들어, 잠재 벡터가 평균 z<sub>mean</sub>과 표준편차 z<sub>sigma</sub>를 가진 정규 분포를 따르도록 하고 싶을 수 있습니다(평균과 표준편차는 모두 특정 차원의 벡터입니다). VAE의 인코더는 이러한 매개변수를 예측하도록 학습하며, 디코더는 이 분포에서 무작위 벡터를 가져와 객체를 재구성합니다.

요약하자면:

* 입력 벡터에서 `z_mean`과 `z_log_sigma`를 예측합니다(표준편차 자체 대신, 표준편차의 로그를 예측합니다).
* 분포 N(z<sub>mean</sub>,exp(z<sub>log_sigma</sub>))에서 `sample` 벡터를 샘플링합니다.
* 디코더는 `sample`을 입력 벡터로 사용하여 원본 이미지를 디코딩하려고 시도합니다.

<img src="images/vae.png" width="50%">

> 이미지 출처: [Isaak Dykeman의 블로그 글](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

변분 오토인코더는 두 가지 부분으로 구성된 복잡한 손실 함수를 사용합니다:

* **재구성 손실(Reconstruction loss)**: 재구성된 이미지가 목표 이미지와 얼마나 가까운지를 나타내는 손실 함수입니다(평균 제곱 오차, MSE 등을 사용할 수 있습니다). 이는 일반 오토인코더에서 사용하는 손실 함수와 동일합니다.
* **KL 손실(KL loss)**: 잠재 변수 분포가 정규 분포에 가깝게 유지되도록 보장합니다. 이는 [쿨백-라이블러 발산(Kullback-Leibler divergence)](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained)이라는 개념에 기반하며, 두 통계적 분포가 얼마나 유사한지를 측정하는 지표입니다.

VAE의 중요한 장점 중 하나는 잠재 벡터를 샘플링할 분포를 알고 있기 때문에 새로운 이미지를 비교적 쉽게 생성할 수 있다는 점입니다. 예를 들어, MNIST 데이터셋에서 2D 잠재 벡터를 사용하여 VAE를 훈련하면, 잠재 벡터의 구성 요소를 변화시켜 서로 다른 숫자를 생성할 수 있습니다:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> 이미지 출처: [Dmitry Soshnikov](http://soshnikov.com)

잠재 매개변수 공간의 다른 부분에서 잠재 벡터를 가져오면서 이미지가 서로 어떻게 섞이는지 관찰할 수 있습니다. 또한, 이 공간을 2D로 시각화할 수도 있습니다:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> 이미지 출처: [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ 연습: 오토인코더

다음 노트북에서 오토인코더에 대해 더 알아보세요:

* [TensorFlow를 사용한 오토인코더](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [PyTorch를 사용한 오토인코더](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## 오토인코더의 특성

* **데이터 특화** - 훈련된 이미지 유형에만 잘 작동합니다. 예를 들어, 꽃에 대해 초해상도 네트워크를 훈련하면, 초상화에는 잘 작동하지 않습니다. 이는 네트워크가 훈련 데이터셋에서 학습한 세부 특징을 사용하여 고해상도 이미지를 생성하기 때문입니다.
* **손실 발생** - 재구성된 이미지는 원본 이미지와 동일하지 않습니다. 손실의 성격은 훈련 중 사용된 *손실 함수*에 의해 정의됩니다.
* **비라벨링 데이터**에서 작동

## [강의 후 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/209)

## 결론

이 강의에서는 AI 연구자가 사용할 수 있는 다양한 유형의 오토인코더에 대해 배웠습니다. 오토인코더를 구축하고 이미지를 재구성하는 방법을 배웠으며, VAE를 사용하여 새로운 이미지를 생성하는 방법도 배웠습니다.

## 🚀 도전 과제

이 강의에서는 이미지에 오토인코더를 사용하는 방법을 배웠습니다. 하지만 오토인코더는 음악에도 사용할 수 있습니다! Magenta 프로젝트의 [MusicVAE](https://magenta.tensorflow.org/music-vae)를 확인해보세요. 이 프로젝트는 오토인코더를 사용하여 음악을 재구성하는 방법을 학습합니다. 이 라이브러리를 사용하여 [실험](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb)을 진행하며 무엇을 만들 수 있는지 확인해보세요.

## [강의 후 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## 복습 및 자기 학습

참고로, 다음 자료에서 오토인코더에 대해 더 읽어보세요:

* [Keras로 오토인코더 구축하기](https://blog.keras.io/building-autoencoders-in-keras.html)
* [NeuroHive 블로그 글](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [변분 오토인코더 설명](https://kvfrans.com/variational-autoencoders-explained/)
* [조건부 변분 오토인코더](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## 과제

[TensorFlow를 사용하는 이 노트북](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)의 끝부분에 '과제'가 있습니다. 이를 과제로 사용하세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.