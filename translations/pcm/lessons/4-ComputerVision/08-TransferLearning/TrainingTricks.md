<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ae074cd940fc2f4dc24fc07b66ccbd99",
  "translation_date": "2025-11-18T18:17:33+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/TrainingTricks.md",
  "language_code": "pcm"
}
-->
# Deep Learning Training Tricks

As neural networks dey go deeper, e dey harder to train dem. One big wahala wey fit happen na [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) or [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Dis post](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) explain well well about dis problems.

To make training of deep networks better, some techniques dey wey we fit use.

## Keep values for correct range

To make sure say calculations no go scatter, we go wan make sure say all the values for inside our neural network dey for correct range, like [-1..1] or [0..1]. No be say e dey compulsory like that, but because of how floating point calculations dey work, values wey get different size no dey work well together. For example, if we add 10<sup>-10</sup> and 10<sup>10</sup>, wetin we go get fit be 10<sup>10</sup>, because the smaller value go just disappear.

Most activation functions dey work well for values around [-1..1], so e make sense to scale all input data to [-1..1] or [0..1].

## Initial Weight Initialization

We go like make the values still dey for the same range after dem pass through network layers. So, e dey important to initialize weights in a way wey go keep the values balanced.

Normal distribution **N(0,1)** no too good, because if we get *n* inputs, the standard deviation of output go be *n*, and the values fit jump comot from [0..1].

Dis na some common ways to initialize weights:

 * Uniform distribution -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** go make sure say inputs wey get zero mean and standard deviation of 1 go still maintain the same mean/standard deviation
 * **N(0,&radic;2/(n_in+n_out))** -- dem dey call dis one **Xavier initialization** (`glorot`), e dey help keep signals for correct range during forward and backward propagation

## Batch Normalization

Even if we initialize weights well, weights fit still grow too big or too small during training, and e go scatter the signals. We fit use **normalization** techniques to bring the signals back. Even though we get different types (Weight normalization, Layer Normalization), the one wey people dey use pass na Batch Normalization.

The idea of **batch normalization** na to use all the values for the minibatch, and normalize dem (subtract mean and divide by standard deviation). E dey work as one network layer wey dey normalize after weights don apply, but before activation function. E dey help training go faster and give better accuracy.

Here be the [original paper](https://arxiv.org/pdf/1502.03167.pdf) on batch normalization, the [explanation on Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), and [a good introductory blog post](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (and the one [in Russian](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** na one kind technique wey dey remove some random neurons during training. E dey work as one layer wey get one parameter (percentage of neurons to remove, like 10%-50%), and during training, e go set some random parts of the input vector to zero before e pass am to the next layer.

Even though e fit sound strange, you fit see how dropout dey work for training MNIST digit classifier for [`Dropout.ipynb`](Dropout.ipynb) notebook. E dey make training faster and help us get better accuracy with fewer training epochs.

Dis na why dropout dey work:

 * E fit act like random shock to the model, wey go help am comot from local minimum
 * E fit act like *implicit model averaging*, because during dropout, we dey train small small different models

> *Some people dey talk say if drunk person dey learn something, e go remember am better the next day compared to sober person, because brain wey no dey work well go try adapt better. We never test am sha to know if na true.*

## How to stop overfitting

One big thing for deep learning na how to stop [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Even though e dey sweet to use very powerful neural network model, we suppose balance the number of model parameters with the number of training samples.

> Make sure say you sabi the meaning of [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) wey we don talk about before!

Ways to stop overfitting:

 * Early stopping -- dey check validation error and stop training when validation error begin increase.
 * Explicit Weight Decay / Regularization -- add extra penalty to loss function for weights wey get high values, so the model no go scatter.
 * Model Averaging -- train different models and average the result. E dey reduce variance.
 * Dropout (Implicit Model Averaging)

## Optimizers / Training Algorithms

Another important thing for training na to choose better training algorithm. Even though **gradient descent** dey okay, e fit slow or get other wahala.

For deep learning, we dey use **Stochastic Gradient Descent** (SGD), wey be gradient descent wey dey work on minibatches wey dem pick randomly from training set. Weights dey adjust like this:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

For **momentum SGD**, we dey keep part of the gradient from before. E be like say if person dey waka with speed, and something push am for another direction, e no go change direction immediately. We dey use another vector v to show the *speed*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

The parameter &gamma; dey show how much inertia we go use: &gamma;=0 na normal SGD; &gamma;=1 na pure motion.

### Adam, Adagrad, etc.

For each layer, we dey multiply signals by matrix W<sub>i</sub>. Depending on ||W<sub>i</sub>||, gradient fit reduce to 0 or blow up. Dis na the wahala of Exploding/Vanishing Gradients.

One way to solve dis problem na to use only the direction of the gradient, ignore the size:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), where ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Dis algorithm na **Adagrad**. Other similar algorithms: **RMSProp**, **Adam**

> **Adam** dey work well for many things, so if you no sure which one to use, use Adam.

### Gradient clipping

Gradient clipping na extension of the idea above. If ||&nabla;&lagran;|| &le; &theta;, we go use the original gradient for weight optimization. But if ||&nabla;&lagran;|| > &theta;, we go divide the gradient by e norm. Here &theta; na parameter, most times we fit use &theta;=1 or &theta;=10.

### Learning rate decay

Training success dey depend on learning rate parameter &eta;. Big &eta; fit make training fast for the beginning, but small &eta; fit help fine-tune the network later. So, most times we go wan reduce &eta; as training dey go.

We fit do am by multiplying &eta; by small number (e.g., 0.98) after each epoch, or use more complex **learning rate schedule**.

## Different Network Architectures

To choose correct network architecture for your problem fit hard. Normally, we go use architecture wey don work for similar task before. Here be [good overview](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) of neural network architectures for computer vision.

> E dey important to choose architecture wey go fit the number of training samples wey we get. If the model too powerful, e fit cause [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Another way na to use architecture wey go adjust to the complexity wey we need. **ResNet** and **Inception** dey adjust small small. [More on computer vision architectures](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg make you sabi say automated translations fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di one wey you go take as di correct source. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->