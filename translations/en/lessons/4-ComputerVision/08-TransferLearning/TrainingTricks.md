<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ae074cd940fc2f4dc24fc07b66ccbd99",
  "translation_date": "2025-08-31T17:37:47+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md",
  "language_code": "en"
}
-->
# Deep Learning Training Tricks

As neural networks grow deeper, training them becomes increasingly challenging. One major issue is the [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) or [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [This post](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) provides a good introduction to these problems.

To make training deep networks more efficient, several techniques can be applied.

## Keeping values within a reasonable range

To ensure numerical computations are stable, it's important to keep all values within the neural network at a reasonable scale, typically [-1..1] or [0..1]. While this isn't a strict requirement, the nature of floating-point computations makes it difficult to accurately manipulate values of vastly different magnitudes. For instance, adding 10<sup>-10</sup> and 10<sup>10</sup> will likely result in 10<sup>10</sup>, as the smaller value gets "converted" to the same order as the larger one, losing its mantissa.

Most activation functions exhibit non-linearities around [-1..1], so scaling all input data to the [-1..1] or [0..1] range is often a good idea.

## Initial Weight Initialization

Ideally, values should remain within the same range as they pass through network layers. Therefore, initializing weights in a way that preserves the distribution of values is crucial.

Using a normal distribution **N(0,1)** is not ideal because, with *n* inputs, the standard deviation of the output would be *n*, causing values to likely exceed the [0..1] range.

Common initialization methods include:

- Uniform distribution — `uniform`
- **N(0,1/n)** — `gaussian`
- **N(0,1/√n_in)** ensures that inputs with zero mean and a standard deviation of 1 retain the same mean and standard deviation.
- **N(0,√2/(n_in+n_out))** — known as **Xavier initialization** (`glorot`), which helps keep signals within range during both forward and backward propagation.

## Batch Normalization

Even with proper weight initialization, weights can grow arbitrarily large or small during training, pushing signals out of the desired range. Normalization techniques can bring signals back into range. While there are several methods (e.g., Weight Normalization, Layer Normalization), **Batch Normalization** is the most commonly used.

The idea behind **batch normalization** is to normalize values across the minibatch (subtracting the mean and dividing by the standard deviation). This is implemented as a network layer that performs normalization after applying weights but before the activation function. Batch normalization often results in faster training and higher final accuracy.

Here are the [original paper](https://arxiv.org/pdf/1502.03167.pdf) on batch normalization, the [Wikipedia explanation](https://en.wikipedia.org/wiki/Batch_normalization), and [a helpful blog post](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (and one [in Russian](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** is a technique that randomly removes a percentage of neurons during training. Implemented as a layer with one parameter (the percentage of neurons to remove, typically 10%-50%), dropout zeroes out random elements of the input vector before passing it to the next layer.

Although it may seem counterintuitive, dropout can speed up training and achieve higher accuracy in fewer epochs. You can observe its effect on training a MNIST digit classifier in the [`Dropout.ipynb`](Dropout.ipynb) notebook.

This effect can be explained in several ways:

- It acts as a random shock to the model, helping it escape local minima.
- It serves as *implicit model averaging*, as dropout essentially trains slightly different models.

> *Some people claim that when a drunk person tries to learn something, they remember it better the next morning compared to a sober person, as their brain adapts to compensate for malfunctioning neurons. We haven't tested this ourselves.*

## Preventing overfitting

Preventing [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) is a critical aspect of deep learning. While it may be tempting to use a highly powerful neural network model, it's essential to balance the number of model parameters with the number of training samples.

> Make sure you understand the concept of [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) introduced earlier!

Ways to prevent overfitting include:

- Early stopping — monitoring validation error and stopping training when it starts to increase.
- Explicit Weight Decay / Regularization — adding a penalty to the loss function for large weight values to prevent instability.
- Model Averaging — training multiple models and averaging their results to reduce variance.
- Dropout (Implicit Model Averaging)

## Optimizers / Training Algorithms

Choosing the right training algorithm is another key aspect of training. While classical **gradient descent** is a reasonable choice, it can sometimes be slow or lead to other issues.

In deep learning, **Stochastic Gradient Descent** (SGD) is commonly used. It applies gradient descent to minibatches randomly selected from the training set. Weights are updated using the formula:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

In **momentum SGD**, a portion of the gradient from previous steps is retained, similar to inertia. If you receive a push in a different direction, your trajectory doesn't change immediately but retains some of the original movement. Here, a vector *v* represents the "speed":

- v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
- w<sup>t+1</sup> = w<sup>t</sup> + v<sup>t+1</sup>

The parameter γ determines how much inertia is considered: γ=0 corresponds to classical SGD, while γ=1 represents pure motion.

### Adam, Adagrad, etc.

In each layer, signals are multiplied by a matrix W<sub>i</sub>. Depending on ||W<sub>i</sub>||, the gradient can either diminish to near zero or grow indefinitely, leading to the Exploding/Vanishing Gradients problem.

One solution is to use only the gradient's direction in the equation, ignoring its magnitude:

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), where ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

This algorithm is called **Adagrad**. Other algorithms using similar ideas include **RMSProp** and **Adam**.

> **Adam** is widely regarded as an efficient algorithm for many applications. If you're unsure which optimizer to use, start with Adam.

### Gradient clipping

Gradient clipping extends the idea above. When ||∇ℒ|| ≤ θ, the original gradient is used for weight optimization. When ||∇ℒ|| > θ, the gradient is divided by its norm. The parameter θ is typically set to 1 or 10.

### Learning rate decay

The learning rate parameter η significantly impacts training success. Larger values of η can speed up training early on, while smaller values allow for fine-tuning later. Thus, it's common to decrease η during training.

This can be achieved by multiplying η by a factor (e.g., 0.98) after each epoch or using a more complex **learning rate schedule**.

## Different Network Architectures

Choosing the right network architecture for your problem can be challenging. Typically, you would select an architecture proven to work for your specific task (or a similar one). Here's a [helpful overview](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) of neural network architectures for computer vision.

> It's important to choose an architecture powerful enough for the number of training samples available. Selecting an overly powerful model can lead to [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Another option is to use architectures that automatically adjust to the required complexity. To some extent, **ResNet** and **Inception** architectures are self-adjusting. [Learn more about computer vision architectures](../07-ConvNets/CNN_Architectures.md).

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.