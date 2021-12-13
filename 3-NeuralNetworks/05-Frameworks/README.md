# Neural Network Frameworks

As we have learnt already, to be able to train neural networks efficiently we need to do two things:

* To operate on tensors, eg. to multiply, add, and compute some functions such as sigmoid or softmax
* To compute gradients of all expressions, in order to perform gradient descent optimization

While `numpy` library can do the first part, we need some mechanism to compute gradients. In [our framework](../04-OwnFramework/OwnFramework.ipynb) that we have developed in the previous section we had to manually program all derivative functions inside the `backward` method, which does back propagation. Ideally, a framework should give us the opportunity to compute gradients of *any  expression* that we can define.

Another important thing is to be able to perform computations on GPU, or any other specialized compute units, such as [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). Deep neural network training requires *a lot* of computations, and to be able to parallelize those computations on GPUs is very important.

Currently, there are two most popular neural frameworks: [Tensorflow](http://tensorflow.org), and [PyTorch](https://pytorch.org/). Both provide low-level API to operate with tensors on both CPU and GPU. On top of the low-level API, there is also higher-level API, called [Keras](https://keras.io/) and [PyTorch Lightning](https://pytorchlightning.ai/) correspondingly.

Low-Level API | [TensorFlow](http://tensorflow.org) | [PyTorch](https://pytorch.org/)
--------------|-------------------------------------|--------------------------------
High-level API| [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**Low-level APIs** in both frameworks allow you to build so-called **computational graph**. This graph defines how to compute the output (usually the loss function) with given input parameters, and can be pushed for computation on GPU, if it is available. There are functions to differentiate this computational graph and compute gradients, which can then be used for optimizing model parameters.

**High-level APIs** pretty much consider neural network as a **sequence of layers**, and make constructing most of the neural networks much easier. Training the model usually requires preparing the data and then calling `fit` function to do the job.

High-level API allows you to construct typical neural networks very fast, without worrying about lots of details. At the same time, low-level API offer much more control over training process, and thus they are used a lot in research, when you are dealing with new neural network architectures. 

It is also important to understand that you can use both APIs together, eg. you can develop your own network layer architecture using low-level API, and then use it inside the larger network constructed and trained with high-level API. Or you can define a network using high-level API as a sequence of layers, and then use your own low-level training loop to perform optimization. Both APIs use the same basic underlying concepts, and they are designed to work well together.

## Learning

In this course, we offer most of the content both for PyTorch and Tensorflow. You can chose your preferred framework and only go through the corresponding notebooks. If you are not sure which framework to chose - read some discussions on the internet regarding **PyTorch vs. Tensorflow**. You can also have a look at both frameworks to get better understanding.

Where possible, we will use High-Level APIs for simplicity. However, we believe it is important to understand how neural networks work from the ground up, thus in the beginning we start by working with low-level API and tensors. However, if you want to get going fast and do not want to spend a lot of time on details, you can skip those, and go straight into high-level API notebooks.

## Continue into Notebooks

Low-Level API | [TensorFlow+Keras Notebook](IntroKerasTF.ipynb) | [PyTorch](IntroPyTorch.ipynb)
--------------|-------------------------------------|--------------------------------
High-level API| [Keras](IntroKeras.ipynb) | *PyTorch Lightning*

