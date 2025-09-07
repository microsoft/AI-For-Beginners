<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4522e22e150be0845e03aa41209a39d5",
  "translation_date": "2025-08-25T20:50:40+00:00",
  "source_file": "lessons/5-NLP/13-TextRep/README.md",
  "language_code": "sw"
}
-->
# Kuwakilisha Maandishi kama Tensors

## [Jaribio la Kabla ya Somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/113)

## Uainishaji wa Maandishi

Katika sehemu ya kwanza ya somo hili, tutazingatia kazi ya **uainishaji wa maandishi**. Tutatumia Dataset ya [AG News](https://www.kaggle.com/amananandrai/ag-news-classification-dataset), ambayo ina makala za habari kama ifuatavyo:

* Kategoria: Sayansi/Teknolojia  
* Kichwa: Kampuni ya Ky. Yashinda Ruzuku ya Kuchunguza Peptidi (AP)  
* Mwili: AP - Kampuni iliyoanzishwa na mtafiti wa kemia katika Chuo Kikuu cha Louisville ilishinda ruzuku ya kuendeleza...  

Lengo letu litakuwa kuainisha kipengele cha habari katika moja ya kategoria kulingana na maandishi.

## Kuwakilisha Maandishi

Ili kutatua kazi za Usindikaji wa Lugha Asilia (NLP) kwa kutumia mitandao ya neva, tunahitaji njia ya kuwakilisha maandishi kama tensors. Kompyuta tayari zinawakilisha herufi za maandishi kama namba zinazolingana na fonti kwenye skrini yako kwa kutumia encodings kama ASCII au UTF-8.

<img alt="Picha inayoonyesha mchoro wa kuonyesha ramani ya herufi kwa uwakilishi wa ASCII na binary" src="images/ascii-character-map.png" width="50%"/>

> [Chanzo cha Picha](https://www.seobility.net/en/wiki/ASCII)

Kwa wanadamu, tunaelewa kile kila herufi **inawakilisha**, na jinsi herufi zote zinavyoungana kuunda maneno ya sentensi. Hata hivyo, kompyuta zenyewe hazina uelewa huo, na mtandao wa neva lazima ujifunze maana wakati wa mafunzo.

Kwa hivyo, tunaweza kutumia mbinu tofauti wakati wa kuwakilisha maandishi:

* **Uwakilishi wa kiwango cha herufi**, ambapo tunawakilisha maandishi kwa kuchukulia kila herufi kama namba. Kwa kuwa tuna *C* herufi tofauti katika korpasi yetu ya maandishi, neno *Hello* litaakilishwa na tensor ya 5x*C*. Kila herufi italingana na safu ya tensor katika one-hot encoding.  
* **Uwakilishi wa kiwango cha neno**, ambapo tunaunda **msamiati** wa maneno yote katika maandishi yetu, kisha tunawakilisha maneno kwa kutumia one-hot encoding. Mbinu hii ni bora zaidi kwa kiasi fulani, kwa sababu kila herufi peke yake haina maana kubwa, na kwa hivyo kwa kutumia dhana za juu zaidi za kisemantiki - maneno - tunarahisisha kazi kwa mtandao wa neva. Hata hivyo, kutokana na ukubwa wa kamusi, tunahitaji kushughulikia tensors kubwa na zilizo na nafasi nyingi tupu.

Bila kujali uwakilishi, tunahitaji kwanza kubadilisha maandishi kuwa mlolongo wa **tokeni**, tokeni moja ikiwa herufi, neno, au wakati mwingine hata sehemu ya neno. Kisha, tunabadilisha tokeni kuwa namba, kwa kawaida kwa kutumia **msamiati**, na namba hii inaweza kulishwa kwenye mtandao wa neva kwa kutumia one-hot encoding.

## N-Grams

Katika lugha asilia, maana halisi ya maneno inaweza tu kuamuliwa katika muktadha. Kwa mfano, maana za *neural network* na *fishing network* ni tofauti kabisa. Njia moja ya kuzingatia hili ni kujenga mfano wetu kwa jozi za maneno, na kuzingatia jozi za maneno kama tokeni tofauti za msamiati. Kwa njia hii, sentensi *I like to go fishing* itawakilishwa na mlolongo wa tokeni zifuatazo: *I like*, *like to*, *to go*, *go fishing*. Tatizo la mbinu hii ni kwamba ukubwa wa kamusi unakua kwa kiasi kikubwa, na mchanganyiko kama *go fishing* na *go shopping* huwakilishwa na tokeni tofauti, ambazo hazishiriki uhusiano wowote wa kisemantiki licha ya kitenzi sawa.  

Katika baadhi ya matukio, tunaweza kuzingatia kutumia tri-grams -- mchanganyiko wa maneno matatu -- pia. Kwa hivyo mbinu hii mara nyingi huitwa **n-grams**. Pia, inafaa kutumia n-grams na uwakilishi wa kiwango cha herufi, ambapo n-grams zitakaribia kuwakilisha silabi tofauti.

## Mfuko wa Maneno na TF/IDF

Wakati wa kutatua kazi kama uainishaji wa maandishi, tunahitaji kuwakilisha maandishi kwa vector moja ya ukubwa wa kudumu, ambayo tutatumia kama pembejeo kwa classifier ya mwisho yenye msongamano. Njia rahisi zaidi ya kufanya hivyo ni kuunganisha uwakilishi wa kila neno, kwa mfano kwa kuyaongeza. Tukiongeza one-hot encodings za kila neno, tutapata vector ya marudio, inayoonyesha mara ngapi kila neno linatokea ndani ya maandishi. Uwakilishi wa maandishi wa aina hii unaitwa **mfuko wa maneno** (BoW).

<img src="images/bow.png" width="90%"/>

> Picha na mwandishi

BoW kimsingi huwakilisha maneno yanayotokea katika maandishi na kwa wingi gani, ambayo inaweza kuwa kiashiria kizuri cha kile maandishi yanahusu. Kwa mfano, makala ya habari kuhusu siasa huenda ikawa na maneno kama *rais* na *nchi*, wakati chapisho la kisayansi linaweza kuwa na maneno kama *collider*, *discovered*, n.k. Kwa hivyo, marudio ya maneno yanaweza mara nyingi kuwa kiashiria kizuri cha maudhui ya maandishi.

Tatizo na BoW ni kwamba maneno fulani ya kawaida, kama *na*, *ni*, n.k. yanatokea katika maandishi mengi, na yana marudio ya juu zaidi, yakifunika maneno ambayo ni muhimu kweli. Tunaweza kupunguza umuhimu wa maneno hayo kwa kuzingatia marudio ambayo maneno yanatokea katika mkusanyiko mzima wa nyaraka. Hii ndiyo wazo kuu nyuma ya mbinu ya TF/IDF, ambayo imeelezewa kwa undani zaidi katika daftari zilizoshikamana na somo hili.

Hata hivyo, hakuna mojawapo ya mbinu hizi zinazoweza kuzingatia kikamilifu **semantiki** ya maandishi. Tunahitaji mifano yenye nguvu zaidi ya mitandao ya neva kufanya hivyo, ambayo tutajadili baadaye katika sehemu hii.

## ✍️ Mazoezi: Uwakilishi wa Maandishi

Endelea kujifunza katika daftari zifuatazo:

* [Uwakilishi wa Maandishi na PyTorch](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationPyTorch.ipynb)  
* [Uwakilishi wa Maandishi na TensorFlow](../../../../../lessons/5-NLP/13-TextRep/TextRepresentationTF.ipynb)  

## Hitimisho

Hadi sasa, tumejifunza mbinu zinazoweza kuongeza uzito wa marudio kwa maneno tofauti. Hata hivyo, haziwezi kuwakilisha maana au mpangilio. Kama mwanaisimu maarufu J. R. Firth alivyosema mwaka 1935, "Maana kamili ya neno daima ni ya muktadha, na hakuna utafiti wa maana bila muktadha unaoweza kuchukuliwa kwa uzito." Tutajifunza baadaye katika kozi jinsi ya kunasa taarifa za muktadha kutoka kwa maandishi kwa kutumia uundaji wa lugha.

## 🚀 Changamoto

Jaribu mazoezi mengine kwa kutumia mfuko wa maneno na mifano tofauti ya data. Unaweza kupata msukumo kutoka kwa [shindano hili kwenye Kaggle](https://www.kaggle.com/competitions/word2vec-nlp-tutorial/overview/part-1-for-beginners-bag-of-words)

## [Jaribio la Baada ya Somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/213)

## Mapitio na Kujisomea

Fanya mazoezi ya ujuzi wako kwa kutumia embeddings za maandishi na mbinu za mfuko wa maneno kwenye [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/?WT.mc_id=academic-77998-cacaste)

## [Kazi: Daftari](assignment.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.