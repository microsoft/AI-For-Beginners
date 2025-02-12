# Skip-Gram 모델 훈련

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)에서의 실습 과제입니다.

## 과제

이번 실습에서는 Skip-Gram 기법을 사용하여 Word2Vec 모델을 훈련하는 도전을 합니다. $N$-토큰 너비의 Skip-Gram 윈도우에서 이웃 단어를 예측하기 위해 임베딩이 있는 네트워크를 훈련하세요. [이번 수업의 코드](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)를 사용하고, 약간 수정해도 좋습니다.

## 데이터셋

원하는 책을 자유롭게 사용할 수 있습니다. [Project Gutenberg](https://www.gutenberg.org/)에서 많은 무료 텍스트를 찾을 수 있으며, 예를 들어 루이스 캐럴의 [이상한 나라의 앨리스](https://www.gutenberg.org/files/11/11-0.txt)로 가는 직접 링크가 있습니다. 또는 다음 코드를 사용하여 셰익스피어의 희곡을 사용할 수 있습니다:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## 탐색해보세요!

시간이 있고 주제에 대해 더 깊이 파고들고 싶다면 여러 가지를 탐색해 보세요:

* 임베딩 크기가 결과에 어떤 영향을 미칩니까?
* 다양한 텍스트 스타일이 결과에 어떤 영향을 미칩니까?
* 매우 다른 유형의 단어와 그 동의어를 여러 개 선택하고, 이들의 벡터 표현을 얻은 다음, PCA를 적용하여 차원을 2로 줄이고 2D 공간에 플롯해 보세요. 어떤 패턴이 보이나요?

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 권위 있는 자료로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.