# Tricks for Training Deep Learning Models

As neural networks grow deeper, training them becomes increasingly challenging. A significant issue is the so-called [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) or [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [This article](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) provides a solid introduction to these challenges.

To enhance the efficiency of training deep networks, several techniques can be employed.

## Maintaining Values within a Reasonable Range

To ensure more stable numerical computations, it is essential to keep all values within our neural network at a reasonable scale, typically in the range of [-1..1] or [0..1]. While this is not a strict requirement, the nature of floating-point calculations means that values of vastly different magnitudes cannot be accurately processed together. For instance, if we add 10<sup>-10</sup> and 10<sup>10</sup>, the result will likely be 10<sup>10</sup>, as the smaller value gets "converted" to match the order of the larger one, resulting in the loss of precision in the mantissa.

Most activation functions exhibit non-linearities around [-1..1], making it sensible to scale all input data to fall within this range.

## Initial Weight Initialization

Ideally, we want the values to remain within the same range after passing through the layers of the network. Therefore, it is crucial to initialize weights in a way that preserves the distribution of values.

Using a normal distribution **N(0,1)** is not advisable, as having *n* inputs would result in an output standard deviation of *n*, causing values to likely exceed the [0..1] range.

The following initialization methods are commonly used:

 * Uniform distribution -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** guarantees that for inputs with a zero mean and a standard deviation of 1, the same mean/standard deviation will be maintained
 * **N(0,√2/(n_in+n_out))** -- known as **Xavier initialization** (`glorot`), this helps keep the signals within range during both forward and backward propagation

## Batch Normalization

Even with proper weight initialization, weights can become arbitrarily large or small during training, leading to signals being pushed out of the appropriate range. We can bring the signals back within range by employing one of the normalization techniques. While several methods exist (Weight normalization, Layer Normalization), the most commonly used is Batch Normalization.

The concept of **batch normalization** involves taking into account all values across the minibatch and performing normalization (i.e., subtracting the mean and dividing by the standard deviation) based on these values. This is implemented as a network layer that applies normalization after the weights but before the activation function. Consequently, we are likely to achieve higher final accuracy and faster training.

Here is the [original paper](https://arxiv.org/pdf/1502.03167.pdf) on batch normalization, along with an [explanation on Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization) and [a useful introductory blog post](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (and the one [in Russian](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** is a fascinating technique that randomly removes a certain percentage of neurons during training. It is also implemented as a layer with a single parameter (the percentage of neurons to drop, typically between 10% and 50%), and during training, it zeroes out random elements of the input vector before passing it to the next layer.

While this may sound unconventional, you can observe the impact of dropout on training an MNIST digit classifier in [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb). It accelerates training and enables us to achieve higher accuracy in fewer training epochs.

This phenomenon can be explained in various ways:

 * It can be viewed as a random perturbation to the model, which helps to escape local minima during optimization.
 * It can also be seen as *implicit model averaging*, since during dropout, we are effectively training slightly different models.

> *Some people suggest that when a person under the influence of alcohol attempts to learn something, they may remember it better the next day compared to a sober person, as the brain with some impaired neurons tries to adapt more effectively to grasp the meaning. We have never tested this theory ourselves.*

## Preventing Overfitting

A critical aspect of deep learning is the ability to prevent [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). While it may be tempting to employ a highly powerful neural network model, we should always balance the number of model parameters with the number of training samples.

> Ensure you grasp the concept of [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) that we discussed earlier!

Several strategies can help prevent overfitting:

 * Early stopping -- continuously monitor the error on the validation set and halt training when the validation error begins to rise.
 * Explicit Weight Decay / Regularization -- adding an extra penalty to the loss function for high absolute weight values, preventing the model from producing highly unstable results.
 * Model Averaging -- training multiple models and then averaging their results. This helps minimize variance.
 * Dropout (Implicit Model Averaging)

## Optimizers / Training Algorithms

Another vital aspect of training is selecting a suitable training algorithm. While classical **gradient descent** is a reasonable option, it can sometimes be too slow or lead to other issues.

In deep learning, we employ **Stochastic Gradient Descent** (SGD), which applies gradient descent to minibatches randomly selected from the training set. Weights are adjusted using the following formula:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

In **momentum SGD**, we retain a portion of the gradient from previous steps. This is akin to moving with inertia; if we are struck from a different direction, our trajectory doesn't change instantly but retains some aspect of the original motion. Here, we introduce another vector v to represent the *speed*:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup> + v<sup>t+1</sup>

Here, the parameter γ indicates the degree to which we consider inertia: γ=0 corresponds to classical SGD; γ=1 represents a pure motion equation.

### Adam, Adagrad, etc.

Since in each layer we multiply signals by some matrix W<sub>i</sub>, depending on ||W<sub>i</sub>||, the gradient can either diminish and approach 0 or increase indefinitely. This encapsulates the essence of the Exploding/Vanishing Gradients problem.

One solution to this issue is to use only the direction of the gradient in the equation and disregard the absolute value, i.e.,

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), where ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

This algorithm is known as **Adagrad**. Other algorithms that utilize the same concept include **RMSProp** and **Adam**.

> **Adam** is regarded as a highly efficient algorithm for many applications, so if you're uncertain about which one to use, opt for Adam.

### Gradient Clipping

Gradient clipping extends the idea mentioned above. When ||∇ℒ|| ≤ θ, we consider the original gradient in weight optimization; when ||∇ℒ|| > θ, we divide the gradient by its norm. Here, θ is a parameter, and in most cases, we can set θ=1 or θ=10.

### Learning Rate Decay

The success of training often hinges on the learning rate parameter η. It is logical to assume that larger values of η lead to faster training, which is typically desirable at the beginning of the training process, while smaller values of η allow for fine-tuning the network later. Thus, in most cases, we aim to reduce η as training progresses.

This can be achieved by multiplying η by a certain factor (e.g., 0.98) after each training epoch or by implementing a more complex **learning rate schedule**.

## Various Network Architectures

Choosing the right network architecture for your problem can be challenging. Typically, we would select an architecture that has proven effective for our specific task (or a similar one). Here is a [good overview](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) of neural network architectures for computer vision.

> It is crucial to choose an architecture that is sufficiently powerful for the number of training samples available. Opting for an excessively powerful model can lead to [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Another effective approach is to use an architecture that automatically adapts to the required complexity. To some extent, **ResNet** and **Inception** architectures are self-adjusting. [More on computer vision architectures](../07-ConvNets/CNN_Architectures.md).

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.