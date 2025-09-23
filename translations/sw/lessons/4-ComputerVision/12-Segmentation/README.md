<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-25T20:53:33+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "sw"
}
-->
# Ugawaji

Tumejifunza awali kuhusu Utambuzi wa Vitu, ambao hutuwezesha kutambua vitu kwenye picha kwa kutabiri *mipaka ya vitu* yao. Hata hivyo, kwa baadhi ya kazi hatuhitaji tu mipaka ya vitu, bali pia utambuzi wa vitu kwa usahihi zaidi. Kazi hii inaitwa **ugawaji**.

## [Maswali ya awali ya somo](https://ff-quizzes.netlify.app/en/ai/quiz/23)

Ugawaji unaweza kuonekana kama **utambuzi wa pikseli**, ambapo kwa **kila** pikseli ya picha tunapaswa kutabiri darasa lake (*mandharinyuma* ikiwa mojawapo ya madarasa). Kuna mbinu kuu mbili za ugawaji:

* **Ugawaji wa kisemantiki** huonyesha tu darasa la pikseli, bila kutofautisha kati ya vitu tofauti vya darasa moja.
* **Ugawaji wa kielelezo** hugawanya madarasa katika vielelezo tofauti.

Kwa ugawaji wa kielelezo, kondoo hawa ni vitu tofauti, lakini kwa ugawaji wa kisemantiki kondoo wote wanawakilishwa na darasa moja.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Picha kutoka [makala hii ya blogu](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Kuna usanifu tofauti wa neva kwa ugawaji, lakini yote yana muundo sawa. Kwa namna fulani, ni sawa na autoencoder uliyojifunza awali, lakini badala ya kuvunja picha ya asili, lengo letu ni kuvunja **maski**. Hivyo, mtandao wa ugawaji una sehemu zifuatazo:

* **Encoder** huchukua vipengele kutoka kwenye picha ya ingizo.
* **Decoder** hubadilisha vipengele hivyo kuwa **picha ya maski**, yenye ukubwa sawa na idadi ya njia zinazolingana na idadi ya madarasa.

<img src="images/segm.png" width="80%">

> Picha kutoka [chapisho hili](https://arxiv.org/pdf/2001.05566.pdf)

Tunapaswa kutaja hasa kazi ya hasara inayotumika kwa ugawaji. Tunapotumia autoencoders za kawaida, tunahitaji kupima ufanano kati ya picha mbili, na tunaweza kutumia mean square error (MSE) kufanya hivyo. Katika ugawaji, kila pikseli kwenye picha ya maski ya lengo inawakilisha namba ya darasa (imekodwa kwa njia ya one-hot kwenye kipimo cha tatu), hivyo tunahitaji kutumia kazi za hasara maalum kwa utambuzi - hasara ya msalaba-entropy, iliyopimwa wastani kwa pikseli zote. Ikiwa maski ni ya binary - **binary cross-entropy loss** (BCE) hutumika.

> ✅ One-hot encoding ni njia ya kuweka lebo ya darasa katika vekta yenye urefu sawa na idadi ya madarasa. Angalia [makala hii](https://datagy.io/sklearn-one-hot-encode/) kuhusu mbinu hii.

## Ugawaji kwa Picha za Matibabu

Katika somo hili, tutaona ugawaji ukifanya kazi kwa kufundisha mtandao kutambua nevi za binadamu (pia zinajulikana kama moles) kwenye picha za matibabu. Tutatumia <a href="https://www.fc.up.pt/addi/ph2%20database.html">Hifadhidata ya PH<sup>2</sup></a> ya picha za dermoscopy kama chanzo cha picha. Hifadhidata hii ina picha 200 za madarasa matatu: nevus ya kawaida, nevus isiyo ya kawaida, na melanoma. Picha zote pia zina **maski** inayotambulisha nevus.

> ✅ Mbinu hii ni maalum kwa aina hii ya picha za matibabu, lakini ni matumizi gani mengine ya ulimwengu halisi unayoweza kufikiria?

<img alt="navi" src="images/navi.png"/>

> Picha kutoka Hifadhidata ya PH<sup>2</sup>

Tutafundisha modeli kugawa nevus yoyote kutoka mandharinyuma yake.

## ✍️ Mazoezi: Ugawaji wa Kisemantiki

Fungua daftari zilizo hapa chini ili kujifunza zaidi kuhusu usanifu tofauti wa ugawaji wa kisemantiki, fanya mazoezi ya kufanya kazi nao, na uone jinsi wanavyofanya kazi.

* [Ugawaji wa Kisemantiki Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Ugawaji wa Kisemantiki TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Maswali ya baada ya somo](https://ff-quizzes.netlify.app/en/ai/quiz/24)

## Hitimisho

Ugawaji ni mbinu yenye nguvu sana kwa utambuzi wa picha, ikihama kutoka mipaka ya vitu hadi utambuzi wa kiwango cha pikseli. Ni mbinu inayotumika katika picha za matibabu, miongoni mwa matumizi mengine.

## 🚀 Changamoto

Ugawaji wa mwili ni mojawapo ya kazi za kawaida tunazoweza kufanya na picha za watu. Kazi nyingine muhimu ni pamoja na **utambuzi wa mifupa** na **utambuzi wa mkao**. Jaribu maktaba ya [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) ili kuona jinsi utambuzi wa mkao unavyoweza kutumika.

## Mapitio na Kujifunza Binafsi

Makala hii ya [Wikipedia](https://wikipedia.org/wiki/Image_segmentation) inatoa muhtasari mzuri wa matumizi mbalimbali ya mbinu hii. Jifunze zaidi peke yako kuhusu sehemu ndogo za Ugawaji wa Kielelezo na Ugawaji wa Panoptic katika uwanja huu wa uchunguzi.

## [Kazi ya nyumbani](lab/README.md)

Katika maabara hii, jaribu **ugawaji wa mwili wa binadamu** kwa kutumia [Hifadhidata ya Segmentation Full Body MADS](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) kutoka Kaggle.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya kutafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.