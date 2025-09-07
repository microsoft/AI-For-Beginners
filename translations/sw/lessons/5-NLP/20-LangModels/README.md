<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2efbb183384a50f0fc0cde02534d912f",
  "translation_date": "2025-08-25T22:05:57+00:00",
  "source_file": "lessons/5-NLP/20-LangModels/README.md",
  "language_code": "sw"
}
-->
# Miundo Mikubwa ya Lugha Iliyofunzwa Kabla

Katika kazi zetu zote za awali, tulikuwa tunafundisha mtandao wa neva kufanya kazi fulani kwa kutumia seti ya data yenye lebo. Kwa miundo mikubwa ya transformer, kama BERT, tunatumia uundaji wa lugha kwa njia ya kujifunza binafsi ili kujenga mfano wa lugha, ambao baadaye unataalam kwa kazi maalum za chini kwa mafunzo zaidi ya kikoa maalum. Hata hivyo, imeonyeshwa kuwa miundo mikubwa ya lugha inaweza pia kutatua kazi nyingi bila mafunzo yoyote maalum ya kikoa. Familia ya miundo inayoweza kufanya hivyo inaitwa **GPT**: Generative Pre-Trained Transformer.

## [Jaribio la Kabla ya Somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/120)

## Uundaji wa Maandishi na Perplexity

Wazo la mtandao wa neva kuwa na uwezo wa kufanya kazi za jumla bila mafunzo ya chini linaonyeshwa katika karatasi ya [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf). Wazo kuu ni kwamba kazi nyingine nyingi zinaweza kuundwa kwa kutumia **uundaji wa maandishi**, kwa sababu kuelewa maandishi kimsingi kunamaanisha kuwa na uwezo wa kuyazalisha. Kwa sababu mfano umefundishwa kwa kiasi kikubwa cha maandishi yanayojumuisha maarifa ya binadamu, pia unakuwa na maarifa kuhusu mada mbalimbali.

> Kuelewa na kuwa na uwezo wa kuzalisha maandishi pia kunahusisha kujua kitu kuhusu ulimwengu unaotuzunguka. Watu pia hujifunza kwa kusoma kwa kiwango kikubwa, na mtandao wa GPT ni sawa katika muktadha huu.

Mitandao ya uundaji wa maandishi hufanya kazi kwa kutabiri uwezekano wa neno linalofuata $$P(w_N)$$. Hata hivyo, uwezekano usio na masharti wa neno linalofuata ni sawa na marudio ya neno hilo katika hifadhidata ya maandishi. GPT inaweza kutupatia **uwezekano wa masharti** wa neno linalofuata, ikizingatia yale ya awali: $$P(w_N | w_{n-1}, ..., w_0)$$

> Unaweza kusoma zaidi kuhusu uwezekano katika [Mtaala wetu wa Sayansi ya Data kwa Anayeanza](https://github.com/microsoft/Data-Science-For-Beginners/tree/main/1-Introduction/04-stats-and-probability)

Ubora wa mfano wa uundaji wa lugha unaweza kufafanuliwa kwa kutumia **perplexity**. Ni kipimo cha ndani kinachoturuhusu kupima ubora wa mfano bila seti ya data maalum ya kazi. Kinategemea dhana ya *uwezekano wa sentensi* - mfano unatoa uwezekano mkubwa kwa sentensi inayoweza kuwa halisi (yaani, mfano haujachanganyikiwa nayo), na uwezekano mdogo kwa sentensi ambazo hazina maana (mfano: *Je, inaweza kufanya nini?*). Tunapotoa mfano wetu sentensi kutoka hifadhidata halisi ya maandishi, tunatarajia kuwa na uwezekano mkubwa, na **perplexity** ndogo. Kihisabati, inafafanuliwa kama uwezekano wa kinyume uliowekwa wa seti ya majaribio:
$$
\mathrm{Perplexity}(W) = \sqrt[N]{1\over P(W_1,...,W_N)}
$$ 

**Unaweza kujaribu uundaji wa maandishi kwa kutumia [kihariri cha maandishi kinachotumia GPT kutoka Hugging Face](https://transformer.huggingface.co/doc/gpt2-large)**. Katika kihariri hiki, unaanza kuandika maandishi yako, na ukibonyeza **[TAB]** utapewa chaguo kadhaa za kukamilisha. Ikiwa ni fupi sana, au haujaridhika nazo - bonyeza [TAB] tena, na utakuwa na chaguo zaidi, ikiwa ni pamoja na vipande virefu vya maandishi.

## GPT ni Familia

GPT si mfano mmoja, bali ni mkusanyiko wa miundo iliyotengenezwa na kufundishwa na [OpenAI](https://openai.com). 

Chini ya miundo ya GPT, tunayo:

| [GPT-2](https://huggingface.co/docs/transformers/model_doc/gpt2#openai-gpt2) | [GPT 3](https://openai.com/research/language-models-are-few-shot-learners) | [GPT-4](https://openai.com/gpt-4) |
| -- | -- | -- |
|Mfano wa lugha wenye hadi vigezo bilioni 1.5. | Mfano wa lugha wenye hadi vigezo bilioni 175 | Vigezo trilioni 100 na unakubali pembejeo za picha na maandishi na kutoa maandishi. |


Miundo ya GPT-3 na GPT-4 inapatikana [kama huduma ya utambuzi kutoka Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/#overview?WT.mc_id=academic-77998-cacaste), na kama [API ya OpenAI](https://openai.com/api/).

## Uhandisi wa Maagizo

Kwa sababu GPT imefundishwa kwa kiasi kikubwa cha data ili kuelewa lugha na msimbo, hutoa matokeo kwa kujibu pembejeo (maagizo). Maagizo ni pembejeo au maswali ya GPT ambapo mtu hutoa maelekezo kwa miundo kuhusu kazi wanazotaka kukamilisha. Ili kupata matokeo yanayotarajiwa, unahitaji agizo bora zaidi ambalo linahusisha kuchagua maneno sahihi, miundo, misemo au hata alama. Mbinu hii ni [Uhandisi wa Maagizo](https://learn.microsoft.com/en-us/shows/ai-show/the-basics-of-prompt-engineering-with-azure-openai-service?WT.mc_id=academic-77998-bethanycheum)

[Hati hii](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/?WT.mc_id=academic-77998-bethanycheum) inakupa maelezo zaidi kuhusu uhandisi wa maagizo.

## ✍️ Daftari la Mfano: [Kucheza na OpenAI-GPT](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

Endelea kujifunza katika daftari zifuatazo:

* [Kuzalisha maandishi kwa OpenAI-GPT na Hugging Face Transformers](../../../../../lessons/5-NLP/20-LangModels/GPT-PyTorch.ipynb)

## Hitimisho

Miundo mipya ya lugha iliyofunzwa kabla haifanyi tu uundaji wa muundo wa lugha, bali pia ina kiasi kikubwa cha lugha ya asili. Kwa hivyo, inaweza kutumika kwa ufanisi kutatua baadhi ya kazi za NLP katika mipangilio ya zero-shop au few-shot.

## [Jaribio la Baada ya Somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/220)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.