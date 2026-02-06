# Etikal at Responsableng AI

Malapit mo nang matapos ang kursong ito, at sana sa puntong ito ay malinaw na sa iyo na ang AI ay nakabatay sa iba't ibang pormal na matematikal na pamamaraan na nagbibigay-daan sa atin upang matuklasan ang mga relasyon sa datos at sanayin ang mga modelo upang gayahin ang ilang aspeto ng kilos ng tao. Sa kasalukuyang panahon, itinuturing natin ang AI bilang isang napakalakas na kasangkapan upang kumuha ng mga pattern mula sa datos, at gamitin ang mga pattern na ito upang lutasin ang mga bagong problema.

## [Pre-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Gayunpaman, sa science fiction, madalas nating nakikita ang mga kuwento kung saan ang AI ay nagdudulot ng panganib sa sangkatauhan. Karaniwan, ang mga kuwentong ito ay nakasentro sa isang uri ng pag-aalsa ng AI, kung saan ang AI ay nagpasya na kalabanin ang mga tao. Ipinapahiwatig nito na ang AI ay may emosyon o kaya nitong gumawa ng mga desisyon na hindi inaasahan ng mga tagapagpaunlad nito.

Ang uri ng AI na natutunan natin sa kursong ito ay walang iba kundi malalaking matrix arithmetic. Isa itong napakalakas na kasangkapan upang tulungan tayong lutasin ang ating mga problema, at tulad ng anumang makapangyarihang kasangkapan - maaari itong magamit para sa mabuti at masamang layunin. Mahalagang tandaan na maaari itong *magamit nang mali*.

## Mga Prinsipyo ng Responsableng AI

Upang maiwasan ang aksidental o sinadyang maling paggamit ng AI, ipinahayag ng Microsoft ang mahahalagang [Prinsipyo ng Responsableng AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Ang mga sumusunod na konsepto ang pundasyon ng mga prinsipyong ito:

* **Pagiging Makatarungan** ay nauugnay sa mahalagang problema ng *bias ng modelo*, na maaaring sanhi ng paggamit ng bias na datos para sa pagsasanay. Halimbawa, kapag sinusubukan nating hulaan ang posibilidad ng pagkakaroon ng trabaho bilang software developer para sa isang tao, malamang na mas paboran ng modelo ang mga lalaki - dahil ang dataset para sa pagsasanay ay malamang na bias patungo sa mga lalaki. Kailangan nating maingat na balansehin ang datos para sa pagsasanay at suriin ang modelo upang maiwasan ang bias, at tiyakin na isinasaalang-alang ng modelo ang mas may kaugnayang mga tampok.
* **Kahusayan at Kaligtasan**. Sa kanilang likas na katangian, maaaring magkamali ang mga modelo ng AI. Ang neural network ay nagbabalik ng mga probabilidad, at kailangan nating isaalang-alang ito kapag gumagawa ng mga desisyon. Ang bawat modelo ay may ilang precision at recall, at kailangan nating maunawaan ito upang maiwasan ang pinsala na maaaring idulot ng maling payo.
* **Pagkapribado at Seguridad** ay may ilang implikasyon na partikular sa AI. Halimbawa, kapag ginamit natin ang ilang datos para sa pagsasanay ng modelo, ang datos na ito ay nagiging "integrado" sa modelo. Sa isang banda, pinapataas nito ang seguridad at pagkapribado, ngunit sa kabilang banda - kailangan nating tandaan kung aling datos ang ginamit sa pagsasanay ng modelo.
* **Pagiging Inklusibo** ay nangangahulugan na hindi natin itinatayo ang AI upang palitan ang mga tao, kundi upang palakasin ang mga tao at gawing mas malikhain ang ating trabaho. Kaugnay din ito sa pagiging makatarungan, dahil kapag nakikitungo sa mga komunidad na hindi gaanong kinakatawan, karamihan sa mga dataset na kinokolekta natin ay malamang na bias, at kailangan nating tiyakin na ang mga komunidad na ito ay kasama at tamang pinangangasiwaan ng AI.
* **Pagiging Transparent**. Kasama rito ang pagtiyak na palagi tayong malinaw tungkol sa paggamit ng AI. Gayundin, hangga't maaari, nais nating gumamit ng mga sistema ng AI na *maipapaliwanag*.
* **Pananagutan**. Kapag ang mga modelo ng AI ay gumagawa ng ilang desisyon, hindi palaging malinaw kung sino ang responsable sa mga desisyong iyon. Kailangan nating tiyakin na nauunawaan natin kung saan nakasalalay ang responsibilidad ng mga desisyon ng AI. Sa karamihan ng mga kaso, nais nating isama ang mga tao sa proseso ng paggawa ng mahahalagang desisyon, upang ang mga aktwal na tao ang managot.

## Mga Kasangkapan para sa Responsableng AI

Ang Microsoft ay bumuo ng [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) na naglalaman ng hanay ng mga kasangkapan:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard na kinabibilangan ng:

   - EconML - kasangkapan para sa Causal Analysis, na nakatuon sa mga tanong na "paano kung"
   - DiCE - kasangkapan para sa Counterfactual Analysis na nagbibigay-daan sa iyo upang makita kung aling mga tampok ang kailangang baguhin upang maapektuhan ang desisyon ng modelo

Para sa karagdagang impormasyon tungkol sa Etika ng AI, bisitahin ang [araling ito](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) sa Machine Learning Curriculum na may kasamang mga gawain.

## Review at Pag-aaral sa Sarili

Kunin ang [Learn Path](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) upang matuto pa tungkol sa responsableng AI.

## [Post-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.