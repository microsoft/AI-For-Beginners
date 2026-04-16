# Mga Pre-Trained na Malalaking Language Models

Sa lahat ng ating mga nakaraang gawain, nagte-train tayo ng neural network upang maisagawa ang isang partikular na gawain gamit ang labeled dataset. Sa malalaking transformer models, tulad ng BERT, ginagamit natin ang language modelling sa self-supervised na paraan upang makabuo ng isang language model, na pagkatapos ay isinasapersonal para sa partikular na downstream task gamit ang karagdagang domain-specific na training. Gayunpaman, napatunayan na ang malalaking language models ay maaari ring magsagawa ng maraming gawain nang WALANG anumang domain-specific na training. Ang pamilya ng mga modelong may kakayahang gawin ito ay tinatawag na **GPT**: Generative Pre-Trained Transformer.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Text Generation at Perplexity

Ang ideya ng isang neural network na kayang magsagawa ng pangkalahatang gawain nang walang downstream training ay ipinakita sa [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) na papel. Ang pangunahing ideya ay maraming iba pang gawain ang maaaring i-modelo gamit ang **text generation**, dahil ang pag-unawa sa teksto ay mahalagang nangangahulugan ng kakayahang lumikha nito. Dahil ang modelo ay na-train sa napakalaking dami ng teksto na sumasaklaw sa kaalaman ng tao, nagiging maalam din ito sa iba't ibang paksa.

> Ang pag-unawa at kakayahang lumikha ng teksto ay nangangahulugan din ng kaalaman tungkol sa mundo sa paligid natin. Ang mga tao ay natututo rin sa malaking bahagi sa pamamagitan ng pagbabasa, at ang GPT network ay katulad sa aspetong ito.

Ang mga text generation networks ay gumagana sa pamamagitan ng pag-predict ng probability ng susunod na salita $$P(w_N)$$ Gayunpaman, ang unconditional probability ng susunod na salita ay katumbas ng frequency ng salitang ito sa text corpus. Ang GPT ay kayang magbigay sa atin ng **conditional probability** ng susunod na salita, batay sa mga naunang salita: $$P(w_N | w_{n-1}, ..., w_0)$$

> Maaari kang magbasa pa tungkol sa probabilities sa aming [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)

Ang kalidad ng language generating model ay maaaring tukuyin gamit ang **perplexity**. Ito ay intrinsic metric na nagbibigay-daan sa atin upang sukatin ang kalidad ng modelo nang walang anumang task-specific dataset. Batay ito sa konsepto ng *probability ng isang pangungusap* - ang modelo ay nagbibigay ng mataas na probability sa isang pangungusap na malamang na totoo (ibig sabihin, ang modelo ay hindi **perplexed** dito), at mababang probability sa mga pangungusap na hindi gaanong makatuwiran (hal. *Can it does what?*). Kapag binigyan natin ang ating modelo ng mga pangungusap mula sa totoong text corpus, inaasahan natin na magkakaroon ito ng mataas na probability, at mababang **perplexity**. Matematika, ito ay tinutukoy bilang normalized inverse probability ng test set:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Maaari kang mag-eksperimento sa text generation gamit ang [GPT-powered text editor mula sa Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. Sa editor na ito, magsisimula kang magsulat ng iyong teksto, at sa pag-pindot sa **[TAB]** ay mag-aalok ito sa iyo ng ilang mga opsyon para sa pagkompleto. Kung masyadong maikli ang mga ito, o hindi ka nasisiyahan sa mga ito - pindutin muli ang [TAB], at magkakaroon ka ng mas maraming opsyon, kabilang ang mas mahahabang piraso ng teksto.

## Ang GPT ay Isang Pamilya

Ang GPT ay hindi isang solong modelo, kundi isang koleksyon ng mga modelong binuo at na-train ng [OpenAI](https://openai.com). 

Sa ilalim ng mga GPT models, mayroon tayo:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Language model na may hanggang 1.5 bilyong parameters. | Language model na may hanggang 175 bilyong parameters | 100T parameters at tumatanggap ng parehong image at text inputs at naglalabas ng text. |


Ang mga GPT-3 at GPT-4 models ay available [bilang cognitive service mula sa Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), at bilang [OpenAI API](https://openai.com/api/).

## Prompt Engineering

Dahil ang GPT ay na-train sa napakalaking dami ng data upang maunawaan ang wika at code, nagbibigay ito ng outputs bilang tugon sa inputs (prompts). Ang prompts ay mga inputs o queries para sa GPT kung saan nagbibigay ang isa ng mga instruksyon sa mga modelo tungkol sa mga gawain na kanilang susunod na gagawin. Upang makuha ang nais na resulta, kailangan ang pinaka-epektibong prompt na kinabibilangan ng tamang pagpili ng mga salita, format, parirala, o kahit mga simbolo. Ang diskarteng ito ay tinatawag na [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)

[Ang dokumentasyong ito](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) ay nagbibigay sa iyo ng mas maraming impormasyon tungkol sa prompt engineering.

## ✍️ Halimbawa ng Notebook: [Paglalaro gamit ang OpenAI-GPT](GPT-PyTorch.ipynb)

Ipagpatuloy ang iyong pag-aaral sa mga sumusunod na notebooks:

* [Pagbuo ng teksto gamit ang OpenAI-GPT at Hugging Face Transformers](GPT-PyTorch.ipynb)

## Konklusyon

Ang mga bagong general pre-trained language models ay hindi lamang nagmo-modelo ng istruktura ng wika, kundi naglalaman din ng napakalaking dami ng natural na wika. Kaya, maaari silang epektibong magamit upang maisagawa ang ilang NLP tasks sa zero-shot o few-shot settings.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

