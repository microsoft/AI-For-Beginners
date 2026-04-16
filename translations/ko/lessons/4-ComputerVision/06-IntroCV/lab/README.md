# 광학 흐름을 사용한 움직임 감지

[AI for Beginners Curriculum](https://aka.ms/ai-beginners)에서 제공하는 실습 과제입니다.

## 과제

[이 비디오](../../../../../../lessons/4-ComputerVision/06-IntroCV/lab/palm-movement.mp4)를 참고하세요. 이 비디오에서는 한 사람의 손바닥이 안정된 배경 위에서 좌/우/상/하로 움직입니다.

**목표**는 광학 흐름을 사용하여 비디오의 어느 부분에서 상/하/좌/우 움직임이 발생하는지 판단하는 것입니다.

**추가 목표**는 [이 블로그 글](https://dev.to/amarlearning/finger-detection-and-tracking-using-opencv-and-python-586m) 또는 [여기](http://www.benmeline.com/finger-tracking-with-opencv-and-python/)에서 설명된 것처럼 피부 톤을 사용하여 손바닥/손가락 움직임을 실제로 추적하는 것입니다.

## 시작 노트북

[MovementDetection.ipynb](../../../../../../lessons/4-ComputerVision/06-IntroCV/lab/MovementDetection.ipynb)를 열어 실습을 시작하세요.

## 배울 점

움직임 감지나 손가락 끝 감지와 같은 비교적 복잡한 작업도 순수하게 컴퓨터 비전만으로 해결할 수 있는 경우가 있습니다. 따라서 OpenCV와 같은 라이브러리가 할 수 있는 일을 아는 것이 매우 유용합니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서의 원어 버전을 권위 있는 출처로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 책임을 지지 않습니다.