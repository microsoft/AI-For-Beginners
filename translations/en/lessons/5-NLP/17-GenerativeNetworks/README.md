<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "51be6057374d01d70e07dd5ec88ebc0d",
  "translation_date": "2025-09-23T11:52:13+00:00",
  "source_file": "lessons/5-NLP/17-GenerativeNetworks/README.md",
  "language_code": "en"
}
-->
# Generative Networks

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/33)

Recurrent Neural Networks (RNNs) and their gated cell variants, such as Long Short Term Memory Cells (LSTMs) and Gated Recurrent Units (GRUs), provide a mechanism for language modeling by learning word order and predicting the next word in a sequence. This makes RNNs suitable for **generative tasks**, such as text generation, machine translation, and even image captioning.

> ✅ Think about all the times you've benefited from generative tasks like text completion while typing. Research your favorite applications to see if they use RNNs.

In the RNN architecture discussed in the previous unit, each RNN unit produced the next hidden state as output. However, we can also add another output to each recurrent unit, enabling the generation of a **sequence** (equal in length to the original sequence). Additionally, we can use RNN units that do not take input at each step but instead start with an initial state vector and produce a sequence of outputs.

This enables different neural architectures, as shown in the image below:

![Image showing common recurrent neural network patterns.](../../../../../translated_images/en/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.jpg)

> Image from the blog post [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) by [Andrej Karpathy](http://karpathy.github.io/)

* **One-to-one**: A traditional neural network with one input and one output.
* **One-to-many**: A generative architecture that takes one input value and generates a sequence of output values. For example, in **image captioning**, we can input an image, pass it through a CNN to obtain its hidden state, and then use a recurrent chain to generate a caption word by word.
* **Many-to-one**: Corresponds to the RNN architectures described in the previous unit, such as text classification.
* **Many-to-many**, or **sequence-to-sequence**: Used for tasks like **machine translation**, where one RNN collects information from the input sequence into the hidden state, and another RNN chain unrolls this state into the output sequence.

In this unit, we will focus on simple generative models for text generation. For simplicity, we will use character-level tokenization.

We will train an RNN to generate text step by step. At each step, we will take a sequence of characters of length `nchars` and ask the network to generate the next output character for each input character:

![Image showing an example RNN generation of the word 'HELLO'.](../../../../../translated_images/en/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.png)

When generating text (during inference), we start with a **prompt**, which is passed through RNN cells to generate its intermediate state. From this state, the generation begins. We generate one character at a time, passing the state and the generated character to another RNN cell to generate the next one, until we have generated enough characters.

<img src="images/rnn-generate-inf.png" width="60%"/>

> Image by the author

## ✍️ Exercises: Generative Networks

Continue your learning in the following notebooks:

* [Generative Networks with PyTorch](GenerativePyTorch.ipynb)
* [Generative Networks with TensorFlow](GenerativeTF.ipynb)

## Soft Text Generation and Temperature

The output of each RNN cell is a probability distribution of characters. If we always select the character with the highest probability as the next character in the generated text, the text can often become repetitive, cycling through the same sequences of characters, as shown in this example:

```
today of the second the company and a second the company ...
```


However, if we examine the probability distribution for the next character, the difference between the highest probabilities might not be significant. For instance, one character might have a probability of 0.2, while another has 0.19. For example, when predicting the next character in the sequence '*play*', the next character could just as likely be a space or **e** (as in the word *player*).

This suggests that it is not always "fair" to select the character with the highest probability, as choosing the second-highest might still produce meaningful text. A better approach is to **sample** characters from the probability distribution provided by the network output. We can also use a parameter called **temperature** to adjust the probability distribution. A higher temperature adds more randomness, while a lower temperature makes the distribution steeper, favoring the highest-probability characters.

Explore how this soft text generation is implemented in the notebooks linked above.

## Conclusion

While text generation can be useful on its own, its major benefits come from the ability to generate text using RNNs from an initial feature vector. For example, text generation is used in machine translation (sequence-to-sequence, where the state vector from the *encoder* is used to generate or *decode* the translated message) or in generating textual descriptions of images (where the feature vector comes from a CNN extractor).

## 🚀 Challenge

Take some lessons on Microsoft Learn on this topic:

* Text Generation with [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/34)

## Review & Self Study

Here are some articles to expand your knowledge:

* Different approaches to text generation with Markov Chain, LSTM, and GPT-2: [blog post](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Text generation example in the [Keras documentation](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Assignment](lab/README.md)

We have seen how to generate text character by character. In the lab, you will explore word-level text generation.

---

