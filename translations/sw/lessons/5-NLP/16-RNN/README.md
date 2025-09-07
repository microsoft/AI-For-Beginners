<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58bf4adb210aab53e8f78c8082040e7c",
  "translation_date": "2025-08-25T20:49:04+00:00",
  "source_file": "lessons/5-NLP/16-RNN/README.md",
  "language_code": "sw"
}
-->
# Mitandao ya Neural ya Kurudiarudia

## [Jaribio la kabla ya somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/116)

Katika sehemu zilizopita, tumekuwa tukitumia uwakilishi wa maana tajiri wa maandishi na mklasifaya rahisi ya mstari juu ya embeddings. Hii usanifu hufanya kazi ya kunasa maana iliyojumlishwa ya maneno katika sentensi, lakini haizingatii **mpangilio** wa maneno, kwa sababu operesheni ya kujumuisha juu ya embeddings huondoa taarifa hii kutoka kwa maandishi ya awali. Kwa sababu mifano hii haiwezi kuiga mpangilio wa maneno, haziwezi kutatua kazi ngumu zaidi au zenye utata kama vile uzalishaji wa maandishi au kujibu maswali.

Ili kunasa maana ya mlolongo wa maandishi, tunahitaji kutumia usanifu mwingine wa mtandao wa neural, unaoitwa **mtandao wa neural wa kurudiarudia**, au RNN. Katika RNN, tunapitisha sentensi yetu kupitia mtandao ishara moja kwa wakati, na mtandao huzalisha **hali fulani**, ambayo tunapitisha tena kwenye mtandao pamoja na ishara inayofuata.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.sw.png)

> Picha na mwandishi

Kwa kuzingatia mlolongo wa pembejeo wa tokeni X<sub>0</sub>,...,X<sub>n</sub>, RNN huunda mlolongo wa vizuizi vya mtandao wa neural, na kufundisha mlolongo huu kutoka mwanzo hadi mwisho kwa kutumia backpropagation. Kila kizuizi cha mtandao huchukua jozi (X<sub>i</sub>,S<sub>i</sub>) kama pembejeo, na huzalisha S<sub>i+1</sub> kama matokeo. Hali ya mwisho S<sub>n</sub> au (matokeo Y<sub>n</sub>) huingia kwenye mklasifaya ya mstari ili kutoa matokeo. Vizuizi vyote vya mtandao vinashiriki uzito sawa, na hufundishwa kutoka mwanzo hadi mwisho kwa kutumia mchakato mmoja wa backpropagation.

Kwa sababu vekta za hali S<sub>0</sub>,...,S<sub>n</sub> zinapitishwa kupitia mtandao, ina uwezo wa kujifunza utegemezi wa mlolongo kati ya maneno. Kwa mfano, neno *siyo* linapotokea mahali fulani katika mlolongo, linaweza kujifunza kukanusha vipengele fulani ndani ya vekta ya hali, na kusababisha kukanusha.

> ✅ Kwa kuwa uzito wa vizuizi vyote vya RNN kwenye picha hapo juu vinashirikiana, picha hiyo hiyo inaweza kuwakilishwa kama kizuizi kimoja (kulia) chenye kitanzi cha maoni ya kurudiarudia, ambacho hupitisha hali ya matokeo ya mtandao kurudi kwenye pembejeo.

## Muundo wa Seli ya RNN

Hebu tuone jinsi seli rahisi ya RNN imepangwa. Inapokea hali ya awali S<sub>i-1</sub> na ishara ya sasa X<sub>i</sub> kama pembejeo, na inapaswa kutoa hali ya matokeo S<sub>i</sub> (na, wakati mwingine, tunavutiwa pia na matokeo mengine Y<sub>i</sub>, kama ilivyo kwa mitandao ya kizazi).

Seli rahisi ya RNN ina matriki mawili ya uzito ndani: moja hubadilisha ishara ya pembejeo (tuiite W), na nyingine hubadilisha hali ya pembejeo (H). Katika kesi hii, matokeo ya mtandao huhesabiwa kama σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b), ambapo σ ni kazi ya uanzishaji na b ni upendeleo wa ziada.

<img alt="Muundo wa Seli ya RNN" src="images/rnn-anatomy.png" width="50%"/>

> Picha na mwandishi

Katika hali nyingi, tokeni za pembejeo hupitishwa kupitia safu ya embedding kabla ya kuingia kwenye RNN ili kupunguza ukubwa wa vipimo. Katika kesi hii, ikiwa kipimo cha vekta za pembejeo ni *emb_size*, na vekta ya hali ni *hid_size* - ukubwa wa W ni *emb_size*×*hid_size*, na ukubwa wa H ni *hid_size*×*hid_size*.

## Kumbukumbu ya Muda Mrefu na Mfupi (LSTM)

Moja ya matatizo makuu ya RNN za kawaida ni tatizo linaloitwa **kupotea kwa gradients**. Kwa sababu RNN hufundishwa kutoka mwanzo hadi mwisho kwa mchakato mmoja wa backpropagation, inapata ugumu wa kueneza kosa hadi kwenye tabaka za mwanzo za mtandao, na hivyo mtandao hauwezi kujifunza uhusiano kati ya tokeni za mbali. Njia moja ya kuepuka tatizo hili ni kuanzisha **usimamizi wa hali wazi** kwa kutumia milango inayoitwa **gates**. Kuna usanifu mbili maarufu wa aina hii: **Kumbukumbu ya Muda Mrefu na Mfupi** (LSTM) na **Kitengo cha Relay Chenye Milango** (GRU).

![Picha inayoonyesha mfano wa seli ya kumbukumbu ya muda mrefu na mfupi](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Chanzo cha picha TBD

Mtandao wa LSTM umeandaliwa kwa namna inayofanana na RNN, lakini kuna hali mbili zinazopitishwa kutoka tabaka moja hadi nyingine: hali halisi C, na vekta iliyofichwa H. Katika kila kitengo, vekta iliyofichwa H<sub>i</sub> inachanganywa na pembejeo X<sub>i</sub>, na zinadhibiti kinachotokea kwa hali C kupitia **milango**. Kila mlango ni mtandao wa neural wenye uanzishaji wa sigmoid (matokeo katika safu [0,1]), ambao unaweza kufikiriwa kama maski ya bitwise inapozidishwa na vekta ya hali. Kuna milango ifuatayo (kutoka kushoto kwenda kulia kwenye picha hapo juu):

* **Mlango wa kusahau** huchukua vekta iliyofichwa na kuamua ni vipengele vipi vya vekta C tunavyohitaji kusahau, na vipi kupitisha.
* **Mlango wa pembejeo** huchukua taarifa fulani kutoka kwa pembejeo na vekta zilizofichwa na kuingiza kwenye hali.
* **Mlango wa matokeo** hubadilisha hali kupitia safu ya mstari yenye uanzishaji wa *tanh*, kisha huchagua baadhi ya vipengele vyake kwa kutumia vekta iliyofichwa H<sub>i</sub> ili kutoa hali mpya C<sub>i+1</sub>.

Vipengele vya hali C vinaweza kufikiriwa kama bendera fulani zinazoweza kuwashwa na kuzimwa. Kwa mfano, tunapokutana na jina *Alice* katika mlolongo, tunaweza kudhani kuwa linahusu mhusika wa kike, na kuinua bendera katika hali kwamba tuna nomino ya kike katika sentensi. Tunapokutana zaidi na maneno *na Tom*, tutainua bendera kwamba tuna nomino ya wingi. Hivyo kwa kudhibiti hali tunaweza kudumisha mali za kisarufi za sehemu za sentensi.

> ✅ Rasilimali bora ya kuelewa undani wa LSTM ni makala hii nzuri [Kuelewa Mitandao ya LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) na Christopher Olah.

## RNN za Mwelekeo Mbili na Tabaka Nyingi

Tumeelezea mitandao ya kurudiarudia inayofanya kazi kwa mwelekeo mmoja, kutoka mwanzo wa mlolongo hadi mwisho. Inaonekana kuwa ya asili, kwa sababu inafanana na jinsi tunavyosoma na kusikiliza hotuba. Hata hivyo, kwa kuwa katika hali nyingi za vitendo tunaweza kufikia mlolongo wa pembejeo kwa nasibu, inaweza kuwa na maana kuendesha hesabu ya kurudiarudia katika mwelekeo wote. Mitandao kama hiyo inaitwa **RNN za mwelekeo mbili**. Tunaposhughulika na mtandao wa mwelekeo mbili, tutahitaji vekta mbili za hali zilizofichwa, moja kwa kila mwelekeo.

Mtandao wa kurudiarudia, iwe wa mwelekeo mmoja au wa mwelekeo mbili, hunasa mifumo fulani ndani ya mlolongo, na inaweza kuihifadhi kwenye vekta ya hali au kuipitisha kwenye matokeo. Kama ilivyo kwa mitandao ya convolutional, tunaweza kujenga safu nyingine ya kurudiarudia juu ya ile ya kwanza ili kunasa mifumo ya kiwango cha juu na kujenga kutoka kwa mifumo ya kiwango cha chini iliyotolewa na safu ya kwanza. Hii inatupeleka kwenye dhana ya **RNN ya tabaka nyingi** ambayo inajumuisha mitandao miwili au zaidi ya kurudiarudia, ambapo matokeo ya safu ya awali hupitishwa kwa safu inayofuata kama pembejeo.

![Picha inayoonyesha RNN ya tabaka nyingi ya kumbukumbu ya muda mrefu na mfupi](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.sw.jpg)

*Picha kutoka [chapisho hili zuri](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) na Fernando López*

## ✍️ Mazoezi: Embeddings

Endelea kujifunza katika daftari zifuatazo:

* [RNNs na PyTorch](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [RNNs na TensorFlow](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## Hitimisho

Katika kitengo hiki, tumeona kwamba RNN zinaweza kutumika kwa uainishaji wa mlolongo, lakini kwa kweli, zinaweza kushughulikia kazi nyingi zaidi, kama vile uzalishaji wa maandishi, tafsiri ya mashine, na zaidi. Tutazingatia kazi hizo katika kitengo kijacho.

## 🚀 Changamoto

Soma baadhi ya fasihi kuhusu LSTM na zingatia matumizi yake:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Onyesha, Hudhuria na Hadithi: Kizazi cha Maelezo ya Picha ya Neural na Umakini wa Kijisura](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Jaribio la baada ya somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/216)

## Mapitio na Kujisomea

- [Kuelewa Mitandao ya LSTM](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) na Christopher Olah.

## [Kazi: Daftari](assignment.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.