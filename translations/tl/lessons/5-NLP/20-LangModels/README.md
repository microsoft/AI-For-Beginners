<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-28T02:43:02+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "tl"
}
-->
# Mga Pre-Trained na Malalaking Language Model

Sa lahat ng ating mga nakaraang gawain, sinanay natin ang isang neural network upang magsagawa ng isang partikular na gawain gamit ang labeled dataset. Sa mga malalaking transformer model, tulad ng BERT, gumagamit tayo ng language modeling sa self-supervised na paraan upang makabuo ng isang language model, na pagkatapos ay isinasapinal para sa mga tiyak na downstream na gawain sa pamamagitan ng karagdagang domain-specific na pagsasanay. Gayunpaman, napatunayan na ang mga malalaking language model ay maaari ring lutasin ang maraming gawain nang WALANG anumang domain-specific na pagsasanay. Ang pamilya ng mga modelong may kakayahang gawin ito ay tinatawag na **GPT**: Generative Pre-Trained Transformer.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/39)

## Pagbuo ng Teksto at Perplexity

Ang ideya ng isang neural network na kayang magsagawa ng mga pangkalahatang gawain nang walang downstream na pagsasanay ay ipinakita sa papel na [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Ang pangunahing ideya ay maraming iba pang mga gawain ang maaaring i-modelo gamit ang **text generation**, dahil ang pag-unawa sa teksto ay nangangahulugan din ng kakayahang makabuo nito. Dahil ang modelo ay sinanay sa napakalaking dami ng teksto na sumasaklaw sa kaalaman ng tao, nagiging pamilyar din ito sa malawak na hanay ng mga paksa.

> Ang pag-unawa at kakayahang makabuo ng teksto ay nangangahulugan din ng kaalaman tungkol sa mundo sa paligid natin. Ang mga tao ay natututo rin sa malaking bahagi sa pamamagitan ng pagbabasa, at ang GPT network ay katulad sa aspetong ito.

Ang mga text generation network ay gumagana sa pamamagitan ng paghula ng posibilidad ng susunod na salita $$P(w_N)$$. Gayunpaman, ang unconditional probability ng susunod na salita ay katumbas ng dalas ng salitang ito sa text corpus. Ang GPT ay may kakayahang magbigay ng **conditional probability** ng susunod na salita, batay sa mga naunang salita: $$P(w_N | w_{n-1}, ..., w_0)$$

> Maaari kang magbasa pa tungkol sa probabilities sa aming [Data Science for Beginners Curriculum](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)

Ang kalidad ng isang language generating model ay maaaring matukoy gamit ang **perplexity**. Isa itong intrinsic na sukatan na nagbibigay-daan sa atin upang masukat ang kalidad ng modelo nang walang anumang task-specific dataset. Batay ito sa konsepto ng *probability ng isang pangungusap* - ang modelo ay nag-a-assign ng mataas na probability sa isang pangungusap na malamang na totoo (ibig sabihin, ang modelo ay hindi **nalilito** dito), at mababang probability sa mga pangungusap na hindi gaanong makatuwiran (hal. *Can it does what?*). Kapag binigyan natin ang ating modelo ng mga pangungusap mula sa totoong text corpus, inaasahan nating magkaroon ang mga ito ng mataas na probability, at mababang **perplexity**. Sa matematika, ito ay tinutukoy bilang normalized inverse probability ng test set:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Maaari kang mag-eksperimento sa text generation gamit ang [GPT-powered text editor mula sa Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. Sa editor na ito, magsisimula kang magsulat ng iyong teksto, at sa pagpindot ng **[TAB]**, mag-aalok ito ng ilang mga opsyon para sa pagpapatuloy. Kung masyadong maikli ang mga ito, o hindi ka nasisiyahan sa mga ito - pindutin muli ang [TAB], at magkakaroon ka ng mas maraming opsyon, kabilang ang mas mahahabang piraso ng teksto.

## Ang GPT ay Isang Pamilya

Ang GPT ay hindi isang solong modelo, kundi isang koleksyon ng mga modelong binuo at sinanay ng [OpenAI](https://openai.com). 

Sa ilalim ng mga modelo ng GPT, mayroon tayo ng:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT-3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Language model na may hanggang 1.5 bilyong parameter. | Language model na may hanggang 175 bilyong parameter | 100T na parameter at tumatanggap ng parehong imahe at teksto bilang input at naglalabas ng teksto. |

Ang mga modelo ng GPT-3 at GPT-4 ay magagamit [bilang isang cognitive service mula sa Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), at bilang [OpenAI API](https://openai.com/api/).

## Prompt Engineering

Dahil ang GPT ay sinanay sa napakalaking dami ng data upang maunawaan ang wika at code, nagbibigay ito ng mga output bilang tugon sa mga input (prompts). Ang mga prompt ay mga input o query sa GPT kung saan nagbibigay ang isa ng mga tagubilin sa mga modelo tungkol sa mga gawain na kanilang susunod na tatapusin. Upang makuha ang nais na resulta, kailangan mo ng pinaka-epektibong prompt na kinabibilangan ng pagpili ng tamang mga salita, format, parirala, o kahit mga simbolo. Ang diskarteng ito ay tinatawag na [Prompt Engineering](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum).

[Ang dokumentasyong ito](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) ay nagbibigay sa iyo ng higit pang impormasyon tungkol sa prompt engineering.

## ✍️ Halimbawa ng Notebook: [Paglalaro gamit ang OpenAI-GPT](GPT-PyTorch.ipynb)

Ipagpatuloy ang iyong pag-aaral sa mga sumusunod na notebook:

* [Pagbuo ng teksto gamit ang OpenAI-GPT at Hugging Face Transformers](GPT-PyTorch.ipynb)

## Konklusyon

Ang mga bagong general pre-trained language model ay hindi lamang nagmo-modelo ng istruktura ng wika, kundi naglalaman din ng napakalaking dami ng natural na wika. Dahil dito, maaari silang epektibong magamit upang lutasin ang ilang mga gawain sa NLP sa zero-shot o few-shot na mga setting.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/40)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.