<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b544f20b796402507fb05a0df893323",
  "translation_date": "2025-08-25T21:00:46+00:00",
  "source_file": "lessons/3-NeuralNetworks/05-Frameworks/README.md",
  "language_code": "sw"
}
-->
# Mfumo wa Mitandao ya Neural

Kama tulivyojifunza tayari, ili kufundisha mitandao ya neural kwa ufanisi tunahitaji kufanya mambo mawili:

* Kufanya kazi na tensors, kwa mfano kuzidisha, kuongeza, na kuhesabu baadhi ya kazi kama sigmoid au softmax  
* Kuhesabu derivatives za maelezo yote, ili kufanya uboreshaji wa gradient descent  

## [Jaribio la kabla ya somo](https://ff-quizzes.netlify.app/en/ai/quiz/9)

Ingawa maktaba ya `numpy` inaweza kufanya sehemu ya kwanza, tunahitaji utaratibu wa kuhesabu derivatives. Katika [mfumo wetu](../../../../../lessons/3-NeuralNetworks/04-OwnFramework/OwnFramework.ipynb) ambao tumeunda katika sehemu iliyopita, tulilazimika kuandika kwa mkono kazi zote za derivatives ndani ya njia ya `backward`, ambayo hufanya backpropagation. Kwa hali bora, mfumo unapaswa kutupa fursa ya kuhesabu derivatives za *maelezo yoyote* tunayoweza kufafanua.

Jambo lingine muhimu ni uwezo wa kufanya mahesabu kwenye GPU, au vitengo vingine maalum vya mahesabu, kama [TPU](https://en.wikipedia.org/wiki/Tensor_Processing_Unit). Mafunzo ya mitandao ya neural ya kina yanahitaji *mahesabu mengi sana*, na uwezo wa kuendesha mahesabu hayo kwa sambamba kwenye GPUs ni muhimu sana.

> ✅ Neno 'kuendesha kwa sambamba' linamaanisha kusambaza mahesabu kwenye vifaa vingi.

Kwa sasa, mifumo miwili maarufu zaidi ya neural ni: [TensorFlow](http://TensorFlow.org) na [PyTorch](https://pytorch.org/). Zote mbili zinatoa API ya kiwango cha chini kufanya kazi na tensors kwenye CPU na GPU. Juu ya API ya kiwango cha chini, kuna pia API ya kiwango cha juu, inayoitwa [Keras](https://keras.io/) na [PyTorch Lightning](https://pytorchlightning.ai/) kwa mtiririko huo.

Low-Level API | [TensorFlow](http://TensorFlow.org) | [PyTorch](https://pytorch.org/)  
--------------|-------------------------------------|--------------------------------  
High-level API| [Keras](https://keras.io/) | [PyTorch Lightning](https://pytorchlightning.ai/)  

**APIs za kiwango cha chini** katika mifumo yote miwili hukuruhusu kujenga kinachoitwa **michoro ya mahesabu**. Mchoro huu hufafanua jinsi ya kuhesabu matokeo (kawaida kazi ya hasara) kwa kutumia vigezo vilivyotolewa, na inaweza kusukumwa kwa mahesabu kwenye GPU, ikiwa inapatikana. Kuna kazi za kutofautisha mchoro huu wa mahesabu na kuhesabu derivatives, ambazo zinaweza kutumika kuboresha vigezo vya mfano.

**APIs za kiwango cha juu** huchukulia mitandao ya neural kama **mfululizo wa tabaka**, na hufanya ujenzi wa mitandao mingi ya neural kuwa rahisi zaidi. Kufundisha mfano kawaida kunahitaji kuandaa data na kisha kuita kazi ya `fit` kufanya kazi hiyo.

API ya kiwango cha juu hukuruhusu kujenga mitandao ya neural ya kawaida haraka sana bila kuwa na wasiwasi kuhusu maelezo mengi. Wakati huo huo, API ya kiwango cha chini inatoa udhibiti zaidi juu ya mchakato wa mafunzo, na hivyo hutumika sana katika utafiti, unaposhughulika na usanifu mpya wa mitandao ya neural.

Ni muhimu pia kuelewa kwamba unaweza kutumia APIs zote mbili pamoja, kwa mfano, unaweza kuunda usanifu wako wa tabaka la mtandao kwa kutumia API ya kiwango cha chini, na kisha kuitumia ndani ya mtandao mkubwa ulioundwa na kufundishwa kwa API ya kiwango cha juu. Au unaweza kufafanua mtandao kwa kutumia API ya kiwango cha juu kama mfululizo wa tabaka, na kisha kutumia mzunguko wako wa mafunzo wa kiwango cha chini kufanya uboreshaji. APIs zote mbili hutumia dhana za msingi sawa, na zimeundwa kufanya kazi vizuri pamoja.

## Kujifunza

Katika kozi hii, tunatoa maudhui mengi kwa PyTorch na TensorFlow. Unaweza kuchagua mfumo unaoupenda na kupitia tu daftari zinazohusiana. Ikiwa huna uhakika ni mfumo gani wa kuchagua, soma mijadala fulani mtandaoni kuhusu **PyTorch vs. TensorFlow**. Unaweza pia kuangalia mifumo yote miwili ili kupata uelewa bora.

Pale inapowezekana, tutatumia APIs za kiwango cha juu kwa urahisi. Hata hivyo, tunaamini ni muhimu kuelewa jinsi mitandao ya neural inavyofanya kazi kutoka mwanzo, hivyo mwanzoni tunaanza kwa kufanya kazi na API ya kiwango cha chini na tensors. Hata hivyo, ikiwa unataka kuanza haraka na hutaki kutumia muda mwingi kujifunza maelezo haya, unaweza kuruka hizo na kwenda moja kwa moja kwenye daftari za API ya kiwango cha juu.

## ✍️ Mazoezi: Mifumo

Endelea kujifunza katika daftari zifuatazo:

Low-Level API | [TensorFlow+Keras Notebook](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKerasTF.ipynb) | [PyTorch](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroPyTorch.ipynb)  
--------------|-------------------------------------|--------------------------------  
High-level API| [Keras](../../../../../lessons/3-NeuralNetworks/05-Frameworks/IntroKeras.ipynb) | *PyTorch Lightning*  

Baada ya kufahamu mifumo, hebu tukumbuke dhana ya overfitting.

# Overfitting

Overfitting ni dhana muhimu sana katika ujifunzaji wa mashine, na ni muhimu sana kuielewa vizuri!

Fikiria tatizo lifuatalo la kukadiria alama 5 (zinazowakilishwa na `x` kwenye grafu hapa chini):

![linear](../../../../../translated_images/overfit1.f24b71c6f652e59e6bed7245ffbeaecc3ba320e16e2221f6832b432052c4da43.sw.jpg) | ![overfit](../../../../../translated_images/overfit2.131f5800ae10ca5e41d12a411f5f705d9ee38b1b10916f284b787028dd55cc1c.sw.jpg)  
-------------------------|--------------------------  
**Mfano wa Linear, vigezo 2** | **Mfano wa Non-linear, vigezo 7**  
Makosa ya mafunzo = 5.3 | Makosa ya mafunzo = 0  
Makosa ya uthibitishaji = 5.1 | Makosa ya uthibitishaji = 20  

* Kushoto, tunaona makadirio mazuri ya mstari wa moja kwa moja. Kwa sababu idadi ya vigezo ni ya kutosha, mfano unapata wazo sahihi la usambazaji wa alama.  
* Kulia, mfano ni wenye nguvu kupita kiasi. Kwa sababu tuna alama 5 tu na mfano una vigezo 7, unaweza kurekebisha kwa njia ya kupita kwenye alama zote, na kufanya makosa ya mafunzo kuwa 0. Hata hivyo, hii inazuia mfano kuelewa muundo sahihi wa data, hivyo makosa ya uthibitishaji ni makubwa sana.  

Ni muhimu sana kupata usawa sahihi kati ya utajiri wa mfano (idadi ya vigezo) na idadi ya sampuli za mafunzo.

## Kwa nini overfitting hutokea

  * Data ya mafunzo haitoshi  
  * Mfano wenye nguvu kupita kiasi  
  * Kelele nyingi kwenye data ya ingizo  

## Jinsi ya kugundua overfitting

Kama unavyoona kutoka kwenye grafu hapo juu, overfitting inaweza kugunduliwa kwa makosa ya mafunzo ya chini sana, na makosa ya uthibitishaji ya juu. Kawaida wakati wa mafunzo tutaona makosa ya mafunzo na uthibitishaji yakianza kupungua, na kisha wakati fulani makosa ya uthibitishaji yanaweza kuacha kupungua na kuanza kuongezeka. Hii itakuwa ishara ya overfitting, na kiashiria kwamba tunapaswa labda kuacha mafunzo wakati huo (au angalau kuchukua snapshot ya mfano).

![overfitting](../../../../../translated_images/Overfitting.408ad91cd90b4371d0a81f4287e1409c359751adeb1ae450332af50e84f08c3e.sw.png)

## Jinsi ya kuzuia overfitting

Ikiwa unaona kwamba overfitting inatokea, unaweza kufanya mojawapo ya yafuatayo:

 * Ongeza kiasi cha data ya mafunzo  
 * Punguza ugumu wa mfano  
 * Tumia baadhi ya [mbinu za kudhibiti](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md), kama [Dropout](../../4-ComputerVision/08-TransferLearning/TrainingTricks.md#Dropout), ambayo tutazingatia baadaye.  

## Overfitting na Bias-Variance Tradeoff

Overfitting kwa kweli ni hali ya tatizo la jumla zaidi katika takwimu linaloitwa [Bias-Variance Tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff). Tukizingatia vyanzo vinavyowezekana vya makosa katika mfano wetu, tunaweza kuona aina mbili za makosa:

* **Makosa ya Bias** husababishwa na algorithimu yetu kushindwa kunasa uhusiano kati ya data ya mafunzo kwa usahihi. Inaweza kusababishwa na ukweli kwamba mfano wetu hauna nguvu ya kutosha (**underfitting**).  
* **Makosa ya Variance**, ambayo husababishwa na mfano kukadiria kelele kwenye data ya ingizo badala ya uhusiano wa maana (**overfitting**).  

Wakati wa mafunzo, makosa ya bias hupungua (kama mfano wetu unavyojifunza kukadiria data), na makosa ya variance huongezeka. Ni muhimu kuacha mafunzo - ama kwa mikono (tunapogundua overfitting) au kiotomatiki (kwa kuanzisha udhibiti) - ili kuzuia overfitting.

## Hitimisho

Katika somo hili, umejifunza tofauti kati ya APIs mbalimbali za mifumo miwili maarufu ya AI, TensorFlow na PyTorch. Zaidi ya hayo, umejifunza kuhusu mada muhimu sana, overfitting.

## 🚀 Changamoto

Katika daftari zinazofuatana, utapata 'kazi' chini; pitia daftari na ukamilishe kazi hizo.

## [Jaribio la baada ya somo](https://ff-quizzes.netlify.app/en/ai/quiz/10)

## Mapitio & Kujisomea

Fanya utafiti kuhusu mada zifuatazo:

- TensorFlow  
- PyTorch  
- Overfitting  

Jiulize maswali yafuatayo:

- Tofauti kati ya TensorFlow na PyTorch ni ipi?  
- Tofauti kati ya overfitting na underfitting ni ipi?  

## [Kazi](lab/README.md)

Katika maabara hii, unatakiwa kutatua matatizo mawili ya uainishaji kwa kutumia mitandao ya tabaka moja na tabaka nyingi kwa kutumia PyTorch au TensorFlow.

* [Maelekezo](lab/README.md)  
* [Daftari](../../../../../lessons/3-NeuralNetworks/05-Frameworks/lab/LabFrameworks.ipynb)  

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.