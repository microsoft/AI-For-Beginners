# 할리우드 헤드 데이터셋을 이용한 머리 탐지

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)에서의 실습 과제입니다.

## 작업

비디오 감시 카메라 스트림에서 사람 수를 세는 것은 상점의 방문객 수, 레스토랑의 바쁜 시간 등을 추정할 수 있게 해주는 중요한 작업입니다. 이 작업을 해결하기 위해서는 다양한 각도에서 사람의 머리를 탐지할 수 있어야 합니다. 사람 머리를 탐지하는 객체 탐지 모델을 훈련시키기 위해 [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/)을 사용할 수 있습니다.

## 데이터셋

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip)에는 할리우드 영화의 224,740개 영화 프레임에서 주석이 달린 369,846개의 인간 머리가 포함되어 있습니다. 이 데이터셋은 각 이미지에 대해 XML 설명 파일이 제공되는 [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) 형식으로 제공됩니다. XML 파일은 다음과 같은 형식을 가집니다:

```xml
<annotation>
	<folder>HollywoodHeads</folder>
	<filename>mov_021_149390.jpeg</filename>
	<source>
		<database>HollywoodHeads 2015 Database</database>
		<annotation>HollywoodHeads 2015</annotation>
		<image>WILLOW</image>
	</source>
	<size>
		<width>608</width>
		<height>320</height>
		<depth>3</depth>
	</size>
	<segmented>0</segmented>
	<object>
		<name>head</name>
		<bndbox>
			<xmin>201</xmin>
			<ymin>1</ymin>
			<xmax>480</xmax>
			<ymax>263</ymax>
		</bndbox>
		<difficult>0</difficult>
	</object>
	<object>
		<name>head</name>
		<bndbox>
			<xmin>3</xmin>
			<ymin>4</ymin>
			<xmax>241</xmax>
			<ymax>285</ymax>
		</bndbox>
		<difficult>0</difficult>
	</object>
</annotation>
```

이 데이터셋에는 `head`라는 하나의 객체 클래스만 있으며, 각 머리에 대해 경계 상자의 좌표를 제공합니다. Python 라이브러리를 사용하여 XML을 파싱하거나 [이 라이브러리](https://pypi.org/project/pascal-voc/)를 사용하여 PASCAL VOC 형식과 직접적으로 작업할 수 있습니다.

## 객체 탐지 훈련

다음 방법 중 하나를 사용하여 객체 탐지 모델을 훈련할 수 있습니다:

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)과 그 Python API를 사용하여 클라우드에서 프로그래밍 방식으로 모델을 훈련합니다. Custom Vision은 모델 훈련에 사용할 수 있는 이미지 수를 몇 백 장으로 제한할 수 있으므로 데이터셋을 제한해야 할 수도 있습니다.
* [Keras 튜토리얼](https://keras.io/examples/vision/retinanet/)의 예제를 사용하여 RetinaNet 모델을 훈련합니다.
* [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)에서 제공하는 torchvision 내장 모듈을 사용합니다.

## 요점

객체 탐지는 산업에서 자주 요구되는 작업입니다. 객체 탐지를 수행하는 데 사용할 수 있는 서비스가 있지만([Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)와 같은), 객체 탐지가 어떻게 작동하는지를 이해하고 자신의 모델을 훈련할 수 있는 것이 중요합니다.

**면책 조항**:  
이 문서는 기계 기반 AI 번역 서비스를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원본 문서는 해당 언어로 작성된 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.