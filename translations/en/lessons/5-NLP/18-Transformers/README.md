<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f335dfcb4a993920504c387973a36957",
  "translation_date": "2025-09-23T11:52:37+00:00",
  "source_file": "lessons/5-NLP/18-Transformers/README.md",
  "language_code": "en"
}
-->
# Attention Mechanisms and Transformers

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/35)

One of the most important challenges in the NLP field is **machine translation**, a key task behind tools like Google Translate. In this section, we will focus on machine translation, or more broadly, on any *sequence-to-sequence* task (also known as **sentence transduction**).

With RNNs, sequence-to-sequence tasks are implemented using two recurrent networks: the **encoder**, which compresses an input sequence into a hidden state, and the **decoder**, which expands this hidden state into a translated output. However, this approach has some limitations:

* The encoder's final state struggles to retain information from the beginning of a sentence, leading to poor performance for long sentences.
* All words in a sequence are treated as equally important, even though certain words often have a greater influence on the output.

**Attention Mechanisms** address these issues by assigning different weights to the contextual impact of each input vector on each output prediction of the RNN. This is achieved by creating shortcuts between intermediate states of the input RNN and the output RNN. When generating output symbol y<sub>t</sub>, all input hidden states h<sub>i</sub> are considered, with varying weight coefficients &alpha;<sub>t,i</sub>.

![Image showing an encoder/decoder model with an additive attention layer](../../../../../translated_images/en/encoder-decoder-attention.7a726296894fb567aa2898c94b17b3289087f6705c11907df8301df9e5eeb3de.png)

> The encoder-decoder model with additive attention mechanism in [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf), cited from [this blog post](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)

The attention matrix {&alpha;<sub>i,j</sub>} represents the extent to which specific input words contribute to the generation of a particular word in the output sequence. Below is an example of such a matrix:

![Image showing a sample alignment found by RNNsearch-50, taken from Bahdanau - arviz.org](../../../../../translated_images/en/bahdanau-fig3.09ba2d37f202a6af11de6c82d2d197830ba5f4528d9ea430eb65fd3a75065973.png)

> Figure from [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf) (Fig.3)

Attention mechanisms are responsible for much of the current or near-current state-of-the-art in NLP. However, adding attention significantly increases the number of model parameters, which led to scaling challenges with RNNs. A key limitation of scaling RNNs is their sequential nature, which makes it difficult to batch and parallelize training. In RNNs, each element of a sequence must be processed in order, preventing easy parallelization.

![Encoder Decoder with Attention](../../../../../lessons/5-NLP/18-Transformers/images/EncDecAttention.gif)

> Figure from [Google's Blog](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)

The adoption of attention mechanisms, combined with this limitation, led to the development of the now state-of-the-art Transformer Models, such as BERT and Open-GPT3.

## Transformer models

The core idea behind transformers is to eliminate the sequential nature of RNNs and create a model that can be parallelized during training. This is achieved through two key concepts:

* Positional encoding
* Using a self-attention mechanism to capture patterns instead of relying on RNNs (or CNNs). This is why the paper introducing transformers is titled *[Attention is all you need](https://arxiv.org/abs/1706.03762)*.

### Positional Encoding/Embedding

The concept of positional encoding works as follows:
1. In RNNs, the relative position of tokens is implicitly represented by the number of steps, so explicit representation is unnecessary.
2. However, with attention mechanisms, the relative positions of tokens within a sequence must be explicitly represented.
3. To achieve positional encoding, we augment the sequence of tokens with their positions in the sequence (e.g., a sequence of numbers 0, 1, ...).
4. We then combine the token positions with token embedding vectors. To transform positions (integers) into vectors, different approaches can be used:

* Trainable embeddings, similar to token embeddings. This approach is considered here. Embedding layers are applied to both tokens and their positions, resulting in embedding vectors of the same dimensions, which are then added together.
* Fixed position encoding functions, as proposed in the original paper.

<img src="images/pos-embedding.png" width="50%"/>

> Image by the author

The result of positional embedding combines both the original token and its position within the sequence.

### Multi-Head Self-Attention

Next, we need to identify patterns within the sequence. Transformers achieve this using a **self-attention** mechanism, which applies attention to the same sequence for both input and output. Self-attention allows the model to consider **context** within the sentence and identify interrelated words. For example, it can determine which words are referenced by pronouns like *it* and incorporate the surrounding context:

![](../../../../../translated_images/en/CoreferenceResolution.861924d6d384a7d68d8d0039d06a71a151f18a796b8b1330239d3590bd4947eb.png)

> Image from the [Google Blog](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)

Transformers use **Multi-Head Attention** to enable the network to capture various types of dependencies, such as long-term vs. short-term word relationships, co-references, and more.

[TensorFlow Notebook](TransformersTF.ipynb) contains more details on the implementation of transformer layers.

### Encoder-Decoder Attention

In transformers, attention is applied in two areas:

* To capture patterns within the input text using self-attention.
* To perform sequence translation via the attention layer between the encoder and decoder.

Encoder-decoder attention is similar to the attention mechanism used in RNNs, as described earlier in this section. This animated diagram illustrates the role of encoder-decoder attention.

![Animated GIF showing how the evaluations are performed in transformer models.](../../../../../lessons/5-NLP/18-Transformers/images/transformer-animated-explanation.gif)

Since each input position is mapped independently to each output position, transformers can parallelize more effectively than RNNs, enabling much larger and more expressive language models. Each attention head can learn different relationships between words, improving downstream NLP tasks.

## BERT

**BERT** (Bidirectional Encoder Representations from Transformers) is a large multi-layer transformer network with 12 layers for *BERT-base* and 24 layers for *BERT-large*. The model is first pre-trained on a large corpus of text data (Wikipedia + books) using unsupervised training (predicting masked words in a sentence). During pre-training, the model acquires significant language understanding, which can then be leveraged for other datasets through fine-tuning. This process is known as **transfer learning**.

![picture from http://jalammar.github.io/illustrated-bert/](../../../../../translated_images/en/jalammarBERT-language-modeling-masked-lm.34f113ea5fec4362e39ee4381aab7cad06b5465a0b5f053a0f2aa05fbe14e746.png)

> Image [source](http://jalammar.github.io/illustrated-bert/)

## ✍️ Exercises: Transformers

Continue your learning in the following notebooks:

* [Transformers in PyTorch](TransformersPyTorch.ipynb)
* [Transformers in TensorFlow](TransformersTF.ipynb)

## Conclusion

In this lesson, you learned about Transformers and Attention Mechanisms, essential tools in the NLP toolkit. There are many variations of Transformer architectures, including BERT, DistilBERT, BigBird, OpenGPT3, and more, which can be fine-tuned. The [HuggingFace package](https://github.com/huggingface/) provides a repository for training many of these architectures using both PyTorch and TensorFlow.

## 🚀 Challenge

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/36)

## Review & Self Study

* [Blog post](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/), explaining the classical [Attention is all you need](https://arxiv.org/abs/1706.03762) paper on transformers.
* [A series of blog posts](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452) on transformers, explaining the architecture in detail.

## [Assignment](assignment.md)

---

