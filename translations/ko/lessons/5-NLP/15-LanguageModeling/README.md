# 언어 모델링

Word2Vec와 GloVe 같은 의미 임베딩은 사실 **언어 모델링**의 첫 단계입니다. 이는 언어의 본질을 *이해*하거나 (*표현*)하는 모델을 만드는 것을 목표로 합니다.

## [강의 전 퀴즈](https://ff-quizzes.netlify.app/en/ai/quiz/29)

언어 모델링의 주요 아이디어는 비지도 학습 방식으로 레이블이 없는 데이터셋을 학습시키는 것입니다. 이는 레이블이 없는 텍스트는 방대한 양이 존재하는 반면, 레이블이 있는 텍스트는 레이블링에 필요한 노력의 한계로 인해 항상 제한적일 수밖에 없기 때문에 중요합니다. 대부분의 경우, 텍스트에서 **누락된 단어를 예측**할 수 있는 언어 모델을 구축할 수 있습니다. 이는 텍스트에서 임의의 단어를 마스킹하여 학습 샘플로 사용하는 것이 쉽기 때문입니다.

## 임베딩 학습

이전 예제에서는 사전 학습된 의미 임베딩을 사용했지만, 이러한 임베딩이 어떻게 학습되는지 살펴보는 것도 흥미롭습니다. 사용할 수 있는 몇 가지 아이디어는 다음과 같습니다:

* **N-그램** 언어 모델링: 이전 N개의 토큰을 보고 다음 토큰을 예측하는 방식 (N-그램)
* **연속적인 단어 묶음** (CBoW): 토큰 시퀀스 $W_{-N}$, ..., $W_N$에서 가운데 토큰 $W_0$을 예측하는 방식
* **스킵그램**: 가운데 토큰 $W_0$에서 주변 토큰 {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$}을 예측하는 방식

![단어를 벡터로 변환하는 알고리즘에 대한 논문 이미지](../../../../../translated_images/ko/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6.webp)

> 이미지 출처: [이 논문](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ 예제 노트북: CBoW 모델 학습

다음 노트북에서 학습을 이어가세요:

* [TensorFlow로 CBoW Word2Vec 학습하기](CBoW-TF.ipynb)
* [PyTorch로 CBoW Word2Vec 학습하기](CBoW-PyTorch.ipynb)

## 결론

이전 강의에서 단어 임베딩이 마치 마법처럼 작동한다는 것을 확인했습니다! 이제 단어 임베딩을 학습시키는 것이 그리 복잡한 작업이 아니라는 것을 알게 되었으며, 필요하다면 특정 도메인 텍스트에 대해 직접 단어 임베딩을 학습시킬 수 있을 것입니다.

## [강의 후 퀴즈](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## 복습 및 자기 학습

* [PyTorch 공식 언어 모델링 튜토리얼](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html)
* [TensorFlow 공식 Word2Vec 모델 학습 튜토리얼](https://www.TensorFlow.org/tutorials/text/word2vec)
* **gensim** 프레임워크를 사용하여 몇 줄의 코드로 가장 일반적으로 사용되는 임베딩을 학습시키는 방법은 [이 문서](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html)에 설명되어 있습니다.

## 🚀 [과제: 스킵그램 모델 학습](lab/README.md)

실습에서는 이번 강의의 코드를 수정하여 CBoW 대신 스킵그램 모델을 학습시키는 도전을 하게 됩니다. [자세히 읽기](lab/README.md)

---

