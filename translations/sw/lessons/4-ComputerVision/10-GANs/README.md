<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-25T20:53:58+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "sw"
}
-->
# Mitandao ya Kizazi ya Kifedhuli (Generative Adversarial Networks)

Katika sehemu iliyopita, tulijifunza kuhusu **miundo ya kizazi**: miundo inayoweza kuzalisha picha mpya zinazofanana na zile zilizopo kwenye seti ya mafunzo. VAE ilikuwa mfano mzuri wa muundo wa kizazi.

## [Jaribio la kabla ya somo](https://ff-quizzes.netlify.app/en/ai/quiz/19)

Hata hivyo, tukijaribu kuzalisha kitu chenye maana zaidi, kama mchoro wa kiwango cha azimio la kuridhisha, kwa kutumia VAE, tutaona kuwa mafunzo hayafikii lengo vizuri. Kwa matumizi haya, tunapaswa kujifunza kuhusu usanifu mwingine unaolenga hasa miundo ya kizazi - **Mitandao ya Kizazi ya Kifedhuli**, au GANs.

Wazo kuu la GAN ni kuwa na mitandao miwili ya neva ambayo itafundishwa dhidi ya kila mmoja:

<img src="images/gan_architecture.png" width="70%"/>

> Picha na [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Msamiati mdogo:
> * **Generator** ni mtandao unaochukua vekta ya nasibu na kuzalisha picha kama matokeo.
> * **Discriminator** ni mtandao unaochukua picha na unatakiwa kusema kama ni picha halisi (kutoka kwenye seti ya mafunzo) au imezalishwa na generator. Kimsingi ni mklasifaya wa picha.

### Discriminator

Usanifu wa discriminator hauna tofauti na mtandao wa kawaida wa uainishaji wa picha. Katika hali rahisi inaweza kuwa mklasifaya wa tabaka zilizounganishwa kikamilifu, lakini mara nyingi zaidi itakuwa [mtandao wa convolutional](../07-ConvNets/README.md).

> ✅ GAN inayotegemea mitandao ya convolutional inaitwa [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

Discriminator ya CNN inajumuisha tabaka zifuatazo: convolution+pooling kadhaa (zikiwa na ukubwa wa anga unaopungua) na, tabaka moja au zaidi zilizounganishwa kikamilifu ili kupata "veka ya sifa", na mklasifaya wa mwisho wa binary.

> ✅ 'Pooling' katika muktadha huu ni mbinu inayopunguza ukubwa wa picha. "Tabaka za pooling hupunguza vipimo vya data kwa kuchanganya matokeo ya vikundi vya neva katika tabaka moja kuwa neva moja kwenye tabaka inayofuata." - [chanzo](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generator

Generator ni ngumu kidogo. Unaweza kuiona kama discriminator iliyogeuzwa. Kuanzia na vekta ya siri (badala ya veka ya sifa), ina tabaka lililounganishwa kikamilifu ili kuibadilisha kuwa ukubwa/umbo linalohitajika, ikifuatiwa na deconvolution+upscaling. Hii ni sawa na sehemu ya *decoder* ya [autoencoder](../09-Autoencoders/README.md).

> ✅ Kwa sababu tabaka la convolution linatekelezwa kama kichujio cha mstari kinachopita kwenye picha, deconvolution kimsingi ni sawa na convolution, na inaweza kutekelezwa kwa kutumia mantiki sawa ya tabaka.

<img src="images/gan_arch_detail.png" width="70%"/>

> Picha na [Dmitry Soshnikov](http://soshnikov.com)

### Mafunzo ya GAN

GANs zinaitwa **kifedhuli** kwa sababu kuna mashindano ya mara kwa mara kati ya generator na discriminator. Wakati wa mashindano haya, generator na discriminator zote mbili huboresha, hivyo mtandao hujifunza kuzalisha picha bora zaidi.

Mafunzo hufanyika katika hatua mbili:

* **Mafunzo ya discriminator**. Kazi hii ni rahisi: tunazalisha kundi la picha kwa kutumia generator, tukiziwekea lebo 0, ambayo inamaanisha picha bandia, na kuchukua kundi la picha kutoka kwenye seti ya mafunzo (zikiwa na lebo 1, picha halisi). Tunapata *hasara ya discriminator*, na kufanya backprop.
* **Mafunzo ya generator**. Hii ni ngumu kidogo, kwa sababu hatujui matokeo yanayotarajiwa moja kwa moja kwa generator. Tunachukua mtandao mzima wa GAN unaojumuisha generator ikifuatiwa na discriminator, tunaupa vekta za nasibu, na tunatarajia matokeo yawe 1 (yanayolingana na picha halisi). Kisha tunagandisha vigezo vya discriminator (hatutaki ifundishwe katika hatua hii), na kufanya backprop.

Wakati wa mchakato huu, hasara za generator na discriminator hazishuki sana. Katika hali bora, zinapaswa kutetereka, zikionyesha mitandao yote miwili inavyoboresha utendaji wake.

## ✍️ Mazoezi: GANs

* [Notebook ya GAN katika TensorFlow/Keras](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [Notebook ya GAN katika PyTorch](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### Changamoto za Mafunzo ya GAN

GANs zinajulikana kuwa ngumu sana kufundisha. Hapa kuna changamoto chache:

* **Mode Collapse**. Kwa neno hili tunamaanisha kuwa generator inajifunza kuzalisha picha moja yenye mafanikio inayomdanganya discriminator, badala ya aina mbalimbali za picha tofauti.
* **Unyeti kwa hyperparameters**. Mara nyingi unaweza kuona kuwa GAN haifiki lengo kabisa, na kisha ghafla inapungua kiwango cha kujifunza na kufikia lengo.
* Kuweka **usawa** kati ya generator na discriminator. Katika hali nyingi hasara ya discriminator inaweza kushuka hadi sifuri haraka, jambo linalosababisha generator kushindwa kufundishwa zaidi. Ili kushinda hili, tunaweza kujaribu kuweka viwango tofauti vya kujifunza kwa generator na discriminator, au kuruka mafunzo ya discriminator ikiwa hasara tayari ni ndogo sana.
* Mafunzo kwa **azimio la juu**. Hii inahusiana na tatizo sawa na autoencoders, ambapo kujenga upya tabaka nyingi za mtandao wa convolutional husababisha kasoro. Tatizo hili kwa kawaida hutatuliwa kwa kutumia **ukuaji wa hatua kwa hatua**, ambapo tabaka chache za kwanza hufundishwa kwenye picha za azimio la chini, kisha tabaka zinafunguliwa au kuongezwa. Suluhisho jingine ni kuongeza miunganisho ya ziada kati ya tabaka na kufundisha maazimio kadhaa kwa wakati mmoja - angalia karatasi hii ya [Multi-Scale Gradient GANs](https://arxiv.org/abs/1903.06048) kwa maelezo zaidi.

## Uhamishaji wa Mtindo

GANs ni njia nzuri ya kuzalisha picha za kisanii. Mbinu nyingine ya kuvutia ni ile inayoitwa **uhamishaji wa mtindo**, ambayo huchukua **picha ya maudhui**, na kuichora upya kwa mtindo tofauti, ikitumia vichujio kutoka kwa **picha ya mtindo**.

Jinsi inavyofanya kazi ni kama ifuatavyo:
* Tunaanza na picha ya kelele ya nasibu (au na picha ya maudhui, lakini kwa urahisi wa kuelewa ni bora kuanza na kelele ya nasibu)
* Lengo letu litakuwa kuunda picha ambayo itakuwa karibu na picha ya maudhui na picha ya mtindo. Hii itaamuliwa na hasara mbili:
   - **Hasara ya maudhui** inahesabiwa kulingana na sifa zilizotolewa na CNN katika tabaka fulani kutoka picha ya sasa na picha ya maudhui.
   - **Hasara ya mtindo** inahesabiwa kati ya picha ya sasa na picha ya mtindo kwa njia ya busara kwa kutumia matriki za Gram (maelezo zaidi katika [notebook ya mfano](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)).
* Ili kufanya picha iwe laini na kuondoa kelele, tunaongeza pia **Hasara ya Mabadiliko**, ambayo huhesabu umbali wa wastani kati ya pikseli zilizo jirani.
* Mzunguko mkuu wa uboreshaji hubadilisha picha ya sasa kwa kutumia gradient descent (au algorithm nyingine ya uboreshaji) ili kupunguza jumla ya hasara, ambayo ni jumla ya uzito wa hasara zote tatu.

## ✍️ Mfano: [Uhamishaji wa Mtindo](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Jaribio la baada ya somo](https://ff-quizzes.netlify.app/en/ai/quiz/20)

## Hitimisho

Katika somo hili, umejifunza kuhusu GANs na jinsi ya kuzifundisha. Pia umejifunza kuhusu changamoto maalum ambazo aina hii ya Mtandao wa Neva inaweza kukutana nazo, na mikakati ya jinsi ya kuzitatua.

## 🚀 Changamoto

Pitia [notebook ya Uhamishaji wa Mtindo](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) ukitumia picha zako mwenyewe.

## Mapitio na Kujisomea

Kwa marejeleo, soma zaidi kuhusu GANs katika rasilimali hizi:

* Marco Pasini, [Masomo 10 Niliyojifunza Nikifundisha GANs kwa Mwaka Mmoja](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), usanifu wa GAN wa *de facto* wa kuzingatia
* [Kuzalisha Sanaa ya Kizazi kwa kutumia GANs kwenye Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Kazi

Rudia moja ya notebook mbili zinazohusiana na somo hili na fundisha tena GAN kwa kutumia picha zako mwenyewe. Unaweza kuunda nini?

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.