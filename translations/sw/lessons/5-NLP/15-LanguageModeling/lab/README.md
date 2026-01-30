# Kufundisha Mfano wa Skip-Gram

Kazi ya Maabara kutoka [Mtaala wa AI kwa Kompyuta](https://github.com/microsoft/ai-for-beginners).

## Kazi

Katika maabara hii, tunakupa changamoto ya kufundisha mfano wa Word2Vec kwa kutumia mbinu ya Skip-Gram. Fundisha mtandao wenye embedding ili kutabiri maneno jirani katika dirisha la Skip-Gram lenye upana wa $N$-tokens. Unaweza kutumia [msimbo kutoka somo hili](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb), na kuubadilisha kidogo.

## Seti ya Takwimu

Unakaribishwa kutumia kitabu chochote. Unaweza kupata maandishi mengi ya bure kwenye [Project Gutenberg](https://www.gutenberg.org/), kwa mfano, hapa kuna kiungo cha moja kwa moja cha [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt)) kilichoandikwa na Lewis Carroll. Au, unaweza kutumia michezo ya Shakespeare, ambayo unaweza kupata kwa kutumia msimbo ufuatao:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Chunguza!

Ikiwa una muda na unataka kuingia kwa undani zaidi kwenye mada hii, jaribu kuchunguza mambo kadhaa:

* Je, ukubwa wa embedding unaathirije matokeo?
* Je, mitindo tofauti ya maandishi inaathirije matokeo?
* Chukua aina kadhaa tofauti za maneno na visawe vyake, pata uwakilishi wa vekta zao, tumia PCA kupunguza vipimo hadi 2, na uchore kwenye nafasi ya 2D. Je, unaona mifumo yoyote?

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.