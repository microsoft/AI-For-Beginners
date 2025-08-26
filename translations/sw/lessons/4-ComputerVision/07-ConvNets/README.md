<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "088837b42b7d99198bf62db8a42411e0",
  "translation_date": "2025-08-25T20:55:08+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/README.md",
  "language_code": "sw"
}
-->
# Mitandao ya Neural ya Convolutional

Tumeona hapo awali kwamba mitandao ya neural ni nzuri sana katika kushughulikia picha, na hata perceptron ya tabaka moja inaweza kutambua namba zilizoandikwa kwa mkono kutoka kwenye seti ya data ya MNIST kwa usahihi wa kuridhisha. Hata hivyo, seti ya data ya MNIST ni maalum sana, na namba zote ziko katikati ya picha, jambo ambalo hufanya kazi kuwa rahisi zaidi.

## [Maswali ya awali ya somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/107)

Katika maisha halisi, tunataka kuwa na uwezo wa kutambua vitu kwenye picha bila kujali eneo lao halisi ndani ya picha. Maono ya kompyuta ni tofauti na uainishaji wa kawaida, kwa sababu tunapojaribu kutafuta kitu fulani kwenye picha, tunachanganua picha tukitafuta **mifumo** fulani na mchanganyiko wake. Kwa mfano, tunapotafuta paka, tunaweza kwanza kutafuta mistari ya mlalo, ambayo inaweza kuunda sharubu, na kisha mchanganyiko fulani wa sharubu unaweza kutuambia kwamba ni picha ya paka. Nafasi ya jamaa na uwepo wa mifumo fulani ni muhimu, na si nafasi yao halisi kwenye picha.

Ili kutoa mifumo, tutatumia dhana ya **vichujio vya convolutional**. Kama unavyojua, picha inawakilishwa na matriki ya 2D, au tensor ya 3D yenye kina cha rangi. Kutumia kichujio kunamaanisha kwamba tunachukua **kernel ya kichujio** ndogo, na kwa kila pikseli kwenye picha ya awali tunahesabu wastani wa uzito na pointi za jirani. Tunaweza kuona hili kama dirisha dogo linaloteleza juu ya picha nzima, na kujumlisha pikseli zote kulingana na uzito katika kernel ya kichujio.

![Kichujio cha Mstari Wima](../../../../../translated_images/filter-vert.b7148390ca0bc356ddc7e55555d2481819c1e86ddde9dce4db5e71a69d6f887f.sw.png) | ![Kichujio cha Mstari Mlalo](../../../../../translated_images/filter-horiz.59b80ed4feb946efbe201a7fe3ca95abb3364e266e6fd90820cb893b4d3a6dda.sw.png)
----|----

> Picha na Dmitry Soshnikov

Kwa mfano, tukitumia vichujio vya mstari wima na mlalo vya 3x3 kwenye namba za MNIST, tunaweza kupata sehemu zilizojitokeza (mfano, thamani za juu) ambapo kuna mistari wima na mlalo kwenye picha yetu ya awali. Kwa hivyo, vichujio hivyo viwili vinaweza kutumika "kutafuta" mistari. Vilevile, tunaweza kubuni vichujio tofauti kutafuta mifumo mingine ya kiwango cha chini:

> Picha ya [Leung-Malik Filter Bank](https://www.robots.ox.ac.uk/~vgg/research/texclass/filters.html)

Hata hivyo, wakati tunaweza kubuni vichujio ili kutoa mifumo fulani kwa mikono, tunaweza pia kubuni mtandao kwa njia ambayo utajifunza mifumo hiyo kiotomatiki. Hii ni moja ya mawazo makuu nyuma ya CNN.

## Mawazo Makuu Nyuma ya CNN

Njia ambayo CNN hufanya kazi inategemea mawazo haya muhimu:

* Vichujio vya convolutional vinaweza kutoa mifumo
* Tunaweza kubuni mtandao kwa njia ambayo vichujio vinajifunza kiotomatiki
* Tunaweza kutumia mbinu hiyo hiyo kutafuta mifumo kwenye vipengele vya kiwango cha juu, si tu kwenye picha ya awali. Kwa hivyo uchimbaji wa vipengele wa CNN hufanya kazi kwenye uongozi wa vipengele, kuanzia mchanganyiko wa pikseli za kiwango cha chini, hadi mchanganyiko wa kiwango cha juu wa sehemu za picha.

![Uchimbaji wa Vipengele vya Kihierarkia](../../../../../translated_images/FeatureExtractionCNN.d9b456cbdae7cb643fde3032b81b2940e3cf8be842e29afac3f482725ba7f95c.sw.png)

> Picha kutoka [karatasi ya Hislop-Lynch](https://www.semanticscholar.org/paper/Computer-vision-based-pedestrian-trajectory-Hislop-Lynch/26e6f74853fc9bbb7487b06dc2cf095d36c9021d), kulingana na [tafiti yao](https://dl.acm.org/doi/abs/10.1145/1553374.1553453)

## ✍️ Mazoezi: Mitandao ya Neural ya Convolutional

Tuendelee kuchunguza jinsi mitandao ya neural ya convolutional inavyofanya kazi, na jinsi tunavyoweza kufanikisha vichujio vinavyoweza kufundishwa, kwa kufanya kazi kupitia daftari husika:

* [Mitandao ya Neural ya Convolutional - PyTorch](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsPyTorch.ipynb)
* [Mitandao ya Neural ya Convolutional - TensorFlow](../../../../../lessons/4-ComputerVision/07-ConvNets/ConvNetsTF.ipynb)

## Muundo wa Piramidi

CNN nyingi zinazotumika kwa usindikaji wa picha hufuata kile kinachoitwa muundo wa piramidi. Tabaka la kwanza la convolutional linalotumika kwenye picha za awali kwa kawaida lina idadi ndogo ya vichujio (8-16), ambavyo vinahusiana na mchanganyiko tofauti wa pikseli, kama vile mistari ya mlalo/wima ya mistari. Katika kiwango kinachofuata, tunapunguza vipimo vya anga vya mtandao, na kuongeza idadi ya vichujio, ambavyo vinahusiana na mchanganyiko zaidi wa vipengele rahisi. Kwa kila tabaka, tunapokaribia mklasifaya wa mwisho, vipimo vya anga vya picha hupungua, na idadi ya vichujio huongezeka.

Kwa mfano, hebu tuangalie muundo wa VGG-16, mtandao uliopata usahihi wa 92.7% katika uainishaji wa juu-5 wa ImageNet mwaka 2014:

![Tabaka za ImageNet](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.sw.jpg)

![Piramidi ya ImageNet](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.sw.jpg)

> Picha kutoka [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

## Miundo Maarufu ya CNN

[Endelea kujifunza kuhusu miundo maarufu ya CNN](CNN_Architectures.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.