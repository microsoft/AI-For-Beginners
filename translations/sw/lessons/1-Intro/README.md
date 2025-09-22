<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-25T20:52:37+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "sw"
}
-->
> Picha na [Dmitry Soshnikov](http://soshnikov.com)

Kadri muda ulivyopita, rasilimali za kompyuta zimekuwa nafuu, na data zaidi imepatikana, hivyo mbinu za mitandao ya neva zimeanza kuonyesha utendaji mzuri katika kushindana na binadamu katika maeneo mengi, kama vile kuona kwa kompyuta au kuelewa sauti. Katika muongo uliopita, neno Akili Bandia limekuwa likitumika zaidi kama jina la mitandao ya neva, kwa sababu mafanikio mengi ya AI tunayoyasikia yanatokana na teknolojia hii.

Tunaweza kuona jinsi mbinu zilivyobadilika, kwa mfano, katika kuunda programu ya kompyuta inayocheza chess:

* Programu za chess za awali zilitegemea utafutaji – programu ilijaribu kwa makusudi kutathmini hatua zinazowezekana za mpinzani kwa idadi fulani ya hatua zijazo, na kuchagua hatua bora kulingana na nafasi bora inayoweza kufikiwa katika hatua chache. Hii ilisababisha maendeleo ya [algorithimu ya alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).
* Mikakati ya utafutaji hufanya kazi vizuri mwishoni mwa mchezo, ambapo nafasi ya utafutaji imepunguzwa na idadi ndogo ya hatua zinazowezekana. Hata hivyo, mwanzoni mwa mchezo, nafasi ya utafutaji ni kubwa, na algorithimu inaweza kuboreshwa kwa kujifunza kutoka kwa mechi zilizopo kati ya wachezaji wa binadamu. Majaribio ya baadaye yalitumia [case-based reasoning](https://en.wikipedia.org/wiki/Case-based_reasoning), ambapo programu ilitafuta kesi katika hifadhidata zinazofanana sana na nafasi ya sasa katika mchezo.
* Programu za kisasa zinazoshinda wachezaji wa binadamu zinategemea mitandao ya neva na [ujifunzaji wa kuimarisha](https://en.wikipedia.org/wiki/Reinforcement_learning), ambapo programu hujifunza kucheza kwa kucheza muda mrefu dhidi ya yenyewe na kujifunza kutokana na makosa yake – kama vile binadamu wanavyofanya wanapojifunza kucheza chess. Hata hivyo, programu ya kompyuta inaweza kucheza michezo mingi zaidi kwa muda mfupi, na hivyo kujifunza haraka zaidi.

✅ Fanya utafiti kidogo kuhusu michezo mingine ambayo AI imecheza.

Vivyo hivyo, tunaweza kuona jinsi mbinu za kuunda programu za "kuongea" (ambazo zinaweza kupita mtihani wa Turing) zilivyobadilika:

* Programu za awali za aina hii kama [Eliza](https://en.wikipedia.org/wiki/ELIZA), zilitegemea sheria rahisi za kisarufi na kuunda upya sentensi ya pembejeo kuwa swali.
* Wasaidizi wa kisasa, kama Cortana, Siri au Google Assistant ni mifumo mseto inayotumia mitandao ya neva kubadilisha sauti kuwa maandishi na kutambua nia yetu, kisha kutumia baadhi ya mantiki au algorithimu za wazi kutekeleza vitendo vinavyohitajika.
* Katika siku zijazo, tunaweza kutarajia mfano kamili wa msingi wa neva kushughulikia mazungumzo yenyewe. Familia ya mitandao ya neva ya hivi karibuni kama GPT na [Turing-NLG](https://turing.microsoft.com/) inaonyesha mafanikio makubwa katika hili.

> Picha na Dmitry Soshnikov, [picha](https://unsplash.com/photos/r8LmVbUKgns) na [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Utafiti wa Hivi Karibuni wa AI

Ukuaji mkubwa wa hivi karibuni katika utafiti wa mitandao ya neva ulianza karibu mwaka 2010, wakati seti kubwa za data za umma zilipoanza kupatikana. Mkusanyiko mkubwa wa picha unaoitwa [ImageNet](https://en.wikipedia.org/wiki/ImageNet), ambao una takriban picha milioni 14 zilizo na maelezo, ulizaa [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![Usahihi wa ILSVRC](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Picha na [Dmitry Soshnikov](http://soshnikov.com)

Mnamo 2012, [Mitandao ya Neva ya Convolutional](../4-ComputerVision/07-ConvNets/README.md) ilitumiwa kwa mara ya kwanza katika uainishaji wa picha, jambo ambalo lilisababisha kupungua kwa makosa ya uainishaji (kutoka karibu 30% hadi 16.4%). Mnamo 2015, usanifu wa ResNet kutoka Microsoft Research [ulifanikisha usahihi wa kiwango cha binadamu](https://doi.org/10.1109/ICCV.2015.123).

Tangu wakati huo, Mitandao ya Neva imeonyesha mafanikio makubwa katika kazi nyingi:

---

Mwaka | Usawa wa Binadamu ulifanikishwa
-----|--------
2015 | [Uainishaji wa Picha](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Utambuzi wa Hotuba ya Mazungumzo](https://arxiv.org/abs/1610.05256)
2018 | [Tafsiri ya Mashine ya Kiotomatiki](https://arxiv.org/abs/1803.05567) (Kutoka Kichina hadi Kiingereza)
2020 | [Uwekaji Maelezo ya Picha](https://arxiv.org/abs/2009.13682)

Katika miaka michache iliyopita tumeshuhudia mafanikio makubwa na mifano mikubwa ya lugha, kama BERT na GPT-3. Hii ilitokea hasa kwa sababu kuna data nyingi za maandishi ya jumla zinazopatikana ambazo zinaturuhusu kufundisha mifano ili kunasa muundo na maana ya maandishi, kuifundisha awali kwenye mkusanyiko wa maandishi ya jumla, na kisha kuiboresha kwa kazi maalum zaidi. Tutajifunza zaidi kuhusu [Usindikaji wa Lugha Asilia](../5-NLP/README.md) baadaye katika kozi hii.

## 🚀 Changamoto

Fanya ziara ya mtandao ili kubaini wapi, kwa maoni yako, AI inatumiwa kwa ufanisi zaidi. Je, ni katika programu ya Ramani, huduma ya hotuba-kwa-maandishi, au mchezo wa video? Tafiti jinsi mfumo ulivyojengwa.

## [Maswali ya Baada ya Somo](https://ff-quizzes.netlify.app/en/ai/quiz/2)

## Mapitio na Kujisomea

Pitia historia ya AI na ML kwa kusoma [somo hili](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Chukua kipengele kutoka kwenye sketchnote mwanzoni mwa somo hilo au hili na kifanyie utafiti kwa kina ili kuelewa muktadha wa kitamaduni unaoathiri mageuzi yake.

**Kazi**: [Game Jam](assignment.md)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.