# 전이 학습을 활용한 Oxford Pets 분류

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)에서 제공하는 실습 과제입니다.

## 과제

애완동물 보육원을 위한 애플리케이션을 개발해야 한다고 상상해보세요. 이러한 애플리케이션의 훌륭한 기능 중 하나는 사진을 통해 자동으로 품종을 식별하는 것입니다. 이번 과제에서는 전이 학습을 사용하여 [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) 애완동물 데이터셋의 실제 애완동물 이미지를 분류할 것입니다.

## 데이터셋

우리는 원본 [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) 애완동물 데이터셋을 사용할 것입니다. 이 데이터셋은 35가지 다른 품종의 개와 고양이를 포함하고 있습니다.

데이터셋을 다운로드하려면 아래 코드 스니펫을 사용하세요:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## 시작 노트북

실습을 시작하려면 [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)를 열어보세요.

## 주요 내용

전이 학습과 사전 학습된 네트워크를 활용하면 실제 이미지 분류 문제를 비교적 쉽게 해결할 수 있습니다. 하지만 사전 학습된 네트워크는 유사한 종류의 이미지에서 잘 작동하며, 만약 매우 다른 이미지를 분류하려고 한다면(예: 의료 이미지), 결과가 훨씬 나빠질 가능성이 높습니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.