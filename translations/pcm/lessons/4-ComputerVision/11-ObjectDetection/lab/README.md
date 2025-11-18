<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ad568d55ae65c856fe929fc2b278510a",
  "translation_date": "2025-11-18T18:20:22+00:00",
  "source_file": "lessons/4-ComputerVision/11-ObjectDetection/lab/README.md",
  "language_code": "pcm"
}
-->
# Head Detection wit Hollywood Heads Dataset

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

To count how many people dey for video surveillance camera stream na important task wey fit help us know di number of visitors wey enter shop, di busy time for restaurant, and so on. To fit do dis kain task, we need sabi detect human head from different angles. To train object detection model wey go fit detect human heads, we fit use [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## Di Dataset

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) get 369,846 human heads wey dem mark for 224,740 movie frames from Hollywood movies. Dem provide am for [https://host.robots.ox.ac.uk/pascal/VOC/](../../../../../../lessons/4-ComputerVision/11-ObjectDetection/lab/PASCAL VOC) format, where for each image, e get XML description file wey go look like dis:

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

For dis dataset, e get only one class of objects `head`, and for each head, you go see di coordinates of di bounding box. You fit use Python libraries to parse XML, or use [dis library](https://pypi.org/project/pascal-voc/) to handle PASCAL VOC format directly.

## Training Object Detection 

You fit train object detection model using any of dis methods:

* Use [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) and di Python API to train di model for cloud programmatically. Custom Vision no go fit use more than few hundred images to train di model, so you go need limit di dataset.
* Use di example from [Keras tutorial](https://keras.io/examples/vision/retinanet/) to train RetunaNet model.
* Use [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) wey dey built-in for torchvision.

## Takeaway

Object detection na task wey dem dey use well well for industry. Even though some services dey wey fit help you do object detection (like [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), e still dey important make you understand how object detection dey work and sabi train your own models.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis docu don dey translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even though we dey try make sure say e correct, abeg sabi say automatic translation fit get mistake or no dey accurate well. Di original docu for di language wey dem write am first na di main correct one. For important information, e good make una use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->