<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b708c9b85b833864c73c6281f1e6b96e",
  "translation_date": "2025-11-18T18:37:36+00:00",
  "source_file": "lessons/5-NLP/14-Embeddings/README.md",
  "language_code": "pcm"
}
-->
# Embeddings

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/27)

Wen we dey train classifiers wey base on BoW or TF/IDF, we dey use high-dimensional bag-of-words vectors wey get length `vocab_size`, and we dey change from low-dimensional positional representation vectors go sparse one-hot representation. But dis one-hot representation no dey save memory well. Plus, e dey treat each word as if dem no relate, meaning say one-hot encoded vectors no fit show any semantic similarity between words.

Di idea of **embedding** na to represent words wit lower-dimensional dense vectors, wey go somehow show di meaning of di word. Later, we go discuss how to build better word embeddings, but for now, just think say embeddings na way to reduce di size of word vector.

So, di embedding layer go take one word as input, and e go produce output vector wey get di `embedding_size` wey you set. In one way, e be like `Linear` layer, but instead of using one-hot encoded vector, e fit take word number as input, so we no go need to create big one-hot-encoded vectors.

If we use embedding layer as di first layer for our classifier network, we fit change from bag-of-words to **embedding bag** model. For here, we go first convert each word for our text into di embedding wey match am, then we go calculate one aggregate function like `sum`, `average` or `max` for all di embeddings.  

![Image showing an embedding classifier for five sequence words.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.pcm.png)

> Image by di author

## ✍️ Exercises: Embeddings

Continue to learn wit di following notebooks:
* [Embeddings with PyTorch](EmbeddingsPyTorch.ipynb)
* [Embeddings TensorFlow](EmbeddingsTF.ipynb)

## Semantic Embeddings: Word2Vec

Even though di embedding layer dey map words to vector representation, di representation no really get plenty semantical meaning. E go make sense if we fit learn vector representation wey similar words or synonyms go dey close to each other based on vector distance (like Euclidean distance).

To do dis, we need to pre-train our embedding model on big text collection in one special way. One way to train semantic embeddings na [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). E get two main architectures wey dem dey use to create distributed representation of words:

 - **Continuous bag-of-words** (CBoW) — for dis architecture, we dey train di model to predict one word from di words wey dey around am. If we get di ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$, di model go try predict $W_0$ from $(W_{-2},W_{-1},W_1,W_2)$.
 - **Continuous skip-gram** na di opposite of CBoW. Di model go use di words wey dey around di main word to predict di main word.

CBoW dey faster, but skip-gram dey slow small, though e dey represent words wey no dey common better.

![Image showing both CBoW and Skip-Gram algorithms to convert words to vectors.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.pcm.png)

> Image from [this paper](https://arxiv.org/pdf/1301.3781.pdf)

Word2Vec pre-trained embeddings (and other models like GloVe) fit replace embedding layer for neural networks. But we go need to handle vocabularies, because di vocabulary wey dem use train Word2Vec/GloVe fit no match di vocabulary for our text corpus. Check di Notebooks above to see how to solve dis problem.

## Contextual Embeddings

One big wahala wey traditional pretrained embedding representations like Word2Vec get na di problem of word sense disambiguation. Even though pretrained embeddings fit capture some meaning of words for context, dem dey put all di possible meanings of one word inside di same embedding. Dis fit cause problem for downstream models, because plenty words like 'play' get different meanings based on di context.

For example, di word 'play' for dis two sentences get different meanings:

- I go watch one **play** for di theatre.
- John wan **play** wit im friends.

Di pretrained embeddings wey we talk about before go represent di two meanings of di word 'play' as di same embedding. To solve dis problem, we need to build embeddings wey base on **language model**, wey dem don train on big text corpus, and e sabi how words dey work together for different contexts. To talk about contextual embeddings no dey inside dis tutorial, but we go come back to am wen we dey talk about language models later for di course.

## Conclusion

For dis lesson, you don learn how to build and use embedding layers for TensorFlow and Pytorch to better show di semantic meanings of words.

## 🚀 Challenge

Word2Vec don dey used for some interesting things, like creating song lyrics and poetry. Check [dis article](https://www.politetype.com/blog/word2vec-color-poems) wey explain how di author use Word2Vec to create poetry. Watch [dis video by Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) too to see another way dem explain dis technique. Then try use dis techniques for your own text corpus, maybe from Kaggle.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/28)

## Review & Self Study

Read dis paper on Word2Vec: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [Assignment: Notebooks](assignment.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am correct, abeg make you sabi say automatik transleshion fit get mistake or no dey accurate well. Di original dokyument wey dey for im native language na di one wey you go take as di main source. For important informashon, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong interpretashon wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->