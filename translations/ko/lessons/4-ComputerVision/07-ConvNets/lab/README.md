<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-24T21:30:23+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "ko"
}
-->
# 반려동물 얼굴 분류

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)에서 제공하는 실습 과제입니다.

## 과제

반려동물 보육원을 위한 애플리케이션을 개발해야 한다고 상상해보세요. 이 애플리케이션의 훌륭한 기능 중 하나는 사진을 통해 자동으로 품종을 식별하는 것입니다. 이는 신경망을 사용하여 성공적으로 구현할 수 있습니다.

**Pet Faces** 데이터셋을 사용하여 고양이와 개의 다양한 품종을 분류하는 컨볼루션 신경망을 훈련해야 합니다.

## 데이터셋

우리는 [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) 반려동물 데이터셋에서 파생된 **Pet Faces** 데이터셋을 사용할 것입니다. 이 데이터셋은 35가지의 서로 다른 개와 고양이 품종을 포함하고 있습니다.

![우리가 다룰 데이터셋](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.ko.png)

데이터셋을 다운로드하려면 아래 코드 스니펫을 사용하세요:

```python
!wget https://mslearntensorflowlp.blob.core.windows.net/data/petfaces.tar.gz
!tar xfz petfaces.tar.gz
!rm petfaces.tar.gz
```

## 시작 노트북

[PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb)를 열어 실습을 시작하세요.

## 주요 성과

여러분은 이미지를 분류하는 비교적 복잡한 문제를 처음부터 해결했습니다! 클래스가 꽤 많았음에도 불구하고 합리적인 정확도를 얻을 수 있었습니다. 또한, top-k 정확도를 측정하는 것도 의미가 있습니다. 왜냐하면 인간조차도 명확히 구분하기 어려운 클래스들이 있기 때문입니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전이 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.