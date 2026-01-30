# 객체 탐지

지금까지 다룬 이미지 분류 모델은 이미지를 입력받아 MNIST 문제에서 '숫자' 클래스와 같은 범주형 결과를 출력했습니다. 하지만 많은 경우, 단순히 이미지에 객체가 있다는 것을 아는 것만으로는 충분하지 않습니다. 우리는 객체의 정확한 위치를 파악하고 싶어합니다. 이것이 바로 **객체 탐지**의 핵심입니다.

## [강의 전 퀴즈](https://ff-quizzes.netlify.app/en/ai/quiz/21)

![객체 탐지](../../../../../translated_images/ko/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be.webp)

> 이미지 출처: [YOLO v2 웹사이트](https://pjreddie.com/darknet/yolov2/)

## 객체 탐지에 대한 단순한 접근법

사진에서 고양이를 찾고 싶다고 가정해 봅시다. 객체 탐지에 대한 매우 단순한 접근법은 다음과 같습니다:

1. 이미지를 여러 타일로 나눕니다.
2. 각 타일에 대해 이미지 분류를 실행합니다.
3. 충분히 높은 활성화를 보이는 타일은 해당 객체를 포함하고 있다고 간주합니다.

![단순 객체 탐지](../../../../../translated_images/ko/naive-detection.e7f1ba220ccd08c6.webp)

> *이미지 출처: [실습 노트북](ObjectDetection-TF.ipynb)*

하지만 이 접근법은 이상적이지 않습니다. 이 방법은 객체의 경계 상자를 매우 부정확하게 위치시킬 수밖에 없습니다. 더 정확한 위치를 찾으려면 경계 상자의 좌표를 예측하기 위해 **회귀**를 실행해야 하며, 이를 위해 특정 데이터셋이 필요합니다.

## 객체 탐지를 위한 회귀

[이 블로그 글](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491)은 도형 탐지에 대한 훌륭한 입문 자료입니다.

## 객체 탐지를 위한 데이터셋

다음과 같은 데이터셋을 접할 수 있습니다:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 20개의 클래스
* [COCO](http://cocodataset.org/#home) - 컨텍스트 내 일반 객체. 80개의 클래스, 경계 상자 및 세분화 마스크 제공

![COCO](../../../../../translated_images/ko/coco-examples.71bc60380fa6cceb.webp)

## 객체 탐지 평가 지표

### 교집합 비율 (Intersection over Union)

이미지 분류에서는 알고리즘의 성능을 측정하기 쉽지만, 객체 탐지에서는 클래스의 정확성과 예측된 경계 상자 위치의 정밀도를 모두 측정해야 합니다. 후자를 위해 **교집합 비율**(IoU)을 사용합니다. 이는 두 상자(또는 임의의 두 영역)가 얼마나 잘 겹치는지를 측정합니다.

![IoU](../../../../../translated_images/ko/iou_equation.9a4751d40fff4e11.webp)

> *출처: [이 훌륭한 IoU 블로그 글](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

IoU의 개념은 간단합니다. 두 도형의 교집합 면적을 합집합 면적으로 나눕니다. 두 영역이 동일하면 IoU는 1이 되고, 완전히 분리된 경우 0이 됩니다. 그 외의 경우 0에서 1 사이의 값을 가집니다. 일반적으로 IoU가 특정 값 이상인 경계 상자만 고려합니다.

### 평균 정밀도 (Average Precision)

특정 클래스 $C$의 객체가 얼마나 잘 인식되는지 측정하려면 **평균 정밀도**(AP) 지표를 사용합니다. 계산 방법은 다음과 같습니다:

1. 정밀도-재현율 곡선은 탐지 임계값 값(0에서 1까지)에 따라 정확도를 보여줍니다.
2. 임계값에 따라 이미지에서 탐지된 객체 수와 정밀도 및 재현율 값이 달라집니다.
3. 곡선은 다음과 같은 형태를 가집니다:

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *이미지 출처: [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

클래스 $C$에 대한 평균 정밀도는 이 곡선 아래의 면적입니다. 보다 정확히는, 재현율 축을 10개 부분으로 나누고, 각 점에서 정밀도를 평균화합니다:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP와 IoU

IoU가 특정 값 이상인 탐지만 고려합니다. 예를 들어, PASCAL VOC 데이터셋에서는 일반적으로 $\mbox{IoU Threshold} = 0.5$를 사용하며, COCO에서는 다양한 $\mbox{IoU Threshold}$ 값에 대해 AP를 측정합니다.

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *이미지 출처: [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### 평균 평균 정밀도 - mAP

객체 탐지의 주요 평가지표는 **평균 평균 정밀도**(mAP)입니다. 이는 모든 객체 클래스에 대해 평균화된 평균 정밀도 값이며, 때로는 $\mbox{IoU Threshold}$에 대해서도 평균화됩니다. **mAP** 계산 과정은 [이 블로그 글](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3)과 [코드 샘플](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734)에서 자세히 설명되어 있습니다.

## 다양한 객체 탐지 접근법

객체 탐지 알고리즘은 크게 두 가지로 나뉩니다:

* **영역 제안 네트워크**(R-CNN, Fast R-CNN, Faster R-CNN). 주요 아이디어는 **관심 영역**(ROI)을 생성하고, CNN을 통해 최대 활성화를 찾는 것입니다. 이는 단순한 접근법과 비슷하지만, ROI가 더 정교하게 생성된다는 점이 다릅니다. 이러한 방법의 주요 단점은 이미지에 대해 CNN 분류기를 여러 번 실행해야 하므로 느리다는 점입니다.
* **한 번에 처리**(YOLO, SSD, RetinaNet) 방법. 이러한 아키텍처에서는 네트워크가 한 번의 실행으로 클래스와 ROI를 예측하도록 설계됩니다.

### R-CNN: 영역 기반 CNN

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf)은 [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf)를 사용하여 ROI 영역의 계층 구조를 생성합니다. 그런 다음 이를 CNN 특징 추출기와 SVM 분류기를 통해 객체 클래스를 결정하고, 선형 회귀를 통해 *경계 상자* 좌표를 결정합니다. [공식 논문](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/ko/rcnn1.cae407020dfb1d1f.webp)

> *이미지 출처: van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/ko/rcnn2.2d9530bb83516484.webp)

> *이미지 출처: [이 블로그](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - Fast R-CNN

이 접근법은 R-CNN과 유사하지만, 영역이 합성곱 계층이 적용된 후에 정의됩니다.

![FRCNN](../../../../../translated_images/ko/f-rcnn.3cda6d9bb4188875.webp)

> 이미지 출처: [공식 논문](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

이 접근법의 주요 아이디어는 ROI를 예측하기 위해 신경망을 사용하는 것입니다. 이를 *영역 제안 네트워크*라고 합니다. [논문](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../translated_images/ko/faster-rcnn.8d46c099b87ef30a.webp)

> 이미지 출처: [공식 논문](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: 영역 기반 완전 합성곱 네트워크

이 알고리즘은 Faster R-CNN보다 더 빠릅니다. 주요 아이디어는 다음과 같습니다:

1. ResNet-101을 사용하여 특징을 추출합니다.
2. 특징은 **위치 민감 점수 맵**으로 처리됩니다. $C$ 클래스의 각 객체는 $k\times k$ 영역으로 나뉘며, 객체의 부분을 예측하도록 학습합니다.
3. $k\times k$ 영역의 각 부분에 대해 모든 네트워크가 객체 클래스를 투표하며, 최대 투표를 받은 객체 클래스가 선택됩니다.

![r-fcn 이미지](../../../../../translated_images/ko/r-fcn.13eb88158b99a3da.webp)

> 이미지 출처: [공식 논문](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO는 실시간 한 번 처리 알고리즘입니다. 주요 아이디어는 다음과 같습니다:

 * 이미지를 $S\times S$ 영역으로 나눕니다.
 * 각 영역에 대해 **CNN**이 $n$개의 가능한 객체, *경계 상자* 좌표 및 *신뢰도*=*확률* * IoU를 예측합니다.

 ![YOLO](../../../../../translated_images/ko/yolo.a2648ec82ee8bb4e.webp)

> 이미지 출처: [공식 논문](https://arxiv.org/abs/1506.02640)

### 기타 알고리즘

* RetinaNet: [공식 논문](https://arxiv.org/abs/1708.02002)
   - [Torchvision의 PyTorch 구현](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Keras 구현](https://github.com/fizyr/keras-retinanet)
   - Keras 샘플에서 [RetinaNet을 사용한 객체 탐지](https://keras.io/examples/vision/retinanet/)
* SSD (Single Shot Detector): [공식 논문](https://arxiv.org/abs/1512.02325)

## ✍️ 연습: 객체 탐지

다음 노트북에서 학습을 계속하세요:

[ObjectDetection.ipynb](ObjectDetection.ipynb)

## 결론

이 강의에서는 객체 탐지를 수행할 수 있는 다양한 방법을 빠르게 살펴보았습니다!

## 🚀 도전 과제

YOLO에 대한 다음 기사와 노트북을 읽고 직접 시도해 보세요:

* [YOLO에 대한 좋은 블로그 글](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/)
 * [공식 사이트](https://pjreddie.com/darknet/yolo/)
 * Yolo: [Keras 구현](https://github.com/experiencor/keras-yolo2), [단계별 노트북](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
 * Yolo v2: [Keras 구현](https://github.com/experiencor/keras-yolo2), [단계별 노트북](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [강의 후 퀴즈](https://ff-quizzes.netlify.app/en/ai/quiz/22)

## 복습 및 자기 학습

* [객체 탐지](https://tjmachinelearning.com/lectures/1718/obj/) by Nikhil Sardana
* [객체 탐지 알고리즘 비교](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [객체 탐지를 위한 딥러닝 알고리즘 리뷰](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [기본 객체 탐지 알고리즘에 대한 단계별 소개](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Python을 사용한 Faster R-CNN 구현](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [과제: 객체 탐지](lab/README.md)

---

