<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ad568d55ae65c856fe929fc2b278510a",
  "translation_date": "2025-08-31T17:41:21+00:00",
  "source_file": "lessons/4-ComputerVision/11-ObjectDetection/lab/README.md",
  "language_code": "en"
}
-->
# Head Detection using Hollywood Heads Dataset

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

Counting the number of people on a video surveillance camera stream is an important task that helps estimate the number of visitors in stores, peak hours in restaurants, and more. To accomplish this, we need to detect human heads from various angles. To train an object detection model for identifying human heads, we can use the [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## The Dataset

The [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) includes 369,846 human heads annotated across 224,740 movie frames from Hollywood films. It is provided in [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) format, where each image is accompanied by an XML description file that looks like this:

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

This dataset contains only one object class, `head`, and provides bounding box coordinates for each head. You can parse the XML files using Python libraries or use [this library](https://pypi.org/project/pascal-voc/) to work directly with the PASCAL VOC format.

## Training Object Detection 

You can train an object detection model using one of the following approaches:

* Using [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) and its Python API to programmatically train the model in the cloud. Note that Custom Vision may only support a few hundred images for training, so you might need to limit the dataset.
* Following the example from the [Keras tutorial](https://keras.io/examples/vision/retinanet/) to train a RetinaNet model.
* Using the built-in module [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) in torchvision.

## Takeaway

Object detection is a task frequently required in industry. While there are services available for performing object detection (such as [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), it is essential to understand how object detection works and to have the ability to train your own models.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.