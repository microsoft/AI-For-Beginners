<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "789d6c3fb6fc7948a470b33078a5983a",
  "translation_date": "2025-09-23T11:51:20+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "en"
}
-->
# Introduction to Neural Networks. Multi-Layered Perceptron

In the previous section, you learned about the simplest neural network model—the single-layer perceptron, which is a linear model for two-class classification.

In this section, we will expand this model into a more versatile framework, enabling us to:

* perform **multi-class classification** in addition to two-class classification,
* solve **regression problems** alongside classification tasks,
* distinguish between classes that are not linearly separable.

We will also develop our own modular framework in Python, which will allow us to construct various neural network architectures.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Formalization of Machine Learning

Let’s begin by formalizing the Machine Learning problem. Suppose we have a training dataset **X** with labels **Y**, and we need to build a model *f* that makes the most accurate predictions. The quality of predictions is measured by the **Loss function** &lagran;. Commonly used loss functions include:

* For regression problems, where we predict a numerical value, we can use **absolute error** &sum;<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| or **squared error** &sum;<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>.
* For classification tasks, we use **0-1 loss** (essentially equivalent to the model’s **accuracy**) or **logistic loss**.

For a single-layer perceptron, the function *f* was defined as a linear function *f(x)=wx+b* (where *w* is the weight matrix, *x* is the vector of input features, and *b* is the bias vector). For more complex neural network architectures, this function can take on more intricate forms.

> In classification tasks, it is often desirable for the network output to represent probabilities of the corresponding classes. To convert arbitrary numbers into probabilities (e.g., to normalize the output), we often use the **softmax** function &sigma;, making the function *f* become *f(x)=&sigma;(wx+b)*.

In the definition of *f* above, *w* and *b* are referred to as **parameters** &theta;=⟨*w,b*⟩. Given the dataset ⟨**X**,**Y**⟩, we can compute the overall error across the entire dataset as a function of the parameters &theta;.

> ✅ **The goal of neural network training is to minimize the error by adjusting the parameters &theta;.**

## Gradient Descent Optimization

A well-known method for function optimization is **gradient descent**. The idea is to compute the derivative (or **gradient** in multi-dimensional cases) of the loss function with respect to the parameters and adjust the parameters in a way that reduces the error. This can be formalized as follows:

* Initialize the parameters with random values w<sup>(0)</sup>, b<sup>(0)</sup>.
* Repeat the following steps multiple times:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-&eta;&part;&lagran;/&part;w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-&eta;&part;&lagran;/&part;b

During training, optimization steps are ideally calculated using the entire dataset (since the loss is computed as a sum over all training samples). However, in practice, we use small portions of the dataset called **minibatches** and calculate gradients based on these subsets. Since the subsets are chosen randomly each time, this method is referred to as **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons and Backpropagation

A single-layer network, as we’ve seen, can classify linearly separable classes. To create a more powerful model, we can stack multiple layers in the network. Mathematically, this means the function *f* will have a more complex form and will be computed in multiple steps:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>&alpha;(z<sub>1</sub>)+b<sub>2</sub>
* f = &sigma;(z<sub>2</sub>)

Here, &alpha; is a **non-linear activation function**, &sigma; is the softmax function, and the parameters are &theta;=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

The gradient descent algorithm remains the same, but calculating gradients becomes more complex. Using the chain differentiation rule, we can compute derivatives as follows:

* &part;&lagran;/&part;w<sub>2</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;w<sub>2</sub>)
* &part;&lagran;/&part;w<sub>1</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;&alpha;)(&part;&alpha;/&part;z<sub>1</sub>)(&part;z<sub>1</sub>/&part;w<sub>1</sub>)

> ✅ The chain differentiation rule is used to compute derivatives of the loss function with respect to the parameters.

Notice that the leftmost part of all these expressions is the same, allowing us to efficiently compute derivatives starting from the loss function and working "backwards" through the computational graph. This method of training a multi-layered perceptron is called **backpropagation**, or 'backprop'.

<img alt="compute graph" src="images/ComputeGraphGrad.png"/>

> TODO: image citation

> ✅ We will explore backpropagation in much greater detail in our notebook example.

## Conclusion

In this lesson, we built our own neural network library and used it for a simple two-dimensional classification task.

## 🚀 Challenge

In the accompanying notebook, you will implement your own framework for building and training multi-layered perceptrons. This will give you a detailed understanding of how modern neural networks function.

Proceed to the [OwnFramework](OwnFramework.ipynb) notebook and work through it.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Review & Self Study

Backpropagation is a widely used algorithm in AI and ML. It’s worth studying [in more detail](https://wikipedia.org/wiki/Backpropagation).

## [Assignment](lab/README.md)

In this lab, you will use the framework you built in this lesson to solve the MNIST handwritten digit classification task.

* [Instructions](lab/README.md)
* [Notebook](lab/MyFW_MNIST.ipynb)

---

