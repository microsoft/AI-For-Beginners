# Head Detection using Hollywood Heads Dataset

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

Counting number of people on video surveillance camera stream is an important task that will allow us to estimate the number of visitors in a shops, busy hours in a restaurant, etc. To solve this task, we need to be able to detect human heads from different angles. To train object detection model to detect human heads, we can use [Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/).

## The Dataset

[Hollywood Heads Dataset](https://www.di.ens.fr/willow/research/headdetection/release/HollywoodHeads.zip) contains 369,846 human heads annotated in 224,740 movie frames from Hollywood movies. It is provided in [https://host.robots.ox.ac.uk/pascal/VOC/](PASCAL VOC) format, where for each image there is also an XML description file that looks like this:

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

In this dataset, there is only one class of objects `head`, and for each head, you get the coordinates of the bounding box. You can parse XML using Python libraries, or use [this library](https://pypi.org/project/pascal-voc/) to deal directly with PASCAL VOC format.

## Training Object Detection 

You can train an object detection model using one of the following ways:

* Using [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste) and it's Python API to programmatically train the model in the cloud. Custom vision will not be able to use more than a few hundred images for training the model, so you may need to limit the dataset.
* Using the example from [Keras tutorial](https://keras.io/examples/vision/retinanet/) to train RetunaNet model.
* Using [torchvision.models.detection.RetinaNet](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html) build-in module in torchvision.

## Takeaway

Object detection is a task that is frequently required in industry. While there are some services that can be used to perform object detection (such as [Azure Custom Vision](https://docs.microsoft.com/azure/cognitive-services/custom-vision-service/quickstarts/object-detection?tabs=visual-studio&WT.mc_id=academic-77998-cacaste)), it is important to understand how object detection works and to be able to train your own models. 