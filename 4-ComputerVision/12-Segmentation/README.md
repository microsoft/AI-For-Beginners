# Segmentation

We have already learnt about Object Detection, which allows us to locate objects in the image by predicting their *bounding boxes*. However, for some tasks we do not only need bounding boxes, but also more precise object localization. This task is called  **segmentation**.

Segmentation can be viewed as **pixel classification**, whereas for **each** pixel of image we must predict its class (*background* being one of the classes). There are two main segmentation algorithms:

* **Semantic segmentation** only tells pixel class, and does not make a distinction between different objects of the same class
* **Instance segmentation** divides classes into different instances. 

For instance segmentation 10 sheep are different objects, for semantic segmentation all sheep are represented by one class.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Image from [this blog post](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

There are different neural architectures for segmentation, but they all have the same structure. In a way, it is similar to autoencoder, but instead of deconstructing the original image, our goal is to deconstruct a **mask**. Thus, segmentation network has the following parts:

* **Encoder** extracts features from input image
* **Decoder** transforms those features into the **mask image**, with the same size and number of channels corresponding to the number of classes.

<img src="images/segm.png" width="80%">

> Image from [this publication](https://arxiv.org/pdf/2001.05566.pdf)

We should especially mention the loss function that is used for segmentation. In classical autoencoders we need to measure the similarity between two images, and we can use mean square error to do that. In segmentation, each pixel in the target mask image represents the class number (one-hot-encoded along the third dimension), so we need to use loss functions specific for classification - cross-entropy loss, averaged over all pixels. If the mask is binary - **binary cross-entropy loss** (BCE) is used.   

## Segmentation for Medical Imaging

In this lesson, we will see the segmentation in action by training the network to recognize human nevi on the medical images. We will be using <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> Database</a> of dermoscopy images. This dataset contains 200 images of three classes: typical nevus, atypical nevus, and melanoma. All images also contain corresponding **mask** that outline the nevus.

<img src="images/navi.png"/>

We will train a model to segment any nevus from the background.

## Notebooks

Open [the notebook](SemanticSegmentationPytorch.ipynb) to learn more about different semantic segmentation architectures and see them in action. 

## [Lab](lab/README.md)

In this lab, we encourage you to try ** human body segmentation** using [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) from Kaggle.

## Assignment

Body segmentation is just one of the common tasks that we can do with images of people. Another important tasks include **skeleton detection** and **pose detection**. Try out [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) library to see how pose detection can be used.

