<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-31T17:47:08+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "en"
}
-->
> Image by [Dmitry Soshnikov](http://soshnikov.com)

As time progressed, computing resources became more affordable, and larger datasets became accessible, allowing neural network approaches to demonstrate remarkable performance in competing with humans in various domains, such as computer vision and speech recognition. Over the past decade, the term Artificial Intelligence has often been used interchangeably with Neural Networks, as most of the notable AI achievements we hear about are based on these technologies.

We can observe the evolution of approaches in creating chess-playing computer programs:

* Early chess programs relied on search algorithms, explicitly estimating possible moves of an opponent for a given number of future moves and selecting the optimal move based on the best achievable position within those moves. This led to the development of the [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) search algorithm.
* Search strategies proved effective toward the end of the game, where the search space is limited by fewer possible moves. However, at the beginning of the game, the search space is vast, and the algorithm was improved by learning from existing matches between human players. Later experiments employed [case-based reasoning](https://en.wikipedia.org/wiki/Case-based_reasoning), where the program searched for cases in its knowledge base that closely resembled the current game position.
* Modern programs that outperform human players are based on neural networks and [reinforcement learning](https://en.wikipedia.org/wiki/Reinforcement_learning). These programs learn to play by repeatedly playing against themselves and learning from their mistakes—similar to how humans learn to play chess. However, a computer program can play far more games in a much shorter time, enabling it to learn much faster.

✅ Research other games that AI has successfully played.

Similarly, we can observe the evolution of approaches in creating "talking programs" that might pass the Turing test:

* Early programs like [Eliza](https://en.wikipedia.org/wiki/ELIZA) were based on simple grammatical rules and reformulated input sentences into questions.
* Modern assistants, such as Cortana, Siri, or Google Assistant, are hybrid systems that use neural networks to convert speech into text, recognize user intent, and then employ reasoning or explicit algorithms to perform the required actions.
* In the future, we may see fully neural-based models capable of handling dialogue independently. Recent advancements in neural networks, such as GPT and [Turing-NLG](https://turing.microsoft.com/), have shown significant success in this area.

> Image by Dmitry Soshnikov, [photo](https://unsplash.com/photos/r8LmVbUKgns) by [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Recent AI Research

The rapid growth in neural network research began around 2010, when large public datasets became accessible. A massive collection of images called [ImageNet](https://en.wikipedia.org/wiki/ImageNet), containing approximately 14 million annotated images, led to the creation of the [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![ILSVRC Accuracy](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Image by [Dmitry Soshnikov](http://soshnikov.com)

In 2012, [Convolutional Neural Networks](../4-ComputerVision/07-ConvNets/README.md) were first applied to image classification, resulting in a significant reduction in classification errors (from nearly 30% to 16.4%). By 2015, Microsoft's ResNet architecture [achieved human-level accuracy](https://doi.org/10.1109/ICCV.2015.123).

Since then, Neural Networks have shown remarkable success across various tasks:

---

Year | Human Parity achieved
-----|--------
2015 | [Image Classification](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Conversational Speech Recognition](https://arxiv.org/abs/1610.05256)
2018 | [Automatic Machine Translation](https://arxiv.org/abs/1803.05567) (Chinese-to-English)
2020 | [Image Captioning](https://arxiv.org/abs/2009.13682)

In recent years, we've seen significant advancements with large language models like BERT and GPT-3. This progress is largely due to the abundance of general text data, which enables training models to understand the structure and meaning of text, pre-train them on broad text collections, and then fine-tune them for specific tasks. We'll explore more about [Natural Language Processing](../5-NLP/README.md) later in this course.

## 🚀 Challenge

Explore the internet to identify where, in your opinion, AI is being used most effectively. Is it in a mapping application, a speech-to-text service, or a video game? Investigate how the system was developed.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Review & Self Study

Review the history of AI and ML by reading through [this lesson](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Choose an element from the sketchnote at the beginning of that lesson or this one, and research it further to understand the cultural context behind its development.

**Assignment**: [Game Jam](assignment.md)

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.