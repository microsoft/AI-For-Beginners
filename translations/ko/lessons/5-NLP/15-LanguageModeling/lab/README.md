# Skip-Gram 모델 학습

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)에서 제공하는 실습 과제입니다.

## 과제

이번 실습에서는 Skip-Gram 기법을 사용하여 Word2Vec 모델을 학습하는 과제를 수행합니다. $N$-토큰 너비의 Skip-Gram 윈도우에서 이웃 단어를 예측하기 위해 임베딩을 포함한 네트워크를 학습하세요. [이 강의의 코드](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)를 사용하고 약간 수정하여 활용할 수 있습니다.

## 데이터셋

어떤 책이든 사용할 수 있습니다. [Project Gutenberg](https://www.gutenberg.org/)에서 많은 무료 텍스트를 찾을 수 있습니다. 예를 들어, Lewis Carroll의 [이상한 나라의 앨리스](https://www.gutenberg.org/files/11/11-0.txt))에 직접 접근할 수 있습니다. 또는 셰익스피어의 희곡을 사용할 수도 있습니다. 아래 코드를 사용하여 다운로드할 수 있습니다:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## 탐구해보세요!

시간이 있고 주제에 대해 더 깊이 탐구하고 싶다면, 다음을 시도해보세요:

* 임베딩 크기가 결과에 어떤 영향을 미치는지 확인하세요.
* 서로 다른 텍스트 스타일이 결과에 어떤 영향을 미치는지 확인하세요.
* 매우 다른 유형의 단어와 그 동의어를 몇 가지 선택하여 벡터 표현을 얻고, PCA를 사용해 차원을 2로 줄인 후 2D 공간에 플롯하세요. 어떤 패턴이 보이나요?

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.