# Convolutional Neural Networks

We have seen before that neural networks are quite good at dealing with images, and even one-layer perceptron is able to recognize handwritten digits from MNIST dataset with reasonable accuracy. However, MNIST dataset is very special, and all digits are centered inside the image, which makes the task simpler.

In real life, we want to be able to recognize objects on the picture regardless of their exact location in the image. Computer vision is different from generic classification, because when we are trying to find a certain object in the picture, we are scanning the image looking for some specific **patterns** and their combinations. For example, when looking for a cat, we first may look for horizontal lines, which can form whiskers, and then certain combination of whiskers can tell us that it is actually a picture of a cat. Relative position and presence of certain patterns is important, and not their exact position on the image. 

To extract patterns, we will use the notion of **convolutional filters**. As you know, an image is represented by a 2D-matrix, or 3D-tensor with color depth. Applying a filter means that we take relatively small **filter kernel** matrix, and for each pixel in the original image we compute the weighted average with neighboring points. We can view this like a small window sliding over the whole image, and averaging out all pixels according to the weights in the filter kernel matrix.

![Vertical Edge Filter](images/filter-vert.png) | ![Horizontal Edge Filter](images/filter-horiz.png)
----|----

For example, if we apply 3x3 vertical edge and horizontal edge filters to the MNIST digits, we can get highlights (e.g. high values) where there are vertical and horizontal edges in our original image. Thus those two filters can be used to "look for" edges. Similarly, we can design different filters to look for other low-level patterns:

<img src="images/lmfilters.jpg" width="500" align="center"/>

> Image of Leung-Malik Filter Bank, from [here](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

However, while we can design the filters to extract some patterns manually, we can also design the network in such a way that it will learn the patterns automatically. It is one of the main ideas behind the CNN.

## Main ideas behind CNN

The way CNNs work is based on the following important ideas:
* Convolutional filters can extract patterns
* We can design the network in such a way that filters are trained automatically
* We can use the same approach to find patterns in high-level features, not only in the original image. Thus CNN feature extraction work on a hierarchy of features, starting from low-level pixel combinations, up to higher level combination of picture parts.

![Hierarchical Feature Extraction](images/FeatureExtractionCNN.png)

> Image from [this paper](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), based on [this research](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## Continue in Notebook

Let's continue exploring how convolutional neural networks work, and how we can achieve trainable filters, in corresponding notebooks:

* [Convolutional Neural Networks - PyTorch](ConvNetsPyTorch.ipynb)
* [Convolutional Neural Networks - TensorFlow](ConvNetsTF.ipynb)

## Pyramid Architecture

Most of CNNs used for image processing follow so-called pyramid architecture. First convolutional layer applied to the original images typically has relatively low number of filters (8-16), which correspond to different pixel combinations, such as horizontal/vertical lines of strokes. At the next level, we reduce the spatial dimension of the network, and increase the number of filters, which corresponds to more possible combinations of simple features. With each layer, as we move towards the final classifier, spatial dimensions of the image decrease, and the number of filters grow.

As an example, let's look at the architecture of VGG-16, a network that achieved 92.7% accuracy in ImageNet top-5 classification in 2014:

![ImageNet Layers](images/vgg-16-arch1.jpg)

![ImageNet Pyramid](images/vgg-16-arch.jpg)

> Image from [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

[**Often Used CNN Architectures**](CNN_Architectures.md)

## [Lab](lab/README.md)

In the lab, you are tasked with classification of different cats and dogs breeds. Images are more complex than MNIST dataset and of higher dimensions, and there are more than 10 classes.
## CNNs for Other Tasks

While CNNs are most often used for Computer Vision tasks, they are generally good for extracting fix-sized patterns. For example, if we are dealing with sounds, we may also want to use CNNs to look for some specific patterns in audio signal - in which case filters would be 1-dimensional (and this CNN would be called 1D-CNN). Also, sometimes 3D-CNN is used to extract features in multi-dimensional space, such as certain events occurring on video - CNN can capture certain patterns of feature changing over time. 
