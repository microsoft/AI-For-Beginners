# 애완동물 얼굴 분류

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)에서 제공하는 실습 과제입니다.

## 작업

애완동물 보육원용 애플리케이션을 개발해야 한다고 상상해 보세요. 이 애플리케이션의 훌륭한 기능 중 하나는 사진에서 품종을 자동으로 발견하는 것입니다. 이는 신경망을 사용하여 성공적으로 수행할 수 있습니다.

**Pet Faces** 데이터셋을 사용하여 고양이와 개의 다양한 품종을 분류하기 위해 컨볼루션 신경망을 훈련해야 합니다.

## 데이터셋

우리는 [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) 애완동물 데이터셋에서 파생된 **Pet Faces** 데이터셋을 사용할 것입니다. 이 데이터셋에는 35가지의 서로 다른 개와 고양이 품종이 포함되어 있습니다.

![우리가 다룰 데이터셋](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.ko.png)

데이터셋을 다운로드하려면 다음 코드 스니펫을 사용하세요:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## 노트북 시작하기

[PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb)를 열어 실습을 시작하세요.

## 주요 내용

당신은 처음부터 이미지 분류라는 비교적 복잡한 문제를 해결했습니다! 클래스가 상당히 많았음에도 불구하고 합리적인 정확도를 얻을 수 있었습니다! 또한, 일부 클래스는 인간에게도 명확히 구분되지 않기 때문에 top-k 정확도를 측정하는 것이 의미가 있습니다.

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서는 해당 언어로 된 권위 있는 자료로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 우리는 책임을 지지 않습니다.