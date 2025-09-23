<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9de7847385eeeda67cfdcce1640ab72",
  "translation_date": "2025-08-25T20:50:07+00:00",
  "source_file": "lessons/5-NLP/17-GenerativeNetworks/README.md",
  "language_code": "sw"
}
-->
# Mitandao ya Kizazi

## [Jaribio la Kabla ya Somo](https://ff-quizzes.netlify.app/en/ai/quiz/33)

Mitandao ya Neural Inayojirudia (RNNs) na aina zake kama vile Long Short Term Memory Cells (LSTMs) na Gated Recurrent Units (GRUs) zilitoa njia ya kuunda mifano ya lugha kwa kuwa zinaweza kujifunza mpangilio wa maneno na kutoa utabiri wa neno linalofuata katika mfuatano. Hii inatuwezesha kutumia RNNs kwa **kazi za kizazi**, kama vile utengenezaji wa maandishi ya kawaida, tafsiri ya mashine, na hata uundaji wa maelezo ya picha.

> ✅ Fikiria mara zote ulivyonufaika na kazi za kizazi kama vile kukamilisha maandishi unapoandika. Fanya utafiti kuhusu programu unazozipenda ili kuona kama zilitumia RNNs.

Katika usanifu wa RNN tuliojadili katika kitengo kilichopita, kila kitengo cha RNN kilizalisha hali fiche inayofuata kama matokeo. Hata hivyo, tunaweza pia kuongeza matokeo mengine kwa kila kitengo kinachojirudia, ambacho kingeturuhusu kutoa **mfuatano** (ambao ni sawa kwa urefu na mfuatano wa awali). Zaidi ya hayo, tunaweza kutumia vitengo vya RNN ambavyo havipokei pembejeo katika kila hatua, na badala yake huchukua vigezo vya hali ya awali, na kisha kuzalisha mfuatano wa matokeo.

Hii inaruhusu usanifu tofauti wa neural unaoonyeshwa kwenye picha hapa chini:

![Picha inayoonyesha mifumo ya kawaida ya mitandao ya neural inayojirudia.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.sw.jpg)

> Picha kutoka kwa chapisho la blogu [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) na [Andrej Karpaty](http://karpathy.github.io/)

* **Moja-kwa-moja** ni mtandao wa neural wa jadi wenye pembejeo moja na matokeo moja.
* **Moja-kwa-nyingi** ni usanifu wa kizazi unaopokea thamani moja ya pembejeo, na kuzalisha mfuatano wa thamani za matokeo. Kwa mfano, ikiwa tunataka kufundisha mtandao wa **uundaji wa maelezo ya picha** ambao utatoa maelezo ya maandishi ya picha, tunaweza kuchukua picha kama pembejeo, kuipitisha kupitia CNN ili kupata hali yake fiche, na kisha kuwa na mnyororo unaojirudia kuzalisha maelezo neno kwa neno.
* **Nyingi-kwa-moja** inahusiana na usanifu wa RNN tulioelezea katika kitengo kilichopita, kama vile uainishaji wa maandishi.
* **Nyingi-kwa-nyingi**, au **mfuatano-kwa-mfuatano** inahusiana na kazi kama vile **tafsiri ya mashine**, ambapo tunayo RNN ya kwanza inayokusanya taarifa zote kutoka kwa mfuatano wa pembejeo hadi hali fiche, na mnyororo mwingine wa RNN unafungua hali hii kuwa mfuatano wa matokeo.

Katika kitengo hiki, tutazingatia mifano rahisi ya kizazi inayotusaidia kuzalisha maandishi. Kwa urahisi, tutatumia tokeni za kiwango cha herufi.

Tutafundisha RNN hii kuzalisha maandishi hatua kwa hatua. Katika kila hatua, tutachukua mfuatano wa herufi wa urefu `nchars`, na kuiuliza mtandao kuzalisha herufi inayofuata kwa kila herufi ya pembejeo:

![Picha inayoonyesha mfano wa kizazi cha RNN cha neno 'HELLO'.](../../../../../translated_images/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.sw.png)

Wakati wa kuzalisha maandishi (wakati wa utabiri), tunaanza na **msukumo** fulani, ambao hupitishwa kupitia seli za RNN ili kuzalisha hali yake ya kati, na kisha kutoka kwa hali hii kizazi huanza. Tunazalisha herufi moja kwa wakati, na kupitisha hali na herufi iliyozalishwa kwa seli nyingine ya RNN ili kuzalisha inayofuata, hadi tutakapozalisha herufi za kutosha.

<img src="images/rnn-generate-inf.png" width="60%"/>

> Picha na mwandishi

## ✍️ Mazoezi: Mitandao ya Kizazi

Endelea kujifunza katika daftari zifuatazo:

* [Mitandao ya Kizazi na PyTorch](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb)
* [Mitandao ya Kizazi na TensorFlow](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)

## Kizazi cha Maandishi Laini na Joto

Matokeo ya kila seli ya RNN ni usambazaji wa uwezekano wa herufi. Ikiwa kila mara tutachukua herufi yenye uwezekano mkubwa zaidi kama herufi inayofuata katika maandishi yanayozalishwa, maandishi mara nyingi yanaweza "kurudiwa" kati ya mfuatano wa herufi zile zile tena na tena, kama katika mfano huu:

```
today of the second the company and a second the company ...
```

Hata hivyo, tukitazama usambazaji wa uwezekano wa herufi inayofuata, inaweza kuwa tofauti kati ya uwezekano wa juu zaidi si kubwa sana, kwa mfano herufi moja inaweza kuwa na uwezekano wa 0.2, nyingine - 0.19, n.k. Kwa mfano, tunapotafuta herufi inayofuata katika mfuatano '*play*', herufi inayofuata inaweza kuwa nafasi, au **e** (kama katika neno *player*).

Hii inatupeleka kwenye hitimisho kwamba si kila mara "haki" kuchagua herufi yenye uwezekano mkubwa zaidi, kwa sababu kuchagua ya pili kwa juu bado kunaweza kutupeleka kwenye maandishi yenye maana. Ni busara zaidi **kuchagua kwa sampuli** herufi kutoka kwa usambazaji wa uwezekano uliotolewa na matokeo ya mtandao. Tunaweza pia kutumia kigezo, **joto**, ambacho kitapunguza usambazaji wa uwezekano, ikiwa tunataka kuongeza nasibu, au kuufanya kuwa mkali zaidi, ikiwa tunataka kushikamana zaidi na herufi zenye uwezekano mkubwa zaidi.

Chunguza jinsi kizazi hiki laini cha maandishi kinavyotekelezwa katika daftari zilizounganishwa hapo juu.

## Hitimisho

Ingawa kizazi cha maandishi kinaweza kuwa na manufaa chenyewe, faida kubwa hutokana na uwezo wa kuzalisha maandishi kwa kutumia RNNs kutoka kwa vigezo vya awali. Kwa mfano, kizazi cha maandishi kinatumika kama sehemu ya tafsiri ya mashine (mfuatano-kwa-mfuatano, katika kesi hii hali fiche kutoka kwa *encoder* hutumika kuzalisha au *kufasiri* ujumbe uliotafsiriwa), au kuzalisha maelezo ya maandishi ya picha (ambapo vigezo vya awali vinatoka kwa kiondoa CNN).

## 🚀 Changamoto

Chukua masomo fulani kwenye Microsoft Learn kuhusu mada hii:

* Kizazi cha Maandishi na [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste)

## [Jaribio la Baada ya Somo](https://ff-quizzes.netlify.app/en/ai/quiz/34)

## Mapitio na Kujisomea

Hapa kuna makala za kupanua maarifa yako:

* Njia tofauti za kizazi cha maandishi na Markov Chain, LSTM na GPT-2: [blogu](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Mfano wa kizazi cha maandishi katika [nyaraka za Keras](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Kazi ya Nyumbani](lab/README.md)

Tumeona jinsi ya kuzalisha maandishi herufi kwa herufi. Katika maabara, utachunguza kizazi cha maandishi kwa kiwango cha maneno.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.