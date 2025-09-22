<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e40b47ac3fd48f71304ede1474e66293",
  "translation_date": "2025-08-25T20:49:42+00:00",
  "source_file": "lessons/5-NLP/14-Embeddings/README.md",
  "language_code": "sw"
}
-->
# Uwekaji wa Neno

## [Maswali ya awali ya somo](https://ff-quizzes.netlify.app/en/ai/quiz/27)

Wakati wa kufundisha vionyeshi vya kuainisha kwa kutumia BoW au TF/IDF, tulikuwa tunatumia vekta za maneno zenye vipimo vingi zenye urefu `vocab_size`, na tulikuwa tunabadilisha vekta za uwakilishi wa nafasi zenye vipimo vichache kuwa uwakilishi wa sparse one-hot. Hata hivyo, uwakilishi huu wa one-hot si wa ufanisi wa kumbukumbu. Zaidi ya hayo, kila neno linachukuliwa kuwa huru kutoka kwa mengine, yaani, vekta za one-hot hazionyeshi uhusiano wa kisemantiki kati ya maneno.

Wazo la **uwekaji wa neno** ni kuwakilisha maneno kwa vekta zenye vipimo vichache, ambazo kwa namna fulani zinaonyesha maana ya kisemantiki ya neno. Tutajadili baadaye jinsi ya kujenga uwekaji wa maneno wenye maana, lakini kwa sasa wacha tuwaze uwekaji wa neno kama njia ya kupunguza vipimo vya vekta ya neno.

Kwa hivyo, safu ya uwekaji itachukua neno kama ingizo, na kutoa vekta ya matokeo yenye ukubwa wa `embedding_size`. Kwa namna fulani, ni sawa na safu ya `Linear`, lakini badala ya kuchukua vekta ya one-hot, itakuwa na uwezo wa kuchukua namba ya neno kama ingizo, ikituwezesha kuepuka kuunda vekta kubwa za one-hot.

Kwa kutumia safu ya uwekaji kama safu ya kwanza katika mtandao wetu wa kuainisha, tunaweza kubadilisha kutoka mfuko wa maneno hadi **mfuko wa uwekaji**, ambapo tunabadilisha kila neno katika maandishi yetu kuwa uwekaji unaolingana, na kisha tunahesabu kazi ya jumla juu ya uwekaji wote, kama vile `sum`, `average` au `max`.  

![Picha inayoonyesha kionyeshi cha uwekaji kwa maneno matano ya mfululizo.](../../../../../translated_images/embedding-classifier-example.b77f021a7ee67eeec8e68bfe11636c5b97d6eaa067515a129bfb1d0034b1ac5b.sw.png)

> Picha na mwandishi

## ✍️ Mazoezi: Uwekaji wa Neno

Endelea kujifunza katika daftari zifuatazo:
* [Uwekaji wa Neno na PyTorch](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsPyTorch.ipynb)
* [Uwekaji wa Neno na TensorFlow](../../../../../lessons/5-NLP/14-Embeddings/EmbeddingsTF.ipynb)

## Uwekaji wa Kisemantiki: Word2Vec

Ingawa safu ya uwekaji ilijifunza kuwakilisha maneno kwa vekta, uwakilishi huu haukuwa na maana ya kisemantiki sana. Ingekuwa vizuri kujifunza uwakilishi wa vekta ambapo maneno yanayofanana au visawe vinahusiana kwa vekta zilizo karibu kwa umbali fulani wa vekta (mfano, umbali wa Euclidean).

Ili kufanya hivyo, tunahitaji kufundisha mtindo wetu wa uwekaji kwenye mkusanyiko mkubwa wa maandishi kwa njia maalum. Njia moja ya kufundisha uwekaji wa kisemantiki inaitwa [Word2Vec](https://en.wikipedia.org/wiki/Word2vec). Inategemea usanifu mbili kuu zinazotumika kutoa uwakilishi wa maneno uliosambazwa:

 - **Mfuko endelevu wa maneno** (CBoW) — katika usanifu huu, tunafundisha mtindo kutabiri neno kutoka muktadha wa karibu. Kwa ngram $(W_{-2},W_{-1},W_0,W_1,W_2)$, lengo la mtindo ni kutabiri $W_0$ kutoka $(W_{-2},W_{-1},W_1,W_2)$.
 - **Skip-gram endelevu** ni kinyume cha CBoW. Mtindo hutumia dirisha la muktadha wa maneno ya karibu kutabiri neno la sasa.

CBoW ni ya haraka, wakati skip-gram ni polepole, lakini inafanya kazi bora ya kuwakilisha maneno yasiyo ya kawaida.

![Picha inayoonyesha CBoW na Skip-Gram algorithms za kubadilisha maneno kuwa vekta.](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.sw.png)

> Picha kutoka [karatasi hii](https://arxiv.org/pdf/1301.3781.pdf)

Uwekaji wa Word2Vec uliotangulia kufundishwa (pamoja na mifano mingine kama GloVe) unaweza pia kutumika badala ya safu ya uwekaji katika mitandao ya neva. Hata hivyo, tunahitaji kushughulikia misamiati, kwa sababu msamiati uliotumika kufundisha Word2Vec/GloVe huenda ukatofautiana na msamiati katika mkusanyiko wetu wa maandishi. Angalia daftari zilizo juu ili kuona jinsi tatizo hili linaweza kutatuliwa.

## Uwekaji wa Muktadha

Kikwazo kimoja kikuu cha uwakilishi wa uwekaji uliotangulia kufundishwa kama Word2Vec ni tatizo la kutofautisha maana ya neno. Ingawa uwekaji uliotangulia kufundishwa unaweza kunasa baadhi ya maana ya maneno katika muktadha, kila maana inayowezekana ya neno huwakilishwa katika uwekaji mmoja. Hii inaweza kusababisha matatizo katika mifano ya baadaye, kwa sababu maneno mengi kama neno 'play' yana maana tofauti kulingana na muktadha yanayotumika.

Kwa mfano, neno 'play' katika sentensi hizi mbili lina maana tofauti kabisa:

- Nilikwenda kwenye **play** katika ukumbi wa michezo.
- John anataka **play** na marafiki zake.

Uwekaji uliotangulia kufundishwa hapo juu unawakilisha maana zote mbili za neno 'play' katika uwekaji mmoja. Ili kushinda kikwazo hiki, tunahitaji kujenga uwekaji kulingana na **mtindo wa lugha**, ambao umefundishwa kwenye mkusanyiko mkubwa wa maandishi, na *unajua* jinsi maneno yanavyoweza kuwekwa pamoja katika muktadha tofauti. Kujadili uwekaji wa muktadha ni nje ya mada ya mafunzo haya, lakini tutarudi kwao wakati wa kuzungumzia mitindo ya lugha baadaye katika kozi.

## Hitimisho

Katika somo hili, umejifunza jinsi ya kujenga na kutumia safu za uwekaji katika TensorFlow na Pytorch ili kuonyesha vyema maana za kisemantiki za maneno.

## 🚀 Changamoto

Word2Vec imetumika kwa matumizi ya kuvutia, ikiwa ni pamoja na kuunda mashairi na nyimbo. Angalia [makala hii](https://www.politetype.com/blog/word2vec-color-poems) ambayo inaelezea jinsi mwandishi alitumia Word2Vec kuunda mashairi. Tazama [video hii na Dan Shiffmann](https://www.youtube.com/watch?v=LSS_bos_TPI&ab_channel=TheCodingTrain) pia ili kugundua maelezo tofauti ya mbinu hii. Kisha jaribu kutumia mbinu hizi kwenye mkusanyiko wako wa maandishi, labda kutoka Kaggle.

## [Maswali ya baada ya somo](https://ff-quizzes.netlify.app/en/ai/quiz/28)

## Mapitio na Kujifunza Binafsi

Soma karatasi hii kuhusu Word2Vec: [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/pdf/1301.3781.pdf)

## [Kazi: Daftari](assignment.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.