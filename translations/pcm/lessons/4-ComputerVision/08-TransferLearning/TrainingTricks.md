# Deep Learning Training Tricks

As neural networks dey go deeper, di training process dey become more hard. One big problem na wetin dem dey call [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) or [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Dis post](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) give better introduction to dis kain problems.

To make training deep networks better, some beta techniques dey wey fit use.

## Keeping values for correct range

To make numerical computation steady, we want make sure say all values inside our neural network dey inside correct size, normally na [-1..1] or [0..1]. E no be strict rule, but the way floating point computations be, values wey big different no fit join well. Like if we add 10<sup>-10</sup> and 10<sup>10</sup>, e go likely become 10<sup>10</sup>, because the small value go "convert" to the same size as the big one, so the small part for number go loss.

Most activation functions get non-linearities near [-1..1], so e make sense to scale all input data to [-1..1] or [0..1].

## Initial Weight Initialization

Ideally, we want values to stay for the same range after dem pass through network layers. So e important to initialize weights in a way wey go keep the distribution of values.

Normal distribution **N(0,1)** no good idea, because if we get *n* inputs, the standard deviation of output na *&radic;n*, and values fit jump out from [0..1].

These initializations dey commonly use:

 * Uniform distribution -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** mean say if inputs get zero mean and standard deviation of 1, the same mean/standard deviation go still dey
 * **N(0,&radic;2/(n_in+n_out))** -- na wetin dem dey call **Xavier initialization** (`glorot`), e help keep signals inside range during both forward and backward propagation

## Batch Normalization

Even with correct weight initialization, weights fit become any how big or small during training, and dem fit make signals go out of proper range. We fit bring signals back by using one of **normalization** techniques. Plenty normalizations dey like Weight normalization, Layer Normalization, but Batch Normalization na di one wey people dey use pass.

The idea for **batch normalization** na to check all values across the minibatch, and do normalization (subtract mean and divide by standard deviation) based on those values. E dey as network layer to do normalization after weight apply, but before activation function. Because of that, training accuracy fit be higher and training go fast.

Here be the [original paper](https://arxiv.org/pdf/1502.03167.pdf) on batch normalization, the [explanation for Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), and [a good introductory blog post](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (and the one [for Russian](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** na beta technique wey dey remove some percent random neurons during training. E also be layer with one parameter (percent of neurons to remove, normally 10%-50%), and during training e zero random input vector parts before e pass am go next layer.

E fit sound like strange idea, but you fit see how dropout affect training MNIST digit classifier for [`Dropout.ipynb`](Dropout.ipynb) notebook. E dey speed up training and make us get better accuracy in fewer training epochs.

This effect fit explain like dis:

 * E fit be like random shock factor to model, wey fit carry optimization comot for local minimum
 * E fit be like *implicit model averaging*, because during dropout we dey train slightly different model

> *Some people talk say if drunk person try learn something, e go remember am better next morning pass sober person, because brain wey get some faulty neurons dey try adapt well to understand wetin dey happen. We no test if dis one true or no*

## Preventing overfitting

One important side for deep learning na to fit prevent [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Even though e fit sweet to use strong neural network model, we suppose always balance number of model parameters with how many training samples we get.

> Make sure say you sabi the concept of [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) we mention before!

Ways to prevent overfitting dey:

 * Early stopping -- dey check error for validation set continuously and stop training when validation error start increase.
 * Explicit Weight Decay / Regularization -- dey add extra punishment to loss function for high absolute weight values, e dey stop model from getting unstable result
 * Model Averaging -- dey train many models, then average results. E help reduce variance.
 * Dropout (Implicit Model Averaging)

## Optimizers / Training Algorithms

Another important thing for training na to choose beta training algorithm. Classical **gradient descent** dey okay, but sometimes e slow or get other wahala.

For deep learning, we use **Stochastic Gradient Descent** (SGD), na gradient descent wey dem apply to minibatches, wey dem randomly select from training set. We dey adjust weights with this formula:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

For **momentum SGD**, we keep small part of gradient from before steps. E be like when we dey move with inertia, but somebody give we punch for different direction, we no change path sharp sharp, but keep some move original movement. Here we put another vector v as *speed*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Parameter &gamma; show how much we consider inertia: &gamma;=0 mean classical SGD; &gamma;=1 na pure motion equation.

### Adam, Adagrad, etc.

Because for each layer we multiply signals by matrix W<sub>i</sub>, based on ||W<sub>i</sub>||, gradient fit either reduce come near 0, or increase without limit. Na di Exploding/Vanishing Gradients wahala.

One solution na to use only direction of gradient, ignore absolute value, like

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), where ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Dis algorithm na **Adagrad**. Another algorithms wey dey use dis idea: **RMSProp**, **Adam**

> **Adam** na beta efficient algorithm for many cases, so if you no sure which one to use - use Adam.

### Gradient clipping

Gradient clipping na extension of the idea wey i talk earlier. When ||&nabla;&lagran;|| &le; &theta;, we dey use original gradient for weight optimization, and if ||&nabla;&lagran;|| > &theta; we go divide gradient by its norm. &theta; na parameter, we fit use &theta;=1 or &theta;=10 for most cases.

### Learning rate decay

Training success dey often depend on learning rate parameter &eta;. E make sense say bigger &eta; mean faster training, wey na wetin we want first for training start, then smaller &eta; go help fine-tune network. So, for most cases we want reduce &eta; as training dey go.

This one fit do by multiplying &eta; by some number (for example 0.98) after each epoch of training, or by using more complex **learning rate schedule**.

## Different Network Architectures

To select correct network architecture for your problem fit hard. Normally, we go use architecture wey don show say e dey work for our specific task (or similar). Here na [good overview](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) of neural network architectures for computer vision.

> E important to select architecture wey strong enough for number of training samples we get. If you select too strong model fit cause [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Another beta way na to use architecture wey go automatically fit the needed complexity. To some extent, **ResNet** architecture and **Inception** dey self-adjusting. [More on computer vision architectures](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->