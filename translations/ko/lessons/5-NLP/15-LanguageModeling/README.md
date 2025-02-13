# 언어 모델링

Word2Vec 및 GloVe와 같은 의미 임베딩은 사실 **언어 모델링**을 향한 첫 번째 단계로, 언어의 본질을 어느 정도 *이해*하거나 *표현*하는 모델을 만드는 것입니다.

## [강의 전 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

언어 모델링의 주요 아이디어는 비지도 방식으로 레이블이 없는 데이터셋에서 모델을 훈련하는 것입니다. 이는 사용할 수 있는 레이블이 없는 텍스트가 방대하지만, 레이블이 있는 텍스트의 양은 레이블링에 쏟을 수 있는 노력의 양에 항상 제한받기 때문에 중요합니다. 대개 우리는 텍스트에서 **누락된 단어를 예측**할 수 있는 언어 모델을 구축할 수 있습니다. 이는 텍스트에서 임의의 단어를 마스킹하고 이를 훈련 샘플로 사용하는 것이 쉽기 때문입니다.

## 임베딩 훈련

이전 예제에서는 사전 훈련된 의미 임베딩을 사용했지만, 이러한 임베딩이 어떻게 훈련될 수 있는지 보는 것은 흥미롭습니다. 사용할 수 있는 몇 가지 가능한 아이디어가 있습니다:

* **N-그램** 언어 모델링: N개의 이전 토큰을 보고 토큰을 예측하는 방법 (N-그램)
* **연속 단어 가방** (CBoW): 토큰 시퀀스 $W_{-N}$, ..., $W_N$에서 중간 토큰 $W_0$를 예측하는 방법.
* **스킵-그램**: 중간 토큰 $W_0$에서 이웃 토큰 집합 {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$}을 예측하는 방법.

![단어를 벡터로 변환하는 알고리즘의 예시 이미지](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.ko.png)

> [이 논문](https://arxiv.org/pdf/1301.3781.pdf)에서 발췌한 이미지

## ✍️ 예제 노트북: CBoW 모델 훈련

다음 노트북에서 학습을 계속하세요:

* [TensorFlow로 CBoW Word2Vec 훈련하기](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [PyTorch로 CBoW Word2Vec 훈련하기](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## 결론

이전 수업에서 우리는 단어 임베딩이 마법처럼 작동한다는 것을 보았습니다! 이제 단어 임베딩을 훈련하는 것이 그렇게 복잡한 작업이 아니라는 것을 알게 되었으며, 필요하다면 도메인 특화 텍스트에 대해 자체 단어 임베딩을 훈련할 수 있어야 합니다.

## [강의 후 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## 리뷰 & 자기 학습

* [언어 모델링에 대한 공식 PyTorch 튜토리얼](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Word2Vec 모델 훈련에 대한 공식 TensorFlow 튜토리얼](https://www.TensorFlow.org/tutorials/text/word2vec).
* **gensim** 프레임워크를 사용하여 몇 줄의 코드로 가장 일반적으로 사용되는 임베딩을 훈련하는 방법은 [이 문서](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html)에서 설명되어 있습니다.

## 🚀 [과제: 스킵-그램 모델 훈련하기](lab/README.md)

실습에서는 이 수업의 코드를 수정하여 CBoW 대신 스킵-그램 모델을 훈련하도록 도전합니다. [자세한 내용 읽기](lab/README.md)

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서는 해당 언어로 작성된 권위 있는 자료로 간주되어야 합니다. 중요한 정보에 대해서는 전문 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 우리는 책임을 지지 않습니다.