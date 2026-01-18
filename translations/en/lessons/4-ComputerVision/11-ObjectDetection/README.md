<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d76a7eda28de5210c8b1ba50a6216c69",
  "translation_date": "2025-09-23T11:45:25+00:00",
  "source_file": "lessons/4-ComputerVision/11-ObjectDetection/README.md",
  "language_code": "en"
}
-->
# Object Detection

The image classification models we've explored so far take an image as input and produce a categorical output, such as identifying the class 'number' in the MNIST dataset. However, in many scenarios, it's not enough to simply know that an image contains certain objects—we also want to pinpoint their exact locations. This is the purpose of **object detection**.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/21)

![Object Detection](../../../../../translated_images/en/Screen_Shot_2016-11-17_at_11.14.54_AM.b4bb3769353287be1b905373ed9c858102c054b16e4595c76ec3f7bba0feb549.png)

> Image from [YOLO v2 website](https://pjreddie.com/darknet/yolov2/)

## A Naive Approach to Object Detection

Imagine we want to locate a cat in an image. A very simplistic approach to object detection might look like this:

1. Divide the image into a grid of smaller tiles.
2. Perform image classification on each tile.
3. Identify tiles with sufficiently high activation as containing the object of interest.

![Naive Object Detection](../../../../../translated_images/en/naive-detection.e7f1ba220ccd08c68a2ea8e06a7ed75c3fcc738c2372f9e00b7f4299a8659c01.png)

> *Image from [Exercise Notebook](ObjectDetection-TF.ipynb)*

However, this method is far from ideal because it only provides a rough estimate of the object's bounding box. For more precise localization, we need to use **regression** to predict the bounding box coordinates—and for that, we require specialized datasets.

## Regression for Object Detection

[This blog post](https://towardsdatascience.com/object-detection-with-neural-networks-a4e2c46b4491) offers an excellent introduction to detecting shapes.

## Datasets for Object Detection

Here are some commonly used datasets for object detection:

* [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/) - 20 classes
* [COCO](http://cocodataset.org/#home) - Common Objects in Context. Includes 80 classes, bounding boxes, and segmentation masks.

![COCO](../../../../../translated_images/en/coco-examples.71bc60380fa6cceb7caad48bd09e35b6028caabd363aa04fee89c414e0870e86.jpg)

## Object Detection Metrics

### Intersection over Union

While evaluating image classification models is straightforward, object detection requires assessing both the accuracy of the predicted class and the precision of the bounding box location. For the latter, we use **Intersection over Union** (IoU), which measures the overlap between two bounding boxes (or areas).

![IoU](../../../../../translated_images/en/iou_equation.9a4751d40fff4e119ecd0a7bcca4e71ab1dc83e0d4f2a0d66ff0859736f593cf.png)

> *Figure 2 from [this excellent blog post on IoU](https://pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)*

The concept is simple: divide the area of intersection between two shapes by the area of their union. For two identical shapes, IoU equals 1. For completely non-overlapping shapes, IoU equals 0. Typically, we only consider bounding boxes with IoU above a certain threshold.

### Average Precision

To evaluate how well a specific object class $C$ is detected, we use the **Average Precision** metric, calculated as follows:

1. Plot a Precision-Recall curve, which shows accuracy as a function of the detection threshold (ranging from 0 to 1).
2. Depending on the threshold, the number of detected objects and the precision-recall values will vary.
3. The resulting curve looks like this:

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecall.png"/>

> *Image from [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

The Average Precision for a class $C$ is the area under this curve. More specifically, the Recall axis is divided into 10 segments, and Precision is averaged across these points:

$$
AP = {1\over11}\sum_{i=0}^{10}\mbox{Precision}(\mbox{Recall}={i\over10})
$$

### AP and IoU

We only consider detections with IoU above a certain threshold. For example, the PASCAL VOC dataset typically uses $\mbox{IoU Threshold} = 0.5$, while COCO evaluates AP across multiple $\mbox{IoU Threshold}$ values.

<img src="https://github.com/shwars/NeuroWorkshop/raw/master/images/ObjDetectionPrecisionRecallIoU.png"/>

> *Image from [NeuroWorkshop](http://github.com/shwars/NeuroWorkshop)*

### Mean Average Precision - mAP

The primary metric for object detection is **Mean Average Precision** (mAP). This is the Average Precision averaged across all object classes, and sometimes across multiple $\mbox{IoU Threshold}$ values. The process of calculating **mAP** is explained in detail [in this blog post](https://medium.com/@timothycarlen/understanding-the-map-evaluation-metric-for-object-detection-a07fe6962cf3) and [here with code examples](https://gist.github.com/tarlen5/008809c3decf19313de216b9208f3734).

## Different Object Detection Approaches

Object detection algorithms can be broadly categorized into two types:

* **Region Proposal Networks** (R-CNN, Fast R-CNN, Faster R-CNN): These methods generate **Regions of Interest** (ROIs) and run a CNN over them to find the highest activations. This approach is somewhat similar to the naive method but uses more sophisticated ROI generation. A major drawback is that these methods are slow because the CNN classifier must process the image multiple times.
* **One-pass methods** (YOLO, SSD, RetinaNet): These architectures predict both object classes and ROIs in a single pass.

### R-CNN: Region-Based CNN

[R-CNN](http://islab.ulsan.ac.kr/files/announcement/513/rcnn_pami.pdf) uses [Selective Search](http://www.huppelen.nl/publications/selectiveSearchDraft.pdf) to generate a hierarchical structure of ROIs. These ROIs are passed through CNN feature extractors and SVM classifiers to determine object classes, while linear regression predicts the *bounding box* coordinates. [Official Paper](https://arxiv.org/pdf/1506.01497v1.pdf)

![RCNN](../../../../../translated_images/en/rcnn1.cae407020dfb1d1fb572656e44f75cd6c512cc220591c116c506652c10e47f26.png)

> *Image from van de Sande et al. ICCV’11*

![RCNN-1](../../../../../translated_images/en/rcnn2.2d9530bb83516484ec65b250c22dbf37d3d23244f32864ebcb91d98fe7c3112c.png)

> *Images from [this blog](https://towardsdatascience.com/r-cnn-fast-r-cnn-faster-r-cnn-yolo-object-detection-algorithms-36d53571365e)*

### F-RCNN - Fast R-CNN

This method is similar to R-CNN, but the regions are defined after applying convolutional layers.

![FRCNN](../../../../../translated_images/en/f-rcnn.3cda6d9bb41888754037d2d9763e2298a96de5d9bc2a21db3147357aa5da9b1a.png)

> Image from [the Official Paper](https://www.cv-foundation.org/openaccess/content_iccv_2015/papers/Girshick_Fast_R-CNN_ICCV_2015_paper.pdf), [arXiv](https://arxiv.org/pdf/1504.08083.pdf), 2015

### Faster R-CNN

This approach introduces a neural network to predict ROIs, known as the *Region Proposal Network*. [Paper](https://arxiv.org/pdf/1506.01497.pdf), 2016

![FasterRCNN](../../../../../translated_images/en/faster-rcnn.8d46c099b87ef30ab2ea26dbc4bdd85b974a57ba8eb526f65dc4cd0a4711de30.png)

> Image from [the official paper](https://arxiv.org/pdf/1506.01497.pdf)

### R-FCN: Region-Based Fully Convolutional Network

This algorithm is faster than Faster R-CNN. The key idea is:

1. Extract features using ResNet-101.
2. Process features with a **Position-Sensitive Score Map**. Each object from $C$ classes is divided into $k\times k$ regions, and the network predicts parts of objects.
3. For each part of the $k\times k$ regions, the networks vote for object classes, and the class with the highest vote is selected.

![r-fcn image](../../../../../translated_images/en/r-fcn.13eb88158b99a3da50fa2787a6be5cb310d47f0e9655cc93a1090dc7aab338d1.png)

> Image from [official paper](https://arxiv.org/abs/1605.06409)

### YOLO - You Only Look Once

YOLO is a real-time, one-pass algorithm. The main idea is:

* Divide the image into $S\times S$ regions.
* For each region, the **CNN** predicts $n$ possible objects, *bounding box* coordinates, and *confidence* = *probability* × IoU.

![YOLO](../../../../../translated_images/en/yolo.a2648ec82ee8bb4ea27537677adb482fd4b733ca1705c561b6a24a85102dced5.png)

> Image from [official paper](https://arxiv.org/abs/1506.02640)

### Other Algorithms

* RetinaNet: [official paper](https://arxiv.org/abs/1708.02002)
   - [PyTorch Implementation in Torchvision](https://pytorch.org/vision/stable/_modules/torchvision/models/detection/retinanet.html)
   - [Keras Implementation](https://github.com/fizyr/keras-retinanet)
   - [Object Detection with RetinaNet](https://keras.io/examples/vision/retinanet/) in Keras Samples
* SSD (Single Shot Detector): [official paper](https://arxiv.org/abs/1512.02325)

## ✍️ Exercises: Object Detection

Continue your learning in the following notebook:

[ObjectDetection.ipynb](ObjectDetection.ipynb)

## Conclusion

In this lesson, you explored a variety of approaches to object detection!

## 🚀 Challenge

Explore these articles and notebooks about YOLO and try implementing them:

* [Good blog post](https://www.analyticsvidhya.com/blog/2018/12/practical-guide-object-detection-yolo-framewor-python/) describing YOLO
* [Official site](https://pjreddie.com/darknet/yolo/)
* YOLO: [Keras implementation](https://github.com/experiencor/keras-yolo2), [step-by-step notebook](https://github.com/experiencor/basic-yolo-keras/blob/master/Yolo%20Step-by-Step.ipynb)
* YOLO v2: [Keras implementation](https://github.com/experiencor/keras-yolo2), [step-by-step notebook](https://github.com/experiencor/keras-yolo2/blob/master/Yolo%20Step-by-Step.ipynb)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/22)

## Review & Self Study

* [Object Detection](https://tjmachinelearning.com/lectures/1718/obj/) by Nikhil Sardana
* [A good comparison of object detection algorithms](https://lilianweng.github.io/lil-log/2018/12/27/object-detection-part-4.html)
* [Review of Deep Learning Algorithms for Object Detection](https://medium.com/comet-app/review-of-deep-learning-algorithms-for-object-detection-c1f3d437b852)
* [A Step-by-Step Introduction to the Basic Object Detection Algorithms](https://www.analyticsvidhya.com/blog/2018/10/a-step-by-step-introduction-to-the-basic-object-detection-algorithms-part-1/)
* [Implementation of Faster R-CNN in Python for Object Detection](https://www.analyticsvidhya.com/blog/2018/11/implementation-faster-r-cnn-python-object-detection/)

## [Assignment: Object Detection](lab/README.md)

---

