<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "717775c4050ccbffbe0c961ad8bf7bf7",
  "translation_date": "2025-08-25T20:56:35+00:00",
  "source_file": "lessons/4-ComputerVision/08-TransferLearning/README.md",
  "language_code": "sw"
}
-->
# Mitandao Iliyojifunza Tayari na Uhamishaji wa Kujifunza

Kufundisha CNNs kunaweza kuchukua muda mwingi, na data nyingi zinahitajika kwa kazi hiyo. Hata hivyo, muda mwingi hutumika kujifunza vichujio vya kiwango cha chini ambavyo mtandao unaweza kutumia kutoa mifumo kutoka kwenye picha. Swali la asili linajitokeza - je, tunaweza kutumia mtandao wa neva uliowekwa tayari kwenye seti moja ya data na kuubadilisha ili kuainisha picha tofauti bila kuhitaji mchakato kamili wa mafunzo?

## [Jaribio la Kabla ya Somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/108)

Mbinu hii inaitwa **uhamishaji wa kujifunza**, kwa sababu tunahamisha maarifa fulani kutoka kwa mfano mmoja wa mtandao wa neva kwenda mwingine. Katika uhamishaji wa kujifunza, mara nyingi tunaanza na mfano uliowekwa tayari, ambao umefundishwa kwenye seti kubwa ya data ya picha, kama vile **ImageNet**. Mifano hiyo tayari inaweza kufanya kazi nzuri ya kutoa vipengele tofauti kutoka kwa picha za jumla, na mara nyingi kujenga kionainishaji juu ya vipengele hivyo vilivyotolewa kunaweza kutoa matokeo mazuri.

> ✅ Uhamishaji wa Kujifunza ni neno linalopatikana katika nyanja nyingine za kitaaluma, kama vile Elimu. Linahusu mchakato wa kuchukua maarifa kutoka uwanja mmoja na kuyatumia katika mwingine.

## Mifano Iliyojifunza Tayari kama Vitoa Vipengele

Mitandao ya convolutional tuliyozungumzia katika sehemu iliyopita ina tabaka kadhaa, kila moja ikiwa na jukumu la kutoa vipengele fulani kutoka kwenye picha, kuanzia mchanganyiko wa pikseli wa kiwango cha chini (kama vile mistari ya mlalo/wima au mistari ya mdundo), hadi mchanganyiko wa kiwango cha juu wa vipengele, vinavyohusiana na vitu kama jicho la moto. Ikiwa tutafundisha CNN kwenye seti kubwa ya data ya picha za jumla na tofauti, mtandao unapaswa kujifunza kutoa vipengele hivyo vya kawaida.

Zote Keras na PyTorch zina kazi za kupakia kwa urahisi uzito wa mitandao ya neva iliyojifunza tayari kwa baadhi ya usanifu wa kawaida, nyingi zikiwa zimefundishwa kwenye picha za ImageNet. Zile zinazotumika mara nyingi zimeelezwa kwenye ukurasa wa [Usanifu wa CNN](../07-ConvNets/CNN_Architectures.md) kutoka somo lililopita. Hasa, unaweza kufikiria kutumia mojawapo ya zifuatazo:

* **VGG-16/VGG-19** ambazo ni mifano rahisi inayotoa usahihi mzuri. Mara nyingi kutumia VGG kama jaribio la kwanza ni chaguo zuri kuona jinsi uhamishaji wa kujifunza unavyofanya kazi.
* **ResNet** ni familia ya mifano iliyopendekezwa na Microsoft Research mwaka 2015. Ina tabaka nyingi zaidi, na hivyo inahitaji rasilimali zaidi.
* **MobileNet** ni familia ya mifano yenye ukubwa mdogo, inayofaa kwa vifaa vya rununu. Tumia ikiwa una rasilimali chache na unaweza kukubali kupoteza usahihi kidogo.

Hapa kuna sampuli za vipengele vilivyotolewa kutoka kwenye picha ya paka na mtandao wa VGG-16:

![Vipengele vilivyotolewa na VGG-16](../../../../../translated_images/features.6291f9c7ba3a0b951af88fc9864632b9115365410765680680d30c927dd67354.sw.png)

## Seti ya Data ya Paka dhidi ya Mbwa

Katika mfano huu, tutatumia seti ya data ya [Paka na Mbwa](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), ambayo inakaribia hali halisi ya uainishaji wa picha.

## ✍️ Zoezi: Uhamishaji wa Kujifunza

Hebu tuone uhamishaji wa kujifunza ukiwa kazini katika daftari zinazohusiana:

* [Uhamishaji wa Kujifunza - PyTorch](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningPyTorch.ipynb)
* [Uhamishaji wa Kujifunza - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/TransferLearningTF.ipynb)

## Kuonyesha Picha ya Paka Adhimu

Mtandao wa neva uliowekwa tayari una mifumo tofauti ndani ya *ubongo* wake, ikijumuisha dhana za **paka bora** (pamoja na mbwa bora, pundamilia bora, n.k.). Itakuwa ya kuvutia kujaribu **kuonyesha picha hii**. Hata hivyo, si rahisi, kwa sababu mifumo imeenea kwenye uzito wa mtandao, na pia imepangwa katika muundo wa kihierarkia.

Njia moja tunayoweza kutumia ni kuanza na picha ya nasibu, kisha kujaribu kutumia mbinu ya **optimizoni ya mteremko wa gradienti** kurekebisha picha hiyo kwa njia ambayo mtandao unaanza kufikiria kuwa ni paka.

![Mzunguko wa Optimizoni ya Picha](../../../../../translated_images/ideal-cat-loop.999fbb8ff306e044f997032f4eef9152b453e6a990e449bbfb107de2493cc37e.sw.png)

Hata hivyo, tukifanya hivi, tutapata kitu kinachofanana sana na kelele ya nasibu. Hii ni kwa sababu *kuna njia nyingi za kufanya mtandao kufikiria picha ya ingizo ni paka*, ikijumuisha zile ambazo hazina maana kwa macho. Ingawa picha hizo zina mifumo mingi ya kawaida kwa paka, hakuna kinachozuia kuwa za kuvutia kwa macho.

Ili kuboresha matokeo, tunaweza kuongeza kipengele kingine kwenye kazi ya hasara, kinachoitwa **hasara ya tofauti**. Ni kipimo kinachoonyesha jinsi pikseli za jirani za picha zinavyofanana. Kupunguza hasara ya tofauti hufanya picha kuwa laini, na kuondoa kelele - hivyo kufichua mifumo ya kuvutia zaidi kwa macho. Hapa kuna mfano wa picha kama hizo "bora", zinazotambuliwa kama paka na kama pundamilia kwa uwezekano mkubwa:

![Paka Bora](../../../../../translated_images/ideal-cat.203dd4597643d6b0bd73038b87f9c0464322725e3a06ab145d25d4a861c70592.sw.png) | ![Pundamilia Bora](../../../../../translated_images/ideal-zebra.7f70e8b54ee15a7a314000bb5df38a6cfe086ea04d60df4d3ef313d046b98a2b.sw.png)
-----|-----
 *Paka Bora* | *Pundamilia Bora*

Njia kama hiyo inaweza kutumika kufanya kile kinachoitwa **mashambulizi ya hila** kwenye mtandao wa neva. Tuseme tunataka kuudanganya mtandao wa neva na kufanya mbwa aonekane kama paka. Ikiwa tutachukua picha ya mbwa, ambayo inatambuliwa na mtandao kama mbwa, tunaweza kuibadilisha kidogo kwa kutumia optimizoni ya mteremko wa gradienti, hadi mtandao uanze kuitambua kama paka:

![Picha ya Mbwa](../../../../../translated_images/original-dog.8f68a67d2fe0911f33041c0f7fce8aa4ea919f9d3917ec4b468298522aeb6356.sw.png) | ![Picha ya mbwa inayotambuliwa kama paka](../../../../../translated_images/adversarial-dog.d9fc7773b0142b89752539bfbf884118de845b3851c5162146ea0b8809fc820f.sw.png)
-----|-----
*Picha ya asili ya mbwa* | *Picha ya mbwa inayotambuliwa kama paka*

Tazama msimbo wa kuzalisha matokeo hapo juu katika daftari ifuatayo:

* [Paka Bora na wa Hila - TensorFlow](../../../../../lessons/4-ComputerVision/08-TransferLearning/AdversarialCat_TF.ipynb)

## Hitimisho

Kwa kutumia uhamishaji wa kujifunza, unaweza kuunda haraka kionainishaji kwa kazi ya uainishaji wa kitu maalum na kufanikisha usahihi wa juu. Unaweza kuona kwamba kazi ngumu zaidi tunazotatua sasa zinahitaji nguvu kubwa ya kompyuta, na haziwezi kutatuliwa kwa urahisi kwenye CPU. Katika kitengo kijacho, tutajaribu kutumia utekelezaji mwepesi zaidi kufundisha mfano huo kwa kutumia rasilimali za chini, ambayo husababisha kupungua kidogo kwa usahihi.

## 🚀 Changamoto

Katika daftari zinazohusiana, kuna maelezo chini kuhusu jinsi maarifa ya uhamishaji hufanya kazi vyema na data ya mafunzo inayofanana kiasi (aina mpya ya mnyama, labda). Fanya majaribio na aina mpya kabisa za picha ili kuona jinsi mifano yako ya maarifa ya uhamishaji inavyofanya kazi vizuri au vibaya.

## [Jaribio la Baada ya Somo](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Mapitio na Kujisomea

Soma [TrainingTricks.md](TrainingTricks.md) ili kuongeza maarifa yako kuhusu njia nyingine za kufundisha mifano yako.

## [Kazi](lab/README.md)

Katika maabara hii, tutatumia seti halisi ya data ya wanyama wa kipenzi ya [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) yenye aina 35 za paka na mbwa, na tutajenga kionainishaji cha uhamishaji wa kujifunza.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.