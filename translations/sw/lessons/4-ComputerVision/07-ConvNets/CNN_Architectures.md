<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f7b97b375358cb51a1e098df306bf73",
  "translation_date": "2025-08-25T20:55:29+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md",
  "language_code": "sw"
}
-->
# Miundo Maarufu ya CNN

### VGG-16

VGG-16 ni mtandao uliopata usahihi wa 92.7% katika uainishaji wa ImageNet top-5 mwaka 2014. Ina muundo wa tabaka zifuatazo:

![Tabaka za ImageNet](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.sw.jpg)

Kama unavyoona, VGG inafuata usanifu wa jadi wa piramidi, ambao ni mlolongo wa tabaka za convolution-pooling.

![Piramidi ya ImageNet](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.sw.jpg)

> Picha kutoka [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet ni familia ya mifano iliyopendekezwa na Microsoft Research mwaka 2015. Wazo kuu la ResNet ni kutumia **residual blocks**:

<img src="images/resnet-block.png" width="300"/>

> Picha kutoka [karatasi hii](https://arxiv.org/pdf/1512.03385.pdf)

Sababu ya kutumia njia ya kupitisha utambulisho ni kuruhusu tabaka zetu kutabiri **tofauti** kati ya matokeo ya tabaka ya awali na matokeo ya residual block - hivyo jina *residual*. Vitalu hivi ni rahisi zaidi kufundisha, na mtu anaweza kujenga mitandao yenye mamia ya vitalu hivi (toleo maarufu zaidi ni ResNet-52, ResNet-101 na ResNet-152).

Unaweza pia kufikiria mtandao huu kama unaoweza kurekebisha ugumu wake kulingana na seti ya data. Mwanzoni, unapokuwa unaanza kufundisha mtandao, thamani za uzito ni ndogo, na ishara nyingi hupitia tabaka za utambulisho. Kadri mafunzo yanavyoendelea na uzito unavyokuwa mkubwa, umuhimu wa vigezo vya mtandao huongezeka, na mtandao unarekebisha ili kufanikisha nguvu ya kueleza inayohitajika kwa uainishaji sahihi wa picha za mafunzo.

### Google Inception

Usanifu wa Google Inception unachukua wazo hili hatua moja zaidi, na hujenga kila tabaka la mtandao kama mchanganyiko wa njia kadhaa tofauti:

<img src="images/inception.png" width="400"/>

> Picha kutoka [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Hapa, tunapaswa kusisitiza jukumu la convolution za 1x1, kwa sababu mwanzoni hazionekani kuwa na maana. Kwa nini tungehitaji kupitisha picha kwa kichujio cha 1x1? Hata hivyo, unahitaji kukumbuka kwamba vichujio vya convolution pia hufanya kazi na njia kadhaa za kina (awali - rangi za RGB, katika tabaka zinazofuata - njia za vichujio tofauti), na convolution ya 1x1 hutumika kuchanganya njia hizo za pembejeo kwa kutumia uzito tofauti wa mafunzo. Inaweza pia kuonekana kama kupunguza ukubwa (pooling) juu ya mwelekeo wa njia.

Hapa kuna [blogi nzuri kuhusu hili](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578), na [karatasi ya awali](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

MobileNet ni familia ya mifano yenye ukubwa mdogo, inayofaa kwa vifaa vya rununu. Tumia ikiwa una rasilimali chache, na unaweza kukubali kupunguza usahihi kidogo. Wazo kuu nyuma yake ni kinachoitwa **depthwise separable convolution**, ambacho huruhusu kuwakilisha vichujio vya convolution kwa muundo wa convolution za anga na convolution za 1x1 juu ya njia za kina. Hii inapunguza sana idadi ya vigezo, na kufanya mtandao kuwa mdogo kwa ukubwa, na pia rahisi kufundisha kwa data kidogo.

Hapa kuna [blogi nzuri kuhusu MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Hitimisho

Katika somo hili, umejifunza dhana kuu nyuma ya mitandao ya neva ya maono ya kompyuta - mitandao ya convolution. Miundo halisi inayowezesha uainishaji wa picha, utambuzi wa vitu, na hata mitandao ya kizazi cha picha yote inategemea CNNs, lakini ikiwa na tabaka zaidi na mbinu za ziada za mafunzo.

## 🚀 Changamoto

Katika daftari zinazofuatana, kuna maelezo chini kuhusu jinsi ya kupata usahihi mkubwa zaidi. Fanya majaribio ili kuona kama unaweza kufanikisha usahihi wa juu zaidi.

## [Jaribio baada ya somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/207)

## Mapitio na Kujisomea

Ingawa CNNs hutumika mara nyingi kwa kazi za Maono ya Kompyuta, kwa ujumla ni nzuri kwa kutoa mifumo ya ukubwa wa kudumu. Kwa mfano, ikiwa tunashughulika na sauti, tunaweza pia kutaka kutumia CNNs kutafuta mifumo maalum katika ishara ya sauti - ambapo vichujio vitakuwa vya mwelekeo mmoja (na CNN hii itaitwa 1D-CNN). Pia, wakati mwingine 3D-CNN hutumika kutoa sifa katika nafasi ya mwelekeo mwingi, kama vile matukio fulani yanayotokea kwenye video - CNN inaweza kunasa mifumo fulani ya mabadiliko ya sifa kwa muda. Fanya mapitio na kujisomea kuhusu kazi nyingine zinazoweza kufanywa na CNNs.

## [Kazi](lab/README.md)

Katika maabara hii, unatakiwa kuainisha aina tofauti za paka na mbwa. Picha hizi ni changamano zaidi kuliko seti ya data ya MNIST na zina vipimo vya juu, na kuna zaidi ya madarasa 10.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.