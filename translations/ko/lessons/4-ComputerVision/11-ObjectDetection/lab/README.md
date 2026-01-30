# 할리우드 헤드 데이터셋을 이용한 머리 탐지

[AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners)에서 제공하는 실습 과제입니다.

## 과제

비디오 감시 카메라 스트림에서 사람 수를 세는 것은 상점의 방문자 수를 추정하거나, 식당의 혼잡한 시간을 파악하는 데 중요한 작업입니다. 이 작업을 해결하기 위해서는 다양한 각도에서 인간의 머리를 탐지할 수 있어야 합니다. 인간의 머리를 탐지하는 객체 탐지 모델을 학습시키기 위해 [할리우드 헤드 데이터셋](https://www.di.ens.fr/willow/research/headdetection/)을 사용할 수 있습니다.

## 데이터셋

[할리우드 헤드 데이터셋](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip)은 할리우드 영화의 224,740개의 프레임에서 369,846개의 인간 머리를 주석 처리한 데이터를 포함하고 있습니다. 이 데이터셋은 [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) 형식으로 제공되며, 각 이미지에 대해 XML 설명 파일이 함께 제공됩니다. XML 파일은 다음과 같은 형식입니다:

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

이 데이터셋에는 `head`라는 하나의 객체 클래스만 있으며, 각 머리에 대해 바운딩 박스의 좌표가 제공됩니다. XML 파일은 Python 라이브러리를 사용하여 파싱하거나, [이 라이브러리](https://pypi.org/project/pascal-voc/)를 사용하여 PASCAL VOC 형식을 직접 처리할 수 있습니다.

## 객체 탐지 모델 학습

객체 탐지 모델을 학습시키는 방법은 다음과 같습니다:

* [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)을 사용하여 클라우드에서 모델을 프로그래밍 방식으로 학습시키는 Python API를 활용합니다. Custom Vision은 모델 학습을 위해 몇백 개의 이미지만 사용할 수 있으므로 데이터셋을 제한해야 할 수도 있습니다.
* [Keras 튜토리얼](https://keras.io/examples/vision/retinanet/)의 예제를 사용하여 RetunaNet 모델을 학습시킵니다.
* [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) 모듈을 사용하여 학습합니다.

## 주요 내용

객체 탐지는 산업에서 자주 요구되는 작업입니다. [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)과 같은 서비스를 사용하여 객체 탐지를 수행할 수 있지만, 객체 탐지가 어떻게 작동하는지 이해하고 직접 모델을 학습시킬 수 있는 능력을 갖추는 것이 중요합니다.

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있지만, 자동 번역에는 오류나 부정확성이 포함될 수 있습니다. 원본 문서를 해당 언어로 작성된 상태에서 권위 있는 자료로 간주해야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.