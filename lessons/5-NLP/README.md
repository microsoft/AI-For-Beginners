# Natural Language Processing

![Summary of NLP tasks in a doodle](../sketchnotes/ai-nlp.png)

In this section, we will focus on using Neural Networks to handle tasks related to **Natural Language Processing (NLP)**. There are many NLP problems that we want computers to be able to solve:

* **Text classification** is a typical classification problem pertaining to text sequences. Examples include classifying e-mail messages as spam vs. no-spam, or categorizing articles as sport, business, politics, etc. Also, when developing chat bots, we often need to understand what a user wanted to say -- in this case we are dealing with **intent classification**. Often, in intent classification we need to deal with many categories.
* **Sentiment analysis** is a typical regression problem, where we need to attribute a number (a sentiment) corresponding to how positive/negative the meaning of a sentence is. A more advanced version of sentiment analysis is **aspect-based sentiment analysis** (ABSA), where we attribute sentiment not to the whole sentence, but to different parts of it (aspects), eg. *In this restaurant, I liked the cuisine, but the atmosphere was awful*.
* **Named Entity Recognition** (NER) refers to the problem of extracting certain entities from text. For example, we might need to understand that in the phrase *I need to fly to Paris tomorrow* the word *tomorrow* refers to DATE, and *Paris* is a LOCATION.  
* **Keyword extraction** is similar to NER, but we need to extract words important to the meaning of the sentence automatically, without pre-training for specific entity types.
* **Text clustering** can be useful when we want to group together similar sentences, for example, similar requests in technical support conversations.
* **Question answering** refers to the ability of a model to answer a specific question. The model receives a text passage and a question as inputs, and it needs to provide a place in the text where the answer to the question is contained (or, sometimes, to generate the answer text).
* **Text Generation** is the ability of a model to generate new text. It can be considered as classification task that predicts next letter/word based on some *text prompt*. Advanced text generation models, such as GPT-3, are able to solve other NLP tasks such as classification using a technique called [prompt programming](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0) or [prompt engineering](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29)
* **Text summarization** is a technique when we want a computer to "read" long text and summarize it in a few sentences.
* **Machine translation** can be viewed as a combination of text understanding in one language, and text generation in another one.

Initially, most of NLP tasks were solved using traditional methods such as grammars. For example, in machine translation parsers were used to transform initial sentence into a syntax tree, then higher level semantic structures were extracted to represent the meaning of the sentence, and based on this meaning and grammar of the target language the result was generated. Nowadays, many NLP tasks are more effectively solved using neural networks.

> Many classical NLP methods are implemented in [Natural Language Processing Toolkit (NLTK)](https://www.nltk.org) Python library. There is a great [NLTK Book](https://www.nltk.org/book/) available online that covers how different NLP tasks can be solved using NLTK.

In our course, we will mostly focus on using Neural Networks for NLP, and we will use NLTK where needed.

We have already learned about using neural networks for dealing with tabular data and with images. The main difference between those types of data and text is that text is a sequence of variable length, while the input size in case of images is known in advance. While convolutional networks can extract patterns from input data, patterns in text are more complex. Eg., we can have negation being separated from the subject be arbitrary for many words (eg. *I do not like oranges*, vs. *I do not like those big colorful tasty oranges*), and that should still be interpreted as one pattern. Thus, to handle language we need to introduce new neural network types, such as *recurrent networks* and *transformers*.

## Install Libraries

If you are using local Python installation to run this course, you may need to install all required libraries for NLP using the following commands:

**For PyTorch**
```bash
pip install -r requirements-torch.txt
```
**For TensorFlow**
```bash
pip install -r requirements-tf.txt
```

> You can try NLP with TensorFlow on [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/?WT.mc_id=academic-77998-cacaste)

## GPU Warning

In this section, in some of the examples we will be training quite large models.
* **Use a GPU-Enabled Computer**: It's advisable to run your notebooks on a GPU-enabled computer to reduce waiting times when working with large models.
* **GPU Memory Constraints**: Running on a GPU may lead to situations where you run out of GPU memory, especially when training large models.
* **GPU Memory Consumption**: The amount of GPU memory consumed during training depends on various factors, including the minibatch size.
* **Minimize Minibatch Size**: If you encounter GPU memory issues, consider reducing the minibatch size in your code as a potential solution.
* **TensorFlow GPU Memory Release**: Older versions of TensorFlow may not release GPU memory correctly when training multiple models within one Python kernel. To manage GPU memory usage effectively, you can configure TensorFlow to allocate GPU memory only as needed.
* **Code Inclusion**: To set TensorFlow to grow GPU memory allocation only when required, include the following code in your notebooks:

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
```

If you're interested in learning about NLP from a classic ML perspective, visit [this suite of lessons](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP)

## In this Section
In this section we will learn about:

* [Representing text as tensors](13-TextRep/README.md)
* [Word Embeddings](14-Emdeddings/README.md)
* [Language Modeling](15-LanguageModeling/README.md)
* [Recurrent Neural Networks](16-RNN/README.md)
* [Generative Networks](17-GenerativeNetworks/README.md)
* [Transformers](18-Transformers/README.md)
