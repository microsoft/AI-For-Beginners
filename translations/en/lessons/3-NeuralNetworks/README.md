<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1c6b8c7c1778a35fc1139b7f2aecb7b3",
  "translation_date": "2025-08-31T17:48:41+00:00",
  "source_file": "lessons/3-NeuralNetworks/README.md",
  "language_code": "en"
}
-->
# Introduction to Neural Networks

![Summary of Intro Neural Networks content in a doodle](../../../../translated_images/ai-neuralnetworks.1c687ae40bc86e834f497844866a26d3e0886650a67a4bbe29442e2f157d3b18.en.png)

As we discussed in the introduction, one way to achieve intelligence is by training a **computer model** or an **artificial brain**. Since the mid-20th century, researchers have experimented with various mathematical models, and in recent years, this approach has proven to be highly successful. These mathematical models of the brain are called **neural networks**.

> Sometimes neural networks are referred to as *Artificial Neural Networks* (ANNs) to clarify that we are discussing models, not actual networks of neurons.

## Machine Learning

Neural Networks are part of a broader field called **Machine Learning**, which aims to use data to train computer models capable of solving problems. Machine Learning is a significant subset of Artificial Intelligence, but this curriculum does not cover classical ML.

> Check out our separate **[Machine Learning for Beginners](http://github.com/microsoft/ml-for-beginners)** curriculum to learn more about traditional Machine Learning.

In Machine Learning, we assume we have a dataset of examples **X** and corresponding output values **Y**. Examples are often N-dimensional vectors made up of **features**, while outputs are referred to as **labels**.

We will explore the two most common types of machine learning problems:

* **Classification**, where the goal is to categorize an input object into two or more classes.
* **Regression**, where the goal is to predict a numerical value for each input sample.

> When inputs and outputs are represented as tensors, the input dataset is a matrix of size M×N, where M is the number of samples and N is the number of features. Output labels **Y** form a vector of size M.

In this curriculum, we will focus exclusively on neural network models.

## A Model of a Neuron

From biology, we know that our brain is made up of neural cells, each with multiple "inputs" (axons) and one output (dendrite). Axons and dendrites transmit electrical signals, and the connections between them can vary in conductivity (regulated by neuromediators).

![Model of a Neuron](../../../../translated_images/synapse-wikipedia.ed20a9e4726ea1c6a3ce8fec51c0b9bec6181946dca0fe4e829bc12fa3bacf01.en.jpg) | ![Model of a Neuron](../../../../translated_images/artneuron.1a5daa88d20ebe6f5824ddb89fba0bdaaf49f67e8230c1afbec42909df1fc17e.en.png)
----|----
Real Neuron *([Image](https://en.wikipedia.org/wiki/Synapse#/media/File:SynapseSchematic_lines.svg) from Wikipedia)* | Artificial Neuron *(Image by Author)*

Thus, the simplest mathematical model of a neuron includes several inputs X<sub>1</sub>, ..., X<sub>N</sub>, an output Y, and a set of weights W<sub>1</sub>, ..., W<sub>N</sub>. The output is calculated as:

<img src="images/netout.png" alt="Y = f\left(\sum_{i=1}^N X_iW_i\right)" width="131" height="53" align="center"/>

where **f** is a non-linear **activation function**.

> Early neuron models were introduced in the classic paper [A logical calculus of the ideas immanent in nervous activity](https://www.cs.cmu.edu/~./epxing/Class/10715/reading/McCulloch.and.Pitts.pdf) by Warren McCulloch and Walter Pitts in 1943. Donald Hebb, in his book "[The Organization of Behavior: A Neuropsychological Theory](https://books.google.com/books?id=VNetYrB8EBoC)," proposed a method for training these networks.

## In this Section

In this section, we will explore:
* [Perceptron](03-Perceptron/README.md), one of the earliest neural network models for two-class classification
* [Multi-layered networks](04-OwnFramework/README.md) along with a notebook on [how to build our own framework](04-OwnFramework/OwnFramework.ipynb)
* [Neural Network Frameworks](05-Frameworks/README.md), with these notebooks: [PyTorch](05-Frameworks/IntroPyTorch.ipynb) and [Keras/Tensorflow](05-Frameworks/IntroKerasTF.ipynb)
* [Overfitting](../../../../lessons/3-NeuralNetworks/05-Frameworks)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.