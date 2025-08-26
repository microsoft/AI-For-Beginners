<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-25T20:51:14+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "sw"
}
-->
# Uundaji wa Lugha

Uwakilishi wa semantiki, kama Word2Vec na GloVe, kwa kweli ni hatua ya kwanza kuelekea **uundaji wa lugha** - kuunda mifano inayoweza *kuelewa* (au *kuwakilisha*) asili ya lugha.

## [Maswali ya awali ya somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/115)

Wazo kuu nyuma ya uundaji wa lugha ni kuifundisha kwenye seti za data zisizo na lebo kwa njia isiyo ya kusimamiwa. Hili ni muhimu kwa sababu tuna kiasi kikubwa cha maandishi yasiyo na lebo yanayopatikana, wakati kiasi cha maandishi yaliyo na lebo daima kitakuwa kidogo kutokana na juhudi tunazoweza kutumia katika kuweka lebo. Mara nyingi, tunaweza kujenga mifano ya lugha inayoweza **kutabiri maneno yanayokosekana** katika maandishi, kwa sababu ni rahisi kuficha neno la bahati nasibu katika maandishi na kulitumia kama sampuli ya mafunzo.

## Mafunzo ya Uwakilishi

Katika mifano yetu ya awali, tulitumia uwakilishi wa semantiki uliokwisha kufundishwa, lakini ni jambo la kuvutia kuona jinsi uwakilishi huo unavyoweza kufundishwa. Kuna mawazo kadhaa yanayoweza kutumika:

* **Uundaji wa lugha wa N-Gram**, ambapo tunatabiri tokeni kwa kuangalia tokeni N za awali (N-gram).
* **Mfuko Endelevu wa Maneno** (CBoW), ambapo tunatabiri tokeni ya katikati $W_0$ katika mlolongo wa tokeni $W_{-N}$, ..., $W_N$.
* **Skip-gram**, ambapo tunatabiri seti ya tokeni za jirani {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} kutoka tokeni ya katikati $W_0$.

![picha kutoka karatasi kuhusu kubadilisha maneno kuwa vekta](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.sw.png)

> Picha kutoka [karatasi hii](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Noti za Mfano: Mafunzo ya Mfano wa CBoW

Endelea kujifunza katika noti zifuatazo:

* [Mafunzo ya CBoW Word2Vec kwa kutumia TensorFlow](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [Mafunzo ya CBoW Word2Vec kwa kutumia PyTorch](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Hitimisho

Katika somo la awali tuliona kwamba uwakilishi wa maneno hufanya kazi kama uchawi! Sasa tunajua kwamba kufundisha uwakilishi wa maneno si kazi ngumu sana, na tunapaswa kuwa na uwezo wa kufundisha uwakilishi wetu wa maneno kwa maandishi maalum ya kikoa ikiwa inahitajika.

## [Maswali ya baada ya somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/215)

## Mapitio na Kujifunza Binafsi

* [Mafunzo rasmi ya PyTorch kuhusu Uundaji wa Lugha](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Mafunzo rasmi ya TensorFlow kuhusu kufundisha mfano wa Word2Vec](https://www.TensorFlow.org/tutorials/text/word2vec).
* Kutumia mfumo wa **gensim** kufundisha uwakilishi unaotumika sana kwa mistari michache ya msimbo imeelezwa [katika nyaraka hizi](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).

## 🚀 [Kazi: Fundisha Mfano wa Skip-Gram](lab/README.md)

Katika maabara, tunakupa changamoto ya kurekebisha msimbo kutoka somo hili ili kufundisha mfano wa skip-gram badala ya CBoW. [Soma maelezo](lab/README.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.