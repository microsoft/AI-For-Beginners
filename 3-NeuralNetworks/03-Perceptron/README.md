# Introduction to Neural Networks. Perceptron.

One of the first attempts to implement something similar to a modern neural network was done by Frank Rosenblatt from Cornell Aeronautical Laboratory in 1957. It was hardware implementation called "Mark-1", designed to recognize primitive geometric figures, such as triangles, squares and circles.

<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />
-----|-----

An input image was represented by 20x20 photocell array, so the neural network had 400 inputs and one binary output. Simple network contained one neuron, also called **threshold logic unit**. Neural network weights were potentiometers that required manual adjustment during the training phase.

> New York Times wrote about perceptron at that time:
> *the embryo of an electronic computer that [the Navy] expects will be able to walk, talk, see, write, reproduce itself and be conscious of its existence.*

## Perceptron Model

Suppose we have N features in our model, in which case the input vector would be a vector of size N. Perceptron is a **binary classification** model, i.e. it can distinguish between two classes of input data. We will assume that for each input vector x the output of our perceptron would be either +1 or -1, depending on the class. The output will be computed using the formula

y(x) = f(w<sup>T</sup>x)

where f is a step activation function

<img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" />

## Training the Perceptron

To train a perceptron we need to find weights vector w that classifies most of the values correctly, i.e. results in the smallest **error**. This error is defined by **perceptron criterion** on the following manner:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

where
* the sum is taken on those training data points i that result in the wrong classification
* x<sub>i</sub> is the input data, and t<sub>i</sub> is either -1 or +1 for negative and positive examples accordingly. 

This criteria is considered as a function of weights w, and we need to minimize it. Often, a method called **gradient descent** is used, in which we start with some initial weights w<sup>(0)</sup>, and then at each step update the weights according to the formula

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Here &eta; is so-called **learning rate**, and &nabla;E(w) denotes the **gradient** of E. After we calculate the gradient, we end up with

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

## Proceed in Notebook

To see how we can use perceptron to solve some toy as well as real-life problems, and to continue learning - go to [Perceptron](Perceptron.ipynb) notebook.
