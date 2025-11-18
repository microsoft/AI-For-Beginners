<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c34cbba802058b6fa267e1a294d4e510",
  "translation_date": "2025-11-18T18:28:01+00:00",
  "source_file": "lessons/3-NeuralNetworks/03-Perceptron/README.md",
  "language_code": "pcm"
}
-->
# Introduction to Neural Networks: Perceptron

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/5)

One of di first try wey dem do to create somtin wey resemble modern neural network na Frank Rosenblatt from Cornell Aeronautical Laboratory for 1957. E be hardware wey dem call "Mark-1", wey dem design to sabi primitive geometric shapes like triangle, square and circle.

|      |      |
|--------------|-----------|
|<img src='../../../../../translated_images/Rosenblatt-wikipedia.294821b285ac796d2281a556fe3de9a7aa328e34cdd25f3ac9deefa0982ea2df.pcm.jpg' alt='Frank Rosenblatt'/> | <img src='../../../../../translated_images/Mark_I_perceptron_wikipedia.1f84eaa2d4b76ec9fb32bab6ae07e40faa202be1935c0fbd8c2bc2600a87bcb1.pcm.jpg' alt='The Mark 1 Perceptron' />|

> Images [from Wikipedia](https://en.wikipedia.org/wiki/Perceptron)

Di input image na 20x20 photocell array, so di neural network get 400 inputs and one binary output. Di simple network get one neuron, wey dem dey call **threshold logic unit**. Di neural network weights dey act like potentiometer wey dem go need adjust manually during di training phase.

> ✅ Potentiometer na device wey person fit use to adjust di resistance for circuit.

> Di New York Times talk about perceptron for dat time: *di embryo of one electronic computer wey [di Navy] dey expect say e go fit waka, talk, see, write, reproduce itself and sabi say e dey exist.*

## Perceptron Model

Make we assume say we get N features for our model, di input vector go be vector wey get size N. Perceptron na **binary classification** model, e mean say e fit separate two classes of input data. We go assume say for each input vector x, di output of our perceptron go be either +1 or -1, depending on di class. Di output go dey calculate with di formula:

y(x) = f(w<sup>T</sup>x)

where f na step activation function

<!-- img src="http://www.sciweavers.org/tex2img.php?eq=f%28x%29%20%3D%20%5Cbegin%7Bcases%7D%0A%20%20%20%20%20%20%20%20%20%2B1%20%26%20x%20%5Cgeq%200%20%5C%5C%0A%20%20%20%20%20%20%20%20%20-1%20%26%20x%20%3C%200%0A%20%20%20%20%20%20%20%5Cend%7Bcases%7D%20%5C%5C%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0" align="center" border="0" alt="f(x) = \begin{cases} +1 & x \geq 0 \\ -1 & x < 0 \end{cases} \\" width="154" height="50" / -->
<img src="../../../../../translated_images/activation-func.b4924007c7ce77648d4b1dd3e81c689453204902c096c626735c7b53688cdc63.pcm.png"/>

## Training the Perceptron

To train perceptron, we need to find weights vector w wey go classify most of di values correct, e mean say e go give di smallest **error**. Dis error E na wetin dem dey define with **perceptron criterion** like dis:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

where:

* di sum na for di training data points i wey dey give wrong classification
* x<sub>i</sub> na di input data, and t<sub>i</sub> na either -1 or +1 for negative and positive examples.

Dis criteria na function of weights w, and we need to minimize am. Most times, dem dey use method wey dem dey call **gradient descent**, wey we go start with some initial weights w<sup>(0)</sup>, and then for each step we go update di weights with di formula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Here &eta; na wetin dem dey call **learning rate**, and &nabla;E(w) na di **gradient** of E. After we calculate di gradient, we go get:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Di algorithm for Python go look like dis:

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

For dis lesson, you don learn about perceptron, wey be binary classification model, and how to train am by using weights vector.

## 🚀 Challenge

If you wan try build your own perceptron, try [dis lab for Microsoft Learn](https://docs.microsoft.com/en-us/azure/machine-learning/component-reference/two-class-averaged-perceptron?WT.mc_id=academic-77998-cacaste) wey dey use [Azure ML designer](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer?WT.mc_id=academic-77998-cacaste).

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/6)

## Review & Self Study

To see how we fit use perceptron solve toy problem and real-life problems, and to continue di learning - go [Perceptron](Perceptron.ipynb) notebook.

Here na one interesting [article about perceptrons](https://towardsdatascience.com/what-is-a-perceptron-basics-of-neural-networks-c4cfea20c590
) too.

## [Assignment](lab/README.md)

For dis lesson, we don implement perceptron for binary classification task, and we don use am to classify between two handwritten digits. For dis lab, dem dey ask you to solve di problem of digit classification completely, e mean say make you determine which digit dey most likely correspond to di given image.

* [Instructions](lab/README.md)
* [Notebook](lab/PerceptronMultiClass.ipynb)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis docu don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) take translate am. Even though we dey try make e accurate, abeg sabi say automated translations fit get mistake or no correct well. Di original docu for di language wey dem write am first na di main correct one. For important information, e good make una use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->