# Deep Learning Training Tricks

As neural networks become deeper, the process of their training becomes more and more challenging. One major problem is so-called [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) or [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [This post](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) gives a good introduction into those problems.

To make training deep networks more efficient, there are a few techniques that can be used.

## Keeping values in reasonable interval

To make numerical computations more stable, we want to make sure that all values within our neural network are within reasonable scale, typically [-1..1] or [0..1]. It is not a very strict requirement, but the nature of floating point computations is such that values of different magnitudes cannot be accurately manipulated together. For example, if we add 10<sup>-10</sup> and 10<sup>10</sup>, we are likely to get 10<sup>10</sup>, because smaller value would be "converted" to the same order as the larger one, and thus mantissa would be lost.

Most activation functions have non-linearities around [-1..1], and thus it makes sense to scale all input data to [-1..1] or [0..1] interval.

## Initial Weight Initialization

Ideally, we want the values to be in the same range after passing through network layers. Thus it is important to initialize weights in such a way as to preserve the distribution of values.

Normal distribution **N(0,1)** is not a good idea, because if we have *n* inputs, the standard deviation of output would be *n*, and values are likely to jump out of [0..1] interval.

The following initializations are often used:

 * Uniform distribution -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** guarantees that for inputs with zero mean and standard deviation of 1 the same mean/standard deviation would remain
 * **N(0,&radic;2/(n_in+n_out))** -- so-called **Xavier initialization** (`glorot`), it helps to keep the signals in range during both forward and backward propagation

## Batch Normalization

Even with proper weight initialization, weights can get arbitrary big or small during the training, and they will bring signals out of proper range. We can bring signals back by using one of **normalization** techniques. While there are several of them (Weight normalization, Layer Normalization), the most often used is Batch Normalization.

The idea of **batch normalization** is to take into account all values across the minibatch, and perform normalization (i.e. subtract mean and divide by standard deviation) based on those values. It is implemented as a network layer that does this normalization after applying the weights, but before activation function. As a result, we are likely to see higher final accuracy and faster training.

Here is the [original paper](https://arxiv.org/pdf/1502.03167.pdf) on batch normalization, the [explanation on Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), and [a good introductory blog post](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (and the one [in Russian](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** is an interesting technique that removes a certain percentage of random neurons during training. It is also implemented as a layer with one parameter (percentage of neurons to remove, typically 10%-50%), and during training it zeroes random elements of the input vector, before passing it to the next layer.

While this may sound like a strange idea, you can see the effect of dropout on training MNIST digit classifier in [`Dropout.ipynb`](Dropout.ipynb) notebook. It speeds up training and allows us to achieve higher accuracy in less training epochs.

This effect can be explained in several ways:

 * It can be considered to be a random shocking factor to the model, which takes optimiation out of local minimum
 * It can be considered as *implicit model averaging*, because we can say that during dropout we are training slightly different model

> *Some people say that when a drunk person tries to learn something, he will remember this better next morning, comparing to a sober person, because a brain with some malfunctioning neurons tries to adapt better to gasp the meaning. We never tested ourselves if this is true of not*

## Preventing overfitting

One of the very important aspect of deep learning is too be able to prevent [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). While it might be tempting to use very powerful neural network model, we should always balance the number of model parameters with the number of training samples.

> Make sure you understand the concept of [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) we have introduced earlier!

There are several ways to prevent overfitting:

 * Early stopping -- continuously monitor error on validation set and stopping training when validation error starts to increase.
 * Explicit Weight Decay / Regularization -- adding an extra penalty to the loss function for high absolute values of weights, which prevents the model of getting very unstable results
 * Model Averaging -- training several models and then averaging the result. This helps to minimize the variance.
 * Dropout (Implicit Model Averaging)

## Optimizers / Training Algorithms

Another important aspect of training is to chose good training algorithm. While classical **gradient descent** is a reasonable choice, it can sometimes be too slow, or result in other problems.

In deep learning, we use **Stochastic Gradient Descent** (SGD), which is a gradient descent applied to minibatches, randomly selected from the training set. Weights are adjusted using this formula:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

In **momentum SGD**, we are keeping a portion of a gradient from previous steps. It is similar to when we are moving somewhere with inertia, and we receive a punch in a different direction, our trajectory does not change immediately, but keeps some part of the original movement. Here we introduce another vector v to represent the *speed*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Here parameter &gamma; indicates the extent to which we take inertia into account: &gamma;=0 corresponds to classical SGD; &gamma;=1 is a pure motion equation.

### Adam, Adagrad, etc.

Since in each layer we multiply signals by some matrix W<sub>i</sub>, depending on ||W<sub>i</sub>||, the gradient can either diminish and be close to 0, or rise indefinitely. It is the essence of Exploding/Vanishing Gradients problem.

One of the solutions to this problem is to use only direction of the gradient in the equation, and ignore the absolute value, i.e.

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), where ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

This algorithm is called **Adagrad**. Another algorithms that use the same idea: **RMSProp**, **Adam**

> **Adam** is considered to be a very efficient algorithm for many applications, so if you are not sure which one to use - use Adam.

### Gradient clipping

Gradient clipping is an extension the idea above. When the ||&nabla;&lagran;|| &le; &theta;, we consider the original gradient in the weight optimization, and when ||&nabla;&lagran;|| > &theta; - we divide the gradient by it's norm. Here &theta; is a parameter, in most cases we can take &theta;=1 or &theta;=10.

### Learning rate decay

Training success often depends on the learning rate parameter &eta;. It is logical to assume that larger values of &eta; result in faster training, which is something we typically want in the beginning of the training, and then smaller value of &eta; allow us to fine-tune the network. Thus, in most of the cases we want to decrease &eta; in the process of the training.

This can be done by multiplying &eta; by some number (eg. 0.98) after each epoch of the training, or by using more complicated **learning rate schedule**.

## Different Network Architectures

Selecting right network architecture for your problem can be tricky. Normally, we would take an architecture that has proven to work for our specific task (or similar one). Here is a [good overview](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) or neural network architectures for computer vision.

> It is important to select an architecture that will be powerful enough for the number of training samples that we have. Selecting too powerful model can result in [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Another good way would be to use and architecture that will automatically adjust to the required complexity. To some extent, **ResNet** architecture and **Inception** are self-adjusting. [More on computer vision architectures](../07-ConvNets/CNN_Architectures.md)
