<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "97836d30a6bec736f8e3b4411c572bc2",
  "translation_date": "2025-11-18T18:42:53+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "pcm"
}
-->
# Pre-Trained Large Language Models

For all di tasks wey we don do before, we dey train neural network to do one kain task wey dey use labeled dataset. But wit big transformer models like BERT, we dey use language modelling for self-supervised way to build language model, wey we go later train for specific downstream task wit domain-specific training. E don show say big language models fit solve plenty tasks even witout ANY domain-specific training. Di models wey fit do dis kain thing na dem we dey call **GPT**: Generative Pre-Trained Transformer.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Text Generation and Perplexity

Di idea say neural network fit do general tasks witout downstream training dey inside [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) paper. Di main idea be say plenty other tasks fit dey modeled wit **text generation**, because to understand text mean say you fit produce am. Since di model dey trained wit plenty text wey cover human knowledge, e go sabi plenty topics.

> To understand and fit produce text mean say you sabi somtin about di world wey dey around us. People dey learn wella by reading, and GPT network dey similar for dis area.

Text generation networks dey work by predicting di probability of di next word $$P(w_N)$$. But di unconditional probability of di next word na di frequency of di word for di text corpus. GPT fit give us **conditional probability** of di next word, based on di ones wey don dey before: $$P(w_N | w_{n-1}, ..., w_0)$$

> You fit read more about probabilities for our [Data Science for Beginers Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)

Di quality of language generating model fit dey measured wit **perplexity**. E be intrinsic metric wey dey help us measure di model quality witout any task-specific dataset. E dey based on di idea of *probability of a sentence* - di model go give high probability to sentence wey fit dey real (wey mean say di model no **perplexed** by am), and low probability to sentences wey no make sense (like *Can it does what?*). If we give di model sentences from real text corpus, we go expect say dem go get high probability, and low **perplexity**. Mathematically, e dey defined as normalized inverse probability of di test set:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**You fit try text generation wit [GPT-powered text editor from Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. For dis editor, you go start to write your text, and if you press **[TAB]**, e go show you some completion options. If dem short or you no like dem - press [TAB] again, and you go see more options, including longer text.

## GPT na Family

GPT no be one model, but na group of models wey [OpenAI](https://openai.com) develop and train.

Under di GPT models, we get:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Language model wey get up to 1.5 billion parameters. | Language model wey get up to 175 billion parameters | 100T parameters wey fit accept both image and text inputs and outputs text. |

Di GPT-3 and GPT-4 models dey available [as a cognitive service from Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), and as [OpenAI API](https://openai.com/api/).

## Prompt Engineering

Because GPT don train wit plenty data to sabi language and code, e dey give outputs based on di inputs (prompts). Prompts na GPT inputs or queries wey person go use give di model instructions for di task wey e wan make e do. To get di result wey you want, you go need di best prompt wey involve choosing di correct words, formats, phrases or even symbols. Dis method na [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)

[Dis documentation](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) go give you more gist about prompt engineering.

## ✍️ Example Notebook: [Playing with OpenAI-GPT](GPT-PyTorch.ipynb)

Continue your learning wit di notebooks wey dey below:

* [Generating text with OpenAI-GPT and Hugging Face Transformers](GPT-PyTorch.ipynb)

## Conclusion

New general pre-trained language models no dey only model language structure, but dem get plenty natural language knowledge. So, dem fit dey used wella to solve some NLP tasks for zero-shop or few-shot settings.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even as we dey try make am accurate, abeg sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important mata, e good make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->