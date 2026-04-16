# Mbinu za Mafunzo ya Kujifunza Kina

Kadri mitandao ya neva inavyozidi kuwa na kina, mchakato wa mafunzo yake unazidi kuwa changamoto. Tatizo moja kubwa ni kinachojulikana kama [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) au [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Chapisho hili](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) linatoa utangulizi mzuri kuhusu matatizo haya.

Ili kufanya mafunzo ya mitandao yenye kina kuwa bora zaidi, kuna mbinu kadhaa zinazoweza kutumika.

## Kuweka Thamani Kwenye Kipimo Kinachofaa

Ili kufanya hesabu za namba kuwa thabiti zaidi, tunataka kuhakikisha kuwa thamani zote ndani ya mtandao wetu wa neva ziko kwenye kipimo kinachofaa, kwa kawaida [-1..1] au [0..1]. Hili si hitaji kali sana, lakini asili ya hesabu za namba za kuelea ni kwamba thamani za ukubwa tofauti haziwezi kushughulikiwa kwa usahihi pamoja. Kwa mfano, tukijumlisha 10<sup>-10</sup> na 10<sup>10</sup>, kuna uwezekano mkubwa tutapata 10<sup>10</sup>, kwa sababu thamani ndogo itabadilishwa kuwa kiwango sawa na ile kubwa, na hivyo mantissa itapotea.

Kazi nyingi za uanzishaji zina hali zisizo za mstari karibu na [-1..1], na kwa hivyo inafaa kupima data yote ya ingizo kwenye kipimo cha [-1..1] au [0..1].

## Uanzishaji wa Awali wa Uzito

Kwa hali bora, tunataka thamani ziwe kwenye kipimo sawa baada ya kupita kwenye tabaka za mtandao. Kwa hivyo ni muhimu kuanzisha uzito kwa njia ambayo inahifadhi usambazaji wa thamani.

Usambazaji wa kawaida **N(0,1)** si wazo zuri, kwa sababu ikiwa tuna *n* ingizo, upotofu wa kawaida wa matokeo utakuwa *n*, na thamani zinaweza kuruka nje ya kipimo cha [0..1].

Uanzishaji ufuatao mara nyingi hutumika:

- Usambazaji wa sare -- `uniform`
- **N(0,1/n)** -- `gaussian`
- **N(0,1/√n_in)** inahakikisha kuwa kwa ingizo lenye wastani wa sifuri na upotofu wa kawaida wa 1, wastani/upotofu wa kawaida utabaki sawa
- **N(0,√2/(n_in+n_out))** -- kinachojulikana kama **Xavier initialization** (`glorot`), husaidia kuweka ishara kwenye kipimo wakati wa upitishaji wa mbele na nyuma

## Kawaida ya Kundi

Hata kwa uanzishaji sahihi wa uzito, uzito unaweza kuwa mkubwa au mdogo kiholela wakati wa mafunzo, na wataondoa ishara nje ya kipimo kinachofaa. Tunaweza kurudisha ishara kwa kutumia mojawapo ya mbinu za **kawaida**. Ingawa kuna kadhaa (Kawaida ya Uzito, Kawaida ya Tabaka), inayotumika zaidi ni Kawaida ya Kundi.

Wazo la **kawaida ya kundi** ni kuzingatia thamani zote kwenye kundi dogo, na kufanya kawaida (yaani, kutoa wastani na kugawanya kwa upotofu wa kawaida) kulingana na thamani hizo. Inatekelezwa kama tabaka la mtandao ambalo hufanya kawaida hii baada ya kutumia uzito, lakini kabla ya kazi ya uanzishaji. Matokeo yake, kuna uwezekano wa kuona usahihi wa mwisho wa juu na mafunzo ya haraka.

Hapa kuna [karatasi ya asili](https://arxiv.org/pdf/1502.03167.pdf) kuhusu kawaida ya kundi, [maelezo kwenye Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), na [chapisho la blogu la utangulizi mzuri](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (na moja [kwa Kirusi](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** ni mbinu ya kuvutia inayotoa asilimia fulani ya neurons kwa nasibu wakati wa mafunzo. Pia inatekelezwa kama tabaka lenye kigezo kimoja (asilimia ya neurons za kuondoa, kwa kawaida 10%-50%), na wakati wa mafunzo inafuta vipengele vya nasibu vya vector ya ingizo, kabla ya kuipitisha kwenye tabaka inayofuata.

Ingawa hii inaweza kuonekana kama wazo la ajabu, unaweza kuona athari ya dropout kwenye mafunzo ya classifier ya tarakimu ya MNIST katika daftari [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb). Inaharakisha mafunzo na inatuwezesha kufikia usahihi wa juu katika vipindi vichache vya mafunzo.

Athari hii inaweza kuelezewa kwa njia kadhaa:

- Inaweza kuchukuliwa kuwa ni mshtuko wa nasibu kwa modeli, ambao unatoa uboreshaji nje ya kiwango cha chini cha ndani
- Inaweza kuchukuliwa kama *kawaida ya modeli isiyo ya moja kwa moja*, kwa sababu tunaweza kusema kwamba wakati wa dropout tunafundisha modeli tofauti kidogo

> *Watu wengine wanasema kwamba mtu mlevi anapojaribu kujifunza kitu, atakumbuka vizuri zaidi asubuhi inayofuata, ikilinganishwa na mtu asiye mlevi, kwa sababu ubongo wenye neurons zinazofanya kazi vibaya unajaribu kujifunza vizuri zaidi. Hatujawahi kujaribu wenyewe kama hili ni kweli au la.*

## Kuzuia Overfitting

Moja ya vipengele muhimu sana vya kujifunza kina ni kuweza kuzuia [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Ingawa inaweza kuwa ya kuvutia kutumia modeli yenye nguvu sana ya mtandao wa neva, tunapaswa kila wakati kusawazisha idadi ya vigezo vya modeli na idadi ya sampuli za mafunzo.

> Hakikisha unaelewa dhana ya [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) tuliyoanzisha awali!

Kuna njia kadhaa za kuzuia overfitting:

- Kusimamisha mapema -- kufuatilia makosa kwenye seti ya uthibitishaji na kusimamisha mafunzo wakati makosa ya uthibitishaji yanaanza kuongezeka.
- Kupungua kwa Uzito wa Wazi / Kawaida -- kuongeza adhabu ya ziada kwenye kazi ya hasara kwa thamani kubwa za uzito, ambayo huzuia modeli kupata matokeo yasiyo thabiti sana
- Kawaida ya Modeli -- kufundisha modeli kadhaa na kisha kujumlisha matokeo. Hii husaidia kupunguza tofauti.
- Dropout (Kawaida ya Modeli Isiyo ya Moja kwa Moja)

## Optimizers / Algorithms za Mafunzo

Jambo lingine muhimu la mafunzo ni kuchagua algorithm nzuri ya mafunzo. Ingawa **gradient descent** ya kawaida ni chaguo la busara, wakati mwingine inaweza kuwa polepole sana, au kusababisha matatizo mengine.

Katika kujifunza kina, tunatumia **Stochastic Gradient Descent** (SGD), ambayo ni gradient descent inayotumika kwa minibatches, zilizochaguliwa kwa nasibu kutoka kwenye seti ya mafunzo. Uzito hubadilishwa kwa kutumia fomula hii:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

Katika **momentum SGD**, tunahifadhi sehemu ya gradient kutoka hatua za awali. Ni sawa na tunaposonga mahali fulani kwa kasi, na tunapokea mshtuko katika mwelekeo tofauti, mwelekeo wetu hauwezi kubadilika mara moja, lakini unahifadhi sehemu ya mwendo wa awali. Hapa tunaanzisha vector nyingine v kuwakilisha *kasi*:

- v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
- w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Hapa kigezo γ kinaonyesha kiwango ambacho tunazingatia kasi: γ=0 inalingana na SGD ya kawaida; γ=1 ni equation ya mwendo safi.

### Adam, Adagrad, nk.

Kwa kuwa katika kila tabaka tunazidisha ishara kwa matrix W<sub>i</sub>, kulingana na ||W<sub>i</sub>||, gradient inaweza kupungua na kuwa karibu na 0, au kupanda bila kikomo. Hii ndiyo kiini cha tatizo la Exploding/Vanishing Gradients.

Moja ya suluhisho la tatizo hili ni kutumia mwelekeo tu wa gradient katika equation, na kupuuza thamani halisi, yaani

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), ambapo ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Algorithm hii inaitwa **Adagrad**. Algorithm nyingine zinazotumia wazo hili: **RMSProp**, **Adam**

> **Adam** inachukuliwa kuwa algorithm yenye ufanisi sana kwa matumizi mengi, kwa hivyo ikiwa huna uhakika ni ipi ya kutumia - tumia Adam.

### Gradient clipping

Gradient clipping ni upanuzi wa wazo hapo juu. Wakati ||∇ℒ|| ≤ θ, tunazingatia gradient ya awali katika uboreshaji wa uzito, na wakati ||∇ℒ|| > θ - tunagawanya gradient kwa norm yake. Hapa θ ni kigezo, katika hali nyingi tunaweza kuchukua θ=1 au θ=10.

### Kupungua kwa Kiwango cha Kujifunza

Mafanikio ya mafunzo mara nyingi hutegemea kigezo cha kiwango cha kujifunza η. Ni mantiki kudhani kwamba thamani kubwa za η husababisha mafunzo ya haraka, ambayo ni kitu tunachotaka kwa kawaida mwanzoni mwa mafunzo, na kisha thamani ndogo za η zinaturuhusu kurekebisha mtandao. Kwa hivyo, katika hali nyingi tunataka kupunguza η katika mchakato wa mafunzo.

Hii inaweza kufanywa kwa kuzidisha η kwa nambari fulani (mfano 0.98) baada ya kila kipindi cha mafunzo, au kwa kutumia ratiba ya kiwango cha kujifunza iliyo ngumu zaidi.

## Miundo Tofauti ya Mitandao

Kuchagua muundo sahihi wa mtandao kwa tatizo lako inaweza kuwa changamoto. Kwa kawaida, tungechukua muundo ambao umethibitishwa kufanya kazi kwa kazi yetu maalum (au inayofanana). Hapa kuna [muhtasari mzuri](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) wa miundo ya mitandao ya neva kwa maono ya kompyuta.

> Ni muhimu kuchagua muundo ambao utakuwa na nguvu ya kutosha kwa idadi ya sampuli za mafunzo tulizo nazo. Kuchagua modeli yenye nguvu sana kunaweza kusababisha [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Njia nyingine nzuri inaweza kuwa kutumia muundo ambao utajirekebisha kiotomatiki kwa ugumu unaohitajika. Kwa kiwango fulani, muundo wa **ResNet** na **Inception** unajirekebisha. [Zaidi kuhusu miundo ya maono ya kompyuta](../07-ConvNets/CNN_Architectures.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.