<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7ba20f54a5bfcd6521018cdfb17c7c57",
  "translation_date": "2025-11-18T18:41:06+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "pcm"
}
-->
# Language Modeling

Semantic embeddings like Word2Vec and GloVe na di first step wey dey lead to **language modeling** - wey mean say we dey create models wey fit *understand* (or *represent*) how language dey work.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/29)

Di main idea for language modeling na to train am for datasets wey no get label in an unsupervised way. Dis one dey important because we get plenty text wey no get label, but di amount of labeled text go always dey small because of di effort wey e go take to label am. Most times, we fit build language models wey fit **predict missing words** for text, because e dey easy to cover one random word for text and use am as training sample.

## Training Embeddings

For di examples wey we don do before, we use pre-trained semantic embeddings, but e go dey interesting to see how dem dey train di embeddings. Plenty ideas dey wey we fit use:

* **N-Gram** language modeling, wey mean say we go predict one token by looking di N tokens wey dey before am (N-gram).
* **Continuous Bag-of-Words** (CBoW), wey mean say we go predict di middle token $W_0$ for one token sequence $W_{-N}$, ..., $W_N$.
* **Skip-gram**, wey mean say we go predict set of neighboring tokens {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} from di middle token $W_0$.

![image from paper on converting words to vectors](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.pcm.png)

> Image from [this paper](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Example Notebooks: Training CBoW model

Make you continue your learning for di notebooks wey dey below:

* [Training CBoW Word2Vec with TensorFlow](CBoW-TF.ipynb)
* [Training CBoW Word2Vec with PyTorch](CBoW-PyTorch.ipynb)

## Conclusion

For di last lesson, we don see say word embeddings dey work like magic! Now we sabi say to train word embeddings no too hard, and we fit train our own word embeddings for domain-specific text if e dey necessary.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Review & Self Study

* [Official PyTorch tutorial on Language Modeling](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Official TensorFlow tutorial on training Word2Vec model](https://www.TensorFlow.org/tutorials/text/word2vec).
* How to use di **gensim** framework to train di most common embeddings with just few lines of code dey described [for dis documentation](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Assignment: Train Skip-Gram Model](lab/README.md)

For di lab, we dey challenge you to change di code from dis lesson to train skip-gram model instead of CBoW. [Read di details](lab/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg make you sabi say machine translation fit get mistake or no dey correct well. Di original dokyument wey dey for di native language na di main source wey you go trust. For important information, e good make professional human translator check am. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->