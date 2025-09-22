<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "186bf7eeab776b36f557357ea56d4751",
  "translation_date": "2025-08-31T17:49:15+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "en"
}
-->
# Introduction to Neural Networks. Multi-Layered Perceptron

In the previous section, you learned about the simplest neural network model—the single-layer perceptron, a linear model for two-class classification.

In this section, we will expand this model into a more versatile framework, enabling us to:

* perform **multi-class classification** in addition to two-class classification
* solve **regression problems** alongside classification
* distinguish between classes that are not linearly separable

We will also create our own modular framework in Python, which will allow us to design various neural network architectures.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Formalizing Machine Learning

Let’s begin by formalizing the Machine Learning problem. Suppose we have a training dataset **X** with labels **Y**, and we need to build a model *f* that makes the most accurate predictions. The quality of these predictions is measured by a **Loss function** ℒ. Common loss functions include:

* For regression problems, where we predict a number, we can use **absolute error** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| or **squared error** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>.
* For classification, we use **0-1 loss** (essentially the same as the model’s **accuracy**) or **logistic loss**.

For a single-layer perceptron, the function *f* was defined as a linear function *f(x)=wx+b* (where *w* is the weight matrix, *x* is the vector of input features, and *b* is the bias vector). For more complex neural network architectures, this function can take on more intricate forms.

> In classification tasks, it’s often useful to output probabilities for each class. To convert arbitrary numbers into probabilities (i.e., normalize the output), we frequently use the **softmax** function σ, making the function *f* become *f(x)=σ(wx+b)*.

In the definition of *f* above, *w* and *b* are referred to as **parameters** θ=⟨*w,b*⟩. Given the dataset ⟨**X**,**Y**⟩, we can compute the overall error across the entire dataset as a function of the parameters θ.

> ✅ **The goal of training a neural network is to minimize the error by adjusting the parameters θ.**

## Gradient Descent Optimization

A well-known method for function optimization is **gradient descent**. The idea is to compute the derivative (or **gradient** in multi-dimensional cases) of the loss function with respect to the parameters and adjust the parameters to reduce the error. This can be formalized as follows:

* Initialize the parameters with random values w<sup>(0)</sup>, b<sup>(0)</sup>.
* Repeat the following steps multiple times:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

In theory, these optimization steps should be calculated using the entire dataset (since the loss is computed as a sum over all training samples). However, in practice, we use small portions of the dataset called **minibatches** and calculate gradients based on these subsets. Since the subsets are chosen randomly each time, this method is called **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons and Backpropagation

A single-layer network, as we’ve seen, can classify linearly separable classes. To create a more powerful model, we can stack multiple layers in the network. Mathematically, this means the function *f* will have a more complex form and will be computed in several steps:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Here, α is a **non-linear activation function**, σ is the softmax function, and the parameters are θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

The gradient descent algorithm remains the same, but calculating the gradients becomes more complex. Using the chain rule of differentiation, we can compute the derivatives as follows:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ The chain rule of differentiation is used to compute the derivatives of the loss function with respect to the parameters.

Notice that the leftmost part of these expressions is the same, allowing us to efficiently compute derivatives by starting from the loss function and working "backwards" through the computational graph. This training method for multi-layered perceptrons is called **backpropagation**, or simply 'backprop'.

<img alt="compute graph" src="images/ComputeGraphGrad.png"/>

> TODO: image citation

> ✅ We will explore backpropagation in much greater detail in the accompanying notebook example.

## Conclusion

In this lesson, we built our own neural network library and used it for a simple two-dimensional classification task.

## 🚀 Challenge

In the accompanying notebook, you will implement your own framework for building and training multi-layered perceptrons. This will give you a detailed understanding of how modern neural networks function.

Proceed to the [OwnFramework](OwnFramework.ipynb) notebook and work through it.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Review & Self Study

Backpropagation is a widely used algorithm in AI and ML. It’s worth studying [in more detail](https://wikipedia.org/wiki/Backpropagation).

## [Assignment](lab/README.md)

In this lab, you will use the framework you built in this lesson to solve the MNIST handwritten digit classification problem.

* [Instructions](lab/README.md)
* [Notebook](lab/MyFW_MNIST.ipynb)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.