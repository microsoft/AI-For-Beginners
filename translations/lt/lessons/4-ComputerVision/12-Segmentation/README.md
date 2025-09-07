<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-31T17:42:34+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "lt"
}
-->
# Segmentacija

Anksčiau mokėmės apie objektų atpažinimą, kuris leidžia nustatyti objektų vietą paveikslėlyje, prognozuojant jų *apibrėžimo dėžutes* (bounding boxes). Tačiau kai kurioms užduotims mums reikia ne tik apibrėžimo dėžučių, bet ir tikslesnės objektų lokalizacijos. Ši užduotis vadinama **segmentacija**.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

Segmentaciją galima suprasti kaip **pikselių klasifikaciją**, kur kiekvienam paveikslėlio pikseliui turime prognozuoti jo klasę (*fonas* yra viena iš klasių). Yra du pagrindiniai segmentacijos algoritmai:

* **Semantinė segmentacija** nurodo tik pikselio klasę ir neskiria skirtingų tos pačios klasės objektų.
* **Objektų segmentacija** (instance segmentation) padalina klases į skirtingus objektus.

Pavyzdžiui, objektų segmentacijoje šios avys yra skirtingi objektai, tačiau semantinėje segmentacijoje visos avys yra atvaizduojamos kaip viena klasė.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Paveikslėlis iš [šio tinklaraščio įrašo](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Yra įvairių neuroninių tinklų architektūrų segmentacijai, tačiau jos visos turi tą pačią struktūrą. Tam tikra prasme tai panašu į autoenkoderį, apie kurį mokėtės anksčiau, tačiau vietoj originalaus paveikslėlio rekonstrukcijos mūsų tikslas yra rekonstruoti **kaukę**. Taigi segmentacijos tinklas turi šias dalis:

* **Koderis** (encoder) išgauna savybes iš įvesties paveikslėlio.
* **Dekoderis** (decoder) transformuoja šias savybes į **kaukės paveikslėlį**, kurio dydis ir kanalų skaičius atitinka klasių skaičių.

<img src="images/segm.png" width="80%">

> Paveikslėlis iš [šios publikacijos](https://arxiv.org/pdf/2001.05566.pdf)

Ypatingą dėmesį reikėtų skirti nuostolių funkcijai, naudojamai segmentacijai. Naudojant klasikinius autoenkoderius, reikia matuoti dviejų paveikslėlių panašumą, ir tam galima naudoti vidutinės kvadratinės paklaidos (MSE) metodą. Segmentacijoje kiekvienas taikinio kaukės paveikslėlio pikselis atspindi klasės numerį (vieno karšto kodavimo būdu užkoduotą trečioje dimensijoje), todėl reikia naudoti klasifikacijai skirtas nuostolių funkcijas - kryžminės entropijos nuostolius, vidutiniškai apskaičiuotus visiems pikseliams. Jei kaukė yra dvejetainė, naudojami **dvejetainės kryžminės entropijos nuostoliai** (BCE).

> ✅ Vieno karšto kodavimas (one-hot encoding) yra būdas užkoduoti klasės etiketę į vektorių, kurio ilgis lygus klasių skaičiui. Pažvelkite į [šį straipsnį](https://datagy.io/sklearn-one-hot-encode/) apie šią techniką.

## Segmentacija medicininiams vaizdams

Šioje pamokoje pamatysime segmentaciją veikiant, treniruodami tinklą atpažinti žmogaus apgamus (dar vadinamus nevusais) medicininiuose vaizduose. Naudosime <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> duomenų bazę</a>, kurioje yra dermatoskopijos vaizdai. Šiame duomenų rinkinyje yra 200 vaizdų, suskirstytų į tris klases: tipinis apgamas, netipinis apgamas ir melanoma. Visi vaizdai taip pat turi atitinkamą **kaukę**, kuri apibrėžia apgamą.

> ✅ Ši technika ypač tinkama tokio tipo medicininiams vaizdams, tačiau kokias kitas realaus pasaulio taikymo sritis galėtumėte įsivaizduoti?

<img alt="navi" src="images/navi.png"/>

> Paveikslėlis iš PH<sup>2</sup> duomenų bazės

Mes treniruosime modelį, kad jis galėtų atskirti bet kokį apgamą nuo fono.

## ✍️ Pratimai: Semantinė segmentacija

Atidarykite žemiau pateiktus užrašus, kad sužinotumėte daugiau apie skirtingas semantinės segmentacijos architektūras, praktikuotumėte darbą su jomis ir pamatytumėte jas veikiant.

* [Semantinė segmentacija Pytorch](SemanticSegmentationPytorch.ipynb)
* [Semantinė segmentacija TensorFlow](SemanticSegmentationTF.ipynb)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Išvada

Segmentacija yra labai galinga technika vaizdų klasifikavimui, pereinant nuo apibrėžimo dėžučių prie pikselių lygio klasifikacijos. Ji naudojama medicininiuose vaizduose ir kitose srityse.

## 🚀 Iššūkis

Kūno segmentacija yra tik viena iš įprastų užduočių, kurias galime atlikti su žmonių vaizdais. Kitos svarbios užduotys apima **skeletų aptikimą** ir **pozų aptikimą**. Išbandykite [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) biblioteką, kad pamatytumėte, kaip galima naudoti pozų aptikimą.

## Peržiūra ir savarankiškas mokymasis

Šis [Vikipedijos straipsnis](https://wikipedia.org/wiki/Image_segmentation) siūlo gerą šios technikos įvairių taikymo sričių apžvalgą. Sužinokite daugiau savarankiškai apie objektų segmentacijos ir panoraminės segmentacijos subdomenus šioje srityje.

## [Užduotis](lab/README.md)

Šioje laboratorijoje išbandykite **žmogaus kūno segmentaciją**, naudodami [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) iš Kaggle.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius dėl šio vertimo naudojimo.