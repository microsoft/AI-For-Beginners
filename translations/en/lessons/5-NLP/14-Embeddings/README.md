<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e40b47ac3fd48f71304ede1474e66293",
  "translation_date": "2025-08-31T18:00:47+00:00",
  "source_file": "lessons/5-NLP/14-Embeddings/README.md",
  "language_code": "en"
}
-->
# Embeddings

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/27)

When training classifiers using BoW or TF/IDF, we worked with high-dimensional bag-of-words vectors of length `vocab_size`, explicitly converting low-dimensional positional representation vectors into sparse one-hot representations. However, this one-hot representation is not memory-efficient. Additionally, each word is treated independently, meaning one-hot encoded vectors do not capture any semantic similarity between words.

The concept of **embedding** is to represent words as lower-dimensional dense vectors that reflect the semantic meaning of a word. We will later explore how to create meaningful word embeddings, but for now, think of embeddings as a way to reduce the dimensionality of a word vector.

An embedding layer takes a word as input and produces an output vector of a specified `embedding_size`. In essence, it is similar to a `Linear` layer, but instead of taking a one-hot encoded vector, it can take a word number as input, avoiding the need to create large one-hot-encoded vectors.

By using an embedding layer as the first layer in our classifier network, we can transition from a bag-of-words model to an **embedding bag** model. Here, we first convert each word in our text into its corresponding embedding and then compute an aggregate function over all those embeddings, such as `sum`, `average`, or `max`.

![Image showing an embedding classifier for five sequence words.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.en.png)

> Image by the author

## ✍️ Exercises: Embeddings

Continue your learning in the following notebooks:
* [Embeddings with PyTorch](EmbeddingsPyTorch.ipynb)
* [Embeddings TensorFlow](EmbeddingsTF.ipynb)

## Semantic Embeddings: Word2Vec

While the embedding layer maps words to vector representations, these representations may not necessarily carry much semantic meaning. Ideally, we want a vector representation where similar words or synonyms correspond to vectors that are close to each other in terms of some vector distance (e.g., Euclidean distance).

To achieve this, we need to pre-train our embedding model on a large text corpus in a specific way. One method for training semantic embeddings is called [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). It is based on two main architectures for producing distributed word representations:

 - **Continuous bag-of-words** (CBoW) — In this architecture, the model is trained to predict a word based on its surrounding context. Given the n-gram $(W_{-2},W_{-1},W_0,W_1,W_2)$, the model's goal is to predict $W_0$ using $(W_{-2},W_{-1},W_1,W_2)$.
 - **Continuous skip-gram** — This is the opposite of CBoW. The model uses the surrounding context words to predict the current word.

CBoW is faster, while skip-gram is slower but better at representing infrequent words.

![Image showing both CBoW and Skip-Gram algorithms to convert words to vectors.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.en.png)

> Image from [this paper](https://arxiv.org/pdf/1301.3781.pdf)

Pre-trained Word2Vec embeddings (and similar models like GloVe) can also replace the embedding layer in neural networks. However, handling vocabularies is necessary because the vocabulary used to pre-train Word2Vec/GloVe may differ from the vocabulary in our text corpus. Check the above notebooks to learn how to address this issue.

## Contextual Embeddings

A key limitation of traditional pre-trained embeddings like Word2Vec is the issue of word sense disambiguation. While pre-trained embeddings can capture some contextual meaning of words, all possible meanings of a word are encoded into the same embedding. This can create problems in downstream models, as many words, such as "play," have different meanings depending on the context.

For example, the word "play" has distinct meanings in these two sentences:

- I went to a **play** at the theatre.
- John wants to **play** with his friends.

The pre-trained embeddings mentioned earlier represent both meanings of "play" in the same embedding. To address this limitation, we need to build embeddings based on a **language model**, which is trained on a large text corpus and *understands* how words are used in different contexts. While discussing contextual embeddings is beyond the scope of this tutorial, we will revisit them when we cover language models later in the course.

## Conclusion

In this lesson, you learned how to build and use embedding layers in TensorFlow and PyTorch to better capture the semantic meanings of words.

## 🚀 Challenge

Word2Vec has been applied to some fascinating projects, such as generating song lyrics and poetry. Check out [this article](https://www.politetype.com/blog/word2vec-color-poems), which explains how the author used Word2Vec to create poetry. Also, watch [this video by Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) for another explanation of this technique. Then, try applying these methods to your own text corpus, perhaps sourced from Kaggle.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/28)

## Review & Self Study

Read this paper on Word2Vec: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [Assignment: Notebooks](assignment.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.