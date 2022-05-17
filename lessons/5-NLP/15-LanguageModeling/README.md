
# Language Modeling

Semantic embeddings, such as Word2Vec and GloVe, are in fact a first step towards **language modeling** - creating models that somehow *understand* (or *represent*) the nature of the language.

## [Pre-lecture quiz](tbd)

The main idea behind language modeling is training them on unlabeled datasets in an unsupervised manner. This is important because we have huge amounts of unlabeled text available, while the amount of labeled text would always be limited by the amount of effort we can spend on labeling. Most often, we can build language models that can **predict missing words** in the text, because it is easy to mask out a random word in text and use it as a training sample.

## Training Embeddings

In our previous examples, we used pre-trained semantic embeddings, but it is interesting to see how those embeddings can be trained using either CBoW, or Skip-gram architectures.

![image from paper on converting words to vectors](../14-Embeddings/images/example-algorithms-for-converting-words-to-vectors.png)

> Image from [this paper](https://arxiv.org/pdf/1301.3781.pdf)

The idea underpinning CBoW involves how to predict a missing word, but to do this we take a small sliding window of text tokens. We can denote them from W<sub>-2</sub> to W<sub>2</sub>, and train a model to predict the central word W<sub>0</sub> from a few surrounding words.

## Conclusion

TBD

## 🚀 Challenge

TBD

## [Post-lecture quiz](tbd)

## Review & Self Study

* [Official PyTorch tutorial on Language Modeling](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Official TensorFlow tutorial on training Word2Vec model](https://www.TensorFlow.org/tutorials/text/word2vec).
* Using the **gensim** framework to train most commonly used embeddings in a few lines of code is described [in this documentation](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## [Assignment: Notebooks](assignment.md) - TBD
