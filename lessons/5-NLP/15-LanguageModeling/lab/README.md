# Training Skip-Gram Model

Lab Assignment from [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Task

In this lab, you we challenge you to train Word2Vec model using Skip-Gram technique. Train a network with embedding to predict neighboring words in $N$-tokens-wide Skip-Gram window. You can use the [code from this lesson](../CBoW-TF.ipynb), and slightly modify it.

## The Dataset

You are welcome to use any book. You can find a lot of free texts at [Project Gutenberg](https://www.gutenberg.org/), for example, here is a direct link to [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt)) by Lewis Carroll. Or, you can use Shakespeare's plays, which you can get using the following code:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Explore!

If you have time and want to get deeper into the subject, try to explore several things:

* How does embedding size affects the results?
* How does different text styles affect the result?
* Take several very different types of words and their synonyms, obtain their vector representations, apply PCA to reduce dimensions to 2, and plot them in 2D space. Do you see any patterns?
 