<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2273cc150380a5e191903cea858f021",
  "translation_date": "2025-11-18T18:44:40+00:00",
  "source_file": "lessons/5-NLP/16-RNN/README.md",
  "language_code": "pcm"
}
-->
# Recurrent Neural Networks

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/31)

For di sections wey don pass, we don dey use beta semantic representation of text and one simple linear classifier on top di embeddings. Wetin dis architecture dey do na to capture di overall meaning of words for one sentence, but e no dey consider di **order** of di words, because di aggregation operation wey dey on top di embeddings don comot dis information from di original text. Since dis kain models no fit model word ordering, dem no fit solve more complex or ambiguous tasks like text generation or question answering.

To fit capture di meaning of text sequence, we go need another neural network architecture, wey dem dey call **recurrent neural network**, or RNN. For RNN, we go pass our sentence through di network one symbol at a time, and di network go produce one **state**, wey we go pass back to di network again with di next symbol.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.pcm.png)

> Image by di author

If we get input sequence of tokens X<sub>0</sub>,...,X<sub>n</sub>, RNN go create sequence of neural network blocks, and go train dis sequence end-to-end using backpropagation. Each network block go take pair (X<sub>i</sub>,S<sub>i</sub>) as input, and e go produce S<sub>i+1</sub> as result. Di final state S<sub>n</sub> or (output Y<sub>n</sub>) go enter linear classifier to produce di result. All di network blocks dey share di same weights, and dem dey train am end-to-end using one backpropagation pass.

Because state vectors S<sub>0</sub>,...,S<sub>n</sub> dey pass through di network, e fit learn di sequential dependencies between words. For example, if di word *not* show for somewhere inside di sequence, e fit learn how to negate some elements inside di state vector, wey go result in negation.

> ✅ Since di weights of all RNN blocks for di picture above dey shared, di same picture fit represent as one block (for di right) with one recurrent feedback loop, wey dey pass di output state of di network back to di input.

## Anatomy of an RNN Cell

Make we see how simple RNN cell dey organized. E dey accept di previous state S<sub>i-1</sub> and current symbol X<sub>i</sub> as inputs, and e go produce di output state S<sub>i</sub> (and sometimes, we dey also interested in some other output Y<sub>i</sub>, like for di case of generative networks).

Simple RNN cell get two weight matrices inside: one dey transform input symbol (make we call am W), and another one dey transform input state (H). For dis case, di output of di network dey calculate as &sigma;(W&times;X<sub>i</sub>+H&times;S<sub>i-1</sub>+b), where &sigma; na di activation function and b na additional bias.

<img alt="RNN Cell Anatomy" src="../../../../../translated_images/rnn-anatomy.79ee3f3920b3294bd52e9543ef36102dbca3cecf6d4d78d8c63bf0bbc95fdc90.pcm.png" width="50%"/>

> Image by di author

For many cases, input tokens dey pass through di embedding layer before dem enter di RNN to reduce di dimensionality. For dis case, if di dimension of di input vectors na *emb_size*, and state vector na *hid_size* - di size of W go be *emb_size*&times;*hid_size*, and di size of H go be *hid_size*&times;*hid_size*.

## Long Short Term Memory (LSTM)

One big wahala wey classical RNNs get na di **vanishing gradients** problem. Because RNNs dey train end-to-end in one backpropagation pass, e dey hard to propagate error go di first layers of di network, and so di network no fit learn relationships between distant tokens. One way to avoid dis problem na to introduce **explicit state management** by using wetin dem dey call **gates**. Two popular architectures wey dey do dis na **Long Short Term Memory** (LSTM) and **Gated Relay Unit** (GRU).

![Image showing an example long short term memory cell](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Image source TBD

Di LSTM Network dey organized like RNN, but e get two states wey dem dey pass from layer to layer: di actual state C, and di hidden vector H. For each unit, di hidden vector H<sub>i</sub> go join with input X<sub>i</sub>, and dem go control wetin go happen to di state C through **gates**. Each gate na neural network with sigmoid activation (output dey range [0,1]), wey you fit think of as bitwise mask when e multiply di state vector. Di gates wey dey (from left to right for di picture above) na:

* Di **forget gate** go take hidden vector and decide which parts of di vector C we go forget, and which ones we go pass through.
* Di **input gate** go take some information from di input and hidden vectors and put am inside di state.
* Di **output gate** go transform state through linear layer with *tanh* activation, then e go select some parts of di state using hidden vector H<sub>i</sub> to produce new state C<sub>i+1</sub>.

Di components of di state C fit be like flags wey you fit switch on and off. For example, if we see name *Alice* for di sequence, we fit assume say e dey refer to female character, and we go raise di flag for di state say we get female noun for di sentence. If we later see phrase *and Tom*, we go raise di flag say we get plural noun. So by manipulating di state, we fit track di grammatical properties of sentence parts.

> ✅ One beta resource to understand di internals of LSTM na dis great article [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) by Christopher Olah.

## Bidirectional and Multilayer RNNs

We don talk about recurrent networks wey dey work for one direction, from di beginning of sequence go di end. E dey look natural, because e resemble how we dey read and listen to speech. But, since for many practical cases we fit get random access to di input sequence, e fit make sense to run recurrent computation for both directions. Dis kain networks dem dey call **bidirectional** RNNs. When we dey deal with bidirectional network, we go need two hidden state vectors, one for each direction.

Recurrent network, whether na one-directional or bidirectional, dey capture some patterns inside sequence, and e fit store dem inside state vector or pass am into output. Just like convolutional networks, we fit build another recurrent layer on top di first one to capture higher level patterns and build from di low-level patterns wey di first layer extract. Dis one dey lead us to di idea of **multi-layer RNN** wey get two or more recurrent networks, where di output of di previous layer dey pass to di next layer as input.

![Image showing a Multilayer long-short-term-memory- RNN](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.pcm.jpg)

*Picture from [this wonderful post](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) by Fernando López*

## ✍️ Exercises: Embeddings

Continue your learning for di following notebooks:

* [RNNs with PyTorch](RNNPyTorch.ipynb)
* [RNNs with TensorFlow](RNNTF.ipynb)

## Conclusion

For dis unit, we don see say RNNs fit dey used for sequence classification, but in fact, dem fit handle many other tasks, like text generation, machine translation, and more. We go look into those tasks for di next unit.

## 🚀 Challenge

Read some literature about LSTMs and think about how dem dey apply:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/32)

## Review & Self Study

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) by Christopher Olah.

## [Assignment: Notebooks](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make you sabi say machine transleshion fit get mistake or no dey correct well. Di original dokyument wey dey for im native language na di main source wey you go fit trust. For important informashon, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong meaning wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->