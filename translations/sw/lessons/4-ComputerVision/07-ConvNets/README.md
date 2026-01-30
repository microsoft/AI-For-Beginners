# Mitandao ya Neural ya Convolutional

Tumeona awali kwamba mitandao ya neural ni nzuri sana katika kushughulikia picha, na hata perceptron ya tabaka moja inaweza kutambua namba zilizoandikwa kwa mkono kutoka kwenye seti ya data ya MNIST kwa usahihi wa kuridhisha. Hata hivyo, seti ya data ya MNIST ni maalum sana, na namba zote ziko katikati ya picha, jambo ambalo hufanya kazi kuwa rahisi.

## [Maswali ya awali ya somo](https://ff-quizzes.netlify.app/en/ai/quiz/13)

Katika maisha halisi, tunataka kuwa na uwezo wa kutambua vitu kwenye picha bila kujali mahali halisi vilipo kwenye picha. Maono ya kompyuta ni tofauti na uainishaji wa kawaida, kwa sababu tunapojaribu kutafuta kitu fulani kwenye picha, tunachanganua picha tukitafuta **mifumo** fulani na mchanganyiko wake. Kwa mfano, tunapotafuta paka, tunaweza kwanza kutafuta mistari ya mlalo, ambayo inaweza kuunda sharubu, na kisha mchanganyiko fulani wa sharubu unaweza kutuambia kwamba hiyo ni picha ya paka. Nafasi ya jamaa na uwepo wa mifumo fulani ni muhimu, na si mahali pake halisi kwenye picha.

Ili kutoa mifumo, tutatumia dhana ya **vichujio vya convolutional**. Kama unavyojua, picha inawakilishwa na matriki ya 2D, au tensor ya 3D yenye kina cha rangi. Kutumia kichujio kunamaanisha kwamba tunachukua matriki ndogo ya **kernel ya kichujio**, na kwa kila pikseli kwenye picha ya awali tunahesabu wastani wa uzito na pointi za jirani. Tunaweza kuona hili kama dirisha dogo linalosonga juu ya picha nzima, na kujumlisha pikseli zote kulingana na uzito katika matriki ya kernel ya kichujio.

![Kichujio cha Mstari Wima](../../../../../translated_images/sw/filter-vert.b7148390ca0bc356.webp) | ![Kichujio cha Mstari Mlalo](../../../../../translated_images/sw/filter-horiz.59b80ed4feb946ef.webp)
----|----

> Picha na Dmitry Soshnikov

Kwa mfano, tukitumia vichujio vya mstari wima na mstari mlalo vya 3x3 kwenye namba za MNIST, tunaweza kupata sehemu zenye mwangaza (mfano, thamani za juu) ambapo kuna mistari wima na mlalo kwenye picha yetu ya awali. Kwa hivyo vichujio hivyo viwili vinaweza kutumika "kutafuta" mistari. Vivyo hivyo, tunaweza kubuni vichujio tofauti kutafuta mifumo mingine ya kiwango cha chini:

<img src="../../../../../translated_images/sw/lmfilters.ea9e4868a82cf74c.webp" width="500" align="center"/>

> Picha ya [Leung-Malik Filter Bank](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

Hata hivyo, ingawa tunaweza kubuni vichujio ili kutoa mifumo fulani kwa mikono, tunaweza pia kubuni mtandao kwa njia ambayo utajifunza mifumo kiotomatiki. Hii ni moja ya mawazo makuu nyuma ya CNN.

## Mawazo Makuu Nyuma ya CNN

Njia CNN zinavyofanya kazi inategemea mawazo muhimu yafuatayo:

* Vichujio vya convolutional vinaweza kutoa mifumo
* Tunaweza kubuni mtandao kwa njia ambayo vichujio vinajifunza kiotomatiki
* Tunaweza kutumia mbinu hiyo hiyo kutafuta mifumo kwenye vipengele vya kiwango cha juu, si tu kwenye picha ya awali. Kwa hivyo uchimbaji wa vipengele vya CNN hufanya kazi kwenye uhierakia wa vipengele, kuanzia mchanganyiko wa pikseli za kiwango cha chini, hadi mchanganyiko wa kiwango cha juu wa sehemu za picha.

![Uchimbaji wa Vipengele vya Kihierakia](../../../../../translated_images/sw/FeatureExtractionCNN.d9b456cbdae7cb64.webp)

> Picha kutoka [karatasi ya Hislop-Lynch](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), kulingana na [utafiti wao](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Mazoezi: Mitandao ya Neural ya Convolutional

Tuendelee kuchunguza jinsi mitandao ya neural ya convolutional inavyofanya kazi, na jinsi tunavyoweza kufanikisha vichujio vinavyoweza kufundishwa, kwa kufanya kazi kupitia daftari husika:

* [Mitandao ya Neural ya Convolutional - PyTorch](ConvNetsPyTorch.ipynb)
* [Mitandao ya Neural ya Convolutional - TensorFlow](ConvNetsTF.ipynb)

## Muundo wa Piramidi

CNN nyingi zinazotumika kwa usindikaji wa picha hufuata kile kinachoitwa muundo wa piramidi. Tabaka la kwanza la convolutional linalotumika kwenye picha za awali kwa kawaida lina idadi ndogo ya vichujio (8-16), ambavyo vinahusiana na mchanganyiko tofauti wa pikseli, kama mistari ya mlalo/wima ya mistari. Katika kiwango kinachofuata, tunapunguza mwelekeo wa anga wa mtandao, na kuongeza idadi ya vichujio, ambavyo vinahusiana na mchanganyiko zaidi wa vipengele rahisi. Kwa kila tabaka, tunapokaribia kihakiki cha mwisho, vipimo vya anga vya picha vinapungua, na idadi ya vichujio inaongezeka.

Kwa mfano, hebu tuangalie muundo wa VGG-16, mtandao uliopata usahihi wa 92.7% katika uainishaji wa juu-5 wa ImageNet mwaka 2014:

![Tabaka za ImageNet](../../../../../translated_images/sw/vgg-16-arch1.d901a5583b3a51ba.webp)

![Piramidi ya ImageNet](../../../../../translated_images/sw/vgg-16-arch.64ff2137f50dd49f.webp)

> Picha kutoka [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## Miundo Maarufu ya CNN

[Endelea kujifunza kuhusu miundo maarufu ya CNN](CNN_Architectures.md)

---

