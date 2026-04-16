# 인간 신체 분할

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)에서 제공하는 실습 과제입니다.

## 과제

비디오 제작, 예를 들어 날씨 예보에서, 카메라로 촬영된 인간 이미지를 잘라내어 다른 영상 위에 배치해야 하는 경우가 종종 있습니다. 이는 일반적으로 **크로마 키** 기술을 사용하여 이루어지며, 사람이 단색 배경 앞에서 촬영된 후 배경이 제거됩니다. 이번 실습에서는 인간 실루엣을 잘라내는 신경망 모델을 학습시킬 것입니다.

## 데이터셋

우리는 Kaggle에서 제공하는 [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset)을 사용할 것입니다. Kaggle에서 데이터를 수동으로 다운로드하세요.

## 시작 노트북

[BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb)를 열어 실습을 시작하세요.

## 주요 학습 내용

신체 분할은 사람의 이미지를 활용하여 수행할 수 있는 일반적인 작업 중 하나입니다. 또 다른 중요한 작업으로는 **골격 감지**와 **자세 감지**가 있습니다. 이러한 작업이 어떻게 구현될 수 있는지 알아보려면 [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) 라이브러리를 확인해 보세요.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.