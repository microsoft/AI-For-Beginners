<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c34cbba802058b6fa267e1a294d4e510",
  "translation_date": "2025-09-23T11:51:39+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "en"
}
-->
# Introduction to Neural Networks: Perceptron

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/5)

One of the earliest attempts to create something resembling a modern neural network was made by Frank Rosenblatt from Cornell Aeronautical Laboratory in 1957. It was a hardware implementation called "Mark-1," designed to recognize basic geometric shapes like triangles, squares, and circles.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Images [from Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

The input image was represented by a 20x20 array of photocells, meaning the neural network had 400 inputs and one binary output. This simple network consisted of a single neuron, also known as a **threshold logic unit**. The weights of the neural network acted like potentiometers, which had to be manually adjusted during the training process.

> ✅ A potentiometer is a device that allows the user to adjust the resistance in a circuit.

> At the time, The New York Times described the perceptron as: *the embryo of an electronic computer that [the Navy] expects will be able to walk, talk, see, write, reproduce itself and be conscious of its existence.*

## Perceptron Model

Imagine we have N features in our model, which means the input vector would be of size N. A perceptron is a **binary classification** model, meaning it can differentiate between two classes of input data. For each input vector x, we assume the perceptron's output will be either +1 or -1, depending on the class. The output is calculated using the formula:

y(x) = f(w<sup>T</sup>x)

where f is a step activation function.

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="images/activation-func.png"/>

## Training the Perceptron

To train a perceptron, we need to find a weight vector w that correctly classifies most of the data points, minimizing the **error**. This error E is defined by the **perceptron criterion** as follows:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

where:

* The sum is taken over the training data points i that are misclassified.
* x<sub>i</sub> represents the input data, and t<sub>i</sub> is either -1 or +1 for negative and positive examples, respectively.

This criterion is treated as a function of the weights w, and our goal is to minimize it. A common method used for this is **gradient descent**, where we start with some initial weights w<sup>(0)</sup> and update them at each step using the formula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Here, &eta; is the **learning rate**, and &nabla;E(w) represents the **gradient** of E. After calculating the gradient, the update formula becomes:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

The algorithm in Python looks like this:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```


## Conclusion

In this lesson, you learned about the perceptron, a binary classification model, and how to train it using a weight vector.

## 🚀 Challenge

If you'd like to try building your own perceptron, check out [this lab on Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste), which uses the [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Review & Self Study

To explore how perceptrons can be used to solve both toy problems and real-world challenges, and to continue learning, check out the [Perceptron](Perceptron.ipynb) notebook.

Here's an interesting [article about perceptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590).

## [Assignment](lab/README.md)

In this lesson, we implemented a perceptron for a binary classification task and used it to distinguish between two handwritten digits. In this lab, your task is to solve the problem of digit classification entirely, i.e., determine which digit corresponds to a given image.

* [Instructions](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)

---

