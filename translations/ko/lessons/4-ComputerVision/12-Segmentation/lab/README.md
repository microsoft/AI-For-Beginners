# 인체 분할

[초보자를 위한 AI 커리큘럼](https://github.com/microsoft/ai-for-beginners)에서의 실습 과제입니다.

## 과제

영상 제작, 예를 들어 날씨 예보에서, 우리는 종종 카메라에서 사람 이미지를 잘라내어 다른 영상 위에 배치해야 합니다. 이는 일반적으로 **크로마 키** 기술을 사용하여 수행되며, 사람이 균일한 색상의 배경 앞에서 촬영된 후 해당 배경이 제거됩니다. 이 실습에서는 인체 실루엣을 잘라내기 위해 신경망 모델을 훈련할 것입니다.

## 데이터셋

우리는 Kaggle의 [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset)을 사용할 것입니다. Kaggle에서 데이터셋을 수동으로 다운로드하세요.

## 노트북 시작하기

[BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb)를 열어 실습을 시작하세요.

## 주요 포인트

인체 분할은 사람의 이미지로 수행할 수 있는 일반적인 작업 중 하나일 뿐입니다. 또 다른 중요한 작업으로는 **스켈레톤 감지**와 **포즈 감지**가 있습니다. 이러한 작업이 어떻게 구현될 수 있는지 보려면 [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) 라이브러리를 확인해보세요.

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문적인 인간 번역을 권장합니다. 이 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해서는 저희가 책임지지 않습니다.