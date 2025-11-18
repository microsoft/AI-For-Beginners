<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "789d6c3fb6fc7948a470b33078a5983a",
  "translation_date": "2025-11-18T18:27:00+00:00",
  "source_file": "lessons/3-NeuralNetworks/04-OwnFramework/README.md",
  "language_code": "pcm"
}
-->
# Introduction to Neural Networks. Multi-Layered Perceptron

For di last section, you don learn about di simplest neural network model - one-layered perceptron, wey be linear two-class classification model.

For dis section, we go expand di model make e dey more flexible, so e go fit:

* do **multi-class classification** join di two-class one
* solve **regression problems** join di classification
* separate classes wey no fit separate with straight line

We go also build our own modular framework for Python wey go help us create different neural network architectures.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Formalization of Machine Learning

Make we start with how Machine Learning problem dey formalize. Imagine say we get training dataset **X** with labels **Y**, and we need build model *f* wey go give di most correct predictions. Di quality of di predictions dey measure by **Loss function** &lagran;. Di following loss functions dey common:

* For regression problem, when we need predict number, we fit use **absolute error** &sum;<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, or **squared error** &sum;<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* For classification, we dey use **0-1 loss** (wey be di same as **accuracy** of di model), or **logistic loss**.

For one-level perceptron, function *f* na linear function *f(x)=wx+b* (here *w* na di weight matrix, *x* na di vector of input features, and *b* na bias vector). For different neural network architectures, dis function fit get more complex form.

> For classification, e dey good to get probabilities of di classes as network output. To change random numbers to probabilities (like to normalize di output), we dey use **softmax** function &sigma;, and di function *f* go be *f(x)=&sigma;(wx+b)*

For di definition of *f* above, *w* and *b* na **parameters** &theta;=⟨*w,b*⟩. If we get dataset ⟨**X**,**Y**⟩, we fit calculate di overall error for di whole dataset as function of parameters &theta;.

> ✅ **Di goal of neural network training na to reduce di error by changing parameters &theta;**

## Gradient Descent Optimization

One popular method for function optimization na **gradient descent**. Di idea be say we fit calculate di derivative (for multi-dimensional case na **gradient**) of loss function with respect to parameters, and change di parameters so di error go reduce. E fit formalize like dis:

* Start parameters with random values w<sup>(0)</sup>, b<sup>(0)</sup>
* Repeat di following step many times:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-&eta;&part;&lagran;/&part;w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-&eta;&part;&lagran;/&part;b

For training, di optimization steps suppose calculate based on di whole dataset (remember say loss dey calculate as sum of all training samples). But for real life, we dey use small portions of di dataset wey dem dey call **minibatches**, and calculate gradients based on di subset of data. Because di subset dey pick randomly each time, dis method na **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons and Backpropagation

One-layer network, as we don see before, fit classify linearly separable classes. To build richer model, we fit join plenty layers for di network. Mathematically, e mean say di function *f* go get more complex form, and e go calculate in steps:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>&alpha;(z<sub>1</sub>)+b<sub>2</sub>
* f = &sigma;(z<sub>2</sub>)

Here, &alpha; na **non-linear activation function**, &sigma; na softmax function, and parameters &theta;=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Di gradient descent algorithm go still dey di same, but e go hard to calculate gradients. With di chain differentiation rule, we fit calculate derivatives like dis:

* &part;&lagran;/&part;w<sub>2</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;w<sub>2</sub>)
* &part;&lagran;/&part;w<sub>1</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;&alpha;)(&part;&alpha;/&part;z<sub>1</sub>)(&part;z<sub>1</sub>/&part;w<sub>1</sub>)

> ✅ Di chain differentiation rule dey use to calculate derivatives of di loss function with respect to parameters.

Notice say di left-most part of all di expressions dey di same, so we fit calculate derivatives well starting from di loss function and go "backwards" through di computational graph. So di method of training multi-layered perceptron na **backpropagation**, or 'backprop'.

<img alt="compute graph" src="../../../../../translated_images/ComputeGraphGrad.4626252c0de035075e5cd2b7f71b776d5e3e8f64f2dc472b4420d3fdfaf53ba8.pcm.png"/>

> TODO: image citation

> ✅ We go talk about backprop well for di notebook example.  

## Conclusion

For dis lesson, we don build our own neural network library, and we don use am for simple two-dimensional classification task.

## 🚀 Challenge

For di notebook wey follow, you go build your own framework for creating and training multi-layered perceptrons. You go see how modern neural networks dey work.

Go di [OwnFramework](OwnFramework.ipynb) notebook and work through am.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Review & Self Study

Backpropagation na common algorithm for AI and ML, e good make you study [am well](https://wikipedia.org/wiki/Backpropagation)

## [Assignment](lab/README.md)

For dis lab, dem ask you to use di framework wey you build for dis lesson to solve MNIST handwritten digit classification.

* [Instructions](lab/README.md)
* [Notebook](lab/MyFW_MNIST.ipynb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis docu wey you dey see don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make sure say e correct, make you sabi say automatic translation fit get mistake or no too accurate. Di original docu for di language wey dem first write am na im you go take as di correct one. If na important information, e go better make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->