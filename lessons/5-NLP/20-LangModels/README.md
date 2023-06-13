# Pre-Trained Large Language Models

In all of our previous tasks, we were training a neural network to perform a certain task using labeled dataset. With large transformer models, such as BERT, we use language modelling in self-supervised fashion to build a language model, which is then specialized for specific downstream task with further domain-specific training. However, it has been demonstrated that large language models can also solve many tasks without ANY domain-specific training. A family of models capable of doing that is called **GPT**: Generative Pre-Trained Transformer.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Text Generation and Perplexity

The idea of a neural network being able to do general tasks without downstream training is presented in [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) paper. The main idea is the many other tasks can be modeled using **text generation**, because understanding text essentially means being able to produce it. Because the model is trained on a huge amount of text that encompasses human knowledge, it also becomes knowledgeable about wide variety of subjects.

> Understanding and being able to produce text also entails knowing something about the world around us. People  also learn by reading to the large extent, and GPT network is similar in this respect.

Text generation networks work by predicting probability of the next word $P(w_N)$. However, unconditional probability of the next word equals to the frequency of the this word in the text corpus. GPT is able to give us **conditional probability** of the next word, given the previous ones $P(w_N | w_{n-1}, ..., w_0)$.

> You can read more about probabilities in our [Data Science for Beginers Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)

Quality of language generating model can be defined using **perplexity**. It is intrinsic metric that allows us to measure the model quality without any task-specific dataset. It is based on the notion of *probability of a sentence* - the model assigns high probability to a sentence that is likely to be real (i.e. the model is not **perplexed** by it), and low probability to sentences that make less sense (eg. *Can it does what?*). When we give our model sentences from real text corpus, we would expect them to have high probability, and low **perplexity**. Mathematically, it is defined as normalized inverse probability of the test set:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**You can experiment with text generation using [GPT-powered text editor from Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. In this editor, you start writing your text, and pressing **[TAB]** will offer you several completion options. If they are too short, or you are not satisfied with them - press [TAB] again, and you will have more options, including longer pieces of text.

## GPT is a Family

GPT is not a single model, but rather a collection of models developed and trained by [OpenAI](http://openai.org). The latest model openly available is [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2), which has up to 1.5 billion parameters (there are several variations of the model, so you can select one for your tasks that is a good compromise between size/performance). Latest GPT-3 model has up to 175 billion parameters, and is available [as a cognitive service from Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), and as [OpenAI API](https://openai.com/api/).

## Prompt-based Inference

Because GPT has been trained on a vast volumes of data, it has some commonsense knowledge embedded directly inside the model. This allows us to force GPT to solve certain typical problems by just providing the right prompt. This presents a whole new approach for using pre-trained models, called [Prompt Engineering](https://en.wikipedia.org/wiki/Prompt_engineering). It is particularly useful with GPT-3, which has significantly more parameters, and consequently more embedded knowledge.

Here are a few example of using Prompt Engineering (answers from the model are *in italics*):

**Recommendation Systems**:<br/>
People, who liked the movie "The Matrix" also liked *Star Wars, Jupyter Ascending, Ex Machina*

**Translation**:<br/>
Translate from English to French:<br/>
cat => chat, dog => chien, student => *étudiant*

**Looking for words:**<br/>
Synonyms of a word cat: *feline, feline form, feline spirit*

[This article](https://www.gwern.net/GPT-3#prompts-as-programming) talks more about prompt engineering.

## ✍️ Example Notebook: [Playing with GPT-2](GPT-PyTorch.ipynb)

Continue your learning in the following notebooks:

* [Generating text with GPT-2 and Hugging Face Transformers](GPT-PyTorch.ipynb)

## Conclusion

New general pre-trained language models do not only model language structure, but also contain vast amount of commonsense knowledge. Thus, they can be effectively used to solve some NLP tasks in zero-shop or few-shot settings.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)
