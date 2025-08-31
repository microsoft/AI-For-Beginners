<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-31T17:42:23+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "en"
}
-->
# Segmentation

We previously explored Object Detection, which helps identify objects in an image by predicting their *bounding boxes*. However, for certain tasks, bounding boxes alone aren't enough—we need more precise object localization. This task is known as **segmentation**.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

Segmentation can be thought of as **pixel classification**, where we predict the class of **each** pixel in the image (*background* being one of the classes). There are two main types of segmentation algorithms:

* **Semantic segmentation** identifies the class of each pixel but does not differentiate between individual objects of the same class.
* **Instance segmentation** separates objects of the same class into distinct instances.

For example, in instance segmentation, each sheep is treated as a separate object, whereas in semantic segmentation, all sheep are grouped into a single class.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Image from [this blog post](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

There are various neural network architectures for segmentation, but they all share a similar structure. In some ways, they resemble the autoencoder you learned about earlier, but instead of reconstructing the original image, the goal is to reconstruct a **mask**. A segmentation network typically consists of the following components:

* **Encoder**: Extracts features from the input image.
* **Decoder**: Converts those features into the **mask image**, which has the same dimensions as the input image, with the number of channels corresponding to the number of classes.

<img src="images/segm.png" width="80%">

> Image from [this publication](https://arxiv.org/pdf/2001.05566.pdf)

A key aspect to highlight is the loss function used for segmentation. In classical autoencoders, we measure the similarity between two images, often using mean square error (MSE). In segmentation, however, each pixel in the target mask image represents a class number (one-hot-encoded along the third dimension). Therefore, we use classification-specific loss functions, such as cross-entropy loss, averaged across all pixels. For binary masks, **binary cross-entropy loss** (BCE) is applied.

> ✅ One-hot encoding is a method for converting a class label into a vector with a length equal to the number of classes. Check out [this article](https://datagy.io/sklearn-one-hot-encode/) for more details on this technique.

## Segmentation for Medical Imaging

In this lesson, we'll see segmentation in action by training a network to identify human nevi (commonly known as moles) in medical images. We'll use the <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> Database</a> of dermoscopy images as our dataset. This dataset contains 200 images divided into three classes: typical nevus, atypical nevus, and melanoma. Each image is accompanied by a corresponding **mask** that outlines the nevus.

> ✅ This technique is particularly well-suited for medical imaging, but what other real-world applications can you think of?

<img alt="navi" src="images/navi.png"/>

> Image from the PH<sup>2</sup> Database

Our goal will be to train a model to segment any nevus from its background.

## ✍️ Exercises: Semantic Segmentation

Explore the notebooks below to learn more about different semantic segmentation architectures, practice using them, and see them in action.

* [Semantic Segmentation Pytorch](SemanticSegmentationPytorch.ipynb)
* [Semantic Segmentation TensorFlow](SemanticSegmentationTF.ipynb)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Conclusion

Segmentation is a powerful image classification technique that goes beyond bounding boxes to classify at the pixel level. It has applications in medical imaging and many other fields.

## 🚀 Challenge

Body segmentation is just one of the many tasks we can perform with images of people. Other important tasks include **skeleton detection** and **pose detection**. Try out the [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) library to explore pose detection in action.

## Review & Self Study

This [Wikipedia article](https://wikipedia.org/wiki/Image_segmentation) provides a good overview of the various applications of segmentation. Dive deeper into the subdomains of Instance segmentation and Panoptic segmentation to expand your understanding.

## [Assignment](lab/README.md)

In this lab, experiment with **human body segmentation** using the [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) available on Kaggle.

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.