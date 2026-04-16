<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ddd216f558a255260a9374008002c971",
  "translation_date": "2025-09-23T11:51:53+00:00",
  "source_file": "lessons/3-NeuralNetworks/05-Frameworks/README.md",
  "language_code": "en"
}
-->
# Neural Network Frameworks

As we've already learned, to efficiently train neural networks, we need to do two things:

* Work with tensors, such as performing operations like multiplication, addition, and computing functions like sigmoid or softmax.
* Calculate gradients for all expressions to enable gradient descent optimization.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/9)

While the `numpy` library can handle the first task, we need a mechanism to compute gradients. In [our framework](../04-OwnFramework/OwnFramework.ipynb) developed in the previous section, we manually programmed all derivative functions in the `backward` method for backpropagation. Ideally, a framework should allow us to compute gradients for *any expression* we define.

Another critical aspect is the ability to perform computations on GPUs or other specialized hardware like [TPUs](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). Training deep neural networks requires *a lot* of computations, and leveraging GPUs for parallel processing is essential.

> ✅ The term 'parallelize' means distributing computations across multiple devices.

Currently, the two most popular neural network frameworks are [TensorFlow](http://TensorFlow.org) and [PyTorch](https://pytorch.org/). Both provide low-level APIs for working with tensors on CPUs and GPUs. Additionally, they offer high-level APIs, namely [Keras](https://keras.io/) for TensorFlow and [PyTorch Lightning](https://pytorchlightning.ai/) for PyTorch.

Low-Level API | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)
--------------|-------------------------------------|--------------------------------
High-Level API| [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)

**Low-level APIs** in both frameworks allow you to build **computational graphs**. These graphs define how to compute outputs (e.g., the loss function) based on input parameters and can be executed on GPUs if available. These frameworks also provide functions to differentiate the computational graph and compute gradients, which are then used to optimize model parameters.

**High-level APIs** treat neural networks as a **sequence of layers**, simplifying the process of constructing most neural networks. Training a model typically involves preparing the data and calling a `fit` function to handle the training process.

High-level APIs enable quick construction of standard neural networks without worrying about many details. On the other hand, low-level APIs provide greater control over the training process, making them valuable for research and experimentation with new neural network architectures.

It's worth noting that both APIs can be used together. For example, you can create a custom network layer using the low-level API and integrate it into a larger network built with the high-level API. Alternatively, you can define a network using the high-level API and use a custom low-level training loop for optimization. Both APIs share the same foundational concepts and are designed to work seamlessly together.

## Learning

In this course, we provide content for both PyTorch and TensorFlow. You can choose your preferred framework and focus on the corresponding notebooks. If you're unsure which framework to pick, explore online discussions about **PyTorch vs. TensorFlow** or try both frameworks to gain a better understanding.

Where possible, we will use high-level APIs for simplicity. However, we believe it's important to understand the fundamentals of neural networks, so we start with low-level APIs and tensors. If you prefer to dive in quickly and skip the details, you can proceed directly to the high-level API notebooks.

## ✍️ Exercises: Frameworks

Continue your learning with the following notebooks:

Low-Level API | [TensorFlow+Keras Notebook](IntroKerasTF.ipynb) | [PyTorch](IntroPyTorch.ipynb)
--------------|-------------------------------------|--------------------------------
High-Level API| [Keras](IntroKeras.ipynb) | *PyTorch Lightning*

Once you've mastered the frameworks, let's revisit the concept of overfitting.

# Overfitting

Overfitting is a crucial concept in machine learning, and it's essential to understand it well!

Consider the problem of approximating 5 data points (represented by `x` in the graphs below):

![linear](../../../../../translated_images/en/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.jpg) | ![overfit](../../../../../translated_images/en/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.jpg)
-------------------------|--------------------------
**Linear model, 2 parameters** | **Non-linear model, 7 parameters**
Training error = 5.3 | Training error = 0
Validation error = 5.1 | Validation error = 20

* On the left, we see a good linear approximation. The model has an appropriate number of parameters and captures the underlying pattern of the data.
* On the right, the model is overly complex. With 7 parameters for just 5 data points, the model adjusts to fit all points perfectly, resulting in a training error of 0. However, it fails to generalize the true pattern, leading to a high validation error.

Striking the right balance between model complexity (number of parameters) and the amount of training data is critical.

## Why overfitting occurs

  * Insufficient training data
  * An overly complex model
  * Excessive noise in the input data

## How to detect overfitting

As shown in the graph above, overfitting can be identified by a very low training error and a high validation error. During training, both training and validation errors typically decrease initially. However, at some point, the validation error may stop decreasing and start increasing. This indicates overfitting and suggests that training should be stopped (or a snapshot of the model should be saved).

![overfitting](../../../../../translated_images/en/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.png)

## How to prevent overfitting

If overfitting occurs, you can take the following steps:

 * Increase the amount of training data.
 * Reduce the complexity of the model.
 * Apply [regularization techniques](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), such as [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), which will be covered later.

## Overfitting and Bias-Variance Tradeoff

Overfitting is a specific case of a broader statistical problem known as the [Bias-Variance Tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Errors in a model can generally be categorized into two types:

* **Bias errors** occur when the algorithm fails to capture the relationship in the training data accurately. This often happens when the model is too simple (**underfitting**).
* **Variance errors** occur when the model captures noise in the input data instead of meaningful patterns (**overfitting**).

During training, bias errors decrease as the model learns to approximate the data, while variance errors increase. It's important to stop training—either manually (when overfitting is detected) or automatically (using regularization)—to prevent overfitting.

## Conclusion

In this lesson, you learned about the differences between the APIs of the two most popular AI frameworks, TensorFlow and PyTorch. Additionally, you explored the critical topic of overfitting.

## 🚀 Challenge

In the accompanying notebooks, you'll find 'tasks' at the end. Work through the notebooks and complete the tasks.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/10)

## Review & Self Study

Research the following topics:

- TensorFlow
- PyTorch
- Overfitting

Reflect on these questions:

- What are the differences between TensorFlow and PyTorch?
- How do overfitting and underfitting differ?

## [Assignment](lab/README.md)

In this lab, you'll solve two classification problems using single- and multi-layered fully connected networks with PyTorch or TensorFlow.

* [Instructions](lab/README.md)
* [Notebook](lab/LabFrameworks.ipynb)

---

