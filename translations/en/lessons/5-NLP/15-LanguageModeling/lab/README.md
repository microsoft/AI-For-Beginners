<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5130f01fdc5ebb83032b23d489027aac",
  "translation_date": "2025-08-31T17:56:38+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/lab/README.md",
  "language_code": "en"
}
-->
# Training Skip-Gram Model

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

In this lab, your challenge is to train a Word2Vec model using the Skip-Gram technique. Train a network with embeddings to predict neighboring words within an $N$-token-wide Skip-Gram window. You can use the [code from this lesson](../CBoW-TF.ipynb) and make slight modifications to it.

## The Dataset

You are free to use any book. A large collection of free texts is available at [Project Gutenberg](https://www.gutenberg.org/). For example, here’s a direct link to [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt) by Lewis Carroll. Alternatively, you can use Shakespeare's plays, which you can download using the following code:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Explore!

If you have extra time and want to dive deeper into the topic, try exploring the following:

* How does the size of the embedding affect the results?
* How do different writing styles influence the outcome?
* Select several very distinct types of words along with their synonyms, obtain their vector representations, apply PCA to reduce the dimensions to 2, and plot them in a 2D space. Do you notice any patterns?

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.