# Pre-Trained Large Language Models

In all of our previous tasks, we were training a neural network to perform a certain task using labeled dataset. With large transformer models, such as BERT, we use language modelling in self-supervised fashion to build a language model, which is then specialized for specific downstream task with further domain-specific training. However, it has been demonstrated that large language models can also solve many tasks without ANY domain-specific training. A family of models capable of doing that is called **GPT**: Generative Pre-Trained Transformer.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Text Generation and Perplexity

The idea of a neural network being able to do general tasks without downstream training is presented in [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) paper. The main idea is the many other tasks can be modeled using **text generation**, because understanding text essentially means being able to produce it. Because the model is trained on a huge amount of text that encompasses human knowledge, it also becomes knowledgeable about wide variety of subjects.

> Understanding and being able to produce text also entails knowing something about the world around us. People  also learn by reading to the large extent, and GPT network is similar in this respect.

Text generation networks work by predicting probability of the next word $$P(w_N)$$ However, unconditional probability of the next word equals to the frequency of the this word in the text corpus. GPT is able to give us **conditional probability** of the next word, given the previous ones: $$P(w_N | w_{n-1}, ..., w_0)$$

> You can read more about probabilities in our [Data Science for Beginers Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)

Quality of language generating model can be defined using **perplexity**. It is intrinsic metric that allows us to measure the model quality without any task-specific dataset. It is based on the notion of *probability of a sentence* - the model assigns high probability to a sentence that is likely to be real (i.e. the model is not **perplexed** by it), and low probability to sentences that make less sense (eg. *Can it does what?*). When we give our model sentences from real text corpus, we would expect them to have high probability, and low **perplexity**. Mathematically, it is defined as normalized inverse probability of the test set:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**You can experiment with text generation using [GPT-powered text editor from Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. In this editor, you start writing your text, and pressing **[TAB]** will offer you several completion options. If they are too short, or you are not satisfied with them - press [TAB] again, and you will have more options, including longer pieces of text.

## GPT is a Family

GPT is not a single model, but rather a collection of models developed and trained by [OpenAI](https://openai.com). 

Under the GPT models, we have:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Language model with upto 1.5 billion parameters. | Language model with up to 175 billion parameters | 100T parameters and accepts both image and text inputs and outputs text. |


The GPT-3 and GPT-4 models are available [as a cognitive service from Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), and as [OpenAI API](https://openai.com/api/).

## Prompt Engineering

Because GPT has been trained on a vast volumes of data to understand language and code, they provide outputs in response to inputs (prompts). Prompts are GPT inputs or queries whereby one provides instructions to models on tasks they next completed. To elicit a desired outcome, you need the most effective prompt which involves selecting the right words, formats, phrases or even symbols. This approach is [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)

[This documentation](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) provides you with more information on prompt engineering.

## ✍️ Example Notebook: [Playing with OpenAI-GPT](GPT-PyTorch.ipynb)

Continue your learning in the following notebooks:

* [Generating text with OpenAI-GPT and Hugging Face Transformers](GPT-PyTorch.ipynb)

## Conclusion

New general pre-trained language models do not only model language structure, but also contain vast amount of natural language. Thus, they can be effectively used to solve some NLP tasks in zero-shop or few-shot settings.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)
