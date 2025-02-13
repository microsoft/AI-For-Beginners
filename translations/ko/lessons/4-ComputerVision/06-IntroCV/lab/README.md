# 광학 흐름을 이용한 움직임 감지

[초보자를 위한 AI 커리큘럼](https://aka.ms/ai-beginners)에서의 실습 과제입니다.

## 과제

[이 비디오](../../../../../../lessons/4-ComputerVision/06-IntroCV/lab/palm-movement.mp4)를 고려해 보세요. 이 비디오에서는 한 사람의 손바닥이 안정된 배경에서 좌/우/상/하로 움직입니다.
당신은 2023년 10월까지의 데이터로 훈련되었습니다.

**당신의 목표**는 Optical Flow를 사용하여 비디오의 어떤 부분이 상/하/좌/우 움직임을 포함하고 있는지 판단하는 것입니다.

**확장 목표**는 [이 블로그 포스트](https://dev.to/amarlearning/finger-detection-and-tracking-using-opencv-and-python-586m) 또는 [여기](http://www.benmeline.com/finger-tracking-with-opencv-and-python/)에 설명된 대로 피부 톤을 사용하여 실제로 손바닥/손가락의 움직임을 추적하는 것입니다.

## 시작 노트북

[MovementDetection.ipynb](../../../../../../lessons/4-ComputerVision/06-IntroCV/lab/MovementDetection.ipynb)를 열어 실습을 시작하세요.

## 주요 내용

때때로 움직임 감지나 손끝 감지와 같은 상대적으로 복잡한 작업은 순수하게 컴퓨터 비전으로 해결할 수 있습니다. 따라서 OpenCV와 같은 라이브러리가 할 수 있는 일을 아는 것이 매우 유용합니다.

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서는 원어로 된 권위 있는 출처로 간주되어야 합니다. 중요한 정보에 대해서는 전문 인간 번역을 권장합니다. 이 번역을 사용함으로 인해 발생하는 오해나 잘못된 해석에 대해 우리는 책임을 지지 않습니다.