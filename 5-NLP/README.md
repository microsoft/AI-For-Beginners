# Natural Language Processing

In this section, we will focus on using Neural Networks to handle tasks related to natural language processing (NLP). There are many NLP problems that we want computers to be able to solve:

* **Text classification** is typical classification problem on text sequences. Examples include classifying e-mail messages on spam vs. no-spam, or attributing news article into one of the pre-defined categories (sport, business, politics, etc.). Also, when developing chat bots, we often need to understand what a used wanted to say -- in this case we are dealing with **intent classificaton**. Often, in intent classification we need to deal with many categories.
* **Sentiment analysis** is typical regression problem, where we need to attribute a number -- sentiment -- corresponding to how positive/negative the meaning of a sentence is. More advanced version of sentiment analysis is **aspect-based sentiment analysis** (ABSA), where we attribute sentiment not the the whole sentence, but to different parts of it (aspects), eg. *In this restaurant, I liked the cuisine, but the atmosphere was awful*.
* **Named Entity Recognition** (NER) refers to the problem of extracting certain entities from text. For example, we might need to understand that in the phrase *I need to fly to Paris tomorrow* the word *tomorrow* refers to DATE, and *Paris* is a LOCATION.  
* **Keyword extraction** is similar to NER, but we need to extract words important to the meaning of the sentence automatically, without pre-training for specific entity types.
* **Text clustering** can be useful when we want to group together similar sentences, for example, similar requests in technical support conversations.
* **Question answering** refers to the ability of a model to answer a specific question. The model receives a text passage and a question as inputs, and it needs to provide a place in the text where the answer to the question is contained (or, sometimes, to generate the answer text).
* **Text Generation** is the ability of a model to generate new text. It can be considered as classification task that predicts next letter/word based on some *text prompt*. Advanced text generation models, such as GPT-3, are able to solve other NLP tasks such as classification using a technique called [prompt programming](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0) or [prompt engineering](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29)
* **Text summarization** is a technique when we want a computer to "read" long text, and summarize it in a few sentences.
* **Machine translation** can be viewed as a combination of text understanding in one language, and text generation in another one.

Initially, most of NLP tasks were solved using traditional methods such as grammars. For example, in machine translation parsers were used to transform initial sentence into a syntax tree, then higher level semantic structures were extracted to represent the meaning of the sentence, and based on this meaning and grammar of the target language the result was generated. Nowadays, many NLP tasks are more effectively solved using neural networks.

Many classical NLP methods are implemented in [Natural Language Processing Toolkit (NLTK)](https://www.nltk.org) Python library. There is a great [NLTK Book](https://www.nltk.org/book/) available online that covers how different NLP tasks can be solved using NLTK.

In our course, we will mostly focus on using Neural Networks for NLP, and we will use NLTK where needed.

We have already learnt about using neural networks for dealing with tabular data and with images. The main difference between those types of data and text is that text is a sequence of variable length, while the input size in case of images is known in advance. While convolutional networks can extract patterns from input data, patterns in text are more complex. Eg., we can have negation being separated from the subject be arbitrary many words (eg. *I do not like organges*, vs. *I do not like those big colorful tasty oranges*), and that should still be interpreted as one pattern. Thus, to handle language we need to introduce new neural network types, such as *recurrent networks* and *transformers*. 

## Install Libraries

If you are using local Python installation to run this course, you may need to install all required libraries for NLP using the following commands:

**For PyTorch**
```bash
pip install -r requirements-torch.txt
```
**For Tensorflow**
```bash
pip install -r requirements-tf.txt
```

## Contents

* [Representing text as tensors](13-TextRep/README.md)
* [Word Embeddings](14-Emdeddings/README.md)
