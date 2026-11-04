# Mbinu za Mafunzo ya Kujifunza Kina

Kadri mitandao ya neva inavyozidi kuwa mirefu, mchakato wa mafunzo yao unakuwa mgumu zaidi na zaidi. Tatizo moja kubwa ni kitu kinachojulikana kama [gradi zinazopotea](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) au [gradi zinazopasuka](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Chapisho hili](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) linatoa utangulizi mzuri kwa matatizo hayo.

Ili kufanya mafunzo ya mitandao mirefu kuwa na ufanisi zaidi, kuna mbinu chache zinazoweza kutumika.

## Kudumisha Thamani katika Kiwango Kinachofaa

Ili kufanya mahesabu ya nambari kuwa na utulivu zaidi, tunataka kuhakikisha kuwa thamani zote ndani ya mtandao wetu wa neva ziko katika kiwango kinachofaa, kawaida [-1..1] au [0..1]. Hii si sharti kali sana, lakini asili ya mahesabu ya nambari za kubeba (floating point) ni kwamba thamani za ukubwa tofauti haziwezi kushughulikiwa kwa usahihi pamoja. Kwa mfano, ikiwa tunaongeza 10<sup>-10</sup> na 10<sup>10</sup>, kuna uwezekano wa kupata 10<sup>10</sup>, kwa sababu thamani ndogo itageuzwa kuwa na ukubwa sawa na thamani kubwa, na hivyo mantissa itapotea.

Kazi nyingi za uanzishaji (activation functions) zina nonlinearities karibu na [-1..1], na hivyo ni busara kupunguza data zote za kuingiza kwa kiwango cha [-1..1] au [0..1].

## Uanzishaji wa Uzito wa Awali

Kwa kawaida, tunataka thamani ziko katika kiwango sawa baada ya kupita kwenye tabaka za mtandao. Hivyo ni muhimu kuanzisha uzito kwa njia inayohifadhi usambazaji wa thamani.

Usambazaji wa kawaida **N(0,1)** si wazo zuri, kwa sababu ikiwa tuna *n* pembejeo, kipimo cha kawaida cha matokeo kitakuwa *&radic;n*, na thamani zina uwezekano wa kutoka katika interval ya [0..1].

Uanzishaji ufuatao hutumika mara nyingi:

 * Usambazaji wa sare -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** huhakikisha kuwa kwa pembejeo zenye wastani wa sifuri na kipimo cha kawaida cha 1, wastani na kipimo cha kawaida vitabaki vile vile
 * **N(0,&radic;2/(n_in+n_out))** -- inayoitwa **uanzishaji wa Xavier** (`glorot`), husaidia kuweka ishara katika kiwango wakati wa usambazaji wa mbele na nyuma

## Kawaida kwa Batch

Hata kwa uanzishaji sahihi wa uzito, uzito unaweza kuwa mkubwa au mdogo sana wakati wa mafunzo, na yataleta ishara nje ya kiwango kinachofaa. Tunaweza kurejesha ishara kwa kutumia mojawapo ya mbinu za **kawaida**. Ingawa kuna mbinu kadhaa (Kawaida ya Uzito, Kawaida ya Tabaka), inayotumika zaidi ni Kawaida kwa Batch.

Wazo la **kawaida kwa batch** ni kuzingatia thamani zote katika minibatch, na kufanya kawaida (yaani kutoa wastani na kugawanya kwa kipimo cha kawaida) kulingana na thamani hizo. Imotekelezwa kama tabaka la mtandao linalofanya kawaida hii baada ya kutumia uzito, lakini kabla ya kazi ya uanzishaji. Matokeo yake, tunaweza kuona usahihi wa juu wa mwisho na mafunzo ya haraka.

Hapa kuna [karatasi ya asili](https://arxiv.org/pdf/1502.03167.pdf) juu ya kuwaida kwa batch, [maelezo kwenye Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), na [chapisho nzuri la blogu la utangulizi](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (na moja [kwa Kirusi](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** ni mbinu ya kuvutia inayochukua asilimia fulani ya neurons kwa nasibu wakati wa mafunzo. Pia hufanyiwa kama tabaka lenye parameta moja (asilimia ya neurons kuondolewa, kawaida 10%-50%), na wakati wa mafunzo huweka sifuri vipengele vya nasibu vya vector ya kuingiza, kabla ya kupeleka kwenye tabaka linalofuata.

Ingawa inaweza kuonekana kama wazo la ajabu, unaweza kuona athari ya dropout kwenye mafunzo ya kitaalam wa vokali za MNIST katika daftari la [`Dropout.ipynb`](Dropout.ipynb). Hufanya mafunzo yawe ya haraka na hutuzaa usahihi wa juu katika vipindi vya mafunzo vidogo.

Athari hii inaweza kuelezwa kwa njia kadhaa:

 * Inaweza kuchukuliwa kama mshangao wa nasibu kwa mfano, unaochukua optimization kutoka chini ya kimo cha chini cha eneo
 * Inaweza kuchukuliwa kama *kawaida ya mfano isiyo ya moja kwa moja*, kwa sababu tunaweza kusema kwamba wakati wa dropout tunafunza mfano tofauti kidogo

> *Watu wengine husema kuwa mtu aliyelewa anapojaribu kujifunza kitu, atakumbuka vizuri zaidi asubuhi inayofuata, ukilinganisha na mtu asiyekuwa na pombe, kwa sababu ubongo wenye neurons zile zenye kasoro unajaribu kujirekebisha vizuri ili kuelewa maana. Hatujawahi kujipima wenyewe kama hili ni kweli au la*

## Kuzuia Overfitting

Mojawapo ya mambo muhimu sana katika kujifunza kina ni uwezo wa kuzuia [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Ingawa inaweza kuvutia kutumia mfano wa mtandao wa neva wenye nguvu sana, tunapaswa kila mara kusawazisha idadi ya parameta za mfano na idadi ya sampuli za mafunzo.

> Hakikisha unaelewa dhana ya [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) tuliyoianzisha awali!

Kuna njia kadhaa za kuzuia overfitting:

 * Kusimamisha mapema -- kufuatilia makosa kwenye seti ya uthibitisho kwa kuendelea na kusitisha mafunzo wakati makosa ya uthibitisho inaanza kuongezeka.
 * Kuondoa Uzito kwa Wazi / Udhibiti -- kuongeza adhabu ya ziada kwenye kipengele cha hasara kwa thamani kubwa za uzito, ambayo inazuia mfano kupata matokeo yasiyo thabiti
 * Kawaida ya Mfano -- kufunza mifano kadhaa kisha kuchukua wastani wa matokeo. Hii husaidia kupunguza mabadiliko ya matokeo.
 * Dropout (Kawaida ya Mfano Isiyo ya Moja kwa Moja)

## Wasaidizi / Algorithmi za Mafunzo

Sehemu nyingine muhimu ya mafunzo ni kuchagua algorithmi nzuri ya mafunzo. Ingawa **gradient descent** ya kawaida ni chaguo la busara, mara nyingine inaweza kuwa polepole mno, au kusababisha matatizo mengine.

Katika kujifunza kina, tunatumia **Stochastic Gradient Descent** (SGD), ambayo ni gradient descent inayotumika kwa minibatches, zilizochaguliwa kwa nasibu kutoka kwenye seti ya mafunzo. Uzito hubadilishwa kwa kutumia fomula hii:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

Katika **momentum SGD**, tunahifadhi sehemu ya gradient kutoka hatua za awali. Ni sawa na wakati tunapotembea kwa mwendo na kupewa mshtuko kwa mwelekeo mwingine, mwelekeo wetu haubadiliki mara moja, bali huhifadhi sehemu ya mwendo wa awali. Hapa tunaanzisha vekta nyingine v kuwakilisha *mwendo*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Hapa parameta &gamma; inaonyesha kiwango tunachochukua inertia: &gamma;=0 inahusiana na SGD ya kawaida; &gamma;=1 ni sawa na mlinganyo wa mwendo safi.

### Adam, Adagrad, n.k.

Kwa kuwa kila tabaka tunazidisha ishara na matriki W<sub>i</sub>, kutegemeana na ||W<sub>i</sub>||, gradient inaweza kupungua na kuwa karibu na 0, au kuongezeka bila kikomo. Hii ni tatizo la Gradi Zinazopasuka/Kupotea.

Mojawapo ya suluhisho ni kutumia mwelekeo tu wa gradient katika mlinganyo, na kupuuzia thamani halisi, yaani

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), ambapo ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Algorithmi hii inaitwa **Adagrad**. Algorithmi nyingine zinazotumia wazo sawa ni **RMSProp**, **Adam**

> **Adam** inachukuliwa kuwa algorithmi yenye ufanisi mkubwa kwa matumizi mengi, hivyo kama huna uhakika ni ipi utatumia - tumia Adam.

### Kukata Gradient

Kukata gradient ni upanuzi wa wazo hapo juu. Wakati ||&nabla;&lagran;|| &le; &theta;, tunazingatia gradient ya asili katika optimization ya uzito, na wakati ||&nabla;&lagran;|| > &theta; - tunagawa gradient kwa kawaida yake. Hapa &theta; ni parameta, katika hali nyingi tunaweza kuchukua &theta;=1 au &theta;=10.

### Upunguzaji wa Kiwango cha Kujifunza

Mafanikio ya mafunzo mara nyingi hutegemea parameta ya kiwango cha kujifunza &eta;. Ni mantiki kuona kuwa thamani kubwa za &eta; husababisha mafunzo yawe ya haraka, jambo tunalotaka mwanzoni mwa mafunzo, kisha thamani ndogo ya &eta; hutuzaa fursa ya kuboresha mtandao. Hivyo, mara nyingi tunataka kupunguza &eta; wakati wa mchakato wa mafunzo.

Hii inaweza kufanywa kwa kuzidisha &eta; kwa namba fulani (mfano 0.98) baada ya kila mzunguko wa mafunzo, au kwa kutumia **ratiba ya kiwango cha kujifunza** ngumu zaidi.

## Miundo Mbalimbali ya Mitandao

Kuchagua muundo sahihi wa mtandao kwa tatizo lako kunaweza kuwa mgumu. Kawaida, tunachukua muundo ambao umeonyesha kufaulu kwa kazi yetu maalum (au kazi inayofanana). Hapa kuna [muhtasari mzuri](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) wa miundo ya mitandao ya neva kwa kuona kwa kompyuta.

> Ni muhimu kuchagua muundo ambao utakuwa na nguvu ya kutosha kwa idadi ya sampuli za mafunzo tunazozipata. Kuchagua mfano wenye nguvu mno kunaweza kusababisha [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Njia nyingine nzuri ni kutumia muundo ambao utajirekebisha kiotomatiki kulingana na ugumu unaohitajika. Kwa kiasi fulani, muundo wa **ResNet** na **Inception** hurekebisha wenyewe. [Zaidi kuhusu miundo ya kuona kwa kompyuta](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kionyozo**:
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya asili katika lugha yake halisi inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatutojibu kwa kuelewa vibaya au tafsiri potofu zinazotokea kutokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->