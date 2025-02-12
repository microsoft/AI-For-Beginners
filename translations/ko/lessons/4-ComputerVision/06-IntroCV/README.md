# 컴퓨터 비전 소개

[컴퓨터 비전](https://wikipedia.org/wiki/Computer_vision)은 컴퓨터가 디지털 이미지를 높은 수준으로 이해할 수 있도록 하는 학문입니다. 이는 꽤 넓은 정의로, *이해*는 사진에서 물체 찾기(**물체 탐지**), 발생하는 사건 이해(**이벤트 탐지**), 사진을 텍스트로 설명하기, 또는 3D 장면 재구성 등 다양한 의미를 가질 수 있습니다. 사람의 이미지와 관련된 특별한 작업도 있으며, 여기에는 나이 및 감정 추정, 얼굴 탐지 및 식별, 3D 포즈 추정 등이 포함됩니다.

## [강의 전 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/106)

컴퓨터 비전의 가장 간단한 작업 중 하나는 **이미지 분류**입니다.

컴퓨터 비전은 종종 AI의 한 분야로 간주됩니다. 현재 대부분의 컴퓨터 비전 작업은 신경망을 사용하여 해결됩니다. 이 섹션에서는 컴퓨터 비전에서 사용되는 특별한 유형의 신경망인 [합성곱 신경망](../07-ConvNets/README.md)에 대해 더 배울 것입니다.

그러나 이미지를 신경망에 전달하기 전에, 많은 경우 이미지를 향상시키기 위해 몇 가지 알고리즘 기술을 사용하는 것이 의미가 있습니다.

이미지 처리에 사용할 수 있는 여러 Python 라이브러리가 있습니다:

* **[imageio](https://imageio.readthedocs.io/en/stable/)**는 다양한 이미지 형식을 읽고 쓸 수 있습니다. 또한 비디오 프레임을 이미지로 변환하는 유용한 도구인 ffmpeg를 지원합니다.
* **[Pillow](https://pillow.readthedocs.io/en/stable/index.html)** (PIL로도 알려져 있음)은 좀 더 강력하며, 변형, 팔레트 조정 등과 같은 일부 이미지 조작도 지원합니다.
* **[OpenCV](https://opencv.org/)**는 C++로 작성된 강력한 이미지 처리 라이브러리로, 이미지 처리의 *de facto* 표준이 되었습니다. 편리한 Python 인터페이스를 제공합니다.
* **[dlib](http://dlib.net/)**는 많은 기계 학습 알고리즘을 구현한 C++ 라이브러리로, 컴퓨터 비전 알고리즘도 포함되어 있습니다. Python 인터페이스가 있으며, 얼굴 및 얼굴 랜드마크 탐지와 같은 도전적인 작업에 사용할 수 있습니다.

## OpenCV

[OpenCV](https://opencv.org/)는 이미지 처리의 *de facto* 표준으로 간주됩니다. C++로 구현된 많은 유용한 알고리즘을 포함하고 있으며, Python에서도 OpenCV를 호출할 수 있습니다.

OpenCV를 배우기에 좋은 곳은 [이 Learn OpenCV 과정](https://learnopencv.com/getting-started-with-opencv/)입니다. 우리 커리큘럼의 목표는 OpenCV를 배우는 것이 아니라, OpenCV를 사용할 수 있는 몇 가지 예시를 보여주는 것입니다.

### 이미지 로딩

Python에서 이미지는 NumPy 배열로 편리하게 표현할 수 있습니다. 예를 들어, 320x200 픽셀 크기의 그레이스케일 이미지는 200x320 배열에 저장되며, 동일한 차원의 컬러 이미지는 200x320x3의 형태를 가집니다(3개 색상 채널). 이미지를 로드하려면 다음 코드를 사용할 수 있습니다:

```python
import cv2
import matplotlib.pyplot as plt

im = cv2.imread('image.jpeg')
plt.imshow(im)
```

전통적으로 OpenCV는 컬러 이미지에 대해 BGR(파랑-초록-빨강) 인코딩을 사용하고, 나머지 Python 도구들은 더 전통적인 RGB(빨강-초록-파랑)를 사용합니다. 이미지를 올바르게 보이게 하려면, NumPy 배열에서 차원을 교환하거나 OpenCV 함수를 호출하여 RGB 색상 공간으로 변환해야 합니다:

```python
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)
```

같은 `cvtColor` function can be used to perform other color space transformations such as converting an image to grayscale or to the HSV (Hue-Saturation-Value) color space.

You can also use OpenCV to load video frame-by-frame - an example is given in the exercise [OpenCV Notebook](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb).

### Image Processing

Before feeding an image to a neural network, you may want to apply several pre-processing steps. OpenCV can do many things, including:

* **Resizing** the image using `im = cv2.resize(im, (320,200),interpolation=cv2.INTER_LANCZOS)`
* **Blurring** the image using `im = cv2.medianBlur(im,3)` or `im = cv2.GaussianBlur(im, (3,3), 0)`
* Changing the **brightness and contrast** of the image can be done by NumPy array manipulations, as described [in this Stackoverflow note](https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv).
* Using [thresholding](https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html) by calling `cv2.threshold`/`cv2.adaptiveThreshold` 함수는 종종 밝기나 대비를 조정하는 것보다 선호됩니다.
* 이미지를 [변환](https://docs.opencv.org/4.5.5/da/d6e/tutorial_py_geometric_transformations.html)하는 다양한 방법 적용:
    - **[Affine 변환](https://docs.opencv.org/4.5.5/d4/d61/tutorial_warp_affine.html)**은 이미지에 회전, 크기 조정 및 왜곡을 결합해야 하고 이미지의 세 점의 원본 및 목적 위치를 알고 있는 경우 유용할 수 있습니다. Affine 변환은 평행선을 평행하게 유지합니다.
    - **[Perspective 변환](https://medium.com/analytics-vidhya/opencv-perspective-transformation-9edffefb2143)**은 이미지의 4점의 원본 및 목적 위치를 알고 있을 때 유용합니다. 예를 들어, 스마트폰 카메라로 어떤 각도에서 직사각형 문서의 사진을 찍고, 문서 자체의 직사각형 이미지를 만들고자 할 때입니다.
* **[광학 흐름](https://docs.opencv.org/4.5.5/d4/dee/tutorial_optical_flow.html)**을 사용하여 이미지 내의 움직임 이해하기.

## 컴퓨터 비전 사용 예

우리의 [OpenCV 노트북](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)에서는 컴퓨터 비전이 특정 작업을 수행하는 데 사용될 수 있는 몇 가지 예시를 제공합니다:

* **점자 책의 사진 전처리**. 우리는 점자 기호를 개별적으로 분리하여 신경망으로 추가 분류하기 위해 임계값 설정, 특징 탐지, 원근 변환 및 NumPy 조작을 어떻게 사용할 수 있는지에 중점을 둡니다.

![점자 이미지](../../../../../translated_images/braille.341962ff76b1bd7044409371d3de09ced5028132aef97344ea4b7468c1208126.ko.jpeg) | ![전처리된 점자 이미지](../../../../../translated_images/braille-result.46530fea020b03c76aac532d7d6eeef7f6fb35b55b1001cd21627907dabef3ed.ko.png) | ![점자 기호](../../../../../translated_images/braille-symbols.0159185ab69d533909dc4d7d26a1971b51401c6a80eb3a5584f250ea880af88b.ko.png)
----|-----|-----

> 이미지 출처: [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **프레임 차이를 사용하여 비디오에서 움직임 감지**. 카메라가 고정되어 있다면, 카메라 피드의 프레임은 서로 비슷해야 합니다. 프레임은 배열로 표현되므로, 두 개의 연속된 프레임의 배열을 빼면 픽셀 차이를 얻을 수 있습니다. 정적 프레임에서는 이 차이가 낮고, 이미지에 상당한 움직임이 있을 경우 높아집니다.

![비디오 프레임 및 프레임 차이 이미지](../../../../../translated_images/frame-difference.706f805491a0883c938e16447bf5eb2f7d69e812c7f743cbe7d7c7645168f81f.ko.png)

> 이미지 출처: [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

* **광학 흐름을 사용하여 움직임 감지**. [광학 흐름](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html)은 비디오 프레임의 개별 픽셀이 어떻게 움직이는지를 이해할 수 있게 해줍니다. 광학 흐름에는 두 가지 유형이 있습니다:

   - **밀집 광학 흐름**은 각 픽셀이 어디로 움직이는지를 보여주는 벡터 필드를 계산합니다.
   - **희소 광학 흐름**은 이미지에서 일부 독특한 특징(예: 에지)을 선택하고, 프레임 간의 궤적을 구축하는 데 기반합니다.

![광학 흐름 이미지](../../../../../translated_images/optical.1f4a94464579a83a10784f3c07fe7228514714b96782edf50e70ccd59d2d8c4f.ko.png)

> 이미지 출처: [OpenCV.ipynb](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

## ✍️ 예제 노트북: OpenCV [OpenCV를 행동으로 시도하기](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)

[OpenCV 노트북](../../../../../lessons/4-ComputerVision/06-IntroCV/OpenCV.ipynb)을 탐색하며 OpenCV로 실험해 봅시다.

## 결론

때때로, 움직임 감지나 손끝 감지와 같은 상대적으로 복잡한 작업은 순수하게 컴퓨터 비전만으로 해결할 수 있습니다. 따라서 컴퓨터 비전의 기본 기술과 OpenCV와 같은 라이브러리가 할 수 있는 일을 아는 것이 매우 유용합니다.

## 🚀 도전

AI 쇼에서 [이 비디오](https://docs.microsoft.com/shows/ai-show/ai-show--2021-opencv-ai-competition--grand-prize-winners--cortic-tigers--episode-32?WT.mc_id=academic-77998-cacaste)를 시청하여 Cortic Tigers 프로젝트에 대해 배우고, 그들이 로봇을 통해 컴퓨터 비전 작업을 민주화하기 위해 블록 기반 솔루션을 어떻게 구축했는지 알아보세요. 이 분야에 새로운 학습자를 onboarding하는 데 도움이 되는 다른 프로젝트에 대해 조사해 보세요.

## [강의 후 퀴즈](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/206)

## 리뷰 및 자기 학습

[이 훌륭한 튜토리얼](https://learnopencv.com/optical-flow-in-opencv/)에서 광학 흐름에 대해 더 읽어보세요.

## [과제](lab/README.md)

이 실습에서는 간단한 제스처로 비디오를 촬영하고, 목표는 광학 흐름을 사용하여 위/아래/왼쪽/오른쪽 움직임을 추출하는 것입니다.

<img src="images/palm-movement.png" width="30%" alt="손바닥 움직임 프레임"/>

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서는 해당 언어로 작성된 권위 있는 자료로 간주되어야 합니다. 중요한 정보에 대해서는 전문 인간 번역을 권장합니다. 이 번역을 사용하여 발생하는 오해나 잘못된 해석에 대해서는 책임을 지지 않습니다.