# Named Entity Recognition

Up to now, we have mostly been concentrating on one NLP task - classification. However, there are also other NLP tasks that can be accomplished with neural networks. One of those tasks is **[Named Entity Recognition](https://en.wikipedia.org/wiki/Named-entity_recognition)** (NER), which deals with recognizing specific entities within text, such as places, person names, date-time intervals, chemical formulae and so on.

## [Pre-lecture quiz](https://black-ground-0cc93280f.1.azurestaticapps.net/quiz/119) 

## Example of Using NER

Suppose you want to develop a natural language chat bot, similar to Amazon Alexa or Google Assistant. The way intelligent chat bots work is to *understand* what the user want by doing text classification on the input sentence. The result of this classification is so-called **intent**, which determines what a chat bot should do.

![Bot NER](images/bot-ner.png)

> Image by author

However, a user may provide some parameters as part of the phrase. For example, when asking for a weather, she may specify a location or date. A bot should be able to understand those entities, and fill in the parameter slots accordingly before performing the action. This is exactly when NER comes in. 

Another example would be [analyzing scientific medical papers](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/), one of the main things we need to look for are specific medical terms, such as diseases and medical substances. While a small number of diseases can probably be extracted using substring search, more complex entities, such as chemical compounds and medication names, need more complex approach.

## NER as Token Classification

NER models are essentially **token classification models**, because for each of the input tokens we need to decide whether it belongs to an entity or not, and if it does - to which entity class.

Consider the following paper title:

**Tricuspid valve regurgitation** and **lithium carbonate** **toxicity** in a newborn infant.

Entities here are:
* Tricuspid valve regurgitation is a disease (`DIS`)
* Lithium carbonate is a chemical substance (`CHEM`)
* Toxicity is also a disease (`DIS`)

Notice that one entity can span several tokens. And, as in this case, we need to distinguish between two consecutive entities. Thus it is common to use two classes for each entity - one specifying the first token of the entity (often `B-` prefix is used, for beginning), and another - the continuation of an entity (`I-`, for inner token). We also use `O` as a class to represent all other tokens. Such token tagging is called [BIO tagging](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (or IOB). When tagged, our title will look like this:

Token | Tag
------|-----
Tricuspid | B-DIS
valve | I-DIS
regurgitation | I-DIS
and | O
lithium | B-CHEM
carbonate | I-CHEM
toxicity | B-DIS
in | O
a | O
newborn | O
infant | O
. | O

Since we need to build one-to-one correspondence between tokens and this classes, we can train rightmost **many-to-many** neural network model from this picture:

![Image showing common recurrent neural network patterns.](../17-GenerativeNetworks/images/unreasonable-effectiveness-of-rnn.jpg)

> *Image from blog post [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) by [Andrej Karpaty](http://karpathy.github.io/). NER token classification models correspond to right-most network architecture on this picture.*

## Training NER models

Since NER model is essentially a token classification model, we can use RNNs that we are already familiar with for this task. In this case, each block of recurrent network will return the token ID. Example notebook shows how to train LSTM for token classification.

## ✍️ Example Notebooks: NER

Continue your learning in the following notebooks:

* [NER with TensorFlow](NER-TF.ipynb)

## [Assignment](lab/README.md)

In the assignment for this lesson, you will have to train medical entity recognition model. You can start with training LSTM model as described in this lesson, and proceed with using BERT transformer model. Read [the instructions](lab/README.md) to get all the details.

