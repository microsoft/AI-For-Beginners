# Recurrent Neural Networks

In the previous sections, we have been using rich semantic representations of text, and a simple linear classifier on top of the embeddings. What this architecture does is to capture aggregated meaning of words in a sentence, but it does not take into account the **order** of words, because aggregation operation on top of embeddings removed this information from the original text. Because these models are unable to model word ordering, they cannot solve more complex or ambiguous tasks such as text generation or question answering.

To capture the meaning of text sequence, we need to use another neural network architecture, which is called a **recurrent neural network**, or RNN. In RNN, we pass our sentence through the network one symbol at a time, and the network produces some **state**, which we then pass to the network again with the next symbol.

![RNN](./images/rnn.png)

> Image by author

Given the input sequence of tokens X<sub>0</sub>,...,X<sub>n</sub>, RNN creates a sequence of neural network blocks, and trains this sequence end-to-end using back propagation. Each network block takes a pair (X<sub>i</sub>,S<sub>i</sub>) as an input, and produces S<sub>i+1</sub> as a result. Final state S<sub>n</sub> or (output Y<sub>n</sub>) goes into a linear classifier to produce the result. All network blocks share the same weights, and are trained end-to-end using one backpropagation pass.

Because state vectors S<sub>0</sub>,...,S<sub>n</sub> are passed through the network, it is able to learn the sequential dependencies between words. For example, when the word *not* appears somewhere in the sequence, it can learn to negate certain elements within the state vector, resulting in negation.  

> Since weights of all RNN blocks on the picture are shared, the same picture can be represented as one block (on the right) with a recurrent feedback loop, which passes output state of the network back to the input.

## Anatomy of RNN Cell

Let's see how simple RNN cell is organized. It accepts previous state S<sub>i-1</sub> and current symbol X<sub>i</sub> as inputs, and has to produce output state S<sub>i</sub> (and, sometimes, we are also interested in some other output Y<sub>i</sub>, as in case with generative networks).

Simple RNN cell has two weight matrices inside: one transforms input symbol (let call it W), and another one transforms input state (H). In this case the output of the network is calculated as &sigma;(W&times;X<sub>i</sub>+H&times;S<sub>i-1</sub>+b), where &sigma; is the activation function, b is additional bias.

<img alt="RNN Cell Anatomy" src="images/rnn-anatomy.png" width="50%"/>

> Image by author

In many cases, input tokens are passed through the embedding layer before entering the RNN to lower the dimensionality. In this case, if the dimension of the input vectors is *emb_size*, and state vector is *hid_size* - the size of W is *emb_size*&times;*hid_size*, and the size of H is *hid_size*&times;*hid_size*. 

## Long Short Term Memory (LSTM)

One of the main problems of classical RNNs is so-called **vanishing gradients** problem. Because RNNs are trained end-to-end in one back-propagation pass, it is having hard times propagating error to the first layers of the network, and thus the network cannot learn relationships between distant tokens. One of the ways to avoid this problem is to introduce **explicit state management** by using so called **gates**. There are two most known architectures of this kind: **Long Short Term Memory** (LSTM) and **Gated Relay Unit** (GRU).

![Image showing an example long short term memory cell](./images/long-short-term-memory-cell.svg)

LSTM Network is organized in a manner similar to RNN, but there are two states that are being passed from layer to layer: actual state C, and hidden vector H. At each unit, hidden vector H<sub>i</sub> is concatenated with input X<sub>i</sub>, and they control what happens to the state C via **gates**. Each gate is a neural network with sigmoid activation (output in the range [0,1]), which can be thought of as bitwise mask when multiplied by the state vector. There are the following gates (from left to right on the picture above):
* **forget gate** takes hidden vector and determines, which components of the vector C we need to forget, and which to pass through. 
* **input gate** takes some information from the input and hidden vector, and inserts it into state.
* **output gate** transforms state via some linear layer with *tanh* activation, then selects some of its components using hidden vector H<sub>i</sub> to produce new state C<sub>i+1</sub>.

Components of the state C can be thought of as some flags that can be switched on and off. For example, when we encounter a name *Alice* in the sequence, we may want to assume that it refers to female character, and raise the flag in the state that we have female noun in the sentence. When we further encounter phrases *and Tom*, we will raise the flag that we have plural noun. Thus by manipulating state we can supposedly keep track of grammatical properties of sentence parts.

> **Note**: A great resource for understanding internals of LSTM is this great article [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) by Christopher Olah.

## Bidirectional and multilayer RNNs

We have discussed recurrent networks that operate in one direction, from beginning of a sequence to the end. It looks natural, because it resembles the way we read and listen to speech. However, since in many practical cases we have random access to the input sequence, it might make sense to run recurrent computation in both directions. Such networks are call **bidirectional** RNNs. When dealing with bidirectional network, we would need two hidden state vectors, one for each direction. 

Recurrent network, one-directional or bidirectional, captures certain patterns within a sequence, and can store them into state vector or pass into output. As with convolutional networks, we can build another recurrent layer on top of the first one to capture higher level patterns, build from low-level patterns extracted by the first layer. This leads us to the notion of **multi-layer RNN**, which consists of two or more recurrent networks, where output of the previous layer is passed to the next layer as input.

![Image showing a Multilayer long-short-term-memory- RNN](./images/multi-layer-lstm.jpg)

*Picture from [this wonderful post](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) by Fernando López*

## Continue to Notebooks

* [RNNs with PyTorch](RNNPyTorch.ipynb)
* [RNNs with TensorFlow](RNNTF.ipynb)

## RNNs for other tasks

In this unit, we have seen that RNNs can be used for sequence classification, but in fact, they can handle many more tasks, such as text generation, machine translation, and more. We will consider those tasks in the next unit.
