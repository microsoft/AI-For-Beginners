<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "97836d30a6bec736f8e3b4411c572bc2",
  "translation_date": "2025-09-23T11:53:05+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "en"
}
-->
# Pre-Trained Large Language Models

In all of our previous tasks, we trained a neural network to perform a specific task using a labeled dataset. With large transformer models like BERT, we use language modeling in a self-supervised manner to build a language model, which is then fine-tuned for specific downstream tasks with additional domain-specific training. However, it has been shown that large language models can also solve many tasks without ANY domain-specific training. A family of models capable of this is called **GPT**: Generative Pre-Trained Transformer.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Text Generation and Perplexity

The concept of a neural network being able to perform general tasks without downstream training is introduced in the paper [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). The main idea is that many tasks can be framed as **text generation**, because understanding text essentially means being able to produce it. Since the model is trained on a massive amount of text that encompasses human knowledge, it also becomes knowledgeable about a wide range of topics.

> Understanding and being able to produce text also requires knowing something about the world around us. People also learn extensively by reading, and the GPT network is similar in this regard.

Text generation networks work by predicting the probability of the next word $$P(w_N)$$. However, the unconditional probability of the next word corresponds to the frequency of that word in the text corpus. GPT can provide the **conditional probability** of the next word, given the previous ones: $$P(w_N | w_{n-1}, ..., w_0)$$.

> You can learn more about probabilities in our [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability).

The quality of a language generation model can be measured using **perplexity**. This is an intrinsic metric that allows us to evaluate the model's quality without relying on a task-specific dataset. It is based on the concept of the *probability of a sentence*—the model assigns a high probability to a sentence that is likely to be real (i.e., the model is not **perplexed** by it) and a low probability to sentences that make less sense (e.g., *Can it does what?*). When we provide the model with sentences from a real text corpus, we expect them to have high probability and low **perplexity**. Mathematically, perplexity is defined as the normalized inverse probability of the test set:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**You can experiment with text generation using [GPT-powered text editor from Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. In this editor, you start writing your text, and pressing **[TAB]** will offer you several completion options. If the options are too short or unsatisfactory, press [TAB] again to see more options, including longer pieces of text.

## GPT is a Family

GPT is not a single model but rather a collection of models developed and trained by [OpenAI](https://openai.com). 

The GPT models include:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
| Language model with up to 1.5 billion parameters. | Language model with up to 175 billion parameters. | 100T parameters and accepts both image and text inputs, producing text outputs. |

The GPT-3 and GPT-4 models are available [as a cognitive service from Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste) and through the [OpenAI API](https://openai.com/api/).

## Prompt Engineering

Since GPT has been trained on vast amounts of data to understand language and code, it generates outputs in response to inputs (prompts). Prompts are the inputs or queries provided to GPT, where instructions are given to the model to complete specific tasks. To achieve the desired outcome, you need an effective prompt, which involves carefully selecting the right words, formats, phrases, or even symbols. This process is known as [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[This documentation](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) provides more information on prompt engineering.

## ✍️ Example Notebook: [Playing with OpenAI-GPT](GPT-PyTorch.ipynb)

Continue your learning with the following notebooks:

* [Generating text with OpenAI-GPT and Hugging Face Transformers](GPT-PyTorch.ipynb)

## Conclusion

New general pre-trained language models not only model language structure but also contain a vast amount of natural language knowledge. As a result, they can be effectively used to solve some NLP tasks in zero-shot or few-shot settings.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

