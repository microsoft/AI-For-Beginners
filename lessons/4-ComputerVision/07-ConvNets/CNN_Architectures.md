# Well-Known CNN Architectures

### VGG-16

VGG-16 is a network that achieved 92.7% accuracy in ImageNet top-5 classification in 2014. It has the following layer structure:

![ImageNet Layers](images/vgg-16-arch1.jpg)

As you can see, VGG follows a traditional pyramid architecture, which is a sequence of convolution-pooling layers.

![ImageNet Pyramid](images/vgg-16-arch.jpg)

> Image from [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet is a family of models proposed by Microsoft Research in 2015. The main idea of ResNet is to use **residual blocks**:

<img src="images/resnet-block.png" width="300"/>

> Image from [this paper](https://arxiv.org/pdf/1512.03385.pdf)

The reason for using identity pass-through is to have our layer predict **the difference** between the result of a previous layer and the output of the residual block - hence the name *residual*. Those blocks are much easier to train, and one can construct networks with several hundreds of those blocks (most common variants are ResNet-52, ResNet-101 and ResNet-152).

You can also think of this network as being able to adjust its complexity to the dataset. Initially, when you are starting to train the network, the weights values are small, and most of the signal goes through passthrough identity layers. As training progresses and weights become larger, the significance of network parameters grow, and the networks adjusts to accommodate required expressive power to correctly classify training images.

### Google Inception

Google Inception architecture takes this idea one step further, and builds each network layer as a combination of several different paths:

<img src="images/inception.png" width="400"/>

> Image from [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Here, we need to emphasize the role of 1x1 convolutions, because at first they do not make sense. Why would we need to run through the image with 1x1 filter? However, you need to remember that convolution filters also work with several depth channels (originally - RGB colors, in subsequent layers - channels for different filters), and 1x1 convolution is used to mix those input channels together using different trainable weights. It can be also viewed as downsampling (pooling) over channel dimension.

Here is [a good blog post](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) on the subject, and [the original paper](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

MobileNet is a family of models with reduced size, suitable for mobile devices. Use them if you are short in resources, and can sacrifice a little bit of accuracy. The main idea behind them is so-called **depthwise separable convolution**, which allows representing convolution filters by a composition of spatial convolutions and 1x1 convolution over depth channels. This significantly reduces the number of parameters, making the network smaller in size, and also easier to train with less data.

Here is [a good blog post on MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Conclusion

In this unit, you have learned the main concept behind computer vision neural networks - convolutional networks. Real-life architectures that power image classification, object detection, and even image generation networks are all based on CNNs, just with more layers and some additional training tricks.

## 🚀 Challenge

In the accompanying notebooks, there are notes at the bottom about how to obtain greater accuracy. Do some experiments to see if you can achieve higher accuracy.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/207)

## Review & Self Study

While CNNs are most often used for Computer Vision tasks, they are generally good for extracting fixed-sized patterns. For example, if we are dealing with sounds, we may also want to use CNNs to look for some specific patterns in audio signal - in which case filters would be 1-dimensional (and this CNN would be called 1D-CNN). Also, sometimes 3D-CNN is used to extract features in multi-dimensional space, such as certain events occurring on video - CNN can capture certain patterns of feature changing over time. Do some review and self-study about other tasks that can be done with CNNs.

## [Assignment](lab/README.md)

In this lab, you are tasked with classifying different cat and dog breeds. These images are more complex than the MNIST dataset and of higher dimensions, and there are more than 10 classes.