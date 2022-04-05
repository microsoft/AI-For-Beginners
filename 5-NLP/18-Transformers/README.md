# Attention mechanisms and transformers

One of the most important problems in NLP domain is **machine translation**. In this section, we will focus on machine translation, or, more generally, on any *sequence-to-sequence* task (which is also called **sentence transduction**). 

With RNNs, sequence-to-sequence is implemented by two recurrent networks, where one network (**encoder**) collapses input sequence into hidden state, and another one, **decoder**, unrolls this hidden state into translated result. There are a couple of problems  with this approach:

* Final state of the encoder network would have hard time remembering the beginning of a sentence, thus causing poor quality of the model on long sentences
* All words in a sequence have the same impact on the result. In reality specific words in the input sequence often have more impact on sequential outputs than others.

**Attention Mechanisms** provide means of weighting the contextual impact of each input vector on each output prediction of the RNN. The way it is implemented is by creating shortcuts between intermediate states of the input RNN, and output RNN. In this manner, when generating output symbol y<sub>t</sub>, we will take into account all input hidden states h<sub>i</sub>, with different weight coefficients &alpha;<sub>t,i</sub>. 

![Image showing an encoder/decoder model with an additive attention layer](./images/encoder-decoder-attention.png)

> The encoder-decoder model with additive attention mechanism in [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf), cited from [this blog post](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)

Attention matrix {&alpha;<sub>i,j</sub>} would represent the degree which certain input words play in generation of a given word in the output sequence. Below is the example of such a matrix:

![Image showing a sample alignment found by RNNsearch-50, taken from Bahdanau - arviz.org](./images/bahdanau-fig3.png)

> Figure from [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf) (Fig.3)

Attention mechanisms are responsible for much of the current or near current state of the art in Natural language processing. Adding attention however greatly increases the number of model parameters which led to scaling issues with RNNs. A key constraint of scaling RNNs is that the recurrent nature of the models makes it challenging to batch and parallelize training. In an RNN each element of a sequence needs to be processed in sequential order which means it cannot be easily parallelized.

![Encoder Decoder with Attention](images/EncDecAttention.gif)

> Figure from [Google Blog](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)

Adoption of attention mechanisms combined with this constraint led to the creation of the now State of the Art Transformer Models that we know and use today from BERT to Open-GPT3.

## Transformer models

One of the main ideas behind transformers is to avoid sequential nature of RNNs, and create a model that is parallelizable during training. This is achieved by implementing two ideas:

* positional encoding
* using self-attention mechanism to capture patterns instead of RNNs (or CNNs) (that is why the paper that introduces transformers is called *[Attention is all you need](https://arxiv.org/abs/1706.03762)) 

### Positional Encoding/Embedding

The idea of positional encoding is the following. When using RNNs, the relative position of the tokens is represented by the number of step, and thus does not need to be explicitly represented. However, once we switch to attention, we need to know the relative positions of tokens within a sequence. To get positional encoding, we augment our sequence of tokens with a sequence of token positions in the sequence (i.e., a sequence of numbers 0,1, ...). 

We then mix the token position with token embedding vector. To transform position (integer) into a vector, we can use different approaches:

* Trainable embedding, similar to token embedding. This is the approach we consider here. We apply embedding layers on top of both tokens and their positions, resulting in embedding vectors of the same dimensions, which we then add together. 
* Fixed position encoding function, as proposed in the original paper.

<img src="images/pos-embedding.png" width="50%"/>

> Image by author

The result we get with positional embedding embeds both original token and its position within sequence.

### Multi-Head Self-attention

Next, we need to capture some patterns within our sequence. To do this, transformers use **self-attention** mechanism, which is essentially attention applied to the same sequence as input and output. Applying self-attention allows us to take into account **context** within the sentence, and see which words are inter-related. For example, it allows us to see which words are referred to by coreferences, such as *it*, and also take the context into account:

![](images/CoreferenceResolution.png)

> Image from the [Google Blog](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)

In transformers, we use **Multi-Head Attention**, in order to give network the power to capture several different types of dependencies, eg. long-term vs. short-term word relations, co-reference vs. something else, etc. 

[TensorFlow Notebook](TransformersTF.ipynb) contains more detains on the implementation of transformer layers.

### Encoder-Decoder Attention

In transformers, attention is used in two places:
* To capture patterns within the input text using self-attention
* To perform sequence translation - it is the attention layer between encoder and decoder.

Encoder-decoder attention is very similar to the attention mechanism used in RNNs, as described in the beginning of this section. This animated diagram explains the role of encoder-decoder attention.

![Animated GIF showing how the evaluations are performed in transformer models.](./images/transformer-animated-explanation.gif) 

Since each input position is mapped independently to each output position, transformers can parallelize better than RNNs, which enables much larger and more expressive language models. Each attention head can be used to learn different relationships between words that improves downstream Natural Language Processing tasks.

## BERT

**BERT** (Bidirectional Encoder Representations from Transformers) is a very large multi layer transformer network with 12 layers for *BERT-base*, and 24 for *BERT-large*. The model is first pre-trained on large corpus of text data (WikiPedia + books) using unsupervised training (predicting masked words in a sentence). During pre-training the model absorbs significant level of language understanding which can then be leveraged with other datasets using fine tuning. This process is called **transfer learning**. 

![picture from http://jalammar.github.io/illustrated-bert/](images/jalammarBERT-language-modeling-masked-lm.png)

> Image [source](http://jalammar.github.io/illustrated-bert/)

There are many variations of Transformer architectures including BERT, DistilBERT. BigBird, OpenGPT3 and more that can be fine tuned. The [HuggingFace package](https://github.com/huggingface/) provides repository for training many of these architectures with both PyTorch and TensorFlow.

## Continue to Notebooks

* [Transformers in PyTorch](TransformersPyTorch.ipynb)
* [Transformers in TensorFlow](TransformersTF.ipynb)

## Related materials

* [Blog post](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/), explaining the classical [Attention is all you need](https://arxiv.org/abs/1706.03762) paper on transformers
* [A series of blog posts](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452) on transformers, explaining the architecture in detail.
